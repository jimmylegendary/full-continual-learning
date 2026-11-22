# Ali 미팅 이후 A/B/C 비교 실험 설계

작성: 2026-11-22 (Asia/Seoul). **PROPOSAL / NOT RUN**. 사용자 제안은 [직접 확보 원문](../sources/sync/2026-11-22-discussion.md), 문헌 확인은 [보충 참고문헌](../references/abc-evaluation-2026-11-22.md)에 분리한다. 아래 운영 정의·비교 조건·판정 방식은 제안이며 승인된 수치 gate나 실행 결과가 아니다.

## 1. 질문과 주장의 범위

**USER:** Ali가 제기한 핵심 질문은 (1) 단순한 Transformer에 비해 무엇이 더 좋은가, (2) 그 성능에 도달하려면 얼마나 많은 정보를 학습해야 하는가다. 사용자는 Transformer / HOPE(Sleep) / Melete의 세 군에서 A Basic, B Schema, C Bias 실험을 제안했다.

**PROPOSAL:** A/B/C를 다음처럼 연결한다. 통합 System ONE, continuous latent schema, pretrained retrofit이라는 기존 목표를 유지한다.

| 실험 | 판정할 주장 | 그것만으로 판정하지 못하는 것 |
|---|---|---|
| A Basic | 동일 원천 경험에서 품질, 목표 품질까지의 정보·계산, 장기 유지가 개선된다 | 개선 원인이 schema라는 인과적 귀속 |
| B Schema | 과거의 관계 구조를 새로운 사례에 재사용해 추가 관측과 계산을 줄인다 | 모든 종류의 인간 schema 이론을 구현했다는 주장 |
| C Bias / Discovery | 경험이 만든 선호가 새로운 법칙의 발견·수정·후속 전이를 돕는다 | 제한된 세계의 성공으로 보편적 과학 발견이나 역사적 ET-4 통과를 주장하는 것 |

Inductive bias의 효과는 C에만 있지 않다. B의 관련 경험 이득, 구조 불일치에서의 수정, 선택적 기제 제거가 더 작은 규모에서 직접 검사할 수 있는 증거다. 경험량·계산·용량이 다른 세 모델의 최종 점수만으로 schema 기제의 효과를 귀속하지 않는다.

Transformer는 아키텍처이고 next-token prediction은 학습 목적이다. Melete도 동일 next-token/next-event prediction을 외부 목적의 출발점으로 쓸 수 있다. 아래는 새로운 SBL 정리가 아니라 공통 예측 목적을 가진 상태 유지 모델의 비교 표기다.

\[
\hat y_t=f_{\theta}(x_t,s_{t-1}),\qquad
s_t=U_{\phi}(s_{t-1},x_t,\mathrm{feedback}_t),\qquad
\mathcal L_{\rm pred}=-\sum_t\log p(y_t\mid x_t,s_{t-1}).
\]

여기서 feedback은 프로토콜에 따라 공개된 것만 쓴다. 입력 자체를 이용한 test-time adaptation은 가능하지만 아직 숨긴 결과나 미래 관측을 쓰지 않는다. Schema·router·CMS의 내부 목적과 총 계산 제약은 별도 명세하고, 모델 간 외부 예측 과제와 정보 공개 조건은 공통으로 둔다. 메커니즘을 추가한 만큼 정보/계산/유지의 이득이 나오는지가 복잡성의 정당화다.

## 2. 세 대표군과 최소 추가 대조

| 군 | 대표 곡선의 역할 | 실행 전에 고정할 내용 |
|---|---|---|
| Transformer | 기존 구조의 기준선 | 기반 checkpoint, context 길이, persistent state, 허용한 online adaptation |
| HOPE + Sleep | 다중 시간척도 기억·공고화 기준선 | 실제 구현·논문 버전, CMS 설정, Sleep 자료·주기·예산 |
| Melete | schema 선택·갱신·적응적 계산을 통합한 후보 | 같은 기반, retrofit 자료·비용, 추가 상태·controller·recursion 범위 |

**LITERATURE:** Sleep은 HOPE 전용 알고리즘이 아니다. Sleep v2 Table 3에는 `Sleep (Transformer)`와 `Sleep (Transformer + four-level)`이 따로 있다. 따라서 세 대표군과 별도로 Transformer + 동일 예산의 기억/적응, HOPE의 Sleep 유무, Melete의 핵심 기제 제거를 작은 보조 실험으로 둔다. 모든 가능한 baseline을 한 번에 실행하자는 뜻은 아니다.

Frozen/context-only Transformer는 유용한 제품 기준선이지만 그것만 이기면 지속 기억의 이득과 Melete 고유의 구조적 이득이 섞인다. 같은 예산의 bounded retrieval 또는 online LoRA/replay 등 강한 Transformer 대조를 적어도 하나 둔다. 어느 대조가 주 baseline인지는 dev에서 정하고 confirmation 결과를 본 뒤 바꾸지 않는다.

공통 pretrained checkpoint를 쓴 실용 retrofit 비교에서는 **그 기반 위에서의 추가 경험 효율**을 주장한다. 전체 사전학습까지 더 적은 정보가 필요하다는 주장은 별도다. 변환 직후 품질 Q(0), retrofit/meta-training 경험과 계산을 포함한다. 다른 사전학습 모델끼리 비교하면 시스템 비교이며 순수 architecture 통제 비교라고 부르지 않는다. 필요하면 작은 규모의 동일 학습 조건 실험으로 기제를 보강한다. 논문 구현의 일부만 이식한 경우 HOPE 재현 수준을 명시한다.

## 3. 동일 정보·계산·저장의 계약

같은 token 수보다 **같은 원천 경험을 같은 순서와 공개 시점으로 주는 것**을 우선한다. 일반 텍스트의 의미 정보량을 임의의 단일 bit 수로 환산하지 않는다.

| 장부 | 기록할 것 | 해석 |
|---|---|---|
| 외부 고유 경험 N | 관측 ID, 내용 hash, 순서, 피드백 공개 시점 | 같은 자료를 재독해도 N은 늘지 않는다 |
| 외부 자료 크기 | bytes, 공통 tokenizer tokens, 과제별 독립 관측 수 | 표현 길이와 관측 수를 함께 공개 |
| 학습 노출량 | replay를 포함한 처리 예제·tokens·optimizer step | 같은 N에서 더 많이 최적화한 비용을 드러낸다 |
| 추가 감독 | teacher 정답·설명·logits·human hypothesis·도구 결과 | 추가 외부 정보이며 별도 조건으로 맞춘다 |
| 내부 생성 | 자기 dreaming·synthetic replay·요약의 수와 비용 | 새 외부 관측은 아니지만 생성·학습은 비용이다 |
| 계산 C | retrofit, routing, forward, recursion, backward, replay, Sleep, 검색·색인 | FLOPs와 장치 사용 시간을 구분해 기록 |
| 저장 S | weights, optimizer, neural state, KV, replay, 외부 archive | 활성·상주·할당·예약·peak와 증가율을 구분 |

사전 경험으로 schema를 형성한 비용과 새로운 과제에 필요한 추가 경험은 따로 보인다. 외부 고유 경험의 전체 수는 retrofit/meta·history·new 자료의 원천 ID 합집합 크기로 세고, 중복 노출은 별도 기록한다. 공통 기반의 원래 사전학습은 공통 전제이고, 알려진 범위와 모르는 범위를 기록한다. Meta-training을 Melete에만 추가한 뒤 online N_new만 비교한 결과를 전체 정보 효율이라고 부르지 않는다.

같은 N에서 품질을 비교하는 시험과 같은 총 C에서 품질을 비교하는 시험을 모두 둔다. 두 축을 동시에 한 값으로 강제해 알고리즘 고유의 학습 방식을 없애기보다, 여러 사전 지정 예산에서 quality–information–compute–storage 곡선을 낸다. 모델 선택·hyperparameter 탐색 예산도 기록한다.

## 4. A Basic

### A1. 같은 정보에서의 성능과 목표 성능까지의 정보

주요 산출물은 Q_m(N; C,S), C_m(N), S_m(N)이다. 공통 계산/저장 한도 또는 명시한 운용 조건 아래에서 다음 역방향 지표를 함께 낸다.

\[
N_m^*(q)=\inf\{N:Q_m(N)\ge q\text{가 사전 지정 평가창에서 유지}\}.
\]

C_m^*(q)는 해당 운용 조건에서 목표 품질까지의 누적 계산이다. 미도달은 최대 budget 값을 성공값처럼 대입하지 않고 미도달로 남긴다. 목표 q, 유지창, 품질 퇴행 허용폭은 dev pilot 이후 confirmation 전에 고정한다. 예산 grid의 최솟값은 관측한 grid 내 최솟값이지 모든 가능한 정책에 대한 전역 최적값이 아니다.

**PROPOSAL:** 현재 관측을 제공하고 아직 공개하지 않은 결과를 예측한 뒤, evaluator가 채점하고 허용한 피드백만 공개하여 다음 상태를 만든다. 별도 retention/transfer probe는 checkpoint 분기에서 실행한다. Query 내부의 모델 고유 memory/rapid adaptation은 허용하되 평가 정답은 공개하지 않고, 독립 probe 사이의 상태는 복원한다. 연속 운용 시험은 별도로 상태를 계속 유지한다. HOPE의 정상 test-time memory를 모두 끄는 것을 공정성으로 간주하지 않는다.

평균 정확도 한 값에 현재 경험 적응, 여전히 유효한 이전 지식, 새로운 구조 공유 사례를 섞지 않는다. Q(0), 절대 품질, 학습 후 변화도 함께 보인다.

### A2. Turn 비용과 누적 비용

\[
C_{\rm total}(T)=C_{\rm retrofit/setup}
+\sum_{t=1}^{T}C_{\rm online}(t)+\sum_j C_{\rm sleep}(j).
\]

Online에는 입력 처리, router, 모든 loop, depth read, memory read/write, backward, retrieval, 출력 생성이 포함된다. 동일 단위의 자원 사용량을 더하고, 병렬 작업의 wall-clock latency와 단순 합산하지 않는다. 비동기 Sleep은 응답 지연을 숨겨도 총 장치 사용 비용은 남는다.

보고: turn별 latency·TTFT·p50/p95, loop/update 수, 누적 online/Sleep 계산, peak memory·archive 증가, 운용 amortized 비용과 setup 포함 생애 비용. 입력/출력 길이, 장치, batch, precision, warm/cold 상태를 맞추거나 차이를 공개한다. Sleep 직전/직후 품질과 발생 시점을 표시한다.

**LITERATURE:** Sleep v2 Appendix B.5는 동일 step 수의 비용과 동일 목표 품질까지의 비용을 구분한다. §3.2의 용량 확장도 있으므로 초기 parameter count만 맞추는 것으로 저장 조건이 같아지지 않는다.

**PROPOSAL:** 동일 품질 조건에서 Melete의 setup/학습 부담을 이후의 빠른 응답이 언제 회수하는지 break-even turn도 계산한다. 측정 horizon에서 회수되지 않으면 그대로 기록한다. Forward-only 속도 개선, 추가 경험 효율, 생애 계산 절감은 서로 다른 성공이다.

### A3. 장기 유지와 붕괴

기준선의 붕괴 지점은 결과이지 실험 종료 기준이 아니다. 공통 최대 horizon T_max와 지속 실패 기준을 먼저 정하고 세 군을 같은 끝까지 실행한다.

\[
\tau_q=\inf\{t:Q_{\rm retain}(t)<q\text{가 지정된 연속 평가 횟수 동안 유지}\}.
\]

끝까지 유지하면 tau_q > T_max로 기록한다. 일반적인 무한 유지로 확대하지 않는다. A→B→A 복귀, 간섭 증가, 정당한 규칙 변경, 지연 피드백을 넣는다. 바뀐 규칙에 대해 낡은 답을 계속 내는 것은 retention 성공이 아니다. Context-window 이탈, weight forgetting, 잘못된 retrieval, schema 간섭, 저장 한도 초과를 진단 분류한다.

위 tau_q는 사전 지정한 동일한 유효 문항 cohort에서 획득 기준을 먼저 충족한 시점 이후에 정의한다. 처음부터 배우지 못한 cohort는 NOT_ACQUIRED이며 망각 시점 0으로 처리하지 않는다. 새 평가 문항을 계속 추가해 미학습을 망각처럼 세지 않는다. 전체 공통 cohort 품질·획득률과 획득한 cohort의 age별 유지 곡선을 함께 보고하여, 잘 배운 일부 문항만 골라 유지가 좋은 것처럼 보이지 않게 한다.

두 자원 조건은 분리한다. (a) 총 저장량 고정, (b) 활성 neural memory 고정·외부 archive 증가 허용. 후자에서는 저장량·retrieval 지연·재색인 비용을 공개한다. 반복 구조가 있는 경험과 압축하기 어려운 독립 사실 증가 조건을 함께 두며, 유한한 고정 저장으로 임의의 새 사실을 무제한 정확히 보존하는 것을 목표로 삼지 않는다.

## 5. B Schema

### B0. Environment와 knowledge의 조작적 구분

E는 관측 가능한 상황·개체·초기조건·제약, K는 그 환경을 이해하는 규칙·관계·사실 또는 그 규칙을 배울 사례, q는 질문, y는 evaluator 정답이다. z는 여러 사례가 공유하는 관계 구조로 평가기만 알고 있는 잠재 factor다. 실제 benchmark의 environment가 dynamics까지 포함하는 경우가 있으므로 데이터 문장을 임의로 둘로 자르기보다 생성기의 구조/표면/개별 parameter를 먼저 분리한다.

K의 설명을 나중에 제거해도 어떤 K가 적용되는지 판별할 문맥이나 diagnostic observation은 남아 있어야 한다. 관측이 완전히 같은 두 세계가 서로 다른 정답을 요구하면 단일 정답을 강제할 수 없다. 그 경우 불확실성·추가 정보 요청을 평가한다.

### B1–B5. 사용자 pair 시험의 확장

세 대표군에 같은 (E,K)를 경험시킨 뒤 다음 조건을 측정한다.

| 조건 | 후속 입력 | 의미 |
|---|---|---|
| B1 인출 | 같은 E, K 설명 제거 | 환경–지식 연결을 보존·인출 |
| B2 구조 전이 | 새 개체·표현·수치의 E′, 같은 관계 구조 | 표면을 넘어 구조 재사용 |
| B3 조합 전이 | 본 구성요소들의 처음 보는 결합 | 미관측 조합에 일반화 |
| B4 부적합 감지 | 표면은 비슷하나 구조가 다름; 구별 증거 제공 | 잘못된 schema의 적용 억제·수정 |
| B5 복귀 | A→B→A | 간섭 뒤 유효한 기존 schema를 재사용 |

B1은 유용하지만 그것만으로 schema의 구조적 성격을 입증하지 못한다. B2/B3에서 적은 추가 관측으로 직접 보지 않은 관계를 예측하는지가 중심이다.

완성된 K 규칙을 주는 **teaching 조건**과 관측·결과만 주는 **induction 조건**을 나눈다. 전자는 흡수·보존·적용, 후자는 경험에서 규칙을 형성하는 것까지 평가한다. 내부 z/schema label을 모델에 주는 조건은 oracle 진단이며 headline 성능이 아니다.

### 과제 예시와 지표

첫 과제로 잠재 관계 그래프의 일부 transition만 보여 주고, 새 entity binding·관측 순서에서 경험하지 않은 관계와 경로 결과를 예측하는 생성기를 제안한다. 동일 구조의 새 세계, 표면만 유사한 다른 구조, 동일 구성요소의 새 조합을 함께 만든다. 단순 임의 이름 바꾸기만으로 모든 기존 지식 오염이 사라진다고 가정하지 않는다.

**LITERATURE:** TEM은 다음 sensory observation 예측으로 공유 구조를 학습하고 새로운 감각 배치의 환경에서 직접 보지 않은 transition/loop closure를 검사한다. 이 논리에서 과제를 빌리되 TEM의 해당 결과를 Melete의 장기 유지나 계산 절감 증거로 쓰지 않는다.

**PROPOSAL:** 관련 이력과 양·표면 통계·난도를 맞춘 무관 이력을 비교한다.

\[
G_m(n)=Q_m(\text{관련 이력},n)-Q_m(\text{대조 이력},n).
\]

n은 새 과제에서 받은 추가 고유 경험 수다. 관련/대조 이력 뒤에는 같은 후속 경험 prefix와 같은 계산·저장 예산을 적용한다. G_Melete − G_baseline, 목표 전이 품질까지의 N*, 같은 품질에서의 C*, 부적합 조건의 correction latency·오적용률·calibration을 함께 본다. 잘못된 label을 무작위로 섞어 task 자체를 망가뜨린 조건만을 유일한 무관 이력 대조로 쓰지 않는다.

숙고가 직관으로 바뀌었는지는 같은 난도의 새 구조 공유 사례에서 S0/SE/SES의 고정 depth/update grid를 먼저 비교한다. 그 뒤 controller를 켜 같은 품질을 유지하며 실제 저비용 경로를 고르는지 본다. 쉬운 문제만 조기 종료해 평균 loop가 줄어든 결과와 구별한다. 기존 [08-evaluation.md](../docs/08-evaluation.md) §3의 대표 실험을 유지한다.

Schema 관련 상태 제거·교환, 관계 결속 교란, 쓰기 차단으로 관련 전이만 선택적으로 감소하는지 검사하고 같은 규모의 무관 상태 교란을 대조한다. 재학습한 ablation과 동일 checkpoint lesion을 구분한다. Latent probe의 높은 분류 정확도나 예쁜 clustering만으로 표현의 실제 사용을 확정하지 않는다.

## 6. C Bias / Discovery

### 기존 Einstein test와 연결

사용자 C를 [17-einstein-test.md](../docs/17-einstein-test.md)의 경험 조건부 발견 시험(ET)에 연결한다. 그 문서는 이미 실제 지식 마감 T0를 가진 시간캡슐 기반, W(≤T0), P_pre, P_post, W_delta, checkpoint별 발견 곡선을 구분한다. 이번 제안으로 역사적 최종 목표나 ET-0~ET-4(+ET-3p)를 폐기·재명명하지 않는다. 아래 세 트랙은 실험 조건이며 기존 ET 단이나 입력 tier A/B/C와 다르다.

| 트랙 | 비교 조건 | 목표 |
|---|---|---|
| 역사적 경험 조건부 발견 | 검증된 시대 제한 기반 + 당시 경험 stream | 기존 ET-3/ET-4의 역사적 발견 재구성 |
| 새로운 세계의 공통 관측 | 동일 숨은 법칙 세계·동일 trajectory prefix | 같은 증거에서 더 적은 관측·계산으로 법칙 유도 |
| 능동 실험 | 같은 초기 정보·실험 횟수/비용 한도 | 유용한 실험 선택까지 포함한 발견 |

현대 pretrained 모델에 시대 제한 prompt를 넣는 것은 실제 시간캡슐 모델을 대신하지 못한다. 반대로 기존 ET 설계가 시간캡슐 기반을 이미 택했다는 점을 무시하고 그 설계 전체가 prompt cutoff라고 비판하지 않는다. 기존 후보 모델의 자료 provenance·teacher·tokenizer·추가 학습까지 검토할 필요는 남으며, 이번에는 후보 가중치나 corpus를 새로 감사하지 않았다.

초기 객관 평가에는 새 반사실 세계를 쓴다. 공통 수학·물리 prior는 사용할 수 있지만 평가 세계의 정답 법칙/trajectory는 노출시키지 않는다. 상수만 변경한 세계와 함수 구조·잠재변수·상호작용 자체가 다른 세계는 난도와 주장 범위를 구분한다. C에도 가능하면 세 대표군을 유지해 HOPE 대비 Melete의 추가 기여를 본다.

### Trajectory의 감독 수준

전체 연구 기록을 보존하는 것과 모델에 입력으로 공개하는 것은 다르다. 다음 항목을 별도 조건과 장부에 둔다.

1. 실험 행동·초기조건·관측·결과: 공통 관측 stream의 기본.
2. 사람이 선택한 실험 순서: 정보가 많은 관측을 이미 골라준 도움.
3. 중간 가설·질문·막힌 계산·추론: 사용자가 의도한 인물 경험의 일부이며 추가 감독으로 명시.
4. 발견을 알고 쓴 후대 해설 또는 정답 자체: 해당 발견의 입력에서 제외하거나 정답 제공 대조로 분리.

중간 사고를 전부 배제하자는 제안이 아니다. 기존 ET의 입력 내재 수준·자료 tier와 연결해 어느 감독 수준에서 발견이 나왔는지 보인다. 사람의 실험 선택·추론을 준 경우 관측만으로 한 발견이나 독자적 실험 설계 성공으로 확대하지 않는다.

### 객관적 판정

관측 prefix마다 가설, 예측 가능한 코드/모델, 불확실성을 제출하게 한다. 고정한 상태의 분기에서 새 초기조건·외삽 범위·개입·미관측 조합을 평가하고 결과를 원래 학습 stream으로 돌려주지 않는다. 법칙 명칭이나 그럴듯한 설명만으로 통과시키지 않는다.

법칙 회복률, held-out 예측 오차, 개입/외삽 오차, 복잡도–오차 관계, N*·C*, 실패한 prior의 수정 속도, 다음 세계의 학습 절감이 주요 지표다. 수학적으로 동등한 표현은 인정한다. 서로 다른 법칙이 현재 관측을 똑같이 설명하면 정답을 하나로 강제하지 않고 구별 실험·불확실성·허용된 동치류를 평가한다.

내부 schema를 continuous latent로 만드는 것과 외부 평가용 식/코드를 제출하는 것은 양립한다. Symbolic 출력은 검증 인터페이스이지 내부 schema를 symbolic으로 만들라는 요구가 아니다. 법칙을 읽어내는 decoder/도구가 필요하면 세 군에 같은 접근을 주고 비용·추가 감독을 기록한다.

공통 trajectory 시험은 같은 정보를 통제한다. 능동 실험에서는 선택에 따라 얻는 정보가 달라지므로 같은 **획득 예산**을 통제한다. 둘을 동일 정보 비교 결과로 합치지 않는다.

### 기존 benchmark와의 대응

**LITERATURE:** DiscoverPhysics v2는 현실과 다른 22개 curated 물리 세계에서 trajectory를 관측하고 법칙의 Python 구현과 설명을 제출하며, held-out trajectory 오차와 rubric 설명 점수를 평가한다. 실험 선택 효과를 분리하는 randomized mode가 있다. 세계의 법칙은 curated이고 trajectory가 실행 시 생성된다. 원 suite 그대로의 평가와 미공개 새 법칙으로 확장한 평가를 구분한다.

**LITERATURE:** LLM-SRBench는 알려진 식의 암기 문제를 줄이기 위해 변환된 식과 합성 문제를 사용한다. 더 작은 equation discovery 출발점으로 참고하되 주어진 변수에서 식을 찾는 능력과 변수·실험 설계까지 포함한 발견을 구분한다. 이번에는 PMLR 공식 초록·서지를 확인했고 본문 전체를 재검토하지 않았다.

## 7. 최소 실행 묶음과 기존 phase의 관계

아래는 비교 실험의 실행 순서 제안이지 이미 승인된 구현 작업이나 기존 P0(NP) 폐기가 아니다. 순서 1은 실제 세 군의 비교 가능한 구현이 준비된 뒤의 첫 효용 비교를 뜻하며, 기존 개발 phase 번호를 대체하지 않는다. 비모수 대역 결과는 해당 수준의 증거이고 neural schema 구현의 성능으로 표시하지 않는다.

| 순서 | 범위 | 남길 결과 |
|---|---|---|
| 1 | 한 관계 생성기에서 세 군의 A1/A2 + B1/B2/B4 | 같은 정보/총 계산의 전이 곡선, 초기 품질, 단위·누적 비용 |
| 2 | 같은 생성기를 긴 stream으로 확장, ABA·규칙 변경·간섭 | A3 유지 곡선, 실패 원인, 저장 증가 |
| 3 | B3·관련 이력 대조·핵심 schema/제어 ablation | 구조 재사용과 계산 절감의 인과 증거 |
| 4 | 미공개 작은 물리/인과 세계의 공통 trajectory | 관측 수별 발견과 반증·전이 곡선 |
| 5 | 능동 실험 및 기존 역사적 ET의 단계별 확장 | 정보 획득 효율과 역사적 경험 조건부 발견 |

기존 Melete의 recursive depth·CMS 조율·Sleep·offload를 모두 한 번에 추가해야 비교를 시작할 수 있는 것은 아니다. 가장 작은 실제 구현에서 이득을 확인하고 기능마다 같은 확인 실험으로 한계와 추가 기여를 평가한다. 강한 단순 대조와 차이가 없으면 그 범위에서 추가 복잡성의 필요성을 주장하지 않는다.

## 8. 판정과 self-evolution

결과 전에 baseline, 정보/계산/저장 budget, target quality, horizon, 최소 실용 효과, 보호 성능 한도, random seed, 세계/구조 split, probe 빈도를 등록한다. 수치 값은 dev pilot로 정하되 confirmation 자료를 본 뒤 바꾸지 않는다. 독립 표본은 상관된 개별 turn이 아니라 독립 world/history/task-family 실행이며 같은 stream seed를 paired 비교한다.

Self-evolution 후보는 train/dev에서 개선하고 evaluator·봉인된 답·confirmation 세계는 수정하지 못한다. 제안→예산 제한 실험→A/B 보호 지표 확인→독립 확인→승격/rollback의 기존 정책을 따른다. 작은 개선에 매번 역사 ET-4를 전부 돌릴 필요는 없으며, 주장에 대응하는 단계의 증거를 요구한다. 반복 평가에서 test에 맞춰 튜닝한 이력과 그 비용도 기록하고, 소진된 confirmation set은 새 버전으로 교체한다.

실패 결과의 해석도 사전 정의한다. A만 개선되면 효율적인 기억/학습 시스템의 증거, B의 전이·개입까지 개선되면 schema 기제의 근거, C의 새 법칙 유도까지 개선되면 해당 세계 분포에서 발견을 돕는 근거다. 같은 N에서만 좋고 C가 크게 늘면 sample efficiency 개선이며 compute efficiency 개선은 아니다. 동일 품질에서 lifecycle 비용이 줄지 않으면 생애 비용 절감 주장은 보류한다.

Ali에게 보여줄 핵심 결과는 (1) 품질–고유 경험 수, (2) 목표 품질까지 N*·C*, (3) turn별 지연·누적 비용·저장, (4) 장기 현재/유효 과거/전이 품질, (5) schema 기제 제거 효과다. 현재는 이 결과들의 **설계만 있으며 측정값은 없다.**

## 9. 확인 범위

직접 읽은 범위: 이번 사용자 메시지, 기존 FCL의 작업 지침·동기화 정책, README, 평가 설계, ET의 원문/운영 정의/입력 조건, Sleep v2 관련 절·표, DiscoverPhysics v2 관련 절, TEM의 공개 원문 검색 발췌, Transformer/PMLR 공식 초록. 논문 전체를 모두 재현하거나 모든 관련 문헌을 전수 검토한 것이 아니다.

문서 무결성 검사는 저장소 `tools/validate_docs.py`의 로컬 링크·TSV·JSON·Python syntax 범위다. 모델 실행·학습·효용 실험·클라우드 지출은 **NOT RUN**이다. 원격 게시 여부와 실제 문서 검사 결과는 [동기화 manifest](../sources/sync/manifest.json)의 2026-11-22 항목에 기록한다.
