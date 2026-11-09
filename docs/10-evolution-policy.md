# 10. Self-evolution와 운영 정책

## 1. 세 루프와 권한

| 루프 | 변경 대상 | 성공의 의미 |
|---|---|---|
| Experience learning | fast memory, binding, 잠정 schema state | 이후 관측/판단의 적절한 적응 |
| Sleep/consolidation | slow weights, schema 구조, replay policy | 유지와 새 사례 전이, 계산 효율 |
| Development evolution | 코드·구조·목적함수 후보·controller recipe | 독립 평가에서 더 나은 quality–cost |

개발 절차 자체의 진화는 더 바깥쪽 루프다. 초기에는 작고 고정된 실험 관리 체계를 쓰고, 그것의 추가 가치를 먼저 검증한다. Sleep 논문의 self-modification을 repository 자율 코드 변경과 동일시하지 않는다.

## 2. 목표 계약

최상위 목적: 제한된 경험과 계산으로 조건부 구조를 형성·활용·수정하고 기존 유효 지식을 보존한다. 특정 graph/all-hidden-state/decoder를 목적에 섞지 않는다. 특정 메커니즘의 과학적 가치를 연구하는 제한 탐색은 별도의 가설과 대조군을 둔다.

Objectives, 수치 verification/benchmark, negative feedback, operation policy라는 사용자 요구에 **search space**를 명시적으로 추가한다. 무엇을 바꿀 수 있는지 없으면 자동화는 평가를 우회하거나 너무 많은 변수를 동시에 바꾸기 쉽다.

## 3. 후보 생성 계약

```text
candidate_id / parent_candidate_ids
hypothesis / evidence / expected_mechanism
allowed_files_and_modules / frozen_constraints
changed_variables / invariants / rollback_recipe
code_revision / data_recipe / model_revision
train_budget / eval_budget / total_search_budget
primary_metrics / protected_families / acceptance_rule
result / uncertainty / regressions / actual_cost / decision
```

초기 탐색은 update policy, CMS schedule, depth read, rank/capacity, routing 등 한정된 영역부터 한다. 임의의 전체 rewrite를 곧바로 허용하지 않는다. 최고점 하나뿐 아니라 품질·비용·안정성의 Pareto 후보와 다른 계보를 소수 보존한다. 낮은 성능 후보도 연구용 archive에 남을 수 있지만 운영 승격과는 별개다.

## 4. Negative feedback의 내용

점수 하락 외에 어느 조건의 failure인지, 관측 근거, 원인 가설, 변경 대상, 기대되는 개선, 유지할 능력을 기록한다. AI의 원인 설명은 검증된 원인이 아니라 가설이다.

예: 정정 후 새 조건은 좋아졌지만 A조건 복귀가 나빠졌다 → shared state overwrite 가설 → update 범위만 제한 → reader/router는 고정 → correction과 ABA를 함께 평가.

내부 surprise는 기존 이해와 맞지 않는다는 신호일 뿐 어느 쪽이 틀렸는지의 정답이 아니다. 외부 관측·사용자 선호·독립 benchmark와 자기 생성 해석을 분리한다.

## 5. Evaluator의 독립성

후보는 private answer, held-out split, 채점 규칙, 비용/상태 로그를 수정할 수 없다. 단순 프롬프트 금지로 끝내지 않고 실행 권한을 분리한다. 평가에 쓰이는 관측 자체도 후보의 자기 보고에만 맡기지 않는다. 예를 들어 hallucination marker를 지워 점수를 높이는 행위는 개선이 아니다. DGM 계열에서 논의된 문제를 경계 사례로 기록한다. [E02]

AI가 평가 개선을 제안할 수는 있다. 채택 시 새로운 evaluator version으로 분리하고 기존 후보들을 다시 비교한다. 과거 FAIL을 소급 PASS로 바꾸지 않는다.

## 6. Budget와 자동화

사용자가 승인한 범위·예산 안의 candidate 생성, 격리 학습, dev 평가, 기록은 자동화 가능하다. 목적 변경, private data 사용, 외부 서비스, 운영 승격, 새로운 과금/장시간 compute는 별도 권한이 필요하다.

본 repository 게시 작업은 지속적인 자동 개발·GPU 학습·자동 push의 포괄 권한을 부여하지 않는다. 향후 작업에서 scope를 확인한다.

실제 consumed compute, 실패 job, 취소·재시도도 합계에 포함한다. 예정 상한을 실행 비용으로 보고하지 않는다. 중단 조건: budget 소진, 반복된 동일 failure, 평가 결함, 비재현, privilege violation, 보호 family 퇴행.

## 7. 최소 진화 루프

후보 제안 → schema/contract 검사 → sandbox 구현 → dev 학습/평가 → failure analysis → 후보 archive → 제한 selection → fresh confirmation → 품질/비용/유지 gate → 운영 승격 또는 보류.

같은 search budget의 parameter sweep, random search, 한 번의 AI 수정과 비교한다. evolution을 붙여 점수가 올랐다는 것만으로 더 복잡한 개발 체계의 필요성이 입증되지는 않는다.

## 8. 근거와 적용 범위

AlphaEvolve [E01]: seed program과 evaluator를 이용한 코드 탐색.
DGM [E02]: foundation model이 고정돼도 주변 code/tools/workflow 진화 가능성.
GEPA [E03]: 실행 trajectory와 자연어 failure feedback을 이용한 prompt 탐색.
HyperAgents [E04]: task/meta agent 개선 연구.

이들의 성공을 Melete의 neural schema 형성이나 통합 System ONE 성공의 직접 증거로 사용하지 않는다.
