# 04. 뇌 리듬에서 상태·내용 의존적 학습 조율로

**USER 출발점:** 감정·노력·집중·수면·익숙함에 따라 활동이 달라진다면 모든 내용을 일정 token 주기로만 갱신하는 것으로 충분한가? 여러 주파수의 동시·순차·부분 활성화를 더 본질적으로 이해하고 싶다.

**연구 방향:** 주기 하나를 바꾸는 controller를 넘어, 계산·읽기·정보 교환·학습 후보·변경·통합을 구분하여 조율한다. 이는 공학적 가설이며 뇌의 완성된 학습 알고리즘이라는 주장이 아니다. 근거: [R01–R11](../references/README.md), HOPE/CMS [A02].

## 1. CMS에서 구분할 것

기본 CMS의 느린 level은 파라미터가 덜 자주 갱신될 수 있어도 매 forward에 참여할 수 있다. HOPE에는 입력별 learning rate/retention 등 이미 적응적인 요소가 있으므로 ‘모든 내용을 동일 강도로 무조건 쓴다’고 단순화하지 않는다.

처리 시간척도, update 기회, 실제 변경 크기, 기억의 유지 기간은 서로 다르다. 고정 주기는 GPU batching과 비용 관리에 유용할 수 있다. 문제는 그 간격이 학습의 의미까지 대신 결정하는가다.

상수 gradient g를 C개씩 합산해 learning rate eta로 적용하는 단순 경우 총 T개 입력의 변경량은 (T/C)·C·eta·g=T·eta·g다. 덜 자주 갱신한다고 총 변경량이 반드시 줄지는 않는다. 실제 non-linear update는 순서와 state에 의존하므로 이 식을 일반 거동으로 확대하지 않는다.

## 2. 생물학적 관찰과 적용 한계

| 근거 | 논의한 현상 | 옮길 수 있는 가설 / 금지할 확대 |
|---|---|---|
| R01 LFP 생물물리 | 막 전류·배치·형태가 집합 신호에 영향 | EEG/LFP는 weight update counter가 아니다 |
| R02 aperiodic 분해 | 주기적 peak와 비주기 background를 분리 | band power 증가=주파수 증가가 아니다 |
| R03 rhythmic attention | 느린 위상에 따라 여러 영역의 beta/gamma/alpha 조합 변화 | 동시성과 순차성이 공존할 수 있다. 모든 연결이 인과적이라고 확대하지 않음 |
| R04 beta/gamma bursts | 개별 시행의 짧은 burst가 평균에서는 지속처럼 보일 수 있음 | 평균 빈도뿐 아니라 사건의 시점·길이를 연구 |
| R05 theta phase perturbation | 위상과 과제 구간에 따라 encoding/retrieval 수행 영향 | 같은 주파수의 상대 시점도 중요할 수 있음 |
| R06 novelty theta | 새로운 환경에서 theta frequency 감소 관찰 | 낯섦↑→Hz↑→학습↑의 단조 법칙을 사용하지 않음 |
| R07 인간 수면 결합 | slow oscillation·spindle·ripple의 정렬 | 관찰 상관과 causal intervention 구별 |
| R08 위상 맞춘 spindle | 생쥐에서 적절한 slow-wave 위상의 조작이 기억 효과와 연결 | 단순 발생 횟수보다 관계 시점이 중요할 수 있음 |
| R09 공포 회로 4 Hz | 특정 행동과 PFC–amygdala 결합 | ‘4 Hz=공포’ 범용 대응표를 만들지 않음 |
| R10 학습률/불확실성 | 변동성·관측 신뢰도와 새 정보의 영향 | 노력/각성 scalar 하나로 학습 제어를 끝내지 않음 |
| R11 eligibility | 특정 시냅스 실험에서 delayed modulatory signal의 제한된 시간창 | 과거 activity와 나중 feedback의 귀속. 초 단위를 token에 그대로 옮기지 않음 |

빠른 ripple이 장기 통합에 참여할 수 있으므로 fast frequency=단기기억도 틀린 단순화다. 뇌 전체가 순간마다 한 대역만 ‘선택’한다는 전제도 두지 않는다.

## 3. 조율을 위한 최소 분리

| 동작 | 의미 | 예 |
|---|---|---|
| Activate/read | 현재 판단에 이미 있는 구조 사용 | 익숙한 schema를 강하게 읽되 수정은 안 함 |
| Compute | hidden state 정교화 | 익숙한 긴 관계 합성에 여러 loop |
| Bind | 기존 구조에 새 대상 연결 | 낯선 이름을 역할에 연결 |
| Eligibility | 어느 경험이 어떤 경로를 사용했는지 후보 흔적 | 이후 정정의 대상 보존 |
| Write | 어떤 상태/파라미터를 실제 변경 | 신뢰 가능한 새 증거의 국소 반영 |
| Switch | 다른 기존 schema나 맥락 선택 | 수정 없이 B에서 A로 돌아옴 |
| Consolidate | 여러 경험의 안정적 구조 통합 | replay·적응 후 일반화 학습 |
| Protect/expand | 기존 구조 보호 또는 표현 여유 확보 | 예외 때문에 전체 schema를 덮어쓰지 않음 |

활동한 모든 부분을 학습할 필요가 없다. 간단한 정정은 이해는 쉬워도 즉시 기록해야 한다. 낯선 소문은 계산이 많이 필요해도 강하게 쓰면 안 될 수 있다. 익숙함, 적용성, 신뢰도, 변동성, epistemic uncertainty, aleatoric noise, 결과 중요도는 구별할 후보 신호다.

**USER (B04, 2026-10-05):** 너무 동떨어진 내용은 흘려듣는다. 예: 초등학생과 미적분, 반도체를 모르는 운동선수(관심이 있으면 자기 수준의 다음 내용을 찾음), 2007년 비권위자의 스마트폰 제안, 2008 금융위기 전 비권위자의 폭락 예측. 질문은 threshold 이하의 surprise만 학습 대상인지, 관심·편향·방향성은 학습 대상 결정에 어떻게 들어가는지, 학습량과 충격도는 하나인지였다.

**PROPOSAL:** 학습 가능성(learnability)을 쓰기 허용 u와 별도의 신호로 둔다. 후보 입력은 현재 이해 수준에서 이어 붙일 수 있는 거리, 관심, 출처 신뢰도, 잔차 크기다. 거리가 너무 멀거나 신뢰도가 낮은 입력은 얕게 기록하고 강하게 쓰지 않되 폐기하지 않고 보류 상태로 남긴다. 독립 근거가 오거나 이어 붙일 지점(bridge)이 생기면 다시 평가한다. 새 영역을 영구히 배제하지 않도록 작은 탐색 예산을 둔다. 이 신호들을 하나의 임계값으로 합치지 않으며 학습량(η)·쓰기 허용(u)·계산 깊이(a)와도 분리한다.

**ARCHIVE:** Melete v0.2는 admission 신호를 관심·현재 목표 관련성·연결 가능성·출처 기대·해석 경향·낯섦/예측 불일치로 따로 읽고, 선택을 ignore(최소 encounter trace만), defer(연결이 어려운 이유·anchor·재검토 조건 보존), seek_bridge, reflect, assimilate/restructure로 나눠 선택마다 남길 상태를 정했다 ([experience-system.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/design/experience-system.md) §6). 이후 연구 기록은 '관심 밖 입력에는 얕은 기록·보류, 연결 가능성이 생기면 bridge 탐색, 반복된 변화 근거에는 적극적 재구조화'를 비교하자고 정리했다 ([2026-10-09-learning-foundations.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/research/2026-10-09-learning-foundations.md)). 둘 다 제품 가설이며 검증된 규칙이 아니다.

**OPEN:** [neuroscience-origin.md](/home/jimmy/repos/full-continual-learning/sources/neuroscience-origin.md)는 '연결점이 없으면 학습이 불가능하다'는 단정을 채택하지 않았다. 흘려듣기를 불가능이 아니라 학습 대상 제외·보류로 읽는 것이 사용자 의도에 맞는지 사용자 확인이 필요하다. 평가는 [08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md)의 '가까운 새로움·먼 새로움' family 후보(F19)로 다룬다.

## 4. Eligibility의 제안식

최근 사건에 대한 후보 흔적:

    E[l,n+1] = rho[l,n] * E[l,n] + Psi_l(new_evidence_n)

관련 피드백을 결속한 실제 변경:

    W[l,n+1] = W[l,n] + u[l,n] * eta[l,n] * U_l(E[l,n], bound_feedback_n)

읽기/통신 gate는 별도다. 이 식은 생물학의 확정식이 아닌 설계 표기다. rho는 흔적의 유지, u는 write 허용, eta는 강도다. self-generated content는 외부 관측과 다른 provenance를 가진다. 같은 root를 여러 번 추론해도 독립 증거 수는 늘지 않는다.

## 5. 위상을 넣기 전에 해결할 질문

명시적 oscillator가 해결하려는 문제가 무엇인가? 준비된 정보의 교환, 간섭 감소, 다른 속도의 process 조율, 지연 변화에 대한 강건성 등의 가설을 정의한다.

동기 디지털 모델에서 phase가 단순 execution-stage ID와 동치라면 이를 새로운 뇌 모사 원리라고 부르지 않는다. ‘위상 섞기’ 대조군이 아직 준비되지 않은 memory를 읽게 만드는 잘못된 실행이면 증거로 사용하지 않는다. 모든 비교 경로가 유효한 인과적 실행이어야 한다.

## 6. 필수 실험 계열

A. 고정 CMS: 같은 update cadence와 실행 순서.

B. Frequency-adaptive: 상태별 update frequency만 가변.

C. Event/readiness: eligibility·feedback attribution·선택적 write·준비 상태 기반 통신.

D. Phase-coordinated: C에 상대 위상/주기적 창을 더함.

핵심 비교는 D 대 C다. D가 A보다 낫더라도 eligibility나 선택적 쓰기의 이득을 위상의 이득으로 착각하지 않는다. 원인 분리 실험은 optimizer steps·replay data·capacity를 맞추고, 제품 평가는 routing/동기화/메모리 비용을 포함한다.

**USER (U-T08):** 뇌파 개념을 깊이 파악하고 모든 내용을 일정한 token 주기로 갱신하는 것보다 본질적인 조율로 개선한다. **PROPOSAL:** 위 A–D 계열을 해상도 단계로 배치한다. 단계는 새 로드맵의 phase에 대응시킨다.

- **A 고정 CMS:** 첫 통합 모델의 기본값이자 모든 비교의 대조군이다.
- **B 주파수 적응:** update 빈도만 가변인 최소 변형이다. 첫 recursive 모델 이후 A와 같은 budget으로 비교한다.
- **C event/readiness:** eligibility·선택적 write·준비 상태 기반 통신이다. controller v1([05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §4) 이후에 시작한다.
- **D 위상 조율:** 핵심 질문이 D 대 C이므로 C가 안정된 뒤에만 시작한다. §5의 "단계 번호와 동치" 검사를 통과하지 못하면 중단한다.

각 단계는 앞 단계를 대체하지 않고 대조군으로 남긴다. D가 시작되기 전에는 위상·oscillator를 구현의 필수 요소로 약속하지 않는다.

## 7. 실행 시계

외부 경험 e, token position t, 내부 recursion r, optimizer step u, CMS level별 통합 clock s_l, wall-clock을 별도 기록한다. Loop/replay는 경험을 다시 사용하는 계산이지 새로운 world evidence가 아니다. [상태 계약](07-state-and-storage.md)

## 8. 기대하는 통합 결과

사용할 schema·어떤 부분을 깊게 처리할지·무엇을 언제 학습할지의 조율이 경험을 통해 개선되고, 새 구조 공유 과제에서 더 적은 관측과 계산으로 안정적인 판단을 만든다. ‘뇌파 유사 스펙트럼이 나왔다’가 아니라 이 행동 변화가 제품 지표다.
