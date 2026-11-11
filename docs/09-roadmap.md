# 09. 단계별 MVP: 처음부터 전체 여정을 돌리고 해상도를 높이는 로드맵

**상태 라벨:** 이 로드맵 전체는 **PROPOSAL**이다. phase 경계, 작업 단위, seed 수, 예산, base model, 통계 방법은 사용자가 승인한 값이 아니며 구현·실행 완료를 뜻하지 않는다. 사용자가 명시한 제약(**USER**)은 §1.1에 날짜와 함께 따로 적었다. 문헌 주장(**LITERATURE**)은 이 저장소의 자체 정리를, 과거 기록(**ARCHIVE**)은 이 저장소의 보존본과 고정 커밋의 Melete 기록을 가리킨다. 둘 다 이번 개정에서 새로 실행하거나 재검증한 것이 아니다. 미결정 사항은 **OPEN**(§10의 D-번호)으로 표시한다. 마지막 개정: 2026-11-12.

> **무엇을, 왜 바꿨나**
> - **왜:** 옛 로드맵(P0 연구 계약 → P6 외부화)은 사용자 전역 규칙 "점진적 해상도"(B17, 2026-10-21)와 어긋났다. 조사·계약 전용 phase(P0)가 있었고, phase가 계층·부품별(재귀·controller·Sleep·확대·외부화)로 나뉘었으며, phase 종료물이 "실제로 쓸 수 있는 전체 제품"으로 정의되지 않았고, 데모 시나리오·넓이/깊이 변화·상한·미루는 것·capability 표가 없었다.
> - **무엇을:** 매 phase가 끝날 때마다 `fcl` CLI에서 실제 pretrained 소형 모델이 경험 입력부터 재시작 복원까지 전체 여정을 돈다. phase가 지날수록 같은 제품의 넓이(구조·층·모델·인터페이스)와 깊이(쓰기·정정·계산·공고화·검증)가 함께 올라간다. phase는 5개다.
> - **P0과 spike:** P0은 phase가 아니라 P1 앞쪽 작업(P1-T01~T03)으로 흡수했다. spike도 각 phase의 앞쪽 작업이다. 대조군(고정·무구조·항상-갱신)과 망각·표면/구조 평가는 P1부터 들어간다.
> - **숨기지 않은 것:** 옛 P0–P6와 더 오래된 계획(11-03 P0–P5, Melete N0–N5·J0–J5·P1–P4)은 §9 기존 계획 대응표에 남겼다. 옛 PASS/FAIL·산출물을 새 phase 완료로 옮기지 않는다.
> - **살린 것:** 옛 §2 최소 사용자 여정 → P1의 UJ1, 옛 §4 중단·전환 조건 → §7, 옛 §5 지속 자산 → §8, 옛 §6 기존 phase와의 관계 → §9. 옛 §3 초기 실행 순서 8단계는 §9 대응표에서 작업 단위로 옮겼다. 순서상 가장 큰 변경은 관계 전이·few-shot 과제(옛 5단계)를 고정 깊이 재귀(옛 4단계)보다 앞으로 당긴 것이다.

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

### 1.3 FCL은 모델 제품이다 — "agent 제품은 CLI에서 실제 LLM으로 실제 일을" 규칙의 적용

**USER (B17):** agent 제품이면 claude·codex·prime agent처럼 CLI(TUI)로 실행해 실제 LLM을 연결하고 실제 일을 끝까지 시킬 수 있어야 한다. 실제 사용자 인터페이스와 실제 의존성으로 처음부터 끝까지 돌아야 하고 mock-only는 증거가 아니다.

**PROPOSAL:** FCL은 agent가 아니라 모델 제품이다. 별도 판단기와 외부 LLM의 조합이 최종 제품이라는 해석은 사용자 정정(U-T07)으로 대체됐다([AGENTS.md](/home/jimmy/repos/full-continual-learning/AGENTS.md), [01-intent-and-charter.md](/home/jimmy/repos/full-continual-learning/docs/01-intent-and-charter.md) §5). 그래서 규칙의 정신을 이렇게 옮긴다.

- **실제 LLM:** retrofit한 모델 자체다. 외부 frozen LLM에 원문을 붙인 경로는 최종 제품이 아니라 강한 대조군(`ctx`)으로 유지한다.
- **실제 인터페이스:** `fcl` CLI 세션이다. 평가 harness도 같은 CLI와 같은 session 프로토콜을 통해 모델을 호출한다.
- **실제 일:** 새 개체에 대한 질문에 모델이 답하고, 반례를 받아 고치고, 재시작 뒤에도 유지하는 여정 자체다. 연구용 작은 합성 모델·세계는 이 일의 재료이고, 실제 외부 consumer와 역할이 다르다.
- **외부 agent(codex·prime agent) 연결:** 모델 제품의 소비자(consumer)를 넓히는 **넓이 확장**이며 P5에 둔다. B12의 목표이고, B13·B14의 비판(효용 근거 없이 연결 구조부터 만들지 않는다)을 진입 조건으로 반영한다(§7).

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

## 5. Phase별 계획

**PROPOSAL.** 모든 phase를 같은 라벨 줄로 쓰고 가까운 phase일수록 상세하다. P1은 작업 단위까지, P2는 목표·작업 묶음·gate까지, P3 이후는 목표와 종료 gate 중심으로 짧게 쓴다. UJ1~UJ5(User Journey)는 phase별 데모 시나리오, 곧 전체 여정의 이름이며 뒤 phase의 회귀 gate가 된다(§6). 모든 phase의 종료 gate는 (1) 실제 인터페이스·실제 의존성 E2E, (2) 앞 phase 데모 시나리오 전부의 회귀, (3) 자동 테스트를 포함한다.

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
  - **P1-T05 spike: 최소 retrofit.** 1–2개 layer에 NMM 경로, 1–2개 FFN에 CMS 분기(B_j=0)를 붙여 (i) 초기 출력이 base와 허용오차 안에서 같은지(함수 보존), (ii) 새 모듈이 freeze되지 않는지(trainable-name 규칙, [05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §6), (iii) test-time write가 실제 state를 바꾸는지 확인한다. **완료 판정:** 세 검사가 자동 테스트로 PASS하거나, 실패 원인과 축소 범위(예: NMM 제외·CMS 분기만)가 사용자에게 보고되고 P1 상한 문구에 반영돼 있다.
  - **P1-T06 세계 생성기와 renderer (D-03).** 구조 family 1종 × 개체 이름 pool × 표면 template, 학습용 renderer와 평가용 paraphrase renderer 분리, 규칙 문장 없이 경험만 렌더링, train/dev/sealed world의 seed 분리(sealed cohort는 T14 봉인 뒤에 만든다). **완료 판정:** seed → 같은 hash로 결정론 재생, 관측 0/1/3/10별 식별 가능 질의 비율 보고, 누수 audit 0건.
  - **P1-T07 뼈대 E2E (walking skeleton).** `fcl` CLI와 runtime을 별도 프로세스로 두고 session 프로토콜을 정의한다. 실제 pretrained 가중치를 로드해 `base`·`ctx` arm으로 경험 입력 → 질문 → 응답 → 저장 → runtime 종료 → 새 프로세스 복원을 한 줄기로 잇는다. **완료 판정:** mock 없이 실제 가중치로 돈 E2E 스크립트의 증거 원장 기록과 재시작 전후 프로세스 ID 변경이 있다. 같은 경로로 `base`·`ctx`의 dev 세계 ceiling/floor와 copy baseline을 보고한다(ceiling이나 floor에 붙어 있으면 dev에서만 난이도를 조정하고, 통과 전에는 T14 봉인으로 가지 않는다).
  - **P1-T08 retrofit runtime과 arm.** T05의 모듈을 runtime에 통합하고 committed snapshot → request-local working state → commit write engine(write 정책 접점 포함: Titans식 surprise 정책과 항상-갱신 정책), 규칙형 controller v0(익숙함 신호 두 임계값 → fast/learn/deep, deep = retrofit 블록 r=2)와 결정 trace 필드, 시계 기록, budget meter, `--arm`(`full`·`fixed`·`flat`·`always`·`noctl`) 전환을 구현한다. **완료 판정:** 같은 CLI·같은 session 프로토콜에서 `--arm`만 바꿔 다섯 arm이 돌고 응답마다 결정 trace가 남으며 원장에 arm별 write 수·step·FLOPs 추정이 같은 단위로 남으며, 각 arm이 T03 정의와 일치함을 검사하는 테스트가 PASS한다.
  - **P1-T09 retrofit 학습 (outer loop).** 평가 세계와 분리된 train world로 NMM·CMS 모듈을 학습해 test-time write가 query loss를 줄이게 하고, deep 경로의 r=2 적용에 대한 짧은 적응 학습(retrofitted recurrence의 최소형)을 같은 예산 안에 포함하고 arm별 checkpoint를 만든다(`fixed`는 학습하지 않고 나머지는 같은 학습 예산). 계산 장소·예산은 D-04. **완료 판정:** arm별 학습 예산·곡선이 원장에 있고, 학습 뒤 원능력 probe(일반 텍스트 perplexity·비세계 질문)가 base 대비 값으로 기록돼 있다(임계 판정은 T14 봉인 뒤이며 효용 판정이 아니다).
  - **P1-T10 상태 계약 구현.** bundle manifest v0([07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md) §5의 부분집합), 원자적 commit, 복원, 모델 revision mismatch 거부, 최소 상태 회귀(재전송·같은 ID 다른 payload·중단된 update·restart·rollback·삭제·mismatch·동시 write 거부)를 구현한다. **완료 판정:** 저장 → runtime 종료 → 복원 뒤 같은 질문의 응답과 log-prob이 허용오차 안에서 같고, 위 회귀가 자동 테스트로 PASS한다(Contract 한정).
  - **P1-T11 관찰과 인과 개입.** `fcl diff`(layer·module별 변화량·clock·write 수), probe 질문의 전/후 응답 분포, wrong-schema state swap(다른 세계의 state를 복원 경로로 이식해 같은 질문을 던짐)을 구현한다. **완료 판정:** arm 정의표가 "바뀌어야 한다/바뀌면 안 된다"고 한 state 집합의 diff가 그대로 관측된다는 테스트가 PASS한다(관찰 가능성 검사이며 schema 형성의 증거가 아니다).
  - **P1-T12 평가 harness와 보고서.** dev world에서 UJ1 전체를 모든 arm으로 자동 실행(`fcl eval`)하고 지표를 낸다: 새 개체 전이(관측 0/1/3/10), 표면 함정 negative transfer(2×2), 반례 뒤 국소 수정과 최초 과제 재평가(망각), 이전 조건 재방문(ABA), 원능력 보존, both-correct condition pairs. 보고 생성기는 결과 상태와 등급을 필수로 찍고 등급에 맞지 않는 문구를 검사기로 막는다. **완료 판정:** 모든 arm이 같은 형식의 보고서를 내고 등급 필드가 "등급 2"로 찍히며, 금지 문구 검사기가 시험 문서에서 작동하고, dev 결과로 모든 arm의 ceiling/floor 판정이 보고서에 있다.
  - **P1-T13 source 수정·삭제 (얇게).** 삭제 = source 원장에서 철회한 뒤 committed snapshot에서 남은 source를 같은 순서로 재생해 재구성한다. 수정 = 삭제 + 같은 위치에 다시 삽입. slow 통합이 없으므로 fast state 한정이며 통합 후 삭제는 약속하지 않는다고 보고서에 적는다. **완료 판정:** 삭제 뒤 state가 "그 source 없이 처음부터 재생한 state"와 허용오차 안에서 같고, 삭제 전후 해당 질문의 응답 변화(또는 변화 없음의 사유)가 기록되며, 이 단계가 harness의 UJ1 ⑨로 자동 실행된다.
  - **P1-T14 사전 명세와 봉인.** dev pilot의 분산·식별 가능 질의 수로 primary 지표·통계 방법·multiplicity·최소 효과·seed 수·candidate 수 상한·예산 허용오차·보호 지표(재평가·ABA·원능력) 임계와 controller v0의 두 임계값을 manifest에 쓰고, 구현자와 다른 reviewer의 검토를 받은 뒤 hash로 봉인하고, 그 뒤에 sealed cohort를 만든다. 수치는 이 문서에 없고 여기서 처음 정해진다(D-05). **완료 판정:** 봉인 hash 시각이 sealed cohort 생성 기록보다 앞서고, 평가 코드가 manifest hash 불일치 시 실행을 거부한다. 봉인의 선행 조건은 T07·T12의 ceiling/floor 통과와 `fixed`가 floor가 아님의 확인이다.
  - **P1-T15 sealed readout.** 봉인된 manifest대로 모든 arm을 seed × world 단위로 한 번 실행하고 결과 상태(PASS/FAIL/INCONCLUSIVE), 등급 2 문구, 실제 비용(실패·취소 포함)을 기록한다. 같은 sealed cohort를 다른 candidate에 재사용하지 않는다. **완료 판정:** 보고서가 manifest의 모든 지표를 상태와 함께 담고, 사후에 임계·subset을 바꾼 흔적이 없음을 원장이 보인다.
  - **P1-T16 종료.** UJ1을 `full`과 대조 6 arm으로 실제 CLI·가중치·write·저장·재시작 경로에서 끝까지 자동 실행하고, 계약 테스트를 일괄 실행하고, 재현 절차 문서(설치·가중치 확보·실행)를 새 디렉터리에서 그대로 따라 UJ1이 돌게 하고, B07 세 질문과 capability 표 재검토를 기록한다. **완료 판정:** 위 종료 gate 전 항목이 PASS로 기록되거나, FAIL 항목이 §7 분기에 올라가 있다.
  - **범위 절삭 순서:** 일정·계산이 넘치면 T13(삭제)을 P2로 옮기고, 그다음 readout의 seed 수를 줄인다(등급은 2로 유지). 절삭하지 않는 것: 실제 CLI E2E, controller v0의 세 경로, 고정·무구조·항상-갱신 대조, 망각·표면/구조 평가.

### P2 — 여러 구조와 고정 깊이로 넓히고 첫 확증

- **목표**: 같은 제품·같은 CLI에서 구조 family를 3종으로 넓히고 계산 깊이 축(고정 depth 격자)을 더해 경험 전/후의 quality–compute 곡선을 처음 측정하며, P1의 핵심 대조에 대한 첫 한정 확증(등급 3)을 시도한다.
- **근거**: **USER:** B02·B11·B17. **LITERATURE:** review §5 DQ1·DQ5(고정 깊이의 품질–계산 곡선이 먼저)·DQ6, [05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §7(Retrofitted Recurrence [A13], ETD [A14], Relaxed Recursive Transformers [A15]), [08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md) §3 대표 실험. **PROPOSAL:** 아래 전부.
- **데모 시나리오**: **UJ2** (CLI): 구조 family 3종 중 둘의 세계를 번갈아 경험하고(조건 A→B→A 포함) 같은 질문을 `--depth 1/2/4`로 던져 정확도와 계산량을 나란히 본다. 경험 전(S0)·후(SE)의 quality–compute 곡선이 표시된다. `fcl eval`이 모든 arm × depth를 배치로 돌려 한 보고서를 낸다. UJ1 전체를 그대로 다시 돌려도 통과한다.
- **넓이 변화**: 구조 family 1 → 3종(앞 family는 회귀용으로 유지, lure 확대), retrofit layer 확대(전환마다 회귀), depth 축 신설(`--depth`), 배치 평가(`fcl eval`·compare·session transcript), 참고선 Qwen3-8B+raw history(크기가 달라 대조군이 아니라 참고선).
- **깊이 변화**: 첫 확증(봉인 → fresh cohort → 독립 evaluator 프로세스), 조작적 증거 2종(subspace 재사용·변화량 감소), 예외·ABA family 확대와 보호 영역 대조(slow 동결 대 fast만 쓰기), savings·family별 negative transfer, 계산량 정밀화(depth별 FLOPs·p50/p95·TTFT·메모리, write 예산 u 격자), self-evolution v1.
- **주요 작업 묶음**: **A. spike** — recurrence retrofit 가능성(depth별 adapter/LoRA·중간 depth loss). 한 번도 반복 학습하지 않은 모델의 단순 재호출은 후보가 아니다. 실패하면 depth 축을 P3로 이월하고 P2는 나머지로 종료한다. **B. 세계·평가 v2**(구조 family 3종, lure, F05·F06 확대, F07 최소). **C. retrofit 확대**(layer 수 증가, 전환마다 원능력·state·성능 회귀). **D. depth 축**(고정 grid 학습·측정, `--depth`, depth 시계·causal mask·stale cache 검사). **E. 확증 준비·실행**(봉인, fresh cohort, 시도 수·multiplicity 기록). **F. self-evolution v1**(후보 manifest([10-evolution-policy.md](/home/jimmy/repos/full-continual-learning/docs/10-evolution-policy.md) §3) + 독립 evaluator + 후보 archive. 후보 제안·승인은 사람).
- **성립하는 보장**: UJ1 회귀 유지. depth 시계 분리(recursion index가 token position·경험 수를 늘리지 않음), autoregressive mask가 미래 token·depth 상태를 노출하지 않음, 가중치 갱신 뒤 stale cache 정합성 검사([07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md) §3). 계산량 기록이 encoder·core loops·write/backward를 포함한다. 확증 통계는 사전 명세다. 후보가 evaluator·oracle·split을 수정하지 못하도록 권한이 분리된다.
- **상한**: 등급 3 한정(합성 family 3종·소형 모델 1종·사전 명세 seed). depth 곡선과 조작적 증거는 봉인 확증을 거친 것만 3이고 아니면 2다. controller가 규칙형 v0뿐이므로 "적응 계산"을 약속하지 않는다. 동일 입력 재호출이나 무의미한 loop 증가를 개선으로 세지 않는다. 경험 전/후 곡선의 이동은 H-COMPUTE의 일부(경험 효과)일 뿐이며, 통합(Sleep) 이후의 계산 절감은 P4 전까지 주장하지 않는다. Sleep 없음. Qwen3-8B 참고선에는 등급을 매기지 않는다.
- **종료 gate**: (1) **UJ2 E2E:** 실제 CLI·가중치·write·저장·재시작으로 arm × depth를 끝까지 실행(mock 불인정). (2) **앞 phase 회귀:** UJ1 전부(`full`과 대조 6 arm). (3) **자동 테스트:** depth 시계·mask·stale cache·layer 확대 회귀(원능력)·manifest 봉인·권한 분리(후보가 evaluator·oracle·split을 못 바꿈)가 PASS. (4) 등급 3 readout의 결과 상태 기록(PASS가 아니면 §7). (5) B07 세 질문과 capability 표 재검토.
- **미루는 것**: 학습된 controller·halting·fit 결합 write gate·accommodation 메커니즘, Sleep, 외부화, 외부 agent 연결, 두 번째 base model, 자연어 도메인.

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

### P4 — 세션을 넘는 경험 (Sleep·외부화 v0)

- **목표**: 경험이 세션을 넘어 남게 한다. Sleep(fast → slow 공고화)과 외부화 v0(bundle export/import·offload/reload·version lineage), 다세션 이력을 넣고, H-COMPUTE의 핵심 시험인 SE 대 SES(경험 후 대 같은 경험 + Sleep 후) quality–compute 곡선 이동을 처음 본격적으로 측정한다.
- **근거**: **LITERATURE:** review §5 DQ4(SPENS24의 teacher–student replay가 Sleep의 첫 형태, SWAMI23 Discussion의 반복 rebinding 흡수, HWU20의 novelty×familiarity replay 예산), [05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §11, [07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md) §5–§7, [08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md) §3, Sleep [A03]. **USER:** U07·U10. **PROPOSAL.**
- **데모 시나리오**: **UJ4** (CLI): 세션 1에서 경험 → `fcl sleep` → 프로세스 종료 → 세션 2에서 같은 구조의 새 개체를 더 적은 관측·더 얕은 depth로 푼다. bundle을 내보내 다른 디렉터리·새 프로세스에서 불러와도 같은 판단이 나온다. 삭제 요청의 영향은 측정해서 보고한다(보장하지 않음). UJ1–UJ3 회귀.
- **넓이 변화**: 다세션 이력, bundle export/import, version lineage, 모델 revision 변경 시 migration 거부 규칙, replay 후보 선별.
- **깊이 변화**: Sleep v0(fast→slow teacher–student replay, replay 예산 대조), deep-to-shallow distillation, 보존 평가(savings·세션 간 ABA·zero-shot 재평가), 공고화 시점을 event/readiness 대 고정 주기로 대조, Sleep·offload·warmup 비용을 amortized total에 포함.
- **성립하는 보장**: Sleep 전후 state 버전 계보와 재현 가능한 replay recipe, 같은 데이터·총 계산량의 replay-only·teacher distillation과의 비교, offload/reload 뒤 판단·후속 학습의 일관성 측정(F12).
- **상한**: 등급 3. 저장·재구성 성공을 판단 효용으로 해석하지 않는다. tensor shape/hash만 확인한 외부화는 통과로 보지 않는다. 통합된 weights에서 개별 source 삭제가 완전하다고 약속하지 않는다. Sleep을 코드·아키텍처 자체를 고치는 development evolution과 동일시하지 않는다. 자연어·다모델 일반화 주장 없음.
- **종료 gate**: (1) **UJ4 E2E:** 실제 sleep 학습·실제 저장/offload/reload·실제 프로세스 재시작. (2) **앞 phase 회귀:** UJ1–UJ3 전부. (3) **자동 테스트:** bundle manifest·hash·revision mismatch·rollback·migration 거부·세션 간 state 격리. (4) 등급 3 readout: SE 대 SES의 H-SAMPLE과 H-COMPUTE를 따로 판정하고 replay-only·teacher 대조를 포함. (5) B07 세 질문과 capability 표 재검토, P5를 둘로 나눌지 결정.
- **미루는 것**: 대규모 retrieval·multi-user, 외부 agent 연결, 두 번째 base model·자연어 도메인, 운영 자동화.

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

## 6. 회귀 gate 누적표

**PROPOSAL.** 앞 phase의 사용자 시나리오는 뒤 phase의 종료 gate에서 가장 최신 코드로 다시 돌려 통과해야 한다. 앞 phase의 PASS 기록을 재사용해 회귀를 대신하지 않는다. 회귀 실패는 새 기능 개발보다 먼저 고친다. 앞 시나리오의 등급은 새 phase의 결과로 저절로 오르지 않으며 다시 측정해야 한다.

| phase 종료 | 회귀로 다시 통과할 앞 시나리오 | 새 시나리오 | 새로 추가되는 자동 테스트(Contract) | 효용 판정 기록 |
|---|---|---|---|---|
| P1 | 없음(첫 phase) | UJ1 전체 여정 | 시계 분리·재전송 idempotency·원자적 commit·재시작 동등·revision mismatch 거부·삭제 동등·누수 audit·budget 일치·함수 보존·manifest 봉인·controller v0 결정의 관측 state 근거 | 등급 2 readout 상태 |
| P2 | UJ1 | UJ2 여러 구조·고정 깊이 | depth 시계·causal mask·stale cache·layer 확대 회귀(원능력)·후보와 evaluator의 권한 분리 | 등급 3 readout 상태 |
| P3 | UJ1, UJ2 | UJ3 스스로 고르는 모델 | router 인과성·controller 결정이 관측 state에 근거함·bundle에 제어 상태 포함·보호 family 자동 중단 | 등급 3 readout 상태(controller 대 고정 depth 등) |
| P4 | UJ1, UJ2, UJ3 | UJ4 세션을 넘는 경험 | bundle manifest·hash·migration 거부·세션 간 state 격리·replay 재현 | 등급 3 readout 상태(SE 대 SES) |
| P5 | UJ1, UJ2, UJ3, UJ4 | UJ5 실제 consumer 연결 | 모델·tokenizer 계약·multi-user 격리·삭제 의존성·session 프로토콜 호환 | 등급 4 readout 상태 + 운용 coverage |

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

## 8. 지속적으로 유지할 자산

**PROPOSAL (옛 §5 유지·확장).** 옛 목록을 유지한다: 실패 사례와 negative controls, data generators, source·recipe lineage, state compatibility tests, regression suite, 실제 비용 원장, reference catalog, specification·decision log. 테스트 수·문서량·커밋량을 연구 진전의 대표 지표로 쓰지 않는다.

새로 추가한 것은 다음과 같다.
- arm 정의표와 arm manifest(설정 hash)
- 봉인 manifest와 evaluator 버전, sealed cohort 사용 기록(어떤 candidate에 썼는가)
- phase별 데모 시나리오 스크립트(UJ1…UJ5)와 실행 기록, 회귀 결과
- 세계 생성기와 split(train/dev/sealed), renderer 두 종류
- 결과 보고 생성기와 문구 검사기
- 이 문서의 capability × phase 표와 변경 기록

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

## 10. 계산 자원과 결정 대기

**PROPOSAL.** 비용이 드는 선택(클라우드 GPU, 유료 API, 큰 모델 다운로드, 장시간 GPU 점유)은 결정 대기로 두고 사용자 결정 전에는 실행하지 않는다. 아래 시간·성능 추정은 쓰지 않았고, 실측은 P1-T04에서 한다. 아래 D-번호는 모두 **OPEN**이다.

| 자원 | 확인된 사실 | P1에 대한 판단 |
|---|---|---|
| host | CPU 16코어, RAM 27GB. 메모리 압박이 잦다(이 초안 작성 중 관측: swap 약 10GB 사용) | 무거운 실행은 직렬로 한다. runtime을 CLI와 별도 프로세스로 둬서 runtime만 재기동한다. 135M급 모델의 CPU 실행 이력은 있으나 CPU 학습 시간은 미측정(T04에서 실측) |
| 노트북 GPU | RTX 5070 Ti 12GB, SSH 접근. **ARCHIVE:** Melete 2026-10-11 기록에서 12227MiB·Torch 2.9.1+cu128·sm_120을 확인했고 이번 초안에서는 재접속·재확인하지 않았다([2026-10-11-learning-roadmap-feedback.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/implementation/records/2026-10-11-learning-roadmap-feedback.md)) | retrofit 학습(outer loop)의 기본 후보. 장시간 점유는 결정 대기(D-04) |
| 로컬 llama.cpp의 Qwen3-8B (GGUF) | 추론 전용 양자화 형식 | retrofit 학습 대상으로 부적합하다. GGUF는 autograd 학습과 layer 개조에 쓰기 어렵고, 원본 8B bf16 가중치는 약 16GB라 12GB VRAM에 학습으로 맞지 않는다. 용도는 참고선(`ctx` + raw history, P2 이후)과 세계 난이도 검사다 |
| 로컬 llama.cpp의 Qwen3-Embedding-0.6B (GGUF) | 생성 모델이 아닌 embedding 모델 | retrofit 대상이 아니다. 용도는 2×2 설계의 표면 유사도(표면 거리)를 재는 보조 도구다 |
| SmolLM2-135M(-Instruct) | 134,515,008 parameters. **ARCHIVE:** Melete E5에서 host CPU로 실행([2026-10-07-e5-self-feedback.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/implementation/records/2026-10-07-e5-self-feedback.md)). Llama 계열 구조로 알려져 있으나 모델 카드·config 확인 필요 | P1 골격 후보 1순위(D-01). 가중치 확보는 사용자 승인 뒤. 세계가 floor에 걸리면 360M 등 상위 크기를 검토한다 |
| 외부 공식 코드 | Titan-Llama pin `sarahpannn/titans-pytorch@c60b4efaa3a3c6df4deebd57cbccf75947b87cad`. 라이선스 기록이 이 저장소에 없다([catalog.tsv](/home/jimmy/repos/full-continual-learning/references/catalog.tsv) A04). review §4.5의 원칙은 라이선스 없는 코드를 읽고 인용만 하고 논문 식에서 재구현하는 것이다 | D-02. 결정 전에는 읽기·인용과 재구현 경로로만 진행한다 |

| ID | 결정 | 선택지 | 추천 | 비용 발생 | 결정자 |
|---|---|---|---|---|---|
| D-01 | P1 base model | (a) SmolLM2-135M (b) SmolLM2-360M (c) Qwen3-0.6B (d) 1B급 | (a)로 골격·개발. T07·T12의 floor 검사에서 막히면 (b) | 가중치 다운로드(작음), 크기가 커지면 학습 시간 증가 | 사용자(크기 상향·다운로드 승인) |
| D-02 | Titan-Llama 코드 사용 방식 | (a) 라이선스 확인·허가 뒤 코드 사용 (b) 논문 식에서 재구현, 코드는 읽기·인용만 (c) 비공식 구현(lucidrains/titans-pytorch) 참고 | (b). 라이선스가 명시적으로 허용하면 (a) 재검토 | 재구현 공수(금전 비용 없음) | 사용자 |
| D-03 | P1 구조 family | (a) 역할–결과 규칙 세계 (b) 순서 추론 (c) 쌍 연합·cue→goal (d) 자연어 소규모 관계 그래프 | (a) 단독. (b)는 P2 family 후보 | 없음 | 사용자(방향), 설계 담당(세부) |
| D-04 | retrofit 학습의 계산 장소·시간 상한 | (a) host CPU만 (b) 노트북 GPU (c) 클라우드 GPU | T04 실측 뒤 (b)의 시간 상한을 먼저 승인. (c)는 P5 전까지 보류 | (b) GPU 장시간 점유, (c) 금전 | 사용자 |
| D-05 | readout 통계 계획 | seed·world 수·candidate 수 상한: pilot 분산 기반 최소 n(구간 폭 계획) 또는 고정 소수 | 분산 기반, 상한만 먼저 승인(Melete J1은 candidate 3개 상한을 썼다, ARCHIVE) | 계산 시간 | 사용자(상한), P1-T14(수치) |
| D-06 | P1에 source 삭제 포함 | (a) fast 한정 얇게 포함 (b) P2로 이월 | (a). 저장·원장 뼈대를 P1에서 검증한다 | 작음(재생 공수) | 사용자 |
| D-07 | P1에서 sealed readout 실행 | (a) P1 종료 gate에 포함 (b) dev pilot까지만 하고 확증은 P2 | (a). 효용 gate를 집행하려면 필요하다 | seed × arm 실행 시간 | 사용자 |
| D-08 | 참고선 Qwen3-8B+raw history 도입 시점 | P1 / P2 / 미도입 | P2 | 로컬 추론 시간 | 설계 담당 제안, 사용자 확인 |
| D-09 | 세계 렌더링 언어 | 영어(SmolLM2) / 한국어(Qwen3 계열) | P1은 영어 합성 세계, 한국어·자연어는 P5 | 없음 | 사용자 |
| D-10 | self-evolution 자동화 범위·예산 | 수동 유지 / P3부터 승인된 예산·search space 안에서 자동 | P1–P2는 수동·v1, P3 자동은 별도 승인([10-evolution-policy.md](/home/jimmy/repos/full-continual-learning/docs/10-evolution-policy.md) §6) | 자동 학습·GPU | 사용자 |
| D-11 | 외부 agent 연결 대상·방식·시점 | codex / prime agent, tool(MCP) 대 endpoint | P4 종료 재검토에서 결정. 진입 조건은 §7 | 연결 공수 | 사용자 |
| D-12 | 두 번째 base model·크기 | 다른 크기 / 다른 계열 | P4 종료 재검토에서 결정 | 다운로드·학습(클라우드 가능성) | 사용자 |
| D-13 | 위상(phase) 조율(D) 실험의 배치 | P3 말미 / P4 / 미도입 | P3 종료 재검토에서 C(event/readiness)를 기준선으로 삼아 결정 | 계산 시간 | 사용자 |
| D-14 | schema 판단 구조(controller)의 최소형을 P1에 넣을지 | (a) P3에 두고 P1은 write 정책 접점만 (b) P1에 규칙형 controller v0(경로 선택만) (c) P1에 학습된 문맥 head | **(b)로 반영(2026-11-12 마스터 설계 판단, 사용자 확인 대기).** U-T07 원문은 핵심 거동을 "익숙하면 매우 빠르게, 덜 익숙하면 rapid learning, 더 낯설면 더 깊은 loop"로 정의하고 "이 과정에서 입력 문맥에 대한 schema판단 mlp나 구조를 넣어서"라고 했다. 점진적 해상도 규칙은 P1이 핵심 여정 전체를 얇게 관통하라고 요구한다. 초안의 추천 (a)는 원인 혼동을 우려했으나 `noctl` 대조 arm으로 경로 선택의 기여를 분리한다. (c)는 P3 | P1 공수 증가(controller v0·r=2 적응 학습·`noctl` arm) | 사용자 확인 |

비용이 드는 선택은 D-01(크기 상향)·D-04·D-10·D-12이고, D-13은 계산 시간이 들고, D-14 반영으로 P1 공수가 늘었다(controller v0·r=2 적응 학습·`noctl` arm).

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

| 날짜 | 변경 | 이유 | 영향 |
|---|---|---|---|
| 2026-11-12 | 점진적 해상도 규칙에 맞춰 로드맵 전면 재구성(초안, PROPOSAL) | 옛 P0–P6가 B17과 어긋남(문서 맨 앞 상자) | 전 절. 옛 §2·§4·§5·§6은 갱신해 유지 |
| 2026-11-12 | 검수 반영: 규칙형 controller v0와 deep 경로(r=2)를 P1에 넣고 `noctl` 대조를 추가(D-14), H4 text interface 서술을 OPEN으로 낮춤, B 번호 기간 정정 | U-T07 원문과 점진적 해상도(핵심 여정 전체를 P1에서), 설계 감사의 H4 판정(정리자 추론) | §1.1·§1.2·§1.4·§2·§4·§5 P1–P3·§6·§9·§10 |
