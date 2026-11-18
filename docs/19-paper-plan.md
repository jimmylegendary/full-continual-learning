# 19. 단계별 논문 계획: phase마다 낼 논문의 주장·제목·초록·실험 설계

**상태 라벨:** 이 문서는 **PROPOSAL**이다. 논문의 주장·제목·초록·실험 설계는 모두 계획이고 실행한 것이 없다(**NOT RUN**). 초록의 결과 자리는 전부 [자리표시자]이며 이 문서에는 결과 수치·모델 성능·효과 크기가 없다. 판정 규칙은 형식과 확정 시점만 적었고 임계값·최소 효과·seed 수는 dev pilot의 분산으로 봉인 전에 정해 사용자가 승인한다(D-05). 계산 규모와 비용은 이 문서가 아니라 [15-compute-plan.md](../docs/15-compute-plan.md)의 「PAPER-k 묶음표」가 ESTIMATE로 가진다. 사용자가 승인한 논문 전략이나 투고 결정이 아니며 결정 후보는 §13이다. 외부 발송·연락은 하지 않았고 [14-schema-lifecycle-crud-and-joint-paper.md](../docs/14-schema-lifecycle-crud-and-joint-paper.md)의 공동논문 제안문은 미발송 그대로다. 작성: 2026-11-18.

## 한눈에 보기

**무엇인가.** 사용자 요청의 한 부분에 대한 계획이다(**USER**, 위치는 [2026-11-18-discussion.md](../sources/sync/2026-11-18-discussion.md)의 「사용자 원문」 블록): 「각 단계별(최초 poc포함)논문을 쓴다면 어떤 주장을 할것이고 논문 제목, 초록을 어떻게 할지」. phase 하나가 끝날 때마다 그 phase의 전체 제품(실제 `fcl` CLI에서 끝까지 도는 제품)을 보고하는 논문을 한 편씩 쓴다. P0(NP)부터 P6(ET)까지 PAPER-0~6이고, 절차·benchmark를 따로 내는 선택 논문 PAPER-0b가 있다. 모든 논문은 같은 제품의 해상도가 올라가는 보고이며 한 계층만 보이는 논문, mock만 쓰는 논문, 조사만 하는 논문은 없다.

**읽는 법 세 가지.**

- 초록은 「필요한 결과 등급을 채워 PASS한 경우」의 문장이다. 등급에 못 미치면 그 주장은 pilot 문구로 바꾸고, FAIL이면 negative-result판(논문마다 제목과 주장을 준비했다)으로 낸다. 문구 규칙은 [09-roadmap.md](../docs/09-roadmap.md) §3과 [17-einstein-test.md](../docs/17-einstein-test.md) §3.2의 단별 문구 표를 따른다.
- 주장 Ck-n은 반증 가능하게 쓰고 대응 실험·지표·대조·판정 규칙의 형식·필요 등급을 붙였다. PAPER-0의 주장은 [18-poc-nonparametric.md](../docs/18-poc-nonparametric.md)의 V0-n을 가리킨다.
- 상세도는 PAPER-0·0b·1이 실험 설계까지, PAPER-2·3이 중간, PAPER-4·5·6이 제목·논지·주장의 형식·초록 뼈대와 목표·gate·선택지·결정 대기다. 먼 phase의 모델 이름·규모·수치는 쓰지 않았다.

| 논문 | phase | 작업 제목(영어) | 주장 | 필요 등급 대 phase 상한 | 상세도 |
|---|---|---|---|---|---|
| PAPER-0 | P0(NP) | Schema Memory Without Training: A Non-Parametric Stand-In for Experience-Conditioned Learning over a Frozen Language Model | C0-1 ~ C0-14 | 핵심 주장 3 시도 대 상한 3(주장 단위, 조건 충족 시). 그 밖은 2 이하 | 자세히 |
| PAPER-0b (선택) | P0(NP) 직후 | The Experience-Conditioned Discovery Test: An Operational Protocol and Benchmark for Einstein-Style Discovery | C0b-1 ~ C0b-7 | 절차 1, ET-1 2, ET-0 3 시도 | 자세히 |
| PAPER-1 | P1 | Retrofitting a Small Pretrained Language Model with Titans-Style Memory and CMS Branches: Structure Transfer, Forgetting, and a Rule-Based Familiarity Controller | C1-1 ~ C1-7 | 「schema 이득」은 3이 필요한데 상한 2. 두 안(§5-6) | 자세히 |
| PAPER-2 | P2 | Depth After Experience: Quality–Compute Curves over Structure Families in a Retrofitted Language Model | C2-1 ~ C2-5 | 3 대 3 | 중간 |
| PAPER-3 | P3 | Learning When to Read, Write, and Think: A Learned Controller for Selective Writes and Accommodation | C3-1 ~ C3-5 | 3 대 3 | 중간 |
| PAPER-4 | P4 | Schemas Across Sessions: Sleep Consolidation and Externalization | C4-1 ~ C4-4 | 3 대 3(삭제 보장 없음) | 뼈대 |
| PAPER-5 | P5 | Scaling the Unified Model: Retrofit on Larger and Time-Capsule Bases with a Real Consumer | C5-1 ~ C5-4 | 4(운용 5) 대 4(운용 5). ET-3 주장은 2 | 뼈대 |
| PAPER-6 | P6(ET) | Experience-Conditioned Discovery on Sealed Historical Targets | C6-1 ~ C6-4 | 3 대 P6 상한 제안 3(4는 OPEN) | 뼈대 |

## 1. 지위와 규칙

| 항목 | 내용 |
|---|---|
| 지위 | 논문 계획은 설계 문서의 한 부분이다. 실행하기 전에는 어떤 주장도 결과가 아니다. 논문을 쓰겠다는 약속이나 투고 일정의 승인도 아니다 |
| 증거 표기 | USER(원문이 있는 문장만) / USER-HYPOTHESIS / PROPOSAL / LITERATURE / ARCHIVE / OPEN / NOT RUN / ESTIMATE. 선행 연구는 LITERATURE이고 확인 수준은 [2026-11-18-blueprint-et-design.md](../research/2026-11-18-blueprint-et-design.md)의 선행 연구 표(W2b 조사)를 따른다 |
| 초록 | 영어 180~250단어와 한국어 요약. 결과 자리는 모두 [자리표시자]이고 수치·성능·효과 크기를 쓰지 않는다. 필요 등급을 채워 PASS한 경우의 문장으로 쓰고, 등급에 못 미치면 pilot 문구로, FAIL이면 negative-result판으로 바꾼다 |
| 주장 Ck-n | 반증 가능한 문장 하나에 대응 실험·지표·대조·판정 규칙의 형식·필요 결과 등급을 붙인다. PAPER-0b의 주장은 C0b-n이다. phase별 가설 번호는 만들지 않는다(Melete 시기의 H1~H5와 겹친다) |
| 판정 규칙 | 형식과 확정 시점만 쓴다. 예: world 단위 paired bootstrap의 95% 구간이 0을 넘고 최소 효과 [δ]를 넘으면 PASS. [δ]·seed 수·임계값은 dev pilot의 분산으로 봉인 전에 정하고 사용자가 승인한다. 결과를 본 뒤 고치지 않는다 |
| 결과 상태 | PASS·FAIL·INCONCLUSIVE·BLOCKED·NOT RUN. 통계적으로 유의하지 않음은 동등성이 아니다 |
| 등급과 문구 | 등급은 phase가 아니라 주장 단위로 부여한다([09-roadmap.md](../docs/09-roadmap.md) §3). ET 단별 상한과 쓸 수 있는 문구는 [17-einstein-test.md](../docs/17-einstein-test.md) §3.2의 표 하나가 기준이고 여기서 값을 다시 쓰지 않는다. ET-0·1·2에서는 같은 frozen LLM 안의 arm 사이의 상대 효과만 주장하고 「발견했다」는 시간캡슐 기반의 봉인 단(ET-4)에서만 쓴다 |
| 이름 | 새 phase는 P0(NP)·P6(ET)로 쓴다. 2026-11-03 계획의 P0는 「옛(11-03) P0」다. experiments/phase0의 「Phase-0」, 추적 우선순위 「P0~P2」와 무관하다. 「tier」는 NP 단(NP-0·1·2)·입력 tier(A·B·C)·자원 tier(1~4)로 한정해 쓴다. suite는 「suite S-A」~「suite S-D」로 쓴다 |
| 소유 경계 | feature·flow는 docs/16, ET의 정의·지표·상한·rubric은 docs/17, V0·suite·대조군·실행 행렬은 docs/18, phase 정의와 종료 gate는 docs/09, 계산은 docs/15가 소유한다. 이 문서는 이름으로 가리키고 값을 복제하지 않는다. 계산은 「PAPER-k 묶음표」라는 이름으로만 가리킨다 |
| 논문과 phase | 논문은 phase 종료 제품의 보고다. 앞 phase의 NP arm은 영구 대조군이므로 뒤 논문은 같은 base로 다시 돈 NP arm과 비교한다(MD-1118-O). 학습 모듈은 같은 예산의 NP arm보다 나을 때만 필요하다고 주장한다 |

**가설 문장.** 헌장([01-intent-and-charter.md](../docs/01-intent-and-charter.md) §4)의 두 중심 명제와 이 계획이 쓰는 세 번째 명제 후보다.

- **H-SAMPLE:** 관련 경험에서 배운 구조가 새로운 대상·표현을 가진 과제에 대한 목표 성능까지의 관측 수를 줄인다.
- **H-COMPUTE:** 경험과 통합 이후 새로운 구조 공유 사례에서 같은 정확도를 얻는 데 필요한 총 계산이 줄어든다.
- **H-DISCOVER (PROPOSAL):** 「T0까지의 세계 지식을 가진 기반 위에서, 한 인물의 경험 stream을 schema로 쌓고 미해결 불일치를 보존했다가 재조합·재구조화하는 시스템은, 같은 기반에 같은 자료를 기억 없이 또는 평면 기억으로 준 경우보다 (i) 더 적은 입력에서 (ii) 더 높은 발견 수준에 이르고, (iii) 그 차이는 stream의 내용에 특이적이다(대조 stream에서는 나오지 않는다).」 이 문장은 헌장의 두 중심 명제에 없는 세 번째 명제이므로 헌장 개정이 아니라 PROPOSAL·OPEN으로 표기한다.

## 2. 전체 표: phase × 논문 × 핵심 주장 × 가설 × ET 단 × 계산

「계산」 칸은 값을 쓰지 않고 [15-compute-plan.md](../docs/15-compute-plan.md)의 「PAPER-k 묶음표」(논문마다 실행 수·자원 tier·시간·비용)를 이름으로 가리킨다. ET 단 칸의 「판정」은 그 phase에서 판정 대상인 단이고 「탐색」은 등급 2 이하로만 보고하는 단이다([17-einstein-test.md](../docs/17-einstein-test.md) §3.1).

| phase | 논문 | 핵심 주장(요약) | 가설 | ET 단 | 계산 |
|---|---|---|---|---|---|
| P0(NP) | PAPER-0 | 비모수 schema 기억(NP-0 텍스트·NP-1 잠재)이 같은 예산의 사례·검색·요약 기억보다 구조 전이·간섭·경로 선택·Sleep·ET-0 발견에서 낫다(C0-1 ~ C0-14) | H-SAMPLE·H-COMPUTE(NP판), H-DISCOVER(ET-0판) | ET-0 판정, ET-1·ET-3p 탐색 | 「PAPER-0 묶음표」 |
| P0(NP) 직후 | PAPER-0b | ET의 운영 절차와 ET-0·1 benchmark가 끝까지 돌고 arm·대조 stream을 구분하며 누수를 잡는다. ET-3p는 절차 완주만(C0b-1 ~ C0b-7) | H-DISCOVER(절차) | ET-0·ET-1, ET-3p(탐색) | 「PAPER-0b 묶음표」 |
| P1 | PAPER-1 | 소형 retrofit 모델이 같은 예산의 고정·무구조·항상-갱신 대조와 P0의 NP arm보다 구조 전이·망각 보호에서 낫다(C1-1 ~ C1-7) | H-SAMPLE(H-COMPUTE는 시험하지 않음) | ET-0(학습 arm 대 NP arm), ET-3p 회귀 | 「PAPER-1 묶음표」 |
| P2 | PAPER-2 | 구조 family 3종에서 경험 뒤 같은 품질에 필요한 깊이·계산이 줄고 깊이의 효용이 schema 가용성과 상호작용한다(C2-1 ~ C2-5) | H-COMPUTE(경험 효과), H-SAMPLE | ET-0 깊이 곡선, ET-1 탐색 | 「PAPER-2 묶음표」 |
| P3 | PAPER-3 | 학습된 controller가 규칙형 v0·항상-쓰기·novelty-only보다 같은 예산에서 선택적 write와 accommodation을 잘한다(C3-1 ~ C3-5) | H-COMPUTE, H-SAMPLE | ET-1 판정(조건부 3), ET-2 탐색 | 「PAPER-3 묶음표」 |
| P4 | PAPER-4 | Sleep 통합과 외부화(offload·reload·version)가 세션을 넘어 이득과 호환을 보인다(C4-1 ~ C4-4) | H-COMPUTE(SE 대 SES), H-SAMPLE | ET-1 잠복 효과, ET-2 판정, ET-3 pilot 대상 탐색 | 「PAPER-4 묶음표」 |
| P5 | PAPER-5 | 더 큰·시간캡슐 기반 retrofit과 실제 consumer에서 학습 모듈이 같은 예산의 NP arm보다 나은지(C5-1 ~ C5-4) | H-SAMPLE·H-COMPUTE(복제) | ET-3 판정(pilot 대상, 상한 2) | 「PAPER-5 묶음표」 |
| P6(ET) | PAPER-6 | 봉인 주력 대상에서 stream 특이적 발견 곡선이 사전 명세 판정을 통과하는지(C6-1 ~ C6-4) | H-DISCOVER | ET-4 판정 | 「PAPER-6 묶음표」 |

## 3. PAPER-0 (P0(NP): System ONE-NP) — 자세히

P0(NP)는 사용자가 요청한 POC다(**USER** 원문 「모델 학습없이 non parameter 기반의 무언가로 POC검증을 먼저 해보자」, 위치는 [2026-11-18-discussion.md](../sources/sync/2026-11-18-discussion.md)). 외부 frozen LLM을 쓰는 대역이며 최종형이 아니다([05-integrated-architecture.md](../docs/05-integrated-architecture.md) §3, [09-roadmap.md](../docs/09-roadmap.md) §1.3). 이 논문도 그 한계를 제목·초록·한계 절에서 밝힌다. 동시에 실제 LLM·실제 저장·실제 CLI로 도는 완결 제품이며 mock이나 조사 단계가 아니다.

### 3-1. 제목과 논지

| 구분 | 내용 |
|---|---|
| 영어 제목 | Schema Memory Without Training: A Non-Parametric Stand-In for Experience-Conditioned Learning over a Frozen Language Model |
| 한국어 제목 | 학습 없는 schema 기억: frozen 언어모델 위의 비모수 경험 조건부 학습 대역(System ONE-NP) |
| 한 문장 논지 | 가중치를 한 번도 바꾸지 않고도, 조건별로 분해되고 생명주기를 가진 schema 형태의 비모수 기억은 같은 frozen LLM·같은 token·호출·저장 예산의 사례·검색·요약 기억보다 구조 전이·간섭·경로 선택·Sleep·합성 발견에서 나은가를 실제 CLI에서 끝까지 시험하고, 이긴 범위와 이기지 못한 범위를 모두 보고한다 |

### 3-2. 주장

PAPER-0의 주장은 [18-poc-nonparametric.md](../docs/18-poc-nonparametric.md)의 V0-n을 가리킨다. 대조 arm의 정의는 docs/18 §7, 판정 규칙의 형식 A~F는 docs/18 §4.3이 소유하고 여기서는 번호만 쓴다. 모든 비교는 같은 frozen LLM·같은 revision·같은 backend에서 돈다. 필요 등급 「3 시도」는 docs/09 §3의 등급 3 조건(봉인 manifest, fresh locked cohort, 같은 예산의 대조, 구조 family 2종 이상(lure 포함), 사전 명세 충분 seed, 독립 검토)을 모두 채울 때만 3이고 하나라도 못 채우면 2다.

| Ck-n | 주장(반증 가능) | 대응 | 지표·대조 | 판정 규칙 형식 | 필요 등급 |
|---|---|---|---|---|---|
| C0-1 | 구조는 같고 표면이 다른 새 사례의 정확도는 NP schema arm(`np0`·`np1`)이 사례·검색 기억 arm(`rag`·`ctx`·`base`)보다 높고, 표면은 같고 구조가 다른 lure에서의 negative transfer는 더 낮다 | V0-1 | F01 새 표면 정확도, F02 lure negative transfer, 관측 수별 곡선 | A + B | 3 시도 |
| C0-2 | 조건 B와 충돌하는 경험을 겪은 뒤 조건별로 분해된 기억은 조건 A 질의 정확도를 평면 기억(`flat`·`always`)보다 덜 잃고 A 재방문 때 재학습 관측 수가 더 적다. 조건 B의 새 학습은 쌍으로 지킨다 | V0-2 | A→B→A 정확도(F05·F06), 최초 과제 재평가, savings | A + B | 3 시도 |
| C0-3 | context gating은 무작위·key만 쓰는 선택보다 맞는 schema를 더 자주 고르고, wrong-schema swap은 같은 크기의 무관 내용 swap보다 정확도를 추가로 떨어뜨린다(인과 개입) | V0-3 | swap 뒤 정확도 하락량, 선택 정확도. 선택 오류 지표는 F23 승인 전 보조 | A | 3 시도 |
| C0-4 | 생명주기 판정(update·branch·create·hold)은 create 없음·항상 create·무작위 create보다 새 조건 학습과 기존 조건 보존을 함께 높인다. 「못 찾으면 create」의 두 해석(검색 실패 대 구조적 새로움)은 따로 비교하고 기본 해석을 정하지 않는다(N-4) | V0-4 | 새 조건 학습 곡선과 기존 보존의 쌍, 판정 혼동행렬, 과잉 create율 | A + B | 3 시도 |
| C0-5 | version 되돌리기와 source 삭제 계약이 NP state에서 성립한다(계약). 보존 예산 아래 기능 손실 기반 eviction은 최근성·빈도·무작위보다 재방문 정확도를 더 지킨다(효용, 탐색) | V0-5·V0-7 계약, V0-6 효용 | 되돌린 version의 응답 동등, 삭제 뒤 state 동등, eviction의 재방문 정확도 | C(계약), A + B(보조) | 계약 1, eviction 2(F22는 N-5 승인 뒤 3 시도) |
| C0-6 | 경험 뒤(SE) controller는 익숙한 질문을 fast로 처리해 같은 품질 [q*]에서 LLM 호출·token이 항상 deep이나 controller 없음보다 적다. 쉬운 사례만 조기 종료한 평균과 구분한다(H-COMPUTE의 NP판이며 통합 모델 내부 depth 효율이 아니다) | V0-8 | cost-to-quality 곡선, 난이도 층별 방향, 경로 분포 | D | 3 시도(난이도 층화 필수) |
| C0-7 | 관측 0/1/3/10에서 NP arm은 기억 없음·평면 기억보다 적은 관측으로 같은 정확도에 이르고, 처음 1~3개 관측이 유도한 잘못된 단순 규칙을 반례 뒤 더 빨리 해소하며 원래 조건을 보존한다(H-SAMPLE의 NP판) | V0-9 | 목표 정확도까지 관측 수, 곡선 아래 면적, correction latency, false update | A + B | 3 시도 |
| C0-8 | 관심·수준 admission은 무관·반복 입력을 거르거나 보류해 항상 쓰기보다 같은 저장 예산에서 정확도 저하와 저장 증가를 줄인다 | V0-10 | 유관 질의 정확도와 저장 증가량의 효율, 거른 입력 중 무관 입력 비율 | A + B | 2(흘려듣기 풀이가 사용자 확인 대기) |
| C0-9 | Sleep-NP를 한 상태(SES)는 경험만 한 상태(SE)보다 이후 새 개체 성능이 같거나 높고 저장 크기와 질의당 호출이 줄며, 같은 호출 예산의 replay-only보다 낫다. 가중치 수준 공고화가 아니다 | V0-11 | 세션 2 새 개체 정확도, 저장 bytes, 질의당 호출 | A + D | 3 시도 |
| C0-10 | 긴장 원장과 재조합은 같은 frozen LLM 안에서 기억 없음·평면 기억보다 합성 미시 발견 세계(ET-0)의 발견 수준을 높이고 입력량에 대해 용량–반응을 보이며, 대조 stream(순서 섞기·핵심 입력 제거·무관 stream)에서는 같은 이득이 나오지 않는다. 이는 H-DISCOVER의 ET-0판이고 절대적인 「발견했다」가 아니다 | V0-12 | 발견 수준 곡선(최초 발견 시점·최고 수준·곡선 아래 면적), 오발견율, 특이성, 입력 내재 대비 초과 | A + B | 3 시도(상대 효과만) |
| C0-11 | function·task vector를 schema artifact로 무학습 저장·재적재·합성할 수 있다. 재시작 뒤 효과가 보존되고 새 개체로 전이되며 제거·교체할 때만 효과가 선택적으로 사라진다. 성립은 hook이 되는 backend에서만 시험하고 소형 base급 모델에서의 성립은 소규모 탐색이다 | V0-13, V0-16 | 재적재 뒤 주입 효과, 새 개체 zero-shot 정확도, 합성 과제, 무작위 방향·다른 조건 vector 대조 | A + B | V0-13 3 시도, V0-16 2 |
| C0-12 | 생성물(추상화·재조합 후보)은 관측으로 승격되지 않고 독립 근거로 세어지지 않으며(계약), 틀린 추상화를 반복 조회해도 고착이나 drift 없이 독립 반례 뒤 회복한다(효용, 탐색) | V0-17 | 근거 목록의 생성물 건수(0), 고착률, 회복 속도 | C + A | 계약 1, 효용 2 |
| C0-13 | (선택) frozen LLM 내부에서 Base와 같은 계열의 post-training 변형은 task vector의 분리도·교차 주입 간섭·부분공간 겹침이 다르다. 사용자 가설의 무학습 관찰판이며 인과·가중치 수준의 주장을 하지 않는다 | V0-14 | 과제 분리도, 교차 주입 간섭 행렬, 무작위 방향 대조 | E | 2 이하 |
| C0-14 | 공개 시간캡슐 모델 위에서 NP 시스템이 stream 투입·checkpoint probe·곡선 보고·누수 감사를 끝까지 수행한다(절차 계약). 발견 여부는 주장하지 않는다 | V0-15 | [17-einstein-test.md](../docs/17-einstein-test.md) §10.3의 계약 gate EC-1~EC-7과 docs/18이 더하는 두 항목 | F | 1(탐색, 결과 주장 없음) |

**논문 본문에서 앞세우는 주장.** C0-1·C0-2·C0-3·C0-4·C0-7(구조 전이·간섭·인과·생명주기·표본 효율), C0-6·C0-9(경로 선택·Sleep), C0-10(ET-0 발견), C0-11(잠재 artifact)이다. C0-5·C0-8·C0-12·C0-13·C0-14는 보조 결과 또는 부록이다. 한 논문에 담기에 넓다고 판단되면 둘로 나눌 수 있다(D-42).

**이길 때와 이기지 못할 때의 문구.** 이겨도 쓸 수 있는 말은 「이 합성 family·이 모델·이 seed 집합에서 같은 frozen LLM·같은 예산의 대조 대비 우위(PASS)」까지다(등급 3 조건을 채운 경우). 통합 모델이 필요하다거나 가중치 수준의 schema 형성이 입증됐다는 말은 쓰지 않는다([18-poc-nonparametric.md](../docs/18-poc-nonparametric.md) §1.3, §14.2). 등급 조건을 채우지 못한 주장은 「이 pilot 범위에서 관측했다」로 쓰고 구간을 병기한다. 이기지 못하면 negative-result판(§3-8)으로 낸다.

### 3-3. 초록

초록은 필요 등급(주장별로 위 표)을 채워 PASS한 경우의 문장이다. 등급에 못 미치는 주장은 「이 pilot 범위에서 관측했다」로, FAIL이면 §3-8의 문장으로 바꾼다.

**English abstract.** Continual learning is usually framed as updating weights, yet whether experience-derived structure must live in the weights at all is rarely tested against simple memory baselines. We study a non-parametric stand-in for a unified experience-conditioned learner: a frozen open-weight language model with schema-shaped memory. Experience is abstracted into condition-specific records, read through context gating, and managed by a lifecycle of read, update, branch, create, hold, and evict decisions under a retention budget, with versioning, source deletion, and offline consolidation. No gradient step is taken. A second variant stores and re-injects function vectors and hidden-state associations. We evaluate the system end to end through a command-line interface on synthetic conditional-judgment worlds, separating surface from structure, revisiting an earlier condition after a conflicting one, and using a wrong-schema swap as a causal intervention. Every comparison uses the same frozen model and the same token, call, and storage budgets against no memory, full-history context, dense retrieval, summary, insight, and concept memory, and a flat memory without lifecycle. Decision rules are pre-registered and the manifest is sealed before a fresh cohort is generated. [Result placeholder: structure-transfer difference against case and retrieval memory, with interval.] [Result placeholder: interference and revisit outcome.] [Result placeholder: effect of the wrong-schema swap.] A procedure-only run on a public time-capsule model checks that the discovery protocol executes, without any claim of discovery. The stand-in is not the final form of the system; it is a permanent control for every later learned module.

**한국어 초록.** 지속학습은 보통 가중치 갱신의 문제로 다뤄지지만, 경험에서 얻은 구조가 정말 가중치 안에 있어야 하는지는 단순한 기억 대조군과 직접 비교된 적이 드물다. 이 논문은 통합 경험 조건부 학습기의 비모수 대역을 만들어 시험한다. frozen 공개 가중치 LLM에 schema 형태의 기억을 붙이고, 경험을 조건별 기록으로 추상화하며, context gating으로 읽고, 보존 예산 아래 read·update·branch·create·hold·evict 판정과 version·source 삭제·오프라인 통합을 둔다. gradient 학습은 하지 않는다. 변형으로 활성화에서 뽑은 function vector와 hidden-state key–value 결합 기억을 저장·재주입한다. 자연어로 렌더링한 합성 조건부 판단 세계에서 실제 CLI로 끝까지 돌리며, 표면과 구조를 가르는 설계, 충돌 조건 뒤 이전 조건으로 돌아가는 재방문, 인과 개입인 wrong-schema swap을 쓴다. 모든 비교는 같은 frozen 모델과 같은 token·호출·저장 예산에서 기억 없음·전체 이력·dense 검색·요약·통찰·개념·생명주기 없는 평면 기억과 한다. 판정 규칙은 사전 등록하고 평가 manifest를 봉인한 뒤 새 cohort를 만든다. [결과 자리표시자: 사례·검색 기억 대비 구조 전이 차이의 방향과 구간.] [결과 자리표시자: 간섭과 재방문 결과.] [결과 자리표시자: wrong-schema swap의 효과.] 공개 시간캡슐 모델 위의 절차 시험 한 번은 발견 여부를 주장하지 않고 절차가 끝까지 도는지만 확인한다. 이 대역은 최종형이 아니며 이후 모든 학습 모듈의 영구 대조군이다.

### 3-4. 실험 설계

| 항목 | 계획(PROPOSAL) |
|---|---|
| 실험 환경 (HW / SW / 모델 고정) | HW: 사용자가 재현하는 종료 gate는 host(CPU 16코어, RAM 27GB, GPU 없음)와 소형 모델에서 돈다. 대량 readout은 runcrate의 같은 장치 묶음에서 돌리고 한 비교 안의 arm은 같은 장치를 쓴다. 자원 tier·시간·비용은 「PAPER-0 묶음표」. SW: 실제 `fcl` CLI, session 프로토콜(stdio JSON-lines), 별도 프로세스 runtime, state store, 분리된 evaluator(oracle은 여기에만), 증거 원장(run ID·hash·환경·실제 비용). 모델 고정: 주 모델 1종(8B급 후보, D-01 결정 대기)의 revision·tokenizer hash·seed, 복제 모델(선택), P1 base급 소형 모델(NP-1 성립 확인). NP-1 비교는 hook이 되는 backend에서만. 후보 표는 docs/18의 실험 환경 절 |
| 학습 data | 학습 없음(gradient 0회). 대신 기억에 넣는 경험 data: suite S-A(조건부 판단 세계)·suite S-B(미시 발견 세계)의 생성기가 만드는 경험 stream(관측 0/1/3/10, 충돌 조건 구간, 다세션). 분할 단위는 문장이 아니라 world이고 dev world와 sealed world는 seed·구조 매개변수를 분리한다. 경험과 질문은 renderer를 분리한다(질문은 다른 paraphrase template과 다른 개체 이름 pool). suite S-C(재분장 역사 사례)와 ET-3p의 stream은 탐색용 경험 data다 |
| test data | sealed cohort는 봉인 manifest hash의 시각 뒤에 만든 fresh world다. oracle·잠재 조건 라벨은 evaluator 전용이다. 누수 통제: nonce 어휘, 관측 수별 식별 가능성 audit(식별 불가 질의는 삭제하지 않고 모호 사례로 보존), ceiling·floor 검사(`base`가 floor에 붙어 있지 않으면 dev에서만 난이도 조정), 재분장 suite의 오염 probe. 시간캡슐 run은 시스템 안 모든 생성·판정·검색을 시간캡슐 모델만 쓰고 시간 필터·누수 감사를 거친다(docs/17) |
| 비교 대조 | baseline: `base`, `ctx`(전체 이력), `ctx-deep`, `rag`, `summ`(요약), `insight`(통찰·전략), `concept`(개념), `flat`·`flat-judge`(생명주기 없는 평면), `always`, `noctl-fast`·`noctl-deep`, `nosleep`, `replay-only`. ablation: 판정 규칙 변형(`nocreate`·`always-create`·`random-create`), eviction 정책(`evict-lru`·`evict-lfu`·`evict-rand`), `noadmit`, `np0-nohold`, `np0-notension`, `np0-norecomb`. 인과 개입: wrong-schema swap과 swap-null, `vec-swap`·`vec-random`, lesion. 진단 상한: `oracle` schema. 모든 arm은 같은 frozen LLM과 같은 token·호출·저장 예산을 쓴다 |
| 객관 증명 | 사전 명세(primary 지표·통계·multiplicity·최소 효과·seed 수·candidate 상한·예산 허용오차·보호 지표 임계를 dev pilot의 분산으로 봉인 전에 정하고 사용자가 승인, D-05) → manifest hash 봉인 → fresh cohort 생성 → sealed readout 한 번(같은 cohort 재사용 금지). 통계는 world 단위 paired bootstrap과 다중 비교 보정, query 반복을 독립 표본으로 세지 않는다. 구현자와 다른 독립 검토. 결과 상태와 등급을 필수로 찍는 보고. 재현 seed와 증거 원장의 요약, 세계 생성기·평가 harness·manifest·재현 절차를 공개한다(사료 원문과 비공개 경로는 제외, 공개 범위는 D-44) |

### 3-5. 선행 연구와 차별점

선행 연구 표는 [2026-11-18-blueprint-et-design.md](../research/2026-11-18-blueprint-et-design.md)의 W2b 조사 §1-1을 따른다. 확인 수준은 초록 수준이며 제출 전에 재조회한다(D-40).

- 가장 가까운 것은 비모수 군집 기억(Bayesian Cheatsheet `S52`)과 갱신·대체·맥락 분기·새 schema 생성 판정에 version·provenance를 더한 기억(MINDSET `S53`)이다. 생명주기 판정과 version 자체가 새롭다고 쓰지 않는다. 이 논문이 다르게 주장하는 것은 구조 전이의 인과 개입 평가(C0-1·C0-3), 같은 예산 대조(생명주기 없는 평면 기억 포함), 경로 선택·Sleep·source 삭제 계약을 한 제품에서 끝까지 도는 것이다.
- 통찰·전략·개념 기억(ExpeL `S62`, Dynamic Cheatsheet `S63`, ReasoningBank `S64`, ArcMemo `S66`)은 대조 arm(`insight`·`concept`)의 선행이고, 저장된 추상이 오류를 재생산한다는 보고(`S67`)는 C0-12의 근거다.
- 잠재 artifact는 steering vector 절차 기억(`S68`)과 그 한계(저장된 사실은 거의 쓰이지 않고 다수 기억의 간섭은 시험되지 않음, `S54`)와 추상 개념에 불변 선형 표현이 없다는 보고(`S55`)를 안고 시작한다. 그래서 C0-11은 negative가 될 수 있음을 사전에 명시한다.
- hidden-state kNN 기억(kNN-LM `S70`, Memorizing Transformers `S71`)은 NP-1의 결합 기억의 선행이다.

### 3-6. 그림·표 계획

| 번호 | 내용 | 대응 주장 |
|---|---|---|
| Fig 1 | 구조: 프로세스 경계, state store, evaluator, NP 단(NP-0·1·2)과 flow | 전체 |
| Fig 2 | 표면×구조 2×2 전이 결과와 관측 수별 곡선 [자리표시자] | C0-1, C0-7 |
| Fig 3 | A→B→A 간섭과 재방문 곡선 [자리표시자] | C0-2, C0-4 |
| Fig 4 | wrong-schema swap의 인과 효과와 swap-null 대조 [자리표시자] | C0-3 |
| Fig 5 | 경로 분포와 cost-to-quality 곡선(난이도 층별) [자리표시자] | C0-6 |
| Fig 6 | ET-0 발견 수준 곡선, 용량–반응, 대조 stream [자리표시자] | C0-10 |
| Tab 1 | arm 정의표와 예산 일치(token·호출·저장 단위) | 전체 |
| Tab 2 | 주장별 결과 상태·등급·문구 | 전체 |
| Tab 3 | NP-1 성립 여부(모델 크기·backend별)와 NP-0 성립 여부 | C0-11 |
| Tab 4 | 계약 gate 결과(version·삭제·분리·생성물 격리·ET-3p) | C0-5, C0-12, C0-14 |

### 3-7. 타당성 위협

| 위협 | 내용 | 대응 |
|---|---|---|
| 외적 타당성 | 합성 world, 영어 렌더링, 주 모델 1종이다. 자연어 일반·다른 모델 계열은 주장하지 않는다(P5) | 범위 태그를 문구에 붙이고 복제 모델은 선택 |
| LLM 사전 지식 | 현대 LLM이 규칙을 이미 알면 기억 효과가 가려진다 | nonce 어휘, `base`의 floor 확인을 오염 probe로 사용 |
| 대조군 재구현 | 선행 방법을 같은 계약으로 다시 구현하므로 원 구현과 다를 수 있다 | 재구현 차이를 한계로 적고 원 구현 앵커를 선택(D-22) |
| 추상화 품질 의존 | NP-0은 frozen LLM이 추상화·정합 판정을 하므로 base 크기에 따라 성립하지 않을 수 있다 | NP-1을 대조로 쓰고 성립하지 않은 단은 「없음」으로 기록 |
| 호출·token 가정 | 실행 행렬의 호출 수와 token은 가정이다 | 실측(P0-T04)으로 갱신하고 「PAPER-0 묶음표」가 소유 |
| 다중 비교와 dev 노출 | 주장이 많고 dev 반복이 있다 | 시도 수 기록, primary 비교 목록 봉인, 보호 지표는 평균으로 상쇄하지 않음 |
| 생성물 오염 | 추상화·재조합 후보를 관측처럼 쓰면 순환 근거가 된다 | C0-12의 origin 분리 계약 |

### 3-8. negative-result판

| 구분 | 내용 |
|---|---|
| 영어 제목 | When Case Memory Is Enough: A Negative Result for Non-Parametric Schema Memory over a Frozen Language Model |
| 한국어 제목 | 사례 기억으로 충분할 때: frozen 언어모델 위 비모수 schema 기억의 음성 결과 |
| 주장 | 이 합성 family와 이 모델에서 schema 형태 기억의 이득은 같은 예산의 사례·검색 기억 대비 확인되지 않았다. 병목을 과제 난이도, 검색 key 품질, 추상화 품질, hook 층, 예산, 판정 임계 중 어디에 두는지 분리해 보고하고, 그 범위에서 복잡한 구조의 필요성을 주장하지 않는다 |
| 근거 | docs/18 §14.2의 분기표. FAIL을 소급 PASS로 바꾸지 않는다. 사례 기억이 강했다는 Melete 시기 결과(ARCHIVE)와 같은 방향의 기록이다 |

### 3-9. 투고 후보와 앞 논문에 대한 의존

- **투고 후보(미확정, 일정은 사용자 결정).** 상시 접수 TMLR는 기술적 정확성 중심이고 negative-result판에 친화적일 수 있다. 연 1회 ML 학회(ICML·ICLR·NeurIPS)는 다음 회차의 공지를 확인해야 한다. 공식 마감은 조사 기록의 투고처 표(W2b §6)에 있다. ICML 2027의 전체 논문 마감은 2027-01-22이며 PAPER-0은 구현 전이라 맞추기 어렵다.
- **앞 논문에 대한 의존.** 없음(첫 논문). 이 논문의 UJ0·NP arm·평가 harness·세계 생성기가 이후 모든 논문의 회귀 gate와 영구 대조군이 된다. PAPER-0b와는 같은 P0 산출물을 쓰되 서로의 결과에 의존하지 않는다.

## 4. PAPER-0b (선택: ET 절차·benchmark 논문) — 자세히

P0(NP) 직후에 낼 수 있는 동반 논문 후보다. 낼지는 사용자 결정이다(D-38). 사용자 원문의 「최종적으로는 아인슈타인 테스트 통과를 목표로 함」(**USER**)에서 출발한 경험 조건부 발견 시험(ET)의 운영 정의가 이 논문의 중심이다. ET의 정의·stream 설계·rubric·누수 통제·통과 기준은 [17-einstein-test.md](../docs/17-einstein-test.md)가 소유하고 이 논문은 그것을 절차·benchmark로 보고한다. 「아인슈타인 테스트 통과」라는 문구는 쓰지 않는다(공개된 실행 절차가 없는 시험을 운영 정의로 바꿔 시험하는 것이므로, D-34).

### 4-1. 제목과 논지

| 구분 | 내용 |
|---|---|
| 영어 제목 | The Experience-Conditioned Discovery Test: An Operational Protocol and Benchmark for Einstein-Style Discovery |
| 한국어 제목 | 경험 조건부 발견 시험(ET): 아인슈타인식 발견의 운영 절차와 benchmark |
| 한 문장 논지 | 「T0까지의 세계 지식을 가진 기반 위에 한 인물의 경험 stream을 시간순으로 넣고 checkpoint마다 중립 probe로 발견 수준을 채점한다」는 시험을 입력 tier·대조 stream·입력 내재 수준·누수 감사를 갖춘 실행 가능한 절차로 정의하고, 합성(ET-0)·재분장(ET-1) benchmark에서 그 절차가 기준 시스템을 가르고 대조 stream과 누수를 잡는지 보이며, 공개 시간캡슐 모델 위 ET-3p에서 절차가 끝까지 도는지만 확인한다 |

### 4-2. 주장

| Ck-n | 주장(반증 가능) | 대응 실험 | 지표·대조 | 판정 규칙 형식 | 필요 등급 |
|---|---|---|---|---|---|
| C0b-1 | ET 절차(기반 모델 지정 → stream 투입 → checkpoint probe → 발견 곡선 보고 → 누수 감사)가 실제 `fcl` CLI에서 ET-0·ET-1·ET-3p 모두 끝까지 돈다 | [17-einstein-test.md](../docs/17-einstein-test.md) §10.3의 계약 gate EC-1~EC-7, V0-15 | 감사·시간 필터·모델 사용 규칙·상태 해시·채점·보고·원장의 체크리스트 | C·F(계약형·절차형, 통계 없음) | 1 |
| C0b-2 | (민감도) ET-0 benchmark의 발견 수준 곡선은 강도를 아는 기준 arm들(진단 상한 `oracle`, 하한 `base`, 평면 기억, schema 기억)을 순서대로 가르고 `base`는 floor에, `oracle`은 ceiling에 붙지 않는다 | V0-12의 arm 묶음 | 발견 수준 곡선(최초 발견 시점·최고 수준·곡선 아래 면적), ceiling·floor | A + B | 3 시도 |
| C0b-3 | (stream 특이성 검출력) 같은 구성자·같은 규칙으로 만든 대조 stream(없음·순서 섞기·결론이 다른 stream·무관 stream·핵심 입력 제거)에서 시스템 곡선이 대상 stream보다 낮고, 그 차이는 입력 내재 수준을 통제해도 남는다. 대조에서도 같은 곡선이 나오면 benchmark는 stream 특이성을 재지 못하는 것이다 | ET-0 세계의 대조 stream | 특이성 지표(구성요소·seed 짝의 차), 입력 내재 대비 초과, 오발견율 | A | ET-0 3 시도 |
| C0b-4 | (채점 신뢰도) 입력 stream 자체를 같은 rubric으로 채점한 입력 내재 수준을 쓰면 요약 기억 arm의 출력이 입력을 옮겨 적은 것으로 판정되어 되풀이와 초월이 구분되고, 맹검 채점자 간 일치도는 [κ_min] 이상이다 | docs/17 §7.5·§9.6 | 채점자 간 일치도, 입력 내재 수준 대 출력 수준 | A(일치도 하한) | 2 |
| C0b-5 | (누수·오염 감사 민감도) 의도적으로 주입한 누설 항목과 오염 사례를 항목·stream·기반 모델·인프라 네 층의 감사가 사전 정한 비율 이상 검출한다 | 누수 주입 시험 | 주입 대비 검출률, 누설도 채점의 일치 | A(검출률 하한) | 2 |
| C0b-6 | (재분장 보존성) ET-1 재분장 사례는 원 사례의 구조 구성요소를 보존하면서(평가자 대조), 모델이 원 사례를 알아보는 오염 probe 정확도는 [임계] 이하다 | suite S-C | 구성요소 보존 점검, 오염 probe 정확도 | B | 2 |
| C0b-7 | 공개 시간캡슐 모델 위 pilot 대상 하나에서 NP 시스템이 절차를 완주하고 감사·채점·원장 기록이 계약을 통과한다. 발견 곡선은 기술 보고로만 싣고 발견 여부를 주장하지 않는다 | ET-3p run(V0-15) | 계약 체크리스트, 누설도 채점 결과, 입력 내재 수준 | F | 1(탐색) |

**문구.** ET-0 결과는 「이 합성 family·이 frozen LLM·이 seed 집합에서 같은 예산의 대조 대비 …」까지, ET-1은 「오염 probe 수치([값])와 함께 arm 사이 상대 차이를 관측했다」까지, ET-3p는 「절차가 끝까지 돌았고 감사·채점·원장 기록이 계약을 통과했다」까지다. 「발견했다」·「재현했다」·「확증」·「성공」은 쓰지 않는다([17-einstein-test.md](../docs/17-einstein-test.md) §3.2).

### 4-3. 초록

초록은 필요 등급(위 주장 표)을 채워 PASS한 경우의 문장이다. 등급에 못 미치는 주장은 「이 pilot 범위에서 관측했다」로, FAIL이면 §4-8의 negative-result판 문장으로 바꾼다.

**English abstract.** A widely discussed proposal asks whether an AI system that knows the world only up to a historical date can reach a later breakthrough, but proposals so far outline the idea without an executable protocol, controls, or leakage audits. We define an experience-conditioned discovery test as such a protocol. A person's experience stream, composed of reading, observation, notes, questions, discussion, and trials, is fed in time order to a system built on a base model, and neutral probes at pre-registered checkpoints score the level of discovery on a shared scale that runs from no discovery to a paper-level systematization. The protocol specifies input tiers that separate dated primary sources from retrospective reconstruction and plausible synthesis, control streams that remove, shuffle, replace, or ablate the stream, an input-inherent level that separates repetition of the input from going beyond it, per-item date and leakage scoring, and contamination probes. We release a benchmark ladder of synthetic micro-discovery worlds and re-skinned historical archetypes, and we test whether the resulting curves separate systems of known strength, detect planted leakage, and distinguish a stream's content from its volume. [Result placeholder: separation of reference systems on synthetic worlds.] [Result placeholder: detection rate of planted leakage.] [Result placeholder: specificity against control streams.] Finally, we run the whole procedure once on a public time-capsule model as a procedural preview and report audit and scoring outcomes without claiming that any discovery occurred.

**한국어 초록.** 특정 시점까지의 지식만 가진 AI가 이후의 돌파구에 이를 수 있는가라는 제안은 널리 논의되지만, 실행 가능한 절차·대조·누수 감사는 비어 있다. 이 논문은 경험 조건부 발견 시험(ET)을 그런 절차로 정의한다. 한 인물의 경험 stream(읽기·관찰·메모·질문·토론·시도)을 기반 모델 위 시스템에 시간순으로 넣고, 사전 등록한 checkpoint마다 중립 probe로 발견 수준을 같은 척도(발견 없음에서 논문 수준 체계화까지)로 채점한다. 절차는 날짜 있는 1차 사료·회고 재구성·그럴듯한 합성을 가르는 입력 tier, stream을 없애거나 섞거나 바꾸거나 핵심 입력을 제거하는 대조 stream, 입력을 되풀이한 것과 넘어선 것을 가르는 입력 내재 수준, 항목별 날짜·누설도 채점, 오염 probe를 정한다. 합성 미시 발견 세계와 재분장한 역사 원형의 benchmark를 공개하고, 곡선이 강도를 아는 기준 시스템을 가르는지, 주입한 누수를 잡는지, stream의 내용과 양을 구분하는지 시험한다. [결과 자리표시자: 합성 세계에서 기준 시스템의 분리.] [결과 자리표시자: 주입한 누수의 검출률.] [결과 자리표시자: 대조 stream 대비 특이성.] 마지막으로 공개 시간캡슐 모델 위에서 전 절차를 한 번 돌려 감사·채점 결과를 발견 주장 없이 보고한다.

### 4-4. 실험 설계

| 항목 | 계획(PROPOSAL) |
|---|---|
| 실험 환경 (HW / SW / 모델 고정) | PAPER-0과 같은 host·runcrate 규칙(한 비교 안의 arm은 같은 장치, 비용은 「PAPER-0b 묶음표」). SW: `fcl` CLI의 ET 명령(가칭, docs/17 §11), 분리된 evaluator, 증거 원장. 모델: ET-0·1은 PAPER-0의 주 frozen LLM, ET-3p는 지식 마감이 맞는 공개 시간캡슐 모델 1종(대상 묶음의 pilot 대상은 docs/17이 소유하고 실행 가능 여부·형식은 docs/18의 실험 환경 절). 시스템 안의 모든 생성·판정·검색은 시간캡슐 모델만 쓰고 현대 임베딩은 쓰지 않는다 |
| 학습 data | 학습 없음. 기억에 넣는 경험 data: ET-0은 세계 생성기가 만든 stream, ET-1은 구성자가 사료 제약 아래 만든 재분장 stream, ET-3p는 pilot 대상의 stream(입력 tier A·B·C, 항목마다 날짜·출처·누설도). 구성자와 시스템 개발자의 역할을 분리한다. 사료 원문은 재배포하지 않는다 |
| test data | ET-0·ET-1의 sealed cohort(봉인 뒤 생성). ET-3p의 pilot 대상은 개발에 노출되므로 봉인하지 않고 노출 사실을 기록한다. 객관 하위 과제(수식 동치·수치 예측)와 사전 작성한 중립 probe 은행. 누수 통제: 시간 필터(날짜 없는 항목 거부), 누수 감사 네 층, 누설 제거 변형, 오염 probe |
| 비교 대조 | arm: `base`, `ctx`, `rag`, `summ`, `flat`, `np0`, `np1`, `oracle`. 대조 stream: 없음·순서 섞기·결론이 다른 stream(ET-0)과 같은 시기 비발견자(ET-3p·이후)·무관 인물·핵심 입력 제거(같은 크기의 무작위 제거 병행). 입력 tier A·A+B·A+B+C와 누설 변형별 곡선. 인과 개입: 핵심 입력 제거와 주입 누수 |
| 객관 증명 | stream·probe 은행·rubric·누설 어휘 사전·분석 계획·핵심 입력 집합의 해시 봉인, 맹검 채점 2인 이상과 일치도, 구현자와 다른 독립 검토, 통계 단위는 대상·구성요소(ET-0은 world), 재현 seed·원장·생성기·rubric·probe 작성 규칙·감사 보고 공개(사료 원문 제외) |

### 4-5. 선행 연구와 차별점

[2026-11-18-blueprint-et-design.md](../research/2026-11-18-blueprint-et-design.md)의 W2b 조사 §1-2를 따른다(초록 수준, 제출 전 재조회).

- 반사실 법칙 이동과 변환·합성으로 암기를 막는 법칙 발견 benchmark(NewtonBench `S76`, LLM-SRBench `S77`), 원형·반사실 쌍과 prior-only 프로토콜(SciGame `S78`), 단계적 정보 공개(ProjectionBench `S56`)와 출판 이전 서지 복원(Reconstruction `S57`)이 가장 가깝다. 확인한 범위에서 인물 경험 stream의 시간순 투입·checkpoint 곡선·대조 stream 특이성·입력 내재 수준·항목별 사후 편향 감사를 한 절차로 묶은 것은 보지 못했다(「없다」의 주장이 아니다).
- 누수 통제는 시간 정합 모델(`S58`)과 오염 감사(`S59`, `S60`)와 같은 방향이다. Einstein test의 출처·공개 시간캡슐 모델·공식 제안의 절차 골격과 우리 ET의 차이는 [17-einstein-test.md](../docs/17-einstein-test.md) §4와 W2c 조사 기록이 소유한다.

### 4-6. 그림·표 계획

| 번호 | 내용 | 대응 주장 |
|---|---|---|
| Fig 1 | ET 절차 flow(기반 지정 → stream 투입 → checkpoint probe → 곡선 보고 → 감사)와 역할 분리 | C0b-1 |
| Fig 2 | ET 사다리(ET-0~ET-4, ET-3p)와 단별 등급 상한·문구 | 전체 |
| Fig 3 | 기준 시스템의 곡선 분리와 ceiling·floor [자리표시자] | C0b-2 |
| Fig 4 | 대조 stream별 곡선과 특이성, 입력 내재 곡선 겹침 [자리표시자] | C0b-3, C0b-4 |
| Fig 5 | 주입 누수의 검출률(층별) [자리표시자] | C0b-5 |
| Tab 1 | 입력 tier·대조 stream·누설도 정의 | 전체 |
| Tab 2 | 발견 수준 척도 L0~L5와 객관 하위 과제 | C0b-2, C0b-4 |
| Tab 3 | ET-3p 계약 gate 결과와 감사 보고 | C0b-1, C0b-7 |

### 4-7. 타당성 위협

| 위협 | 내용 | 대응 |
|---|---|---|
| rubric 주관성 | 발견 수준 채점은 사람이 한다 | 맹검 2인 이상, 일치도, 객관 하위 과제 병행, 입력 내재 수준 |
| 구성자의 사후 지식 | stream을 만드는 사람이 정답을 안다 | 구성자와 개발자 역할 분리, 누설도 채점, 입력 tier 표시 |
| 합성 world의 대표성 | ET-0이 역사적 발견을 대표하지 않을 수 있다 | ET-1 재분장과 ET-3p로 단계 확장, 단별 문구 상한 |
| 재분장의 구조 훼손 | 이름·상수를 바꾸며 핵심 관계가 변할 수 있다 | C0b-6의 구성요소 보존 점검 |
| ET-3p 단일 run | 한 번의 실행은 통계가 없다 | 결과 주장 없음, 계약 통과만 |
| 시간캡슐 모델의 능력 하한 | 수식·추론 능력이 부족하면 절차가 무의미해질 수 있다 | 소형판으로 절차 존재만 확인하고 모델 교체는 사용자 결정 |
| 사료 권리 | stream 원문을 재배포할 수 없다 | 공개 범위를 목록과 해시로 제한(D-44) |

### 4-8. negative-result판

| 구분 | 내용 |
|---|---|
| 영어 제목 | What an Experience-Conditioned Discovery Test Cannot Distinguish: Failure Modes of an Operational Protocol |
| 한국어 제목 | 경험 조건부 발견 시험이 가르지 못하는 것: 운영 절차의 실패 양상 |
| 주장 | 곡선이 기준 시스템을 가르지 못하거나(ceiling·floor 포화), 대조 stream에서도 같은 곡선이 나오거나, 감사가 주입 누수를 잡지 못하면 그 설계 요소는 이 형태로 쓸 수 없다. 어느 요소가 어느 조건에서 실패했는지와 수정안을 보고한다. 이 보고는 발견 주장을 포함하지 않는다 |

### 4-9. 투고 후보와 앞 논문에 대한 의존

- **투고 후보(미확정).** 평가를 연구 대상으로 삼는 평가·데이터 성격 트랙(NeurIPS의 Evaluations and Datasets 트랙은 2026년 회차 기준이며 2027 공지는 확인하지 못함), 상시 접수 TMLR, NLP 계열(ACL Rolling Review) 중에서 고른다. 성격과 마감은 조사 기록의 투고처 표(W2b §6)를 따르고 선택은 D-38과 D-40다.
- **앞 논문에 대한 의존.** PAPER-0의 세계 생성기·arm 정의·평가 harness·ET-3p run을 재사용하지만 결과에는 의존하지 않는다. PAPER-0이 먼저 나오면 인용하고, 뒤에 나오면 같은 산출물을 인용한다. 이 논문의 절차는 PAPER-6의 ET-4 판정이 그대로 쓴다.

## 5. PAPER-1 (P1: 소형 retrofit 모델) — 자세히

P1의 제품은 소형 pretrained 모델에 NMM(Titans식 기억)·CMS 분기를 retrofit하고 규칙형 controller v0(fast·learn·deep)를 둔 하나의 모델이며, 실제 `fcl` CLI에서 UJ1 전체 여정을 처음부터 끝까지 돈다([09-roadmap.md](../docs/09-roadmap.md) §5 P1). 「P1은 MVP」라는 사용자 전역 규칙과의 관계는 P0(NP)가 뼈대와 전체 여정을 먼저 세우고 P1이 첫 학습 해상도가 된다는 해석이며 사용자 확인 대기다.

### 5-1. 제목과 논지

| 구분 | 내용 |
|---|---|
| 영어 제목 | Retrofitting a Small Pretrained Language Model with Titans-Style Memory and CMS Branches: Structure Transfer, Forgetting, and a Rule-Based Familiarity Controller |
| 한국어 제목 | 소형 사전학습 언어모델에 Titans식 기억과 CMS 분기를 이식하기: 구조 전이·망각·규칙형 익숙함 controller |
| 한 문장 논지 | 소형 pretrained 모델에 기억 경로와 CMS 분기를 retrofit한 하나의 모델이 경험 입력부터 source 삭제까지의 전체 여정을 실제 CLI에서 끝까지 돌고, 같은 계산·쓰기 예산의 고정·무구조·항상-갱신 대조와 같은 base로 다시 돈 P0의 NP arm보다 구조를 공유하는 새 사례의 표본 효율과 망각 보호에서 나은가를 보인다(H-SAMPLE. H-COMPUTE는 P1에서 시험하지 않는다) |

### 5-2. 주장

arm 이름은 [09-roadmap.md](../docs/09-roadmap.md) §5 P1의 정의를 따른다(`full`, `fixed`, `flat`, `always`, `noctl`, `ctx`, `base`). NP arm은 P0의 `np0`·`np1`을 같은 base로 다시 돌린다.

| Ck-n | 주장(반증 가능) | 대응 실험 | 지표·대조 | 판정 규칙 형식 | 필요 등급 |
|---|---|---|---|---|---|
| C1-1 | 구조를 공유하는 새 개체·표면에서 `full`의 정확도는 관측 1/3/10에서 `fixed`·`flat`·`always`·`base`보다 높고 표면 lure의 negative transfer는 더 낮다 | UJ1 ④, 2×2 표면/구조(F01·F02·F03) | 새 개체 전이 정확도, lure negative transfer, 관측 수별 곡선 | A + B | 「schema 이득」 문구는 3. P1 상한은 2(§5-6) |
| C1-2 | 반례·정정 뒤 국소 갱신에서 `full`은 `always`보다 최초 과제 재평가 손실과 이전 조건 재방문(ABA) 손실이 작다. 새 조건 학습은 쌍으로 지킨다 | UJ1 ⑤⑥⑦(F05·F06) | 최초 과제 재평가, ABA 재방문, 새 조건 학습의 쌍, 원능력 probe | B(보호) + A | 2 |
| C1-3 | 같은 base·같은 예산에서 `full`은 P0의 NP arm보다 C1-1·C1-2 지표에서 낫다. 같거나 못하면 학습 모듈의 필요성을 주장하지 않는다(MD-1118-D) | UJ1 전체를 `--arm`만 바꿔 반복 | NP arm 대비 C1-1·C1-2 지표의 차이 | A | 2(3은 (a)안) |
| C1-4 | wrong-schema state swap(다른 세계의 state를 복원 경로로 이식)은 `full`의 전이 이득을 같은 크기의 무관 state swap보다 더 지운다. state 변화가 관찰된다는 것이지 schema 형성의 증거는 아니다 | `fcl diff`와 state swap(UJ1 ③) | swap 뒤 정확도 하락량, swap-null 대조 | A | 2 |
| C1-5 | UJ1의 10단계가 `full`과 대조 6 arm 모두에서 실제 CLI·실제 가중치·실제 write·디스크 저장·runtime 재시작·source 삭제로 끝까지 돈다. 재시작 전후 응답 동등(허용오차는 noise floor [ν]보다 작게 약속하지 않음), 삭제 동등, budget 일치(어긋나면 INVALID), 누수 audit 0 | P1 종료 gate (1)(3) | 자동 E2E, 계약 테스트 | C | 1(Contract·Product) |
| C1-6 | retrofit은 함수를 보존한다: 초기 출력이 base와 허용오차 안에서 같고 학습 뒤 원능력 probe가 base 대비 한도 [ε] 안에 있다 | P1-T05·T09 | 일반 텍스트 perplexity, 비세계 질문 | B | 2 |
| C1-7 | (탐색) 규칙형 controller v0의 경로 분포와 계산량을 보고한다. `noctl` 대비 같은 품질에서의 계산 차이는 탐색이며 H-COMPUTE의 시험이 아니다(경로가 r∈{1,2}뿐) | UJ1 ④ | 경로 분포, 호출·FLOPs 추정(측정만) | E | 2 이하 |

**문구.** 상한 2에서 쓸 수 있는 말은 「이 pilot 범위에서 사전 명세 대조를 통과(미달)했다」와 구간 병기까지다. 「schema 이득」·「개선했다」·「일반화」·「빠른 판단 성립」·「계산 절감」은 쓰지 않는다. 이름만 같은 간이 구현을 원본 HOPE·Titan-Llama 재현이라고 부르지 않고 설계 차이와 생략된 학습을 적는다([09-roadmap.md](../docs/09-roadmap.md) §3의 문구 규칙 2).

### 5-3. 초록

초록은 (b)안(pilot 문구)의 기본 문장이다. (a)안을 택하면 마지막 문장의 등급 표현을 「한정 확증」과 범위 태그로 바꾼다.

**English abstract.** Pretrained language models learn from experience only through in-context text or costly retraining. We retrofit a small pretrained language model with a Titans-style neural memory path in a few attention positions and a continuum-memory branch in a few feed-forward blocks, add a rule-based controller that routes each question to a fast, learn, or deep path by familiarity, and package the result as a complete command-line product: experience input, questions about new entities, counterexamples and corrections, re-evaluation of the first task, revisiting an earlier condition, saving, restart, restoration, and source deletion. The same journey runs unchanged for the target and for six controls that share the module, the write budget, and the compute accounting: a fixed variant, a flat single-memory variant, an always-update variant, a variant without the controller, a raw-history variant, and the base model. A non-parametric arm from the preceding stage, run on the same base, serves as a permanent control. Evaluation crosses surface and structure, includes forgetting probes, and uses a wrong-schema state swap as a causal intervention. The manifest is sealed before a fresh cohort is generated. [Result placeholder: structure-transfer difference against equal-budget controls, with interval.] [Result placeholder: forgetting after correction and after revisiting an earlier condition.] [Result placeholder: comparison with the non-parametric arm.] We report the stage's pre-specified readout under a development-pilot grade, state what this setting does not license, and release the harness, the manifest, and the ledger.

**한국어 초록.** 사전학습 언어모델은 경험에서 배우려면 문맥 텍스트에 기대거나 비싼 재학습을 해야 한다. 이 논문은 소형 사전학습 모델의 일부 attention 위치에 Titans식 신경 기억 경로를, 일부 feed-forward 블록에 continuum memory 분기를 이식하고, 질문마다 익숙함으로 fast·learn·deep 경로를 고르는 규칙형 controller를 더해, 경험 입력·새 개체 질문·반례와 정정·최초 과제 재평가·이전 조건 재방문·저장·재시작 복원·source 삭제를 하나의 CLI 제품으로 끝까지 돌린다. 같은 여정이 같은 모듈·쓰기 예산·계산 기록을 공유하는 여섯 대조(고정, 평면 단일 기억, 항상-갱신, controller 없음, 원 이력, base)와 같은 방식으로 돈다. 앞 단계의 비모수 arm을 같은 base로 다시 돌려 영구 대조로 둔다. 평가는 표면과 구조를 교차하고 망각 probe를 포함하며 wrong-schema state swap을 인과 개입으로 쓴다. 평가 manifest를 봉인한 뒤 새 cohort를 만든다. [결과 자리표시자: 같은 예산 대조 대비 구조 전이 차이와 구간.] [결과 자리표시자: 정정 뒤와 이전 조건 재방문 뒤의 망각.] [결과 자리표시자: 비모수 arm과의 비교.] 이 단계의 사전 명세 readout을 개발 pilot 등급으로 보고하고 이 설정이 허락하지 않는 것을 적으며, harness·manifest·원장을 공개한다.

### 5-4. 실험 설계

| 항목 | 계획(PROPOSAL) |
|---|---|
| 실험 환경 (HW / SW / 모델 고정) | HW: 종료 gate와 재현은 host(+노트북 12GB GPU), retrofit 학습과 대량 readout은 runcrate의 같은 장치 묶음(자원 tier·시간·비용은 「PAPER-1 묶음표」). SW: 실제 `fcl` CLI·runtime·retrofit write engine·state store(bundle v0, 원자적 commit)·분리된 evaluator·증거 원장. 모델: 소형 pretrained 1종(D-01 후보, 크기는 결정 대기(D-20))의 revision·tokenizer hash·seed 고정, 일부 layer만 retrofit(전 층 아님) |
| 학습 data | outer-loop 학습: 평가 세계와 분리된 train world(구조 family 1종 × 개체 이름 pool × 표면 template)로 NMM·CMS 모듈을 학습해 test-time write가 query loss를 줄이게 하고, deep 경로의 짧은 적응 학습을 같은 예산 안에 둔다. arm마다 같은 학습 예산(`fixed`는 학습하지 않음). 경험 입력은 test-time write로 들어간다. 분할은 train·dev·sealed world이고 renderer는 경험용과 평가용 paraphrase를 분리한다 |
| test data | sealed world(manifest 봉인 뒤 생성, fresh cohort), 2×2 표면/구조(F01·F02), 관측 0/1/3/10, 반례·정정 질의, 최초 과제 재평가, 이전 조건 재방문, 원능력 probe(일반 텍스트 perplexity·비세계 질문). 누수: oracle은 evaluator 전용, 식별 가능성 audit, ceiling·floor 검사(통과 전에는 봉인하지 않음) |
| 비교 대조 | baseline: `fixed`, `flat`, `always`, `noctl`, `ctx`, `base`와 같은 base의 P0 NP arm. ablation: write 정책(Titans식 surprise 대 항상-갱신), controller 유무, retrofit 범위. 인과 개입: wrong-schema state swap과 swap-null, `fcl diff`로 바뀌어야 한다/바뀌면 안 된다고 정의한 state 집합의 관찰 |
| 객관 증명 | P1-T14 사전 명세(primary 지표·통계·multiplicity·최소 효과·seed 수·예산 허용오차·보호 지표 임계·controller 두 임계값을 dev pilot 분산으로 정하고 구현자와 다른 reviewer 검토 뒤 hash 봉인, D-05) → sealed readout 한 번(T15). 통계는 seed × world 단위(query 반복은 독립 표본이 아님). 결과 상태와 「등급 2」를 필수로 찍는 보고, 금지 문구 검사기, 재현 절차 문서를 새 디렉터리에서 그대로 따라 UJ1이 도는지 확인, 원장·manifest·harness 공개 |

### 5-5. 선행 연구, 그림·표, 타당성 위협

**선행 연구와 차별점.** [2026-11-18-blueprint-et-design.md](../research/2026-11-18-blueprint-et-design.md)의 W2b 조사 §1-3을 따른다(초록 수준).

- 가장 가까운 것은 기억 모듈 retrofit 계열(Titans A01, Titan-Llama A04, Nested Learning A02: catalog)과 대청크 test-time 학습·기억 최적화(ATLAS `A39`, LaCT `A40`)다. 이 논문이 다르게 주장하는 것은 장기 문맥 LM 성능이 아니라 구조를 공유하는 새 사례의 표본 효율과 망각이며 같은 base의 NP arm을 영구 대조로 둔다는 점이다.
- 「메모리 slot 갱신 대 low-rank 갱신」은 slot 기반 지속학습(Sparse Memory Finetuning `A42`, Memory Layers at Scale `A41`)과 표현 drift 비교(`A43`)가 가장 가깝다. 비모수 라우팅 + 모수 adapter(CaLLM `A48`, Factorized Skill Memory `A50`)와 비교해 context gating을 한 모델 안 CMS 분기·controller로 구현한다는 점이 다르다.
- 대조 실험: 프로토타입 매칭 라우팅 arm(비모수)과 학습 gating의 비교, 주소 실패와 실행 실패를 가르는 wrong-schema swap.

**그림·표 계획.**

| 번호 | 내용 | 대응 주장 |
|---|---|---|
| Fig 1 | retrofit 구조(NMM 경로·CMS 분기·controller v0·write 정책 접점)와 프로세스 경계 | 전체 |
| Fig 2 | 표면×구조 2×2 전이와 관측 수별 곡선 [자리표시자] | C1-1 |
| Fig 3 | 정정 뒤 최초 과제 재평가와 ABA 재방문 [자리표시자] | C1-2 |
| Fig 4 | NP arm 대비 비교 [자리표시자] | C1-3 |
| Fig 5 | wrong-schema state swap과 swap-null [자리표시자] | C1-4 |
| Tab 1 | arm 정의표와 예산 일치 | 전체 |
| Tab 2 | UJ1 10단계의 arm별 통과와 계약 테스트 | C1-5 |
| Tab 3 | 주장별 결과 상태·등급·문구 | 전체 |

**타당성 위협.**

| 위협 | 내용 | 대응 |
|---|---|---|
| 외적 타당성 | 합성 world, 구조 family 1종, 소형 모델 1종, 부분 layer retrofit, 제한 seed. 부분 layer 결과를 전 층 성공으로 확대하지 않는다 | 범위 태그, 등급 2 문구 |
| 천장·바닥 | `base`나 `fixed`가 floor이거나 `ctx`가 ceiling이면 비교가 무의미하다 | dev에서만 난이도 조정, 통과 전 봉인 금지 |
| 학습 예산 일치 | arm 사이 학습·쓰기 예산이 어긋나면 비교가 무효다 | budget meter, 어긋나면 INVALID |
| 허용오차 | 장치·batch 구성이 바뀌면 출력이 달라진다 | noise floor [ν]를 재고 그보다 작은 허용오차를 약속하지 않음 |
| 이름만 같은 구현 | 간이 retrofit을 원본 재현이라 부를 위험 | 설계 차이와 생략된 학습을 기록 |
| 같은 base에서 NP arm 재실행 | NP 단(NP-0)이 작은 base에서 성립하지 않을 수 있다 | NP-1을 대조로 쓰고 성립하지 않은 단은 「없음」으로 기록(MD-1118-O) |

### 5-6. 필요 등급과 phase 상한이 어긋나는 경우: 두 안

PAPER-1이 앞세울 주장은 「구조 공유 새 사례에서 학습 모듈이 대조보다 낫다」(schema 이득)다. 이 문구는 등급 3부터 쓸 수 있는데 P1의 최대 등급은 2다([09-roadmap.md](../docs/09-roadmap.md) §3). MD-1118-P에 따라 두 안을 나란히 쓰고 사용자 결정 후보로 올린다(D-38).

| 구분 | (a) P1에 등급 3 조건을 채우는 작업을 더한다 | (b) pilot 문구의 논문으로 낸다 |
|---|---|---|
| 내용 | P1 안에서 봉인 manifest·fresh locked cohort·구조 family 2종 이상(lure 포함)·사전 명세 충분 seed·독립 검토를 모두 채운다. 구조 family를 1종에서 2종 이상으로 늘리는 것이 핵심이다 | P1의 상한 2를 유지한다. 구조 family 1종·소형 모델 1종·제한 seed라는 한계를 문구와 한계 절에 쓴다 |
| 쓸 수 있는 문구 | 「이 합성 family 둘·이 모델·이 seed 집합에서 같은 예산의 대조 대비 우위(PASS)」(범위 태그 필수) | 「이 pilot 범위에서 사전 명세 대조를 통과(미달)했다」와 구간 병기 |
| 쓸 수 없는 문구 | 「자연어 일반」·「다른 모델에서도」·「제품 효용」 | 「schema 이득」·「개선했다」·「일반화」·「빠른 판단 성립」·「계산 절감」 |
| 일정·비용 영향 | P2의 첫 확증 작업 일부(구조 family 확대·봉인·fresh cohort)를 P1로 당긴다. P1 범위와 계산이 늘고 docs/09 §3 상한표의 P1 행을 바꿔야 한다. 계산은 「PAPER-1 묶음표」에서 다시 산출한다 | 변화 없음. 확증은 PAPER-2가 맡는다 |
| 추천(PROPOSAL) | 사용자가 P1 논문에서 확증 문구를 원할 때 선택 | **기본.** 점진적 해상도(앞 phase의 시나리오를 회귀 gate로 두고 해상도를 올린다)와 현재 상한에 맞고 비용이 늘지 않는다 |

### 5-7. negative-result판

| 구분 | 내용 |
|---|---|
| 영어 제목 | Equal-Budget Controls Were Not Beaten: A Negative Pilot Result for Titans-Style Memory Retrofitted into a Small Language Model |
| 한국어 제목 | 같은 예산의 대조를 이기지 못했다: 소형 모델에 이식한 Titans식 기억의 음성 pilot 결과 |
| 주장 | 이 pilot에서 `full`은 `fixed`·`flat`·`always`나 P0의 NP arm과 구분되지 않았다. 병목을 write 정책, 학습 예산, retrofit 범위(부분 layer), 세계 난이도(ceiling·floor), controller 임계 중 어디에 두는지 분리해 보고한다. 학습 모듈은 같은 예산의 NP arm보다 나을 때만 필요하다는 원칙에 따라 NP를 유지하고, 학습 모듈 확대(P2) 전에 사용자 결정을 받는다([09-roadmap.md](../docs/09-roadmap.md) §7) |

### 5-8. 투고 후보와 앞 논문에 대한 의존

- **투고 후보(미확정).** 연 1회 ML 학회의 다음 회차(ICML 2027은 전체 논문 마감 2027-01-22로 P1 종료 전이라 맞추기 어렵다)와 상시 접수 TMLR, 평생 학습 계열(CoLLAs는 2027 공지 미확인) 중에서 고른다. 성격·마감은 조사 기록의 투고처 표(W2b §6).
- **앞 논문에 대한 의존.** PAPER-0의 NP arm(영구 대조군), 평가 harness, 세계 생성기, 상태 계약(P1-T01·T02·T03·T06·T07·T10·T12를 P0가 먼저 쓴다)에 의존한다. PAPER-0이 NP-1·NP-0의 성립 여부를 보고한 크기의 base에서만 같은 base 비교가 성립한다.

## 6. PAPER-2 (P2: 구조 family × depth) — 중간

P2의 제품은 같은 CLI에서 구조 family를 3종으로 넓히고 고정 depth 격자(`--depth`)를 더해 경험 전(S0)·후(SE)의 quality–compute 곡선을 처음 재고 P1의 핵심 대조에 대한 첫 한정 확증(등급 3)을 시도하는 제품이다(UJ2, [09-roadmap.md](../docs/09-roadmap.md) §5 P2). 앞 phase의 UJ1은 회귀 gate로 그대로 통과한다.

### 6-1. 제목과 논지

| 구분 | 내용 |
|---|---|
| 영어 제목 | Depth After Experience: Quality–Compute Curves over Structure Families in a Retrofitted Language Model |
| 한국어 제목 | 경험 이후의 깊이: retrofit 언어모델의 구조 family별 품질–계산 곡선 |
| 한 문장 논지 | 경험을 거친 뒤 구조를 공유하는 새 사례는 같은 정확도에 더 얕은 깊이·더 적은 총 계산으로 이르고, 깊이의 이득은 학습된 schema의 유무와 상호작용하는가를 구조 family 3종의 봉인 확증으로 시험한다(H-COMPUTE의 경험 효과. 통합(Sleep) 이후의 계산 절감은 P4 전까지 주장하지 않는다) |

### 6-2. 주장

| Ck-n | 주장(반증 가능) | 대응 실험 | 지표·대조 | 판정 규칙 형식 | 필요 등급 |
|---|---|---|---|---|---|
| C2-1 | 구조 family 3종(lure 포함)의 fresh sealed cohort에서 P1의 핵심 대조 우위(`full` 대 `fixed`·`flat`·`always`와 NP arm)가 유지된다(첫 한정 확증) | UJ2 `fcl eval` | C1-1·C1-2에 대응하는 전이·망각 지표 | A + B | 3 |
| C2-2 | 경험 전(S0)보다 경험 후(SE)에서 같은 정확도에 필요한 depth와 총 계산(encoder·core loops·write·backward 포함)이 줄어든다 | UJ2의 arm × depth, quality–compute 곡선 | 사전 지정 품질 [q*]에서 계산량 차이, 곡선 이동 | D | 3(봉인 확증을 거친 것만, 아니면 2) |
| C2-3 | 깊이 증가의 이득은 schema가 있는 조건(SE)과 없는 조건(S0)에서 다르다(깊이×schema 상호작용). 같은 입력의 단순 재호출이나 무의미한 loop 증가는 개선으로 세지 않는다 | depth 격자, 같은 FLOPs의 고정 깊이 대조, 재호출 대조 | 상호작용 항의 구간, depth별 FLOPs·p50/p95·TTFT·메모리 | A | 3 |
| C2-4 | 새 구조 사례에서 조작적 증거 2종(subspace 재사용, 변화량 감소)이 관찰된다. 봉인 확증을 거치지 않으면 관찰로만 쓰고 「schema 형성」이라는 말은 쓰지 않는다 | P2 조작적 증거 작업 | subspace 겹침, 새 사례당 state 변화량 | A | 3(아니면 2) |
| C2-5 | ET-0의 발견 수준 깊이 곡선에서 학습 arm이 같은 예산의 NP arm보다 낫다. ET-1 재분장은 탐색이다 | suite S-B 깊이 곡선, suite S-C | 발견 수준 곡선, 학습 arm 대 NP arm | A + B | ET-0 3 시도, ET-1 2 |

**문구.** 등급 3에서 쓸 수 있는 말은 「이 합성 family 셋·이 모델·이 seed 집합에서 대조군 대비 우위(PASS)」다. 규칙형 controller가 v0뿐이므로 「적응 계산」은 약속하지 않는다. 깊이 곡선이 봉인 확증을 거치지 않으면 등급 2다.

### 6-3. 초록

초록은 필요 등급(위 주장 표)을 채워 PASS한 경우의 문장이다. 등급에 못 미치는 주장은 「이 pilot 범위에서 관측했다」로, FAIL이면 §6-5의 negative-result판 문장으로 바꾼다.

**English abstract.** Deeper computation is usually evaluated on a fixed model, but whether experience changes how much computation a problem needs is a different question. We extend a retrofitted language model to a grid of fixed recursion depths and to three families of relational structure, and we measure quality-compute curves before and after experience, counting encoder, recurrent core, and write and backward costs in a single ledger. The study asks whether a problem that shares structure with earlier experience reaches the same accuracy at lower total cost, and whether the benefit of depth depends on the availability of a learned schema rather than on additional calls alone. Controls include fixed-depth models at matched compute, repeated invocation of the same input, and a non-parametric arm from the first stage run on the same base. Two operational indicators, reuse of an activation subspace and reduction of the change needed for a new case, are reported as evidence only if they survive a sealed confirmation on a fresh cohort. [Result placeholder: shift of the quality-compute curve after experience.] [Result placeholder: depth-by-schema interaction.] [Result placeholder: operational indicators under confirmation.] A synthetic micro-discovery depth curve compares the learned arm with the non-parametric arm. A learned controller, selective writing, and sleep are explicitly deferred, so adaptive computation is not claimed.

**한국어 초록.** 깊은 계산은 보통 고정된 모델에서 평가되지만 경험이 문제에 필요한 계산량을 바꾸는가는 다른 질문이다. retrofit 언어모델을 고정 recursion depth 격자와 관계 구조 family 3종으로 넓히고, 경험 전후의 품질–계산 곡선을 encoder·재귀 core·write·backward 비용을 한 원장에 넣어 잰다. 이전 경험과 구조를 공유하는 문제가 같은 정확도에 더 적은 총 계산으로 이르는지, 깊이의 이득이 추가 호출이 아니라 학습된 schema의 유무에 달린 것인지를 묻는다. 대조는 같은 계산의 고정 깊이 모델, 같은 입력의 반복 호출, 같은 base로 다시 돌린 앞 단계의 비모수 arm이다. 활성화 subspace 재사용과 새 사례당 변화량 감소의 두 조작적 지표는 새 cohort의 봉인 확증을 거친 경우에만 증거로 보고한다. [결과 자리표시자: 경험 뒤 품질–계산 곡선의 이동.] [결과 자리표시자: 깊이와 schema의 상호작용.] [결과 자리표시자: 확증을 거친 조작적 지표.] 합성 미시 발견 세계의 깊이 곡선으로 학습 arm과 비모수 arm을 비교한다. 학습된 controller·선택적 write·Sleep은 미루므로 적응 계산은 주장하지 않는다.

### 6-4. 실험 설계

| 항목 | 계획(PROPOSAL) |
|---|---|
| 실험 환경 (HW / SW / 모델 고정) | HW: 종료 gate는 host·노트북, 학습·배치 readout은 runcrate의 같은 장치 묶음(「PAPER-2 묶음표」). SW: P1의 CLI·runtime에 `--depth`, depth 시계(recursion index는 token 위치·경험 수를 늘리지 않음), causal mask·stale cache 검사, 배치 평가(`fcl eval`). 모델: P1과 같은 base(retrofit layer 확대는 전환마다 회귀 검사). recurrence retrofit 가능성 spike가 실패하면 depth 축은 P3로 이월하고 이 논문의 C2-2~C2-4는 쓰지 않는다 |
| 학습 data | train world: 구조 family 3종(앞 family는 회귀용으로 유지). depth별 adapter·중간 depth loss를 포함한 recurrence retrofit 학습(같은 학습 예산 안). 경험 입력은 test-time write |
| test data | fresh sealed cohort(봉인 뒤 생성), family별 lure 확대, F05·F06(예외·ABA) 확대, 보호 영역 대조(slow 동결 대 fast만 쓰기). 큰 모델+raw history 참고선은 대조군이 아니라 참고선이며 등급을 매기지 않는다 |
| 비교 대조 | baseline: P1의 대조 arm과 NP arm × depth 격자, 같은 FLOPs의 고정 depth, 동일 입력 재호출. ablation: retrofit layer 범위, write 예산 격자. 인과 개입: wrong-schema state swap을 depth별로 반복. 조작적 증거 2종은 별도 readout |
| 객관 증명 | 사전 명세와 봉인 → fresh cohort → 독립 evaluator 프로세스(후보가 evaluator·oracle·split을 수정하지 못하는 권한 분리). 시도 수·multiplicity 기록, seed × world 단위 통계, 계산량은 depth별 FLOPs·p50/p95·TTFT·메모리를 같은 단위로 원장에 기록. 후보 readout(F-CI)은 측정만이고 등급 2 상한 |

### 6-5. 선행 연구, 위협, negative-result판, 투고·의존

- **선행 연구와 차별점.** W2b 조사 §1-4를 따른다. looped·recurrent depth(A06·A07·A09·A13·A17: catalog), 소형 재귀 모델(Hierarchical Reasoning Model `A53`, Tiny Recursive Model `A54`), 잠재 looping 사전학습(Ouro `A52`), 프롬프트별 계산 최적 배분(`A55`), 연속 잠재 추론(Coconut `A56`)이 가장 가깝다. 이 논문이 다르게 주장하는 것은 깊이의 효용이 학습된 schema에 조건부라는 상호작용이며 배분 신호가 난이도가 아니라 익숙함이라는 점이다. 대조: 난이도 기반 배분 대 익숙함 기반 배분(같은 총 계산).
- **그림·표 계획.** Fig 1 depth 격자 구조와 depth 시계, Fig 2 S0·SE quality–compute 곡선 [자리표시자], Fig 3 깊이×schema 상호작용 [자리표시자], Fig 4 조작적 증거 2종 [자리표시자], Fig 5 ET-0 깊이 곡선 [자리표시자], Tab 1 family별 lure·보호 지표, Tab 2 depth별 비용 원장.
- **타당성 위협.** (i) 깊이 이득이 schema 유무와 무관하게 나오면 상호작용은 서지 못하고 일반 깊이 이득 논문이 된다. (ii) 쉬운 사례만 조기 종료한 평균을 계산 효율 개선으로 쓰지 않는다(난이도 층화). (iii) loop 수만 줄이고 gradient·검색·decoder 비용을 늘린 결과는 계산 개선이 아니다. (iv) 합성 family 3종·소형 모델 1종의 범위. (v) 시계 혼동(recursion·token·experience·optimizer·CMS).
- **negative-result판.** 영어 제목 Depth Without Schema: No Interaction Between Recursion Depth and Learned Structure in a Retrofitted Language Model / 한국어 제목 schema 없는 깊이: retrofit 언어모델에서 recursion 깊이와 학습된 구조 사이에 상호작용이 없었다. 주장: 깊이 이득이 S0와 SE에서 같거나 깊이 곡선이 같은 FLOPs의 고정 모델과 구분되지 않았다. 그 범위에서 「경험이 계산을 줄인다」를 주장하지 않는다.
- **투고 후보(미확정).** ML 학회의 다음 회차와 TMLR(W2b §6). 모델 구조·계산 효율 성격이라 표현학습·구조 계열 트랙이 맞는지는 공지 후 확인한다.
- **앞 논문에 대한 의존.** PAPER-1의 retrofit 모델·UJ1 회귀·NP arm(같은 base)·평가 harness. PAPER-0b의 ET 절차를 ET-0 깊이 곡선과 ET-1 탐색에 재사용한다.

## 7. PAPER-3 (P3: 학습된 controller·선택적 write·accommodation) — 중간

P3의 제품은 P1의 규칙형 controller v0를 학습된 controller로 바꿔 모델이 문맥·경험에 따라 스스로 고르게 하는 제품이다. 문맥 수준(어떤 구조를 적용·전환·조합·수정할지)과 실행 수준(어느 token·block·depth source, write 횟수·강도, 종료)의 controller, fit·친숙도와 결합한 선택적 write, accommodation을 넣는다(UJ3, [09-roadmap.md](../docs/09-roadmap.md) §5 P3).

### 7-1. 제목과 논지

| 구분 | 내용 |
|---|---|
| 영어 제목 | Learning When to Read, Write, and Think: A Learned Controller for Selective Writes and Accommodation in a Unified Model |
| 한국어 제목 | 언제 읽고 쓰고 생각할지 배우기: 통합 모델 안의 선택적 write와 accommodation을 위한 학습된 controller |
| 한 문장 논지 | 한 모델 안에서 학습된 controller가 읽기·쓰기·깊이를 함께 정할 때, 규칙형 v0·항상-쓰기·novelty-only·P0의 NP controller보다 같은 품질·같은 예산(controller 비용 포함)에서 선택적 write와 accommodation(분기·create)을 더 잘하는가를 시험한다 |

### 7-2. 주장

| Ck-n | 주장(반증 가능) | 대응 실험 | 지표·대조 | 판정 규칙 형식 | 필요 등급 |
|---|---|---|---|---|---|
| C3-1 | 학습된 controller는 고정 depth·novelty-only·learned early exit·random gate보다 같은 품질에서 controller 비용을 포함한 총 호출·계산이 적다. 쉬운 사례만 골라 평균 depth를 줄인 결과는 인정하지 않는다 | UJ3의 경로 trace와 예산, 난이도 층화 | cost-to-quality 곡선(층별), 결정 trace | D | 3 |
| C3-2 | fit·친숙도를 결합한 선택적 write gate는 항상-쓰기·surprise-only보다 같은 쓰기 예산에서 새 학습과 기존 보존의 쌍을 더 높인다. 무엇·어디·얼마나·언제로 분해한 ablation이 기여를 가른다 | write 정책 접점의 ablation | 새 학습 곡선과 기존 보존의 쌍, 쓰기 수 | A + B | 3 |
| C3-3 | 구조가 어긋난 사례(F04)에서 accommodation(분기·create)은 덮어쓰기·보류보다 기존 조건 보존과 새 구조 학습을 함께 높이고, 설명 불가·모호한 입력은 보류한다(F09) | 새 구조·불확실성 family | 판정 혼동행렬, 보존·학습의 쌍, 보류 정확도 | A + B | 3 |
| C3-4 | 학습된 controller는 P1의 규칙형 v0와 P0의 규칙형·CRP식 NP controller보다 낫다. 같거나 못하면 학습 모듈의 필요성을 주장하지 않는다(MD-1118-D) | 같은 base의 NP arm 재실행 | NP·v0 대비 C3-1~C3-3 지표 | A | 3 |
| C3-5 | 재분장 사례(ET-1)에서 학습 controller + accommodation은 NP arm·평면 기억보다 발견 수준이 높다(오염 probe 수치 병기). ET-2(컷오프 이후 실제 사례)는 탐색이다 | suite S-C, ET-2 소수 사례 | 발견 수준 곡선, 오염 probe | A + B | ET-1 조건부 3(재분장 family 2종 이상), ET-2 2 이하 |

**문구.** controller는 구성 요소이며 정답 oracle이 아니다. 동기 실행에서 단순 stage ID와 같은 효과이면 새 원리라고 부르지 않는다. 보호 family가 퇴행하면 자동으로 멈춘다.

### 7-3. 초록

초록은 필요 등급(위 주장 표)을 채워 PASS한 경우의 문장이다. 등급에 못 미치는 주장은 「이 pilot 범위에서 관측했다」로, FAIL이면 §7-5의 negative-result판 문장으로 바꾼다.

**English abstract.** Most memory systems for language models decide what to store and when to retrieve with fixed rules or with an external module, and the cost of the controller itself is often left out of the accounting. We replace the rule-based controller of an earlier stage with a learned controller inside the same model. It operates at two levels: the context level, which decides which structure to apply, switch, combine, or revise, and the execution level, which decides which positions and blocks to use, how many writes of what strength to make, and when to stop. Writes are gated by fit and familiarity, and a structural mismatch triggers accommodation, branching or creating a new unit rather than overwriting, or a hold when the input cannot be explained. We compare against the rule-based controller, against always-write and novelty-only writing, against a learned early-exit baseline and a random gate, and against the non-parametric controller from the first stage, at the same quality and the same total budget including controller cost, with difficulty stratification so that easy cases cannot lower the average. A protection family stops training automatically when preserved behavior regresses. [Result placeholder: total-cost comparison at equal quality.] [Result placeholder: selective-write comparison at equal write budget.] [Result placeholder: accommodation outcome.] Re-skinned historical archetypes provide an exploratory discovery readout with contamination probes reported. The controller is a component, not an oracle.

**한국어 초록.** 언어모델의 기억 시스템은 대개 무엇을 저장하고 언제 꺼낼지를 고정 규칙이나 외부 모듈로 정하며 controller 자체의 비용은 계산에서 빠지는 경우가 많다. 앞 단계의 규칙형 controller를 같은 모델 안의 학습된 controller로 바꾼다. 문맥 수준은 어떤 구조를 적용·전환·조합·수정할지를, 실행 수준은 어느 위치·block을 쓰고 어떤 강도로 몇 번 쓰며 언제 멈출지를 정한다. write는 fit과 친숙도로 gate하고 구조가 어긋나면 덮어쓰지 않고 분기하거나 새 단위를 만들며 설명할 수 없는 입력은 보류한다. 규칙형 controller, 항상-쓰기와 novelty-only, 학습된 early exit와 무작위 gate, 앞 단계의 비모수 controller를 같은 품질과 controller 비용을 포함한 같은 총 예산에서 비교하고, 쉬운 사례가 평균을 낮추지 못하게 난이도를 층화한다. 보존된 동작이 퇴행하면 보호 family가 학습을 자동으로 멈춘다. [결과 자리표시자: 같은 품질에서 총 비용 비교.] [결과 자리표시자: 같은 쓰기 예산에서 선택적 write 비교.] [결과 자리표시자: accommodation 결과.] 재분장한 역사 원형은 오염 probe를 병기한 탐색적 발견 readout을 준다. controller는 정답 oracle이 아니라 구성 요소다.

### 7-4. 실험 설계

| 항목 | 계획(PROPOSAL) |
|---|---|
| 실험 환경 (HW / SW / 모델 고정) | HW: P1·P2와 같은 규칙(종료 gate는 host·노트북, 학습·readout은 runcrate의 같은 장치 묶음, 「PAPER-3 묶음표」). SW: 결정이 관측 가능한 state에만 근거하는 router(아직 생성되지 않은 token을 참조하지 않음), controller·router 비용을 계산량에 포함하는 원장, 보호 family 자동 중단. 모델: P1·P2와 같은 base 한 종 |
| 학습 data | controller·write gate·accommodation을 학습하는 train world(구조 family 3종, 새 구조·불확실성·지연 피드백 일부(F04·F09·F08)). 평가 세계와 분리 |
| test data | fresh sealed cohort, 난이도 층화(쉬운 사례 층 분리), lure 확대. ET-1 재분장(오염 probe 병기)과 ET-2 소수 사례(탐색) |
| 비교 대조 | baseline: 규칙형 v0, 고정 depth, novelty-only, learned early exit, random gate, 항상-쓰기, P0의 NP controller. CMS 조율 계열 대조(고정 주기·frequency-adaptive·event/readiness; 위상 조율은 P3에서 다루지 않음). ablation: write gate를 무엇·어디·얼마나·언제로 분해, halting. 인과 개입: wrong-schema swap, 표현 제거·교체(조작적 증거 3종째) |
| 객관 증명 | 사전 명세·봉인·fresh cohort·독립 evaluator, 같은 품질에서의 사전 명세 비교(난이도 층별로도 방향 일치), 시도 수 기록, controller 비용 포함 total cost, 결정 trace 재현(저장·복원 뒤 같은 결정), 원장·manifest·harness 공개 |

### 7-5. 선행 연구, 위협, negative-result판, 투고·의존

- **선행 연구와 차별점.** W2b 조사 §1-5를 따른다. 외부 텍스트 기억의 갱신 판정(Janus `A57`, Memory-R1 `S87`, MINDSET `S53`)과 사용 방식 router(OMCE `S88`, Self-RAG `S89`, MemRL `S90`)가 가장 가깝다. 이 논문이 다르게 주장하는 것은 모델 내부 state의 write와 읽기·깊이를 같은 모델이 학습한다는 점(U05)이다. 비모수 Bayesian expert 증설(CN-DPM `A58`)과 편집·codebook 계열(GRACE `A59`)은 accommodation의 비교 대상이다.
- **그림·표 계획.** Fig 1 controller의 두 수준과 신호·출력, Fig 2 경로 trace와 cost-to-quality 곡선(층별) [자리표시자], Fig 3 write gate 분해 ablation [자리표시자], Fig 4 accommodation 판정 혼동행렬 [자리표시자], Fig 5 ET-1 곡선 [자리표시자], Tab 1 controller 입력·출력과 비용 원장, Tab 2 보호 family와 자동 중단 기록.
- **타당성 위협.** (i) 학습된 controller가 규칙 v0를 같은 예산에서 이기지 못할 수 있다(MD-1118-D). (ii) 쉬운 사례 선택과 평균 depth 감소의 혼동(난이도 층화로 통제). (iii) controller 자체 비용 누락. (iv) accommodation이 단순 stage ID와 같은 효과일 수 있다. (v) 모델 1종·합성 family.
- **negative-result판.** 영어 제목 A Learned Controller Does Not Beat a Rule at Equal Budget: Negative Results for Selective Writing and Accommodation / 한국어 제목 같은 예산에서 학습된 controller가 규칙을 이기지 못했다: 선택적 write와 accommodation의 음성 결과. 주장: C3-1~C3-4에서 학습 controller가 규칙형 v0·NP controller와 구분되지 않았고, 따라서 학습 모듈은 이 범위에서 필요하다고 주장하지 않는다.
- **투고 후보(미확정).** ML 학회의 다음 회차, TMLR, 평생 학습 계열(W2b §6; 2027 공지 미확인). Ali 공동논문(docs/14)과의 관계는 §11과 N-6.
- **앞 논문에 대한 의존.** PAPER-1·PAPER-2의 retrofit 모델·depth 격자·평가 harness, PAPER-0의 NP controller(대조), PAPER-0b의 ET 절차.

## 8. PAPER-4 (P4: Sleep·세션 간 경험·외부화) — 뼈대

먼 phase이므로 제목·논지·주장의 형식·초록 뼈대를 쓰고 실험 설계는 목표·gate·선택지·결정 대기로 쓴다. 모델 이름·규모·수치는 쓰지 않는다. P4의 제품은 경험이 세션을 넘어 남게 하는 제품이다(UJ4, [09-roadmap.md](../docs/09-roadmap.md) §5 P4): Sleep(fast → slow 공고화), 외부화 v0(bundle export/import·offload/reload·version lineage), 다세션 이력.

### 8-1. 제목과 논지

| 구분 | 내용 |
|---|---|
| 영어 제목 | Schemas Across Sessions: Sleep Consolidation and Externalization in a Unified Language Model |
| 한국어 제목 | 세션을 넘는 schema: 통합 언어모델의 Sleep 통합과 외부화 |
| 한 문장 논지 | 같은 경험 뒤 Sleep을 한 상태(SES)가 경험만 한 상태(SE)보다 세션 2의 구조 공유 새 사례를 더 적은 관측·더 적은 총 계산으로 풀고, 외부화한 versioned schema가 reload 뒤에도 판단과 후속 학습의 일관성을 지키는가를 같은 데이터·총 계산량의 replay-only·teacher 대조와 함께 시험한다 |

### 8-2. 주장의 형식

| Ck-n | 주장(형식) | 대응 | 판정 규칙 형식 | 필요 등급 |
|---|---|---|---|---|
| C4-1 | SES는 SE보다 세션 2의 새 구조 사례에서 필요한 관측 수와 amortized total 계산(Sleep·offload·warmup 비용 포함)이 적고, 같은 데이터·총 계산량의 replay-only·teacher distillation 대조를 이긴다. H-SAMPLE과 H-COMPUTE를 따로 판정한다 | UJ4, SE 대 SES | A + D | 3 |
| C4-2 | bundle export/import·offload/reload 뒤 판단과 후속 학습이 허용오차 안에서 일관되고 모델 revision 불일치·migration은 거부된다. stale index·계보 보존은 측정한다 | F12, 외부화 계약 테스트 | C(계약) + A | 계약 1, 효용 3 |
| C4-3 | Sleep 뒤 savings·세션 간 ABA·zero-shot 재평가에서 보존이 대조보다 낫다(보호 지표) | 세션 간 ABA | B + A | 3 |
| C4-4 | ET-1 재분장에서 Sleep 전후 발견 수준의 잠복 효과(미해결 불일치가 Sleep 뒤 재구조화로 이어지는가)가 같은 NP Sleep arm보다 크다. ET-2(컷오프 이후 실제 사례)는 판정 대상이나 기본 2이고, ET-3 pilot 대상은 탐색이다 | suite S-C, ET-2, ET-3 pilot | A + B | ET-1 조건부 3, ET-2 기본 2(3은 OPEN), ET-3 2 이하 |

**상한 문구.** 통합된 weights에서 개별 source 삭제가 완전하다고 약속하지 않는다(삭제 의존성은 측정해서 보고한다). 저장·재구성 성공을 판단 효용으로 해석하지 않는다. tensor shape·hash만 확인한 외부화는 통과로 보지 않는다.

### 8-3. 초록 뼈대

초록은 필요 등급(위 주장 표)을 채워 PASS한 경우의 문장이다. 등급에 못 미치는 주장은 「이 pilot 범위에서 관측했다」로, FAIL이면 §8-5의 negative-result판 문장으로 바꾼다.

**English abstract.** Experience that vanishes when a session ends cannot support lifelong learning. We add to a unified language model an offline consolidation phase, sleep, that moves fast, session-local changes into slower structures, and an externalization layer that exports, offloads, reloads, and versions schema artifacts across processes and sessions, with refusal of incompatible model revisions. In a command-line journey, a first session accumulates experience, a sleep step runs, the process ends, and a second session addresses new entities that share the earlier structure with fewer observations and shallower computation. We separate three questions: whether consolidation improves later learning and cost when the cost of sleep, offloading, and warm-up is included in an amortized total; whether externalized artifacts preserve judgments and later learning after reload; and whether preservation holds across sessions, including revisits of earlier conditions. Controls use the same data and the same total compute for replay-only and teacher distillation, a no-sleep variant, and a text-based sleep stand-in from the first stage. [Result placeholder: effect of consolidation on later learning and amortized cost.] [Result placeholder: reload consistency.] [Result placeholder: cross-session preservation.] Re-skinned historical archetypes probe latent effects of consolidation on discovery, with contamination reported. We make no guarantee that deletion of a single source holds in consolidated weights; its dependence is measured and reported.

**한국어 초록 뼈대.** 세션이 끝나면 사라지는 경험은 평생 학습을 지탱하지 못한다. 통합 언어모델에 fast·세션 국소 변화를 느린 구조로 옮기는 오프라인 공고화(Sleep)와 schema artifact를 프로세스·세션 사이에서 내보내고 offload·reload·version 관리하며 맞지 않는 모델 revision을 거부하는 외부화 층을 더한다. CLI 여정에서 세션 1이 경험을 쌓고 Sleep을 한 뒤 프로세스가 끝나고, 세션 2가 같은 구조의 새 개체를 더 적은 관측과 더 얕은 계산으로 푼다. 세 질문을 가른다. Sleep·offload·warmup 비용을 amortized total에 넣고도 공고화가 이후 학습과 비용을 개선하는가, 외부화한 artifact가 reload 뒤 판단과 후속 학습을 보존하는가, 이전 조건 재방문을 포함해 세션을 넘어 보존이 유지되는가. 대조는 같은 데이터·같은 총 계산량의 replay-only와 teacher distillation, Sleep 없음, 앞 단계의 텍스트 Sleep 대역이다. [결과 자리표시자: 공고화가 이후 학습과 amortized 비용에 준 효과.] [결과 자리표시자: reload 일관성.] [결과 자리표시자: 세션 간 보존.] 재분장한 역사 원형은 공고화의 발견에 대한 잠복 효과를 오염 보고와 함께 탐색한다. 통합된 weights에서 개별 source 삭제가 성립한다고 보장하지 않으며 삭제 의존성은 측정해 보고한다.

### 8-4. 실험 설계: 목표·gate·선택지·결정 대기

| 항목 | 내용 |
|---|---|
| 실험 환경 | 목표: 실제 sleep 학습·실제 저장·offload·reload·실제 프로세스 재시작의 UJ4. gate: UJ4 E2E와 UJ1~UJ3 회귀. 선택지: Sleep 실행 장치(host 대 runcrate, 「PAPER-4 묶음표」). 결정 대기: 계산 결정 D-04, 외부화 형식과 위치 |
| 학습 data | 목표: 다세션 이력과 같은 경험의 replay·teacher–student 학습. 선택지: replay 후보 선별(event/readiness 대 고정 주기), deep-to-shallow distillation 포함 여부. 결정 대기: replay 예산의 단위(호출·token·optimizer step) |
| test data | 목표: 세션 2의 fresh sealed 구조 사례, 세션 간 ABA, zero-shot 재평가, ET-1 잠복 사례, ET-2 소수 사례. 선택지: ET-2 사례 선정(공개 모델의 지식 마감이 확인된 것). 결정 대기: ET-2가 fresh locked cohort 조건을 채우는지(OPEN) |
| 비교 대조 | 같은 데이터·총 계산량의 replay-only와 teacher distillation, Sleep 없음(SE), 텍스트 Sleep-NP(P0), 고정 주기 대 event/readiness 공고화 시점 |
| 객관 증명 | 사전 명세·봉인·독립 evaluator, bundle manifest·hash·revision mismatch·rollback·migration 거부·세션 간 state 격리의 자동 테스트, SE 대 SES의 H-SAMPLE·H-COMPUTE 분리 판정. 결정 대기: 삭제 보장 범위(보장 없음 유지) |

### 8-5. 선행 연구, 위협, negative-result판, 투고·의존

- **선행 연구와 차별점.** W2b 조사 §1-6을 따른다. Sleep·공고화(Language Models Need Sleep A03, SoMem S36: catalog, 사전 계산 `A61`), 텍스트 기억의 야간 통합(DCPM `S92`, Hippo `S93`, Use and Disuse `S94`), 생성적 재생(`A62`)이 가장 가깝고, 외부화는 adapter·KV 아티팩트 계열(S-LoRA A32: catalog, LoraHub `A64`, Text-to-LoRA `A65`, Cartridges `A66`)이다. 다르게 주장하는 것은 schema 수준 Sleep의 이후 효과와 version·호환성 계약·삭제 의존성이다.
- **그림·표 계획(뼈대).** Fig 1 UJ4 여정과 Sleep·외부화 구조, Fig 2 SE 대 SES 곡선과 amortized 비용 [자리표시자], Fig 3 reload 일관성과 stale index [자리표시자], Fig 4 세션 간 ABA·savings [자리표시자], Tab 1 대조(replay-only·teacher)와 예산 일치, Tab 2 외부화 계약 테스트.
- **위협.** 저장된 생성물의 오류 고정(`S67`)이 Sleep 이득을 상쇄할 수 있다. 같은 데이터·총 계산량이 아닌 비교는 무효다. 삭제 완전성은 약속하지 않는다.
- **negative-result판.** 영어 제목 Sleep Does Not Beat Replay at Equal Compute: Negative Results for Schema Consolidation and Externalization / 한국어 제목 같은 계산에서 Sleep이 재생을 이기지 못했다: schema 통합과 외부화의 음성 결과. 주장: C4-1에서 SES가 replay-only·teacher 대조와 구분되지 않았다면 Sleep 이득 문구를 쓰지 않고 P4의 학습 Sleep 기준선이 높아졌다는 사실을 보고한다.
- **투고 후보(미확정).** ML 학회의 다음 회차, TMLR, 평생 학습 계열(W2b §6). Ali 공동논문(docs/14)의 Delete/Retain·Read/Activate 정책과 관련해 §11과 N-6.
- **앞 논문에 대한 의존.** PAPER-1~3의 모델·controller, PAPER-0의 텍스트 Sleep-NP(대조), PAPER-0b의 ET 절차(ET-1 잠복).

## 9. PAPER-5 (P5: 더 큰 모델·시간캡슐 기반 retrofit·실제 consumer) — 뼈대

P5의 제품은 검증된 범위를 넓히고 실제 consumer에 연결하는 제품이다(UJ5): 더 넓은 retrofit, 두 번째 base model, 자연어 혼합 도메인, 실제 agent의 session 접점 연결, 제한 운용. 모델 이름·크기·수치는 선택지와 결정 대기로만 쓴다.

### 9-1. 제목과 논지

| 구분 | 내용 |
|---|---|
| 영어 제목 | Scaling the Unified Model: Retrofit on Larger and Time-Capsule Bases with a Real Consumer |
| 한국어 제목 | 통합 모델 확대하기: 더 큰 base와 시간캡슐 base의 retrofit, 실제 consumer 연결 |
| 한 문장 논지 | 학습 모듈은 같은 예산의 NP arm보다 나을 때만 필요하다(MD-1118-D)는 판정이 두 번째 base·자연어 혼합 도메인·실제 consumer로 넓힌 범위에서도 유지되는지를 새 fresh cohort에서 확인하고, 시간캡슐 기반 retrofit의 pilot 발견 곡선은 개발 pilot 등급으로만 보고한다 |

### 9-2. 주장의 형식

| Ck-n | 주장(형식) | 대응 | 판정 규칙 형식 | 필요 등급 |
|---|---|---|---|---|
| C5-1 | 두 번째 base(크기 또는 계열이 다름)와 자연어 혼합 도메인의 새 fresh cohort에서 앞 논문의 핵심 우위가 유지된다 | UJ5 회귀와 복제 | A + B | 4 |
| C5-2 | 각 base에서 학습 모듈은 같은 base·같은 예산의 NP arm보다 낫다. 같거나 못하면 학습 모듈의 필요성 주장을 철회한다 | NP arm 재실행 | A | 4 |
| C5-3 | 실제 consumer(agent)가 같은 session 접점으로 경험·질문·정정·재시작 복원을 이어가며, 관측한 호출 coverage와 검증한 삭제 의존성 안에서 latency 분포·residency·offload warmup이 보고된다 | UJ5 | C + 측정 | 5(관측한 coverage 안) |
| C5-4 | 시간캡슐 기반에 retrofit한 시스템의 pilot 대상 발견 곡선을 대조 arm·대조 stream 대비 보고한다. pilot 대상은 개발에 노출되므로 상한 2이고 「발견했다」는 쓰지 않는다 | ET-3 | A + B(탐색) | 2 |

### 9-3. 초록 뼈대

초록은 필요 등급(위 주장 표)을 채워 PASS한 경우의 문장이다. 등급에 못 미치는 주장은 「이 pilot 범위에서 관측했다」로, FAIL이면 §9-5의 negative-result판 문장으로 바꾼다.

**English abstract.** Claims about a continual-learning module are only as strong as the models, domains, and consumers on which they were tested. We extend a unified language model along three axes: a second base model that differs in size or family, a natural-language mixed domain, and a real consumer, an agent that uses the system through the same session interface as the command line. The central question is whether a learned module continues to beat a non-parametric arm run on the same base under the same budget, since a learned module is needed only if it does. We replicate the earlier confirmations on a new fresh cohort, report operational measures such as latency percentiles, residency, offload warm-up, and deletion dependency within the call coverage we observed, and run a pilot discovery experiment on a time-capsule base to which the system has been retrofitted. [Result placeholder: replication of confirmed effects on a second base model and a mixed domain.] [Result placeholder: comparison with the non-parametric arm on each base.] [Result placeholder: operational measures within observed coverage.] The pilot discovery readout is limited to a development pilot because its target is exposed to development, so no discovery is claimed. We do not extend results from partially retrofitted layers to all layers, nor to call paths that we did not observe.

**한국어 초록 뼈대.** 지속학습 모듈에 대한 주장은 시험한 모델·도메인·consumer만큼만 강하다. 통합 언어모델을 세 축으로 넓힌다. 크기 또는 계열이 다른 두 번째 base, 자연어 혼합 도메인, 그리고 CLI와 같은 session 접점으로 시스템을 쓰는 실제 consumer(agent)다. 중심 질문은 학습 모듈이 같은 base·같은 예산으로 다시 돌린 비모수 arm을 계속 이기는가이며 이기는 경우에만 학습 모듈이 필요하다. 앞 논문의 확증을 새 fresh cohort에서 복제하고, 관측한 호출 coverage 안에서 latency 분포·residency·offload warmup·삭제 의존성을 보고하며, 시스템을 retrofit한 시간캡슐 기반에서 pilot 발견 실험을 한다. [결과 자리표시자: 두 번째 base와 혼합 도메인에서 확증된 효과의 복제.] [결과 자리표시자: 각 base에서 비모수 arm과의 비교.] [결과 자리표시자: 관측한 coverage 안의 운영 지표.] pilot 발견 readout은 대상이 개발에 노출되므로 개발 pilot 등급으로 한정하며 발견을 주장하지 않는다. 일부 layer만 retrofit한 결과를 전 층으로, 관측하지 않은 호출 경로로 확대하지 않는다.

### 9-4. 실험 설계: 목표·gate·선택지·결정 대기

| 항목 | 내용 |
|---|---|
| 실험 환경 | 목표: 실제 agent·실제 가중치·실제 write·저장·재시작·외부 consumer의 UJ5. gate: UJ5 E2E와 UJ1~UJ4 회귀, 모델 revision·tokenizer 계약, multi-user 격리, 삭제 의존성. 선택지: 두 번째 base의 크기·계열, 시간캡슐 기반 확보 방식(공개 모델 사용[기본] / 소형 자체 사전학습 / 중형 자체 사전학습)과 구현 위치. 결정 대기: D-12(두 번째 base), D-11(consumer 접점), 시간캡슐 기반 확보, 「PAPER-5 묶음표」 |
| 학습 data | 목표: 두 번째 base와 시간캡슐 기반에 대한 retrofit 학습과 자연어 혼합 도메인 경험. 선택지: 혼합 도메인의 구성, 시간캡슐 기반 retrofit의 학습 규모. 결정 대기: 자연어 도메인 data의 출처·라이선스 |
| test data | 목표: 새 fresh cohort(두 번째 base·혼합 도메인), 실제 consumer 과제, ET-3 pilot 대상. 선택지: consumer 과제 구성. 결정 대기: pilot 대상(docs/17의 추천 묶음에서 사용자가 결정) |
| 비교 대조 | 각 base의 NP arm, 외부 frozen LLM + RAG(consumer 접점의 대조군), 앞 논문의 대조 arm, ET-3의 대조 arm·대조 stream |
| 객관 증명 | 등급 4 readout(두 모델·자연어 혼합 도메인·새 fresh cohort의 사전 명세·봉인), 운용 coverage 보고, 독립 검토. 선택지: P5를 범위 확대와 연결·운용으로 나눌지(P4 종료 재검토). 결정 대기: 실험 B(Base와 post-training, [13-schema-decomposition-and-interference.md](../docs/13-schema-decomposition-and-interference.md) §10 B)를 P5에 둘지(N-5) |

### 9-5. 선행 연구, 위협, negative-result판, 투고·의존

- **선행 연구와 차별점.** W2b 조사 §1-7을 따른다. 기억·재귀·선형 RNN을 기존 LLM에 이식·증류하는 retrofit 계열(Titan-Llama A04, Retrofitted Recurrence A13: catalog, Mamba in the Llama `A67`)과 배포 지향 기억 표현(Cartridges `A66`, Sparse Memory Finetuning `A42`), 실서비스형 agent 기억(Mem0 `S74`, A-MEM `S73`, MemGPT `S75`)이 가장 가깝다. 시간캡슐 모델은 W2c 조사 기록이 소유한다.
- **그림·표 계획(뼈대).** Fig 1 확대 축(두 번째 base·혼합 도메인·consumer), Fig 2 복제 결과와 NP arm 대비 [자리표시자], Fig 3 운영 지표 분포(latency·residency·warmup) [자리표시자], Fig 4 ET-3 pilot 곡선(개발 pilot 등급) [자리표시자], Tab 1 관측한 호출 coverage와 삭제 의존성.
- **위협.** 부분 layer 결과를 전 층으로, 관측하지 않은 agent·model-call 경로를 포괄한다고 확대하는 오류. 개인 DB·native 권한 자동 활성화 금지.
- **negative-result판.** 영어 제목 When Learned Modules Fail to Beat Non-Parametric Memory at Scale / 한국어 제목 규모를 키워도 학습 모듈이 비모수 기억을 이기지 못할 때. 주장: C5-2에서 학습 모듈이 NP arm과 구분되지 않았으면 그 범위에서 학습 모듈의 필요성을 주장하지 않는다.
- **투고 후보(미확정).** ML 학회의 다음 회차, 시스템·agent 계열. 성격·마감은 W2b §6.
- **앞 논문에 대한 의존.** PAPER-1~4 전부, PAPER-0의 NP arm, PAPER-0b의 ET 절차.

## 10. PAPER-6 (P6(ET): 역사 ET 최종) — 뼈대

P6의 제품은 사용자가 CLI에서 기반 모델을 지정하고 인물 stream을 시간순으로 투입하며 checkpoint마다 발견 곡선을 보고 봉인 대상 판정 보고를 받는 제품이다(UJ6). 평가만 하는 phase가 아니라 입력 경로(READ·OBSERVE·NOTE·QUESTION·DISCUSS·TRY), 시간 필터·누수 감사, T0 이후 세계 지식의 지속학습 입력, 곡선 보고기를 갖춘 제품의 해상도 상승이다. 대상 묶음과 시간캡슐 기반의 선택은 [17-einstein-test.md](../docs/17-einstein-test.md)의 대상 묶음 절과 사용자 결정이 소유하고 여기서 이름을 고르지 않는다.

### 10-1. 제목과 논지

| 구분 | 내용 |
|---|---|
| 영어 제목 | Experience-Conditioned Discovery on Sealed Historical Targets |
| 한국어 제목 | 봉인된 역사 대상에서의 경험 조건부 발견 |
| 한 문장 논지 | 「T0까지의 세계 지식을 가진 기반 위에서, 한 인물의 경험 stream을 schema로 쌓고 미해결 불일치를 보존했다가 재조합·재구조화하는 시스템은, 같은 기반에 같은 자료를 기억 없이 또는 평면 기억으로 준 경우보다 (i) 더 적은 입력에서 (ii) 더 높은 발견 수준에 이르고, (iii) 그 차이는 stream의 내용에 특이적이다(대조 stream에서는 나오지 않는다).」 이 문장을 봉인 주력 대상 묶음에서 사전 명세 판정으로 시험한다. 「탐색」은 등급 2 이하로만 보고하고 「발견했다」는 이 범위 태그와 함께만 쓴다 |

### 10-2. 주장의 형식

| Ck-n | 주장(형식) | 대응 | 판정 규칙 형식 | 필요 등급 |
|---|---|---|---|---|
| C6-1 | 봉인 주력 대상 묶음·시간캡슐 기반·입력 tier에서 사전 명세 판정 PC-1~PC-10([17-einstein-test.md](../docs/17-einstein-test.md) §10.1)을 통과한다. 통과 문구는 범위 태그가 붙은 문장뿐이다 | UJ6 ET-4 | docs/17 §10.1의 형식(값은 봉인 전 확정) | 3(4는 OPEN) |
| C6-2 | 대조 stream(없음·순서 섞기·같은 시기 비발견자·무관 인물·핵심 입력 제거)에서는 같은 곡선이 나오지 않는다(H-DISCOVER의 stream 특이성) | 대조 stream 곡선 | A | 3 |
| C6-3 | 최초 발견 시점이 같은 기반의 기억 없음·평면 기억·NP arm보다 이르고 최고 수준·곡선 아래 면적이 높으며 입력 내재 수준을 넘는다 | 발견 곡선 지표 | A + B | 3 |
| C6-4 | 누설 제거 변형에서도 C6-1~C6-3이 성립하고 오발견율과 새로움 검사(기반의 지식 W에서 검색되지 않음)를 통과한다 | 누수 감사, 새로움 검사 | B | 3 |

**문구 규칙.** 「아인슈타인 테스트를 통과했다」는 쓰지 않는다(공개된 실행 절차가 없는 시험을 운영 정의로 바꿔 시험하는 것이므로). 쓸 수 있는 말은 「이 대상 묶음·이 시간캡슐 기반·이 입력 tier에서 사전 명세 ET-4 판정을 통과했다(대조 stream 대비 특이적, 입력 내재 수준 초과)」까지다. 대상이 한두 개이고 구성요소가 중도 절단되면 INCONCLUSIVE가 정직한 결과일 수 있다. 사용자 확인 후보는 D-34와 D-45다.

### 10-3. 초록 뼈대

초록은 필요 등급(위 주장 표)을 채워 PASS한 경우의 문장이다. 등급에 못 미치는 주장은 「이 pilot 범위에서 관측했다」로, FAIL이면 §10-5의 negative-result판 문장으로 바꾼다.

**English abstract.** We ask whether a system that knows the world up to a historical date and then receives one person's experience stream in time order reaches a later discovery earlier and at a higher level than the same base given the same material without memory or with flat memory, and whether this difference is specific to the content of the stream. The system is a unified, retrofitted model built on a time-capsule base, and the world after the cutoff enters as continual-learning input rather than through retraining. We evaluate on a sealed bundle of historical targets chosen by pre-registered criteria, using input tiers that separate dated primary sources from reconstruction and plausible synthesis, control streams that remove, shuffle, replace, or ablate the stream, an input-inherent level that separates repetition from going beyond the input, per-item leakage scoring, and a leakage-removed variant. Blind raters score neutral probes at pre-registered checkpoints on a shared scale. [Result placeholder: verdict of the pre-specified decision rule on the sealed targets.] [Result placeholder: discovery curves against control streams.] [Result placeholder: first-discovery point and highest level against memory-free and flat-memory arms.] [Result placeholder: robustness under leakage removal.] A positive verdict is reported only with the scope tags of target bundle, base model, and input tier, and it is not described as passing a general test.

**한국어 초록 뼈대.** 어떤 역사적 시점까지의 세계 지식을 가진 시스템이 이후 한 인물의 경험 stream을 시간순으로 받을 때, 같은 자료를 기억 없이 또는 평면 기억으로 받은 같은 기반보다 더 일찍 더 높은 수준의 발견에 이르는지, 그 차이가 stream의 내용에 특이적인지를 묻는다. 시스템은 시간캡슐 기반 위에 retrofit한 통합 모델이고, 컷오프 이후의 세계는 재학습이 아니라 지속학습 입력으로 들어간다. 사전 등록한 기준으로 고른 봉인 역사 대상 묶음에서 평가하며, 날짜 있는 1차 사료·재구성·그럴듯한 합성을 가르는 입력 tier, stream을 없애거나 섞거나 바꾸거나 핵심 입력을 제거하는 대조 stream, 되풀이와 초월을 가르는 입력 내재 수준, 항목별 누설도 채점, 누설 제거 변형을 쓴다. 맹검 채점자가 사전 등록한 checkpoint의 중립 probe를 같은 척도로 채점한다. [결과 자리표시자: 봉인 대상에서 사전 명세 판정 규칙의 결과.] [결과 자리표시자: 대조 stream 대비 발견 곡선.] [결과 자리표시자: 기억 없음·평면 기억 대비 최초 발견 시점과 최고 수준.] [결과 자리표시자: 누설 제거 아래의 강건성.] 긍정 판정은 대상 묶음·기반 모델·입력 tier의 범위 태그와 함께만 보고하며 일반적인 시험의 통과로 서술하지 않는다.

### 10-4. 실험 설계: 목표·gate·선택지·결정 대기

| 항목 | 내용 |
|---|---|
| 실험 환경 | 목표: 사용자가 CLI에서 기반 지정 → 인물 stream 시간순 투입 → checkpoint 곡선 → 봉인 대상 판정 보고를 끝까지 돌리는 UJ6, UJ1~UJ5 회귀. 선택지: 시간캡슐 기반 확보 방식(공개 모델 사용[기본] / 소형 자체 사전학습 / 중형 자체 사전학습), host 재현 가능 크기 여부. 결정 대기: 확보 방식·구현 위치, 「PAPER-6 묶음표」 |
| 학습 data | 목표: retrofit 학습은 P5까지의 가중치를 쓰고 대상 stream은 test-time 경험 입력이다. T0 이후의 세계 지식 W(T0..t)는 기반을 재학습하지 않고 지속학습 입력으로 넣는 안을 기본으로 검토한다. 선택지: W(T0..t)의 출처와 입력 tier. 결정 대기: 사료 접근·라이선스, 구성자와 개발자의 역할 분리 |
| test data | 목표: 봉인 주력 대상 묶음과 봉인 stream·probe 은행·rubric·누설 어휘 사전. 선택지: 대상 묶음(추천 묶음과 대안은 docs/17). 결정 대기: 대상 선정과 T0·T1(사용자 결정), 봉인 범위(docs/17 §11.4) |
| 비교 대조 | 같은 기반의 기억 없음·평면 기억·NP arm, 대조 stream, 입력 tier 셋, 누설 변형, 핵심 입력 제거 |
| 객관 증명 | 사전 명세 PC-1~PC-10, 맹검 2인 이상과 일치도, 구현자와 다른 독립 검토, 새로움 검사, 통계 단위는 대상·구성요소, 봉인 해시. 선택지: 4를 목표로 두 번째 시간캡슐 기반과 두 번째 봉인 묶음을 더할지(D-34). 결정 대기: 공개물의 범위(stream 원문 재배포 금지) |

### 10-5. 선행 연구, 위협, negative-result판, 투고·의존

- **선행 연구와 차별점.** W2b 조사 §1-8을 따른다. Einstein test 제안·시간캡슐 모델은 W2c 조사 기록이 소유한다. 제한 지식 모델의 개념 발견(`S96`), 학습 데이터와 발견 능력의 관계(`S97`), 개념 재편의 기하 신호(`S98`), 표현 구성의 병목(`S99`), 경쟁 설명 집합(`S100`), AI 과학자 시스템의 발견 주장(Kosmos `E07`, Co-Scientist `E08`)이 가깝다. aha 자기보고 신호가 통찰의 증거가 아니라는 분석(`S61`)에 따라 rubric과 객관 하위 과제로 채점한다.
- **그림·표 계획(뼈대).** Fig 1 UJ6 절차와 봉인 범위, Fig 2 대상별·구성요소별 발견 곡선과 대조 stream·입력 내재 곡선 [자리표시자], Fig 3 입력 tier별 곡선 [자리표시자], Fig 4 핵심 입력 제거와 누설 제거 변형 [자리표시자], Tab 1 판정 PC-1~PC-10의 결과, Tab 2 새로움 검사.
- **위협.** 대상이 적다(통계 단위가 대상·구성요소), 단일 기반, stream 재구성의 불확실성, 사후 편향의 잔존, 인물 사료의 편중, 시간캡슐 모델 자체의 누수. 사료 공백과 저작권.
- **negative-result판.** 영어 제목 No Content-Specific Discovery: A Negative Result for Experience-Conditioned Discovery on Sealed Historical Targets / 한국어 제목 stream 내용에 특이적인 발견은 없었다: 봉인 역사 대상에서의 경험 조건부 발견의 음성 결과. 주장: 대조 stream에서도 같은 곡선이 나오거나 입력 내재 수준을 넘지 못했다면 H-DISCOVER의 (iii) 또는 (ii)를 기각한 것이고 시스템의 이득이 아니라 풍토나 입력 양의 효과로 읽는다.
- **투고 후보(미확정).** ML 학회, 상시 접수 TMLR, 학술지(성격·분량은 확인하지 못한 것이 있어 W2b §6의 미확인 항목을 따른다). 제목에 「Einstein」을 쓸지는 D-45.
- **앞 논문에 대한 의존.** PAPER-0b의 절차와 benchmark, PAPER-5의 시간캡슐 기반 retrofit(ET-3 pilot 곡선), PAPER-0~4의 NP arm·대조.

## 11. docs/14 §7 Ali 공동논문 초안과의 대응표

[14-schema-lifecycle-crud-and-joint-paper.md](../docs/14-schema-lifecycle-crud-and-joint-paper.md) §7은 Ali 공동논문 제안의 흐름 6항목이고 §8은 결정적 실험이다. 그 제안문 초안은 **미발송**이며 이 계획은 그것을 바꾸지도 보내지도 않았다. 아래 대응은 이 계획의 논문이 그 항목을 어디서 다루는지만 보인다. 대응된다고 해서 공동논문 상한이 올라가는 것은 아니다. docs/14의 2026-11-17 OPEN 점검(공통 단위는 가설, 정책 공동학습은 로드맵 밖, retention 추정기는 미검증, MIRAS는 관점 연결 가설로만, 전체 저장 자원 일치는 budget meter에 없음)을 그대로 따른다.

| docs/14 §7 항목 | 내용 | 이 계획의 대응(논문·주장) | 해상도와 상한 |
|---|---|---|---|
| 1. 문제 | 간섭·보존 비용·접근 비용을 동시에 해결해야 하는 장기 경험 학습 | PAPER-0의 C0-2(간섭)·C0-5(보존)·C0-3(접근)의 NP판, PAPER-3·PAPER-4에서 학습 모듈로 | 등급 3 이하. 이 세 비용의 분리는 설계 후보 |
| 2. 공통 단위 | task별 adapter가 아니라 여러 과제에 재사용할 low-rank schema expert | 단위의 형태는 P1에서 NMM·CMS(PAPER-1)로 시작하고, 새 용량 할당은 accommodation(PAPER-3 C3-3), version 단위는 외부화(PAPER-4 C4-2)에서 만난다 | docs/14의 점검에 따라 「가설(low-rank expert, schema 후보)」이며 재사용·기능적 역할·학습 효용이 확인되기 전에는 schema라 부르지 않는다 |
| 3a. 선택적 쓰기·용량 할당 | 정책 1 | PAPER-3 C3-2(선택적 write)·C3-3(accommodation), PAPER-0 C0-4(NP 생명주기) | 등급 3 이하 |
| 3b. 기능 손실 기반 retention | 정책 2 | PAPER-0 C0-5의 eviction(F22는 사용자 결정 N-5 대기), PAPER-4 C4-1·C4-3 | 추정기가 미검증이므로 설계 후보. 폐기·삭제 보장 없음 |
| 3c. 문맥 기반 addressing/activation | 정책 3 | PAPER-0 C0-3(context gating·wrong-schema swap), PAPER-1 C1-4, PAPER-3 | 등급 3 이하 |
| 4. 선행연구 접점 | Nested Learning의 다중 학습 수준과 MIRAS의 retention 관점 | PAPER-1의 선행 연구 절(A02, A31: catalog) | MIRAS의 retention은 순환 memory 갱신의 gate이며 schema·artifact 단위의 보존 예산이 아니다. 「관점을 연결한다」는 가설로만 쓴다 |
| 5. 공동 연구 질문 | 기존 expert의 수정 가능 조건, 기능 거리와 분화·압축 기준, 정책 공동학습 | 탐색 후보(일정 없음): PAPER-3·PAPER-4의 후속 질문. 정책 공동학습은 로드맵 밖의 장기 질문 | 이 계획에 주장을 두지 않는다 |
| 6. 검증 | task ID 없는 구조 전이·재방문·새 관계, 동일 활성/전체 자원 비교 | PAPER-0 C0-1·C0-2·C0-7(NP), PAPER-1 C1-1·C1-2, PAPER-2 C2-1, 자원 일치는 PAPER-2·3의 total cost | 전체 저장 자원의 일치는 budget meter에 없어 범위를 적는다. 결과는 합성 family·소형 모델 범위 |

docs/14 §8의 결정적 실험은 [09-roadmap.md](../docs/09-roadmap.md) §6-1이 이미 기존 phase의 판독으로 배치했다. 이 계획의 논문에서는 다음 자리에 놓인다.

| docs/14 §8 | 이 계획의 자리 | 비고 |
|---|---|---|
| CU(같은 구조·새 개체, 같은 개체·새 구조, 잡음, 독립 정정, ABA) | PAPER-0 C0-1·C0-2(NP판), PAPER-1 C1-1·C1-2, PAPER-2 C2-1 | 새 학습과 무관한 조건의 회귀를 함께 잰다 |
| D(같은 저장 예산의 보존 정책 비교) | PAPER-0 C0-5(eviction, F22 승인 대기), PAPER-4 | 「삭제」는 기능적 망각/보존이며 source 삭제(C0-5의 계약, C1-5)와 다르다 |
| R(oracle 선택·learned gate·random gate·stale index) | PAPER-0 C0-3, PAPER-3 C3-3, PAPER-4 C4-2의 stale index | 선택 오류 지표(F23)는 승인 전 보조 |
| Joint(전체 파라미터·optimizer·버전·index·replay·학습·통합 계산 합산) | PAPER-2 C2-2·C2-3, PAPER-3 C3-1(total cost에 controller 비용 포함) | docs/13 실험 C와 합침 |
| System ONE(controller 우회 depth×update 품질 곡선, 이후 learned routing) | PAPER-2 C2-2·C2-3, PAPER-3 C3-1 | docs/13 실험 E와 같은 실험 |
| 추가 Read 대조군(schema-only 대 원본 근거 확인 가능한 Read) | PAPER-0의 대조 arm 후보 | PROPOSAL. 외부 agent memory의 검증을 neural schema 학습의 증거로 취급하지 않는다 |

Ali가 관심 있다고 전해진 loop transformer·MoD·MoR·depth attention 축(U-T09)은 docs/14의 제안문 초안에 없다. 이 계획에서는 PAPER-2의 depth 축과 겹치지만 공동논문에 넣을지는 사용자 판단이다(**OPEN**, N-6).

## 12. 「schema로 LLM과 System ONE을 함께 설명한다」는 사용자 가설의 논문별 증거 수준

**가설의 원문과 지위.** 사용자의 해법 개념과 가설은 [2026-11-schema-user-verbatim.md](../sources/sync/2026-11-schema-user-verbatim.md)의 USER 원문에 있고, 「LLM은 schema가 분리되지 않고 엉켜 학습되었고 그 간섭이 재앙적 망각을 낳으므로 분해된 형태의 지속학습이 망각을 없애거나 늦춘다」는 **USER-HYPOTHESIS**다. 과학적 입증이 아니라 사용자의 검증 대상 가설이다. [13-schema-decomposition-and-interference.md](../docs/13-schema-decomposition-and-interference.md) §1의 검토는 핵심을 중첩 제거에서 유해한 변경 간섭의 제어로 고쳤고 post-training 전체를 schema 분리 하나로 설명하는 것은 확정 결론이 아니라 경쟁 가설이라고 적었다. feature와의 연결(BF-B3·B4·E1·G4)은 [16-ideal-blueprint.md](../docs/16-ideal-blueprint.md) §7.2에 있다. 망각은 없앤다고 약속하지 않고 늦추는 데까지만 쓴다.

| 논문 | 다루는 부분 | 증거의 종류 | 최대 증거 수준 | 쓸 수 있는 문구 | 다루지 못하는 것 |
|---|---|---|---|---|---|
| PAPER-0 | 분해 기억 대 단일 기억의 간섭(NP 기억 구조 수준, C0-2), schema artifact의 분리·합성(C0-11), frozen LLM 내부 schema 중첩의 무학습 관찰(C0-13, 선택) | 합성 world의 상대 효과와 인과 개입(wrong-schema swap), 관찰 | C0-2·C0-11 3 시도, C0-13 2 이하 | 「이 기억 구조에서 분해 기억이 평면 기억보다 간섭이 작았다」, 「관찰했다」 | 가중치 수준의 간섭, LLM이 엉킨 schema라는 가설의 입증 |
| PAPER-0b | 해당 없음(ET 절차는 schema 가설의 시험이 아니다) | — | — | — | — |
| PAPER-1 | 공유 상태와 분리 상태의 얇은 비교(`always`·`flat` 대 `full`) | 합성 world의 상대 효과 | 2(두 안 (a)면 3) | 「이 pilot 범위에서 관측했다」 | 공유 파라미터를 갱신하는 arm(`ftall`)과 task별 oracle adapter(`adapters`)가 arm 표에 없어 docs/13 실험 A·C의 핵심 비교는 하지 못한다(새 arm은 N-5 결정 대기) |
| PAPER-2 | 중첩·관계 충돌·공유 파라미터 변경의 독립 조작(docs/13 실험 A), 계산 효율(실험 E) | 인과 분리 실험(공유 표현·선택적 update·분리 표현·oracle gate·학습 gate·무작위 분할) | 3 | 「이 합성 family·이 모델에서 공유 표현·선택적 변경이 보호한다(또는 단순 격리와 같다)」 | LLM 사전학습 단계의 중첩, post-training의 효과 |
| PAPER-3 | 선택·변경 경계를 경험에서 학습한다는 최종 명제(docs/13 §11)의 학습 controller판 | 학습 controller와 accommodation의 같은 예산 비교 | 3 | 「학습된 경계가 규칙형보다 나았다(또는 아니었다)」 | 경계 학습이 LLM의 중첩과 같은 현상이라는 해석 |
| PAPER-4 | artifact 재사용·기능 보존·offload/reload(docs/13 실험 D), 용량·지속학습 일부(실험 C) | 외부화 계약과 세션 간 보존 | 3 | 「reload 뒤 판단이 일관되었다」 | 망각을 없앤다는 주장(유한 용량의 한계, docs/13 §7.5), 개별 source 삭제 보장 |
| PAPER-5 | Base와 post-training의 비교(docs/13 실험 B)는 P5 이후이며 docs/09 P5의 「미루는 것」과 충돌해 사용자 결정(N-5). 두 번째 base에서 앞 결과의 복제 | 두 base 복제 | 4 | 「확장한 범위에서도 유지」 | post-training이 schema를 분화했다는 가설(실험 B 없이는 시험하지 않음) |
| PAPER-6 | 해당 없음(ET-4는 H-DISCOVER를 시험하며 schema 가설의 시험이 아니다) | — | — | — | — |

**증거의 사다리.** (1) 무학습 관찰(PAPER-0, 2 이하) → (2) NP 기억 구조 수준의 인과(PAPER-0의 C0-2·C0-3, 3 시도) → (3) 소형 retrofit 모델 안의 인과 분리(PAPER-2, 3) → (4) 모델 사이의 base 대 post-training(PAPER-5의 실험 B, 결정 대기, 4). 「schema로 LLM과 System ONE을 함께 설명한다」는 설명 틀로서의 가설이며 어느 논문에서도 입증으로 쓰지 않는다.

## 13. 사용자 결정 후보 (번호는 docs/09 §10의 결정 번호)

형식은 [09-roadmap.md](../docs/09-roadmap.md) §10 결정표의 열을 따른다. 다른 문서의 후보와 겹치면 docs/09 §10에서 한 행으로 합쳐져 있어 번호가 같을 수 있다([id-map.tsv](../research/2026-11-18-blueprint-et-design/id-map.tsv)). 비용 칸은 새로 생기는 비용의 유무만 쓴다(금액은 「PAPER-k 묶음표」).

| ID | 결정 | 선택지 | 추천 | 비용 발생 | 결정자 |
|---|---|---|---|---|---|
| D-38 | 선택 논문 PAPER-0b를 낼지와 시점 (ET 절차·benchmark를 P0 직후 따로 낼지) | (a) P0 직후 별도 논문 (b) PAPER-6과 합쳐 한 편 (c) 내지 않고 docs/17만 유지 | (a). 공개된 절차가 없다는 점 때문에 P0 직후에 낼 수 있는 동반 논문 후보다 | 추가 계산은 PAPER-0과 공유(「PAPER-0b 묶음표」), 구성자 작업 시간 | 사용자 |
| D-38 | PAPER-1의 필요 등급(3)과 phase 상한(2)의 어긋남 처리 (MD-1118-P의 두 안) | (a) P1에 등급 3 조건을 채우는 작업을 더한다 (b) pilot 문구의 논문으로 낸다 | (b). 점진적 해상도와 현재 상한에 맞고 비용이 늘지 않는다 | (a)는 P1 범위·계산 증가(「PAPER-1 묶음표」), (b)는 없음 | 사용자 |
| D-42 | 논문 단위 정책: phase마다 1편을 고정할지 | (a) 고정 (b) 인접 phase를 합본 (c) 일부 phase는 기술 보고로 대체 | (a)로 시작하고 phase 종료 재검토에서 조정 | 없음 | 사용자 |
| D-42 | PAPER-0의 범위: 한 편으로 쓸지 둘로 나눌지 (14개 주장이 넓다) | (a) 한 편 (b) 둘로 분리(구조 전이·간섭·생명주기 / 경로·Sleep·발견·잠재 artifact) | 계획은 한 편으로 쓰고 V0 결과를 본 뒤 분리를 결정 | 없음 | 사용자 |
| D-41 | 사전 등록(manifest hash)의 공개 시점 | (a) 봉인 때 hash만 공개 (b) 제출 때 공개 (c) 결과 공개 후 | (a). 내용은 제출 때. 외부 공개 행위이므로 승인 필요 | 없음 | 사용자 |
| D-43 | 핵심 주장이 FAIL일 때 negative-result판을 낼지 | (a) 항상 낸다 (b) 핵심 주장 FAIL만 낸다 (c) 내부 기록만 | (b). 투고처는 별도 결정 | 작성 시간 | 사용자 |
| D-44 | 논문 공개물의 범위 | (a) 세계 생성기·평가 harness·manifest·원장 요약·stream 목록과 해시 (b) a + retrofit 가중치 (c) 공개하지 않음 | (a). 사료 원문·비공개 경로 제외. 가중치는 별도 결정 | 없음 | 사용자 |
| N-6 | Ali 공동논문(docs/14)과 PAPER-3·4의 관계: 공저·역할·시점 | (a) PAPER-3·4를 공동논문 후보로 두고 제안문 수정안을 승인한 뒤 사용자가 발송을 판단 (b) 독립 진행 (c) 보류 | (c) 보류. 발송은 사용자 결정이며 이 계획은 발송하지 않았다. loop·MoD·MoR 축(U-T09)을 넣을지도 함께 | 없음 | 사용자 |
| N-5 | 실험 B(Base와 post-training)를 P5와 PAPER-5에 둘지 | (a) P5에 둔다(docs/09 P5의 「미루는 것」을 고친다) (b) P5 이후로 미룬다 | (b). 현재 로드맵을 유지. docs/13의 OPEN과 같은 쟁점 | (a)는 post-training 분기·RL의 시도 횟수가 비용이라 견적하지 않음 | 사용자 |
| D-45 | 논문 제목에 「Einstein」을 쓸지와 「통과」 문구 정책 (D-34와 겹침) | (a) 쓰지 않는다 (b) 「Einstein-style」 수식어만(PAPER-0b 작업 제목) (c) 제한 없이 | (b)는 PAPER-0b에만, PAPER-6 제목은 (a). 「통과했다」는 쓰지 않는다 | 없음 | 사용자 |
| D-41 | preprint 공개 시점 (외부 게시) | (a) 투고와 동시 (b) 결과 확정 뒤 (c) 하지 않음 | 사용자 결정. 어느 쪽이든 승인 전에는 게시하지 않는다 | 없음 | 사용자 |

## 14. 위험과 한계

| 위험 | 내용 | 대응 |
|---|---|---|
| 계획과 실행의 격차 | 모든 논문의 실험은 NOT RUN이다. 주장은 반증 가능하게 썼지만 실행하면 달라질 수 있다 | 판정 규칙의 확정 시점을 봉인 전으로 고정하고 결과를 본 뒤 고치지 않는다 |
| PAPER-0의 등급 3 시도 | 등급 3 시도는 P0 종료 gate가 sealed readout을 포함하는 결정(D-18)에 의존한다. 포함하지 않으면 PAPER-0의 대부분 주장은 2로 내려간다 | 결정 전에는 PAPER-0을 pilot 문구로 준비하고 결정 뒤 등급을 확정 |
| 등급 상한 초과 문구 | 논문 문구가 phase·ET 단 상한을 넘을 수 있다 | 문구 규칙과 보고 생성기의 금지 문구 검사기(P1-T12), 단별 표(docs/17) |
| 선행 연구의 변동 | 2026-06 이후 심사 전 preprint가 많다 | 제출 4주 전 재조회 gate(D-40) |
| 앞 논문 결과에 대한 의존 | PAPER-1 이후는 P0의 NP arm 성립 여부(NP-0·NP-1)에 의존한다 | 성립하지 않은 단은 「없음」으로 기록하고 성립한 단만 대조로 쓴다 |
| negative 결과가 많을 수 있음 | 이전 연구에서 단순 대조가 강했다(ARCHIVE) | 각 논문에 negative-result판을 준비했고 FAIL을 소급 PASS로 바꾸지 않는다 |
| 논문 수와 비용 | 논문이 여덟 편이다 | 「PAPER-k 묶음표」에서 논문별 비용을 보고 PAPER-0b·PAPER-5·PAPER-6은 결정 후 단계적으로 진행 |
| 산출물 재사용의 중복 | 세계 생성기·arm·harness를 여러 논문이 공유한다 | 공유 산출물을 인용하고 새 결과만 주장한다. 같은 결과를 두 논문에 나눠 쓰지 않는다 |
| 공개 안전성 | stream 원문·비공개 경로·계정 정보가 논문 공개물에 섞일 수 있다 | D-44의 공개 범위, 사료 원문 재배포 금지 |

---

**조사 기록:** 초안 끝의 색인(정의 위치와 초안의 가칭), 새 참고문헌, 조사 출처는 [doc19-appendices.md](../research/2026-11-18-blueprint-et-design/doc19-appendices.md)에 있다. 작업 방법, 마스터 결정, 사용자 결정 대기, NOT RUN 선언은 [2026-11-18-blueprint-et-design.md](../research/2026-11-18-blueprint-et-design.md)에 있다.
