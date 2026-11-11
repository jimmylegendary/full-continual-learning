# 11. 후속 가설·불확실성·연구 질문

## 1. Pretraining과 alignment 가설

**사용자 가설:** LLM은 대량 데이터에서 하나의 schema를 학습했고, post-training/RL alignment는 이를 여러 sub-schema로 분화하는 기능을 만들었을 수 있다.

이 가설을 보존하되 현재 사실로 채택하지 않는다. 하나의 parameter set은 여러 조건부 기능을 표현할 수 있다. 전체 지식 체계를 하나의 schema라고 정의하면 반증 가능성이 약해진다. [S26 Function Vectors, S24 Task Schema and Binding]

경쟁 가설:

| 가설 | 관찰할 변화 |
|---|---|
| Access/routing | 기존 기능을 문맥에 맞게 더 잘 선택 |
| Specialization | 기능적 부분의 분리와 전문화 |
| New structure | 이전에 없던 표현/연산의 형성 |
| Output policy | 내부 구조보다 말투·선호·응답 정책 변화 |

같은 base의 Base→SFT→DPO/RL checkpoint를 비교하고 비슷한 token·compute의 control을 둔다. 역할/표면 교차 전이, causal patching/lesion, selective impairment, 새로운 binding을 평가한다. cluster 수 증가, rotation에 민감한 시각화만으로 분화를 주장하지 않는다. 이 연구는 MVP의 선행 조건이 아니다.

**LITERATURE (SWAMI23, W6-swami23-metadata-gap.md:91; 원문 검토 §2):** "LLM에서도 같은 기제"는 저자들이 "We conjecture"라 쓴 추측이며 transformer 실험은 없다. **LITERATURE (SPECTRUM26, W5-spectrum26-structk25.md:96,113-114,121-122):** LLM에 대한 대응(ICL ≈ integration, knowledge conflict ≈ assimilation, fine-tuning ≈ accommodation)은 "Arguably"가 붙은 정성 유추이고 데이터가 없으며, 저자는 현재 모델이 schema에 "akin"한 것을 갖되 효과적으로 쓰지 못할 수 있다고 쓴다.

**PROPOSAL:** 이 두 문헌은 위 사용자 가설(pretraining=하나의 schema, post-training=분화)을 지지하거나 반증하는 증거가 아니다. 경쟁 가설 표의 관찰 계획은 그대로 둔다.

## 2. Schema의 물리적 단위

한 schema가 MLP 하나인지, low-rank subspace인지, recurrent trajectory인지, 여러 모듈의 조합인지 열린 문제다. 여러 표현을 비교하되 재사용/전이/수정/보존 기능을 공통 평가한다. Neural manifold와 symbolic role 구조는 설명 수준이 다를 수 있다.

**LITERATURE (STRUCTK25, W7-remediation.md:51; 원문 검토 §3):** 서술형 리뷰는 schema 모델을 명시적(TEM, SMP, CSCG 등 11개)과 암묵적(Goudar·Driscoll의 manifold, Yang·Dubreuil의 subpopulation 등 4개)으로 나눈다(§3.2.2, Table 3). 이는 분류이며 둘 사이의 우열 증거는 없다. **LITERATURE (SPECTRUM26, W5-spectrum26-structk25.md:72-76):** SPECTRUM26은 schema를 별도 저장소가 아니라 분산 표현의 추상화 수준 스펙트럼으로 보지만 추상화의 측정법은 없다.

**PROPOSAL (원문 검토 §5 출발점 1):** retrofit LLM에서는 둘 중 하나를 고르지 않고 세 측정을 조작적 증거로 쓴다([03-foundations.md](/home/jimmy/repos/full-continual-learning/docs/03-foundations.md) §1). **OPEN (W7-remediation.md:139):** retrofit LM에는 implicit-subspace 계열이 맞아 보이나 STRUCTK25에 우열 증거는 없다.

## 3. 표현 보호와 확장

기존 저차원 표현이 예외에 필요한 구분을 억제할 수 있다. 반대로 모든 입력에서 전체 weights를 고치면 안정된 구조가 사라질 수 있다. 보호·국소 수정·rank expansion·schema branch/split을 후보로 두고 F05/F06에서 비교한다. 논의된 근거: curriculum unlearning [S19], invariant schema [S25], recurrent scaffold [S23].

**LITERATURE (ELDER26, W3-elder26-miconi25.md:21-22,126-130,175; 원문 검토 §2·§3):** [S25]는 순차 학습·새 클래스·망각을 시험하지 않았고, 고정되는 쪽은 출력 쪽 hidden layer(HL1·HL2)이며 갱신되는 쪽은 입력 쪽 가중치(IL)다. 11-09 기록의 "상위 schema circuit"은 같은 사실을 반대 어휘로 적은 것이다. **PROPOSAL (W3-elder26-miconi25.md:145, 원문 검토 §3 ELDER26 주의):** 불변성이 SVM 구성과 weight equalize에서 나왔을 가능성이 있으므로 "보호가 필요하다"의 직접 근거로 읽지 않는다.

**ARCHIVE (S19·S23, 2026-11-09-sbl-tracking.md:11-15,62-64):** [S19]는 인간 행동 실험과 신경망을 다룬 인접 근거이고 neural dimensionality를 직접 측정하지 않았다. [S23]의 수치는 원보고 범위로 귀속하며 이번에 정독하지 않았다.

**PROPOSAL (가설 B, 2026-11-09-sbl-tracking.md:90; 원문 검토 §4.3):** rapid learning에서 보호·국소 수정·표현 확장·분리 중 무엇을 고르는지는 OPEN으로 연구한다. 구조를 불일치 시 그 자리에서 고치는 기제는 읽은 문헌에 없으므로 F05/F06 비교의 대상은 문헌 재현이 아니라 우리 설계다.

## 4. 통찰의 운영적 정의

현재 문제를 더 오래 생각한 사실이 아니라 새로운 관계·표현·적용 조건을 형성하고 새로운 사례에서도 재사용하는 변화다. 동일 정답의 암기, self-consistency, 반복된 confidence 증가는 충분하지 않다. Reconstruction에서 relational generalization으로 넘어가는 경계가 핵심이다.

**LITERATURE (CHU25, W2-chu25-goudar23.md:138-141):** unshaped 망이 shaped 망보다 더 저차원이었다(본문 top-3 PC 분산비 93% 대 82.5%). **ARCHIVE (S20, 2026-11-09-sbl-tracking.md:19-23,88; 확인 깊이 official-search-checked):** 파라미터 공간의 압축과 과제 시간 구조의 형성을 구분하는 것이 가설 A이며, 코드 공개는 당시 미확인이었다.

**PROPOSAL (가설 A):** 저차원성·압축 자체를 구조 형성의 증거로 보지 않고, 안정된 cluster나 저차원화를 schema 형성 PASS로 삼지 않으며 새 과제 예측·전이로 판정한다.

## 5. Rhythm 필요성

Event/readiness controller에 oscillator를 더해야 어떤 이득이 있는가? 지연이 가변적이거나 여러 속도의 process가 상호작용하는 환경에서 추가 가치가 있을 수 있으나 아직 제안이다. 유효한 event-only baseline과 비교한다. 동기적 stage ID와 동치인지 검토한다.

## 6. LLM과 개인 경험의 관계

Base LLM에도 재사용 가능한 구조와 ICL이 있을 수 있다. Melete의 문제는 그 구조를 개인의 새 경험으로 지속 갱신하고, 현재 문맥에 적합하게 사용하고, 장기 보존과 수정의 균형을 맞추는 것이다. ‘schema가 없는 LLM에 최초로 schema를 넣는다’로 차별성을 과장하지 않는다.

**USER (B14/H1, 2026-10-12):** LLM은 일반화 지식에 특화돼 있고 개인의 암묵지와 판단 pattern을 실시간 학습하지 못한다.

**ARCHIVE:** Melete는 H1을 'LLM이 in-context adaptation을 못 한다'는 주장으로 읽지 않고 지속 상태와 경험에 따른 개인적 편향을 분리해 보완하는 제품 가설로 읽었다. 관측 조건은 같은 LLM·같은 질문에서 서로 다른 경험 이력이 다른 경로와 적절한 판단 편향을 만드는가였다 ([neural-basis.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/design/neural-basis.md)).

**PROPOSAL:** 통합 모델에서는 이 가설을 '같은 초기 모델에 서로 다른 경험 이력을 준 두 상태가 같은 질문에서 다른 적절한 판단과 계산 경로를 보이고, 반례가 오면 각자 고칠 수 있는가'로 시험한다. '별도 신경 계층이 LLM을 보완한다'는 구현 형태는 U-T07의 통합 모델로 대체됐다. 평가는 [08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md)의 이력 분기 family 후보 F17(이력 의존 편향 측정 포함)로 한다.

**PROPOSAL (헌장 6층위 가설, 대화에서 도출한 해석):** 이력에 따른 자기 조직화. 같은 초기 모델이라도 경험 이력에 따라 잘 알아보는 구조, 우선 가설(q^-), 계산량, 학습 정책이 달라질 수 있다. 사용자 발화 근거는 "사람마다 익숙하다 느끼는게 아예 다름"(U-T03 PDF p11 발췌)이다.

**OPEN:** 이 가설은 아직 이 문서군의 설계에 연결돼 있지 않다. 시험은 F17(이력 분기, [08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md) §2-1)로 한다. 최소 설계: 같은 초기 체크포인트에서 이력 H_a·H_b를 각각 주고 (a) 같은 입력에서의 schema 선택 분포, (b) 요구 정확도까지의 loop 수, (c) update 정책 출력(write 빈도·강도)을 비교하고, 교차 과제에서 이득의 비대칭(H_a가 H_b 과제를 돕지 못함)을 확인한다. 대조: 같은 이력의 순서 섞기, 같은 이력의 다른 seed, 이력 없음.

**상한:** 분기가 관찰돼도 자기 조직화나 개인화의 일반 원리를 입증한 것이 아니며 단일 world 계열·소형 모델의 관찰로만 보고한다. 이 연구는 MVP의 선행 조건이 아니다.

**LITERATURE (갭 탐색, [2026-11-11-sbl-fulltext-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext-review.md#6-갭-주장-판정) §6, 범위 한정, W6-swami23-metadata-gap.md:117):** 외부 요약의 결론("다양한 경험에서 schema를 스스로 발견·형성·수정·통합하고, 그 schema가 이후 학습 규칙 자체를 제어하는 범용 지속학습 아키텍처는 완성된 형태로 확인되지 않았다")에 대해 검색 범위 안에서 반례를 찾지 못했다. 범위는 2023-01-01~2026-11-11이다. OpenAlex 26개·arXiv API 44개·Semantic Scholar 9개·웹 검색 5개 쿼리로 고유 레코드 1,047건을 얻어 제목 265건과 초록 약 42건을 읽었고 전문은 5건을 부분적으로 읽었다(W6-swami23-metadata-gap.md:117).

**LITERATURE (갭 탐색, 원문 검토 §6, W6-swami23-metadata-gap.md:156):** 판정 기준 (i) 구조의 발견·형성, (ii) 불일치 시 수정·분할·병합, (iii) 그 구조가 이후 학습 규칙(무엇·어디·얼마나·언제 갱신할지) 제어, (iv) 순차 다과제·다영역 평가, (v) 구현·평가된 완성 형태를 모두 만족하는 사례는 발견되지 않았다. 가장 가까운 사례는 Shan·Minni 외 arXiv 2510.20709(문맥 posterior가 저랭크 RNN의 계산과 학습을 gate하나 task id가 입력으로 주어지고 생성 모형 계열이 손으로 정해짐), LCNet, ALMA이며 모두 소규모이거나 오프라인 탐색이다.

**OPEN:** 이 결론은 검색 범위와 근거 깊이에 대한 서술이며 "갭이 존재한다"는 증명이 아니다. Semantic Scholar 쿼리 9개 중 5건은 HTTP 429로 실패했고(W6-swami23-metadata-gap.md:169) Nested Learning/HOPE·Titans·ATLAS는 부분만 만족했으나 대부분 초록 수준 판정이다.

## 7. 우선 읽을 연구 연결

- TEM/transformer–hippocampal relation → 구조와 내용의 분리.
- Goudar/Chu/Yoshida/Boboeva → subspace·attractor·manifold·low-rank scaffold.
- LCNet/S-HAI/latent cause → 맥락 선택과 binding; continuous와 discrete 구분.
- GNM → 선택적 write의 학습 가능성.
- Episodic CLS LLM/Spens → 저장/재구성과 판단/통합의 차이.
- Loop/MoD/MoR/AttnRes/MoDA → 계산 배분과 이번 사고의 표현 재사용.
- HOPE/Titans/Sleep → 빠른 상태와 여러 시간척도의 학습.

**LITERATURE (11편 전체, 원문 검토 §1, 확인 깊이 fulltext-read):** 원문으로 읽은 11편은 SPENS24·HWU20·CHU25·GOUDAR23·ELDER26·MICONI25·TEM20·KUMAR26·SWAMI23(구현·모형 9편)과 STRUCTK25·SPECTRUM26(리뷰·관점 2편)이며 판본과 해시는 [evidence.json](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/evidence.json)에 있다.

**OPEN (원문 검토 §7, 미정독 추적 후보):** Shan·Minni 외 *Separating the what and how...*(arXiv 2510.20709, catalog S35)는 문맥 추론이 계산과 학습을 동시에 gate해 갭에 가장 가깝지만 §1–4·Discussion만 읽었다. SMART(Gao 외 2021)는 지속학습을 직접 다루는 schema 모델이며 STRUCTK25 참고문헌에서 발견했고 DOI는 미확인이다. Kobayashi 외 2025(arXiv 2512.20605)는 transformer 내부 schema로 계층적 행동을 제어하며(SPECTRUM26 ref 96) 식별자가 미확인이다. Lanzillotta·Samiei·Precup·Pascanu 2026(arXiv 2607.05609, "To Retain or to Adapt?")과 Stoianov 외 2022(generative replay와 지속학습)도 미확인이고, Spens & Burgess 2026 compressive RAG(catalog S07)는 SPENS24의 후속으로 두 실험 계열을 섞지 않고 비교한다.

**ARCHIVE (2026-11-09-sbl-tracking.md:96-102):** 11-09 추적 항목 중 P0(Boboeva 코드·수치, GNM write-path·자율 지시, Yoshida 원문·코드), P1(S-HAI schema 생성·경쟁, curriculum 표현 지표, Task Schema 인과 재현, CLS 직접 QA 통합), P2(graph/program schema와 neural 모델의 공통 전이 benchmark)는 11-11 원문 검토에서 다루지 않아 미결이다. Kumar v5(2026-10-20)는 11-11에 원문으로 읽어 최신 버전 재조회가 끝났고 S-HAI v3(10/26)는 재조회하지 않았다.

전체 링크와 확인 수준은 [문헌 목록](../references/README.md)에 있다.

**LITERATURE (GOUDAR23·MICONI25·KUMAR26·SPECTRUM26·SPENS24, [2026-11-11-sbl-fulltext-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext-review.md#8-미해결) §8):** 확인 수준의 한계가 남아 있다. GOUDAR23·MICONI25·KUMAR26·SPECTRUM26은 VoR 조판본이 아니라 accepted manuscript·proof·preprint를 읽었고 SPENS24의 bioRxiv 판은 VoR과 대조하지 못했으며 편집 차이는 배제하지 못한다. KUMAR26은 arXiv v1(2021-06-07)이 제목과 내용이 다른 reservoir 논문이고 v5(2026-10-20)가 J Neurosci early release(2026-10-26)와 초록이 같다(W4-tem20-kumar26.md:229,233,235,239).

**LITERATURE (CHU25·ELDER26·KUMAR26·STRUCTK25, 원문 검토 §8, W7-remediation.md:387-396):** 정의·불일치가 미해결인 수치도 있다. CHU25의 정확도 정의, 93.20의 분모, 쪽수(7103–7121 대 7922–7940), ELDER26의 ± 정의와 978 대 888 clips, KUMAR26의 본문 ± 정의다. STRUCTK25는 동적 HTML에서 받은 텍스트라 해시를 고정했고 그림은 보지 않았다.

**LITERATURE (11편 전체, 원문 검토 §3 서두·§8):** 코드는 하나도 실행하지 않았고 재현성 평가는 정적 읽기이며 그림에서 읽은 수치는 근사값이다. 이 11편의 확인 깊이는 fulltext-read이지 재현이 아니다.

**USER (B08–B10, 2026-10-09~11):** fine-tuning·RL 수준이 아니라 backward·SGD 수준의 근간 학습 방법(forward learning, 뇌과학적 방법·모사 포함)을 전수 조사하고 고찰한다. 학습 방법 50개를 ELI 그림으로 설명하고 제품 적합 순으로 우선순위를 매기며 library 존재와 수학적 완결 여부를 표시하고 조합별 적용 방식과 효과를 정리한다. 거인의 어깨 위에서 새 학습 메커니즘과 논문을 만들지 기존 방식 조합으로 충분한지도 물었다.

**ARCHIVE:** Melete는 12계열 50개 비교 항목과 58개 원 자료 참조의 기초 학습 방법 대장, 그리고 제품 적합 순위와 13개 조합을 가진 atlas를 만들었다 ([2026-10-09-learning-method-catalog.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/research/2026-10-09-learning-method-catalog.md), [2026-10-09-learning-atlas-mechanisms.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/implementation/records/2026-10-09-learning-atlas-mechanisms.md)). 이는 문헌·API·수식 검토이며 실행·채택이 아니고 순위는 외부 memory 구조(Melete) 기준이다. FCL은 이를 이관하지 않았고 통합 모델 기준으로 재검토하지 않았다.

**PROPOSAL:** 학습 규칙 후보 지도를 이 절 아래에 둔다(미작성). 계열별로 신호, 갱신 대상 상태, 근거 문헌, library 존재, 수학적 정의 완결 여부, FCL 적용 자리, 대조군을 채우고 FCL 적용 우선순위는 통합 모델 기준으로 다시 매긴다. 학습 규칙의 조합은 같은 신호·예산의 단순 대조군과 함께 비교하고 검증 수준은 [08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md) §1의 표기를 따른다.

**PROPOSAL (새 메커니즘 대 기존 조합):** 새 학습 메커니즘이나 논문 주장은 두 조건이 모두 확인될 때만 제안한다. (1) 문헌 검토에서 그 기능의 직접 구현이 없다. (2) 같은 예산의 기존 조합과 단순 대조군이 그 기능에서 실패한다. 그 전에는 기존 재료의 조합으로 진행하며, 어느 부분이 빌린 것이고 어느 부분이 새것인지의 기여 지도를 [05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md)에 둔다.

**OPEN:** 학습 규칙 후보 지도의 작성 시점과 담당은 정하지 않았다.

## 8. 검증 없이 주장하지 않을 것

하나의 universal brain switch, schema=특정 Hz, biological state의 완전 재현, 신경망 모든 부분공간의 의미 해독, 범용 AGI, 통합 모델의 미실행 속도 이득, 기존 Melete보다 나은 실제 사용자 성능, 삭제 요구가 모든 consolidated weights에서 완전 제거됨.

**PROPOSAL (원문 검토 §0·§4, 문헌 검토 뒤 추가):** 다음도 검증 없이 주장하지 않는다. 학습된 schema 구조가 같은 예산의 고정·무구조 대조보다 낫다는 것, 문헌이 H-COMPUTE(같은 품질의 추론 계산량 감소)를 뒷받침한다는 것, 불일치 시 구조를 수정하는 기제가 문헌에 있다는 것이다.

**OPEN (가설 C, 2026-11-09-sbl-tracking.md:92; 원문 검토 §4.3·§4.4):** 열린 질문은 둘이다. accommodation은 오류 크기·fit에 따라 새 구조와 미세 조정 중 무엇을 고르고 어떻게 평가하는가(읽은 문헌에는 정성 규칙뿐이다). H-COMPUTE는 어떤 신호(CSCG posterior 엔트로피, recall 신뢰도, attractor 수렴)가 고정 깊이 곡선 위에서 계산을 줄이는가, 곧 schema 선택과 선택적 쓰기가 다음 추론의 비용에 영향을 주는가.

**ARCHIVE (2026-11-09-sbl-tracking.md:94):** 11-09 조사는 이 논문들이 recursive System ONE 전체에서 동일 정확도의 loop/latency 감소를 통합 입증하지 않았다고 정리했다. **LITERATURE (11편 전체, 원문 검토 §0):** 11-11 원문 검토도 우리 H-COMPUTE를 직접 시험한 논문은 없다고 정리한다.
