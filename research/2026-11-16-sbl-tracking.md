# SBL 전용 주간 보고 보존 — 2026-11-16

## 지위와 출처

**ARCHIVE / discussion-import.** 현재 대화에 표시된 2026-11-16 주간 보고(표기된 조사 범위 11/9–11/16)를 저장소용으로 재구성했다. 아래 논문 메타데이터·수치·읽기 범위는 그 보고의 주장을 보존한 것이며, 이번 동기화에서 웹 재검색·전문 재독·코드 실행을 새로 수행하지 않았다. 따라서 현재 최신 상태의 독립 확인으로 인용하지 않는다. 공식 링크는 검증 출발점이다.

이번 보고는 '해당 기간에 continuous neural schema의 형성·선택·수정·장기 학습을 통합 검증한 신규 논문이나 중요한 기존 개정을 확인하지 못했다'고 보고했다. 이는 과거 조사 범위의 미발견 진술이지 관련 연구의 부재 증명이 아니다.

## 1. 원 보고의 핵심 목록

| 원 보고의 분류 | 연구 | 원 보고에 적힌 날짜/상태 |
|---|---|---|
| 신규 발견한 이전 연구 | Domain-specific schema reuse supports flexible learning to learn in the primate brain | Nature Communications 17, 2150; 2026-01-29; 이전 bioRxiv 2024-10-27 |
| 신규 발견한 이전 연구 | Explicitly acquired interrelations among mental schema reduces cognitive load and facilitates emergence of novel responses in mice and artificial neural networks | Experimental Brain Research 244, 78; 2026-03-22; Correction 2026-08-24 |
| 신규 발견한 이전 이론 | Working Paper: Towards Schema-based Learning from a Category-Theoretic Perspective | arXiv:2604.10589 v1; 2026-04-12 |
| 추적 유지 | S-HAI, Yoshida, Kumar, Schema for ICL, IP2-RSNN | 의미 있는 새 변경을 확인하지 못했다고 보고 |

### 보존 시 식별한 중복 문제

Tian의 영장류 schema 연구는 현재 대화의 더 이른 SBL 개괄 답변에서도 이미 언급되어 있다. 따라서 11/16 보고의 '처음 발견'이라는 분류는 대화 전체를 기준으로 확정할 수 없다. **기존 언급 논문의 재검토/상세화 후보**로 처리하고, 주간 신규 발견 수에 중복 산입하지 않는다. 제목·연구 내용을 삭제하거나 새 발표로 바꾸지 않으며, DOI/버전 대조는 후속 검증 대상으로 남긴다.

**처리 (2026-11-17 검토):** 위 중복은 저장소 내부 근거로 확정된다. catalog N28과 [2026-11-02-baseline.md](/home/jimmy/repos/full-continual-learning/research/2026-11-02-baseline.md) 33행에 이미 있어(첫 커밋 2026-11-09) 신규 발견이 아니며 2026-11-09 기록과 2026-11-11 원문 검토에는 없다. DOI 레지스트리 대조로 서지(Nature Communications 17, 2150, 2026-01-29)는 일치한다. 분석 코드 주소와 이전 bioRxiv 2024-10-27은 보고 이관으로 남는다. 자세한 처리는 [2026-11-16-discussion.md](/home/jimmy/repos/full-continual-learning/sources/sync/2026-11-16-discussion.md)에 있다.

## 2. Tian et al. — continuous neural activity의 신경과학 근거

보고된 저자: Kaixi Tian, Zhiping Zhao, Yang Chen 외. [저널](https://www.nature.com/articles/s41467-026-68692-x), [분석 코드](https://github.com/kathytian-kx/DomainSpecific_SchemaReuse).

원 보고에 따르면 수컷 마카크 3마리의 PMd 신경활동을 기록하며 A → B/C → A 재방문 → A 대응 반전을 비교했다. 재사용되는 decision subspace와 변화하는 stimulus subspace가 거의 직교하며, 반전 관계에서는 기존 schema 재사용이 학습을 방해하는 양상이 보고되었다.

보존하는 정량 진술: 14 sessions에서 후속 B/C 학습 가속 P=2.30×10^-4, Hedges' g=1.47; Reverse-A 지연 P=0.0012, g=-1.59; 두 마카크의 재사용 정도–학습 시행 수 관계 R²=0.47/0.49, P=0.04. 이 값은 **원 보고에서 이관한 수치이며 원문 표·정의·분모를 이번에 재대조하지 않았다**.

Schema 분류는 신경집단 활동의 continuous subspace에 대한 해석이다. LFADS의 16차원 분석 공간을 뇌가 저장하는 고정 벡터 객체로 해석하지 않는다. 실제 동물의 순차학습이지 frozen LLM 또는 장기 AI 기억 엔진의 구현이 아니다. 다른 과제에 decoder를 적용한 분석을 신경회로의 인과적 제거 실험으로 부르지 않는다.

원 보고의 읽기 범위: 공개 저널의 본문·Methods·Results·코드 공개 설명을 검색 결과를 통해 확인했다고 기술했다. PMC 직접 접근과 부록 전체에는 제한이 있었다고 밝혔다. 코드는 분석·디코딩·그림용이며 학습형 Melete runtime이 아니다. 원자료 전체의 접근 조건은 재확인이 필요하다.

Melete 연결은 **PROPOSAL**: 공유 판단 구조를 보존하면서 새로운 binding의 표현/변경을 분리할 수 있는가. 활동 부분공간의 직교성을 LoRA update 공간의 직교성 또는 무망각 증명으로 치환하지 않는다. Reverse-A와 같은 표면 유사·관계 반전 대조군을 포함한다.

## 3. Singh et al. — schema 간 관계, 분류 미확정

보고된 저자: Vikram Pal Singh, Shruti Shridhar, Sankhanava Kundu, Richa Bhatt, Balaji Jayaprakash.

[원 논문](https://doi.org/10.1007/s00221-026-07252-7), [정정](https://doi.org/10.1007/s00221-026-07373-z).

원 보고는 쥐가 기존 mental schema 사이의 관계를 학습하면 새로운 상황에 맞는 반응을 만들고 간섭을 줄이는 결과와, 이를 모델링한 ANN을 소개했다. Contrastive Hebbian learning과의 관련을 언급했으나 정확한 수식·sample size·정량 표는 확보하지 못했다고 표시했다.

**확인 수준은 초록 중심**이다. Schema가 구체적으로 어떤 continuous state나 symbolic relation에 표현되는지, 어떤 모듈이 학습되고 고정되는지, 세션 간 상태가 유지되는지, 공식 구현이 있는지, 8월 correction이 무엇을 바꾸는지는 OPEN이다. ANN이라는 이유만으로 continuous schema로 확정 분류하지 않는다. Cognitive load를 FLOPs나 latency와 동일시하지 않는다.

Melete 연결은 **PROPOSAL**: 독립 expert의 축적과 함께 expert 간 재사용 가능한 관계와 조합도 학습해야 할 수 있다. 분리가 모든 상호작용의 제거를 의미하지 않도록 한다.

## 4. Symbolic / formal SBL

Pablo de los Riscos, Fernando J. Corbacho, Michael A. Arbib의 [Working Paper: Towards Schema-based Learning from a Category-Theoretic Perspective](https://arxiv.org/abs/2604.10589)를 원 보고가 소개했다.

Schema의 추상 구조·구현·확률적 의미·실행 및 memory read/write를 형식화하는 연구로 설명되었다. Neural continuous schema 형성의 실험 증거나 학습 benchmark·정량 ablation·공식 코드가 확인됐다고 주장하지 않았다. 이번에도 이를 새로 검증하지 않았다. CRUD 개념 정리에 참고할 후보이지 모델 성능의 근거가 아니다.

**LITERATURE (2026-11-17 확인):** 위 논문의 제목·저자 3명·최초 제출(2026-04-12 v1)은 arXiv 초록 페이지에서 확인했고 2026-11-17 현재 목록에는 v1만 있다. 본문은 초록·목차·§1·§2·§3 일부·§5.2 일부·§7·§8만 읽었다. 저자 스스로 '닫힌 형식 체계가 아니라 구조적 프로그램'이라 밝힌 미완 working paper이며 신경망 학습 실험·코드는 없다. 이 논문의 Add·Del·Update 연산자가 CRUD 어휘의 형식적 선례라는 점과 그 한계는 [14-schema-lifecycle-crud-and-joint-paper.md](/home/jimmy/repos/full-continual-learning/docs/14-schema-lifecycle-crud-and-joint-paper.md) §3에, schema 정의와의 차이는 [03-foundations.md](/home/jimmy/repos/full-continual-learning/docs/03-foundations.md) §6에 적었다. 위 '이번에도 이를 새로 검증하지 않았다'는 서술은 이 확인 범위만큼 갱신한다.

## 5. Hybrid 및 인접 연구의 당시 추적 상태

| 연구 | 분류 | 원 보고에서 보존하는 상태 |
|---|---|---|
| S-HAI | discrete latent / structured probabilistic | [코드](https://github.com/toonvdm/grounding-schemas) 확인을 보고. 이번 주 최초 공개라는 증거는 없음. 여러 grounding을 여러 schema의 생성·경쟁으로 바꾸지 않음 |
| Yoshida et al. | continuous neural manifold | bioRxiv 2026-06-01 v1 및 replay/차원축소/manifold alignment. 새 버전·코드 미확인 |
| Kumar et al. | neural representation + association + control | arXiv 2106.03580 v5(2026-10-20)를 당시 최신으로 보고 |
| Schema for In-Context Learning | explicit structured scaffolding | arXiv 2510.13905 v3(2026-03-28)를 보고. ICL과 세션 간 가중치 학습을 구분 |
| IP2-RSNN | neural dynamics/intrinsic plasticity, adjacent | arXiv 2501.14539 v5(2025-09-26)를 보고 |

위 최신 상태는 원 보고의 주장이지 동기화 시점의 재검증 결과가 아니다. 일반 RAG·DB schema·KG path QA를 이름만으로 SBL 신규 연구에 포함하지 않는 원칙을 유지한다.

## 6. Melete 가설과 실험으로 연결

A. 기능적 분리: 같은 용량에서 일반 LoRA, 무작위 분할, schema별 low-rank, 간섭 제약을 둔 schema별 low-rank 비교.

B. 재사용 실패 판별: 익숙한 개체지만 관계가 반전된 조건에서 재선택·수정·보류를 비교. 높은 유사도만으로 적합성을 판정하지 않음.

C. 조합성: 각각 배운 schema를 연결한 뒤 처음 보는 교차 문제를 평가. 독립성만 높여 전이를 잃지 않는지 확인.

D. 비용: 표본 효율, ABA 복귀, 새/옛 조건 paired correctness, update interference, 인과적 개입, 같은 품질의 loop/FLOPs/latency 및 장기 학습비용을 함께 보고.

## 7. 후속 추적

P0: Tian 원문 수치·decoder transfer·Reverse-A·분석 코드와 데이터 조건. Singh 전문·정정 내용·ANN 학습 규칙·공식 코드. Yoshida/Boboeva/Goudar의 신경 부분공간·재생·전이 메커니즘.

P1: S-HAI가 다중 grounding을 넘어 실제 다중 schema 형성·경쟁·수정으로 확장되는지 확인.

**NOT RUN:** 이번 기록 이관은 모델 구현, 코드 실행, 신경과학 수치 재현, 새 문헌 검색이 아니다. 관련 [CRUD 설계](../docs/14-schema-lifecycle-crud-and-joint-paper.md) 및 [보충 링크](../references/schema-lifecycle-2026-11-16.md)와 연결한다.
