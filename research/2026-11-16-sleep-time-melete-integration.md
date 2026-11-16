# 2026-11-16 Sleep-time Compute 보고 → Melete/System ONE 직접 관련 연구 연결

## 출처·증거 수준

**ARCHIVE / discussion-import:** 2026-11-16 완료된 별도 자동화 「Sleep-time Compute 주간 동향」의 자료 가운데 Melete schema CRUD, low-rank expert, continual learning 평가에 직접 관계가 있는 **8건만 선별하여 재구성**한다. 원 자동화 ID는 6a800173dcdc819198767ca618472810, 완료 run ID는 f4042a8b-df7c-832f-a3c8-95b2e35acfde이다. 기존 주간 보고의 조사 기간은 11월 9~15일이었다. 해당 보고 전체를 이관하거나 모든 대화 원문을 확보한 것은 아니다.

**LITERATURE / abstract-verified:** 아래 8건은 이 동기화 실행에서 공식 arXiv의 초록·최초 제출/개정일·첫 저자·링크를 독립 확인했다. **원문 전체·부록을 정독하거나 코드를 실행하지 않았다.** 수치는 원 저자 보고이며 재현된 값이 아니다. 여기서 학회 채택을 추정하지 않는다.

**PROPOSAL / OPEN:** 설계·검증 연결은 검증할 가설이지 승인된 구현 결정이 아니다. **NOT RUN:** FCL 모델/GPU/serving·HBF 실험은 0회다. 외부 Agent memory와 파일 관리의 persistent state를 **continuous latent neural schema** 또는 세션 간 parametric continual learning과 동일시하지 않는다.

## 1. 선별 연구: 공식 메타데이터와 보고 결과

| 연구 및 공개일 | 검증 가능한 중심 결과 (저자 초록) | Melete에 적용할 연구 질문 |
|---|---|---|
| [MAPE — Discovering Effective Agent Memory Designs through Program Evolution](https://arxiv.org/abs/2611.17068), Xinheng Ding, **11/12 v1** | Agent memory 수명주기 프로그램의 자동 진화. LoCoMo·LongMemEval에서 수작업 기준 대비 최대 12%p 향상, 그 비교에서 serving cost 35%. Query 시 선택적인 증거 조합의 효과도 분석 | **CRUD 최적화:** offline consolidation 비용과 query-time 계산을 함께 최적화 |
| [MIRIX-2.0: Multi-Agent Memory System](https://arxiv.org/abs/2611.12068), Wei-Chieh Huang, **11/09 v1** | 6종 typed memory agent, 원본 증거를 유지하는 provenance hypergraph, offline AutoDream; LoCoMo 91.4%, LongMemEval-S 72.6%. Fine-tuning 불필요 | **Delete/Retain:** 원본 기록·파생 인덱스·skill과 그 계보 구분. 신경망 schema 학습 증거는 아님 |
| [Coding Agent Memory Post-Training II (CAMP-II)](https://arxiv.org/abs/2611.14009), Lirui Luo, **11/10 v1, 11/12 v2** | 파일 기반 memory create/revise/search/reuse 행동을 비동기 on-policy distillation으로 학습. CAMG-II에서 가장 강한 OPD 기준선 대비 개선폭 2.97배 | **Read/Write policy:** 기억 관리 행동을 학습 가능하게 만들되 파일 기억과 low-rank write를 구분 |
| [Continual-ARC: Measuring Skill Acquisition over a Working Lifetime](https://arxiv.org/abs/2611.14505), Daniel Lenton, **11/10 v1, 11/11 v2** | 과거에 접한 과제의 새 instance와 미경험 과제를 분리하고 memory harness와 weight learning 비교. 검토된 harness 기법은 unseen tasks 일반화 개선이 없고 weight learning은 개선 관찰 | **Evaluation:** 이전 경험 검색과 새 기술 획득을 동일 경험·피드백 예산에서 판정 |
| [MemCredit: From Relevance to Utility](https://arxiv.org/abs/2611.15600), Quanjiang Guo, **11/11 v1** | Counterfactual memory utility로 선택. ALFWorld 500-token budget에서 SR@50 86.57%, BM25 65.67% 보고 | **Read / Delete:** 의미 유사성보다 행동 효용을 함께 평가하고 미래 분포에서의 추정 오류 검사 |
| [A Margin Perspective on LoRA (MaLoRA)](https://arxiv.org/abs/2611.14397), Ziqing Xu, **11/10 v1** | 거의 직교한 task와 정규화가 있는 **선형 다중분류**에서 margin 기반 retention/merging 분석; vision/language classification 실험 | **Update/Merge:** schema expert 간 간섭·병합의 제한적 이론 비교. 범용 LLM 무망각 증명 아님 |
| [Maximizing Capacity Utilization of LoRA Adapters](https://arxiv.org/abs/2611.17191), Tomohiro Sawada, **11/12 v1** | Configured rank보다 실제 effective rank가 낮은 현상과 Rényi-2 regularizer 제시; mixed-domain learning–forgetting 비교 | **Update/Create:** expert의 유효 rank와 저장·학습 예산을 비교. rank 사용률이 곧 schema 형성은 아님 |
| [Evolving Infra: Agent-Adaptive LLM Serving at Scale](https://arxiv.org/abs/2611.12304), Hao Kang, **11/09 v1, 11/12 v2** | Agent context에 따른 P/D 자원과 분산 KV cache 관리. 256개까지의 GB300 실험에서 Dynamo 대비 평균 latency 최대 4.1배, P95 TTFT 최대 14배 개선 주장 | **Read 비용의 인접 연구:** expert cold-load/prefetch·logical lifetime과 물리 메모리 배치의 분리. HBF·schema serving 직접 검증 아님 |

모든 결과의 benchmark·비교군·조건이 달라 수치를 서로 직접 비교하지 않는다. 이 연구들은 대부분 neural SBL을 표방하지 않으므로 SBL 신규 논문으로 재분류하지 않는다. [서지·표현 및 읽기 범위](../references/2026-11-16-sleep-time-melete.md) 참조.

## 2. 현행 Schema CRUD 연구에 대한 새 가설 (PROPOSAL)

**Update/Create:** schema-conditioned low-rank expert의 in-place 변경과 새 expert 분화를 구별하는 기존 방향을 유지한다. Fixed-rank의 실효 자유도, 간섭 측정, adapter 병합의 이론적 조건을 독립 검사한다. 같은 expert 내부의 파괴적 간섭과 router/shared encoder의 변경도 점검한다.

**Delete/Retain:** offload는 논리적 삭제가 아니라 위치와 접근 지연의 변경이다. 원본 경험·파생 memory·schema artifact·버전 snapshot을 구분하고, 통합 또는 폐기가 실제 기능·미래 재학습에 미치는 손실을 평가한다. External memory AutoDream은 neural consolidation의 결과가 아니다.

**Read/Activate:** 1차 후보 검색의 semantic similarity와 실제 실행의 conditional utility를 분리한다. 답변에 쓰는 Read와 새로운 경험을 업데이트하기 위해 참조하는 Read를 별도 지표로 측정한다. 잘못된 기억의 빈번한 선택이 그 기억의 retention 점수를 스스로 높이지 않도록 설계한다.

**Sleep 및 총비용:** offline에 계산을 더 투입하는 것이 항상 최적인 것은 아닐 수 있다. Online update·Sleep·index·retrieval·cold-load·서빙의 전체 비용을 동일 정확도 조건으로 비교한다. Evolving Infra는 memory hierarchy 비교에 참고하되 System ONE 구현의 직접 선행으로 간주하지 않는다.

## 3. 우선 검증할 실험 (NOT RUN)

1. **지속학습의 실체:** 동일 경험·feedback/compute budget으로 raw history/RAG/file memory, 일반 LoRA, schema low-rank expert를 비교. A→B→A와 전에 보지 못한 관계 및 같은 관계의 새 instance를 구별한다.
2. **Read의 기여:** 같은 expert pool에서 relevance-only gate, utility-aware gate, oracle gate, stale index 비교. 표면 유사/구조 반대 조건을 포함한다. 선택 오류와 파라미터 기억의 손상을 분리한다.
3. **Update/merge:** 같은 rank·bytes·update budget에서 random partition, schema-conditioned update, effective-rank regularization, margin-guided merge를 비교하고 기존 유효 기능의 회귀를 확인한다.
4. **Delete의 비용:** offload-only, 압축, 통합, 실제 폐기를 별개 군으로 비교. Cold/warm p95, 활성/외부 저장량, 학습·Sleep 비용, 이전 schema 복귀 능력과 기능 손실을 함께 보고한다.

이 기록은 [CRUD·Ali 공동논문 연구안](../docs/14-schema-lifecycle-crud-and-joint-paper.md), [SBL 전용 주간 보고](2026-11-16-sbl-tracking.md), [기존 평가 명세](../docs/08-evaluation.md)의 **보충 참고자료**다. 원래 보고의 다른 자료를 무조건 이관하지 않았다. 모델의 실제 학습·재현·보호 보장은 **OPEN**으로 유지한다.
