# Phase-0: learned continuous-prior sanity check

**ARCHIVE — 최초 실행 2026-11-03.** Library에 실제 존재하는 `Melete_SBL_Research_and_Phase0_20261103.zip`에서 코드와 결과를 확보했다. 이것은 **Bayesian linear prediction의 공유 연속 prior 실험**이다. Titans/HOPE, neural network training, 통합 System ONE, 자연어 schema, Sleep 또는 LLM latency의 PoC가 아니다.

## 1. 이관한 것

- 원본 `probe.py`, `verify.py`, pinned `requirements.txt`.
- 원래 numerical verification을 이름을 구분해 보존한 `verification.original.json`.
- 원래 결과의 핵심 표와 설명을 아래에 보존.
- 원본 전체 ZIP, 2.9 MB per-task `results.json`, 상세 README/plan은 출처 해시로 추적한다. 큰 raw JSON은 이 초기 Git tree에 수동 복사하지 않고 아래 명령으로 재생성할 수 있다. 원본 전체 파일은 이 게시 작업의 별도 다운로드 백업에도 포함한다.

새 실행의 `results.json`, `verification.json`은 원래 결과와 다른 파일이며 원본 검증을 덮어쓰지 않는다. 재생성 결과의 byte identity는 환경·runtime 필드 때문에 자동 보장되지 않는다. 현재 게시 검사는 [VALIDATION](../../VALIDATION.md)에 별도 기록한다.

## 2. 재현

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows: .venv\Scripts\activate
python -m pip install -r experiments/phase0/requirements.txt
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/phase0/probe.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiments/phase0/verify.py
```

환경변수 prefix는 POSIX shell 예시다. Windows에서는 해당 환경변수를 먼저 설정하거나 생략할 수 있다. `verify.py`는 생성된 `results.json`에 대해 두 수치 identity와 각 환경의 첫 seed deterministic rerun을 검사한다. 역사적 결과와의 독립 비교는 별도 절차다. `--seeds 1`은 빠른 실행 확인이며 원래 6-seed 실험을 대신하지 않는다.

역사적 환경 기록: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0. 원래 전체 실행 시간 약4.13초는 그 환경의 실행 기록일 뿐 추론 성능 benchmark가 아니다.

## 3. 데이터와 learner/evaluator 경계

구조 환경:

    x ~ Normal(0,I_24)
    c ∈ {0,1}, a ~ Normal(0,I_3/3)
    w = U_c a, y = xᵀw + noise, noise_sd=0.15

U_c는 두 개의 3차원 직교기저다. 각 기저 내부는 직교하지만 서로 다른 기저가 상호 직교하도록 강제한 것은 아니다. 비구조 control은 w~Normal(0,I_24/24).

- seed당 train 240 tasks ×64 observations.
- calibration 64 tasks, 최대16 support+64 independent query observations.
- test 128 independent tasks.
- seeds 202611030~202611035, 총6.
- shots [0,1,2,3,4,6,8,12,16].

Learner에는 task-indexed (X,y)만 전달한다. true U, task w, family labels는 generator/evaluator 전용이다. 단 **component count=2, rank=3, task boundary를 제공**한다. 따라서 임의 schema 수의 자율 발견이 아니다.

각 train task를 OLS로 추정하고 noise-corrected covariance를 구성한다. K-subspaces는12 restarts/최대60 steps로 unlabeled 방향을 학습한다. Calibration으로 scale [.25,.5,1,2,4], shrinkage [0,.05,.2,.5,1]을 선택한다. test를 보고 hyperparameter를 바꾸지 않는다.

## 4. 비교군

- `isotropic_ridge`: 방향 구조가 없는 calibrated prior.
- `learned_pooled_covariance`: 모든 과제에서 하나의 covariance.
- `learned_mixture`: 학습한 두 covariance와 support likelihood routing.
- `rotated_mixture_ablation`: 같은 스펙트럼·hyperparameter를 유지하고 방향만 회전, retuning 없음.
- `oracle_mixture_unknown_context`: true U 사용, 현재 family는 모름.
- `oracle_known_context`: true U와 family 사용. 명시적인 upper-bound diagnostic.
- 비구조 환경의 `oracle_isotropic`.

## 5. 역사적 결과

아래는 새로운 noiseless query signal의 기대 MSE다. x~N(0,I)이므로 task별 ||w_hat−w||²를 계산한다. Accuracy나 normalized MSE가 아니다. 관측 y 기준 MSE에는0.0225의 noise variance가 더해진다.

| 새 관측 수 | Isotropic | Pooled | Learned mixture | Rotated | Oracle unknown | Oracle known |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | .98305 | .86714 | .84819 | 1.20540 | .84578 | .72312 |
| 2 | .94363 | .69861 | .59915 | 1.68833 | .59664 | .42269 |
| 3 | .90247 | .54591 | .31381 | 2.62262 | .31180 | .17408 |
| 4 | .86104 | .39951 | .14185 | 2.93880 | .14285 | .08247 |
| 6 | .78095 | .15469 | .04062 | 2.03314 | .04086 | .03160 |
| 8 | .69790 | .06867 | .02025 | 1.64370 | .01993 | .01748 |
| 12 | .53645 | .02542 | .00930 | 1.27531 | .00895 | .00877 |
| 16 | .38592 | .01537 | .00625 | 1.12936 | .00591 | .00589 |

평균 signal MSE≤0.1이 된 최초 **측정 grid**: pooled8, learned mixture6, oracle known4. Isotropic은16 이하에서 도달하지 않음. 연속적인 실제 minimum을 추정한 것이 아니다.

Mixture−pooled의 seed-paired 차이:

- 4shot −0.257663, descriptive95% t interval [−0.280881,−0.234445].
- 8shot −0.048420, interval [−0.052866,−0.043973].

이 구간은6개 seed의 기술적 요약이고 보편적 성능·모든 초기화의 분포 보장이 아니다. 같은 task의 반복 query를 독립 sample로 늘리지 않는다.

## 6. Negative control

공유구조가 없는 train/calibration/test 환경에서 학습 prior는 calibration을 통해 모두 shrinkage1의 isotropic prior로 돌아갔다. 대표 signal MSE4shot .86201, 8shot .69990,16shot .38462. 해당 조건의 oracle는 .86190/.69962/.38352.

이것은 **calibration도 비구조 환경을 관측한 경우**다. 구조를 배운 뒤 갑자기 OOD가 들어왔을 때 자율적으로 감지·회복했다는 증거가 아니다. Wrong-direction ablation은 성능을 크게 악화시키며 잘못 적용한 prior의 위험을 보여주지만 자동 복구는 구현하지 않았다.

## 7. 주장할 수 있는 것과 없는 것

가능한 주장: 공유 저차원 구조가 존재하는 제한된 환경에서 그 prior를 학습하면 새 task의 적은 관측으로 예측하는 효율을 높일 수 있다.

아직 없는 것: unknown K/rank discovery, natural-language semantics, online ABA, schema split/merge, neural memory update, HOPE/Titans integration, CMS/Sleep, variable-depth controller, actual latency improvement.

새 task의 few-shot은 **과거240×64 관측으로 prior를 얻은 뒤**의 적응이다. 이 선행 비용을 생략해서 one-shot intelligence라고 부르지 않는다.

## 8. 원본 식별

ZIP SHA-256: `a0581ee2cc86964fa7612b24d03bfe493660a71863d1c4f09825d9b91c641e39`

probe.py SHA-256: `372ff6efdd5e5226e6067a3d9e86c2329d743a196ed306dc295d635a4215abc2`

results.json SHA-256: `b55365218445817ec032cf5bfc63bc2805e46f2c771c77e12f7d5a52d85b0cb5`

verification.json SHA-256: `bff8f9ffe97fe0efb2bd08e3ba590d712da05c6eac2b88f28bb1a5b084c51284`

원래 `MELETE_RESEARCH_PLAN.md`에는 사용자 통합 모델 정정 이전의 phase도 포함된다. 현재의 권장 계획은 [09-roadmap](../../docs/09-roadmap.md)이며 과거 계획을 현재 승인된 명세로 오인하지 않는다.
