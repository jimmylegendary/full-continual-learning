# 08. 검증 체계: schema가 미래 학습과 계산을 바꾸는가

## 1. 세 종류의 성공을 분리

**Contract:** 인과적 입력, state, 재생, 누수 방지, budget, source 계보가 맞는가.

**Efficacy:** 새 사례의 판단·학습·보존·비용이 실제로 나아지는가.

**Product:** 실제 입력→추론→학습→재개→재시작→삭제/복구 사용자 여정이 동작하는가.

Contract PASS나 unit tests 개수는 efficacy/P1 completion을 대신하지 않는다. 효용 미검증 kernel을 기본 consumer 경로로 자동 승격하지 않는다.

## 2. 핵심 benchmark family

| Family | 조작 | 측정 |
|---|---|---|
| F01 구조 전이 | 같은 관계, 다른 개체/표현/수치 | held-out choice/prediction |
| F02 표면 함정 | 같은 어휘·개체, 다른 관계 | negative transfer, 조건별 paired correctness |
| F03 rapid binding | schema 공유, 새 역할 결합 | 0/1/3/10 등 고정 관측 곡선 |
| F04 새로운 구조 | 기존에 없던 관계 | 적절한 보류/학습/분화, 설명 가능 범위 |
| F05 예외·정정 | 규칙→예외→기존 규칙 재검사 | 국소 수정, 원래 조건 보존 |
| F06 ABA 선택 | A→B→A, goal/context 변경 | 수정 없는 재선택 vs 재학습 비용 |
| F07 오염·반복 | 틀린 generated 해석, 동일 root 재전송 | drift, 과잉확신, false update |
| F08 지연 피드백 | 중간에 context 전환 후 옛 사건 feedback | credit assignment 정확도 |
| F09 불확실성 | 여러 schema가 관측상 구별 불가 | calibration, risk/coverage, 유용한 질문 |
| F10 consolidation | fast state 제거, sleep/replay | 장기 유지, 새 task 적응 개선 |
| F11 계산 효율 | 같은 품질에서 depth/update budget 변화 | cost-to-quality 곡선 |
| F12 외부화 | offload/reload, version migration | 판단·후속 학습의 일관성 |

SBL의 ‘대부분 이론’은 이 현상들처럼 조작 가능한 질문으로 분해한다. AI 과제의 재현을 실제 뇌 회로 이론의 증명이라고 부르지 않는다.

## 3. 대표 실험: 경험이 숙고를 직관으로 바꾸는가

S0: retrofit과 기본 학습을 마친 상태.

SE: 지정된 경험을 축적한 상태.

SES: 같은 경험으로 Sleep까지 수행한 상태.

Controller를 먼저 우회하고 r∈고정 depth grid에서 Q_s(r)를 측정한다. Update budget도 고정하거나 2차원 (r,u) grid로 평가한다. 테스트는 새로운 binding/entity/value의 관계 공유 사례다. 다음 단계에서 controller를 켜 실제 policy가 저비용 경로를 선택하는지 본다.

SE/SES의 quality–compute 곡선이 왼쪽으로 이동해야 모델 내부의 계산 효율 변화 근거가 된다. 쉬운 문제만 일찍 종료한 평균 loop 감소와 구별한다. Wrong-schema memory, memory lesion, 구조 shuffled experience를 대조한다.

## 4. 비교군

- 동일 pretrained LLM의 직접 응답과 고정-budget 숙고.
- 같은 경험을 raw history로 준 consumer, strong RAG/structured text memory.
- 동일 capacity의 frozen/random memory, no-memory, same update budget.
- 단일 pooled prior와 mixture prior; 명시적 graph/program schema.
- fixed depth, learned early exit, novelty-only routing, 제안 controller.
- 단일 갱신 주기, 고정 multi-timescale CMS, dynamic-frequency, event/readiness, phase-coordinated.
- replay-only, same-compute teacher distillation, Sleep proposal.

단순 방법이 더 좋으면 그 범위에서 복잡한 구조의 필요성을 주장하지 않는다. Oracle source selection이나 true latent cause는 diagnostic upper bound로만 분리한다.

## 5. 인과적 개입

Learned vs frozen encoder, parameter component lesion, graph/low-rank direction swap, schema artifact swap, write-gradient 차단, depth-read 제거, 동일 정보의 terminal/all-state/pointer 비교를 설계한다.

Retrained ablation과 같은 checkpoint의 inference lesion은 다른 질문이다. Output range/capacity를 바꾼 lesion을 architecture 기여로 과대해석하지 않는다. 오답을 안정화해 flip rate가 줄어드는 현상을 정답 안정성으로 세지 않는다.

## 6. Metrics

학습: 목표 품질까지 관측 수, learning curve/AUC, adaptation update·teacher 비용.

판단: family별 accuracy/MSE/utility, both-correct condition pairs, calibration, proper scoring, abstention risk/coverage.

수정: correction latency, false update, unrelated regression, ABA recovery, backward/forward transfer.

효율: p50/p95 latency, TTFT, decode tokens/s, FLOPs, active parameter/layer 수, memory residency, energy가 측정되면 별도.

비용식: encoder + router + core loops + depth read + memory reads/writes/backward + retrieval/offload + output decoder. Online cost와 Sleep/학습 amortized cost를 둘 다 공개한다. Gradient는 공짜 forward가 아니며 batch·sequence length·hardware·warm/cold state를 맞춘다.

과거 제안된 80% fast coverage / 1pp 품질 margin / fast p95 5배 개선은 **proposal**이었다. 사용자 승인된 gate나 달성값이 아니다. 통합 모델의 목표치는 pilot variability와 실용 요구를 바탕으로 prospective하게 확정한다.

## 7. Data와 통계

독립 world/history/task family/time split. 같은 세계의 paraphrase를 train/test에 섞지 않는다. Test oracle와 latent label은 evaluator 전용. 1/3/10 관측에서 식별 가능한 query 집합이 달라지면 같은 case의 학습곡선인 것처럼 보고하지 않는다. Ambiguous coverage는 accuracy와 별도다.

Dev는 상세 실패를 제공, selection은 사용 횟수와 feedback 제한, confirmation은 fresh locked cohort. 숨긴 데이터도 aggregate score 반복 접근으로 오염될 수 있다. 시도 수와 hypothesis family를 기록하고 multiplicity와 confidence interval을 prospective 계획한다. Seed×world 의존성을 고려하며 query 반복을 독립 sample로 늘리지 않는다.

통계적으로 유의하지 않음은 동등성·반증이 아니다. 효과 크기 부족과 추정 불확실성은 다르다. 결과를 본 뒤 threshold/margin/test subset을 고쳐 PASS로 만들지 않는다.

## 8. 결과 상태

- PASS: 사전 정의한 scope 안에서 quality/uncertainty/family 보호/비용 조건 모두 만족.
- FAIL: 사전 조건 미달. 어떤 가설과 범위를 기각하는지 명시.
- INCONCLUSIVE: 표본/식별성/검정력이 부족. PASS가 아님.
- BLOCKED: 권한·infra·runtime 문제로 실험 질문을 보존한 실행을 못 함.
- NOT RUN: 실행하지 않음. 설계/코드 존재와 구별.

## 9. 수치 보고 원칙

정확한 denominator, filtered/unfiltered, calibration/test, mean/median, signal MSE/observation MSE를 표시한다. 과거 보고의 값은 ARCHIVE, 이번 실행값은 새 run ID·config·code/data hash·환경·실제 비용과 함께 기록한다. 공개 source code가 있다고 본인의 재현을 완료한 것은 아니다.
