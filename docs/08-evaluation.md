# 08. 검증 체계: schema가 미래 학습과 계산을 바꾸는가

## 1. 세 종류의 성공을 분리

**Contract:** 인과적 입력, state, 재생, 누수 방지, budget, source 계보가 맞는가.

**Efficacy:** 새 사례의 판단·학습·보존·비용이 실제로 나아지는가.

**Product:** 실제 입력→추론→학습→재개→재시작→삭제/복구 사용자 여정이 동작하는가.

Contract PASS나 unit tests 개수는 efficacy/P1 completion을 대신하지 않는다. 효용 미검증 kernel을 기본 consumer 경로로 자동 승격하지 않는다.

**PROPOSAL:** 헌장의 두 중심 명제를 이 문서의 family에 대응하고 독립적으로 판정한다. H-SAMPLE(새 구조 공유 과제에서 목표 성능까지의 관측 수 감소)은 F01·F03과 §6 학습 지표로, H-COMPUTE(경험·통합 이후 같은 정확도의 총 계산 감소)는 F11·§3·§6 비용식으로 본다. 한쪽의 PASS는 다른 쪽의 근거가 아니다. Rapid learning이 빨라져도 추론이 느릴 수 있고, early exit가 좋아져도 지속학습이 없을 수 있다.

**USER (U-T09):** 표면에서 meta의 meta까지 의도를 파악해 그 방향으로 설계한다. **PROPOSAL:** 의도 6층위와 설계·검증의 대응은 아래와 같다. 4–6층은 대화에서 도출한 해석이며 사용자 확인 전 확정이 아니다.

| 층위 | 설계 위치 | 검증 | 상태 |
|---|---|---|---|
| 1 구현 재료를 계산 그래프·상태·학습 규칙으로 연결 | 05 §1–§3, 06 §5 | §1 Contract, §5 인과적 개입 | 설계됨 |
| 2 이전 경험에 따라 처리 방식이 달라짐 | 06 §9 | §3 S0/SE/SES, F11 | 설계됨 |
| 3 사고 중 이해의 틀 재선택 | 05 §4·§8, 06 §5 | F15(§2-1 제안) | 지표 추가 제안 |
| 4 경험이 만드는 유용한 편향 | 06 §2 q^-와 편향 정의 | F02·F05, §6 편향 지표 | 정의·지표 추가 제안 |
| 5 학습·사고 정책도 학습 | 06 §4·§6, 10 §1 | F11, controller 단계(§3) | 설계됨 |
| 6 이력에 따른 자기 조직화 | 11 §6(제안 문단) | F17(§2-1 제안) | OPEN 가설 |

**ARCHIVE:** Melete는 N1 효용 meet를 충족하지 않은 채 N2·N3 구성요소 연구를 진행했다. 구현 PASS와 효용 PASS를 문서에서는 구분했지만 다음 단계 진입 조건으로 집행하지 못했다는 것이 사후 검토의 지적이다 ([2026-10-15-neural-judgment-roadmap.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/superpowers/plans/2026-10-15-neural-judgment-roadmap.md)).

**PROPOSAL:** 다음 phase나 다음 구성요소의 연구에 들어가기 전에 앞 단계의 efficacy gate(사전 정의한 대조군 대비 효과)를 통과하거나, 통과하지 못한 채 진행하는 이유와 범위를 결과 상태(INCONCLUSIVE/FAIL)와 함께 기록한다. 통과 없이 진행한 연구는 '선행 미충족 위의 탐색'으로 표시하고 기본 경로·phase 완료로 승격하지 않는다.

**USER (B11, 2026-10-11):** 학습 방법 검증이 가장 중요하다. 조합들이 검증됐는가, 수준은?

**PROPOSAL:** 조합마다 검증 수준을 한 표에 표기한다. NOT RUN(설계만), CONTRACT(상태·누수·재생 검사 통과), PILOT(사전 정의 대조 대비 개발 결과이며 확증 아님), CONFIRMED(fresh locked cohort에서 사전 gate 통과). 낮은 수준의 결과를 높은 수준의 문구로 쓰지 않는다. 현재 통합 모델의 조합은 구현·학습이 없으므로 모두 NOT RUN이다([VALIDATION.md](/home/jimmy/repos/full-continual-learning/VALIDATION.md)의 검증하지 않은 것 참조).

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

**LITERATURE (GOUDAR23, 원문 검토 §4.4 표면 대 구조, W2-chu25-goudar23.md:333):** 구조는 같고 표면만 다르거나 표면은 같고 구조가 다른 lure로 두 요인을 분리한 논문은 읽은 11편에서 찾지 못했다. GOUDAR23은 오히려 학습 속도가 자극 코사인 유사도에 크게 의존함을 보인다(문제 3의 trial 수가 유사도 1에서 약 7, 0에서 약 175, 그림 판독).

**PROPOSAL ([2026-11-11-sbl-fulltext-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext-review.md#5-fcl-설계의-시작점-proposal) §5 출발점 5):** F01(구조 같고 표면 다름)과 F02(표면 같고 구조 다름)를 표면 유사도 단계별로 함께 측정해 두 요인을 분리한다.

**LITERATURE (CHU25·SWAMI23·KUMAR26·MICONI25, W2-chu25-goudar23.md:123, W6-swami23-metadata-gap.md:56, W4-tem20-kumar26.md:353,398, W3-elder26-miconi25.md:313-316):** 문헌에는 GOUDAR23·CHU25의 trial-to-criterion 곡선(CHU25는 5문제·10 seed에서 새 문제 학습 trial이 약 710에서 455로, 그림 판독), SWAMI23 LIALT의 example형(예시 1개 + 새 토큰), KUMAR26의 1회 노출 용량 곡선(reservoir 1024유닛에서 12쌍 중 약 7.8), MICONI25의 list-linking·sham 대조가 있다. MICONI25의 실제 설계는 ABCD+EFGH이고 연결쌍 D>E를 4 trial 제시한다(초록의 예시와 다름).

**PROPOSAL (원문 검토 §5 출발점 5):** F03의 H-SAMPLE 틀은 이 곡선들을 측정 틀로만 빌리고, MICONI25는 초록이 아니라 실제 설계를 따르며, 수치는 우리 harness에서 다시 잰다.

SBL의 ‘대부분 이론’은 이 현상들처럼 조작 가능한 질문으로 분해한다. AI 과제의 재현을 실제 뇌 회로 이론의 증명이라고 부르지 않는다.

### 2-1. SBL 이론별 검증 질문과 추가 family (PROPOSAL)

**USER (U-T06):** schema based learning이 얘기하는 대부분의 이론들이 적용되고 검증되어야 한다. **PROPOSAL:** [03-foundations.md](/home/jimmy/repos/full-continual-learning/docs/03-foundations.md) §2의 13개 이론을 아래처럼 조작 가능한 질문과 family에 대응한다. 대응은 AI 과제에서의 현상 재현이며 실제 뇌 알고리즘의 증명이 아니다.

| 이론 | 조작 가능한 질문 | family | 필수 대조 |
|---|---|---|---|
| CLS | fast state를 제거해도 공통 구조가 남고 새 사건은 빠르게 기록되는가 | F03, F10 | replay-only, Sleep 없음 |
| SBL | 관련 schema가 있을 때 목표 성능까지 관측 수가 줄고 무관한 prior는 줄이지 않는가 | F01, F03 | wrong-schema memory, 무작위·동결 memory |
| Hippocampal match–mismatch | 표면 novelty와 관계 novelty를 분리해 반응하는가 | F02, F04 | novelty 단일 신호 |
| Retrieval-mediated integration | 서로 다른 때 배운 A–B와 B–C로 A–C를 추론하는가 | F13 | 재활성화 제거, raw history consumer |
| Reconsolidation | 재활성화 뒤 조건부로 수정되고 모든 read가 overwrite가 되지는 않는가 | F05, F07 | 항상 쓰기 |
| Latent-cause inference | 같은 원인의 수정과 다른 상황의 분리를 구별하는가 | F05, F06, F09 | 단일 pooled prior, oracle cause(상한 진단) |
| Familiarity/recollection | 친숙함과 이해·정확도를 분리하는가 | F02 | 친숙함 점수만으로 halt |
| Structure-mapping | 표면이 달라도 역할·관계를 대응하는가 | F01, F02 | 표면 shuffle |
| Chunking/expertise | 사례→관계→원리 단위로 다층 재표현해 새 개념의 익숙한 지점이 늘어나는가 | F14, F11 | 단일 수준(표면)만 학습한 같은 양의 사례 |
| Automaticity | 경험 후 같은 품질에 필요한 계산이 줄어드는가 | F11, §3 | 쉬운 문제만 조기 종료 |
| TEM/cognitive map | 구조와 내용을 분리해 새 환경에 전이하는가 | F01, F03 | 비분해 baseline |
| vmPFC→MEC 조직화 | 맥락에 따라 기억을 공유하거나 분리하는가 | F05, F06 | 단일 공유 state |
| MS→MEC 기억 선택 | 학습과 사용을 분리해 수정 없이 재선택하는가 | F06 | 재학습 |

**PROPOSAL (추가 family):**

- **F13 관계 통합 추론:** A–B와 B–C를 다른 시점에 관측시킨 뒤 A–C를 묻는다. held-out 조합 정확도와 재활성화 제거 시 손실을 잰다.
- **F14 다층 추상 전이:** 같은 사례군을 사건·역할·관계·원리 수준으로 재표현해 제공하는 조건을 만들고, 새 표면의 같은 관계(F01)와 다른 도메인의 같은 원리(03 §3 원리 분류)에서 관측 수 곡선을 비교한다. 대조는 같은 양의 사례를 단일 수준으로만 학습한 모델이다.
- **F15 사고 중 재선택:** 첫 loop에서 그럴듯하지만 틀린 schema가 선택되도록 유도 단서를 넣은 입력을 주고 loop 중 전환·조합·보류 비율, 최종 정답, loop 수, 추가 비용을 잰다. 대조는 첫 선택 고정과 oracle schema(상한 진단)다.
- **F16 통찰의 전이:** 깊은 loop 뒤에 (i) 같은 문제 재제시 정확도(암기), (ii) 구조를 공유하는 새 사례의 정확도와 C*_ε 변화(전이), (iii) 형성된 표현을 제거했을 때 (ii)만 선택적으로 감소하는지를 잰다. self-consistency와 반복된 confidence 증가는 통찰의 증거로 세지 않는다([11-research-agenda.md](/home/jimmy/repos/full-continual-learning/docs/11-research-agenda.md) §4).
- **F17 이력 분기:** 같은 초기 모델에 서로 다른 경험 이력 H_a, H_b를 준 뒤 같은 입력에서의 schema 선택 분포 q^-, 요구 정확도까지의 loop 수, update 정책 출력의 분기를 잰다. 대조는 같은 이력의 순서 섞기, 같은 이력의 다른 seed, 이력 없음이다. 이득이 이력별 과제에서 비대칭인지 교차 전이 행렬로 본다. 사실 정보는 같고 이력만 다른 두 상태에서 이력에 맞는 판단 차이와 반례 뒤에도 바뀌지 않는 맹목적 고집을 구분해 잰다(B14/H1, §2-2).

**OPEN:** 추가 family의 생성기·world 수·split은 benchmark set v0(§6)에서 정한다. 이 항목들은 승인된 gate가 아니다.

### 2-2. Melete 시기 피드백에서 온 추가 family (PROPOSAL)

**PROPOSAL:** §2-1의 F13–F17에 이어 아래 후보 family F18–F21을 더한다. 번호는 잠정이며 각 family는 같은 관측·계산·갱신 예산의 대조군과 함께 판정한다. Melete 시기의 '이력 의존 편향'(사실 정보는 같고 경험 이력만 다른 두 상태, B14/H1)은 조작이 같으므로 F17(이력 분기)의 측정 항목으로 합쳤다.

| Family | 조작 | 측정 |
|---|---|---|
| F18 성급한 일반화와 해소 | 처음 1–3개 관측이 잘못된 단순 규칙을 유도한 뒤 반례 | 잠정 편향 형성 속도, 오류 해소 속도, 원래 조건 보존(B08) |
| F19 가까운 새로움·먼 새로움 | 기존 관계에서 한 걸음 나간 입력, 표면만 같은 무관한 입력, 매우 먼 입력 | 가장 가까운 schema 시작 대 write 대 보류, 흘려듣기·보류의 적절성(B14/H2·H3b, B04) |
| F20 반복 조회 자기증폭 | 틀린 초기 경로를 반복 조회하거나 모델 자신의 같은 해석을 반복한 뒤 독립 반례 | 고착·붕괴 여부, 강화 상한·감쇠로의 회복(B14/H3a) |
| F21 생성 단독 반복·선호 변화 | 올바른 경험·틀린 해석·동일 root 반복·목표 변경·선호 변화·조건 복귀를 별도 arm으로 | generated 반복의 drift와 외부 반례 뒤 회복 |

**ARCHIVE:** F17의 이력 의존 측정과 F18–F20은 Melete N0의 D5(자기 이력의 다른 편향)·D3(성급한 일반화와 수정)·D4(가까운 새로움)·D7(자기증폭)에, F21은 J2 측정 계획에 대응한다 ([2026-10-12-neural-validation.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/superpowers/plans/2026-10-12-neural-validation.md), [2026-10-15-neural-judgment-roadmap.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/superpowers/plans/2026-10-15-neural-judgment-roadmap.md)). J2는 J1 미통과로 실행되지 않았다.

## 3. 대표 실험: 경험이 숙고를 직관으로 바꾸는가

S0: retrofit과 기본 학습을 마친 상태.

SE: 지정된 경험을 축적한 상태.

SES: 같은 경험으로 Sleep까지 수행한 상태.

Controller를 먼저 우회하고 r∈고정 depth grid에서 Q_s(r)를 측정한다. Update budget도 고정하거나 2차원 (r,u) grid로 평가한다. 테스트는 새로운 binding/entity/value의 관계 공유 사례다. 다음 단계에서 controller를 켜 실제 policy가 저비용 경로를 선택하는지 본다.

SE/SES의 quality–compute 곡선이 왼쪽으로 이동해야 모델 내부의 계산 효율 변화 근거가 된다. 쉬운 문제만 일찍 종료한 평균 loop 감소와 구별한다. Wrong-schema memory, memory lesion, 구조 shuffled experience를 대조한다.

**USER (U-T06):** 이론·수식과 함께 실험을 통한 PoC 증명까지 한다. **PROPOSAL:** 이 대표 실험의 PoC PASS는 아래 조건을 결과를 보기 전에 사전 등록하고 모두 만족할 때만 선언한다. 값은 pilot 뒤 확정한다.

1. SES가 S0보다 C*_ε가 낮다(§6 비용식 전체, 측정한 budget grid 안에서만 비교).
2. 같은 총 계산의 replay-only, 무작위·동결 memory, raw history consumer보다 SES가 낫다(§4).
3. F02 표면 함정과 F05·F06 보호 family에서 한도를 넘는 퇴행이 없다.
4. memory lesion과 구조 shuffled experience에서 이득이 선택적으로 사라진다(§5).
5. 모든 측정이 실제 입력→모델 응답 경로(실제 CLI와 실제 pretrained 모델)에서 얻어졌다. mock·fake는 진단용이며 PoC 근거가 아니다.

FAIL·INCONCLUSIVE도 같은 틀로 기록한다. 합성 Phase-0([README.md](/home/jimmy/repos/full-continual-learning/experiments/phase0/README.md))은 이 PoC의 선행 증거가 아니라 진입 근거다.

**LITERATURE (HWU20, 원문 검토 §4.4 계산량, W1-spens24-hwu20.md:332):** 같은 품질의 추론 계산량을 잰 논문은 읽은 11편에서 찾지 못해 F11과 SE/SES의 quality–compute 곡선 이동에는 문헌 기준값이 없다. HWU20의 절감도 학습 epoch이다.

**PROPOSAL (원문 검토 §5 출발점 6):** 고정 depth grid의 품질–계산 곡선을 controller보다 먼저 얻는다. controller의 후보 신호와 문헌 지지 수준은 [06-mathematical-framework.md](/home/jimmy/repos/full-continual-learning/docs/06-mathematical-framework.md) §6에 있다.

## 4. 비교군

- 동일 pretrained LLM의 직접 응답과 고정-budget 숙고.
- 같은 경험을 raw history로 준 consumer, strong RAG/structured text memory.
- 동일 capacity의 frozen/random memory, no-memory, same update budget.
- 단일 pooled prior와 mixture prior; 명시적 graph/program schema.
- fixed depth, learned early exit, novelty-only routing, 제안 controller.
- 단일 갱신 주기, 고정 multi-timescale CMS, dynamic-frequency, event/readiness, phase-coordinated.
- replay-only, same-compute teacher distillation, Sleep proposal.

단순 방법이 더 좋으면 그 범위에서 복잡한 구조의 필요성을 주장하지 않는다. Oracle source selection이나 true latent cause는 diagnostic upper bound로만 분리한다.

**PROPOSAL (원문 검토 §4.1·§5 출발점 2·8):** schema 기제를 쓰는 모든 실험은 같은 계산·갱신 예산의 고정/무구조/항상-갱신 대조를 의무로 둔다. 쓰기 gate는 항상 쓰기, surprise만, 고정 무작위 gate를 같은 쓰기 예산에서, replay는 novelty×familiarity 배분을 같은 총 replay 계산의 고정 예산과 비교한다.

**LITERATURE (HWU20·GOUDAR23·ELDER26, W1-spens24-hwu20.md:311, W2-chu25-goudar23.md:364, W3-elder26-miconi25.md:98):** 이런 대조에서 단순한 쪽이 비슷하거나 더 높았던 사례가 읽은 논문에 있다(수치는 [03-foundations.md](/home/jimmy/repos/full-continual-learning/docs/03-foundations.md) §7). **ARCHIVE (S23, 2026-11-09-sbl-tracking.md:64):** 반대 방향의 보고도 있다. 고정 scaffold + 새 readout만으로는 같은 이득이 없었다고 하나 이번에 정독하지 않은 원보고 범위다.

## 5. 인과적 개입

Learned vs frozen encoder, parameter component lesion, graph/low-rank direction swap, schema artifact swap, write-gradient 차단, depth-read 제거, 동일 정보의 terminal/all-state/pointer 비교를 설계한다.

Retrained ablation과 같은 checkpoint의 inference lesion은 다른 질문이다. Output range/capacity를 바꾼 lesion을 architecture 기여로 과대해석하지 않는다. 오답을 안정화해 flip rate가 줄어드는 현상을 정답 안정성으로 세지 않는다.

**LITERATURE (GOUDAR23, W2-chu25-goudar23.md:338,371):** subspace 재사용의 인과 시험이 있다. 재사용을 막은 D→S 교란은 두 번째 문제의 trial이 약 3300으로 문제 1(약 3000)과 비슷해지고, 대조인 S→S는 약 450이다(그림 판독).

**LITERATURE (MICONI25, W3-elder26-miconi25.md:282,300):** W_out 또는 W_in을 교체하면 chance로 떨어진다. 같은 네트워크에서 reinstatement를 제거하는 인과 실험은 없다.

**PROPOSAL (원문 검토 §5 출발점 1):** 구조 전이가 표현 제거·교체 때 선택적으로 사라지는지를 schema의 조작적 증거로 쓴다. 재사용 차단(D→S), 행렬 교체, 재활성화 제거를 설계하되 같은 checkpoint의 inference lesion과 retrained ablation은 구분한다.

## 6. Metrics

학습: 목표 품질까지 관측 수, learning curve/AUC, adaptation update·teacher 비용.

판단: family별 accuracy/MSE/utility, both-correct condition pairs, calibration, proper scoring, abstention risk/coverage.

**PROPOSAL (U-T09 목표 2, 헌장 4층):** 경험이 만든 편향(결과 이전 조건부 prior q^-, [06-mathematical-framework.md](/home/jimmy/repos/full-continual-learning/docs/06-mathematical-framework.md) §2)을 이득과 해악으로 나눠 잰다. 편향 이득: schema 일치 사례에서 추가 loop·write 전 첫 시도의 정확도와 필요한 loop 수. 편향 해악: schema 불일치 사례에서 첫 시도가 일치 답을 내는 비율(conformity), 반례 관측 k개 뒤의 정답 전환(아래 "수정" 지표의 correction latency), 반례 뒤 유지 비율. 둘 다 같은 모델에서 q^-를 균등화한 변형과 쌍으로 보고한다. 편향 이득만 보고하거나 불일치 사례 없이 일치 사례 평균만 보고하지 않는다.

수정: correction latency, false update, unrelated regression, ABA recovery, backward/forward transfer.

**LITERATURE (CHU25·ELDER26·TEM20·KUMAR26·GOUDAR23·MICONI25·HWU20, 원문 검토 §4.4 보존·망각, W2-chu25-goudar23.md:321, W4-tem20-kumar26.md:386):** 보존 측정은 읽은 논문에 거의 없다. CHU25·ELDER26은 측정이 없고 TEM20은 기억을 환경마다 리셋하며 KUMAR26은 기존 쌍 보존을 보고하지 않았다(코드의 2NPA 지표는 새 cue만 센다). GOUDAR23은 재학습 savings뿐이고 MICONI25는 장기 망각이 없으며 HWU20만 부분 측정이 있다.

**PROPOSAL (원문 검토 §5 출발점 7):** 보존 평가(F05·F06·F10)는 우리가 만든다. ABA 조건 복귀, 이전 과제의 zero-shot 재평가, savings를 함께 쓴다.

**LITERATURE (SPENS24, W1-spens24-hwu20.md:120,127,134):** 클래스 내 분산 감소와 DRM lure 회상은 인간 데이터와 정성적 유사성만 보이는 재현이다. **LITERATURE (HWU20, W1-spens24-hwu20.md:290-291):** Tse식 probe는 cued/non-cued/original 항목의 활동으로 새 연합을 본다. **PROPOSAL (원문 검토 §5 출발점 4):** 이들을 schema 과적용(prototype 수축·lure 침입)과 공고화의 진단으로 빌린다.

효율: p50/p95 latency, TTFT, decode tokens/s, FLOPs, active parameter/layer 수, memory residency, energy가 측정되면 별도.

비용식: encoder + router + core loops + depth read + memory reads/writes/backward + retrieval/offload + output decoder. Online cost와 Sleep/학습 amortized cost를 둘 다 공개한다. Gradient는 공짜 forward가 아니며 batch·sequence length·hardware·warm/cold state를 맞춘다.

과거 제안된 80% fast coverage / 1pp 품질 margin / fast p95 5배 개선은 **proposal**이었다. 사용자 승인된 gate나 달성값이 아니다. 통합 모델의 목표치는 pilot variability와 실용 요구를 바탕으로 prospective하게 확정한다.

**USER (U-T02):** 숫자로 환산되는 verification(benchmark set 포함)이 필요하다. **PROPOSAL:** 수치 gate를 아래 틀로 결과를 보기 전에 사전 등록한다. 값은 pilot 뒤 prospective하게 확정하며 이 문단은 승인된 수치가 아니다.

gate 레지스트리 한 행의 필드:

    gate_id / hypothesis(H-SAMPLE, H-COMPUTE 또는 보호 family) / family
    primary_metric / 비교 baseline / 효과 크기 하한 Δ_min
    통계 단위(seed × world × history) / 신뢰구간 규칙 / 보호 family 퇴행 한도
    결과 상태 규칙 / 등록 시점(결과 열람 전) / 대응하는 benchmark set_id

Δ_min은 pilot에서 잰 seed×world 변동의 함수로 정한다. 기본 판정은 신뢰구간 하한이 0을 넘고 중앙값 차이가 Δ_min 이상일 때다. 변동 척도와 배수는 pilot 설계에서 고정한다(OPEN). 결과를 본 뒤 Δ_min·baseline·test subset을 바꾸면 새 gate_id를 만들고 이전 gate는 FAIL 또는 INCONCLUSIVE로 남긴다.

benchmark set v0의 필드(값은 OPEN):

    set_id / family / 생성기(관계 구조, 개체·수치 표현, 역할 순열)
    world 수 / split(train·dev·select·confirmation; world·history·task family·time 독립)
    관측 예산 격자(0/1/3/10 등) / loop·update 예산 격자 / 오염 검사 / 데이터 해시

최소 gate 목록(값 없음):

- **G-SAMPLE:** F03에서 SE 또는 SES가 S0보다 목표 품질까지의 관측 수가 적다.
- **G-COMPUTE:** §3 대표 실험에서 C*_ε(SES) < C*_ε(S0)이고 비용은 위 비용식 전체를 포함하며 쉬운 문제 편중이 아니다.
- **G-STRUCT:** F01의 이득이 F02 표면 함정에서 negative transfer로 뒤집히지 않는다.
- **G-PROTECT:** F05·F06에서 이전 조건 판단의 퇴행이 한도 이내다.
- **G-CAUSAL:** 학습한 표현을 제거·교체하면 구조 전이만 선택적으로 감소한다(§5).
- **G-CONTROL:** 위 gate는 §4의 같은 용량·같은 update budget 대조군보다 우수해야 한다. 대조가 비슷하면 그 범위에서 구조의 독자 기여를 주장하지 않는다.

## 7. Data와 통계

독립 world/history/task family/time split. 같은 세계의 paraphrase를 train/test에 섞지 않는다. Test oracle와 latent label은 evaluator 전용. 1/3/10 관측에서 식별 가능한 query 집합이 달라지면 같은 case의 학습곡선인 것처럼 보고하지 않는다. Ambiguous coverage는 accuracy와 별도다.

**USER (B14, 2026-10-12):** 학습 방법 조합을 검토하려면 dataset과 testcase가 필요하다.

**PROPOSAL:** 각 family는 학습을 시작하기 전에 데이터 생성 계약을 가진다.
- 생성기: 시간순 경험 stream, learner가 보는 공개 view, evaluator 전용 oracle을 분리해 만들고 split 단위는 문장이 아니라 world(이력·latent 구조·도메인)다.
- 식별가능성 audit: 유한한 정책 집합을 정의해 각 query가 해당 관측 수에서 식별 가능한지 먼저 계산한다. 식별 불가능한 사례는 삭제하지 않고 모호 사례로 보존한다. 식별 가능 비율이 사전 기준 미만이면 그 데이터를 쓰지 않는다.
- trivial baseline: 다수결, 최근접, 마지막 label 복사(copy-last), analytic reference를 같은 split에서 먼저 보고한다.
- 독립 의미 검토: 기계적 contract·seal 검사의 통과는 benchmark가 선언한 의미와 실제 fixture가 일치한다는 증명이 아니므로 별도 검토를 요구한다.

**ARCHIVE:** Melete의 설계 진리표는 유한 정책 24개·96 slot 중 40개(41.7%)만 식별 가능했고, 식별 가능 비율의 사전 기준으로 10개 관측 시점의 25%를 제안했다 ([2026-10-15-neural-review-postmortem.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/implementation/records/2026-10-15-neural-review-postmortem.md)). j0-v1은 return fixture가 선언한 정책과 달라 마지막 label을 복사하면 맞는데도 기계적 검사가 이를 놓쳐 PASS가 철회됐다 ([2026-10-15-conditional-judgment-j0-feedback.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/implementation/records/2026-10-15-conditional-judgment-j0-feedback.md)). J1에서는 first-copy가 100%인 ceiling을 조건 발견 성공으로 읽지 않기로 했다 ([2026-10-21-neural-judgment-j1-diagnostics.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/implementation/records/2026-10-21-neural-judgment-j1-diagnostics.md)). 위 수치는 Melete 합성 과제의 값이며 FCL의 기준이 아니다.

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

**LITERATURE (CHU25·ELDER26·KUMAR26·SWAMI23, 원문 검토 §8, W7-remediation.md:317-319):** 읽은 논문에서도 ±와 괄호값의 정의·분모 누락이 반복됐다. CHU25는 정확도 정의와 93.20의 분모가, ELDER26은 ±의 정의와 978 대 888 clips가, KUMAR26은 본문 ±의 정의가 없고, SWAMI23은 같은 괄호 표기가 표에 따라 95% 신뢰구간 폭(Table 1·4·7)이거나 표준오차(Table 5·6·8·9)다.

**PROPOSAL:** 모든 ±와 괄호값에 정의(SD/SE/95% CI)와 독립 단위(seed/world/query)를 적고, 그림에서 읽은 값은 읽은 값으로 표시하며, 문헌 수치를 인용할 때는 위치와 분모를 함께 적는다.
