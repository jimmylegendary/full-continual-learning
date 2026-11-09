"""Small analytic and reproducibility checks for the numerical probe."""
import json
from pathlib import Path

import numpy as np

from probe import Prior, posterior, single_run


base = Path(__file__).parent
results = json.loads((base / "results.json").read_text())
rng = np.random.default_rng(831)
n, k, d = 5, 4, 7
x = rng.normal(size=(n, k, d))
y = rng.normal(size=(n, k))
matrix = rng.normal(size=(d, d))
covariance = matrix @ matrix.T + 0.2 * np.eye(d)
noise = 0.13
prediction, probability = posterior(Prior(covariance[None], np.ones(1), noise), x, y)
reference = np.stack([
    np.linalg.solve(np.linalg.inv(covariance) + xx.T @ xx / noise, xx.T @ yy / noise)
    for xx, yy in zip(x, y)
])
primal_max_error = float(np.max(np.abs(reference - prediction)))
assert primal_max_error < 1e-10
duplicated, routing = posterior(Prior(np.stack([covariance, covariance]),
                                     np.array([0.3, 0.7]), noise), x, y)
duplicate_max_error = float(np.max(np.abs(duplicated - prediction)))
assert duplicate_max_error < 1e-10
assert np.max(np.abs(routing - np.array([0.3, 0.7]))) < 1e-10

reproducibility = {}
for mode in results["config"]["modes"]:
    seed = results["config"]["seeds"][0]
    rerun = single_run(seed, mode, results["config"])
    original = next(r for r in results["runs"] if r["mode"] == mode and r["seed"] == seed)
    assert rerun == original
    reproducibility[mode] = {"seed": seed, "all_per_task_scores_and_tuning_results_exactly_equal": True}

checks = {
    "posterior_vs_independent_primal_precision_solution_max_abs_error": primal_max_error,
    "identical_mixture_components_reduce_to_single_prior_max_abs_error": duplicate_max_error,
    "identical_component_responsibilities_equal_prior_probabilities": True,
    "deterministic_rerun": reproducibility,
    "scope": "Numerical identities and deterministic replay only; not evidence for general schema learning.",
}
(base / "verification.json").write_text(json.dumps(checks, indent=2))
print(json.dumps(checks, indent=2))
