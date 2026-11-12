# 10. Self-evolution와 운영 정책

## 1. 세 루프와 권한

| 루프 | 변경 대상 | 성공의 의미 |
|---|---|---|
| Experience learning | fast memory, binding, 잠정 schema state | 이후 관측/판단의 적절한 적응 |
| Sleep/consolidation | slow weights, schema 구조, replay policy | 유지와 새 사례 전이, 계산 효율 |
| Development evolution | 코드·구조·목적함수 후보·controller recipe | 독립 평가에서 더 나은 quality–cost |

개발 절차 자체의 진화는 더 바깥쪽 루프다. 초기에는 작고 고정된 실험 관리 체계를 쓰고, 그것의 추가 가치를 먼저 검증한다. Sleep 논문의 self-modification을 repository 자율 코드 변경과 동일시하지 않는다.

**USER (U-T02, U-T06):** 가장 간단하게 시작하고 그 방식이 점점 고도화·복잡화·개선되는 방향의 evolutionary 구축, 그리고 phase별 MVP와 self-evolving 작업방식을 유지한다. **PROPOSAL:** 개발 진화 루프의 권한을 아래 사다리로 올린다. 한 단계의 종료 gate가 통과된 뒤에만 다음 단계 권한을 연다. 앞 단계의 시나리오와 실패 기록은 다음 단계의 회귀 gate로 남는다.

| 단계 | 권한 | 후보 생성 | 승격 결정 | 다음 단계를 여는 조건 |
|---|---|---|---|---|
| E0 수동 | 실험 원장·비용 로그·고정 evaluator만 자동화한다 | 사람 | 사람 | evaluator 독립성 점검(§5)과 원장 재현 확인 |
| E1 AI 제안 | AI가 §3 계약 형식으로 후보를 제안만 한다 | AI 제안, 사람이 선택 | 사람 | 같은 search budget의 random search·parameter sweep(§7)보다 나은 Pareto 후보가 한 번 이상 기록됨 |
| E2 샌드박스 구현 | AI가 허용 파일·변수 범위 안에서 구현하고 dev 평가까지 실행한다 | AI | 사람 | 보호 family 퇴행 없이 fresh confirmation을 통과하고 §6 중단 조건이 발동하지 않음 |
| E3 예산 내 자동 | 승인된 범위·예산 안에서 후보 생성·격리 학습·dev 평가·기록을 자동 수행한다(§6) | AI | 사람(운영 승격), evaluator 변경은 새 version으로 분리(§5) | 이 단계가 최종이다. 목적 변경·private data·외부 서비스·운영 승격은 계속 별도 권한이다 |

**OPEN:** 각 단계를 어느 시점에 여는지는 새 로드맵의 phase와 연결해 정한다. 이 사다리는 승인된 일정이나 수치가 아니다.

## 2. 목표 계약

최상위 목적: 제한된 경험과 계산으로 조건부 구조를 형성·활용·수정하고 기존 유효 지식을 보존한다. 특정 graph/all-hidden-state/decoder를 목적에 섞지 않는다. 특정 메커니즘의 과학적 가치를 연구하는 제한 탐색은 별도의 가설과 대조군을 둔다.

Objectives, 수치 verification/benchmark, negative feedback, operation policy라는 사용자 요구에 **search space**를 명시적으로 추가한다. 무엇을 바꿀 수 있는지 없으면 자동화는 평가를 우회하거나 너무 많은 변수를 동시에 바꾸기 쉽다.

**USER (B14, 2026-10-12):** 핵심 가설은 틀렸다고 확인되기 전까지 반드시 유지하는 basis다.

**PROPOSAL:** 현재 FCL에서 같은 지위의 basis는 사용자가 명시한 통합 System ONE 구조(U-T07), H-SAMPLE, H-COMPUTE다. 이들은 반증이 확인되기 전까지 유지한다. 적합한 구현·대조군·학습 예산·데이터를 갖춘 실험 전에는 편의상 다른 메커니즘으로 대체하거나 정의를 바꿔 통과시키지 않는다. 반증을 주장하려면 다음을 기록하고 사용자 검토에 올린다. (1) 어떤 구성과 조건의 어떤 관측이 가설을 위반했는가. (2) 대조군·예산·표본. (3) 가설의 어느 범위를 기각하는가. 한 구성의 FAIL을 이론 전체의 반증으로 확대하지 않는다.

**ARCHIVE:** 같은 절차가 Melete의 H1–H5에 적용됐고 [12-melete-lineage.md](/home/jimmy/repos/full-continual-learning/docs/12-melete-lineage.md)에 과거 규칙으로 남아 있다 ([neural-basis.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/design/neural-basis.md)). 이전 H1–H5 중 통합 모델로 대체된 것으로 사용자 진술이 확인된 부분은 역할 분할(U-T07)뿐이며, 나머지(예: H4의 text interface)는 사용자 확인 전까지 basis 후보로 유지한다.

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

**PROPOSAL (원문 검토 §4.1·§5 출발점 8):** 문헌에서 온 기제를 후보로 만들 때는 hypothesis/evidence 필드에 논문 id·확인 깊이(fulltext-read 등)·근거 위치를 적고, 같은 계산·갱신 예산의 고정/무구조/항상-갱신 대조를 비교군에 함께 넣는다. 대조 없이 통과한 후보는 "기제의 독자 기여 미분리"로 표기해 효용과 기제 기여를 분리 보고한다([09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md) §4와 같은 원칙).

**LITERATURE (11편 전체, [2026-11-11-sbl-fulltext-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext-review.md#4-논문을-가로지르는-관찰) §4.1):** 읽은 11편 어디에도 학습된 구조가 같은 예산의 고정·무구조 대조보다 낫다는 직접 비교가 없다. **PROPOSAL:** 따라서 문헌의 성공을 후보의 expected_mechanism 근거로 곧바로 옮기지 않는다.

## 4. Negative feedback의 내용

점수 하락 외에 어느 조건의 failure인지, 관측 근거, 원인 가설, 변경 대상, 기대되는 개선, 유지할 능력을 기록한다. AI의 원인 설명은 검증된 원인이 아니라 가설이다.

예: 정정 후 새 조건은 좋아졌지만 A조건 복귀가 나빠졌다 → shared state overwrite 가설 → update 범위만 제한 → reader/router는 고정 → correction과 ABA를 함께 평가.

내부 surprise는 기존 이해와 맞지 않는다는 신호일 뿐 어느 쪽이 틀렸는지의 정답이 아니다. 외부 관측·사용자 선호·독립 benchmark와 자기 생성 해석을 분리한다.

## 5. Evaluator의 독립성

후보는 private answer, held-out split, 채점 규칙, 비용/상태 로그를 수정할 수 없다. 단순 프롬프트 금지로 끝내지 않고 실행 권한을 분리한다. 평가에 쓰이는 관측 자체도 후보의 자기 보고에만 맡기지 않는다. 예를 들어 hallucination marker를 지워 점수를 높이는 행위는 개선이 아니다. DGM 계열에서 논의된 문제를 경계 사례로 기록한다. [E02]

**LITERATURE (KUMAR26, W4-tem20-kumar26.md:297,390):** 평가 지표에 맞춘 튜닝은 읽은 논문에도 있다. KUMAR26은 학습률·τ_c·β^control·Ω_ACh를 평가 지표(초기 MPA latency와 OPA·6NPA 방문 비율)로 튜닝했고 튜닝 seed 수가 원문에 없다. **LITERATURE (GOUDAR23·CHU25, W2-chu25-goudar23.md:99-104,299-304):** GOUDAR23의 문제 경계·Adam 리셋·안정화 정규화와 CHU25의 단계 경계는 실험 틀이 공급한다.

**PROPOSAL:** 후보의 학습·튜닝에 쓰는 split과 selection·confirmation 평가 split을 분리하고, 단계·문제 경계가 harness에서 오면 결과에 그 사실을 적는다([08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md) §7).

AI가 평가 개선을 제안할 수는 있다. 채택 시 새로운 evaluator version으로 분리하고 기존 후보들을 다시 비교한다. 과거 FAIL을 소급 PASS로 바꾸지 않는다.

## 6. Budget와 자동화

사용자가 승인한 범위·예산 안의 candidate 생성, 격리 학습, dev 평가, 기록은 자동화 가능하다. 목적 변경, private data 사용, 외부 서비스, 운영 승격, 새로운 과금/장시간 compute는 별도 권한이 필요하다.

본 repository 게시 작업은 지속적인 자동 개발·GPU 학습·자동 push의 포괄 권한을 부여하지 않는다. 향후 작업에서 scope를 확인한다.

실제 consumed compute, 실패 job, 취소·재시도도 합계에 포함한다. 예정 상한을 실행 비용으로 보고하지 않는다. 중단 조건: budget 소진, 반복된 동일 failure, 평가 결함, 비재현, privilege violation, 보호 family 퇴행.

### 6-1. 외부 문헌 추적 운영 (U-T05, U-T10)

**USER (U-T05, U-T10):** SBL을 AI 모델의 근간 이론으로 제시하는 논문을 별도 세션에서 매주 추적해 보고한다. 보고는 symbolic과 latent(continuous)를 구분하고 latent를 우선한다. 범위·분류·필드·보고 순서는 [TRACKING_POLICY.md](/home/jimmy/repos/full-continual-learning/research/TRACKING_POLICY.md)가 정한다.

**PROPOSAL:** 추적과 설계 문서의 연결 규칙.

- 추적 보고는 설계를 자동으로 바꾸지 않는다. 보고자가 설계 영향이 있다고 판단한 항목만 HANDOFF 항목(대상 문서·절, 근거, 확인 깊이)으로 올리고, 편집 초안은 사용자 검토 뒤 해당 문서(03·05·06·08·10·11)에 반영한다.
- 보고마다 [catalog.tsv](/home/jimmy/repos/full-continual-learning/references/catalog.tsv)의 확인 깊이를 갱신한다. metadata·초록 수준 항목은 설계 근거가 아니라 후보로만 쓴다([EVIDENCE.md](/home/jimmy/repos/full-continual-learning/EVIDENCE.md)의 확인 깊이 정의).
- 다음 보고의 첫 항목은 직전 보고의 미해결 추적 항목이다. 현재는 [2026-11-09-sbl-tracking.md](/home/jimmy/repos/full-continual-learning/research/2026-11-09-sbl-tracking.md) §10의 P0–P2와 [2026-11-11-sbl-fulltext-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext-review.md) §7의 미정독 후보다.
- 변화가 없으면 없다고 보고하고 관련 없는 memory 논문으로 채우지 않는다(TRACKING_POLICY.md).

**OPEN:** 이 저장소 게시는 자동화의 생성·수정·실행과 외부 메일 발송을 의미하지 않는다. 추적을 정기 실행으로 재개할지, 실행 주체와 주기는 사용자가 정한다.

## 7. 최소 진화 루프

후보 제안 → schema/contract 검사 → sandbox 구현 → dev 학습/평가 → failure analysis → 후보 archive → 제한 selection → fresh confirmation → 품질/비용/유지 gate → 운영 승격 또는 보류.

**PROPOSAL ([2026-11-11-sbl-fulltext-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext-review.md#4-논문을-가로지르는-관찰) §4.5):** sandbox 구현에서 라이선스 없는 외부 공식 코드는 읽고 인용만 하고, 필요한 기제는 논문 식에서 다시 구현한다. 읽은 구현·모형 9편 중 공식 코드가 있는 것은 7편이고 그중 LICENSE가 있는 것은 GOUDAR23(MIT) 하나이며 CHU25·SWAMI23은 공식 코드가 없다. 기제가 소형(수백 유닛, CPU 가능)이라 재구현 비용은 작다.

**LITERATURE (HWU20·MICONI25·TEM20·KUMAR26·GOUDAR23, 원문 검토 §4.5; W1-spens24-hwu20.md:367,369,371, W3-elder26-miconi25.md:344-345, W4-tem20-kumar26.md:206,437-438, W2-chu25-goudar23.md:423):** 코드와 논문이 어긋난 사례가 많다. HWU20은 Table 1의 N_multimodal 40이 코드·그림의 80과, e_boost 1000이 코드의 2000과 다르고 mPFC→vHPC 가중치가 코드에서는 학습되지 않으며(W1-spens24-hwu20.md:371), MICONI25는 식 4·5가 코드와 다르며, TEM20은 lr 1e-3→1e-4가 코드의 9.4e-4→8e-5와 다르다. KUMAR26은 reservoir N=1024가 코드 기본값 1000과, τ_e 1000 ms가 코드 기본값 xytau=200과 다르고, GOUDAR23의 배포 처리 데이터(10망)는 논문 통계(30망)를 재현하지 않는다.

**PROPOSAL (W1-spens24-hwu20.md:358):** 재구현 전에 어느 판의 실험을 재현할지 정하고 불일치 목록을 만든다.

같은 search budget의 parameter sweep, random search, 한 번의 AI 수정과 비교한다. evolution을 붙여 점수가 올랐다는 것만으로 더 복잡한 개발 체계의 필요성이 입증되지는 않는다.

**USER (B07, 2026-10-07):** 매 단계 self feedback을 한다. 의도된 방향인지, 의도대로 구현됐는지, 단계 기준을 충족하는지 묻는다. pass면 다음 단계로, fail이면 개선한다. 권한이나 필수 인프라 문제로 막히면 멈추고 보고한다.

**PROPOSAL:** phase와 후보 평가가 끝날 때마다 세 질문을 기록한다. (1) 의도 방향: 사용자 요구(U01–U12와 H 목록)에 정렬돼 있는가. (2) 구현 일치: 설계 문서와 계약대로 구현·실행됐는가. (3) 기준 충족: 사전 정의한 종료 gate와 [08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md) §8의 결과 상태에 비춘 판정이 PASS인가. PASS면 다음 단계로 가고 FAIL이면 원인을 분리해 개선한다. 같은 실패의 반복과 평가 결함은 중단 조건이다. BLOCKED(권한·인프라·runtime)이면 멈추고 막힌 이유, 필요한 구체 조건, 보존한 실험 질문을 사용자에게 보고하며 대체 경로로 우회하지 않는다.

**USER (B06, 2026-10-06):** 설계의 타당성·완결성·실현가능성을 최종 검수한다.

**PROPOSAL:** 설계 문서 묶음의 검수는 세 축으로 기록한다. 타당성(근거 라벨과 문헌 범위), 완결성(사용자 요구 원장의 REFLECTED/PARTIAL/MISSING), 실현가능성(소형 모델 규모, 필요한 계산·저장 예산, 실제 의존성 가용성). 통과하지 못한 항목은 완료로 표기하지 않는다.

## 8. 근거와 적용 범위

AlphaEvolve [E01]: seed program과 evaluator를 이용한 코드 탐색.
DGM [E02]: foundation model이 고정돼도 주변 code/tools/workflow 진화 가능성.
GEPA [E03]: 실행 trajectory와 자연어 failure feedback을 이용한 prompt 탐색.
HyperAgents [E04]: task/meta agent 개선 연구.

이들의 성공을 Melete의 neural schema 형성이나 통합 System ONE 성공의 직접 증거로 사용하지 않는다.

**PROPOSAL ([EVIDENCE.md](/home/jimmy/repos/full-continual-learning/EVIDENCE.md) 확인 깊이의 의미, 원문 검토 §2·§6):** 문헌 주장에는 확인 깊이(fulltext-read, metadata-checked, official-search-checked, discussion-import)를 함께 적고 초록·검색 결과 수준의 판정을 원문 정독 수준으로 올려 쓰지 않는다. 외부 요약은 원문으로 검증하기 전에 설계 근거로 쓰지 않는다. 부재·갭 결론은 검색 범위와 근거 깊이를 함께 적는다.

**LITERATURE (STRUCTK25 외 6편, 원문 검토 §2, W7-remediation.md:222):** 2026-11-11에 외부 요약을 원문 11편과 대조하자 정정 여섯 건이 나왔다. 리뷰 STRUCTK25에는 참고문헌·인용 오류 세 건이 있어 이 리뷰를 통한 2차 인용은 원논문을 보기 전에 단정하지 않는다.

### 8-1. 사용자 요청 산출물 정책

**USER (B13, B15, B20):** 사용자는 다음 산출물을 요청했다. 구현 방식의 상세 기술 가이드(B13, 2026-10-11), 평가와 ELI·diagram webapp(B13), Melete 신경망 논문을 Google식 논지로 veridraft로 쓰고 필요하면 veridraft를 개선하는 것(B15, 2026-10-12), 피드백(논문 포함)이 설계에 반영됐는지 확인하고 시각화 백서로 총망라하는 것(B20, 2026-11-12). B16(2026-10-13)에서는 superpowers 사용도 지시했다.

**PROPOSAL:** 산출물 정책으로 다음을 둔다.
- 구현 착수 시 상세 기술 가이드를 코드 pin·실행 순서·상태 계약과 함께 작성한다.
- 설명 산출물은 ELI와 diagram을 갖춘 형태로 만들고 증거 라벨(USER/PROPOSAL/LITERATURE/ARCHIVE/OPEN)을 유지한다.
- 논문은 달성한 gate의 범위만 주장하며 미입증 효용을 결과처럼 쓰지 않는다.
- 사용자 요구의 반영 확인은 요구 원장(요구 → 설계 위치 → 상태)으로 기록하고 시각화 백서가 이를 요약한다.

**OPEN:** 이 감사 시점(2026-11-12)에 이 저장소에는 기술 가이드, webapp, 논문이 없다. 시각화 백서는 같은 날 이 감사 결과를 입력으로 만들었다([README.md](/home/jimmy/repos/full-continual-learning/whitepaper/README.md), 웹 https://fcl-system-one-whitepaper.vercel.app). B15의 논문이 Melete 신경망 논문인지 FCL 논문인지, B16의 superpowers 사용 지시를 FCL 작업에도 적용하는지는 사용자 확인이 필요하다.
