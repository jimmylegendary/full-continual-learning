# 09. 단계별 MVP: 처음부터 전체 여정을 돌리고 해상도를 높이는 로드맵

**상태 라벨:** 이 로드맵 전체는 **PROPOSAL**이다. phase 경계, 작업 단위, seed 수, 예산, base model, 통계 방법은 사용자가 승인한 값이 아니며 구현·실행 완료를 뜻하지 않는다. 사용자가 명시한 제약(**USER**)은 §1.1에 날짜와 함께 따로 적었다. 문헌 주장(**LITERATURE**)은 이 저장소의 자체 정리를, 과거 기록(**ARCHIVE**)은 이 저장소의 보존본과 고정 커밋의 Melete 기록을 가리킨다. 둘 다 이번 개정에서 새로 실행하거나 재검증한 것이 아니다. 미결정 사항은 **OPEN**(§10의 D-번호)으로 표시한다. 마지막 개정: 2026-11-12.

> **무엇을, 왜 바꿨나**
> - **왜:** 옛 로드맵(P0 연구 계약 → P6 외부화)은 사용자 전역 규칙 "점진적 해상도"(B17, 2026-10-21)와 어긋났다. 조사·계약 전용 phase(P0)가 있었고, phase가 계층·부품별(재귀·controller·Sleep·확대·외부화)로 나뉘었으며, phase 종료물이 "실제로 쓸 수 있는 전체 제품"으로 정의되지 않았고, 데모 시나리오·넓이/깊이 변화·상한·미루는 것·capability 표가 없었다.
> - **무엇을:** 매 phase가 끝날 때마다 `fcl` CLI에서 실제 pretrained 소형 모델이 경험 입력부터 재시작 복원까지 전체 여정을 돈다. phase가 지날수록 같은 제품의 넓이(구조·층·모델·인터페이스)와 깊이(쓰기·정정·계산·공고화·검증)가 함께 올라간다. phase는 5개다.
> - **P0과 spike:** P0은 phase가 아니라 P1 앞쪽 작업(P1-T01~T03)으로 흡수했다. spike도 각 phase의 앞쪽 작업이다. 대조군(고정·무구조·항상-갱신)과 망각·표면/구조 평가는 P1부터 들어간다.
> - **숨기지 않은 것:** 옛 P0–P6와 더 오래된 계획(11-03 P0–P5, Melete N0–N5·J0–J5·P1–P4)은 §9 기존 계획 대응표에 남겼다. 옛 PASS/FAIL·산출물을 새 phase 완료로 옮기지 않는다.
> - **살린 것:** 옛 §2 최소 사용자 여정 → P1의 UJ1, 옛 §4 중단·전환 조건 → §7, 옛 §5 지속 자산 → §8, 옛 §6 기존 phase와의 관계 → §9. 옛 §3 초기 실행 순서 8단계는 §9 대응표에서 작업 단위로 옮겼다. 순서상 가장 큰 변경은 관계 전이·few-shot 과제(옛 5단계)를 고정 깊이 재귀(옛 4단계)보다 앞으로 당긴 것이다.

> **2026-11-18 개정 (PROPOSAL):** 2026-11-18 사용자 요청(원문과 위치: [2026-11-18-discussion.md](/home/jimmy/repos/full-continual-learning/sources/sync/2026-11-18-discussion.md))으로 아래 본문의 phase 5개(P1–P5) 앞뒤에 phase가 하나씩 더해져 **phase는 7개**가 됐다. 앞에 **P0(NP)** 무학습 비모수 POC(System ONE-NP), 뒤에 **P6(ET)** 역사 아인슈타인 테스트(ET) 최종이다. 본문의 「phase는 5개다」, 「P0은 phase가 아니라 P1 앞쪽 작업(P1-T01~T03)으로 흡수했다」, 「옛 로드맵(P0 연구 계약 → P6 외부화)」은 **2026-11-12 기준의 서술**이며 이번 개정은 그 문장을 지우거나 고치지 않았다. 새 P0(NP)는 그 옛 P0(연구 계약)를 되살린 것이 아니라 별개이고, 이름 충돌의 정리는 §9 보충 행에 있다.
> - **보충의 방식:** 기존 문장·표·결정은 그대로 두고 바로 아래에 「2026-11-18 개정」으로 표기한 보충 문장·보충 표·새 절만 더한다(§4-1·§6-1과 같은 방식). 보충하는 곳은 §1.2·§1.3·§1.4(phase 정의), §3(상한), §4(capability 표), §5(P0(NP) 절·P6(ET) 절과 P1–P5 조정 주석), §6(회귀 gate), §7(중단·전환), §8, §9(대응표), §10(결정), §11(자체 점검표와 변경 기록)이다.
> - **무엇이 같은가:** 모든 phase는 같은 `fcl` 제품의 해상도를 올린 것이고, 매 phase 종료는 실제 CLI·실제 의존성으로 끝까지 도는 전체 제품이다. P0(NP)도 P6(ET)도 예외가 아니다. phase마다 독립 논문 1편(PAPER-0~6)을 낸다.
> - **함께 읽을 문서:** 이상 청사진 [16-ideal-blueprint.md](/home/jimmy/repos/full-continual-learning/docs/16-ideal-blueprint.md), 아인슈타인 테스트 설계 [17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md), 비모수 POC 설계·검증 계획 [18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md), 단계별 논문 계획 [19-paper-plan.md](/home/jimmy/repos/full-continual-learning/docs/19-paper-plan.md), 계산 계획 [15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md). feature·flow, ET 정의와 단별 상한, P0 상세, 논문 주장, 비용은 그 문서가 소유하고 이 문서는 phase·gate·결정을 소유한다.
> - **기준일:** 위 상태 라벨의 「마지막 개정: 2026-11-12」는 기존 본문의 기준일이다. 이 보충의 기준일은 2026-11-18이다.
> - **「P1은 MVP」:** 이번 구성에서는 P0(NP)가 뼈대와 전체 여정을 먼저 세우고 P1이 첫 학습 해상도가 된다. 사용자 확인 대기다(§1.4 보충 주석, §10).

**읽는 순서:** 먼저 §1.4(한눈에 보기), §4(Capability × phase 표), §5의 P1을 본다. 나머지 절은 근거와 규칙이다.

## 1. 원칙과 FCL 적용

### 1.1 사용자 제약과 이 로드맵의 반영

**USER:** 아래 왼쪽 두 열은 사용자가 한 말에서 로드맵에 직접 영향을 주는 제약이다. 오른쪽 열은 **PROPOSAL**, 곧 우리가 그 제약을 반영한 방식이다. B-번호는 Melete 시기 사용자 피드백(2026-09-27~10-21)과 이번 설계 감사 요청(2026-11-11~12)의 항목 ID이고, U-T 번호는 [user-statements.md](/home/jimmy/repos/full-continual-learning/sources/user-statements.md)의 ID다.

| ID (날짜) | 사용자가 정한 것 | 이 로드맵의 반영 위치 |
|---|---|---|
| U-T02 | objectives, 숫자로 환산되는 verification(benchmark 포함), negative feedback과 evolution, operation policy를 확정하고, 가장 간단히 시작해 점점 고도화한다 | P1이 가장 얇은 전체 여정(§5), 사전 명세 manifest와 등급(§3), negative feedback 분기(§7), operation = 증거 원장·권한 분리(§2) |
| U-T06 | phase를 나눠 단계별 MVP 계획·구현을 하고 self-evolving 작업 방식을 그대로 적용한다 | §5 phase별 MVP, §4 self-evolution 행(P1 수동 → P2 v1 → P3 이후는 승인된 범위만) |
| U-T07 | 기존 모델의 seq layer는 Titan-Llama로, FFN은 CMS로 점진 교체하고, 이후 schema를 외부로 offload·versioning·retrieval하며, 입력 문맥의 schema 판단 구조를 넣는다 | §4 retrofit 행(P1 일부 layer → P5 확대), 외부화 행(P1 bundle → P4 v0 → P5), controller 행(P1 규칙형 controller v0가 익숙함 신호로 fast·learn·deep 경로를 고름 → P3 학습된 controller. "이 과정에서 입력 문맥에 대한 schema판단 mlp나 구조를 넣어서"를 P1부터 반영, D-14) |
| B02 (10-05) | 제한 없는 이상적 청사진의 메커니즘을 정하고, 가장 빨리 검증할 핵심 가치를 찾고, 단계별로 가치를 더하는 phase로 만든다 | P1이 핵심 가치(새 개체 전이·망각·대조군)부터 측정하고 뒤 phase는 같은 제품에 깊이·넓이를 더한다 |
| B05 (10-06) | 구성요소와 구현 방법을 phase로 묶되, 완성된 형태로 test 가능한 것끼리 묶는다 | phase = 여정 전체 × 해상도. 계층·부품 단위 phase 금지(§1.4) |
| B07 (10-07) | 매 단계 self feedback: 의도한 방향인지, 의도대로 구현됐는지, 단계 기준을 충족하는지. pass면 다음, fail이면 개선, 권한·필수 인프라 문제로 막히면 멈추고 보고 | §11 |
| B11 (10-11) | 학습 방법 검증이 가장 중요하다. 조합들이 검증됐는가, 수준은? | §3의 등급이 곧 "검증 수준"이고 §4의 셀마다 도달 가능한 등급을 적었다 |
| B12 (10-11) | 가설·검증 workflow로 진행하고, 실제 쓰는 codex·prime agent에 연동해 continual learning을 의도대로 쓰는 단계까지 간다 | 매 phase의 봉인 manifest = 가설·검증 계약(§2), 외부 agent 연결은 P5 |
| B13 (10-11) | "벌써 agent에 연결해?" — 이른 agent 연결에 대한 비판 | 연결은 P5이며 진입 조건은 핵심 대조의 등급 3 PASS(§7). P1~P4에서는 모델 자체가 실제 LLM이다(§1.3) |
| B14 (10-12) | agent 연결 구조·interface에 치우쳤다, neural이 가장 중요하다, 학습 방법 조합을 검토할 dataset·testcase가 필요하다, H1–H5는 틀렸다고 확인되기 전까지 유지하는 basis다 | dataset·testcase = P1-T06 세계 생성기(dev/sealed 분리). H1–H5는 통합 System ONE의 메커니즘으로 재정의돼 계승된다: familiarity 기반 빠른 처리는 P1(규칙형 controller v0의 fast 경로)부터, hit 경로 강화는 P3(controller·gate), turn별 surprise → 학습 → 최초 query 재구성 → 재개는 P1(정정·재평가·복원)과 P3 |
| B16 (10-13) | 진짜 목표는 Experience → Latent Conditional Judgment → Revisable Decision이며 결과 예측이 아니다. 조건부 판단 benchmark부터 | P1의 질의는 "조건이 주어졌을 때의 판단"과 "정정 뒤의 재선택"이다(P1-T02·T06) |
| B17 (10-21) | 점진적 해상도(전역 규칙): 매 phase 종료 = 실제로 쓸 수 있는 전체 제품, P1 = MVP(walking skeleton), 정직한 상한 | 이 문서 전체 |
| B19 (11-11) | 논문 원문 검토를 생각의 시작점으로 삼는다 | [2026-11-11-sbl-fulltext-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext-review.md) §4.1(같은 예산의 고정·무구조·항상-갱신 대조)·§4.4(망각·표면/구조·계산량 미측정)·§5(DQ1–DQ8, 고정 깊이 곡선이 먼저)가 P1 대조군·평가와 phase 순서가 됐다 |
| B20 (11-12) | 설계에 집중하고, 준 피드백이 반영됐는지 확인하고, 시각화 백서를 만든다 | 이 개정과 이 표 |
| U-T12 (11-16 기록; 발화일 미확인) | 지속학습의 목적을 "무한한 시간동안 경험하는것을 재앙적 망각 없이 학습"으로 두고, 생각할 점을 CRUD에 빗대 간섭 없는 새 지식 학습(Update), 무한히 증가하는 지식에서 망각의 비용(Delete), 현재 문맥에 쓸 지식 가져오기(Read)로 나눈다. 해법은 "Schemal based learning의 조절"로 "기존 지식(low rank expert)에 대한 in place update"를 하고 "적합한 schema를 못찾으면 create"로 새 low rank expert를 만드는 것이며, 목적은 Ali에게 joint paper 상세를 제안하는 것이다([2026-11-16-discussion.md](/home/jimmy/repos/full-continual-learning/sources/sync/2026-11-16-discussion.md)의 사용자 원문; ID는 가칭) | §4-1 CRUD 대응(PROPOSAL): Read·Update는 P1 규칙형 controller v0의 fast·learn·deep부터, Create는 P3 accommodation부터, Delete(기능적 망각/보존)는 측정이 P1 망각 평가부터이고 정책은 P4부터다. 공동논문은 로드맵 밖이며 주장 상한은 §3 등급을 따른다 |
| U-T14 (11-17) | 오늘 날짜 기준으로 다시 검토하고 저장소에 반영하며, host의 runcrate 사용환경에서 melete를 만들고 학습할 때 "너무 과도한 사양이 아닌, 그렇다고 minimum으로 품질이나 효율을 떨어트리지 않으면서" 쓰는 방법을 계획한다(이 저장소에서는 통합 모델 System ONE의 학습으로 읽었고 사용자 확인 대기) | [15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md)(횡단 문서, 별도 phase 아님)와 §10의 자원 표·D-04 개정 추천(PROPOSAL, 결정 대기). P1–P5의 데모·gate·상한은 바꾸지 않는다. '계획해봐'는 비용 승인이 아니다 |

**ARCHIVE:** Melete에서는 구현 PASS와 효용 PASS를 문서로는 구분했지만 다음 단계 진입 gate로 집행하지 못했다([2026-10-15-neural-judgment-roadmap.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/superpowers/plans/2026-10-15-neural-judgment-roadmap.md)). N1(학습된 graph 메커니즘 실험)에서 학습된 graph의 추가 이득은 0.48%(대략 95% 구간 −3.07~4.04%)로 독립 기여가 입증되지 않았는데 N2·N3 구성요소 연구가 이어졌다. J1 seed7 개발 pilot에서는 학습된 graph(Trained-G)가 matched 대조보다 낮았고(고정 graph 대비 −5.08pp, graph 없음 대비 −3.52pp. 같은 roadmap의 "J1 실행 현황"), 이후 pair objective 후보(G-pair)도 대조 대비 +1.95/+2.73pp로 +5pp gate에 못 미쳐 같은 recipe의 확대를 중단했다. N1·J1의 요약은 [12-melete-lineage.md](/home/jimmy/repos/full-continual-learning/docs/12-melete-lineage.md) §2–§3에도 있다. 위 숫자는 과거 기록이며 이 저장소에서 새로 실행한 값이 아니다. 이 로드맵은 그 교훈을 §3의 등급, §2의 봉인·문구 검사, §7의 진입 규칙으로 집행한다.

### 1.2 헌장 목표 U01–U12의 해상도 경로

**PROPOSAL:** [01-intent-and-charter.md](/home/jimmy/repos/full-continual-learning/docs/01-intent-and-charter.md)의 명시적 목표가 어느 phase에서 어떤 해상도로 올라가는지 한 줄로 적는다. 아직 약속하지 않는 구간은 그렇게 적는다.

| 목표 | 해상도 경로 |
|---|---|
| U01 schema 형성·활용 | P1 상태·행동 변화 관찰(형성은 선언 안 함) → P2 조작적 증거 2종 → P3 표현 제거·교체 개입 |
| U02 SBL 이론의 폭넓은 적용·검증 | F01–F12를 phase마다 추가(§4 benchmark 행). 인지 현상 재현과 뇌 알고리즘 입증은 구별 |
| U03 rapid learning | P1 관측 0/1/3/10 곡선 → P2 구조 3종 → P3 쓰기 gate 분해 |
| U04 익숙하면 빠르게, 필요하면 깊게 | P1 규칙형 controller v0의 fast·learn·deep 경로(deep = r=2, 측정만) → P2 고정 깊이 곡선 → P3 학습된 controller·halting → P4 deep-to-shallow |
| U05 System 1+2를 하나의 모델에 | 전 phase에서 한 모델. 외부 판단기·외부 LLM은 대조군으로만 둔다 |
| U06 sequence layer를 Titan-Llama 계열로 retrofit | P1 일부 layer → P2 확대 → P5 범위·모델 확대(전 층은 근거가 있을 때만) |
| U07 FFN을 CMS로 점진 전환, Sleep으로 통합 | P1 CMS 분기(함수 보존) → P2 level 확대 → P4 Sleep 통합 |
| U08 looped·MoD/MoR·depth attention 검토 | P2 고정 depth(retrofitted recurrence) → P3 라우팅·depth read 후보. 동시 채택을 전제하지 않음 |
| U09 문맥별 schema 판단 구조 | P1 규칙형 controller v0(익숙함 신호 → 경로·쓰기·r. 학습된 판단이 아님) → P2 유지(고정 깊이 측정 때는 우회) → P3 학습된 문맥 head(q^-)·전환·조합·보류 |
| U10 schema offload·versioning·retrieval | 상태 경계는 P1 bundle v0 → P4 외부화 v0 → P5 retrieval·migration |
| U11 뇌파에서 상태 의존적 조율 탐구 | P3에서 고정 주기·frequency-adaptive·event/readiness 조율(A·B·C)을 대조. 위상(phase) 조율(D)은 C를 기준선으로 확보한 뒤 D 대 C로 비교([04-rhythms-and-orchestration.md](/home/jimmy/repos/full-continual-learning/docs/04-rhythms-and-orchestration.md) §6)하며 배치는 OPEN(D-13) |
| U12 이론·수식·PoC·단계별 MVP·self-evolution | 이 문서 전체와 §4 self-evolution 행 |

**2026-11-18 개정 (PROPOSAL):** 위 표의 해상도 경로는 P1–P5 기준이며 바꾸지 않았다. 새 P0(NP)는 U01–U12를 frozen 공개 가중치 LLM과 비모수 schema 기억으로, 학습 없이, 가장 얇게 한 번 훑는 시작점이다. U05는 외부 frozen LLM을 쓰는 대역이라 최종형이 아니고, U06·U07의 retrofit·CMS는 P1부터 들어간다(상세: [18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md)). 새 P6(ET)는 헌장의 통찰([01-intent-and-charter.md](/home/jimmy/repos/full-continual-learning/docs/01-intent-and-charter.md) §6: 새 표현·관계·적용 조건의 형성과 이후 전이)을 시간캡슐 기반 모델 위의 역사 발견 시험(ET-4)으로 끝에서 시험한다. 두 phase는 위 경로의 앞과 뒤에 시작점과 도달점을 더할 뿐이다.

### 1.3 FCL은 모델 제품이다 — "agent 제품은 CLI에서 실제 LLM으로 실제 일을" 규칙의 적용

**USER (B17):** agent 제품이면 claude·codex·prime agent처럼 CLI(TUI)로 실행해 실제 LLM을 연결하고 실제 일을 끝까지 시킬 수 있어야 한다. 실제 사용자 인터페이스와 실제 의존성으로 처음부터 끝까지 돌아야 하고 mock-only는 증거가 아니다.

**PROPOSAL:** FCL은 agent가 아니라 모델 제품이다. 별도 판단기와 외부 LLM의 조합이 최종 제품이라는 해석은 사용자 정정(U-T07)으로 대체됐다([AGENTS.md](/home/jimmy/repos/full-continual-learning/AGENTS.md), [01-intent-and-charter.md](/home/jimmy/repos/full-continual-learning/docs/01-intent-and-charter.md) §5). 그래서 규칙의 정신을 이렇게 옮긴다.

- **실제 LLM:** retrofit한 모델 자체다. 외부 frozen LLM에 원문을 붙인 경로는 최종 제품이 아니라 강한 대조군(`ctx`)으로 유지한다.
- **실제 인터페이스:** `fcl` CLI 세션이다. 평가 harness도 같은 CLI와 같은 session 프로토콜을 통해 모델을 호출한다.
- **실제 일:** 새 개체에 대한 질문에 모델이 답하고, 반례를 받아 고치고, 재시작 뒤에도 유지하는 여정 자체다. 연구용 작은 합성 모델·세계는 이 일의 재료이고, 실제 외부 consumer와 역할이 다르다.
- **외부 agent(codex·prime agent) 연결:** 모델 제품의 소비자(consumer)를 넓히는 **넓이 확장**이며 P5에 둔다. B12의 목표이고, B13·B14의 비판(효용 근거 없이 연결 구조부터 만들지 않는다)을 진입 조건으로 반영한다(§7).

**2026-11-18 개정 (PROPOSAL):** **P0(NP)는 사용자가 요청한 POC이며 외부 frozen LLM을 쓰는 비모수 대역(stand-in)이다. 최종형이 아니다**(U05, [05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §3, 위 「FCL은 모델 제품이다」). 이 문장은 docs/16·docs/18·이 문서가 같이 쓴다. 위 규칙은 P0에도 그대로 적용된다. P0도 실제 `fcl` CLI와 실제 frozen 공개 가중치 LLM과 실제 저장 경로로 처음부터 끝까지 돌고, mock이나 조사만 하는 phase가 아니다. 위의 「외부 frozen LLM에 원문을 붙인 경로는 최종 제품이 아니라 강한 대조군(`ctx`)으로 유지한다」는 규칙은 P1–P6에서 그대로이며, P0의 NP arm은 이후 모든 phase의 **영구 대조군**이 된다. 학습 모듈은 같은 예산의 NP arm보다 나을 때만 필요하다고 주장한다. P0로 주장하지 못하는 것은 가중치 수준의 schema 형성, 간섭 해소, 통합 모델의 내부 depth 효율이다.

### 1.4 phase의 정의와 한눈에 보기

**PROPOSAL (B17의 요약):** phase는 (전체 여정 UJ1…UJn) × (해상도)이며 아래 여섯 가지를 지킨다.

1. 종료 = 전체 여정이 실제 CLI·실제 pretrained 가중치·실제 test-time write·실제 저장·실제 프로세스 재시작으로 돈다. mock-only 결과는 E2E 증거가 아니다.
2. 한 계층만 만드는 phase, fake만 도는 phase, 조사만 하는 phase는 없다. spike와 kernel 연구는 phase 앞쪽 작업이며 효용 gate 통과로 혼동하지 않는다.
3. P1은 MVP(walking skeleton)다. 여정 전체를 가장 얇게 관통하고 §2의 뼈대가 P1부터 실제로 있다.
4. 매 phase는 넓이와 깊이를 함께 올린다(§4). 앞 phase의 데모 시나리오는 회귀 gate로 계속 통과한다(§6).
5. 아직 강제하지 못하는 보장은 그 phase에서 약속하지 않는다. 결과에는 등급과 상한을 건다(§3).
6. 계획 상세도도 점진적이다. P1은 작업 단위, P2는 목표·작업 묶음·gate, P3 이후는 목표와 종료 gate까지만 쓴다(§11).

| phase | 종료 때 사용자가 CLI에서 할 수 있는 것 | 최대 등급 |
|---|---|---|
| P1 얇은 전체 여정 | 소형 retrofit 모델에 경험을 주고, 새 개체 질문·반례·최초 과제 재평가·이전 조건 재방문·저장·재시작 복원·source 삭제까지 한 번에 돌리고, 질문마다 모델이 익숙함에 따라 고른 경로(바로 답·학습 후 답·한 번 더 돌린 답)를 trace로 보며, 대조군과 나란히 본다 | 2 개발 pilot |
| P2 여러 구조·고정 깊이 | 같은 여정을 구조 3종과 `--depth` 격자로 돌려 경험 전/후 quality–compute 곡선을 본다 | 3 한정 확증 |
| P3 스스로 고르는 모델 | P1의 규칙 대신 학습된 controller가 낯섦·적합도에 따라 빠른 답·학습 후 답·깊은 계산·보류를 스스로 고르고, 무엇·어디·얼마나·언제 쓸지를 나눠 정하며, 결정 trace를 확인한다 | 3 |
| P4 세션을 넘는 경험 | 세션 사이에 `sleep`을 돌리고, 다음 세션에서 더 적은 관측·더 얕은 depth로 풀며, 상태 bundle을 내보내고 불러온다 | 3 |
| P5 확대와 실제 consumer | 더 넓은 retrofit·두 번째 모델·자연어 도메인에서 확인하고, 실제 codex·prime agent가 같은 session 접점으로 쓴다 | 4 (운용은 관측 범위 안에서 5) |

**2026-11-18 개정 (PROPOSAL): phase 7개의 보충 표.** 위 표는 P1–P5이고 위 여섯 가지 원칙 가운데 1·2·4·5·6은 P0(NP)와 P6(ET)에도 같다(3은 아래 「P1은 MVP」 주석으로 읽는다). 종료 = 전체 여정이 실제 CLI·실제 의존성으로 돈다. P0(NP)와 P6(ET)는 한 계층만 만드는 phase, fake만 도는 phase, 조사만 하는 phase가 아니다. 아래 첫 표는 phase 7개를 한 줄로 놓고, 둘째 표는 위 표의 열(`phase | 종료 때 사용자가 CLI에서 할 수 있는 것 | 최대 등급`)을 P0(NP)와 P6(ET)에 대해 따로 쓴다. 논문의 제목·주장·초록은 [19-paper-plan.md](/home/jimmy/repos/full-continual-learning/docs/19-paper-plan.md), ET 단의 정의는 [17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md) §3.1이 소유한다.

| phase | 한 줄 정의 | 최대 등급 | 논문 | ET 단 (판정 대상 / 탐색·회귀) |
|---|---|---|---|---|
| P0(NP) | System ONE-NP: frozen 공개 가중치 LLM과 비모수 schema 기억, 무학습. 사용자가 요청한 POC이며 대역이고 최종형이 아니다 | 3(주장 단위, 조건부. 그 밖은 2 이하) | PAPER-0 (선택: PAPER-0b) | ET-0 / ET-1, ET-3p |
| P1 | 소형 retrofit 모델(NMM·CMS), 규칙형 controller v0 | 2 | PAPER-1 | ET-0(학습 arm 대 NP arm) / ET-3p 회귀 |
| P2 | 구조 family × depth | 3 | PAPER-2 | ET-0 깊이 곡선 / ET-1 |
| P3 | 학습된 controller, 선택적 write, accommodation | 3 | PAPER-3 | ET-1 / ET-2 |
| P4 | Sleep, 세션 간 경험, 외부화 v0 | 3 | PAPER-4 | ET-1 잠복 효과, ET-2 / ET-3(pilot 대상) |
| P5 | 더 큰 모델과 시간캡슐 기반 retrofit, 실제 consumer(위 P5 정의에 시간캡슐 기반 retrofit을 더한다) | 4 (운용은 5) | PAPER-5 | ET-3 / 없음 |
| P6(ET) | 역사 ET 최종: 시간캡슐 기반 모델 + 봉인된 주력 대상 묶음 | 3(제안, 4는 OPEN) | PAPER-6 | ET-4 / 없음 |

| phase | 종료 때 사용자가 CLI에서 할 수 있는 것 | 최대 등급 |
|---|---|---|
| P0(NP) 무학습 비모수 POC | 외부 frozen 공개 LLM에 비모수 schema 기억을 붙인 System ONE-NP로, 학습 없이 UJ1의 ①–⑩ 전체(경험 입력·새 개체 질문·반례·최초 과제 재평가·이전 조건 재방문·저장·재시작 복원·source 삭제·`--arm` 대조)를 NP arm으로 끝까지 돌리고, Sleep-NP와 합성 발견 세계 run(ET-0)과 공개 시간캡슐 모델 위의 ET-3p run을 한 번씩 돌려 발견 곡선과 누수 감사 보고서를 본다. 이 제품은 대역이며 최종형이 아니다 | 3 (주장 단위, 조건부. 그 밖은 2 이하) |
| P6(ET) 역사 ET 최종 | 시간캡슐 기반 모델에 System ONE을 얹어 기반 모델을 지정하고, 봉인된 인물 stream을 시간순으로 넣어 checkpoint마다 발견 곡선을 보고, 대조 stream·대조 arm과 나란히 놓고, 봉인 대상 판정(ET-4) 보고를 받는다 | 3 (제안, 4는 OPEN) |

**「P1은 MVP」와의 관계 (2026-11-18 개정, PROPOSAL, 사용자 확인 대기):** 사용자 전역 규칙은 P1이 MVP(walking skeleton)다. 이번 구성에서는 P0(NP)가 §2의 뼈대(프로세스 경계·session 프로토콜·state store·분리된 evaluator·증거 원장)와 전체 여정을 가장 얇게 먼저 세우고, P1이 첫 학습 해상도가 된다. 사용자 원문 「모델 학습없이 non parameter 기반의 무언가로 POC검증을 먼저 해보자 … 그뒤 단계별 구현」에 맞춘 해석이다. 위 원칙 3의 「§2의 뼈대가 P1부터 실제로 있다」와 §2의 제목은 「P0(NP)부터」로 읽고, P1의 MVP 지위는 학습 모듈(retrofit)을 처음 얹는 첫 해상도로 읽는다. P1 본문의 데모 시나리오·종료 gate·상한은 바뀌지 않는다. 이 해석을 받아들일지는 §10의 결정 후보다.

## 2. P1부터 있는 아키텍처 뼈대

**PROPOSAL.** 근거: [07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md), [08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md), [10-evolution-policy.md](/home/jimmy/repos/full-continual-learning/docs/10-evolution-policy.md). 뒤 phase는 아래 경계를 바꾸지 않고 안쪽을 키운다. 아래 이름(`fcl`, 명령어)은 가칭이다.

```text
사용자(터미널)
   │  fcl CLI : session · 경험 입력 · 질문 · 정정 · diff · 재평가 · 재방문 · 저장/복원 · 삭제 · eval
   ▼
session 프로토콜 (stdio JSON-lines)        ← P5에서 외부 consumer가 같은 프로토콜을 쓴다
   ▼
fcl-runtime 프로세스 (모델 runtime, CLI와 별도 프로세스)
   ├─ base : pretrained 가중치 (revision pin)
   ├─ retrofit : NMM sequence 경로(선택 layer) + CMS FFN 분기(B_j=0 초기화)   ← arm 설정으로 켜기·고정·학습
   ├─ write engine : committed snapshot → request-local working state → commit   (write 정책은 교체 가능한 접점)
   ├─ clocks : experience/root · token · recursion · optimizer step · level · wall
   └─ budget meter : write 수 · optimizer step · forward/backward · token · FLOPs 추정 · wall
   ▼
state store (디스크) : bundle manifest + weights·fast state·optimizer moments·counters + source ledger(append-only)

evaluator (별도 프로세스·별도 권한) : 세계 생성기(oracle은 여기에만) · split · arm 실행 · 지표 · 결과 상태·등급 · manifest 봉인 검사
증거 원장 : run ID · config·code·data hash · 환경 · 실제 비용(실패·취소 포함)
```

| 뼈대 요소 | P1에서 실제로 있는 것 | 뒤 phase에서 커지는 것 |
|---|---|---|
| CLI와 runtime의 프로세스 경계 | CLI와 runtime이 별도 프로세스이고 session 프로토콜이 stdio JSON-lines로 정의된다. "재시작"은 runtime 프로세스를 실제로 종료·재기동해 검증한다 | P2 `--depth`·배치 평가, P3 결정 trace 필드, P4 `sleep`·`export`, P5 외부 consumer가 같은 프로토콜을 사용 |
| 모델 runtime | 실제 pretrained 가중치(revision pin) + retrofit 모듈 + write engine + 시계 기록 + budget meter | layer 수, depth, controller, Sleep, 모델 종류 |
| 상태·시계·저장([07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md)) | bundle manifest v0, 원자적 commit, 복원, source ledger, 모델 revision mismatch 거부, 최소 상태 회귀 | 다세션, controller 상태, 외부화, retrieval, migration, multi-user 격리 |
| 평가·대조 경로 | evaluator 분리(oracle 비노출), `--arm`으로 대조군을 같은 경로에서 실행, budget 일치 검사, 봉인 manifest | arm 추가, 구조 family, 확증 반복 |
| 증거 원장 | run ID·hash·환경·실제 비용·실패 기록, append-only | 후보 계보, self-evolution 루프 |
| 결과 보고 | 결과 상태와 등급 필드가 필수이고 등급에 맞지 않는 문구는 검사기가 막는다 | 등급 상향 조건 검사 |

- **대조군도 같은 경로로 돈다 (PROPOSAL):** 모든 arm은 같은 CLI, 같은 session 프로토콜, 같은 runtime 코드 경로, 같은 평가 harness를 쓰고 `--arm`과 arm manifest(설정 hash)만 다르다. 학습이 필요한 arm은 자기 checkpoint를 가리키지만 선택 방식은 같다. `ctx`는 경험을 prompt로 넣는 대조라서 계산 예산이 다르므로 "같은 예산 대조"가 아니라 강한 참고 대조로 표기한다.
- **write 정책 접점과 controller v0 (PROPOSAL, U-T07 "이 과정에서 입력 문맥에 대한 schema판단 mlp나 구조를 넣어서"):** write engine는 "무엇·어디·얼마나·언제 쓰는가"를 정책 접점으로 받는다. P1은 이 접점 앞에 규칙형 controller v0를 둔다. 익숙함 신호(NMM surprise·CMS 잔차)의 두 임계값으로 질문마다 fast(쓰기 없이 r=1로 답), learn(Titans식 surprise write 뒤 r=1로 답), deep(write 뒤 retrofit 블록을 한 번 더 적용한 r=2로 답) 중 하나를 고르고 경로·신호값·예산을 결정 trace로 남긴다. 임계값은 dev에서 정해 봉인하며 학습된 schema 판단이 아니다. v0는 사용자가 말한 단계 처리(U-T07)의 가장 얇은 단조 규칙이므로 "익숙해도 긴 관계 합성은 깊게 계산한다" 같은 다중 신호 결정([05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §4)은 다루지 못하며, 이는 P3의 학습된 controller에서 올린다. 고정 깊이 측정(P2 이후)은 controller를 우회한다. P3의 학습된 controller는 같은 접점과 같은 trace 필드를 쓴다(D-14).
- **봉인과 집행 (PROPOSAL, B07·B12·Melete 교훈):** 가설·primary 지표·통계·multiplicity·최소 효과·seed 수·예산 허용오차·보호 지표 임계를 manifest에 쓰고 hash로 봉인한 뒤에만 sealed cohort를 만든다. 평가 코드는 manifest hash가 맞지 않으면 실행을 거부한다. 임계값은 이 문서에 없고 P1-T14에서 dev pilot의 분산으로 처음 정한다.
- **P1에서 일부러 얇게 둔 것:** 단일 사용자·단일 writer(동시 write는 거부), 네트워크 서버·인증 없음, bundle manifest는 [07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md) §5의 부분집합(slow level·consolidation 필드는 `none`). 원 Titan 코드의 `generate()`·`reset_memory=True` 같은 state reset 경로를 session 경계로 오인하지 않는다. session 지속성은 별도 계약이다([05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §6).

## 3. 결과 등급과 상한

**PROPOSAL.** 근거: [08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md) §1(Contract·Efficacy·Product 분리)·§8(결과 상태)·§9(수치 보고), B11, 위 Melete 교훈. 세 축을 섞지 않는다.

- **gate 종류:** Contract(인과 입력·state·재생·누수·budget·출처), Efficacy(새 사례의 판단·학습·보존·비용), Product(실제 입력→추론→학습→재개→재시작→삭제 여정). Contract PASS나 테스트 개수는 Efficacy나 Product 완료를 대신하지 않는다.
- **결과 상태:** PASS·FAIL·INCONCLUSIVE·BLOCKED·NOT RUN. 방향을 말한다. FAIL을 소급 PASS로 바꾸지 않는다.
- **등급:** 증거의 범위를 말한다. 등급은 phase가 아니라 **주장 단위**로 부여한다. 등급 3 FAIL은 "이 범위에서 확인된 음성 결과"이므로 높은 등급의 음성 결과도 정당한 증거다.

| 등급 | 이름 | 필요한 증거 | 쓸 수 있는 문구 | 쓰면 안 되는 문구 |
|---|---|---|---|---|
| 0 | 설계·미실행 | 설계와 코드만 존재 | "설계됨", "NOT RUN" | 성능·효과 |
| 1 | 계약 통과 | Contract gate PASS(재생·누수·budget·출처·상태 계약) | "계약 통과" | "개선", "효과", "schema 형성" |
| 2 | 개발 pilot | 실제 pretrained 가중치·실제 갱신·budget 일치 검사 통과. 합성·단일 구조 family·소형 모델 1종·제한 seed. dev 결과 또는 사전 명세 readout | "이 pilot 범위에서 관측했다 / 사전 명세 대조를 통과(미달)했다", 구간 병기 | "schema 이득", "개선했다", "일반화", "빠른 판단 성립", "계산 절감" |
| 3 | 한정 확증 | 봉인 manifest + fresh locked cohort + 같은 계산·쓰기 예산의 고정·무구조·항상-갱신 대조 + 2종 이상 구조 family(lure 포함) + 사전 명세 충분 seed + 독립 검토. 상태 PASS | "이 합성 family·이 모델·이 seed 집합에서 대조군 대비 우위(PASS)". **schema 이득이라는 문구는 여기서부터**, 범위 태그 필수 | "자연어 일반", "다른 모델에서도", "제품 효용" |
| 4 | 확장 확증 | 등급 3 + 2종 이상 base model(크기 또는 계열이 다름) + 자연어 혼합 도메인 + 새 fresh cohort에서 반복 | "확장한 범위에서도 유지" | "모든 모델·도메인", "운용 안정" |
| 5 | 제한 운용 | 실제 consumer·다세션 이력·외부화를 포함한 실제 E2E + 관측한 coverage 안의 latency·memory·삭제 의존성 | "관측한 범위에서 동작" | "모든 agent·model-call 포괄", "삭제 완전 보장" |

| phase | 최대 등급 | 등급을 막는 것(그 phase의 상한 이유) |
|---|---|---|
| P1 | 2 | 합성·단일 구조 family, 소형 모델 1종, 제한 seed, 부분 retrofit(전 층 아님), 규칙형 controller v0와 r∈{1,2} 경로뿐, Sleep 없음 |
| P2 | 3 | 합성·소형 모델 1종. 확증은 구조 family 3종·사전 명세 seed에서만. depth·조작적 증거 주장은 확증을 거친 것만 3 |
| P3 | 3 | controller 주장은 쉬운 사례 층화와 같은 품질 비교를 통과한 것만. 모델·도메인 1종 |
| P4 | 3 | Sleep·외부화 주장은 같은 데이터·총 계산량의 replay·teacher 대조를 통과한 것만. 삭제 보장 없음 |
| P5 | 4, 운용은 5 | 두 번째 모델과 자연어 혼합 도메인에서 복제된 것만 4. 운용은 관측한 호출 coverage 안에서만 5 |

표의 최대 등급은 phase의 상한일 뿐이고, 각 주장은 그 주장의 증거가 채운 등급만 받는다. 예를 들어 P2의 depth 곡선이 봉인 확증을 거치지 않았다면 등급 2다.

**2026-11-18 개정 (PROPOSAL): P0·P6 보충 행.** 위 상한표의 열(`phase | 최대 등급 | 등급을 막는 것`)에 P0(NP)와 P6(ET)를 더한다. ET 단별 상한과 쓸 수 있는 문구·없는 문구는 [17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md) §3.2의 표 하나가 기준이고 여기서 값을 되풀이하지 않는다.

| phase | 최대 등급 | 등급을 막는 것(그 phase의 상한 이유) |
|---|---|---|
| P0(NP) | 3, 주장 단위. suite S-A·S-B의 개별 주장이 위 등급 3 조건(봉인 manifest, fresh locked cohort, 같은 계산·쓰기 예산의 대조, 구조 family 2종 이상, 사전 명세 충분 seed, 독립 검토)을 모두 채울 때만 3을 시도한다. 그 밖의 P0 주장은 2 이하다. ET-1과 ET-3p는 탐색(등급 2 이하. ET-3p의 절차는 등급 1)이다 | 무학습 비모수 대역(외부 frozen LLM), 합성 세계, 소수 모델, 최종형이 아님. 가중치 수준의 schema 형성·간섭 해소·통합 모델의 내부 depth 효율은 주장하지 못한다. 현대 LLM은 역사적 발견을 이미 알 수 있어 ET-0~ET-2는 같은 frozen LLM 안의 arm 사이 상대 효과만 주장한다 |
| P6(ET) | 3 한정 확증(제안). 4는 같은 절차를 두 번째 시간캡슐 기반과 두 번째 봉인 대상 묶음에서 새 fresh cohort로 복제한 경우에 한해 시도한다(OPEN) | 대상 수가 적다(통계 단위는 대상과 구성요소), 단일 시간캡슐 기반, stream 재구성의 불확실성(입력 tier), 사후 편향의 잔존. 「발견했다」는 ET-4 등급 3에서만 범위 태그와 함께 쓰고 「아인슈타인 테스트를 통과했다」·「모든 발견」·AGI 문구는 쓰지 않는다 |

**「실제 갱신」의 읽기 (2026-11-18 개정, OPEN, 사용자 확인 대기):** 위 등급 2의 필요한 증거 「실제 pretrained 가중치·실제 갱신·budget 일치 검사」에서 「실제 갱신」은 P0(NP)에서는 「실제 비모수 state 쓰기」로 읽는다. 가중치를 바꾸지 않으므로 이 읽기는 P0의 문구에 「비모수」 태그를 달고 P1 이후의 등급과 같은 표에 섞지 않는다는 조건이다(§10).

**문구 규칙 (PROPOSAL):**
1. 등급 필드가 없는 결과는 보고하지 않는다. 결과 보고 생성기가 결과 상태와 등급을 필수로 찍고, 등급에 허용되지 않은 문구는 검사기가 막는다(P1-T12).
2. 이름만 같은 간이 구현을 원본 HOPE·Titan-Llama 재현이라고 부르지 않고 설계 차이와 생략된 학습을 기록한다([05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §5(CMS 식은 원본 HOPE의 정확한 구조식이 아닌 프로젝트 proposal), 옛 §3).
3. 과거(ARCHIVE) 숫자와 이번 실행값을 한 표에 섞지 않는다. 이번 실행은 새 run ID·config·code/data hash·환경·실제 비용과 함께 쓴다([08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md) §9).
4. 임계·margin·subset은 결과를 보기 전에 봉인하고, 본 뒤에 고쳐서 PASS로 만들지 않는다.
5. "schema 형성"이라는 말은 조작적 증거(P2~P3)가 생기기 전에는 쓰지 않는다. P1의 state diff는 "상태가 바뀌었다"는 관찰이다.

## 4. Capability × phase 해상도 표

**PROPOSAL.** 행은 능력, 열은 phase다. 셀은 그 phase 종료 시점에 도달하는 해상도이며 앞 열의 내용을 포함한다. "유지"는 바뀌지 않는다는 뜻이고, "없음(미약속)"은 그 phase에서 약속하지 않는 능력이다. 한 phase에서 모든 행이 한꺼번에 오르지는 않는다.

| Capability | P1 얇은 전체 여정 | P2 여러 구조·고정 깊이 | P3 스스로 고르는 모델 | P4 세션을 넘는 경험 | P5 확대와 실제 consumer |
|---|---|---|---|---|---|
| retrofit 범위: sequence memory (Titans·Titan-Llama 계열 NMM) | 1–2개 layer에 NMM 경로(부분 전환, 전 층 아님. spike 실패 시 "없음") | layer 확대, 전환 1회마다 원능력·state·성능 회귀 | 유지 + controller가 읽는 memory 신호(적합도·잔차) 노출 | 유지 + fast→slow 공고화 경로 연결 | layer 범위·모델 확대(전 층은 근거가 있을 때만) |
| retrofit 범위: FFN→CMS | 1–2개 FFN에 CMS 분기(B_j=0 초기화로 함수 보존), fast level 1개 + 원 FFN을 느린 기반으로 | level 2개 이상(시간척도 분리), layer 확대 | level별 write 허용·보호 정책을 controller가 조정 | slow level로의 공고화(Sleep). 원 FFN 제거는 증류로만 | 전환 범위를 단계적으로 확대(all-FFN은 근거가 있을 때만) |
| schema/binding 상태와 관찰 | `fcl diff`(layer·module별 변화량·clock·write 수) + probe 응답 전/후 + wrong-schema state swap. "형성"은 선언하지 않음 | 조작적 증거 2종: 같은 구조 과제 간 subspace 재사용, 새 같은 구조 과제의 변화량 감소 | 3종째: 표현 제거·교체 시 구조 전이만 선택적으로 사라지는가 + controller의 schema 선택 trace | Sleep 전후 표현 변화, prototype 수축·lure 침입 진단 | 자연어 도메인·다른 모델에서 3종 재측정 |
| 빠른 쓰기 gate (무엇·어디·얼마나·언제) | controller v0가 learn·deep을 고를 때만 쓴다. 쓰기는 Titans식 surprise 정책 하나("얼마나")와 항상-갱신·고정 대조. 무엇·어디·언제는 고정 정책 | write 예산 u 격자와 (depth r, u) 2차원 평가. "어디" = layer·level을 arm으로 비교 | fit·친숙도 결합 선택적 write(확신 있게 맞은 곳은 보호), 학습된 neuromodulator 후보, 무엇·어디·얼마나·언제 분리 ablation | "언제" = 공고화 시점·replay 예산(novelty×familiarity 대 고정) | 자연어·긴 이력에서 false update·과잉 확신 보정 |
| 정정·accommodation | 반례·정정을 국소 갱신으로 반영하고 최초 과제 재평가·이전 조건 재방문으로 부작용을 측정(수정 메커니즘 없음) | 예외·ABA family 확대, 보호 영역 대조(slow 동결 대 fast만 쓰기) | accommodation 메커니즘(새 구조 대 미세 조정, 예외 분리 저장) 설계·대조 | 세션을 넘는 정정(Sleep 이후 수정, savings) | 오염(F07)·지연 피드백(F08)·자연어 반례 |
| 깊이·recursion·controller | 규칙형 controller v0: 익숙함 신호 → fast(r=1)·learn(r=1)·deep(r=2, retrofit 블록 1회 추가 적용과 짧은 적응 학습). 경로 분포·계산량은 측정만, 품질 이득은 약속하지 않음 | controller v0 유지(고정 depth 측정 때는 우회) + 고정 depth 격자 r∈{1,2,4,…}(retrofitted recurrence, 학습 포함), 경험 전/후 quality–compute 곡선 | 학습된 controller(문맥 head q^-·token/block 계산 mask·학습된 halting, 이후 조합·분화·level별 write 허용) + 적응 깊이, 쉬운 사례만 조기 종료한 평균과 구분 | deep-to-shallow distillation으로 같은 품질의 depth 감소 시험 | 확대된 retrofit·모델에서 controller 재검증(비용 포함) |
| Sleep·공고화 | 없음(미약속. consolidation_state = none) | 없음(미약속. replay 가능한 원장만 확보) | 없음(미약속. replay 후보 신호만 기록) | Sleep v0 = fast→slow teacher–student replay, replay 예산 대조 | 다세션·외부화와 결합한 Sleep 확대(Knowledge Seeding·Dreaming은 후보) |
| 대조군 | 고정·무구조·항상-갱신 + `noctl`(controller 없이 learn 경로 고정) + `ctx`(raw history)·`base`, 모두 같은 CLI의 `--arm` | + 고정 depth·random gate, 참고선 Qwen3-8B+raw history(크기가 달라 대조군 아님) | + novelty-only routing·learned early exit·surprise-only gate | + replay-only·같은 계산의 teacher distillation | + 외부 frozen LLM+RAG·구조화 text memory |
| 망각·보존 평가 | 최초 과제 재평가, 이전 조건 재방문(ABA), 원능력 probe | + savings(재학습 관측 수), family별 negative transfer | + 보호 family 퇴행 시 자동 중단 | + 세션·Sleep 전후 보존, zero-shot 재평가 | + 자연어·긴 이력·모델 간 보존 |
| 표면/구조 평가 | 2×2: 같은 구조·새 표면 대 새 구조·같은 표면 | 구조 family 3종·lure 확대, both-correct condition pairs | lure에서 controller의 선택 오류·과적용 진단 | Sleep 후 prototype 수축·lure 침입 | 자연어 paraphrase·표면 변이 |
| 계산량 측정 | budget meter(write 수·optimizer step·forward/backward·token·FLOPs 추정·wall)와 경로(fast/learn/deep)별 계산량. 대조군 예산 일치 검사용 | depth별 FLOPs·p50/p95·TTFT·메모리, (r,u) 격자 | controller·router 비용 포함 total cost, online과 amortized 분리 | Sleep·offload·warmup 비용 포함 amortized total | 운영 지연·residency·(가능하면) 에너지 |
| 상태 저장·재시작·외부화 | bundle v0 + 원자적 commit + 재시작 복원 + 얇은 source 삭제(replay 재구성, fast state 한정) | 다중 session·branch rollback·동시 write 정책 확대 | 제어 상태(controller)도 bundle에 포함 | 외부화 v0: export/import·offload/reload·version lineage·migration 거부 규칙. 통합 후 삭제는 "측정만" | retrieval·migration·multi-user 격리. 삭제 의존성은 검증한 범위만 |
| 사용자 인터페이스(CLI) | `fcl` CLI: session·경험 입력·질문·정정·diff·재평가·재방문·저장/복원·삭제·eval, 응답마다 결정 trace(fast/learn/deep·신호값·예산) | `--depth`, 배치 `fcl eval`·compare, session transcript | 학습된 결정 trace(q^-·전환·보류)·write 분해·예산 표시 | `fcl sleep`, `export`/`import` | 같은 CLI + 외부 consumer가 쓰는 같은 session 프로토콜 |
| 외부 consumer·agent 연결 | 없음(미약속. 모델 자체가 실제 LLM) | 없음(미약속) | 없음(미약속) | 없음(미약속. 방식·진입 조건은 P4 종료 재검토에서 결정, D-11) | codex·prime agent 실제 연결(진입 조건: 핵심 대조 등급 3 PASS) |
| self-evolution 루프 | 수동: 후보 manifest 서식·실험 원장·evaluator 권한 분리 설계 | v1: 봉인 manifest + 독립 evaluator 프로세스 + 후보 archive, 후보 제안·승인은 사람 | v2: 승인된 예산·search space 안에서 후보 생성 자동화(D-10), 같은 예산의 random·sweep 대조 | search space에 Sleep recipe 포함(승인 시) | 운영 승격 gate와 연결, 루프의 추가 가치 재검증 |
| benchmark family ([08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md) F01–F12) | F01·F02·F03·F05·F06 | + F11(고정 depth), F07 최소(동일 root 재전송·틀린 generated 해석) | + F04·F09, F08 일부 | + F10·F12 | + 자연어 표면 변이, F08 전체 |
| 결과 등급 상한 | 2 개발 pilot | 3 한정 확증 | 3 | 3 | 4 (운용은 관측한 coverage 안에서 5) |

**2026-11-18 개정 (PROPOSAL): P0(NP)·P6(ET) 열과 발견·ET·NP 행의 보충 표.** 위 표의 P1–P5 칸은 바꾸지 않았다. 아래 표는 같은 행(capability)에 P0(NP)와 P6(ET) 열을 더하고 새 행 넷(발견·통찰, ET 단, NP 대역, 논문)을 붙인다. 칸은 「NP 대역」과 「학습 모듈」을 구분해 쓴다. NP 대역은 P0(NP)의 비모수 대역이 그 phase의 base 모델로 다시 돌아 영구 대조군으로 남는다는 뜻이고, 학습 모듈은 그 phase에서 처음 들어오거나 깊어지는 것이다. 학습 모듈은 같은 예산의 NP 대역보다 나을 때만 필요하다고 주장한다. feature 단위의 같은 표는 [16-ideal-blueprint.md](/home/jimmy/repos/full-continual-learning/docs/16-ideal-blueprint.md) §4가 소유하며 어긋나면 이 문서가 기준이다.

**위 표의 「없음(미약속)」 칸에 대한 개정 주석 (2026-11-18):** 위 표에서 「없음(미약속)」은 그 phase에 **학습 모듈이 없다**는 뜻으로 읽는다. 해당 능력의 NP 대역은 P0(NP)부터 있고 그 phase의 base 모델로 다시 돌고 있다(**학습 모듈은 없음, NP 대역 유지**). 예: P1–P3의 Sleep 칸은 「학습된 Sleep은 없음. Sleep-NP 대역 유지」, P1–P2의 accommodation 칸은 「학습 모듈은 없음. 생명주기 판정(branch·create)의 NP 대역 유지」다. 예외는 외부 consumer·agent 연결 행이다. 이 행은 NP 대역도 학습 모듈도 P0–P4에서 약속하지 않는다(진입 조건 §7, 결정 D-11).

| Capability | P0(NP) | P6(ET) |
|---|---|---|
| retrofit 범위: sequence memory | NP 대역: NP-1 hidden-state kNN 결합 기억 / 학습 모듈: 없음 | NP 대역 유지 / 학습 모듈: P5까지의 범위를 유지(긴 stream의 용량·망각 관찰) |
| retrofit 범위: FFN→CMS | NP 대역: NP-0 텍스트 artifact schema와 NP-1 잠재 artifact schema(선택: NP-2 닫힌 꼴 선형 expert) / 학습 모듈: 없음 | NP 대역 유지 / 학습 모듈: 유지(장기 stream에서 schema 군의 재구조화) |
| schema/binding 상태와 관찰 | NP 대역: schema artifact의 구조화 기록과 `fcl diff`(artifact 단위 변화량·version), wrong-schema swap 같은 인과 개입. 「바뀌었다」는 관찰이지 schema 형성의 증거가 아니다 / 학습 모듈: 없음 | NP 대역 유지 / 학습 모듈: P5까지의 조작적 증거 재측정, 시간캡슐 기반에서의 관찰 |
| 빠른 쓰기 gate | NP 대역: NP-1 결합 기억 쓰기와 NP-0 기록 갱신(생명주기 판정 update, gradient 0회) / 학습 모듈: 없음 | NP 대역 유지 / 학습 모듈: 유지 |
| 정정·accommodation | NP 대역: 생명주기 판정(branch·create)과 반례의 국소 갱신, 최초 과제 재평가·ABA / 학습 모듈: 없음 | NP 대역 유지 / 학습 모듈: 유지 |
| 깊이·recursion·controller | NP 대역: 규칙형 controller(fast·learn·deep에 hold를 더함)와 NP 숙의 반복(반복 수·생성 token·LLM 호출 수로 측정. 구조적 recursion은 P2부터) / 학습 모듈: 없음 | NP 대역 유지 / 학습 모듈: 유지 |
| Sleep·공고화 | NP 대역: Sleep-NP(오프라인 군집·병합·추상화, 재조합 후보 생성, 저장된 근거에 비춘 자가 검사, 정리) / 학습 모듈: 없음 | NP 대역 유지 / 학습 모듈: 유지(발견용 재조합 단계와 연결) |
| 대조군 | NP arm 자체가 이후 phase의 영구 대조군이 된다. 같은 frozen LLM·같은 token·호출·저장 예산의 대조: 기억 없음, 전체 이력, dense RAG, 요약 기억, 통찰·전략 기억 계열, 개념 기억 계열, 평면 schema, controller 없음, Sleep 없음, wrong-schema swap, oracle schema(진단 상한) | NP arm 영구 대조 + 기억 없음·평면 기억 arm + 대조 stream 5종(없음·순서 섞기·같은 시기 비발견자·무관한 인물·핵심 입력 제거) |
| 망각·보존 평가 | 최초 과제 재평가, 이전 조건 재방문(ABA), 원능력 probe를 NP arm으로, 보존 예산 아래 eviction 측정 | 긴 stream에서의 용량·망각 관찰과 누설 변형(LV0·LV1·LV2)별 곡선 |
| 표면/구조 평가 | 2×2(같은 구조·새 표면 대 새 구조·같은 표면)를 suite S-A에서 NP arm으로. 구조 family 2종 | ET-1·ET-2의 오염·표면 의존 probe와 대조 stream |
| 계산량 측정 | budget meter가 NP 단위로 기록(LLM 호출 수·생성 token·저장 bytes·wall. 학습 FLOPs 없음) | ET run의 전 비용 기록(P5 기록의 연장) |
| 상태 저장·재시작·외부화 | 뼈대: state store(commit·snapshot·복원), bundle v0, source 삭제 계약(NP state 한정), 보존 예산 아래 eviction. NP state의 version 되돌리기 | 뼈대 유지(version 이력을 발견 보고의 근거 계보로 연결) |
| 사용자 인터페이스(CLI) | `fcl` CLI와 session 프로토콜, UJ0 명령 전부(UJ1 명령, `fcl sleep`, 긴장 원장·발견 보고, 가칭 `fcl et` 명령) | 기반 모델 지정·stream 투입·checkpoint probe·발견 곡선 보고·판정(가칭 `fcl et` 명령. 정의는 [17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md) §11) |
| 외부 consumer·agent 연결 | 없음(미약속). 이 행의 예외는 위 주석 | P5에서 연결한 것 유지 |
| self-evolution 루프 | 수동: 후보 manifest 서식·실험 원장·evaluator 권한 분리(P1과 같은 수준. NP arm 설정도 arm manifest hash로 고정) | 운영 승격 gate와 연결(P5 유지). 봉인 뒤에는 후보·기준·대조를 바꾸지 않는다 |
| benchmark family (F01–F12) | F01·F02·F03·F05·F06을 suite S-A에서 NP arm으로. F13·F16·F18·F19·F20·F21은 NP arm에도 적용([18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md) §4) | ET 지표(발견 곡선·특이성·입력 내재 대비 초과)와 새 family 후보([17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md) §8.7) |
| 결과 등급 상한 | 3 (주장 단위, 조건부. 그 밖은 2 이하. ET-1·ET-3p는 탐색) | 3 (제안, 4는 OPEN) |
| **(새 행) 발견·통찰** | NP 대역: 긴장 원장(구조화 기록)·Sleep-NP의 재조합 후보와 자가 검사·발견 보고 생성(생성물 표지). 생성물은 관측 증거로 올리지 않는다 / 학습 모듈: 없음 | NP 대역 유지 / 학습 모듈: P3–P5의 모듈이 ET-4 stream을 처리(P6에서 새 학습 모듈은 약속하지 않는다) |
| **(새 행) ET 단** | 판정 대상 ET-0. 탐색 ET-1, ET-3p | 판정 대상 ET-4 |
| **(새 행) NP 대역(NP-0·NP-1·NP-2)** | NP-0·NP-1은 필수 arm, NP-2는 선택(「비모수」에 넣을지는 사용자 결정). 주 모델(8B급)과 P1 base급(135M급)에서 NP-1 성립 확인 | 영구 대조군으로 같은 base에서 다시 돈다. base-only 시간캡슐 모델에서 NP-0이 성립하지 않으면 그 사실을 보고하고 NP-1을 대조로 쓴다 |
| **(새 행) 논문** | PAPER-0 (선택: PAPER-0b) | PAPER-6 |

### 4-1. CRUD 관점 대응 (2026-11-17 검토 추가, PROPOSAL)

**PROPOSAL.** 사용자가 지속학습의 점검 축으로 든 Update·Delete·Read(Create는 해법 안에서 등장, §1.1 U-T12)를 위 표의 phase에 대응시킨다. 기존 §4·§5의 데모 시나리오·넓이/깊이·보장·종료 gate·미루는 것은 바꾸지 않는다. 표의 기존 항목은 읽는 방법이고, 'P2 진단용 선택'·`nocreate` 등 새 arm과 F22·F23은 사용자 결정 전의 후보이며 §6-1·§10에 올렸다.

먼저 P1 규칙형 controller v0의 세 경로가 덮는 CRUD를 적는다. fast(쓰기 없이 r=1)는 Read, learn(surprise write 뒤 r=1)은 Read + Update, deep(write 뒤 r=2)은 Read + Update + 추가 계산이다. Create와 Delete는 덮지 않는다. write 정책 접점(Titans식 surprise write 대 항상-갱신)은 Update의 강도·허용을 고르는 정책이며 Create·Delete의 정책이 아니다.

| CRUD 연산 | 처음 들어가는 phase와 해상도 | 메커니즘 | 대조 arm | 평가 family | 등급 상한 |
|---|---|---|---|---|---|
| Read/Activate | P1: 선택 없는 읽기(단일 expert, fast 경로). P2: 진단용 선택(oracle·random·규칙 key). P3: 학습된 문맥 head q^-(전환·조합·보류). P4: offload/reload. P5: retrieval·migration | NMM·CMS 읽기 → 문맥 head → 외부 store | `noctl`, `ctx`(raw history), `base`; P2 random gate; P3 novelty-only routing·learned early exit; oracle(진단 상한); P5 외부 frozen LLM+RAG | F01·F02·F03, F04·F09·F15·F19, F12, 제안 F23 | P1 2 → P3 3 → P5 4 |
| Update(in-place) | P1: learn·deep 경로의 surprise write와 CMS fast level 갱신, 정정은 국소 갱신. P2: write 예산 u 격자, "어디"(layer·level), 보호 영역 대조. P3: fit 결합 선택적 write. P4: "언제" = Sleep 공고화 | Titans식 surprise write, 선택적 write gate, fast→slow replay | `always`, `fixed`, `flat`, `noctl`; P2 slow 동결 대 fast만 쓰기·random gate; P3 surprise-only gate; P4 replay-only | F01·F02·F03·F05·F06, F07, F09, F10 | 2 → 3 |
| Create(새 expert 할당·분화) | P1–P2: 없음(미약속; fast level 1개). P3: accommodation(새 구조 대 미세 조정, 예외 분리 저장) | 후보: B=0 초기화 CMS 분기의 추가([05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §5). 트리거 후보: 오류 크기, 구조적 새로움, 검색 실패(사용자 원문) | `nocreate`(미세 조정만), `always-create`, `random-create`, `oracle-create`(진단 상한) | F04·F18·F19 | 3. '분화 성립' 선언 금지 |
| Delete/Retain(기능적 망각/보존) | 측정: P1 최초 과제 재평가·ABA·원능력 probe, P2 savings·용량 제한 망각 곡선. 정책: P4 offload/reload·Sleep 통합·eviction, P5 압축·통합·폐기 | offload → 압축·통합 → 폐기, 기능 손실 추정 | replay-only, offload-only, 최근성·빈도 eviction, P5 압축·폐기 | F05·F06(측정), F10·F12, 제안 F22 | P1–P3 측정만, P4 3, P5 4. '삭제 완전 보장'·'무제한 무망각'은 쓰지 않는다 |
| (구분) source 삭제 | P1-T13 → P4 측정만 → P5 검증한 범위 | source 원장 철회 + 남은 source replay 재구성 | 삭제 동등성(자기 비교) | Contract·Product | fast state 한정 |

controller 사다리와의 대응: [05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §4의 문맥 head(q^-)는 Read, write gate와 레벨별 write 허용 u는 Update, 조합·분화 head는 Create에 해당한다. Delete/Retain에는 대응 head가 없고 Sleep·offload 일정이 맡는다. 두 가지 '삭제'의 구분은 [07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md) §7을 따른다. 배치가 정해지지 않은 항목(Delete/Retain 정책의 첫 phase 등)은 §10의 결정 후보에 올렸다.

## 5. Phase별 계획

**PROPOSAL.** 모든 phase를 같은 라벨 줄로 쓰고 가까운 phase일수록 상세하다. P1은 작업 단위까지, P2는 목표·작업 묶음·gate까지, P3 이후는 목표와 종료 gate 중심으로 짧게 쓴다. UJ1~UJ5(User Journey)는 phase별 데모 시나리오, 곧 전체 여정의 이름이며 뒤 phase의 회귀 gate가 된다(§6). 모든 phase의 종료 gate는 (1) 실제 인터페이스·실제 의존성 E2E, (2) 앞 phase 데모 시나리오 전부의 회귀, (3) 자동 테스트를 포함한다.

**2026-11-18 개정 (PROPOSAL): UJ0·UJ6 주석.** 위 서문의 UJ1~UJ5(User Journey)에 **UJ0**(P0(NP))과 **UJ6**(P6(ET))이 더해져 UJ0~UJ6이다. UJ0은 UJ1(①–⑩)의 상위 집합이다. ①–⑩의 번호와 뜻을 그대로 두고 NP arm으로 모두 실행하며, Sleep → 발견 run(ET-0) → ET-3p run → 보고서를 더한다(상세: [18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md) §2.1). 그래서 뒤 phase는 UJ0을 회귀 gate로 다시 돌린다(§6 보충 행). UJ6은 UJ0의 ET 부분(ET-0 run과 ET-3p run)을 회귀로 포함한다(재료: [17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md) §11.3). 위 서문의 「모든 phase의 종료 gate는 (1) 실제 인터페이스·실제 의존성 E2E, (2) 앞 phase 데모 시나리오 전부의 회귀, (3) 자동 테스트를 포함한다」는 P0(NP)와 P6(ET)에도 같다. 아래 P1 절의 「앞 phase가 없다(P1이 첫 phase)」와 「이 UJ1이 이후 모든 phase의 회귀 gate가 된다」는 2026-11-12 기준의 서술이며, 이번 구성에서는 P0(NP)가 첫 phase이고 UJ0이 회귀 gate의 시작이다. UJ1은 UJ0의 부분집합이므로 UJ0 회귀가 UJ1의 NP arm 회귀를 덮고, P1의 `full`과 대조 6 arm 회귀는 위 §6 표의 P2 이후 행이 그대로 요구한다.

### P0(NP) — 무학습 비모수 POC (System ONE-NP) (2026-11-18 개정, PROPOSAL)

**이름 주의:** 이 P0(NP)는 experiments/phase0의 「Synthetic Phase-0」(ARCHIVE, 통합 모델 PoC가 아님), research/2026-11-09의 추적 우선순위 「P0–P2」, 옛 로드맵(11-09 커밋)의 P0(연구 계약), 옛(11-03) P0와 **무관**하다(§9 보충 행). 이 절의 상세 설계·검증 항목(V0-1~V0-17)·작업 표(P0-T01~T21)는 [18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md)가 소유하고 여기서는 phase 정의·종료 gate·상한만 쓴다.

- **목표**: 사용자가 요청한 POC로서, 학습 없이(gradient 0회) 고정(frozen) 공개 가중치 LLM과 비모수 schema 기억(NP-0 텍스트 artifact schema, NP-1 잠재 artifact schema, 선택 NP-2 닫힌 꼴 선형 expert)만으로 전체 flow(입력 → 인식 → 경로 선택 → 계산 → 출력 → 결과 → 쓰기 → Sleep → 발견)를 실제 `fcl` CLI에서 끝까지 돈다. 이상형 feature마다 같은 계약의 비모수 대역(stand-in)을 두고, 이후 phase가 대역을 학습 모듈로 하나씩 바꾼다. §2의 뼈대(프로세스 경계, session 프로토콜, state store, 분리된 evaluator, 증거 원장)를 그대로 쓴다. **P0는 외부 frozen LLM을 쓰는 대역이며 최종형이 아니다**(§1.3 개정 주석). 동시에 mock이나 조사 단계가 아니라 실제 LLM·실제 저장·실제 CLI로 도는 완결 제품이다.
- **근거**: **USER:** 2026-11-18 요청의 「모델 학습없이 non parameter 기반의 무언가로 POC검증을 먼저 해보자」(원문 위치: [2026-11-18-discussion.md](/home/jimmy/repos/full-continual-learning/sources/sync/2026-11-18-discussion.md), 해석은 PROPOSAL). **LITERATURE·ARCHIVE:** frozen LLM 위의 기억 방법(kNN 기억, task·function vector 계열)의 확인 수준은 [18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md) §3.1에, Melete의 비모수 자산(저장·journal·임베딩 검색·조건부 learner·조건부 판단 benchmark)과 교훈(단순 대조군인 사례 기억이 강했다, ARCHIVE)은 같은 문서 §13에 있다. 이 교훈 때문에 P0는 NP arm이 같은 예산의 사례·검색 기억 대조를 넘는지를 먼저 본다. **PROPOSAL:** 아래 전부.
- **데모 시나리오**: **UJ0** (실제 `fcl` CLI, 실제 frozen 공개 가중치). UJ1의 ①–⑩ 전체를 NP arm으로 돈다: ① 세션 시작(arm·모델 revision·가중치 hash·backend 능력) → ② 경험 입력(k = 1/3/10) → ③ 상태 변화 관찰(`fcl diff`) → ④ 새 개체 질문과 경로 trace(fast/learn/deep/hold) → ⑤ 반례·정정(update·branch·create) → ⑥ 최초 과제 재평가 → ⑦ 이전 조건 재방문(ABA) → ⑧ 저장 → runtime 종료 → 재시작 → 복원 → 같은 응답 → ⑨ source 삭제(NP state 한정) → ⑩ `--arm`만 바꿔 NP arm과 대조군을 한 보고서에 나란히. 여기에 ⑪ Sleep(`fcl sleep`, 경험 후 대 경험 + Sleep 후) → ⑫ 발견 run(ET-0): 합성 미시 발견 세계의 stream을 시간순으로 넣고 긴장 원장을 열람하며 checkpoint마다 발견 곡선을 대조 stream과 나란히 본다 → ⑬ ET-3p run: 공개 시간캡슐 모델 위에서 같은 절차를 한 번 끝까지 돈다(시스템 안의 모든 생성·판정·검색이 그 모델만 쓰며 발견 여부는 주장하지 않는다) → ⑭ 보고서(결과 상태·등급 필드가 필수이고 등급에 맞지 않는 문구는 검사기가 막는다)를 더한다.
- **넓이 변화**: (기준선) 전체 여정을 학습 없이 가장 얇게 포함한다. NP 단 NP-0·NP-1(필수 arm)과 NP-2(선택. 「비모수」에 넣을지는 사용자 결정), 주 모델(8B급) 외에 P1 base급(135M급)에서 NP-1이 성립하는지의 확인, suite S-A(조건부 판단 세계. 2×2 표면/구조, 구조 family 2종), suite S-B(미시 발견 세계, ET-0), suite S-C(재분장한 역사 사례, ET-1 탐색), suite S-D(선택. frozen LLM 내부 schema 중첩 관찰), 대조 arm 약 20묶음(기억 없음·전체 이력·dense RAG·요약 기억·통찰·전략 기억 계열·개념 기억 계열·생명주기 없는 평면 schema·controller 없음·Sleep 없음·wrong-schema swap·oracle schema), 인터페이스는 CLI뿐, 단일 사용자·단일 writer.
- **깊이 변화**: (기준선) CRP식 사전과 정합도 우도로 read·update·branch·create·hold·evict를 판정하는 생명주기와 보존 예산 아래 eviction, 규칙형 controller(P1 controller v0의 fast·learn·deep에 hold를 더함), Sleep-NP(오프라인 군집·병합·추상화·재조합 후보·저장된 근거에 비춘 자가 검사), 긴장 원장(미해결 불일치 보존), source 삭제 계약, 관측과 생성물의 분리(NP-0의 추상화와 Sleep의 재조합 후보는 생성물이며 독립 관측 근거가 아님), 모델 호출 allowlist와 시간 필터(시간캡슐 모드), 사전 명세·봉인과 world 단위 paired bootstrap.
- **성립하는 보장**: Contract·Product 범위만. 시계 분리, 재전송 idempotency, 원자적 commit, 재시작 동등, 모델 revision mismatch 거부, 삭제 동등, version 되돌리기, 누수 audit(oracle 비노출), budget 일치(어긋난 실행은 INVALID), 생성물이 관측으로 승격되지 않음, 가중치 hash 불변, controller 결정이 관측 state에만 근거함, 모델 호출 allowlist(시간캡슐 모드에서 밖의 호출 0건), 시간 필터, probe 전후 시스템 상태 hash 동일. 사용자는 host에서 UJ0 전체를 끝까지 재현할 수 있다. Efficacy는 V0-1~V0-17의 결과 상태를 기록하는 데까지이며 PASS를 보장하지 않는다.
- **상한**: 주장 단위 등급 3(조건부). suite S-A·S-B의 개별 주장이 §3의 등급 3 조건(봉인 manifest, fresh locked cohort, 같은 계산·쓰기 예산의 대조, 구조 family 2종 이상, 사전 명세 충분 seed, 독립 검토)을 모두 채울 때만 3을 시도하고 그 밖의 P0 주장은 2 이하다. ET-1·ET-3p는 탐색이며 ET-3p의 절차는 등급 1(계약 통과)이다. ET 단별 문구는 [17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md) §3.2의 표가 기준이다. 쓸 수 없는 말: 가중치 수준의 schema 형성, 간섭 해소, 통합 모델의 내부 depth 효율, 「통합 모델이 필요하다」, 「학습 모듈이 NP보다 낫다」, 시간캡슐 모델 위에서 「발견했다」. 「실제 갱신」은 「실제 비모수 state 쓰기」로 읽는다(§3 보충 주석, OPEN).
- **종료 gate**: (1) **실제 인터페이스·실제 의존성 E2E:** 실제 `fcl` CLI·실제 frozen 공개 가중치 LLM·실제 NP state 쓰기·실제 디스크 저장·실제 runtime 프로세스 재시작으로 UJ0 전체(①–⑭)를 host에서 `np0`·`np1`(선택 `np2`)과 대조 arm으로 끝까지 실행한다(자동 E2E 스크립트, 증거 원장에 기록). ET-3p는 소형판이 host에서 완주해야 한다. mock만으로 돈 결과나 분리된 module 테스트만 통과한 상태는 완료가 아니다. (2) **앞 phase 회귀:** 앞 phase가 없다(P0(NP)가 첫 phase). 이 UJ0이 이후 모든 phase의 회귀 gate가 된다. (3) **자동 테스트(Contract):** 위 「성립하는 보장」의 항목 전부와 manifest 봉인 검사, 등급 문구 검사기가 PASS한다. (4) **효용 readout 상태:** 판정 대상 주장은 [18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md)의 V0-1~V0-17을 가리키며 여기서 문장으로 다시 쓰지 않는다. 각각의 결과 상태(PASS·FAIL·INCONCLUSIVE·BLOCKED·NOT RUN)와 주장별 등급이 보고서에 있어야 한다. 봉인된 sealed readout(등급 3 시도)을 종료 gate에 포함할지는 §10의 결정이다. 포함하지 않으면 dev pilot의 등급 2까지만 기록한다. PASS가 아니면 P1 진입 대신 §7의 분기와 [18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md) §14.2를 따르고 사용자에게 보고해 결정을 받는다. (5) **self-feedback:** B07 세 질문과 capability 표 재검토 기록(§11). P0 종료 선언은 (1)–(5)가 모두 기록된 뒤에 한다.
- **미루는 것**: 모든 gradient 학습, retrofit(NMM·CMS), 구조적 recursion(P2), 학습된 controller·halting(P3), 학습된 Sleep과 외부화 v0(P4), 외부 agent 연결(P5), 자연어 일반과 다른 모델 계열, 시간캡슐 기반에 System ONE을 얹는 ET-3(P5)와 봉인 주력 대상 ET-4(P6), 다중 사용자·동시 writer.
- **작업 단위**: 앞쪽은 계약과 spike이고(P0-T01~T05), 그 다음 뼈대를 먼저 연결한 뒤 해상도를 올리고 판정으로 닫는다. 작업 표(P0-T01~T21, 소요 시간·위치·계획 실행 횟수)와 종료 작업은 [18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md) §12가 소유한다. 요약하면 계약(T01~T03, P1-T01~T03의 설계 재사용), spike(T04 frozen LLM·backend·자원 실측, T05 NP-1 최소 hook), 세계 생성기와 뼈대 E2E(T06~T07, P1-T06·T07 설계 재사용), NP runtime과 arm(T08~T09), Sleep-NP·상태 계약·관찰과 인과 개입(T10~T12, P1-T10 설계 재사용), 평가 harness·source 삭제·발견 run(T13~T15, P1-T12 설계 재사용), 사전 명세와 봉인·sealed readout(T16~T17), ET-3p·탐색 suite·135M급 base 일치 확인(T18~T20), 종료(T21)다. 호스트 메모리 압박 때문에 무거운 실행은 한 번에 하나씩 직렬로 돌리고, host는 gate의 장소이며 runcrate는 대량 readout 전용이다. 가장 불확실한 작업은 T05(NP-1의 hook 성립), T08(NP-0 정합 판정이 작은 base에서 성립하는지), T16(dev pilot의 분산이 봉인 가능한 수준인지)이다.
- **범위 절삭 순서:** 일정·계산이 넘치면 suite S-D → NP-2 arm → 복제 모델 재현과 suite S-C 규모 → 보조 지표만 받치는 절제 arm 순으로 줄이고, 그다음 sealed readout의 world·seed 수를 줄인다(이 경우 등급 3 시도를 포기하고 등급 2로 보고). 절삭하지 않는 것: 실제 CLI E2E, `np0`·`np1` 두 arm, 기억 없음·평면 기억·항상 쓰기와 전체 이력·dense RAG 대조, 망각·표면/구조 평가, 생성물과 관측의 분리 검사, ET-0 소형 발견 run, ET-3p 소형판.

### P1 — 얇은 전체 여정 (MVP)

- **목표**: 작은 pretrained 언어모델을 retrofit한 하나의 모델이 `fcl` CLI에서 경험 입력 → 새 개체 질문 → 반례·정정 → 최초 과제 재평가 → 이전 조건 재방문 → 상태 저장 → 재시작 복원 → source 삭제의 전체 여정을 처음부터 끝까지 돈다. 질문마다 규칙형 controller v0가 익숙함 신호로 fast·learn·deep 경로를 고른다(U-T07의 핵심 거동을 가장 얇게). 같은 여정이 같은 계산·쓰기 예산의 대조군(고정·무구조·항상-갱신)과 같은 CLI·같은 실제 경로로 돌아 나란히 비교되고, 망각과 표면/구조 평가가 처음부터 포함된다. 효용(Efficacy)은 사전 명세 readout의 상태를 기록하는 데까지가 P1이다.
- **근거**: **USER:** B02·B05·B11·B14·B16·B17(§1.1). **LITERATURE:** [2026-11-11-sbl-fulltext-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext-review.md) §4.1(학습된 구조의 이득이 같은 예산의 고정·무구조 대조와 직접 비교되지 않았다), §4.4(망각·표면/구조·계산량이 잘 측정되지 않았다), §5 DQ3·DQ6·DQ7. **ARCHIVE:** Melete의 제품 P1 실험용 MVP도 같은 규칙으로 실제 CLI·실제 LLM·실제 tool의 E2E를 종료 gate로 삼았다([2026-10-15-neural-judgment-roadmap.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/superpowers/plans/2026-10-15-neural-judgment-roadmap.md)). SmolLM2-135M-Instruct는 Melete E5에서 host CPU로 실행한 이력이 있다([2026-10-07-e5-self-feedback.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/implementation/records/2026-10-07-e5-self-feedback.md)). **PROPOSAL:** 아래 전부.
- **P1의 실제 일**: **PROPOSAL (구조 family는 OPEN, D-03).** 작은 관계 구조 세계를 자연어로 렌더링한 경험과 질문이다. 기본 후보는 "역할–결과 규칙 세계"(조건 A·B에 따라 같은 동사 표면이 다른 결과 규칙을 갖는 세계)다. 규칙 문장은 주지 않고 경험(관측 사례)만 준다. 개체 이름은 nonce로 매번 바꾸고 표면 template은 학습용과 평가용 paraphrase를 분리한다. 질의는 "이 조건에서 어떤 결과·판단이 맞는가"이며(B16) 미래 결과 예측 정확도가 아니다. [08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md)의 F01·F02·F03·F05·F06과 review §5 DQ6의 H-SAMPLE 틀(관측 0/1/3/10에서의 목표 성능, 표면과 구조를 분리한 lure)에 맞춘다.
- **데모 시나리오**: **UJ1** (실제 `fcl` CLI, 실제 가중치). ① 세션 시작: arm·모델 revision·state 버전이 표시된다 → ② 경험 입력: 작은 관계 구조 세계의 관측 k개(k = 1/3/10)를 자연어로 입력한다 → ③ schema/binding 상태 변화 관찰: `fcl diff`가 layer·module별 변화량·clock·write 수를 보이고 같은 probe 질문의 응답이 전/후로 비교된다 → ④ 새 개체(경험에 없던 이름·값·표면, 새 역할 결합)에 대한 질문에 실제 모델이 응답하고, 응답마다 controller v0가 고른 경로(fast/learn/deep)·신호값·예산이 trace로 보인다 → ⑤ 반례·정정 입력: 규칙에 맞지 않는 사례를 주고 국소 갱신한다 → ⑥ 최초 과제 재평가: 정정 전에 처음 평가한 질의 묶음(최초 과제)을 다시 던져 망각을 측정한다 → ⑦ 이전 조건 재방문: 조건 A→B→A에서 A의 질의를 수정 없이 다시 던진다(ABA) → ⑧ 상태 저장 → runtime 프로세스 종료 → 재시작 → 복원 → 같은 질문에 같은 응답 → ⑨ source 삭제: 특정 경험 source를 철회·재구성하고 그 source가 만든 효과가 사라졌는지 본다(fast state 한정) → ⑩ 같은 시나리오를 `--arm`만 바꿔 고정·무구조·항상-갱신·`noctl`·`ctx`·`base`로 반복하고 한 보고서에 나란히 놓는다(등급 2 표기).
- **넓이 변화**: (기준선) 여정의 모든 단계를 가장 얇게 포함한다. 구조 family 1종과 표면 lure, 소형 pretrained 모델 1종, retrofit은 일부 layer(sequence 1–2개, FFN 1–2개. 전 층 아님), 깊이는 controller v0의 r∈{1,2}뿐, 단일 사용자·단일 writer, 인터페이스는 CLI뿐이다. arm은 `full`(대상)과 대조 6개다. 고정(`fixed`: 같은 모듈·같은 write 예산이지만 구조 파라미터를 학습하지 않음), 무구조(`flat`: 같은 용량·같은 write 예산의 단일 평면 fast memory, 레벨·역할/조건 분리 없음), 항상-갱신(`always`: 같은 모듈이지만 write gate를 끄고 예산이 허용하는 만큼 항상 씀), controller 없음(`noctl`: 같은 모듈·같은 write 예산이지만 controller v0 없이 모든 질문을 learn 경로·r=1로 처리해 경로 선택의 기여를 분리), `ctx`(경험을 prompt에 넣은 같은 base), `base`(경험 없이 직접 응답). 정확한 정의와 예산 일치 규칙은 P1-T03에서 결과를 보기 전에 봉인한다.
- **깊이 변화**: (기준선) 각 단계의 최소 깊이다. 쓰기는 Titans식 surprise write 하나와 항상-갱신 대조, 정정은 국소 갱신과 부작용 측정(수정 메커니즘 없음), 평가는 2×2 표면/구조 + 최초 과제 재평가·이전 조건 재방문의 망각 측정 + 원능력 probe + 사전 명세 readout, 저장은 bundle v0·원자적 commit·replay 삭제, 경로 선택은 규칙형 controller v0(두 임계값)이고 계산은 측정만이다.
- **성립하는 보장**: Contract·Product 범위만. (1) 같은 입력 재전송은 같은 root로 한 번만 반영된다. (2) 시계(경험·token·optimizer·wall)가 분리 기록되고 내부 loop·replay는 새 evidence로 세지 않는다. (3) commit은 원자적이고 재시작 전후 같은 snapshot에서 응답이 허용오차 안에서 같다. (4) 모델 revision이 다르면 복원을 거부한다. (5) 삭제 뒤 state는 그 source 없이 같은 순서로 재생한 state와 허용오차 안에서 같다(fast state 한정). (6) 모든 arm이 같은 CLI·같은 실제 경로·같은 단위의 budget 기록으로 돌고 예산이 어긋난 실행은 INVALID다. (7) evaluator 전용 oracle은 learner에 노출되지 않는다. 사용자는 CLI에서 전체 여정을 끝까지 수행할 수 있다. Efficacy는 "사전 명세 readout의 상태를 기록한다"까지만 보장하며 PASS를 보장하지 않는다.
- **상한**: 등급 2(개발 pilot: 합성·단일 구조 family·소형 모델 1종·제한 seed·부분 retrofit). 사전 명세 readout이 PASS여도 "schema 이득"·"개선"·"일반화"·"빠른 판단"·"계산 절감"이라 쓰지 않는다(등급 3부터). 쓸 수 있는 말은 "이 합성 pilot에서 사전 명세 대조를 통과(미달)했다"까지다. 대조군 우위가 사전 명세 통계로 확인되기 전에는 schema 이득이라 쓰지 않는다. 깊이가 규칙형 경로의 r∈{1,2}뿐이므로 H-COMPUTE는 시험하지 않는다(경로 분포와 계산량은 측정만. H-SAMPLE·H-COMPUTE의 정의는 [01-intent-and-charter.md](/home/jimmy/repos/full-continual-learning/docs/01-intent-and-charter.md) §4). Sleep·slow 통합이 없으므로 삭제는 fast state에 한정한다. 부분 layer 결과를 all-layer 성공으로 확대하지 않는다. P1-T05에서 NMM 경로가 실패하면 CMS 분기만으로 P1을 종료하되 sequence memory 행은 "없음"으로 남기고 문구에 밝힌다. "schema/binding 상태 변화 관찰"은 상태가 바뀌었다는 관찰이지 schema 형성의 증거가 아니다. controller v0는 dev에서 정한 임계값 규칙이므로 "학습된 schema 판단"·"적응 계산"이라 쓰지 않는다.
- **종료 gate**: (1) **실제 인터페이스·실제 의존성 E2E:** 실제 `fcl` CLI에서 실제 pretrained 가중치·실제 test-time write·실제 디스크 저장·실제 runtime 프로세스 재시작으로 UJ1 전체를 `full`과 대조 6 arm 모두에 끝까지 실행한다(자동 E2E 스크립트, 증거 원장에 기록. mock-only 결과와 분리된 module 테스트만 통과한 상태는 완료가 아니다). (2) **앞 phase 회귀:** 앞 phase가 없다(P1이 첫 phase). 이 UJ1이 이후 모든 phase의 회귀 gate가 된다. (3) **자동 테스트:** 시계 분리·재전송 idempotency·원자적 commit·재시작 동등·revision mismatch 거부·삭제 동등·누수 audit·budget 일치·함수 보존·manifest 봉인 검사와 controller v0 결정이 관측 state에만 근거한다는 검사가 전부 PASS한다(Contract). (4) **효용 기록:** P1-T15의 결과 상태와 등급 2 보고서가 있다. PASS가 아니면 P2 진입 대신 §7 분기를 따른다. (5) **self-feedback:** B07 세 질문과 capability 표 재검토 기록(§11). P1 종료 선언은 (1)–(5)가 모두 기록된 뒤에 한다.
- **미루는 것**: r>2 depth 격자·학습된 controller·halting, fit 결합 write gate·accommodation 메커니즘, Sleep·slow 통합, 외부화(offload/version/retrieval), 외부 agent 연결, 두 번째 base model·자연어 혼합 도메인, 자동 self-evolution 루프, 다중 사용자·동시 writer, 큰 모델(8B급).
- **작업 단위**: 앞쪽은 연구 계약(옛 P0 흡수)과 spike이고, 그 다음 뼈대를 먼저 연결한 뒤 해상도를 올리고 판정으로 닫는다. 호스트 메모리 압박 때문에 무거운 실행(T04·T09·T15)은 한 번에 하나씩 직렬로 돌린다.
  - **P1-T01 계약: 용어·시계·source 경계 (옛 P0 흡수).** [07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md) §1의 시계 필드와 source/root 규칙(같은 입력 재전송 = 같은 root, generated 해석은 observed로 승격하지 않음, 내부 loop·replay는 새 evidence가 아님)을 타입과 실패부터 쓰는 테스트 목록으로 고정한다. **완료 판정:** 시계 혼동 금지 항목마다 실패하는 테스트가 존재하고 용어 표가 문서에 있다.
  - **P1-T02 계약: 평가 (옛 P0 흡수).** 세계·history·질의 단위 split([08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md) §7), learner view와 evaluator 전용 oracle 분리, 조건부 판단 질의, 2×2 표면/구조 설계, 보존 probe(최초 과제 재평가·ABA·원능력), 결과 상태·등급 어휘, manifest 서식을 정한다. query 반복을 독립 표본으로 늘리지 않는다. **완료 판정:** 무정보 learner(상수·무작위 응답)가 evaluator에서 chance 수준이고 oracle 누수 audit이 0건이다.
  - **P1-T03 계약: budget·대조군 (옛 P0 흡수).** write 수·optimizer step·forward/backward·token·FLOPs 추정·wall의 단위, arm 정의표(고정·무구조·항상-갱신·`noctl`·`ctx`·`base`), 예산 일치 허용오차를 결과를 보기 전에 정한다. **완료 판정:** arm 정의표와 허용오차가 hash로 고정되고, 예산이 어긋난 실행을 evaluator가 INVALID로 거부하는 테스트가 있다.
  - **P1-T04 spike: base model·자원.** §10의 후보 중 하나(기본 SmolLM2-135M)로 host CPU와 노트북 GPU에서 forward/backward·test-time write의 메모리·step 시간을 소배치로 실측하고, Titan-Llama pin(`c60b4efa…`)의 코드를 읽어 라이선스를 확인하며 식에서 재구현하는 경로와 비교한다. **완료 판정:** 실측 표와 선택 근거가 기록되고 D-01·D-02가 사용자 결정 요청으로 올라가 있다(결정 전에는 읽기·인용과 재구현 경로로만 진행한다).
    - **(2026-11-17 PROPOSAL) 추정 보정 절차:** 실측은 ① host·노트북 → ② 사용자 비용 승인 시 runcrate 후보 GPU 1–2종의 짧은 microbenchmark(ESTIMATE: 2 인스턴스 약 3.7 GPU-시간, P50 약 $7.6, 상한 $12) → ③ 결과로 [15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md)의 작업량 표 갱신 순서로 한다. 위 완료 판정은 바뀌지 않으며 클라우드 단계는 비용 승인 전에는 하지 않는다.
  - **P1-T05 spike: 최소 retrofit.** 1–2개 layer에 NMM 경로, 1–2개 FFN에 CMS 분기(B_j=0)를 붙여 (i) 초기 출력이 base와 허용오차 안에서 같은지(함수 보존), (ii) 새 모듈이 freeze되지 않는지(trainable-name 규칙, [05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §6), (iii) test-time write가 실제 state를 바꾸는지 확인한다. **완료 판정:** 세 검사가 자동 테스트로 PASS하거나, 실패 원인과 축소 범위(예: NMM 제외·CMS 분기만)가 사용자에게 보고되고 P1 상한 문구에 반영돼 있다.
  - **P1-T06 세계 생성기와 renderer (D-03).** 구조 family 1종 × 개체 이름 pool × 표면 template, 학습용 renderer와 평가용 paraphrase renderer 분리, 규칙 문장 없이 경험만 렌더링, train/dev/sealed world의 seed 분리(sealed cohort는 T14 봉인 뒤에 만든다). **완료 판정:** seed → 같은 hash로 결정론 재생, 관측 0/1/3/10별 식별 가능 질의 비율 보고, 누수 audit 0건.
  - **P1-T07 뼈대 E2E (walking skeleton).** `fcl` CLI와 runtime을 별도 프로세스로 두고 session 프로토콜을 정의한다. 실제 pretrained 가중치를 로드해 `base`·`ctx` arm으로 경험 입력 → 질문 → 응답 → 저장 → runtime 종료 → 새 프로세스 복원을 한 줄기로 잇는다. **완료 판정:** mock 없이 실제 가중치로 돈 E2E 스크립트의 증거 원장 기록과 재시작 전후 프로세스 ID 변경이 있다. 같은 경로로 `base`·`ctx`의 dev 세계 ceiling/floor와 copy baseline을 보고한다(ceiling이나 floor에 붙어 있으면 dev에서만 난이도를 조정하고, 통과 전에는 T14 봉인으로 가지 않는다).
  - **P1-T08 retrofit runtime과 arm.** T05의 모듈을 runtime에 통합하고 committed snapshot → request-local working state → commit write engine(write 정책 접점 포함: Titans식 surprise 정책과 항상-갱신 정책), 규칙형 controller v0(익숙함 신호 두 임계값 → fast/learn/deep, deep = retrofit 블록 r=2)와 결정 trace 필드, 시계 기록, budget meter, `--arm`(`full`·`fixed`·`flat`·`always`·`noctl`) 전환을 구현한다. **완료 판정:** 같은 CLI·같은 session 프로토콜에서 `--arm`만 바꿔 다섯 arm이 돌고 응답마다 결정 trace가 남으며 원장에 arm별 write 수·step·FLOPs 추정이 같은 단위로 남으며, 각 arm이 T03 정의와 일치함을 검사하는 테스트가 PASS한다.
  - **P1-T09 retrofit 학습 (outer loop).** 평가 세계와 분리된 train world로 NMM·CMS 모듈을 학습해 test-time write가 query loss를 줄이게 하고, deep 경로의 r=2 적용에 대한 짧은 적응 학습(retrofitted recurrence의 최소형)을 같은 예산 안에 포함하고 arm별 checkpoint를 만든다(`fixed`는 학습하지 않고 나머지는 같은 학습 예산). 계산 장소·예산은 D-04. **완료 판정:** arm별 학습 예산·곡선이 원장에 있고, 학습 뒤 원능력 probe(일반 텍스트 perplexity·비세계 질문)가 base 대비 값으로 기록돼 있다(임계 판정은 T14 봉인 뒤이며 효용 판정이 아니다).
  - **P1-T10 상태 계약 구현.** bundle manifest v0([07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md) §5의 부분집합), 원자적 commit, 복원, 모델 revision mismatch 거부, 최소 상태 회귀(재전송·같은 ID 다른 payload·중단된 update·restart·rollback·삭제·mismatch·동시 write 거부)를 구현한다. **완료 판정:** 저장 → runtime 종료 → 복원 뒤 같은 질문의 응답과 log-prob이 허용오차 안에서 같고, 위 회귀가 자동 테스트로 PASS한다(Contract 한정).
    - **OPEN (2026-11-17 검토; [13-schema-decomposition-and-interference.md](/home/jimmy/repos/full-continual-learning/docs/13-schema-decomposition-and-interference.md) §7.3):** 위 「허용오차」(보장 (3)·(5), T05의 함수 보존, T13의 삭제 동등 포함)의 값은 bit 동일성이 아니다. GPU의 부동소수점 비결합성·kernel 선택·batch 구성(batch invariance 부재)으로 같은 입력의 출력이 batch마다 다를 수 있기 때문이다. T14 봉인 전에 변경 없는 checkpoint를 batch 구성·순서·장치만 바꿔 재실행해 noise floor $\nu$를 재고, 허용오차는 $\nu$보다 작게 약속하지 않는다. 같은 장치·같은 batch 형태·결정적 모드에서는 $\nu$가 0에 가까울 수 있으나 측정 전에는 가정하지 않으며, 장치를 바꾸는 복원(예: D-04의 CPU와 GPU)에서는 $\nu>0$이 예상된다. 쓰기 집합 밖 state가 byte 동일한지의 해시 검사는 수치 비결정성과 무관하게 정확히 할 수 있다. 이 측정을 어느 작업 단위(예: T04 spike)에 넣을지는 정해지지 않았다.
  - **P1-T11 관찰과 인과 개입.** `fcl diff`(layer·module별 변화량·clock·write 수), probe 질문의 전/후 응답 분포, wrong-schema state swap(다른 세계의 state를 복원 경로로 이식해 같은 질문을 던짐)을 구현한다. **완료 판정:** arm 정의표가 "바뀌어야 한다/바뀌면 안 된다"고 한 state 집합의 diff가 그대로 관측된다는 테스트가 PASS한다(관찰 가능성 검사이며 schema 형성의 증거가 아니다).
    - **OPEN (2026-11-17 검토; [13-schema-decomposition-and-interference.md](/home/jimmy/repos/full-continual-learning/docs/13-schema-decomposition-and-interference.md) §9.1):** 「바뀌면 안 된다」 state 집합에 optimizer momentum·update counter·감쇠가 닿는 state·공유 통계(norm 통계 등)를 포함하는 검사를 후보로 둔다. [06-mathematical-framework.md](/home/jimmy/repos/full-continual-learning/docs/06-mathematical-framework.md) §3의 빠른 업데이트 식은 감쇠·momentum이 $\gamma$로 gate되지 않아 선택되지 않은 상태도 바꾼다. 이 검사는 쓰기 격리를 주장하는 arm에만 필요하고 P1의 등급과 데모 시나리오를 바꾸지 않는다.
  - **P1-T12 평가 harness와 보고서.** dev world에서 UJ1 전체를 모든 arm으로 자동 실행(`fcl eval`)하고 지표를 낸다: 새 개체 전이(관측 0/1/3/10), 표면 함정 negative transfer(2×2), 반례 뒤 국소 수정과 최초 과제 재평가(망각), 이전 조건 재방문(ABA), 원능력 보존, both-correct condition pairs. 보고 생성기는 결과 상태와 등급을 필수로 찍고 등급에 맞지 않는 문구를 검사기로 막는다. **완료 판정:** 모든 arm이 같은 형식의 보고서를 내고 등급 필드가 "등급 2"로 찍히며, 금지 문구 검사기가 시험 문서에서 작동하고, dev 결과로 모든 arm의 ceiling/floor 판정이 보고서에 있다.
  - **P1-T13 source 수정·삭제 (얇게).** 삭제 = source 원장에서 철회한 뒤 committed snapshot에서 남은 source를 같은 순서로 재생해 재구성한다. 수정 = 삭제 + 같은 위치에 다시 삽입. slow 통합이 없으므로 fast state 한정이며 통합 후 삭제는 약속하지 않는다고 보고서에 적는다. **완료 판정:** 삭제 뒤 state가 "그 source 없이 처음부터 재생한 state"와 허용오차 안에서 같고, 삭제 전후 해당 질문의 응답 변화(또는 변화 없음의 사유)가 기록되며, 이 단계가 harness의 UJ1 ⑨로 자동 실행된다.
    - **용어 주의 (2026-11-17 검토, PROPOSAL):** 이 작업의 '삭제'는 source 삭제(철회·재구성)다. [14-schema-lifecycle-crud-and-joint-paper.md](/home/jimmy/repos/full-continual-learning/docs/14-schema-lifecycle-crud-and-joint-paper.md) §4의 Delete/Retain(예산 아래 압축·통합·폐기로 기능 손실을 치르는 기능적 망각/보존)과 다른 개념이며 P1은 후자의 정책을 약속하지 않는다. P1의 망각 평가(최초 과제 재평가·ABA·원능력)는 후자의 비용을 재는 측정이다. 구분표는 [07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md) §7, CRUD 대응은 §4-1을 본다.
  - **P1-T14 사전 명세와 봉인.** dev pilot의 분산·식별 가능 질의 수로 primary 지표·통계 방법·multiplicity·최소 효과·seed 수·candidate 수 상한·예산 허용오차·보호 지표(재평가·ABA·원능력) 임계와 controller v0의 두 임계값을 manifest에 쓰고, 구현자와 다른 reviewer의 검토를 받은 뒤 hash로 봉인하고, 그 뒤에 sealed cohort를 만든다. 수치는 이 문서에 없고 여기서 처음 정해진다(D-05). **완료 판정:** 봉인 hash 시각이 sealed cohort 생성 기록보다 앞서고, 평가 코드가 manifest hash 불일치 시 실행을 거부한다. 봉인의 선행 조건은 T07·T12의 ceiling/floor 통과와 `fixed`가 floor가 아님의 확인이다.
  - **P1-T15 sealed readout.** 봉인된 manifest대로 모든 arm을 seed × world 단위로 한 번 실행하고 결과 상태(PASS/FAIL/INCONCLUSIVE), 등급 2 문구, 실제 비용(실패·취소 포함)을 기록한다. 같은 sealed cohort를 다른 candidate에 재사용하지 않는다. **완료 판정:** 보고서가 manifest의 모든 지표를 상태와 함께 담고, 사후에 임계·subset을 바꾼 흔적이 없음을 원장이 보인다.
  - **P1-T16 종료.** UJ1을 `full`과 대조 6 arm으로 실제 CLI·가중치·write·저장·재시작 경로에서 끝까지 자동 실행하고, 계약 테스트를 일괄 실행하고, 재현 절차 문서(설치·가중치 확보·실행)를 새 디렉터리에서 그대로 따라 UJ1이 돌게 하고, B07 세 질문과 capability 표 재검토를 기록한다. **완료 판정:** 위 종료 gate 전 항목이 PASS로 기록되거나, FAIL 항목이 §7 분기에 올라가 있다.
  - **범위 절삭 순서:** 일정·계산이 넘치면 T13(삭제)을 P2로 옮기고, 그다음 readout의 seed 수를 줄인다(등급은 2로 유지). 절삭하지 않는 것: 실제 CLI E2E, controller v0의 세 경로, 고정·무구조·항상-갱신 대조, 망각·표면/구조 평가.
- **2026-11-18 개정 주석 (PROPOSAL)**: 위 P1의 목표·데모 시나리오 UJ1·성립하는 보장·상한·종료 gate·미루는 것은 바뀌지 않았다. P0(NP)가 앞에 생기면서 달라지는 것은 셋이다. (1) **P0가 먼저 쓰는 작업:** P1-T01(용어·시계·source 경계)·T02(평가)·T03(budget·대조군)·T06(세계 생성기)·T07(뼈대 E2E)·T10(상태 계약)·T12(평가 harness)은 P0(NP)가 NP 단위로 먼저 구현한다([18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md) §12의 「재사용: P1-Txx 설계」 항목). P1은 같은 설계를 이어 받아 retrofit arm에 필요한 추가분을 더하고 P0가 더한 NP 쪽 추가분을 다시 확인한다. 위 작업의 정의와 완료 판정은 바뀌지 않는다. (2) **NP arm이 영구 대조군:** P1의 readout 보고서에는 P0의 NP arm(`np0`·`np1`)을 같은 CLI·같은 base·같은 예산 일치 규칙으로 돌려 대조군으로 더한다. P1의 arm 7개(`full`과 대조 6개)와 종료 gate (1)의 「대조 6 arm」은 바뀌지 않는다. base가 작아 NP-0이 성립하지 않으면 그 사실을 보고하고 NP-1을 대조로 쓴다. 이 추가는 P1의 상한(등급 2)을 바꾸지 않는다. (3) **회귀와 ET 단:** 회귀 gate에 UJ0이 더해진다(§6 보충 행). ET 단은 판정 대상 ET-0(학습 arm 대 NP arm), 회귀 ET-3p다([17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md) §3.1). 결정 후보: hold 경로를 controller v0에 넣을지(D-14와 연결), P1 base 크기(D-01과 연결), 「P1은 MVP」 해석(§1.4 보충 주석)은 §10에 있다.

### P2 — 여러 구조와 고정 깊이로 넓히고 첫 확증

- **목표**: 같은 제품·같은 CLI에서 구조 family를 3종으로 넓히고 계산 깊이 축(고정 depth 격자)을 더해 경험 전/후의 quality–compute 곡선을 처음 측정하며, P1의 핵심 대조에 대한 첫 한정 확증(등급 3)을 시도한다.
- **근거**: **USER:** B02·B11·B17. **LITERATURE:** review §5 DQ1·DQ5(고정 깊이의 품질–계산 곡선이 먼저)·DQ6, [05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §7(Retrofitted Recurrence [A13], ETD [A14], Relaxed Recursive Transformers [A15]), [08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md) §3 대표 실험. **PROPOSAL:** 아래 전부.
- **데모 시나리오**: **UJ2** (CLI): 구조 family 3종 중 둘의 세계를 번갈아 경험하고(조건 A→B→A 포함) 같은 질문을 `--depth 1/2/4`로 던져 정확도와 계산량을 나란히 본다. 경험 전(S0)·후(SE)의 quality–compute 곡선이 표시된다. `fcl eval`이 모든 arm × depth를 배치로 돌려 한 보고서를 낸다. UJ1 전체를 그대로 다시 돌려도 통과한다.
- **넓이 변화**: 구조 family 1 → 3종(앞 family는 회귀용으로 유지, lure 확대), retrofit layer 확대(전환마다 회귀), depth 축 신설(`--depth`), 배치 평가(`fcl eval`·compare·session transcript), 참고선 Qwen3-8B+raw history(크기가 달라 대조군이 아니라 참고선).
- **깊이 변화**: 첫 확증(봉인 → fresh cohort → 독립 evaluator 프로세스), 조작적 증거 2종(subspace 재사용·변화량 감소), 예외·ABA family 확대와 보호 영역 대조(slow 동결 대 fast만 쓰기), savings·family별 negative transfer, 계산량 정밀화(depth별 FLOPs·p50/p95·TTFT·메모리, write 예산 u 격자), self-evolution v1.
- **주요 작업 묶음**: **A. spike** — recurrence retrofit 가능성(depth별 adapter/LoRA·중간 depth loss). 한 번도 반복 학습하지 않은 모델의 단순 재호출은 후보가 아니다. 실패하면 depth 축을 P3로 이월하고 P2는 나머지로 종료한다. **B. 세계·평가 v2**(구조 family 3종, lure, F05·F06 확대, F07 최소). **C. retrofit 확대**(layer 수 증가, 전환마다 원능력·state·성능 회귀). **D. depth 축**(고정 grid 학습·측정, `--depth`, depth 시계·causal mask·stale cache 검사). **E. 확증 준비·실행**(봉인, fresh cohort, 시도 수·multiplicity 기록). **F. self-evolution v1**(후보 manifest([10-evolution-policy.md](/home/jimmy/repos/full-continual-learning/docs/10-evolution-policy.md) §3) + 독립 evaluator + 후보 archive. 후보 제안·승인은 사람).
- **성립하는 보장**: UJ1 회귀 유지. depth 시계 분리(recursion index가 token position·경험 수를 늘리지 않음), autoregressive mask가 미래 token·depth 상태를 노출하지 않음, 가중치 갱신 뒤 stale cache 정합성 검사([07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md) §3). 계산량 기록이 encoder·core loops·write/backward를 포함한다. 확증 통계는 사전 명세다. 후보가 evaluator·oracle·split을 수정하지 못하도록 권한이 분리된다.
- **상한**: 등급 3 한정(합성 family 3종·소형 모델 1종·사전 명세 seed). depth 곡선과 조작적 증거는 봉인 확증을 거친 것만 3이고 아니면 2다. controller가 규칙형 v0뿐이므로 "적응 계산"을 약속하지 않는다. 동일 입력 재호출이나 무의미한 loop 증가를 개선으로 세지 않는다. 경험 전/후 곡선의 이동은 H-COMPUTE의 일부(경험 효과)일 뿐이며, 통합(Sleep) 이후의 계산 절감은 P4 전까지 주장하지 않는다. Sleep 없음. Qwen3-8B 참고선에는 등급을 매기지 않는다.
- **후보 readout (OPEN, 2026-11-17 검토; 종료 gate·등급 판정에 넣지 않음)**: depth 격자 평가에서 같은 (r, u) 셀의 현재 질의 정확도와, 같은 모델이 연속 갱신(외부 관측 갱신, 자기 생성 token 되먹임)을 거친 뒤의 같은 질의 정확도를 함께 기록하는 F-CI([08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md))를 측정만 시도한다. depth 격자는 recursion 시계 축이고 F-CI의 갱신 길이는 token(경험) 시계 축이므로 두 축을 섞지 않는다. 결과는 등급 2 상한이며 P2의 종료 gate·미루는 것·상한을 바꾸지 않는다. H-COMPUTE의 같은 정확도 비교는 현재 질의 정확도 기준이고 이 readout이 그 정의를 바꾸지 않는다. 근거는 조건부 이론 결과의 인접 선행(arXiv:2611.13760)이며 이 로드맵의 설계 제약이 아니다.
- **종료 gate**: (1) **UJ2 E2E:** 실제 CLI·가중치·write·저장·재시작으로 arm × depth를 끝까지 실행(mock 불인정). (2) **앞 phase 회귀:** UJ1 전부(`full`과 대조 6 arm). (3) **자동 테스트:** depth 시계·mask·stale cache·layer 확대 회귀(원능력)·manifest 봉인·권한 분리(후보가 evaluator·oracle·split을 못 바꿈)가 PASS. (4) 등급 3 readout의 결과 상태 기록(PASS가 아니면 §7). (5) B07 세 질문과 capability 표 재검토.
- **미루는 것**: 학습된 controller·halting·fit 결합 write gate·accommodation 메커니즘, Sleep, 외부화, 외부 agent 연결, 두 번째 base model, 자연어 도메인.
- **2026-11-18 개정 주석 (PROPOSAL)**: 위 P2의 목표·UJ2·보장·상한·종료 gate·미루는 것은 바뀌지 않았다. NP arm은 P2의 base 모델로 다시 돌아 영구 대조군으로 남는다(같은 예산 일치). depth 축의 NP판은 숙의 반복 수·생성 token·LLM 호출 수이며 구조적 recursion은 P2부터다. ET 단은 판정 대상 ET-0 깊이 곡선, 탐색 ET-1이다. 회귀 gate에 UJ0이 더해진다(§6 보충 행).

### P3 — 스스로 고르는 모델 (controller·선택적 쓰기·accommodation)

- **목표**: P1의 규칙형 controller v0를 학습된 controller로 바꿔, 같은 제품에서 모델이 문맥·경험에 따라 스스로 고르게 한다. 문맥 수준(어떤 구조를 적용·전환·조합·수정할지)과 실행 수준(어느 token·block, 어느 depth source, write 횟수·강도, 종료)의 controller, fit·친숙도와 결합한 선택적 write(P1부터 있는 write 정책 접점에 꽂는다), accommodation을 넣는다.
- **근거**: **LITERATURE:** review §4.2(새로움·일치도 신호가 바꾸는 대상이 논문마다 다른 다섯 기제), §4.3(구조를 실행 중에 고치는 논문은 없다), §5 DQ2·DQ3·DQ5(논문 ID는 review §1 표 기준: SWAMI23의 선택적 갱신 마스크에서 출발, MICONI25의 학습된 neuromodulator는 더 강한 후보, SPENS24의 "예외만 따로 저장"), [04-rhythms-and-orchestration.md](/home/jimmy/repos/full-continual-learning/docs/04-rhythms-and-orchestration.md) §6, [05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §4. **USER:** U04·U09(§1.2), H2·H3의 familiarity 기반 빠른 처리와 hit 경로 강화(B14). **PROPOSAL.**
- **데모 시나리오**: **UJ3** (CLI): 같은 세션에서 익숙한 질문은 얕게 답하고, 낯선 binding은 write한 뒤 답하고, 구조가 어긋나면 더 깊게 계산하거나 보류하는 모습이 결정 trace(fast/learn/deep)와 예산으로 보인다. UJ1·UJ2를 그대로 돌려도 통과한다.
- **넓이 변화**: controller 입력 신호(구조 적합성·prediction residual·observed/generated 구분·불확실성)와 출력(적용·전환·보류·질문), 새 구조(F04)·불확실성(F09)·지연 피드백 일부(F08), lure 확대, CMS 조율 계열 대조(고정 주기·frequency-adaptive·event/readiness).
- **깊이 변화**: write gate를 무엇·어디·얼마나·언제로 분해해 ablation, halting(적응 깊이), accommodation 메커니즘, 조작적 증거 3종째(표현 제거·교체), controller 비용 포함 total cost.
- **성립하는 보장**: 결정이 관측 가능한 state에만 근거한다(router가 아직 생성되지 않은 token을 참조하지 않음). controller·router 비용이 계산량에 포함된다. 보호 family가 퇴행하면 자동으로 멈춘다.
- **상한**: 등급 3. 쉬운 사례만 골라 평균 depth를 줄인 결과를 계산 효율 개선으로 쓰지 않는다(난이도 층화 필수). controller는 구성 요소이며 정답 oracle이 아니다. 위상(phase) 조율(D)은 event/readiness(C)를 기준선으로 확보한 뒤에 D 대 C로 비교하며 P3에서는 C까지만 다룬다([04-rhythms-and-orchestration.md](/home/jimmy/repos/full-continual-learning/docs/04-rhythms-and-orchestration.md) §6, [11-research-agenda.md](/home/jimmy/repos/full-continual-learning/docs/11-research-agenda.md) §5). 동기 실행에서 단순 stage ID와 같은 효과이면 새 원리라고 부르지 않는다. Sleep 없음.
- **종료 gate**: (1) **UJ3 E2E:** 실제 CLI·가중치·write·저장·재시작에서 결정 trace가 나오고 저장·복원 뒤에도 같은 결정이 재현된다. (2) **앞 phase 회귀:** UJ1·UJ2 전부. (3) **자동 테스트:** router 인과성, controller 정책 변경이 관측 state에 근거함, bundle에 제어 상태 포함, 보호 family 자동 중단. (4) 등급 3 readout: controller 대 고정 depth·novelty-only·learned early exit·random gate를 같은 품질·같은 예산에서 사전 명세로 판정. (5) B07 세 질문과 capability 표 재검토.
- **미루는 것**: Sleep·공고화, 외부화, 외부 agent 연결, 두 번째 base model·자연어 도메인, 위상 조율(D) 실험(P3 종료 재검토에서 C를 기준선으로 배치를 결정, D-13).
- **2026-11-18 개정 주석 (PROPOSAL)**: 위 P3의 목표·UJ3·보장·상한·종료 gate·미루는 것은 바뀌지 않았다. 학습된 controller는 P0의 규칙형 controller(hold 포함)와 같은 예산에서 비교하며, 그 규칙형 controller가 NP arm에 남는다. ET 단은 판정 대상 ET-1(재분장 사례, 오염 probe 병기), 탐색 ET-2다. 발견·통찰 feature의 학습 모듈을 어느 phase에 두는지는 §10의 결정이다. 회귀 gate에 UJ0이 더해진다(§6 보충 행).

### P4 — 세션을 넘는 경험 (Sleep·외부화 v0)

- **목표**: 경험이 세션을 넘어 남게 한다. Sleep(fast → slow 공고화)과 외부화 v0(bundle export/import·offload/reload·version lineage), 다세션 이력을 넣고, H-COMPUTE의 핵심 시험인 SE 대 SES(경험 후 대 같은 경험 + Sleep 후) quality–compute 곡선 이동을 처음 본격적으로 측정한다.
- **근거**: **LITERATURE:** review §5 DQ4(SPENS24의 teacher–student replay가 Sleep의 첫 형태, SWAMI23 Discussion의 반복 rebinding 흡수, HWU20의 novelty×familiarity replay 예산), [05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §11, [07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md) §5–§7, [08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md) §3, Sleep [A03]. **USER:** U07·U10. **PROPOSAL.**
- **데모 시나리오**: **UJ4** (CLI): 세션 1에서 경험 → `fcl sleep` → 프로세스 종료 → 세션 2에서 같은 구조의 새 개체를 더 적은 관측·더 얕은 depth로 푼다. bundle을 내보내 다른 디렉터리·새 프로세스에서 불러와도 같은 판단이 나온다. 삭제 요청의 영향은 측정해서 보고한다(보장하지 않음). UJ1–UJ3 회귀.
- **넓이 변화**: 다세션 이력, bundle export/import, version lineage, 모델 revision 변경 시 migration 거부 규칙, replay 후보 선별.
- **깊이 변화**: Sleep v0(fast→slow teacher–student replay, replay 예산 대조), deep-to-shallow distillation, 보존 평가(savings·세션 간 ABA·zero-shot 재평가), 공고화 시점을 event/readiness 대 고정 주기로 대조, Sleep·offload·warmup 비용을 amortized total에 포함.
- **성립하는 보장**: Sleep 전후 state 버전 계보와 재현 가능한 replay recipe, 같은 데이터·총 계산량의 replay-only·teacher distillation과의 비교, offload/reload 뒤 판단·후속 학습의 일관성 측정(F12).
- **후보 readout (OPEN, 2026-11-17 검토; 측정만, 등급 3 gate 판정에 넣지 않음)**: F12의 후속 학습 일관성 측정에 (i) reload·갱신 뒤 색인·view를 다시 만든 경우의 stale index 검사, (ii) 원본 관측 → 파생 해석 → version → 색인 계보의 보존, (iii) 갱신 뒤 읽기 보존(F-CI, [08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md))을 추가로 기록한다. 압축·통합·폐기·offload-only는 같은 표에서 별개 군으로 보고하고, 출처 연결이 끊긴 압축과 되돌릴 수 없는 폐기를 구별한다. 외부 agent memory 연구(SoMem 등)의 view 재구축과 근거 링크 검증은 비교 정책 후보일 뿐 parametric 지속학습의 근거가 아니다. 조건부 상태 용량 결과(arXiv:2611.13760)를 Sleep·외부화 설계의 제약으로 쓰지 않는다. 상세: [2026-11-16-sleep-time-melete-integration.md](/home/jimmy/repos/full-continual-learning/research/2026-11-16-sleep-time-melete-integration.md), [2026-11-17-sleep-time-melete-selected-addendum.md](/home/jimmy/repos/full-continual-learning/research/2026-11-17-sleep-time-melete-selected-addendum.md).
- **상한**: 등급 3. 저장·재구성 성공을 판단 효용으로 해석하지 않는다. tensor shape/hash만 확인한 외부화는 통과로 보지 않는다. 통합된 weights에서 개별 source 삭제가 완전하다고 약속하지 않는다. Sleep을 코드·아키텍처 자체를 고치는 development evolution과 동일시하지 않는다. 자연어·다모델 일반화 주장 없음.
- **종료 gate**: (1) **UJ4 E2E:** 실제 sleep 학습·실제 저장/offload/reload·실제 프로세스 재시작. (2) **앞 phase 회귀:** UJ1–UJ3 전부. (3) **자동 테스트:** bundle manifest·hash·revision mismatch·rollback·migration 거부·세션 간 state 격리. (4) 등급 3 readout: SE 대 SES의 H-SAMPLE과 H-COMPUTE를 따로 판정하고 replay-only·teacher 대조를 포함. (5) B07 세 질문과 capability 표 재검토, P5를 둘로 나눌지 결정.
- **미루는 것**: 대규모 retrieval·multi-user, 외부 agent 연결, 두 번째 base model·자연어 도메인, 운영 자동화.
- **2026-11-18 개정 주석 (PROPOSAL)**: 위 P4의 목표·UJ4·보장·상한·종료 gate·미루는 것은 바뀌지 않았다. 학습된 Sleep은 P0의 Sleep-NP와 같은 호출 예산으로 비교하고(`replay-only` 대조 포함) Sleep-NP는 NP arm에 남는다. ET 단은 판정 대상 ET-1 잠복 효과와 ET-2, 탐색 ET-3(pilot 대상)이다. 회귀 gate에 UJ0이 더해진다(§6 보충 행).

### P5 — 확대와 실제 consumer 연결

- **목표**: 검증된 범위를 넓히고 실제 consumer에 연결한다. 더 넓은 retrofit, 두 번째 base model, 자연어 혼합 도메인에서 확증을 반복(등급 4)하고, 실제 codex·prime agent가 같은 session 접점으로 쓰게 하며, retrieval·migration·multi-user 격리·운영 지표를 갖춘 제한 운용(관측한 범위 안에서 등급 5)에 이른다. 진입 조건은 §7의 B13 조건이다. P5는 가장 멀어 해상도가 낮으며 P4 종료 재검토에서 둘로 나눌지(범위 확대 / 연결·운용) 결정한다.
- **근거**: **USER:** B12·B13·B14·U10(§1.1). **LITERATURE:** [05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §10(latent read를 hidden computation에 연결하는 경로, source pointer·terminal·all-state·learned interface를 같은 정보·예산으로 비교), [07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md) §7(multi-user), [10-evolution-policy.md](/home/jimmy/repos/full-continual-learning/docs/10-evolution-policy.md) §6. **ARCHIVE:** Melete의 제품 P4(제한된 native continual 제품). **PROPOSAL.**
- **데모 시나리오**: **UJ5**: 실제 codex 또는 prime agent 세션이 FCL session 접점(tool 또는 endpoint, D-11)으로 경험을 주고, 질문하고, 정정하고, 재시작 뒤 복원된 상태로 이어서 일한다. 같은 CLI에서 UJ1–UJ4도 그대로 돈다. 외부 frozen LLM+RAG 대조군과 나란히 본다.
- **넓이 변화**: layer 범위, 모델 크기·계열(D-12), 자연어 혼합 도메인, 외부 consumer, 다수 schema artifact retrieval, multi-user.
- **깊이 변화**: 확증 반복(복제), 운영 지표(latency p50/p95·residency·offload warmup), 삭제 의존성 검증 범위, self-evolution의 운영 승격 gate, 보호 family 자동 중단 유지.
- **성립하는 보장**: 관측한 호출 coverage와 검증한 삭제 의존성 안에서만. 외부 consumer 경로에서도 session·저장·검증 경로는 P1과 같다.
- **상한**: 등급 4(효용), 5(운용, 관측한 coverage 안). 부분 layer 결과를 all-layer 성공으로, 관측하지 않은 agent·model-call 경로를 포괄한다고 확대하지 않는다. 개인 DB·native 권한을 자동 활성화하지 않는다([07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md) §7).
- **종료 gate**: (1) **UJ5 E2E:** 실제 agent·실제 가중치·실제 write·저장·재시작·외부 consumer. (2) **앞 phase 회귀:** UJ1–UJ4 전부. (3) **자동 테스트:** 모델 revision·tokenizer 계약, multi-user 격리, 삭제 의존성, session 프로토콜 호환. (4) 등급 4 readout(두 모델·자연어 혼합 도메인·새 fresh cohort)과 운용 coverage 보고. (5) B07 세 질문과 capability 표 재검토.
- **미루는 것**: pretraining·alignment의 분화 가설([11-research-agenda.md](/home/jimmy/repos/full-continual-learning/docs/11-research-agenda.md) §1), 원논문 규모 재현, 상용 규모의 다수 사용자 운영, vec2text, oscillator·위상 조율.
- **2026-11-18 개정 주석 (PROPOSAL)**: 위 P5의 목표·UJ5·보장·상한(등급 4, 운용 5)·종료 gate·미루는 것은 바뀌지 않았다. 이번 구성에서는 P5의 「두 번째 base model」 후보에 시간캡슐 기반 모델이 더해진다. 같은 시간캡슐 모델에 System ONE을 얹은 retrofit(ET-3, pilot 대상)이 P5의 판정 대상이고, 같은 base의 NP arm과 같은 예산으로 비교한다. 시간캡슐 기반의 확보 방식(공개 모델 사용·소형 자체 사전학습·중형 자체 사전학습)은 비용이 드는 결정이며 §10과 [15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md)에 있다. ET-3의 등급 상한(pilot 대상이라 2)은 [17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md) §3.2의 표가 기준이며 P5의 상한(4)이 그 단의 주장 등급을 올리지 않는다. 회귀 gate에 UJ0이 더해진다(§6 보충 행).

### P6(ET) — 역사 아인슈타인 테스트 최종 (2026-11-18 개정, PROPOSAL)

**2026-11-18 개정 (PROPOSAL):** 이 절은 먼 phase라서 목표와 종료 gate 중심으로 짧게 쓴다. 이름 「P6」은 옛 로드맵(11-09 커밋)의 P6(schema 외부화)와 무관하다(§9 보충 행). ET의 정의와 단별 상한은 [17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md), 논문 주장은 [19-paper-plan.md](/home/jimmy/repos/full-continual-learning/docs/19-paper-plan.md)가 소유한다.

- **목표**: 같은 `fcl` 제품에서, 시간캡슐 기반 모델에 System ONE을 얹고 사용자가 한 인물의 경험 stream을 시간순으로 넣어 checkpoint마다 발견 곡선을 보고 봉인된 주력 대상 묶음에 대한 사전 명세 판정(ET-4)을 받는다. 사용자의 최종 목표인 아인슈타인 테스트를 우리 운영 정의(경험 조건부 발견 시험)로 처음부터 끝까지 돈다. 평가만 하는 phase가 아니다. P5까지의 학습 모듈(정정·accommodation·Sleep·외부화·학습된 controller)이 시간캡슐 기반 위에서 긴 인물 stream(형성기 → 연구기와 T0 이후 세계 지식)을 schema로 쌓고, 미해결 불일치를 보존했다가 재조합·재구조화하는 제품의 넓이와 깊이가 올라간 것이다.
- **근거**: **USER:** 2026-11-18 요청의 최종 목표 문장(원문과 위치: [2026-11-18-discussion.md](/home/jimmy/repos/full-continual-learning/sources/sync/2026-11-18-discussion.md), 해석은 PROPOSAL). **LITERATURE (2차 출처 요약):** Einstein test의 출처, 공개 시간캡슐 모델, 대상 후보와 추천 묶음은 [2026-11-18-blueprint-et-design.md](/home/jimmy/repos/full-continual-learning/research/2026-11-18-blueprint-et-design.md)와 docs/17 §4·§5에 확인 수준과 함께 있다. **PROPOSAL:** 아래 전부.
- **데모 시나리오**: **UJ6** (실제 `fcl` CLI, 실제 시간캡슐 기반 가중치). ① 기반 모델 지정: 시간캡슐 모델의 revision과 실효 마감, 봉인 manifest 해시를 확인한다 → ② 감사: 누수 감사 4층(항목·stream·기반 모델·인프라)이 보고서를 낸다 → ③ 인물 stream을 시간순으로 투입: 형성기, T0, 연구기와 T0 이후 세계 지식을 입력 tier A·B·C로 → ④ checkpoint마다 읽기 전용 중립 probe로 발견 곡선을 본다(자발·중립·주제·과제 채널) → ⑤ 같은 stream을 대조 stream(없음·순서 섞기·같은 시기 비발견자·무관한 인물·핵심 입력 제거)과 대조 arm(NP arm 등)으로 반복해 한 보고서에 놓는다 → ⑥ 맹검 채점·일치도·입력 내재 대비 초과·특이성 → ⑦ 봉인 대상을 열어 판정 보고(결과 상태, 등급 3 이하, 범위 태그)를 받는다. UJ0–UJ5가 모두 회귀로 다시 돈다(특히 UJ0의 ET-0 run과 ET-3p run).
- **넓이 변화**: ET 대상이 pilot에서 봉인 주력 묶음으로(묶음의 대상 수는 OPEN), 입력 tier 세 곡선, 대조 stream 5종과 대조 arm, 인물 stream 길이(항목 수 천 단위), P5에서 확보한 시간캡슐 기반 retrofit 위에서 전 모듈을 같은 CLI로 돈다. 외부 consumer 접점(UJ5)은 유지된다.
- **깊이 변화**: 봉인과 사전 명세와 독립 검토, 맹검 2인 이상의 채점과 일치도, 누설 변형 3종(LV0·LV1·LV2), 새로움 검사, 핵심 입력 제거, 오염·누수 감사, 용량–반응 곡선과 특이성 판정. 판정의 형식은 docs/17 §10의 조건 PC-1~PC-10(값은 dev pilot의 분산으로 봉인 전에 정하고 사용자가 승인)이다.
- **성립하는 보장**: Contract·Product 범위(시간 필터, 읽기 전용 probe의 상태 해시, 시스템 안 모델 사용 규칙의 호출 로그 감사, 봉인 해시 불일치 거부, evaluator 전용 권한)와 봉인 대상에서의 사전 명세 판정 상태(PASS·FAIL·INCONCLUSIVE·BLOCKED·NOT RUN). FAIL과 INCONCLUSIVE도 같은 틀로 보고하며 소급해서 바꾸지 않는다.
- **상한**: 등급 3 한정 확증(제안; 근거와 4의 조건은 docs/17 §3.2의 표). 「발견했다」는 ET-4 등급 3에서만 범위 태그(대상 묶음·시간캡슐 기반·입력 tier)와 함께 쓴다. 「아인슈타인 테스트를 통과했다」·「모든 발견·인물·분야」·AGI 문구는 쓰지 않는다. 대상 수가 소수이고 통계 단위가 대상과 구성요소이므로 일반화 주장은 없다. 입력 tier C 단독 결과를 발견으로 읽지 않는다.
- **종료 gate**: (1) **UJ6 E2E:** 실제 CLI·실제 시간캡슐 기반 가중치·실제 write·저장·재시작으로, 봉인된 주력 대상의 stream을 시간순으로 투입해 checkpoint별 곡선과 판정 보고까지 끝까지 실행한다(mock·조사만의 결과는 불인정). (2) **앞 phase 회귀:** UJ0–UJ5 전부. (3) **자동 테스트:** 시간 필터(날짜 없는 항목·미래 항목 거부)·읽기 전용 probe의 상태 해시·모델 사용 규칙(호출 로그에 현대 모델 없음)·봉인 manifest 해시 불일치 거부·권한 분리(기준 해답·핵심 입력 집합·봉인 stream은 evaluator에만)·누설도 3 항목 거부가 PASS한다(Contract). (4) **효용 판정 기록:** 판정 대상 주장은 [19-paper-plan.md](/home/jimmy/repos/full-continual-learning/docs/19-paper-plan.md)의 PAPER-6 주장(C6-1~C6-4)을 가리키며 여기서 다시 쓰지 않는다. 결과 상태와 등급 필드가 기록돼야 한다. PASS가 아니면 §7의 분기를 따른다. (5) **self-feedback:** B07 세 질문과 capability 표 재검토 기록(§11).
- **미루는 것**: closed-loop(모의 인물이 시스템 출력에 반응하는 설정), 두 번째 봉인 대상 묶음과 두 번째 시간캡슐 기반(등급 4 시도), 직접 사전학습한 시간캡슐 모델(공개 모델이 맞지 않을 때의 선택지이며 비용 결정), 다른 분야·언어의 대상, ET를 외부에 공개하는 benchmark로 만드는 일.

## 6. 회귀 gate 누적표

**PROPOSAL.** 앞 phase의 사용자 시나리오는 뒤 phase의 종료 gate에서 가장 최신 코드로 다시 돌려 통과해야 한다. 앞 phase의 PASS 기록을 재사용해 회귀를 대신하지 않는다. 회귀 실패는 새 기능 개발보다 먼저 고친다. 앞 시나리오의 등급은 새 phase의 결과로 저절로 오르지 않으며 다시 측정해야 한다.

| phase 종료 | 회귀로 다시 통과할 앞 시나리오 | 새 시나리오 | 새로 추가되는 자동 테스트(Contract) | 효용 판정 기록 |
|---|---|---|---|---|
| P1 | 없음(첫 phase) | UJ1 전체 여정 | 시계 분리·재전송 idempotency·원자적 commit·재시작 동등·revision mismatch 거부·삭제 동등·누수 audit·budget 일치·함수 보존·manifest 봉인·controller v0 결정의 관측 state 근거 | 등급 2 readout 상태 |
| P2 | UJ1 | UJ2 여러 구조·고정 깊이 | depth 시계·causal mask·stale cache·layer 확대 회귀(원능력)·후보와 evaluator의 권한 분리 | 등급 3 readout 상태 |
| P3 | UJ1, UJ2 | UJ3 스스로 고르는 모델 | router 인과성·controller 결정이 관측 state에 근거함·bundle에 제어 상태 포함·보호 family 자동 중단 | 등급 3 readout 상태(controller 대 고정 depth 등) |
| P4 | UJ1, UJ2, UJ3 | UJ4 세션을 넘는 경험 | bundle manifest·hash·migration 거부·세션 간 state 격리·replay 재현 | 등급 3 readout 상태(SE 대 SES) |
| P5 | UJ1, UJ2, UJ3, UJ4 | UJ5 실제 consumer 연결 | 모델·tokenizer 계약·multi-user 격리·삭제 의존성·session 프로토콜 호환 | 등급 4 readout 상태 + 운용 coverage |

**2026-11-18 개정 (PROPOSAL): 회귀 gate 보충 행.** 위 표의 P1–P5 행은 바꾸지 않는다. 아래 보충 표는 같은 열로 P0(NP)와 P6(ET)의 행을 더하고, P1–P5에는 「UJ0 추가 회귀」를 보충 행으로 적는다. UJ0은 UJ1의 상위 집합이다(§5 서문 주석). 앞 시나리오의 등급이 새 phase의 결과로 저절로 오르지 않는 위 원칙은 같다.

| phase 종료 | 회귀로 다시 통과할 앞 시나리오 | 새 시나리오 | 새로 추가되는 자동 테스트(Contract) | 효용 판정 기록 |
|---|---|---|---|---|
| P0(NP) | 없음(첫 phase) | UJ0 (UJ1 ①–⑩의 NP arm 실행 + Sleep·발견 run·ET-3p run·보고서) | 시계 분리·재전송 idempotency·원자적 commit·재시작 동등·revision mismatch 거부·삭제 동등·version 되돌리기·누수 audit·budget 일치·생성물이 관측으로 승격되지 않음·가중치 hash 불변·controller 결정이 관측 state에 근거·모델 호출 allowlist·시간 필터·probe 전후 상태 hash 동일·manifest 봉인·등급 문구 검사기([18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md) §12.1) | V0-1~V0-17의 결과 상태(주장별 등급 최대 3, 조건부). ET-3p는 절차 계약 |
| P1 (보충) | 위 P1 행에 UJ0 추가(NP arm. 같은 CLI) | 없음(위 P1 행 그대로) | 위 P1 행에 더해 NP arm이 P1의 base로 다시 돌아 예산 일치 검사를 통과함 | 위 P1 행에 더해 NP arm 대조 병기(상한 2 그대로) |
| P2 (보충) | 위 P2 행에 UJ0 추가 | 없음 | 위 P2 행 그대로 | 위 P2 행에 ET-0 깊이 곡선(판정 대상) 병기 |
| P3 (보충) | 위 P3 행에 UJ0 추가 | 없음 | 위 P3 행 그대로 | 위 P3 행에 ET-1(판정 대상, 오염 probe 병기) 병기 |
| P4 (보충) | 위 P4 행에 UJ0 추가 | 없음 | 위 P4 행 그대로 | 위 P4 행에 ET-1 잠복 효과·ET-2 병기 |
| P5 (보충) | 위 P5 행에 UJ0 추가 | 없음 | 위 P5 행에 더해 시간캡슐 기반 가중치의 revision 계약 | 위 P5 행에 ET-3(pilot 대상, 상한 2) 병기 |
| P6(ET) | UJ0, UJ1, UJ2, UJ3, UJ4, UJ5 (UJ0의 ET-0 run과 ET-3p run 포함) | UJ6 역사 ET 최종 | 시간 필터(날짜 없는 항목·미래 항목 거부)·읽기 전용 probe의 상태 해시·모델 사용 규칙(호출 로그)·봉인 manifest 해시 불일치 거부·권한 분리(기준 해답·핵심 입력 집합·봉인 stream은 evaluator에만)·누설도 3 항목 거부 | 등급 3 이하 readout 상태(ET-4 판정). 주장은 [19-paper-plan.md](/home/jimmy/repos/full-continual-learning/docs/19-paper-plan.md)의 PAPER-6 주장을 가리킴 |

### 6-1. 간섭·CRUD 실험의 배치 (2026-11-17 검토 추가, PROPOSAL / NOT RUN)

[13-schema-decomposition-and-interference.md](/home/jimmy/repos/full-continual-learning/docs/13-schema-decomposition-and-interference.md) §10의 실험 A–E와 [14-schema-lifecycle-crud-and-joint-paper.md](/home/jimmy/repos/full-continual-learning/docs/14-schema-lifecycle-crud-and-joint-paper.md) §8의 CU·D·R·Joint·System ONE을 기존 phase의 UJ 안의 판독으로 배치한다. 실험 전용 phase나 새 UJ를 만들지 않는다. 앞 phase에는 가장 얇은 형태(계측·측정·Contract 테스트 1개)를 넣고, 새 arm은 그 arm이 의미를 갖는 phase에서 처음 넣는다. §3의 등급 상한과 §5의 데모 시나리오·종료 gate·미루는 것은 바꾸지 않는다. seed 수(D-05)가 정해지기 전에는 계산 규모 수치를 이 문서에 쓰지 않는다.

| 실험 | P1(등급 2) | P2(3) | P3(3) | P4(3) | P5(4) | 새 arm |
|---|---|---|---|---|---|---|
| A 간섭 분리 | `fcl diff`·재평가·ABA·원능력으로 간섭 판독만 | 쓰기 범위(local/shared) × lure × 표면 거리 | 학습 gate 대 oracle 대 random partition | – | 자연어·모델 2종 | `ftall`, `adapters` |
| B post-training | – | (제안·결정 전) dev 사이드: 같은 계열 Base/Instruct 2종 | – | – | (제안·결정 전) 두 번째 base의 Base/Instruct 쌍 | `--base-ckpt` 축 |
| C 용량(= Joint) | `full` 대 `flat` + bytes 기록 + 새 학습·보존 쌍 보고 | `adapters`(oracle ID) 용량 일치 | 추론 ID: create 대 no-create | B_total·cold-load 포함 | 모델 2종 | `adapters` |
| D artifact | + resume 후 update 동등 Contract 1개 | rollback·다 session | offload/reload·lineage·F12 | – | migration | `weights-only`(음성 대조) |
| E(= System ONE) | 경로 분포·계산량 측정만 | depth 격자 × S0/SE | controller 대 고정 depth | SE 대 SES | 운영 지연 | (기존) |
| CU | Update(2×2·정정·ABA) | 3 family | Create 대 no-create | Sleep 뒤 분화 안정성 | – | `nocreate` 등 |
| D(보존·망각) | 망각 측정 지표만 | 용량 제한 망각 곡선 | – | offload-only 대 eviction | 압축·폐기 | `evict-*` |
| R | `ctx` 대 `full`, wrong-schema swap | oracle/random/key 선택 | 학습 head | stale index | rag·근거 확인 Read | `sel-*` |

**주의·결정 후보.** (1) 공유 파라미터를 갱신하는 순차 갱신 arm(`ftall`)과 task별 oracle adapter(`adapters`)가 arm 표에 없다. P1의 arm 7개는 바꾸지 않고 P2에 추가하는 안이다. (2) 실험 B는 §5 P5 '미루는 것'과 P1·P2 상한 이유 '모델 1종'과 충돌하므로 표의 B 행은 제안일 뿐이며 사용자 결정(D-12 연계) 전에는 §5의 phase 계획에 넣지 않는다. (3) P1에 더하는 것은 계측 열(active·total bytes, 기록만) 1개, resume 후 update 동등 Contract 테스트 1개, 새 학습과 보존의 쌍 보고 서식뿐이며 범위 절삭 순서에 영향이 없다. (4) family 배치: [08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md) §2·§2-1·§2-2에는 F01–F21이 있으나 §4의 benchmark family 행은 F01–F12만 배치한다. 이 실험들이 쓰는 F13(관계 통합 추론)·F18·F19·F20은 P3에 둔다(F20은 §9의 J2 행과 같다). F14–F17·F21의 배치는 이번 검토의 범위 밖이다.

## 7. 중단·전환 조건

**PROPOSAL (옛 §4 유지·갱신).** 옛 조건은 그대로 유지한다. 현재 recipe의 비용과 품질이 baseline을 넘지 못하면 원인을 분리한다. 방법을 확장하기 전에 학습 목표, 데이터 식별성, representation capacity, reader/interface, 계산 예산 중 어떤 병목인지 구분한다. 같은 test를 반복해서 보고 새 candidate를 최적화하지 않는다. 같은 조건에서 단순한 pooled/linear/text 방법이 낫다면 그 후보를 유지한다. 제품에 효용이 있어도 neural schema의 독자 기여가 미입증이면 두 상태를 분리 보고한다. 불리한 결과를 이론 전체의 반증으로 확대하지 않되 기준을 낮춰 성공으로 바꾸지도 않는다. 아래는 새 phase 구조에 맞춰 추가한 것이다.

**진입 규칙 (Melete 교훈의 집행).** 다음 phase 진입 = 현재 phase 종료 gate 통과(Contract·Product) + 효용 상태. 효용 상태가 PASS면 다음 phase로 간다. FAIL이나 INCONCLUSIVE면 아래 분기표를 따르고 사용자에게 보고해 결정을 받는다. 구현 PASS를 효용 PASS로 읽고 진행하지 않는다.

| 상황 | 먼저 할 일 | 허용되는 다음 행동 | 금지 |
|---|---|---|---|
| Contract FAIL | 원인을 고쳐 같은 gate를 다시 검증 | 같은 phase 안에서 수정 | Efficacy 실행으로 진행 |
| Efficacy FAIL(사전 명세 미달) | 병목 분리: 학습 목표·데이터 식별성·representation capacity·reader/interface·계산 예산 중 무엇인가. AI의 원인 설명은 검증 전까지 가설이다 | 가설 1개를 사전 등록한 새 candidate(새 ID·fresh cohort). 사전 등록한 candidate 상한 안에서만 | 같은 recipe 확대, 같은 test를 보고 튜닝, 임계·margin·subset의 사후 변경 |
| INCONCLUSIVE | 표본·식별성·검정력 중 무엇이 부족한지 구분 | 새 protocol·새 manifest·새 fresh cohort | PASS로 읽기, 같은 cohort 재사용 |
| BLOCKED(권한·필수 인프라) | 멈추고 구체적으로 보고(B07) | 사용자 결정 뒤 재개 | 다른 모델·장비·권한으로 바꿔치기 |
| 단순 baseline(`flat`·`fixed`·`always`)이 같은 예산에서, 또는 `ctx`가 사전 명세한 token·계산 예산 기준에서 같거나 낫다 | 그 후보를 유지하고 두 상태를 분리 보고: 제품 효용 / neural schema의 독자 기여 | 그 범위에서 복잡한 구조의 필요성을 주장하지 않고 다음 phase의 범위를 줄이거나 설계를 사용자와 재검토 | 복잡한 구조의 필요성 주장 |
| 보호 지표 퇴행(최초 과제 재평가·ABA·원능력) | 자동 중단 | 원인 분리 뒤 재개 | 평균 향상으로 상쇄 |
| spike 실패 | 실패 원인과 축소 범위를 보고 | 해당 능력은 다음 phase로 이월하고 현 phase는 나머지로 종료(제품은 계속 동작하고 표에는 "없음"을 유지) | 실패한 능력이 있는 것처럼 문구 유지 |

**외부 consumer 연결의 진입 조건 (B13·B14).** P5의 외부 agent 연결은 핵심 대조(`full` 대 고정·무구조·항상-갱신)가 등급 3 PASS로 기록된 뒤에만 시작한다. 없으면 연결 구조·interface부터 만들지 않는다. 단순 baseline이 이기고 있으면 연결할 대상 자체를 재검토한다.

**프로그램 수준 중단([10-evolution-policy.md](/home/jimmy/repos/full-continual-learning/docs/10-evolution-policy.md) §6).** budget 소진, 반복된 동일 failure, 평가 결함, 비재현, 권한 위반, 보호 family 퇴행, candidate 상한 소진이면 멈추고 사용자에게 보고해 결정을 받는다. 실제 소모한 compute는 실패·취소·재시도를 포함해 합계에 넣는다.

**ARCHIVE:** Melete에서는 N1의 독립 기여가 입증되지 않은 채 N2·N3 구성요소 연구가 진행됐고, J1 FAIL 뒤에야 같은 recipe 확대를 중단했다. 이 표는 그 두 시점을 앞으로 당겨 gate로 만든 것이다.

**2026-11-18 개정 (PROPOSAL): P0(NP)와 ET의 분기.** 위 분기표와 진입 규칙은 P0(NP)·P6(ET)에도 그대로 적용된다. **P0의 결과에 따른 분기(NP arm이 대조군을 이기지 못할 때, NP-0 또는 NP-1이 성립하지 않을 때, 효용이 FAIL·INCONCLUSIVE일 때 등)는 [18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md) §14.2를 따른다.** 아래 표는 위 표에 없는 ET·NP 쪽 상황만 더한다.

| 상황 | 먼저 할 일 | 허용되는 다음 행동 | 금지 |
|---|---|---|---|
| ET-3p의 절차 계약이 깨진다([17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md) §10.3의 EC-1~EC-7) | 원인(모델 형식·문맥 길이·누수 감사·호출 규칙·채점)을 분리해 보고 | 같은 pilot 대상으로 절차를 고쳐 다시 도는 것(dev). 시간캡슐 모델 교체는 사용자 결정 | System ONE을 얹은 ET-3로 올라가기, 실패한 절차를 통과로 보고 |
| 학습 arm이 같은 base·같은 예산의 NP arm보다 낫지 않다(P1 이후) | 그 범위에서 학습 모듈의 필요성을 주장하지 않고 두 상태를 분리 보고: 제품 효용 / 학습 모듈의 독자 기여 | 가설 1개를 사전 등록한 새 candidate, 또는 다음 phase의 범위 축소·재검토 | 같은 recipe 확대, 대조를 바꿔 PASS로 만들기 |
| 누수 감사에서 누설도 3 항목, 시간 필터 위반, 시스템 안 현대 모델 호출이 발견된다 | 그 run을 INVALID로 표시하고 원인 분리 | 원인을 고쳐 새 manifest와 새 run으로 다시 시작 | 그 run을 결과에 포함, 소급 수정 |
| ET-4가 FAIL·INCONCLUSIVE·BLOCKED(사료 접근 등)이다 | 어느 가설과 범위를 기각하는지, 표본·식별성·검정력 중 무엇이 부족한지 구분 | 새 protocol·새 manifest·새 fresh cohort, 대안 대상으로의 전환(전환 규칙은 pilot 결과를 보기 전에 선언해 둔 것만) | PASS로 읽기, 같은 봉인 대상 재사용, 임계·대조·subset의 사후 변경, 「아인슈타인 테스트를 통과했다」 문구 |

## 8. 지속적으로 유지할 자산

**PROPOSAL (옛 §5 유지·확장).** 옛 목록을 유지한다: 실패 사례와 negative controls, data generators, source·recipe lineage, state compatibility tests, regression suite, 실제 비용 원장, reference catalog, specification·decision log. 테스트 수·문서량·커밋량을 연구 진전의 대표 지표로 쓰지 않는다.

새로 추가한 것은 다음과 같다.
- arm 정의표와 arm manifest(설정 hash)
- 봉인 manifest와 evaluator 버전, sealed cohort 사용 기록(어떤 candidate에 썼는가)
- phase별 데모 시나리오 스크립트(UJ1…UJ5)와 실행 기록, 회귀 결과
- 세계 생성기와 split(train/dev/sealed), renderer 두 종류
- 결과 보고 생성기와 문구 검사기
- 이 문서의 capability × phase 표와 변경 기록

**2026-11-18 개정:** 위 목록의 「phase별 데모 시나리오 스크립트(UJ1…UJ5)」는 「UJ0…UJ6」으로 읽는다. 새로 유지할 자산은 다음과 같다.
- NP arm manifest(설정 hash)와 영구 대조군의 결과 기록(phase마다 같은 base로 다시 돈 것)
- ET의 stream manifest·rubric·probe 은행·누설 어휘 사전·핵심 입력 집합의 봉인 기록과 개봉 기록, 누수 감사 보고서, 모델 호출 원장(allowlist 검사)
- suite S-B·S-C의 생성기와 재분장 대응표
- 사용한 시간캡슐 모델의 revision과 마감 probe 결과

## 9. 기존 계획 대응표

**ARCHIVE·PROPOSAL.** 이 표는 옛 계획의 내용·새 위치·바뀐 점·이유를 남겨 숨기지 않기 위한 것이다. "새 위치"는 개념·설계·자산이 이어지는 자리이며 **완료의 승계가 아니다.** 옛 PASS/FAIL·실행 산출물을 새 phase의 완료로 이식하지 않는다. 쓸 만한 옛 산출물은 새 phase의 작업으로 다시 실행해 새 run ID로 기록하고, 재실행 전에는 NOT RUN으로 본다. 번호가 같아도 FCL P1–P5와 Melete P1–P4는 다른 계획이다. Melete는 private 저장소이므로 고정 커밋 `1d95136c3a64580ec25bc588c96c191eecb85b41`의 링크로 가리키며 접근 권한이 없으면 읽지 못할 수 있다([12-melete-lineage.md](/home/jimmy/repos/full-continual-learning/docs/12-melete-lineage.md) §5).

| 옛 계획 | 옛 단계 | 내용 | 새 위치(phase·작업) | 바뀐 점 | 이유 |
|---|---|---|---|---|---|
| FCL P0–P6 | P0 연구 계약 | 용어·state clocks·source boundary·baselines·평가 split·budget | P1-T01(용어·시계·source), T02(평가 split), T03(baseline·budget), T06(세계 생성기) | phase가 아니라 P1 앞쪽 작업 | 조사·계약 전용 phase는 실행 가능한 제품이 아니다(B17). 2026-11-03 선형 실험만으로 통합 P0 전체 완료로 부르지 않는 조항은 유지 |
| FCL P0–P6 | P1 얇은 통합 모델 | 작은 pretrained 모델 일부에 Titan sequence path + CMS FFN, 실제 입력·저장·재시작 | P1 전체(T04–T16) | 모델·저장만이 아니라 CLI 전체 여정 + 대조군 + 망각·표면/구조 평가 + 사전 명세 readout | "분리된 module 테스트만 통과"를 완료로 보지 않는 옛 조항을 종료 gate로 강제 |
| FCL P0–P6 | P2 recursive computation | 같은 core의 1/2/4/… 반복, 중간-depth 출력, causal cache | P1 deep 경로(r=2 최소형), P2 묶음 A(spike)·D(고정 depth 격자) | 단독 계층 phase가 아니라 같은 여정에 depth 축을 더함. 실패하면 P3로 이월하고 제품은 계속 동작 | 엔진만 만드는 phase 금지. 동일 입력 재호출은 개선이 아니라는 조항 유지 |
| FCL P0–P6 | P3 schema/controller | 문맥 관계 판단 + token routing + 선택적 update + halting | 규칙형 controller v0는 P1(T08), 학습된 controller·token routing·halting·선택적 update는 P3 | controller를 P1부터 가장 얇게 두고 P3에서 학습된 형태로 깊게 한다. gate·accommodation은 P3. 쉬운 사례만 고른 평균 depth 감소 금지는 난이도 층화 요구로 유지 | 부품 완성 후 조립이 아니라 해상도 상승 |
| FCL P0–P6 | P4 experience+Sleep | binding·수정·ABA·replay·통합·deep-to-shallow | 경험·정정·ABA 기본형은 P1(UJ1), 예외·ABA 확대는 P2, accommodation은 P3, replay·통합·deep-to-shallow는 P4 | 한 묶음을 해상도 순서로 분산 | 경험 → 정정이 MVP 여정의 핵심이라 뒤로 미루면 P1이 MVP가 아니다. 저장·재구성 성공을 판단 효용으로 해석하지 않는 조항 유지 |
| FCL P0–P6 | P5 전체 retrofit 확대 | sequence/FFN 전환 범위를 단계적으로 증가 | §4 retrofit 행: P1 일부 layer → P2 확대 → P5 범위·모델 확대 | 마지막에 한꺼번에가 아니라 매 phase 소폭 확대하고 전환마다 회귀 | 부분 layer 결과를 all-layer 성공으로 확대하지 않는 조항 유지 |
| FCL P0–P6 | P6 schema 외부화 | offload·version·retrieval·migration·delete | bundle v0와 삭제는 P1-T10·T13, 외부화 v0는 P4, retrieval·migration·multi-user는 P5 | 상태 경계를 P1부터 실제로 둠 | 헌장 U10: 전면 구현은 후반이지만 상태 경계는 초기 설계부터. tensor shape/hash만 확인하면 통과가 아니라는 조항 유지 |
| FCL P0–P6 | 옛 §3 초기 실행 순서 8단계 | ① checkpoint·baseline pin ② wrapper 하나씩 ③ state·clock·cache 계약 ④ 고정 depth 재귀 ⑤ 관계 전이·few-shot ⑥ controller·선택적 쓰기 ⑦ 경험 후·Sleep 후 곡선 분리 ⑧ 검증된 범위 확대·외부화 | ①→T04·T06, ②→T05, ③→T01·T10, ④→P2, ⑤→P1(T06·T12), ⑥→P1(규칙형 controller v0)·P3(학습된 controller·선택적 쓰기), ⑦→P2(S0/SE)·P4(SES), ⑧→P5 | ⑤를 ④ 앞(P1)으로 당김 | 관계 전이·few-shot이 가장 빨리 검증할 핵심 가치(B02)이고 MVP 여정의 일부다 |
| 11-03 P0–P5 | P0–P5(단계별 내용 미확인) | 11월 3일 외부 fast-model 중심 계획. 원문 위치 미확인 — docs/09 §6 언급만. 이 저장소의 [2026-11-02-baseline.md](/home/jimmy/repos/full-continual-learning/research/2026-11-02-baseline.md), [README.md](/home/jimmy/repos/full-continual-learning/experiments/phase0/README.md), [02-discussion-history.md](/home/jimmy/repos/full-continual-learning/docs/02-discussion-history.md), [12-melete-lineage.md](/home/jimmy/repos/full-continual-learning/docs/12-melete-lineage.md)에는 단계 목록이 없다. [archive-manifest.json](/home/jimmy/repos/full-continual-learning/experiments/phase0/archive-manifest.json)이 원본 ZIP 안의 MELETE_RESEARCH_PLAN.md(22,448 bytes)를 "사용자 통합 모델 정정 이전 phase 포함"으로 지목하지만 원문은 이 저장소에 없다 | 매핑하지 않음 | 새 phase로 이식하지 않음 | 통합 System ONE 정정(U-T07) 이후 별도 fast 모델은 최종 목표가 아니다. 실험용 작은 모형·baseline·외부 teacher는 대조군·teacher로만 허용한다([05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §3) |
| 11-03 P0–P5 | P0 실험 산출물(Phase-0) | 합성 Bayesian linear prediction의 공유 연속 prior 실험. 통합 모델 PoC가 아니다([README.md](/home/jimmy/repos/full-continual-learning/experiments/phase0/README.md)) | 완료 승계 없음. 설계 참고만: 대조군 철학(isotropic·pooled·mixture·rotated·oracle)과 negative control → P1-T02·T03·T06 | 옛 PASS를 어느 phase 완료로도 세지 않음 | 선형 실험만으로 통합 P0 전체 완료로 부르지 않는 조항 유지 |
| Melete N0–N5 | N0 | H1–H5 audit + chronology·split·seed·oracle을 고정한 stream dataset + trace schema + baseline evaluator (합성 8개 수치 cue, D1–D8) | P1-T02·T06·T12 | D1–D8의 설계 원칙(split 단위 = history·mechanism·domain, evaluator 전용 oracle, 학습 전 snapshot 평가)을 F01–F12 부분집합과 2×2로 재구성. 효용 판정 없음 원칙 유지 | 측정 계약을 phase가 아니라 P1 앞쪽 작업으로 |
| Melete N0–N5 | N1 | neural memory·ordered trajectory·familiarity·전체 hit 강화·working graph compiler. 학습된 graph의 추가 이득 0.48%(대략 95% 구간 −3.07~4.04%)로 독립 기여 미입증 | P1 `full` arm의 쓰기·읽기와 대조군(고정·무구조), P1(규칙형 controller v0의 familiarity 기반 fast 경로), P3(학습된 familiarity 처리·hit 경로 강화는 gate 후보) | 외부 graph가 아니라 모델 내부 state. 같은 예산 대조를 처음부터 둠 | N1의 meet 미충족인 채 N2·N3로 진행한 선례를 진입 규칙(§7)으로 막음 |
| Melete N0–N5 | N2 | 전체 hidden-state trajectory를 소비하는 latent-to-text reader + frozen LLM prefix. calibration 문장 exact all-state 29/256, terminal 38/256 | P5 외부 consumer 접점의 선택지(source pointer·terminal·all-state·learned interface를 같은 정보·예산으로 비교) | H4의 text interface를 필수 경로로 두지 않는다(정리자 추론, 사용자 확인 대기 — OPEN) | 통합 모델에서는 latent read를 hidden computation에 직접 연결할 수 있다. 전체 hidden-state 전달과 terminal·pointer 대조는 basis로 유지한다([12-melete-lineage.md](/home/jimmy/repos/full-continual-learning/docs/12-melete-lineage.md) §1, [05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §10) |
| Melete N0–N5 | N3 | multi-turn runner + 출력 재입력·compatibility·surprise·세 입력 학습·최초 query 재compile·중단 재개(실제 frozen Qwen consumer 3-turn smoke) | P1(반례·정정 → 최초 과제 재평가 → 재개·복원, 모델 내부 write), P3(compatibility·surprise 기반 controller. generated는 학습 신호이되 독립 근거가 아님) | 외부 frozen LLM 폐루프가 아니라 같은 모델 안의 write·재평가 | H5의 메커니즘은 계승하고 구조는 정정 |
| Melete N0–N5 | N4 | held-out 이력·도메인, cost-matched controls, causal ablation | P1(대조·인과 개입을 작게 시작), P2(첫 확증), P3(lesion·swap), P5(도메인·모델 확대 반복) | 뒤쪽 단계가 아니라 P1부터 작게 시작하고 P2에서 확증 | 대조 없는 구현 PASS가 효용으로 읽히는 것을 방지 |
| Melete N0–N5 | N5 | 효과가 분리된 구성을 Codex·Prime에서 제한된 실제 task에 연결 | P5 외부 consumer 연결 | 연결 대상이 Melete memory가 아니라 FCL 모델의 session 접점. 진입 조건을 추가 | B13·B14 |
| Melete J0–J5 | J0 측정 계약 | 시간순 경험 dataset, evaluator-only oracle, 식별가능성 audit, baseline, split·seed·예산·통계 protocol. 학습 효용 판정 없음 | P1-T02·T06, 봉인은 P1-T14 | 연구 gate가 아니라 P1 앞쪽 작업 | 측정 계약 전용 단계는 phase가 아니다 |
| Melete J0–J5 | J1 조건부 neural memory | 학습된 memory graph 대 fixed·no-memory-graph. 5pp gate. seed7 pilot에서 학습된 graph가 matched 대조보다 낮았고(−5.08pp·−3.52pp) 이후 후보도 gate 미달, 같은 recipe 확대 중단 | P1 대조군(`fixed`·`flat`·`always`)과 사전 명세 readout(T14·T15), §7의 같은 recipe 확대 금지 | 연구 gate를 phase 안의 sealed readout으로 편입하고 진입 gate로 집행. J1의 수치(5pp·표본 계획·보정)는 이식하지 않고 FCL 자체 pilot 분산으로 봉인 | 효용 gate를 집행하지 못한 Melete 교훈 |
| Melete J0–J5 | J2 누적 학습 안정성 | observed·generated·derived 계보, 동일 root 반복, 독립 반례 후 회복, 선호 변화, root budget | P1-T01(계보 규칙), P2(F07 최소: 동일 root 재전송·틀린 generated 해석), P3(자기증폭·hit 강화의 포화·감쇠 진단) | 계보 규칙은 P1부터, 자기증폭 진단은 gate가 생기는 P3 | generated는 학습 신호이되 독립 evidence가 아니다([07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md) §2) |
| Melete J0–J5 | J3 trajectory readout | all-state·terminal·IR·pointer를 같은 held-out 이력·의미 필드에서 비교 | P5 외부 consumer 접점의 선택지(N2와 같음) | 필수 경로로 두지 않음(OPEN) | H4의 text interface를 필수가 아니라고 본 것은 U-T07 통합 구조에서 정리자가 도출한 추론이며 사용자 확인 대기다([12-melete-lineage.md](/home/jimmy/repos/full-continual-learning/docs/12-melete-lineage.md) §1) |
| Melete J0–J5 | J4 frozen LLM 효용 | raw history·RAG와 동일 consumer·prefix 위치·token/call 예산에서 비교 | P1 `ctx` arm(같은 소형 모델에 raw history), P2 참고선(Qwen3-8B+raw history), P5 외부 frozen LLM+RAG 대조 | 대조군을 phase 끝이 아니라 P1부터 둠 | 외부 frozen LLM 경로를 강한 대조군으로 유지([01-intent-and-charter.md](/home/jimmy/repos/full-continual-learning/docs/01-intent-and-charter.md) §5) |
| Melete J0–J5 | J5 실제 continual 운영 | 제한 Codex·Prime 경로, 삭제 의존성, rollback, capacity·latency 상한 | P5. 삭제는 P1-T13(fast 한정) → P4(측정만) → P5(검증한 범위) | 삭제를 P1부터 얇게 시작 | source/revision·snapshot·root 중복 제어는 가져올 자산이다([12-melete-lineage.md](/home/jimmy/repos/full-continual-learning/docs/12-melete-lineage.md) §4) |
| Melete P1–P4 | P1 실험용 MVP | CLI session + 실제 frozen LLM·reader·저장소·도구, 갱신·재compile·재개·재시작·삭제. 한정된 structured 조건·한 task·짧은 history | FCL P1 | 외부 frozen LLM과 tool 작업이 아니라 retrofit 모델 자체가 응답하는 질의 여정. 같은 규칙(실제 의존성 E2E, mock 금지)은 유지 | FCL은 모델 제품이다(§1.3) |
| Melete P1–P4 | P2 반복 경험에 적응하는 같은 제품 | 독립 반례·잘못된 해석·동일 root 반복·조건 복귀 | FCL P2(예외·ABA 확대·F07 최소) + P3(accommodation) | 경험 종류를 넓히는 일과 정정 메커니즘을 나눔 | 정정 메커니즘은 대조할 기준선(P2)이 생긴 뒤에 설계한다 |
| Melete P1–P4 | P3 자연어와 새 상황으로 확장 | 의미 encoder·all-state alignment, 다중 독립 history | FCL P5(자연어 혼합 도메인, 등급 4) | 합성 family 3종 확증이 먼저 | 표면 변이를 분리한 뒤에 자연어로 간다(B16) |
| Melete P1–P4 | P4 제한된 native continual 제품 | Codex·Prime 경로, source 수정·삭제·rollback, coverage·비용 | FCL P5(외부 consumer). 삭제는 P1·P4·P5에서 점진 | 같은 번호라도 FCL P1–P4와 다른 계획이다. 대응은 이 표가 기준 | 관측한 범위만 보장하는 원칙 유지 |

**대응표의 근거 문서.** 옛 FCL 로드맵: [09-roadmap.md](https://github.com/jimmylegendary/full-continual-learning/blob/58613da820656953355ec38beb716206a60e189b/docs/09-roadmap.md)(2026-11-09 커밋). Melete N0–N5: [2026-10-12-neural-validation.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/superpowers/plans/2026-10-12-neural-validation.md), [2026-10-12-neural-execution.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/superpowers/plans/2026-10-12-neural-execution.md). Melete J0–J5·P1–P4: [2026-10-15-neural-judgment-roadmap.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/superpowers/plans/2026-10-15-neural-judgment-roadmap.md). H1–H5: [neural-basis.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/design/neural-basis.md). J1 진단: [2026-10-21-neural-judgment-j1-diagnostics.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/implementation/records/2026-10-21-neural-judgment-j1-diagnostics.md). 더 오래된 Melete 학습 로드맵(A1–D3, 2026-10-11)은 N0–N5로 우선순위가 정정된 역사적 계획이라 새 위치를 따로 만들지 않았다: [2026-10-11-learning-roadmap.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/superpowers/plans/2026-10-11-learning-roadmap.md). 이관 경계: [12-melete-lineage.md](/home/jimmy/repos/full-continual-learning/docs/12-melete-lineage.md).

**2026-11-18 개정 (PROPOSAL): 이름 충돌 정리 보충 행.** 저장소에는 새 P0(NP)·P6(ET)와 이름이 겹치는 것이 이미 있다. 아래 행은 같은 열(`옛 계획 | 옛 단계 | 내용 | 새 위치(phase·작업) | 바뀐 점 | 이유`)로 그 충돌을 정리한다. 이 표에서 「P1」처럼 번호만 쓰면 위 본문(2026-11-12)의 P1–P5를 뜻하고, 새 phase는 문서에서 처음 나올 때 「P0(NP)」, 「P6(ET)」로 쓰며, 2026-11-03 계획은 언제나 「옛(11-03) P0」처럼 쓴다. 옛 PASS/FAIL·산출물을 새 phase의 완료로 옮기지 않는다는 위 원칙은 그대로다.

| 옛 계획 | 옛 단계 | 내용 | 새 위치(phase·작업) | 바뀐 점 | 이유 |
|---|---|---|---|---|---|
| 옛(11-03) P0–P5 | 옛(11-03) P0 | 11월 3일 외부 fast-model 중심 계획(위 「11-03 P0–P5」 행. 단계별 내용 미확인) | 매핑하지 않음. 2026-11-18의 새 P0(NP)–P6(ET)와는 이름만 같다 | 새 phase로 이식하지 않음 | 이름 충돌 방지. 옛(11-03) 계획의 이름은 언제나 「옛(11-03) P0」처럼 쓴다 |
| 옛 로드맵 P0–P6 (11-09 커밋) | P0 연구 계약 | 용어·state clocks·source boundary·baselines·평가 split·budget(위 「FCL P0–P6」 행) | P1-T01~T03·T06으로 흡수됨(2026-11-12 개정). **2026-11-18의 새 P0(NP)는 그 옛 P0를 되살린 것이 아니라 별개다** | 옛 P0는 조사·계약 전용 phase라 폐기됐다. 새 P0(NP)는 실제 CLI·실제 frozen LLM으로 도는 완결 제품(무학습 비모수 POC)이다 | 옛 P0는 점진적 해상도 규칙(B17)과 어긋났다. 새 P0(NP)는 사용자 요청(2026-11-18) 「모델 학습없이 non parameter 기반의 무언가로 POC검증을 먼저 해보자」에서 왔다 |
| 옛 로드맵 P0–P6 (11-09 커밋) | P6 schema 외부화 | offload·version·retrieval·migration·delete(위 「FCL P0–P6」 행) | P1-T10·T13(bundle v0·삭제), P4(외부화 v0), P5(retrieval·migration·multi-user)로 분산됨. 새 P6(ET)와 무관하다 | 새 P6(ET)는 외부화가 아니라 역사 아인슈타인 테스트 최종(ET-4)이다 | 옛 P6는 이미 분산돼 번호가 비었으므로 새 phase가 이름을 쓰되 충돌을 이 행에 남긴다 |
| Synthetic Phase-0 (experiments/phase0, ARCHIVE) | 합성 Bayesian linear prediction | 공유 연속 prior의 표본 효율 실험. 통합 모델 PoC가 아니다([README.md](/home/jimmy/repos/full-continual-learning/experiments/phase0/README.md)) | 완료 승계 없음. 새 P0(NP)와 무관하다 | 새 P0(NP)의 결과를 Phase-0의 PASS로 읽거나 그 반대로 읽지 않는다 | [AGENTS.md](/home/jimmy/repos/full-continual-learning/AGENTS.md)의 「Synthetic Phase-0은 통합 neural model PoC가 아니다」 유지 |
| research/2026-11-09 추적 우선순위 | P0–P2 | 연구 추적 항목의 읽기 우선순위([2026-11-09-sbl-tracking.md](/home/jimmy/repos/full-continual-learning/research/2026-11-09-sbl-tracking.md), [11-research-agenda.md](/home/jimmy/repos/full-continual-learning/docs/11-research-agenda.md)가 인용) | phase가 아니다. 새 phase와 무관하다 | 새 문서에서 가리킬 때는 「추적 우선순위 P0」처럼 쓴다 | 이름 충돌 방지 |
| Melete P1–P4 | 전체 | 위 「Melete P1–P4」 행 | 위 행 그대로. 새 P0(NP)·P6(ET)와 무관하다 | 바뀐 점 없음 | 같은 번호라도 Melete는 다른 계획이다 |

## 10. 계산 자원과 결정 대기

**PROPOSAL.** 비용이 드는 선택(클라우드 GPU, 유료 API, 큰 모델 다운로드, 장시간 GPU 점유)은 결정 대기로 두고 사용자 결정 전에는 실행하지 않는다. 이 절의 표에는 시간·성능 추정을 쓰지 않았다. 계산 추정(**ESTIMATE, NOT RUN**)은 [15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md)에 따로 있고, 실측은 P1-T04에서 한다. 아래 D-번호는 모두 **OPEN**이다.

| 자원 | 확인된 사실 | P1에 대한 판단 |
|---|---|---|
| host | CPU 16코어, RAM 27GB. 메모리 압박이 잦다(이 초안 작성 중 관측: swap 약 10GB 사용) | 무거운 실행은 직렬로 한다. runtime을 CLI와 별도 프로세스로 둬서 runtime만 재기동한다. 135M급 모델의 CPU 실행 이력은 있으나 CPU 학습 시간은 미측정(T04에서 실측). ESTIMATE: 135M retrofit run 1건이 CPU 유효 0.2–0.5 TFLOPS 가정에서 약 10–25시간이라 학습 장소가 아니다. host는 계약·E2E·회귀 gate(사용자 재현)·세계 생성·소규모 평가의 장소다 |
| 노트북 GPU | RTX 5070 Ti 12GB, SSH 접근. **ARCHIVE:** Melete 2026-10-11 기록에서 12227MiB·Torch 2.9.1+cu128·sm_120을 확인했고 이번 초안에서는 재접속·재확인하지 않았다([2026-10-11-learning-roadmap-feedback.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/implementation/records/2026-10-11-learning-roadmap-feedback.md)) | P1 135M의 retrofit 학습(outer loop)·개발의 기본 후보. ESTIMATE: 약 20 run에 P50 약 7.7시간(P10–P90 1.7–37시간; 노트북 사양은 AI TOPS에서 유도한 가정이며 T04에서 실측). 12GB라 360M은 step당 token을 줄여야 하고 0.6B 이상은 비현실적이며, 연결이 간헐적이라 checkpoint·재개가 필수다. 장시간 점유는 결정 대기(D-04) |
| 로컬 llama.cpp의 Qwen3-8B (GGUF) | 추론 전용 양자화 형식 | retrofit 학습 대상으로 부적합하다. GGUF는 autograd 학습과 layer 개조에 쓰기 어렵고, 원본 8B bf16 가중치는 약 16GB라 12GB VRAM에 학습으로 맞지 않는다. 용도는 참고선(`ctx` + raw history, P2 이후)과 세계 난이도 검사다 |
| 로컬 llama.cpp의 Qwen3-Embedding-0.6B (GGUF) | 생성 모델이 아닌 embedding 모델 | retrofit 대상이 아니다. 용도는 2×2 설계의 표면 유사도(표면 거리)를 재는 보조 도구다 |
| SmolLM2-135M(-Instruct) | 134,515,008 parameters. **ARCHIVE:** Melete E5에서 host CPU로 실행([2026-10-07-e5-self-feedback.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/implementation/records/2026-10-07-e5-self-feedback.md)). Llama 계열 구조로 알려져 있으나 모델 카드·config 확인 필요 | P1 골격 후보 1순위(D-01). 가중치 확보는 사용자 승인 뒤. 세계가 floor에 걸리면 360M 등 상위 크기를 검토한다 |
| 외부 공식 코드 | Titan-Llama pin `sarahpannn/titans-pytorch@c60b4efaa3a3c6df4deebd57cbccf75947b87cad`. 라이선스 기록이 이 저장소에 없다([catalog.tsv](/home/jimmy/repos/full-continual-learning/references/catalog.tsv) A04). review §4.5의 원칙은 라이선스 없는 코드를 읽고 인용만 하고 논문 식에서 재구현하는 것이다 | D-02. 결정 전에는 읽기·인용과 재구현 경로로만 진행한다 |
| runcrate 클라우드 GPU (유료 임대) | **ARCHIVE·스냅샷(2026-11-17 조회, 가격 변동 가능):** 시간 단위 과금(대부분 초 단위), 부팅은 과금되지 않음, 생성할 때 max runtime·idle shutdown을 지정할 수 있고 terminate는 로컬 디스크를 지운다. GPU 상품 152개(vm·container). 소형 모델 학습 후보는 48GB급 1장 VM 시간당 약 $1.2–1.4(RTX 6000 Ada·L40S), 대형은 A100 80GB 약 $1.7·H100 약 $3.1–3.9. 현재 쓸 수 있는 키는 다른 프로젝트 계정에 속해 예산이 공유된다 | 비용 결정 대기(D-04). 계획과 추정(ESTIMATE, NOT RUN)은 [15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md)에 있다. P1은 host·노트북으로 시작할 수 있고 클라우드가 실질적으로 필요해지는 곳은 P2 학습부터다(ESTIMATE). 사용자 비용 승인 전에는 인스턴스 생성·유료 API·GPU 사용·가중치 다운로드를 하지 않는다 |

| ID | 결정 | 선택지 | 추천 | 비용 발생 | 결정자 |
|---|---|---|---|---|---|
| D-01 | P1 base model | (a) SmolLM2-135M (b) SmolLM2-360M (c) Qwen3-0.6B (d) 1B급 | (a)로 골격·개발. T07·T12의 floor 검사에서 막히면 (b). 2026-11-17 후보 점검: 추천은 바뀌지 않는다. Granite-4.0-350M-Base(dense decoder, 한국어 포함)는 P5 후보, Qwen3.5-0.8B-Base(Gated DeltaNet 하이브리드)는 retrofit base로 부적합해 OPEN 후보로만 둔다([15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md) §6.2) | 가중치 다운로드(작음), 크기가 커지면 학습 시간 증가 | 사용자(크기 상향·다운로드 승인) |
| D-02 | Titan-Llama 코드 사용 방식 | (a) 라이선스 확인·허가 뒤 코드 사용 (b) 논문 식에서 재구현, 코드는 읽기·인용만 (c) 비공식 구현(lucidrains/titans-pytorch) 참고 | (b). 라이선스가 명시적으로 허용하면 (a) 재검토 | 재구현 공수(금전 비용 없음) | 사용자 |
| D-03 | P1 구조 family | (a) 역할–결과 규칙 세계 (b) 순서 추론 (c) 쌍 연합·cue→goal (d) 자연어 소규모 관계 그래프 | (a) 단독. (b)는 P2 family 후보 | 없음 | 사용자(방향), 설계 담당(세부) |
| D-04 | retrofit 학습의 계산 장소·시간 상한 | (a) host CPU만 (b) 노트북 GPU (c) 클라우드 GPU | 2026-11-12 추천(개정 대상): T04 실측 뒤 (b)의 시간 상한을 먼저 승인. (c)는 P5 전까지 보류. **2026-11-17 개정 추천 (PROPOSAL·ESTIMATE(NOT RUN)·OPEN):** (b)로 P1 135M 개발·T09를 시작하되 노트북 시간 상한과 재개 조건을 먼저 승인. (c)는 둘로 나눠 묻는다: ① T04의 소액 microbenchmark(2종, ESTIMATE P50 약 $7.6, 상한 $12)를 승인 요청, ② 학습·readout용 (c)는 T04로 보정한 phase별 비용 상한을 phase 시작 때 따로 승인. '(c)는 P5 전까지 보류'는 근거가 약해 철회를 제안(P2 학습만 노트북 환산 P50 약 82시간, [15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md) §10). 결정은 사용자이고 OPEN | (b) GPU 장시간 점유, (c) 금전 | 사용자 |
| D-05 | readout 통계 계획 | seed·world 수·candidate 수 상한: pilot 분산 기반 최소 n(구간 폭 계획) 또는 고정 소수 | 분산 기반, 상한만 먼저 승인(Melete J1은 candidate 3개 상한을 썼다, ARCHIVE) | 계산 시간 | 사용자(상한), P1-T14(수치) |
| D-06 | P1에 source 삭제 포함 | (a) fast 한정 얇게 포함 (b) P2로 이월 | (a). 저장·원장 뼈대를 P1에서 검증한다 | 작음(재생 공수) | 사용자 |
| D-07 | P1에서 sealed readout 실행 | (a) P1 종료 gate에 포함 (b) dev pilot까지만 하고 확증은 P2 | (a). 효용 gate를 집행하려면 필요하다 | seed × arm 실행 시간 | 사용자 |
| D-08 | 참고선 Qwen3-8B+raw history 도입 시점 | P1 / P2 / 미도입 | P2 | 로컬 추론 시간 | 설계 담당 제안, 사용자 확인 |
| D-09 | 세계 렌더링 언어 | 영어(SmolLM2) / 한국어(Qwen3 계열) | P1은 영어 합성 세계, 한국어·자연어는 P5 | 없음 | 사용자 |
| D-10 | self-evolution 자동화 범위·예산 | 수동 유지 / P3부터 승인된 예산·search space 안에서 자동 | P1–P2는 수동·v1, P3 자동은 별도 승인([10-evolution-policy.md](/home/jimmy/repos/full-continual-learning/docs/10-evolution-policy.md) §6) | 자동 학습·GPU | 사용자 |
| D-11 | 외부 agent 연결 대상·방식·시점 | codex / prime agent, tool(MCP) 대 endpoint | P4 종료 재검토에서 결정. 진입 조건은 §7 | 연결 공수 | 사용자 |
| D-12 | 두 번째 base model·크기 | 다른 크기 / 다른 계열 | P4 종료 재검토에서 결정 | 다운로드·학습(클라우드 가능성. ESTIMATE: P5에서 두 번째 모델이 1.7B이면 P50 $548(P10–P90 $141–2,537), 360M이면 P50 $205($66–791), [15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md) §6.4). 후보로 Granite-4.0-350M-Base(한국어·dense·Apache-2.0)와 Qwen3-1.7B를 추가 검토(OPEN) | 사용자 |
| D-13 | 위상(phase) 조율(D) 실험의 배치 | P3 말미 / P4 / 미도입 | P3 종료 재검토에서 C(event/readiness)를 기준선으로 삼아 결정 | 계산 시간 | 사용자 |
| D-14 | schema 판단 구조(controller)의 최소형을 P1에 넣을지 | (a) P3에 두고 P1은 write 정책 접점만 (b) P1에 규칙형 controller v0(경로 선택만) (c) P1에 학습된 문맥 head | **(b)로 반영(2026-11-12 마스터 설계 판단, 사용자 확인 대기).** U-T07 원문은 핵심 거동을 "익숙하면 매우 빠르게, 덜 익숙하면 rapid learning, 더 낯설면 더 깊은 loop"로 정의하고 "이 과정에서 입력 문맥에 대한 schema판단 mlp나 구조를 넣어서"라고 했다. 점진적 해상도 규칙은 P1이 핵심 여정 전체를 얇게 관통하라고 요구한다. 초안의 추천 (a)는 원인 혼동을 우려했으나 `noctl` 대조 arm으로 경로 선택의 기여를 분리한다. (c)는 P3 | P1 공수 증가(controller v0·r=2 적응 학습·`noctl` arm) | 사용자 확인 |

비용이 드는 선택은 D-01(크기 상향)·D-04·D-10·D-12이고, D-13은 계산 시간이 들고, D-14 반영으로 P1 공수가 늘었다(controller v0·r=2 적응 학습·`noctl` arm).

**2026-11-17 갱신 (PROPOSAL):** 11-12 이후의 새 사용자 원문(11-16 블록 2개, 11-17 요청)에 비춰 위 결정을 다시 봤다. 영향이 있는 것은 D-01·D-04·D-12(11-17 요청: runcrate 사용환경을 전제로 한 비용효율·품질 균형 계획)와 D-14(11-16 CRUD 블록: 문맥 기반 schema 탐색과 update/create 분기)다. 나머지 10개는 변화가 없다. 해소된 결정은 없고 전부 OPEN이다. 근거와 11-12 감사 §5의 사용자 확인 19건의 판정은 [2026-11-17-design-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review.md) §7에 있다.

**결정 후보 (2026-11-17 CRUD·간섭 검토, PROPOSAL; D-번호는 사용자 결정 목록에 오를 때 부여):**
- Delete/Retain(기능적 망각/보존)의 정책을 어느 phase에 둘지. 제안: 측정은 P1부터(이미 있음), 정책은 P4(offload·Sleep)에서 얇게, 압축·폐기는 P5. B01과 [2026-11-12-design-audit.md](/home/jimmy/repos/full-continual-learning/research/2026-11-12-design-audit.md) §5 #17이 미해결로 남긴 질문이다. 비용: P4 작업량 증가.
- 사용자 원문 "적합한 schema를 못찾으면 create"를 [14-schema-lifecycle-crud-and-joint-paper.md](/home/jimmy/repos/full-continual-learning/docs/14-schema-lifecycle-crud-and-joint-paper.md) §3처럼 '구조적 새로움이 확인될 때만 create'로 읽어도 되는지. 비용: 없음.
- low-rank expert를 schema 보관 단위의 기본 후보로 올릴지([11-research-agenda.md](/home/jimmy/repos/full-continual-learning/docs/11-research-agenda.md) §2의 열린 문제와의 관계). 비용: 없음.
- 두 가지 '삭제'(기능적 망각/보존 대 source 삭제) 용어 구분의 수용([07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md) §7). 비용: 없음.
- 신규 arm(`ftall`, `adapters`, `sel-*`)과 신규 family(F22·F23·F24)의 채택, 실험 B(Base/Instruct)의 도입. 비용: P2 계산 증가, 가중치 다운로드(D-01·D-12와 연동).
- expert 수·rank·검색 key·분화 기준·retention budget·압축 손실·commit 단위·정답 접근권([14-schema-lifecycle-crud-and-joint-paper.md](/home/jimmy/repos/full-continual-learning/docs/14-schema-lifecycle-crud-and-joint-paper.md) §9)은 아직 결정 항목이 아니다. self-evolution 탐색 변수에 넣을지는 [10-evolution-policy.md](/home/jimmy/repos/full-continual-learning/docs/10-evolution-policy.md) §3을 따른다.

**ESTIMATE (2026-11-17 검토):** 위 비용 선택의 규모를 [15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md)에서 가늠했다(NOT RUN). SmolLM2-135M 기준 P1의 클라우드 비용은 P50 약 $17(P10–P90 $10–35), P1–P4는 P50 약 $198($86–516), P5는 두 번째 모델에 따라 P50 $205(360M)–$548(1.7B)이다. 노트북 환산으로 P2 학습만 P50 약 82시간이라 클라우드 사용 결정은 P2 시작 전에 필요하다. 가격은 2026-11-17 조회 시점이며 변동 가능하다. 어떤 비용도 승인되지 않았고 D-04는 OPEN이다.

**2026-11-18 갱신 (ESTIMATE, NOT RUN):** 위 ESTIMATE의 수치(P1 P50 약 $17, P1–P4 약 $198, P5 $205–$548)는 2026-11-17 기준의 기록이며 고치지 않았다. 2026-11-18에 상품 목록이 192개에서 177개로 바뀌었고(바뀌는 것은 가격이 아니라 목록이다) 11-17 표를 오늘 가격으로 다시 계산하면 변화가 −0.0%에서 +0.3%다. 새 phase와 새 항목의 비용은 [15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md)의 2026-11-18 갱신에 있다. P0(NP)는 §6.7, 시간캡슐 기반 확보 3안은 §6.8, 시간캡슐 기반 retrofit과 ET run은 §6.9, P1 base 크기 비교와 phase별 NP arm·ET 단 추가분은 §6.10, 논문별 실행 수·자원·시간·비용은 §6.11의 「PAPER-k 묶음표」다. 위 P5 수치는 두 번째 모델이 소형일 때의 것이며, 시간캡슐 기반 retrofit이 P5에 더해진 뒤의 P5와 P6의 수치는 docs/15가 따로 가진다(수치를 이 절에 복제하지 않는다). 모두 가정에서 나온 ESTIMATE이고 P0-T04 실측 전까지 바뀐다. 승인된 비용은 없고 D-04·D-19·D-29·N-11은 OPEN이다.

**2026-11-18 개정 (PROPOSAL): 새 결정 후보 D-15~D-47.** 2026-11-18 요청의 설계 작업에서 새로 생긴 결정이다. 위 표(D-01~D-14)와 같은 열을 쓰고 번호는 D-15부터 잇는다. 같은 결정은 한 행으로 합쳤고 기존 결정과 겹치는 것은 새 행을 만들지 않고 번호를 가리켰다(표 아래 목록). 추천은 PROPOSAL이며 결정된 것이 아니다. 어떤 비용도 승인되지 않았고 전부 **OPEN**이다. 위의 비용 수치는 2026-11-17 기준의 기록이며 이번 개정에서 고치지 않았다. 다만 위 자원 표의 「클라우드가 실질적으로 필요해지는 곳은 P2 학습부터다」는 P1–P5 기준의 서술이다. P0(NP)의 대량 readout(추론 전용)과 ET-3p 정식 run은 runcrate에서 돌 수 있고 host는 gate를 재현하는 장소다(D-18·D-19, 비용은 [15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md)).

| ID | 결정 | 선택지 | 추천 | 비용 발생 | 결정자 |
|---|---|---|---|---|---|
| D-15 | phase 구성과 「P1은 MVP」 해석(§1.4 보충 주석) | (a) P0(NP)–P6(ET) 7개 phase. P0(NP)가 뼈대와 전체 여정을 먼저 세우고 P1이 첫 학습 해상도 (b) P0(NP)를 P1 앞쪽 작업으로 흡수(phase 6개, NP arm은 P1의 대조군으로만) (c) P0(NP)와 P1을 한 phase로 합침 | (a). 사용자 원문의 순서(POC를 먼저 하고 그 뒤에 단계별로 구현한다)와 매 phase가 전체 제품이라는 전역 규칙을 함께 만족한다. (b)는 POC가 별도 종료 gate를 가질 수 없다 | 없음 | 사용자 |
| D-16 | P0의 NP 단 범위: NP-2(닫힌 꼴 선형 expert, 파라미터가 있다)를 「비모수」 대역에 포함할지 | (a) 포함 (b) 구현은 선택으로 두되 「비모수」 주장에서는 제외 (c) 제외 | (b). 비모수 주장에는 NP-0·NP-1만 넣는다 | 구현 공수 | 사용자 |
| D-17 | §3 등급 2의 「실제 갱신」을 P0에서 「실제 비모수 state 쓰기」로 읽을지(§3 보충 주석) | (a) 그렇게 읽고 P0 문구에 「비모수」 태그를 단다 (b) 가중치 갱신이어야 하므로 P0의 상한은 등급 1 | (a) | 없음 | 사용자 |
| D-18 | P0 종료 gate에 sealed readout(등급 3 시도)을 포함할지(D-07의 P0판) | (a) 포함 (b) dev pilot(등급 2)까지만 하고 확증은 P1 이후 | (a). D-07과 같은 이유(효용 gate를 집행하려면 필요) | runcrate 대량 readout(승인 시. [15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md)) | 사용자 |
| D-19 | P0의 frozen LLM 주 모델·복제 모델·backend와 가중치 확보 | (a) Qwen3-8B 계열(HF와 GGUF) (b) 다른 계열 8B급 (c) 후보를 더 조사 | (a)로 gate와 readout, 복제 모델은 선택. 후보 확인 뒤 재검토 | HF 가중치(8B bf16 약 16GB)와 시간캡슐 모델 다운로드, runcrate(D-04, N-11) | 사용자 |
| D-20 | P1 base 크기를 135M급으로 둘지 P0·시간캡슐 모델급(1.7B–4B급)으로 올릴지(D-01의 선택지 (a)–(d)에 상향 안을 더하는 질문) | (a) 135M급 유지 (b) 1.7B–4B급으로 상향 | P0의 V0-16 결과(P1 base급에서 NP-1이 성립하는가)를 본 뒤 결정. 기본은 (a) | 상향 시 P1 학습 비용 증가([15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md)) | 사용자 |
| D-21 | hold 경로를 P1 controller v0에도 넣을지(D-14와 연결) | (a) P1부터 fast·learn·deep·hold(hold는 쓰기 없이 trace만) (b) P1은 fast·learn·deep만 두고 hold는 P3부터 | 한쪽으로 고르지 않고 P0의 `np0-nohold` 결과를 본 뒤 결정한다. docs/16은 NP arm과 P1 학습 arm의 경로 집합이 같은 (a)를, docs/18은 기본 (b)를 제안했다 | (a)는 P1 공수 소폭(임계값 하나와 trace 필드) | 사용자 |
| D-22 | NP 대조군의 충실도와 NP-0의 생성·판정 분리 | 계열 대조(요약 기억·통찰 기억·개념 기억 계열)와 그래프·연결 기억 계열 arm: (a) 핵심 연산만 구현한 간이판과 원본과의 차이 기록 (b) 대표 방법의 공식 구현 사용. NP-0의 분리: (a) 같은 LLM·같은 prompt 계열 (b) 판정을 로그우도 비교로 한정해 생성과 분리 (c) 별도 frozen 판정 모델 | 선행 연구 조사 결과를 본 뒤 결정. 먼저 간이판, NP-0은 (b) | 공식 구현 사용과 별도 판정 모델은 구현·계산 비용 | 사용자(NP-0 분리는 설계 담당 제안, 사용자 확인) |
| D-23 | 구현 위치와 Melete 파일 이관 방식 | (a) 공개 저장소의 `fcl/` 패키지에 파일 단위로 이관하고 옮기기 전에 비공개 내용을 점검 (b) 별도 저장소 | (a) | 이관 공수 | 사용자 |
| D-24 | 이상 청사진의 feature 목록에 BF-D4(응답 형성과 불확실성 표현)를 더한 것의 수용과 기존 문서(docs/05·07·13·14) 용어의 개정 범위 | feature: (a) 32개(BF-D4 포함) (b) 31개(BF-D4를 BF-C2·BF-D1에 흡수). 용어: (a) 개정하지 않고 링크로만 연결 (b) 구현 착수 전에 별도 정합 개정 | feature (a). 용어 (a)이고 (b)는 P1 시작 전에 다시 본다 | (b)는 문서 공수 | 사용자(승인), 설계 담당(세부) |
| D-25 | CRUD 판정에서 branch와 create를 나눠 쓸지([14-schema-lifecycle-crud-and-joint-paper.md](/home/jimmy/repos/full-continual-learning/docs/14-schema-lifecycle-crud-and-joint-paper.md) §3의 「새 expert 할당 또는 분화」 한 칸의 분리. 「못 찾으면 create」의 트리거 해석은 N-4가 맡는다) | (a) 나눈다: branch = 같은 계열의 조건별 version 공존, create = 새 schema 할당 (b) docs/14처럼 create 하나에 분화를 포함 | (a). A→B→A 재방문의 보존과 새 구조 할당은 대조 arm과 평가가 다르다 | 없음 | 사용자 |
| D-26 | 발견 feature 묶음과 가설 H-DISCOVER를 헌장에 올릴지(N-8의 U13 질문과 한 번에 묶을 수 있다) | (a) PROPOSAL·OPEN으로 유지하고 헌장은 개정하지 않는다 (b) 헌장 §4에 세 번째 중심 명제와 새 목표 항목을 더한다 | (a). 근거 문헌이 없고 효용이 NOT RUN이다. P0의 ET-0 결과 뒤에 재검토 | 없음 | 사용자 |
| D-27 | 발견 feature(긴장 원장·재조합·후보 원리·통찰 사건·보고)의 학습 모듈을 어느 phase에 둘지 | (a) P3(학습된 hold gate)와 P4(Sleep 재조합·잠복 효과)에 둔다 (b) P5 이후로 미루고 P1–P4는 NP 대역과 측정만 한다 | (a). phase별 ET 단 대응(P3에서 ET-1 판정)을 따르려면 필요하다. P3·P4 공수가 늘고 상한은 그대로다 | P3·P4 공수와 계산([15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md)) | 사용자 |
| D-28 | ET 대상 묶음(주력·pilot·대안과 묶음의 대상 수), 주력의 기반 checkpoint와 T0, 원문 「1904」의 읽기 | 묶음: (a) 주력 Einstein 1905, pilot Planck 1900과 Chadwick 중성자 1932, 대안 일반상대성 1915와 Turing 1936 (b) 주력을 일반상대성 1915로 교체 (c) 주력 둘(Einstein 1905와 Turing 1936). 기반·T0: (a) 1900년 이전만의 체인 checkpoint, T0 1900-01-01 (b) 표준 판 (c) 1905 마감 기반을 비교로 병행. 연도: 입력 구간의 끝을 구성요소별 발견 진술 시점으로 정의하고 「1904」를 오기(Y1) 또는 입력 구간의 끝(Y2)으로 읽는다 | 묶음 (a), 기반·T0는 (a)에 (c)를 병행, 연도는 구성요소별 정의를 유지. 근거는 [17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md) §5와 조사 기록의 후보 매트릭스 | 없음(후속 실행 비용은 docs/15) | 사용자 |
| D-29 | 시간캡슐 기반 모델의 확보 방식(P5–P6), 모델별 라이선스 확인, 공개 상태의 재점검 주기 | 확보: (a) 공개 모델 사용 (b) 소형 자체 사전학습 (c) 중형 자체 사전학습. 라이선스: (i) 확인 전에는 그 모델을 쓰는 대안 대상을 보류 (ii) 저자에게 문의(외부 연락이라 이번 범위 밖). 재점검: phase 시작 때마다 1회 / 하지 않는다 | (a)를 기본으로 하고 (b)·(c)는 (a)가 맞지 않을 때의 선택지. 라이선스는 (i), 재점검은 phase 시작 때마다 1회 | (a) 가중치 다운로드, (b)·(c) 사전학습과 corpus 전처리 비용([15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md)의 확보 3안). 사용자 비용 승인 전에는 하지 않는다 | 사용자 |
| D-30 | ET의 「입력」을 경험을 받는 학습자(L)로 읽을지 대화하는 동반 AI(C)로 읽을지([17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md) §2.4) | (a) L (b) C (c) 둘 다 | (a)를 기본으로 하고 C는 같은 stream 항목의 `render` 변형으로 ET-3 이후에 | 없음 | 사용자 |
| D-31 | ET 판정의 사전 명세 선택: 입력 tier의 주 판정 단위, 용량–반응의 판정 x축, 머리 결과 채널(dev pilot 뒤 확정) | tier: A / A+B / 세 곡선 모두. x축: 날짜 / 항목 수 / token 수. 채널: 자발 / 중립 probe / 주제 probe / 과제 probe | 세 곡선을 모두 보고하고 주 판정은 A+B. 판정 x축은 항목 수(또는 token 수)이고 날짜는 기술용. 머리 결과는 중립 probe | 없음 | 사용자(dev pilot 뒤 확정) |
| D-32 | T0 이후 세계 지식(W_delta)의 투입 방식과 모의 인물(closed-loop) 도입 | W_delta: (a) 인물이 읽은 것은 인물 stream에 흡수하고 사전 규칙으로 고른 공통 stream을 더함 (b) 주지 않음(원문의 「그 이후 특정 인물의 data」만) (c) 별도 stream만. closed-loop: (a) open-loop만 (b) 모의 인물 도입 | W_delta (a). open-loop로 고정하고 closed-loop는 후속 연구 | 모의 인물을 도입하면 현대 LLM 호출 비용 | 사용자 |
| D-33 | ET 채점자 구성 | (a) 사람 전문가 2인 이상(맹검) (b) 사람 1인 + 보조 (c) 현대 LLM 패널만 | (a). 불가하면 등급 3 주장을 쓰지 않는다(등급 2 이하) | 사람 채점자의 시간과 보상 | 사용자 |
| D-34 | P6의 등급 상한과 「아인슈타인 테스트 통과」 문구, 판정의 최소 수준 | 상한: 3 확정 / 4를 시도(두 번째 시간캡슐 기반·두 번째 봉인 대상 묶음). 문구: 금지 유지 / 허용. 최소 수준 [L*]: L3 / L4 | 상한 3, 문구 금지 유지, [L*]는 dev pilot 뒤 사용자 승인 | 4를 시도하면 기반과 사료 확보 비용이 늘어난다 | 사용자 |
| D-35 | ET 사료의 접근·공개 범위·저작권 | 공개: manifest만 / 이용 조건이 허용하는 본문 / 봉인 중 비공개 후 판정 뒤 공개. 접근: (a) 무료 범위로 주력·pilot의 사료를 먼저 확인하고 구독은 P5 시작 때 결정 (b) 지금 구독 | 봉인 중에는 해시만, 판정 뒤 이용 조건이 허용하는 범위만 공개, 합성 입력은 누수 감사 뒤 공개. 접근은 (a) | 사료 이용 허가·편집판 구독 비용이 있을 수 있다(규모 미확인) | 사용자 |
| D-36 | stream 구성에 현대 LLM과 번역을 쓰는 범위 | 현대 LLM 보조: 조건부 허용(입력 tier C 표시·누설도 채점·사람 감사) / 사람만. 영어 전용 기반에서 독일어 사료: (a) 영어 동시대 자료와 당대 영어 요약만 (b) 사람이 한 소멸 저작권의 번역만 (c) 현대 LLM 번역을 시스템 밖 구성 보조로 쓰고 입력 tier C와 누설도 채점을 붙임 | 조건부 허용. 독일어는 (a)와 (b) | 호출 비용 | 사용자 |
| D-37 | 참고 영상의 정체 확인 | (a) 사람이 설명란·자막을 확인해 알려준다 (b) needs-resolution 유지 | (b) | 없음 | 사용자 |
| D-38 | 논문 전략: 동반 논문 PAPER-0b(ET 절차·benchmark 논문)를 낼지, 논문 핵심 주장에 필요한 등급이 phase 상한보다 높을 때의 처리 | PAPER-0b: 낸다 / 내지 않고 PAPER-0에 흡수 / 나중에 결정. 등급 불일치: (a) 그 phase에 등급 3 조건을 채우는 작업을 더한다 (b) pilot 문구의 논문으로 낸다 | 논문별로 [19-paper-plan.md](/home/jimmy/repos/full-continual-learning/docs/19-paper-plan.md)가 두 안을 나란히 쓴다. PAPER-0b는 P0 직후의 동반 논문 후보로 계획만 둔다. 외부 발송·연락은 범위 밖 | (a)는 해당 phase의 공수·계산 증가 | 사용자 |
| D-39 | 외부 발견 benchmark 앵커: NP arm을 공개 benchmark(예: NewtonBench·LLM-SRBench) 한 곳에서 한 번 돌려 ET-0의 외부 타당도 증거를 만들지 | (a) P0 말미에 benchmark 1개에서 한 번 (b) 하지 않는다 | (a). 공개 데이터의 접근·라이선스를 확인한 뒤 | 계산 소량(이 run은 [15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md)의 실행 행렬에 아직 없다) | 사용자 |
| D-40 | 투고 준비 정책: (i) 제출 4주 전에 가장 가까운 선행 연구를 다시 조회하는 gate(2026-06 이후 preprint는 심사 전이다) (ii) PAPER-0b의 투고 성격 | (i) 둔다 / 두지 않는다. (ii) 평가·데이터 트랙형 / 저널형 / 일반 ML 본 트랙 | (i) 둔다. (ii) 2027 회차 공지를 확인한 뒤 평가·데이터 트랙형을 우선 검토 | 없음 | 사용자 |
| D-41 | 외부 공개의 시점: 사전 등록(manifest hash)과 preprint | 사전 등록: (a) 봉인 때 hash만 공개 (b) 제출 때 공개 (c) 결과 공개 후. preprint: (a) 투고와 동시 (b) 결과 확정 뒤 (c) 하지 않음 | 사전 등록은 (a)이고 내용은 제출 때. preprint는 사용자 결정이다. 어느 쪽이든 외부 공개 행위이므로 승인 전에는 게시하지 않는다 | 없음 | 사용자 |
| D-42 | 논문 단위 정책: phase마다 1편으로 고정할지, PAPER-0의 범위(주장이 넓다) | 단위: (a) 고정 (b) 인접 phase를 합본 (c) 일부 phase는 기술 보고로 대체. PAPER-0: (a) 한 편 (b) 둘로 분리(구조 전이·간섭·생명주기 / 경로·Sleep·발견·잠재 artifact) | 단위는 (a)로 시작하고 phase 종료 재검토에서 조정한다. PAPER-0은 계획을 한 편으로 쓰고 V0 결과를 본 뒤 분리를 결정한다 | 없음 | 사용자 |
| D-43 | 핵심 주장이 FAIL일 때 negative-result판 논문을 낼지 | (a) 항상 낸다 (b) 핵심 주장 FAIL만 낸다 (c) 내부 기록만 | (b). 투고처는 별도 결정 | 작성 시간 | 사용자 |
| D-44 | 논문 공개물의 범위 | (a) 세계 생성기·평가 harness·manifest·원장 요약·stream 목록과 해시 (b) (a)에 retrofit 가중치를 더함 (c) 공개하지 않음 | (a). 사료 원문과 비공개 경로는 제외한다. 가중치는 별도 결정 | 없음 | 사용자 |
| D-45 | 논문 제목에 「Einstein」을 쓸지와 「통과」 문구 정책(D-34와 함께 본다) | (a) 쓰지 않는다 (b) 「Einstein-style」 수식어만 쓴다(PAPER-0b 작업 제목) (c) 제한 없이 | (b)는 PAPER-0b에만, PAPER-6 제목은 (a). 「통과했다」는 쓰지 않는다 | 없음 | 사용자 |
| D-46 | P0 대량 readout의 서빙 방식과 보조 run의 모델 크기(D-19의 모델 선택과 함께 본다) | (a) HF eager 8B급 (b) 서버형 continuous batching (c) 4B급 복제·보조 run (d) 서버형과 4B급 | (b)를 기본으로 검토하되 「같은 CLI·session 프로토콜·runtime 경로」의 동등성과 NP-1 hook 호환을 P0-T04에서 확인한 뒤에 정한다. 주 모델은 8B급을 유지한다 | 있음(금액은 [15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md) §6.7) | 사용자 |
| D-47 | 자체 사전학습용 다중 GPU 노드와 월 약정(D-29에서 소형·중형 자체 사전학습을 고를 때만 해당) | (a) 쓰지 않는다 (b) 소형 자체 사전학습에서만 4장 이상 노드 1개 | (a). D-29에서 자체 사전학습을 택하면 다시 묻는다 | (b)에서 있음([15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md) §6.8) | 사용자 |

**새 행을 만들지 않고 기존 번호를 가리킨 것 (2026-11-18 개정):** D-01(P1 base model. D-20이 선택지를 넓힌다), D-04(계산 장소. D-19·D-29의 비용이 연결된다), D-05(통계 계획. P0·ET의 판정 기준 값 [δ]·[ε]·[L*]·seed 수는 D-05의 확정 시점을 따른다), D-07(P1의 sealed readout. D-18이 P0판), D-09(P1은 영어 합성 세계. P0 세계의 언어는 [18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md)가 밝힌다), D-12(두 번째 base model·크기. P5의 두 번째 base 후보에 시간캡슐 모델이 더해지며 확보 방식은 D-29), D-11(외부 agent 연결. 외부 consumer 접점을 P0부터 얇게 둘지는 이 결정에 합쳤고 추천은 위 §4 그대로 P5부터다), D-14(controller v0. hold는 D-21), N-3(Delete/Retain 정책의 phase), N-4(「못 찾으면 create」의 해석. branch와 create의 분리는 D-25), N-5(F22–F24·새 arm·실험 B), N-8(지속학습의 목적을 헌장 U13으로 올릴지. D-26과 묶을 수 있다), N-10(문서 검사기의 절대 링크 처리), N-11(FCL 전용 runcrate 키·예산), 11-12 감사 §5의 사용자 확인 #7–#11·#17(이상 청사진이 해당 feature에 가리킴). 논문·계산 단계의 후보 가운데 P0 대조군의 구현 출처는 D-22에, PAPER-0b를 낼지와 필요 등급이 phase 상한보다 높을 때의 처리는 D-38에, Ali 공동논문과의 관계는 N-6에, 실험 B의 배치는 N-5에, FCL 전용 키·예산과 P0의 클라우드 상한은 N-11(과 D-04)에, 시간캡슐 기반 확보 안은 D-29에, P1 base 크기는 D-20에 합쳤다. 비용이 드는 새 결정은 D-18·D-19·D-20·D-21·D-22·D-27·D-29·D-33·D-34·D-35·D-39·D-46·D-47이다.

## 11. 로드맵 재검토 규칙

**PROPOSAL (B07·B17).** 계획 상세도는 점진적이다. 이 문서는 P1만 작업 단위까지 쓰고 나머지는 목표·gate까지만 쓴다. 상세 계획은 해당 phase를 시작할 때 쓴다.

1. **phase 시작.** 직전 phase의 종료 재검토(아래 4)를 읽고, 그 phase의 상세 계획(작업 단위를 파일·함수·테스트·명령 수준으로)을 별도 계획으로 써서 사용자 검토를 받는다. P1은 이 문서의 작업 단위를 같은 방식으로 내려 쓴다. 해당 phase 열을 §4 표에서 "계획"에서 "확정 계획"으로 갱신하고 먼 phase는 목표·gate만 유지한다.
2. **phase 중.** 작업 단위마다 완료 판정 한 줄로 self-check한다. spike 결과가 계획을 바꾸면 즉시 §4와 §5를 고치고 변경 기록에 남긴다. 호스트 자원이나 권한 문제로 막히면 우회하지 않고 멈춰 보고한다.
3. **phase 종료: self-feedback 세 질문(B07).**

| 질문 | 무엇과 대조하나 | 판정 |
|---|---|---|
| 의도한 방향인가 | §1.1의 사용자 제약, 헌장 U01–U12, 그 phase의 목표·상한 | 어긋나면 멈추고 보고 |
| 의도대로 구현됐는가 | Contract gate·자동 테스트·E2E 기록 | FAIL이면 같은 phase 안에서 개선(§7) |
| 단계 기준을 충족하는가 | 종료 gate 항목별 PASS/FAIL. Efficacy는 결과 상태와 등급을 따로 | PASS면 다음 phase 시작, FAIL이면 §7 분기. 권한·필수 인프라 문제로 막히면 멈추고 보고(BLOCKED) |

4. **로드맵 재검토(phase 종료마다).** (a) §4 표에서 도달한 셀과 계획한 셀을 대조한다. (b) 앞 phase 시나리오의 회귀 결과를 확인한다. (c) 주장별 등급이 상한 안에 있는지 확인한다. (d) "미루는 것" 목록과 열린 결정(§10)을 갱신한다. (e) 먼 phase를 쪼개거나 합칠지 결정한다(특히 P5). (f) 변경 기록에 남긴다.
5. **재검토가 막지 못하는 것.** 이 절차는 사용자 승인을 대신하지 않는다. 범위·예산·권한이 바뀌는 변경은 사용자 결정(§10)을 거친다.

**2026-11-18 개정 (PROPOSAL): 점진적 해상도 자체 점검표.** phase마다 사용자 전역 규칙(B17)의 네 질문에 답한다. 모든 phase는 「예, 아니오, 아니오, 아니오」여야 하고 하나라도 어긋나면 그 phase를 다시 나눈다. 근거는 각 phase의 종료 gate (1)이다.

| phase | 실제 UI와 실제 의존성으로 끝까지 도는가 | 한 계층만 만드는가 | mock만으로 도는가 | 조사만 하는가 | 근거(종료 gate) |
|---|---|---|---|---|---|
| P0(NP) | 예. 실제 `fcl` CLI, 실제 frozen 공개 가중치 LLM, 실제 비모수 state 저장·재시작으로 UJ0 전체 | 아니오. 경험 입력부터 Sleep·발견(ET-0)·ET-3p까지 전 여정을 가장 얇게 | 아니오 | 아니오. spike는 P0 앞쪽 작업이다 | §5의 P0(NP) 절 종료 gate (1) |
| P1 | 예. 실제 CLI·실제 pretrained 가중치·실제 write·실제 재시작으로 UJ1과 대조 6 arm | 아니오 | 아니오 | 아니오 | P1 종료 gate (1) |
| P2 | 예. UJ2를 arm × depth로 | 아니오 | 아니오 | 아니오 | P2 종료 gate (1) |
| P3 | 예. UJ3 결정 trace와 복원 | 아니오 | 아니오 | 아니오 | P3 종료 gate (1) |
| P4 | 예. 실제 sleep 학습·저장/offload/reload·재시작(UJ4) | 아니오 | 아니오 | 아니오 | P4 종료 gate (1) |
| P5 | 예. 실제 agent·실제 가중치·외부 consumer(UJ5) | 아니오 | 아니오 | 아니오 | P5 종료 gate (1) |
| P6(ET) | 예. 실제 CLI, 실제 시간캡슐 기반 가중치, 봉인된 인물 stream의 시간순 투입(UJ6) | 아니오. 평가만 하는 phase가 아니라 P5까지의 모듈이 긴 인물 stream 위에서 도는 제품이다 | 아니오 | 아니오. 사료 조사와 stream 구성은 P6 앞쪽 작업이다 | §5의 P6(ET) 절 종료 gate (1) |

| 날짜 | 변경 | 이유 | 영향 |
|---|---|---|---|
| 2026-11-12 | 점진적 해상도 규칙에 맞춰 로드맵 전면 재구성(초안, PROPOSAL) | 옛 P0–P6가 B17과 어긋남(문서 맨 앞 상자) | 전 절. 옛 §2·§4·§5·§6은 갱신해 유지 |
| 2026-11-12 | 검수 반영: 규칙형 controller v0와 deep 경로(r=2)를 P1에 넣고 `noctl` 대조를 추가(D-14), H4 text interface 서술을 OPEN으로 낮춤, B 번호 기간 정정 | U-T07 원문과 점진적 해상도(핵심 여정 전체를 P1에서), 설계 감사의 H4 판정(정리자 추론) | §1.1·§1.2·§1.4·§2·§4·§5 P1–P3·§6·§9·§10 |
| 2026-11-17 | 델타 설계 반영 감사의 편집 반영: 11-12 감사 이후 동기화 자료(docs/13·14, 11-16~17 기록)와 사용자 공유 링크 연구 카드의 항목별 대조 결과를 §1.1(U-T12·U-T14 행)·§4-1(CRUD 대응)·§5 P1·P2·P4의 주석과 후보 readout·§6-1(간섭·CRUD 실험 배치)·§10(결정 후보·열린 결정 영향)으로 옮김(전부 PROPOSAL·OPEN, 구현·실행 0회) | 사용자 요청(2026-11-17) '오늘 날짜 기준으로 다시 검토해봐'와 '저장소 반영'. 근거: [2026-11-17-design-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review.md) | §1.1·§4-1·§5 P1·P2·P4·§6-1·§10. phase·데모 시나리오·넓이/깊이 변화·보장과 상한·종료 gate·미루는 것은 바뀌지 않음 |
| 2026-11-17 | 계산 자원 계획 추가: runcrate 클라우드 GPU 사용 계획([15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md)) 신설, §10의 자원 표·D-04·D-01·D-12 개정안 제안(전부 OPEN, 비용 승인 없음) | 사용자 요청(2026-11-17): Melete 구현·학습에 runcrate를 과하지도 최소도 아닌 사양으로 쓰는 방법 | §10과 신규 문서. phase·데모 시나리오·넓이/깊이·보장과 상한·종료 gate·미루는 것은 바뀌지 않음 |
| 2026-11-18 | 사용자 요청(2026-11-18)에 따라 phase를 P0(NP)–P6(ET) 7개로 보충: 머리 상자 개정 주석, §1.2·§1.3 주석, §1.4 보충 phase 표와 「P1은 MVP」 해석 주석, §3 상한 보충 행과 「실제 갱신」 읽기, P0(NP) 절·P6(ET) 절 신설(UJ0·UJ6), §4 보충 표(NP 대역 / 학습 모듈), P1–P5 조정 주석, §6 회귀 gate 보충 행, §7·§8·§9 보충, §10 새 결정 후보, §11 점진적 해상도 자체 점검표(전부 PROPOSAL·OPEN, 구현·실행 0회) | 사용자 요청(2026-11-18): 이상 청사진, 모델 학습 없는 비모수 POC 먼저, 단계별 구현·논문 계획, 아인슈타인 테스트 설계. 근거: [2026-11-18-blueprint-et-design.md](/home/jimmy/repos/full-continual-learning/research/2026-11-18-blueprint-et-design.md) | 기존 P1–P5의 데모 시나리오·넓이/깊이 변화·보장과 상한·종료 gate·미루는 것은 바뀌지 않았다(조정 주석만). 앞뒤에 phase가 더해졌고 NP arm이 이후 모든 phase의 영구 대조군이 된다 |
| 2026-11-18 | 통합 보충: §10에 새 결정 D-39~D-47(논문·공개·계산 쪽)을 잇고 기존 번호(N-5·N-6·N-11·D-20·D-22·D-29·D-38)와 겹치는 후보를 합친 것을 적음, 11-17 비용 수치 아래에 「2026-11-18 갱신」 주석을 더함, P6(ET) 종료 gate의 판정 대상 주장을 [19-paper-plan.md](/home/jimmy/repos/full-continual-learning/docs/19-paper-plan.md)의 C6-1~C6-4로 맞춤, 설계 작업의 가칭 결정 번호를 최종 번호로 바꿈(전부 PROPOSAL·OPEN, 구현·실행 0회) | 같은 요청(2026-11-18)의 통합 작업. 근거: [2026-11-18-blueprint-et-design.md](/home/jimmy/repos/full-continual-learning/research/2026-11-18-blueprint-et-design.md) §4–§6 | §10·§5 P6(ET) 종료 gate. 앞 행의 phase·데모 시나리오·넓이/깊이·보장과 상한·종료 gate 구조는 바뀌지 않았다 |
