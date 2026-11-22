# 2026-11-23 SBL 주간 보고 — Melete 관련 항목 선별 동기화

**ARCHIVE / discussion-import + 일부 LITERATURE(official abstract checked); NOT RUN.** 독립 자동화 `Schema 기반 AI 연구 동향`의 2026-11-23 완료 보고(run `cf2a13f1-5a60-832b-a5f2-ae489225b19e`, 표기 조사 범위 11/16–23)를 직접 읽어 **전체 보고가 아니라 Melete/System ONE과 연결되는 사항만 선별·재구성**했다. 아래 메타데이터와 초록 핵심은 별도로 공식 arXiv/PubMed/학술지 페이지에서 대조했고, 실험 상세 수치·ablation·코드는 이번 동기화에서 재현하지 않았다. 신경망의 연속 표상(continuous representation)과 세션 간 지속학습(continual learning)은 독립 축이다. **출처/확인 범위:** [2026-11-23 보충 원문 목록](../references/2026-11-23-sbl-sleep-sources.md). 이전 기록 [11/16 SBL](2026-11-16-sbl-tracking.md), [11/11 full-text 검토](2026-11-11-sbl-fulltext-review.md)를 대체하지 않는다.

## 1. 최근 변화 — 새 출판과 이전 연구의 새 발견을 구분

- **11/17 정식 게재 (LITERATURE / PubMed metadata+abstract checked):** Yu et al., *A Neuro-symbolic Framework under Statistical Relational Learning*, IEEE TPAMI, online ahead of print 2026-11-17, DOI [10.1109/TPAMI.2026.3755075](https://doi.org/10.1109/TPAMI.2026.3755075), [PubMed](https://pubmed.ncbi.nlm.nih.gov/43043738/). 선행 preprint는 [arXiv:2309.08931](https://arxiv.org/abs/2309.08931) (v1 2023-09-16, v2 2025-02-22). **분류 HYBRID**: continuous neural representations로 latent predicate를 학습하지만 first-order logic rules는 명시적 symbolic이다. Neuro-symbolic interaction과 variational EM이 핵심. 세션 간 neural schema CRUD/continual learning 또는 latent-only schema 효과를 증명한 것은 아니다. 새 TPAMI 전문 비교·코드 실행은 **NOT RUN**.
- **이전에 발표됐지만 이번 주간 보고에서 새로 포착 (LITERATURE / official abstract checked):** Deng et al., [*Early Learning Shapes Later Directions Of Representation Change In Continual Learning*](https://arxiv.org/abs/2609.36081), v1 **2026-09-28**, v2 **2026-10-01**. 네 개 pretrained visual encoders·두 데이터셋의 연속학습에서 초기 경험이 만든 low-dimensional representation-drift subspace(scaffold)를 이후 갱신이 선호한다. **명시적 SBL 아님; continuous neural representation의 기능적 인접 연구**. 중요 반례: scaffold 내부로만 갱신을 강제하면 무작위 제약보다 새 학습이 느려지고 구지식 보존도 일관적이지 않다. [저자 코드](https://github.com/YuantaoDeng/latent-scaffold) 링크는 arXiv 초록에 표시되나 실행/재현은 안 함.
- **이전 연구의 새 발견 (LITERATURE / official abstract+선별 HTML checked):** Goo et al., [*SchemaMem: Schema-Indexed Recurrent Memory for Delayed State Retrieval*](https://arxiv.org/abs/2609.33436), v1 **2026-09-27**, preprint. 학습된 정적 schema embeddings와 에피소드별 동적 state를 통한 bounded recurrent memory. 여기의 'schema'는 추상 관계 규칙의 자율 발견보다 **학습된 읽기/쓰기 기준 공간**에 가깝다. 저자 초록은 9개 주소/값 조건·3 seed에서 장기 기록값 보존과 갱신값 복원의 이득을 보고하나, 기본값 추론은 Gated DeltaNet이 낫고 optimizer step은 크게 더 많다고 명시한다. 정확도·학습 step의 추가 숫자는 **독립 재계산/재현하지 않았으므로** 원 보고 값을 입증 결과로 승격하지 않는다. Neural continuous ≠ 검증된 일반 SBL ≠ 지속적 추상 학습.
- **이전 연구의 새 발견 (LITERATURE / 학술지 본문 일부 checked):** Dong et al., [*Symmetry-Aware Schema–Session Decoupled LoRA Adaptation for Continual Knowledge Graph Completion*](https://doi.org/10.3390/sym18060953), *Symmetry* 18(6), 953, **2026-06-01**. Frozen ChatGLM3-6B backbone에 공유 Schema-LoRA와 세션 전용 Session-LoRA를 더해 5개 순차 세션 knowledge graph completion을 평가한다. LoRA rank 8, OGP/Session-EWC, 3 seeds는 논문 본문 확인. **표현은 학습되는 continuous adapter이나, 관계 schema를 추론 시 독립적으로 발견/선택한 것은 아님**: session identity가 제공된다. 데이터셋 MRR의 이전 주간 보고 수치는 저자 조건이며 결과를 새 실험으로 표현하지 않는다.

**ARCHIVE:** 독립 보고가 '11/16–23에 direct continuous neural SBL의 전 생명주기를 통합 실증한 신규 모델을 발견하지 못했다'고 기술했다. 이는 검색 범위의 **미발견**이지 논문의 부재 증명이 아니다. 기존 TEM/Goudar/Chu/Yoshida/Kumar/Spens/S-HAI 등은 새 변경 확인 없이 반복하지 않았다. `CSCG`/`S-HAI`의 discrete latent와 continuous neural schema의 분류를 합치지 않는다.

## 2. Melete / Ali A-B-C 실험과 연결 (PROPOSAL / OPEN / NOT RUN)

| 주장 | 새 비교·개입 설계 후보 | 성공 주장 전에 필요한 통제 |
|---|---|---|
| A: 경험량·계산 | SchemaMem식 지연보존·값 변경·미기록 기본값을 분리하고 target quality까지 **unique experience N***, optimization steps/FLOPs, online/Sleep·storage C*를 모두 기록 | 같은 품질/원천 경험/저장 예산. retention이 좋아도 학습 비용이 커질 수 있음 |
| B: 구조 전이·편향 | 처음 겪는 이력 H1/H2를 다르게 준 뒤 **동일한 새 데이터**에서 update direction과 unseen 구조 공유 사례의 sample efficiency를 측정 | scaffold alignment와 유익한 transfer를 별도로 입증. 강제 subspace update와 random constraint, wrong-schema, frozen/ablation |
| B: schema 선택 | Shared Schema-LoRA + Session-LoRA를 **oracle session ID 제공** 진단군과 task-ID-free context-conditioned read/activate군으로 분리 | oracle session ID의 편의와 expert content/routing의 효과, 저장량 증가, negative transfer 구분 |
| C: 발견 | 표면이 다른 새 환경과 관계 mismatch를 사용하여 발견 후 새로운 예측과 법칙 수정 확인 | 기존 [ET](../docs/17-einstein-test.md)와 A/B/C 조건 구별, 현대 사전지식/trajectory 누수 봉쇄 |

Schema가 내부적으로 연속 latent에 있다는 것, 그 부분공간이 사후 관측되는 것, 새로운 사례의 학습량/계산을 절약하는 것, 장기간 망각이 없는 것은 각각 다른 claim이다. 수치 gate·신규 모델 구현·실험 착수는 **승인된 사실 아님**. 관련 기준: [Ali A/B/C](2026-11-22-ali-abc-evaluation.md), [Schema lifecycle](../docs/14-schema-lifecycle-crud-and-joint-paper.md), [평가](../docs/08-evaluation.md).

## 3. 접근 제한

11/23 독립 주간 보고는 자동화의 완료 결과 텍스트로 **전체 확인**했다. 위 선별 원문은 official arXiv landing/abstract, Symmetry 논문 본문 선택 구간, NSF-SRL PubMed metadata/abstract이며 논문 원문 전체·부록·코드 실험 재현은 **NOT RUN**. 원 보고의 모든 숫자와 관찰을 통째로 가져오지 않았으며, 새로운 Neural-SBL efficacy·실제 유의성·확정 구현을 선언하지 않는다.
