#!/usr/bin/env python3
"""Phase-0 learned continuous-prior probe, not a Titans/HOPE reproduction.

Learning gets only task-indexed (X, y) experience. True subspaces, task weights,
and family labels live in the generator/evaluator and are never inputs to fit.
Hyperparameters are selected on independent calibration tasks, using independent
observed query outcomes. Final task truths are used only for scoring/oracles.
"""
from __future__ import annotations

import argparse
import json
import platform
import time
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import scipy
from scipy.special import logsumexp
from scipy.stats import t as student_t


@dataclass
class Experience:
    x: np.ndarray
    y: np.ndarray


@dataclass
class EvalTruth:
    w: np.ndarray
    family: np.ndarray


@dataclass
class Prior:
    covariances: np.ndarray
    probabilities: np.ndarray
    noise_variance: float


def orthonormal(rng, d, r):
    return np.linalg.qr(rng.normal(size=(d, r)))[0][:, :r]


def make_tasks(rng, n, n_obs, d, rank, true_bases, noise_sd, mode):
    # Ground-truth quantities are returned in a separate evaluator-only object.
    if mode == "structured":
        family = rng.integers(0, len(true_bases), size=n)
        coefficients = rng.normal(size=(n, rank)) / np.sqrt(rank)
        w = np.einsum("ndr,nr->nd", true_bases[family], coefficients)
    else:
        family = np.full(n, -1, dtype=int)
        w = rng.normal(size=(n, d)) / np.sqrt(d)
    x = rng.normal(size=(n, n_obs, d))
    y = np.einsum("nkd,nd->nk", x, w) + noise_sd * rng.normal(size=(n, n_obs))
    return Experience(x, y), EvalTruth(w, family)


def ols_experience_estimates(experience):
    x, y = experience.x, experience.y
    gram = np.einsum("nkd,nke->nde", x, x)
    rhs = np.einsum("nkd,nk->nd", x, y)
    w_hat = np.linalg.solve(gram, rhs[..., None])[..., 0]
    residual = y - np.einsum("nkd,nd->nk", x, w_hat)
    d = x.shape[-1]
    sigma2 = np.sum(residual * residual, axis=1) / (x.shape[1] - d)
    estimation_cov = sigma2[:, None, None] * np.linalg.inv(gram)
    return w_hat, estimation_cov, float(np.mean(sigma2))


def positive_covariance(matrix, rank=None, floor=1e-10):
    values, vectors = np.linalg.eigh((matrix + matrix.T) / 2)
    values = np.maximum(values, 0.0)
    if rank is not None:
        values[:-rank] = 0.0
    return (vectors * np.maximum(values, floor)) @ vectors.T


def covariance_from_subset(weights, estimation_cov, selected, rank=None):
    w = weights[selected]
    debiased = w.T @ w / len(w) - np.mean(estimation_cov[selected], axis=0)
    return positive_covariance(debiased, rank=rank)


def fit_unlabelled_subspaces(weights, estimation_cov, count, rank, rng,
                            restarts=12, max_steps=60):
    """Fixed-K/rank k-subspaces. No generator labels or true bases are supplied.

    Clustering minimizes residual energy of noisy OLS estimates. Noise-corrected
    second moments are used to fit continuous Gaussian priors after clustering.
    This is a deliberately small, explicit estimator, not arbitrary discovery.
    """
    n, d = weights.shape
    outer = np.einsum("ni,nj->nij", weights, weights)
    best = None
    for _ in range(restarts):
        assignment = rng.integers(count, size=n)
        for step in range(max_steps):
            projectors = []
            for component in range(count):
                selected = assignment == component
                if np.sum(selected) < rank + 2:
                    selected = np.zeros(n, dtype=bool)
                    selected[rng.choice(n, size=max(rank + 2, n // count), replace=False)] = True
                moment = np.mean(outer[selected], axis=0)
                _, vectors = np.linalg.eigh(moment)
                basis = vectors[:, -rank:]
                projectors.append(basis @ basis.T)
            captured = np.einsum("ni,cij,nj->nc", weights,
                                 np.asarray(projectors), weights)
            new_assignment = np.argmax(captured, axis=1)
            if np.array_equal(assignment, new_assignment):
                break
            assignment = new_assignment
        if any(np.sum(assignment == c) < rank + 2 for c in range(count)):
            continue
        objective = float(np.sum(weights * weights) - np.sum(np.max(captured, axis=1)))
        if best is None or objective < best[0]:
            best = (objective, assignment.copy(), step + 1)
    if best is None:
        raise RuntimeError("All k-subspace initializations failed.")
    objective, assignment, steps = best
    covariances = np.asarray([
        covariance_from_subset(weights, estimation_cov, assignment == c, rank)
        for c in range(count)
    ])
    probabilities = np.asarray([np.mean(assignment == c) for c in range(count)])
    return covariances, probabilities, {"training_residual_objective": objective,
        "cluster_sizes": [int(np.sum(assignment == c)) for c in range(count)],
        "converged_iteration_of_best_restart": steps, "restarts": restarts}


def posterior(prior, x, y):
    """Bayesian mixture posterior from support observations only.

    p(c|X,y) is proportional to p(c) N(y; 0, X C_c X^T + sigma^2 I).
    The output is the mixture posterior mean of the task's coefficient vector.
    """
    n, k, d = x.shape
    if k == 0:
        return np.zeros((n, d)), np.broadcast_to(prior.probabilities, (n, len(prior.probabilities)))
    means, log_weights = [], []
    for covariance, probability in zip(prior.covariances, prior.probabilities):
        xc = x @ covariance
        kernel = xc @ np.swapaxes(x, 1, 2)
        kernel += prior.noise_variance * np.eye(k)[None]
        alpha = np.linalg.solve(kernel, y[..., None])[..., 0]
        means.append(np.einsum("nkd,nk->nd", xc, alpha))
        signs, logdet = np.linalg.slogdet(kernel)
        if not np.all(signs > 0):
            raise ArithmeticError("Nonpositive predictive covariance")
        log_weights.append(np.log(probability) - 0.5 * (
            logdet + np.sum(y * alpha, axis=1) + k * np.log(2 * np.pi)))
    log_weights = np.stack(log_weights, axis=1)
    probabilities = np.exp(log_weights - logsumexp(log_weights, axis=1, keepdims=True))
    return np.einsum("nc,cnd->nd", probabilities, np.asarray(means)), probabilities


def tune_prior(base_covariances, probabilities, sigma2, scale_reference,
               calibration, query, shots, shrinkages, scales):
    """Only calibration observation pairs are used. No latent truth is read."""
    d = calibration.x.shape[-1]
    candidates = []
    best = None
    for shrink in shrinkages:
        for scale in scales:
            covariances = scale * ((1 - shrink) * base_covariances
                + shrink * scale_reference * np.eye(d)[None])
            prior = Prior(covariances, probabilities, sigma2)
            per_shot_mse = []
            for k in shots:
                if k == 0:
                    continue
                estimate, _ = posterior(prior, calibration.x[:, :k], calibration.y[:, :k])
                predicted = np.einsum("nqd,nd->nq", query.x, estimate)
                per_shot_mse.append(float(np.mean((predicted - query.y) ** 2)))
            objective = float(np.mean(per_shot_mse))
            record = {"shrinkage": shrink, "scale": scale,
                      "calibration_observed_query_mse": objective}
            candidates.append(record)
            if best is None or objective < best[0]:
                best = (objective, prior, record)
    return best[1], {"selected": best[2], "all_candidates": candidates}


def score_prior(prior, experience, truth, shots, true_noise_variance):
    result = {}
    for k in shots:
        estimate, routing = posterior(prior, experience.x[:, :k], experience.y[:, :k])
        squared_error = np.sum((estimate - truth.w) ** 2, axis=1)
        # For independent x_query~N(0,I), this is exact expected prediction MSE
        # per held-out task, without additional finite-query Monte Carlo noise.
        result[str(k)] = {
            "signal_mse": float(np.mean(squared_error)),
            "observed_mse": float(np.mean(squared_error) + true_noise_variance),
            "routing_entropy_nats": float(np.mean(-np.sum(
                routing * np.log(np.maximum(routing, 1e-300)), axis=1))),
            "per_task_signal_mse": squared_error.tolist(),
        }
    return result


def single_run(seed, mode, config):
    rng = np.random.default_rng(seed)
    d, rank, count = config["ambient_dimension"], config["rank"], config["components"]
    bases = np.stack([orthonormal(rng, d, rank) for _ in range(count)])
    noise_sd = config["noise_sd"]
    train, _ = make_tasks(rng, config["training_tasks"], config["training_observations"],
                         d, rank, bases, noise_sd, mode)
    max_shots = max(config["shots"])
    calibration_all, _ = make_tasks(rng, config["calibration_tasks"],
        max_shots + config["calibration_query_observations"], d, rank, bases, noise_sd, mode)
    calibration = Experience(calibration_all.x[:, :max_shots], calibration_all.y[:, :max_shots])
    query = Experience(calibration_all.x[:, max_shots:], calibration_all.y[:, max_shots:])
    test, test_truth = make_tasks(rng, config["test_tasks"], max_shots,
                                 d, rank, bases, noise_sd, mode)
    w_hat, estimation_cov, sigma2 = ols_experience_estimates(train)
    full_cov = covariance_from_subset(w_hat, estimation_cov, np.ones(len(w_hat), dtype=bool))
    tau = float(np.trace(full_cov) / d)
    cluster_cov, cluster_probs, fit_info = fit_unlabelled_subspaces(
        w_hat, estimation_cov, count, rank, rng)
    shots = config["shots"]
    scales = [0.25, 0.5, 1.0, 2.0, 4.0]
    shrinkages = [0.0, 0.05, 0.2, 0.5, 1.0]
    iso, iso_tune = tune_prior(tau * np.eye(d)[None], np.ones(1), sigma2, tau,
        calibration, query, shots, [0.0], scales)
    pooled, pooled_tune = tune_prior(full_cov[None], np.ones(1), sigma2, tau,
        calibration, query, shots, shrinkages, scales)
    mixture, mixture_tune = tune_prior(cluster_cov, cluster_probs, sigma2, tau,
        calibration, query, shots, shrinkages, scales)
    # Counterfactual ablation: keep mixture spectra and selected hyperparameters,
    # rotate its learned directions independently of the data, without retuning.
    rotation = orthonormal(rng, d, d)
    rotated = Prior(np.stack([rotation @ c @ rotation.T for c in mixture.covariances]),
                    mixture.probabilities.copy(), mixture.noise_variance)
    models = {"isotropic_ridge": iso, "learned_pooled_covariance": pooled,
              "learned_mixture": mixture, "rotated_mixture_ablation": rotated}
    if mode == "structured":
        true_covariances = np.einsum("cdr,cer->cde", bases, bases) / rank
        models["oracle_mixture_unknown_context"] = Prior(true_covariances,
                                                    np.ones(count) / count, noise_sd ** 2)
    else:
        true_covariances = np.eye(d)[None] / d
        models["oracle_isotropic"] = Prior(true_covariances, np.ones(1), noise_sd ** 2)
    scores = {name: score_prior(prior, test, test_truth, shots, noise_sd ** 2)
              for name, prior in models.items()}
    if mode == "structured":
        oracle_scores = {}
        for k in shots:
            estimates = np.empty_like(test_truth.w)
            for c in range(count):
                selected = test_truth.family == c
                # Only this explicitly named oracle may read the family label.
                prior = Prior(true_covariances[c:c+1], np.ones(1), noise_sd ** 2)
                estimates[selected], _ = posterior(prior, test.x[selected, :k], test.y[selected, :k])
            error = np.sum((estimates - test_truth.w) ** 2, axis=1)
            oracle_scores[str(k)] = {"signal_mse": float(np.mean(error)),
                "observed_mse": float(np.mean(error) + noise_sd ** 2),
                "per_task_signal_mse": error.tolist()}
        scores["oracle_known_context"] = oracle_scores
    return {"seed": seed, "mode": mode, "estimated_noise_variance": sigma2,
            "mean_test_signal_variance": float(np.mean(np.sum(test_truth.w ** 2, axis=1))),
            "fit_diagnostics": fit_info,
            "hyperparameter_selection": {"isotropic_ridge": iso_tune,
                "learned_pooled_covariance": pooled_tune, "learned_mixture": mixture_tune},
            "scores": scores}


def interval(values):
    values = np.asarray(values, dtype=float)
    mean = float(np.mean(values))
    sd = float(np.std(values, ddof=1)) if len(values) > 1 else 0.0
    radius = float(student_t.ppf(0.975, len(values) - 1) * sd / np.sqrt(len(values))) if len(values) > 1 else 0.0
    return {"mean": mean, "sd_across_seeds": sd,
            "descriptive_95pct_t_interval": [mean - radius, mean + radius]}


def summarize(runs, config):
    summary = {}
    for mode in config["modes"]:
        selected = [r for r in runs if r["mode"] == mode]
        models = list(selected[0]["scores"])
        by_model = {}
        for model in models:
            curve = {str(k): interval([r["scores"][model][str(k)]["signal_mse"] for r in selected])
                     for k in config["shots"]}
            auc = interval([np.mean([r["scores"][model][str(k)]["signal_mse"]
                         for k in config["shots"] if k > 0]) for r in selected])
            threshold_shots = [k for k in config["shots"]
                               if curve[str(k)]["mean"] <= config["risk_threshold"]]
            by_model[model] = {"signal_mse_curve": curve,
                "mean_risk_over_nonzero_shot_grid": auc,
                "first_grid_shot_at_or_below_risk_threshold": threshold_shots[0] if threshold_shots else None}
        paired = {}
        for baseline in ["isotropic_ridge", "learned_pooled_covariance"]:
            paired[baseline] = {str(k): interval([
                r["scores"]["learned_mixture"][str(k)]["signal_mse"]
                - r["scores"][baseline][str(k)]["signal_mse"] for r in selected])
                for k in config["shots"]}
        summary[mode] = {"models": by_model,
            "paired_delta_learned_mixture_minus_baseline": paired,
            "mixture_selected_hyperparameters_by_seed": [
                {"seed": r["seed"], **r["hyperparameter_selection"]["learned_mixture"]["selected"]}
                for r in selected]}
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    parser.add_argument("--seeds", type=int, default=6)
    args = parser.parse_args()
    config = {"ambient_dimension": 24, "rank": 3, "components": 2,
        "training_tasks": 240, "training_observations": 64,
        "calibration_tasks": 64, "calibration_query_observations": 64,
        "test_tasks": 128, "shots": [0, 1, 2, 3, 4, 6, 8, 12, 16],
        "noise_sd": 0.15, "risk_threshold": 0.10,
        "seeds": list(range(202611030, 202611030 + args.seeds)),
        "modes": ["structured", "no_shared_structure"]}
    start = time.perf_counter()
    runs = []
    for mode in config["modes"]:
        for seed in config["seeds"]:
            run_start = time.perf_counter()
            runs.append(single_run(seed, mode, config))
            print(f"{mode} seed={seed} completed in {time.perf_counter()-run_start:.2f}s", flush=True)
    payload = {"experiment": "Melete SBL phase-0 continuous-prior sanity check",
        "claim_scope": "Synthetic Bayesian linear prediction only; no actual Titans/HOPE, no general schema discovery, no LLM speed benchmark.",
        "config": config,
        "environment": {"python": platform.python_version(), "numpy": np.__version__,
                        "scipy": scipy.__version__, "platform": platform.platform()},
        "runtime_seconds": time.perf_counter() - start,
        "summary": summarize(runs, config), "runs": runs}
    args.output.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Saved {args.output} ({args.output.stat().st_size} bytes)", flush=True)


if __name__ == "__main__":
    main()
