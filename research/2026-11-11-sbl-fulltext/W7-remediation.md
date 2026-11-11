# 보완 — STRUCTK25 원문 정독, 위치 보완, 표기 점검, 재집계

> 2026-11-11 SBL 원문 검토 워크플로에서 worker가 쓴 보고를 마스터가 원문 대조로 검수해 옮겼다. 종합은 [2026-11-11-sbl-fulltext-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext-review.md)에 있다.
>
> `fcl-sbl-fulltext-20261111/...` 경로는 저장소 밖 호스트 작업 폴더다. 원문은 저작권 때문에 저장소에 넣지 않았다. 판본과 해시는 [evidence.json](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/evidence.json)에 있다.
>
> 이 문서는 리더 검증(FAIL) 뒤의 보완 보고다. STRUCTK25 원문 확보, ELDER26·MICONI25·SWAMI23 위치 보완, 표기 점검, TEM20 재집계, CHU25 쪽수 확인을 담는다. §2의 줄번호는 정정·머리말을 붙이기 전 원 보고 기준이다.

---

## 보완 보고: STRUCTK25 원문 확보 + 과제 B·C

전제: 하위 worker 3명을 띄웠으나 세션 한도로 즉시 중단되어 과제 B·C는 모두 직접 수행했다. 스크립트는 `_scripts/structk25/`에 있다. `_scripts/B2`, `_scripts/B3`의 스크립트 5개는 중단된 하위 worker가 남긴 것이며 쓰지 않았다. git은 건드리지 않았고 .md는 0개다.

### 1. 과제 A: STRUCTK25

#### 1.1 접근 증거

| 항목 | 값 |
|---|---|
| 대상 | https://link.springer.com/article/10.1007/s10462-025-11270-2. VoR(Version of record 2025-06-04), OA CC BY-NC-ND 4.0. PDF가 아니라 HTML이다. |
| 경로 | 사용자 Paseo 브라우저의 열려 있던 탭(browserId b8895c52-2e6f-44ab-ac11-5382d63cf881, 페이지에 "You have full access to this open access article"). curl 봇월은 건드리지 않았다. |
| 추출 대상 T | `document.querySelector('article').innerText`, 가공 없음. 캡처 2026-11-11 약 08:05–08:08 UTC. |
| 크기와 해시 | 브라우저가 계산한 H = `fac2773e55390c00acf58009384a567f3626d37ad37390c7956064d9315a60f7`. 111,957자, 112,612 bytes, 1,362줄, 14,449단어. astral 문자·고립 surrogate·CR 없음, NBSP 365개, TAB 6개. |
| 전송 | 30,000자 4청크(offset 0/30000/60000/90000)를 evaluate 결과로 받았다. 청크 SHA-256 4/4와 재조립 전체 SHA-256이 브라우저 값과 일치한다. |
| 저장 | worker transcript JSONL을 `python3 -I`로 파싱해 저장했다(손으로 다시 치지 않음). `fcl-sbl-fulltext-20261111/STRUCTK25/fulltext.txt`의 `sha256sum` = H(일치). `wc -w` = 14,449. `LC_ALL=C`에서는 14,292로 나오는데 NBSP 때문이다. |
| 포함 범위 | 초록(0426–1667), 본문 §1–§6(2231–71280), 참고문헌 169개 전부(71281–108779, Crossref 169와 일치), 식 (1)–(6)의 LaTeX 원문, Fig. 1–6 캡션 텍스트, back matter. 머리글 0–425와 추천 블록 1668–2230("Similar content…")은 논문이 아니다. |
| 표 | `<article>` 안에는 Table 1–5의 캡션과 "Full size table" 링크만 있다. 표 본문은 같은 브라우저에서 /tables/1–5를 same-origin fetch(HTTP 200)해 `fcl-sbl-fulltext-20261111/STRUCTK25/tables_from_springer_html.txt`로 따로 저장했다(17,149자, 2,554단어, SHA-256 `d2001b82e9584f9017250850012f53ae4f9ebfd82839df09f0bf33657c3f6fa8`, 브라우저 해시와 일치, 푸터 포함). |
| 그림 | 이미지는 보지 않았다. 원문에는 Fig. 1–6만 있고 Fig. 7–8은 없다(W5의 "Fig 7–8 미독"은 오류였다). |
| 갱신 | `fcl-sbl-fulltext-20261111/STRUCTK25/access.json`: status "fulltext", words 14449, chars, 브라우저 해시, 청크 해시, `fulltext_scope`(오프셋·표·그림·식·참고문헌 포함 여부), `sections_read`, `supplementary`(없음), `attempted_routes` 12→13건. 기존 12건과 `webfetch_evidence.txt`는 그대로다. 고정 15키는 모두 유지했다(pages는 null이고 사유는 `pages_null_reason`에 있다). `fcl-sbl-fulltext-20261111/STRUCTK25/SHA256SUMS.txt`는 13→15행이고 `sha256sum -c` 15/15 OK다. |
| 미수정 | STRUCTK25/extraction.json은 W5의 WebFetch판 그대로다. 이제 구판이므로 통합 때 이 보고로 대체해야 한다. |

#### 1.2 STRUCTK25 보고 (원문 기준 재작성)

범례: 별도 표기가 없으면 [LITERATURE]이고 위치(§, Fig., Table)를 병기했다. "(집계)"는 우리가 fulltext.txt와 표 파일에서 센 수다. [PROPOSAL]은 우리 추론이다.

**과제 A-6 질문 (i)–(vi) 답**
- (i) 서술적(narrative) taxonomic survey이고 체계적 리뷰가 아니다. 근거:
  - Methods 절이 없다(0회).
  - PRISMA, inclusion, exclusion, criteria, database, Scopus, Web of Science, 단독 단어 "search"가 모두 0회다(집계).
  - "systematic"은 §5.1 제목 "Systematic generalization"에서 한 번 나온다. 방법 서술이 아니다.
  - 자기 서술은 "survey", "comprehensive review", "the first comprehensive review of brain structural knowledge and cognitive computational models as a bridge"다(Abstract, §1, §6).
  - "Literature review"는 CRediT 역할로만 나온다(Contributions).
- (ii) "schema" 정의가 영역마다 다르다.
  - 신경 기질: §1 "highly structured and abstract dynamic memories distilled from multiple scenarios or recurring environments (Ghosh and Gilboa 2014)". §2.2 "abstract common patterns across multiple tasks or environments".
  - 계산 모델: §3.2 "abstract commonalities from past experiences, enabling generalization, transfer learning, and flexible cognition".
  - AI 응용: 별도 정의가 없다. §4.1은 계산 모델의 abstraction mechanism을 채택한 정도다. §4.2–4.3(traditional)에는 "schema"가 0회다(절별 집계). 다른 용법은 §5.3의 motor schemas와 §5.4.1의 "schema-based diagnostic models"(느슨한 용법)다.
- (iii) §3.2 계산 모델 목록.
  - 본문 대표 모델, explicit(§3.2.2): TEM(독립 RNN 모듈), SMP(visual slots), Stoewer 2023a(multi-scale SR의 coarse-grained SR), CSCG(transition graph).
  - 본문 대표 모델, implicit: manifold-based(Goudar 2023; Driscoll 2022), subpopulation-based(Yang 2017; Dubreuil 2022).
  - Table 3에서 schema 유형인 행은 15개다(집계). explicit 11개는 Hwu&Krichmar 2018, TEM, SMP, CSCG, DR(Piray&Daw), Stoianov 2022, Stoewer 2023a, Bakermans 2023, Kymn 2024, Wientjes&Holroyd 2024, Whittington 2025다. implicit 4개는 Yang 2017, Dubreuil 2022, Goudar 2023, CML(Stöckl 2024)이다.
- (iv) §5.2의 열린 문제는 세 가지다: catastrophic forgetting, 대규모 재학습 없는 효율적 적응, knowledge fusion. 뇌 메커니즘으로는 local synaptic plasticity, experience replay, slow-fast memory integration을 든다. 지침은 4개다: 계산 모델 개발, sparsity 기반 선택 갱신, generative replay + sleep-inspired consolidation, multi-stage 계층 기억 통합. 한계는 stability-plasticity tradeoff, 계산 비용, 그리고 "memory integration complexity … remains an open challenge"다.
- (v) 지속 학습에서 schema가 학습 규칙을 제어하는 통합 아키텍처는 언급하지 않는다. §5.2에서 "schema"는 2회뿐이고 둘 다 "cognitive maps and schemas" 병렬 표현이다. 가장 가까운 이웃 문장은 넷이다.
  - §2.2 / Fig. 3b(신경 수준): mPFC가 입력과 기존 schema의 일치도를 감지한다. 일치가 높으면 MTL의 instance 기반 consolidation을 억제하고 rapid schema updating을 촉진한다. 불일치면 top-down 영향을 줄여 MTL이 encoding을 주도한다.
  - §3.2.1(가이드): "The schemas are updated if any error occurs, and larger errors may prompt the model to create new schemas."
  - §4.1 / Table 4: Gao 2021 SMART는 연속학습이 연구 초점인 유일한 행이다(abstract structure mechanism, NCC가 장·단기 forgetting을 완화). 수치는 없다.
  - §5.4.1(윤리 절의 한 문장): "incorporating adaptive schema refinement through continuous learning can enable models to dynamically update their representations".
- (vi) §3.3은 표 없는 산문이다. 비교표는 Table 3이다. Table 4와 5는 HTML에서 §3.3 앞뒤에 놓여 있지만 본문 인용은 §4.1과 §4.2다. 표 내용은 필드 8과 R1에 정리했다.

**필드 1. 서지**
- Yu Y, Yan Y, Jin Y, "Structural knowledge: from brain to artificial intelligence", Artif Intell Rev 58, 264 (2025). 머리글은 "Volume 58, article number 264 (2025)"이고 issue 9는 Crossref 값이다. DOI 10.1007/s10462-025-11270-2.
- 날짜: Accepted 12 May 2025, Published 04 June 2025, Version of record 04 June 2025(About this article). received는 표기가 없다.
- 소속(Authors and Affiliations): College of Information Science and Technology, Donghua University, Shanghai(Yu, Jin). School of Engineering, Westlake University, Hangzhou(Yan, Jin). "Yingchao Yu and Yuping Yan have contributed equally"(Author notes). 교신저자는 Yaochu Jin이다.
- 펀딩(Acknowledgements): Key Project of Zhejiang Provincial Natural Science Foundation (D25F020001). Conflict of interest 없음(Ethics declarations).
- CRediT(Contributions): Yu는 Literature review 등과 visualization, Yan은 conceptualization·supervision 등, Jin은 writing—review & editing과 project administration이다.
- Data/Code availability 문구와 supplementary는 없다(집계 0). 라이선스는 CC BY-NC-ND 4.0이다(Rights and permissions).

**필드 2. schema 정의와 위치**
- 구조 지식은 정식 정의가 없다. "Structural knowledge in the brain mainly includes two types: cognitive maps and schemas"(§1)가 전부다.
- 세 영역 정의는 위 (ii)와 같다.
- 신경 기질(§2.2, Fig. 3, Table 2의 schema 6행):
  - HPC: 초기 형성, retrieval, 수면 중 replay로 안정화, 충돌 감지.
  - mPFC: 안정 schema로 통합, 갱신.
  - 두 경로: mPFC-MTL은 schema가 완성된 경우, mPFC-HPC는 부분 형성된 경우(Fig. 3a).
  - Table 2의 schema 6행: El-Gaby 2024(mPFC goal-progress cells), Schapiro 2016, McKenzie 2014, Zhou 2021(OFC), Zeithamova&Preston 2010, Audrain&McAndrews 2022.
- 관계:
  - §2.3 "schemas can be viewed as generalized extensions of cognitive maps (Farzanfar et al. 2023)", "cognitive maps represent concrete configurations, whereas schemas encode abstract structures generalized from diverse experiences".
  - §3.3 "From a unified perspective, schemas function as broader and more abstract cognitive structures, while cognitive maps serve as their instantiations in specific environments or tasks".
  - §3.3 표현 방식: cognitive map 모델은 explicit, schema 모델은 explicit 또는 implicit priors.
- 연속/이산: schema 분류축이 아니다. mechanism 이름에 "continuous attractor-based"와 "discrete slots"가 나올 뿐이다(§3.1.3).
- 분량(집계): §3.1(cognitive map) 약 11.4천자, §3.2(schema) 약 6.7천자. Table 3은 cognitive-map-only 8행, schema-only 4행, 둘 다 11행이다.

**필드 3. 아키텍처**
- TEM(§3.1.2, Fig. 5a): "The HPC components (H, A) are responsible for updating and retrieving associative memory (M_t), while the MEC component (G) learns structural representations and generates future spatial encodings (g_{t+1})".
- SMP(§3.1.2): 여러 RNN으로 MEC를 모사하고 외부 메모리 모듈을 HPC로 쓴다.
- CSCG(§3.1.2, Fig. 5c): 관측 특징을 컨텍스트별로 복제하는 higher-order graph다.
- schema 저장 위치(§3.2.2): TEM은 독립 RNN 모듈, SMP는 visual slots, Stoewer 2023a는 coarse-grained SR, CSCG는 transition graph다.
- 모델별 frozen/trainable과 fast/slow 구분은 서술이 없다. §5.2에 일반 서술만 있다: "Short-term memories are rapidly encoded in the HPC … gradually consolidate into the neocortex".

**필드 4. 학습 규칙**
- Eq.(1)–(2) TEM(§3.1.2): g_{t+1} = G(g_t, a_{t+1}, A(M_{t−1}, x_t)), M_{t+1} = H(g_{t+1}, x_{t+1}, M_t).
- Eq.(3) 상태가치 V_π(s) = E_π[R_s^a + γV_π(s_{t+1}) | s_t = s]. Eq.(4) 최적가치 V*(s) = max_π V_π(s). Eq.(5)–(6) 행렬형 v = Σγᵗ Tᵗ r = S r, S = Σγᵗ Tᵗ(§3.1.2, SR 설명).
- 그 밖의 규칙 서술:
  - Hebbian(association-based, TEM과 Chandra 2025, §3.1.3).
  - CSCG는 EM + hierarchical clustering(§3.1.3).
  - predictive coding은 "minimizing prediction errors or through surprise-driven learning"(§3.1.3).
  - TEM의 schema 학습은 "a self-supervision term in the loss function"(§3.2.2).
  - SMP는 self-consistency constraints(§3.2.2).
  - SMART는 NCC(§4.1).
- outer loop와 within-lifetime의 구분은 서술이 없다.

**필드 5. 형성·선택·적용·개정**
- 뇌(§2.2, Fig. 3b·3c): 위 (v)의 mPFC-MTL 경로와, mPFC-HPC 경로의 prediction error. "Large errors may trigger the formation of new schemas, while minor discrepancies serve to fine-tune existing ones".
- 계산(§3.2.1):
  - schema learning과 schema-based adaptation 2단계. 적응은 맥락 단서로 retrieval → 여러 schema 통합으로 예측·행동 → 오류 시 갱신.
  - 도전 과제: 일반화 대 세부 보존, stability-plasticity, 계산 복잡도, 모호 상황의 retrieval, task flexibility, 동적 환경.
- "assimilation"과 "accommodation" 명사는 0회다. "assimilate"(동사)는 §1에서 LLM이 구조 지식을 암묵적으로 흡수한다는 비피아제식 용법으로 1회 나온다. novelty·merge·split도 본문에 없다.

**필드 6. 지속성**
- §2.2: "during rest and sleep, the HPC enhances the long-term stability of schemas by replaying stored memories (Durrant and Johnson 2021)". 경로 설명 끝에 "lifelong schema learning"이 나온다.
- §4.1: SMART의 NCC가 장·단기 forgetting을 완화한다(Gao 2021, 수치 없음).
- §5.2 지침은 인용 없는 일반 서술이다(generative replay, sleep-inspired consolidation, multi-stage 기억).
- W5의 "Swaminathan 2023의 ICL은 activation 수준이다"는 STRUCTK25 원문에 없는 문장이다(우리가 SWAMI23에서 가져온 것). 이 필드에서 철회하고 [PROPOSAL]로만 쓴다.

**필드 7. 과제·결과**
- 자체 실험·결과가 없다. 본문의 수는 인용 연도뿐이다. Table 1–5는 정성 비교다.

**필드 8. 신경과학 대응**
- Table 2는 26행(cognitive map 20, schema 6)이다. 열은 Work, Structural knowledge type, Neural substrate, Function이다(집계).
- Table 3의 "Neural substrate" 열이 모델을 뇌 구조에 대응시킨다. Hwu&Krichmar 2018은 mPFC/vHPC/dHPC, TEM은 HPC/LEC/MEC/place·grid·border·object-vector cells다.
- Table 3은 23행(1997–2025)이다. cognitive-map taxonomy는 structure-based 9, prediction-based 11, "–" 3이다. schema taxonomy는 explicit 11, implicit 4, "–" 8이다(집계).
- 증거 수준은 문헌 종합이고 저자 자체 검증이 없다. 두 경로 도식(Fig. 3)은 hedging 없이 단정적으로 쓰였다(§2.2).

**필드 9. 한계·미제시**
- 서베이 자체의 한계 진술은 없다. "limitation" 12회는 모두 §5.1–§5.3의 "Potential limitations"로, 제안한 연구 방향의 한계다(집계).
- 미제시: 선정 방법, 정량 종합과 head-to-head 비교, schema→학습 규칙 연결. "halting", "test-time", "hypernetwork", "fast weights", "meta-learning", "EWC", "elastic"이 모두 0회다(집계).

**필드 10. 클레임 표**

| ID | 주장 | 판정 | 위치 | 근거 |
|---|---|---|---|---|
| SK1 | 뇌 schema를 AI 학습 모델로 연결한 연구를 "체계적으로" 정리 | PARTIAL(유지) | Abstract, §1, 절 구성, §6 | 뇌 → 계산 모델 → AI 응용 taxonomy로 조직된 것은 사실이다. 검색·선정 프로토콜이 없다. |
| SK1a | 저자·게재처(Yu, Yan, Jin; AI Review 2025) | CONFIRMED | 머리글, back matter | 일치한다. |
| SK1b | schema-based learning을 신경망 아키텍처·학습 메커니즘으로 다룸 | PARTIAL(유지) | §3.2, §4.1, Table 3–4 | taxonomy 수준이다. 식은 TEM(Eq.1–2)과 SR(Eq.3–6)뿐이고 둘 다 cognitive map 모델이다. §3.1이 §3.2보다 길고, Table 3은 map-only 8행 대 schema-only 4행이다. |
| SK2 | schema가 이후 학습 규칙을 제어하는 연속학습 open problem을 서술 | NOT-FOUND(유지) | §5.2 | (v)의 이웃 문장 네 가지는 있으나 §5.2에 schema–학습규칙 연결은 없다. |
| SK3 | assimilation/accommodation 틀 사용 | NOT-FOUND(유지) | 전체 | 필드 5 참조. 가장 가까운 것은 오류 크기에 따른 create 대 fine-tune 서술이다(§2.2, §3.2.1). |

**필드 11. FCL 연결 [PROPOSAL]** (이 리뷰는 FCL 메커니즘이 작동한다는 증거가 아니다)
- DQ1: explicit(모듈, slot, graph)과 implicit(공유 subspace)의 설계 공간 지도로 쓴다(§3.2.2, Table 3의 11 대 4). retrofit LM에는 implicit-subspace 계열이 맞아 보이나 리뷰에 우열 증거는 없다 [OPEN]. explicit graph 계열은 Melete 교훈상 주의가 필요하다.
- DQ2: §3.2.1의 retrieve → integrate → act → update on error가 context-controller 명세의 골격이다. §2.2의 두 경로는 controller의 두 모드로 읽을 수 있으나 증거는 없다.
- DQ3: 오류 크기 임계값이 fine-tune과 create를 가른다(§2.2, §3.2.1). 실험은 mismatch 강도 sweep으로 retention과 샘플 효율을 잰다. 실패 양상은 임계값 보정과 잡음-구조 novelty 혼동이다.
- DQ4: §5.2의 sparse update, generative replay, sleep consolidation, slow-fast 통합은 HOPE/CMS + Sleep과 구호 수준에서만 겹친다. 구체 메커니즘은 CR47(SMART)과 CR132(Stoianov)를 읽어야 한다.
- DQ5: 리뷰가 다루지 않는다(adaptive depth, halting, test-time memory 0회). MoE + compositional attention을 selective activation으로 언급할 뿐이다(§5.1).
- DQ6: "structure learning이 이후 online learning을 줄인다"(§3.1.1)와 CSCG의 "efficient learning of new rooms"(§3.2.2)는 수치가 없다. 원문(CR50, CR58)을 봐야 한다.
- DQ7: SMART/NCC는 단서일 뿐 증거가 아니다.
- DQ8: explicit/implicit, structure-/prediction-based 같은 축을 baseline 분류에 빌릴 수 있다. CogEval(Table 4, Momennejad 2024)은 LLM의 planning과 cognitive map 평가이고 schema 전용이 아니다.
- 이 리뷰 사용 시 위험: 선택 편향, 실증 부재, 참고문헌 서지 오류(아래 변경 목록 마지막 3행).

**필드 12. 재현·프로토타입**
- 재현할 대상이 없다(코드·데이터 없음). 식 (1)–(6)은 LaTeX 원문으로 확보했다. 후보 구현(SMART, CSCG, Stoianov)이 12GB GPU나 CPU에서 가능한지는 원문을 읽기 전에는 [OPEN]이다.

**R1. 분류축**
- 유형: cognitive map / schema.
- cognitive map 모델: structure-based(TEM, SMP) / prediction-based(SR, CSCG)(§3.1.2, Fig. 4).
- schema 모델: explicitly learned / implicitly emergent(manifold-based, subpopulation-based)(§3.2.2).
- abstraction mechanism 9종(§3.1.3, §3.2.3, Fig. 6):
  - cognitive map 쪽: continuous attractor-based, association-based(binding, Hebbian), graph-based, SR-based, predictive coding, behavior-map co-evolution.
  - schema 쪽: abstract structure, subspace-based, subpopulation-based.
- AI 모델(Table 4, 13행):
  - 열은 Year / Work / Research Focus / Key Technology / Abstraction mechanism / AI Paradigm이다. 연도 분포는 2018 1, 2021 2, 2023 1, 2024 9다(집계).
  - 초점은 navigation·planning, LLM의 ICL과 평가, role-filler binding, graph schema transfer, 연속학습(SMART 1행)이다.
- AI 모델(Table 5, 23행):
  - 열은 Year / AI Model / Taxonomy / Structural knowledge role / Research focus / Key technology / Paradigm이다.
  - Taxonomy는 implicit embedding 12, KG 6, symbolic 3, KG+symbolic 2다(집계).
- 역할 열(Table 5)은 Performance / Generalization / Interpretability 세 가지다. §4.2.2 본문은 generalization과 interpretability 두 가지만 쓴다.
- Table 1은 Whittington 2022, Peng 2023, Wang 2024, You 2024, Bai 2024, Nie 2024, Bein&Niv 2025와 Ours를 비교한다.

**R2. 우리 9편 인용 여부** (CR 번호 = Springer `ref-CR<n>` = Crossref key. 표시 순서와 id 순서가 4곳에서 다르다: CR137, CR34/35, CR107/108, CR161–163)

| 논문 | STRUCTK25 | 위치 |
|---|---|---|
| SPENS24 | 아니오 | "Spens" 0회 |
| HWU20 | 참고문헌과 표에만 | CR71 "Hwu T, Krichmar JL (2018) … bioRxiv", DOI는 2019/2020판 `10.1007/s00422-019-00808-7`. Table 3 "Two-stream model" 행. 본문 0회. |
| CHU25 | 아니오 | NeurIPS 2025라 시점상 불가 |
| GOUDAR23 | 예 | CR57. §3.2.2, §3.2.3, Fig. 5d 캡션, Table 3 "RNN (Goudar et al. 2023)": schema, implicitly emergent, sequential learning, neural manifold, PFC. |
| ELDER26 | 아니오 | 2026이라 불가 |
| MICONI25 | 아니오 | "Miconi" 0회 |
| TEM20 | 예 | CR148 Whittington 2020. §3.1.2(Eq.1–2), §3.1.3, §3.2.2, Fig. 5a, Table 3. 본문 7회와 표 1회(집계). |
| KUMAR26 | 아니오 | 2026이라 불가 |
| SWAMI23 | 예 | CR135. §4.1 본문 1회, Table 4 행. |

- Table 4에서 Swaminathan은 Year 열이 2024이고 괄호 안 인용과 참고문헌은 2023이다. 연도가 어긋난다.
- 우리 목록에 없는 구현 후보의 Springer 키(CR47, CR58, CR50, CR132, CR20, CR95, CR141, CR33/34/155, CR150/10/79/19, CR29, CR129)는 DOM id로 모두 확인했다.

**R3. 열린 문제(§5)**
- 5.1 systematic generalization: 문제는 compositional generalization 부족과 OOD generalization 한계다. 원리는 hierarchical organization과 decoupled·compositional representation이다. 지침은 계산 모델 개발, modular AI 아키텍처, hierarchical latent space, MoE + compositional attention의 selective activation이다. 한계는 모델 복잡도와 국소 최적화 필요다.
- 5.2 lifelong learning: 위 (iv)와 같다.
- 5.3 embodied: 문제는 perception-action loop, 멀티모달 통합, 운동 제어 학습이다. 지침은 Neural SLAM, CLIP, Sim2Real을 든다.
- 5.4 윤리: 편향(cognitive-map 모델의 구조 편향, schema 모델의 abstract representation bias)과 프라이버시(inference attack, differential privacy, homomorphic encryption, federated learning)를 다룬다.
- schema가 어떤 파라미터를 언제 학습할지 제어한다는 서술은 없다. 연속학습 알고리즘 이름(EWC, replay buffer, complementary learning systems)은 본문에 나오지 않는다. 마지막은 McClelland 2013 참고문헌 제목에만 나온다.

**R4. SPECTRUM26과의 상호 인용**
- STRUCTK25는 SPECTRUM26을 인용하지 않는다. STRUCTK25 accepted 2025-05-12, SPECTRUM26 received 2025-10-27이라 불가능하다. 본문과 참고문헌에서 Samiei, Precup이 0회다.
- SPECTRUM26은 STRUCTK25를 인용하지 않는다. 최종 PDF와 v2에서 Yingchao, Yaochu, "Structural knowledge", "10462"가 모두 0회다.
- DOI 수준 공통 참고문헌 9개는 양쪽 참고문헌 텍스트를 대조해 재확인했다: Van Kesteren 2012, Van Kesteren 2013, Ghosh&Gilboa 2014, Gilboa&Marlatte 2017, Audrain&McAndrews 2022, Bein&Niv 2025, Richards 2014, Bartlett(STRUCTK25는 1995판, SPECTRUM26은 1932로 표기, DOI `10.1017/CBO9780511759185` 동일), Schank&Abelson 1977.
- Rumelhart 1980은 이름·연도·제목만 일치한다.

#### 1.3 W5 판정 대비 변경 목록

| 항목 | 판정 | 근거·위치 |
|---|---|---|
| 접근 증거(status partial, WebFetch 매개, Table 5와 Fig 7–8 미독) | 수정 | status fulltext. Table 5를 읽었다. Fig. 7–8은 존재하지 않는다. |
| SK1 PARTIAL | 유지 | 위 (i). |
| SK1a, SK1b | 유지 | SK1b에 집계를 보강했다(§3.1 대 §3.2 분량, Table 3 행 분포). |
| SK2 NOT-FOUND | 유지 + 보강 | 이웃 문장 네 가지: §2.2 Fig. 3b, §3.2.1, §4.1 SMART, §5.4.1. |
| SK3 NOT-FOUND | 유지 + 정정 | "assimilation/accommodation 용어 없음"에서 "assimilate"(동사) 1회(§1, LLM 용법)를 명시. |
| 필드 1 | 유지 | CRediT, 라이선스, 데이터·코드 문구 없음 확인을 보강했다. |
| 필드 2 | 수정 | 신경·계산·AI 세 영역 정의를 분리했다. 연속/이산 문구는 §3.1.3의 mechanism 이름을 인정하되 schema 축은 아니라고 보완했다. |
| 필드 3 | 유지 | SMP와 schema별 저장 위치(§3.2.2)를 보강했다. |
| 필드 4 | 수정 | W5는 "Eq(3)–(6)은 v=S r"이라고만 적었다. 실제는 Eq.(3) 상태가치, (4) 최적가치, (5)–(6) 행렬형이다. SMP의 self-consistency를 추가했다. |
| 필드 5 | 유지 | |
| 필드 6 | 수정 | "Swaminathan 2023의 ICL은 activation 수준" 철회(원문에 없음). §2.2의 "lifelong schema learning"을 추가했다. |
| 필드 7, 8 | 유지 | |
| 필드 9 | 수정 | "limitation" 12회는 모두 §5의 제안 방향 한계이고 서베이 자체 한계 진술은 없음을 확정했다. |
| 필드 10 | 유지 | |
| 필드 11 | 유지 | 위치만 갱신했다. 위험 항목에 참고문헌 오류를 추가했다. |
| 필드 12 | 유지 | |
| R1 | 수정 | 역할 열에 Performance를 추가했다(Table 5). |
| R2 | 유지 | 본문 횟수·위치를 보강했다. Table 4의 Swaminathan 연도 불일치를 추가했다. |
| R3 | 수정 | §5.1·§5.2 첫 지침("계산 모델 개발")이 W5에서 빠져 있어 추가했다. |
| R4 | 유지 | 양방향 재확인. |
| 새로 확인(W5가 소형 모델 주장이라 채택 안 했던 건) | 신규 | 참고문헌·인용 오류 세 건. ① §5.4.2 "differential privacy (Van Kesteren et al. 2013)": 인용된 논문은 "Differential roles for medial prefrontal and medial temporal cortices in schema-dependent encoding"(신경과학)이다. ② Hwu 참고문헌은 "bioRxiv"인데 Springer DOI다. ③ Atienza 2024는 arXiv:2402.02219에 Biol Cybern 2015형 DOI(`10.1007/s00422-015-0644-8`)가 붙어 있다. 이 리뷰의 2차 인용은 원논문 확인 전에는 단정하지 않는 것이 안전하다. |

### 2. 과제 B 교체 목록

`code/…` 위치는 해당 repo의 상대경로다. "[CODE]"는 논문 사실이 아니라 코드에서 읽은 사실이다.

#### 2.1 ELDER26 (reports/W3.txt 줄번호)

**필드 3**
- (62줄) "고정된 ImageNet VGG-16(keras 3.5.0, GAP) → 프레임 4장 × 512 = 2048 → 2×3 tanh → 3 클래스(NB/SB/HB)" → 고친 문장:
  - ImageNet 사전학습 VGG-16(keras v3.5.0, include_top=False 후 GlobalAveragePooling2D로 프레임당 512 특징)을 임베딩 생성기로만 쓴다(Methods > VGG-16).
  - 프레임은 4장이며 경계 전 2, 후 2다(Results 첫 문단, Methods > Frames). 각각 독립 통과시켜 4×512로 이어 붙인다(Methods > Frames, Fig. 3a 범례).
  - 이어 은닉층 2개(각 3 interneuron, tanh)가 3 클래스 NB/SB/HB를 분류한다(Methods > Top models, Fig. 2a 범례).
  - "2048"은 원문에 없고 4×512의 우리 곱셈 값이다.
- (63줄) "ENN과 MLP의 구조는 동일" → 유지+위치: Methods > Top models "explicitly identical in architecture (number of hidden layers = 2, … = 3, activation function = tanh)", Methods > Backpropagation networks "(identical to ENNs)".
- (64줄) "fast/slow 구분은 없다. 제목의 'plastic'은 학습 가능하다는 뜻이다." → 고친 문장:
  - 모델에 fast/slow 가중치 구분은 없다(ENN과 MLP 동일 구조, Methods > Top models).
  - 다만 Introduction은 schema를 "central logic changes slowly … unconstrained degrees of freedom are allowed to vary rapidly"로 개념화한다(Introduction).
  - "plastic = 학습 가능"은 우리 해석이다 [PROPOSAL].
- (65줄) "불변성은 제약이 아니라 결과로 나온다" → 고친 문장: 불변성은 관찰 결과로 서술된다(Results "Hierarchical networks converge to a stable schema robust to further training", Fig. 3b). 원인 설명은 Discussion의 "each sub-concept neuron computes an effectively digital 'AND' operation on its upstream differentia neurons"다. "제약이 아니라 결과"라는 대비는 우리 요약이다 [PROPOSAL].

**필드 4**
- (67줄) "비gradient, layer-wise" → 유지+위치: Methods > Top models > Essence neural networks "trained using a non-gradient-based schema". layer-wise는 differentia(1층) → subconcept(2층) → concept(출력) 순 서술이다.
- (68줄) "class별 Ward 군집화" → 논문은 "unsupervised learning divides concepts into subconcepts"까지만 쓴다(같은 절). Ward는 [CODE] `code/bdENN/enn/train_enn.py:495`(`cl_metric = 'ward'`).
- (69줄) "differentia: 쌍별 linear SVM, C=15" → 쌍별 linear SVM은 논문(같은 절). C=15는 [CODE] `code/bdENN/enn/learnBoundaries.py:22`(`'svm_cost_1': 15`).
- (70줄) "subconcept: … mult 8, C=1000, margin_ratio=inf, tanh로 거의 ±1 포화" → SVM 구성은 논문(같은 절). 수치는 [CODE] `learnBoundaries.py:23–26`(`margin_ratio: np.inf`, `svm_multiplier_1: 8`, `svm_multiplier_2: 8`, `svm_cost_2: 1000`). "tanh로 거의 ±1 포화"는 논문에 없고 우리 해석이다 [PROPOSAL].
- (71, 72줄) "concept: SVM", "y = w·x + b, tanh" → 유지+위치: Methods > Essence neural networks와 Methods > Top models(`y = tanh(w·x + b)`).
- (72줄) "equalize_weights ±1e-4·max|w|" → 논문에 없음. [CODE] `code/bdENN/enn/enn_svm.py:288`(not use_exact일 때 호출), `:309` 정의, `:317` `mx_value = np.max(np.absolute(self.weights))`, `:323, :334` `np.isclose(|w|, |w_i|, atol=.0001*mx_value)`. 즉 절댓값이 1e-4·max|w| 이내인 가중치를 같은 값으로 맞춘다.
- (73줄) "num_subclasses=3은 hiddenLayerSize를 그대로 넘긴 값" → 논문은 "2 hidden layers (differentia and subconcept), each with 3 interneurons"(Methods > Essence neural networks). 코드는 `scripts/VariableTrainingData.py:74, :92`(`hiddenLayerSize = 3`; `lB.main_0(xTrain, yTrain, 0, hiddenLayerSize)`)와 `enn/learnBoundaries.py:20, :103`이다. "클래스당 subconcept 1개, differentia C(3,2)=3"은 우리 해석이다 [PROPOSAL].
- (74줄) "backprop 기준선 sklearn 1.5.2 MLPClassifier(adam, max_iter 10000, 나머지 기본값)" → 유지+위치: Methods > Backpropagation networks("scikit-learn 1.5.2 MLPClassifier", "max_iter: 10000", "solver: 'adam'", learning_rate_init와 regularization은 defaults). "VariableTrainingData.py는 max_iter=1000"은 [CODE] `scripts/VariableTrainingData.py:84`다. 10000은 `VariableSplitsAndReproducibility.py:76`, `NoiseInjection.py:82`, `ParameterRobustness.py:117`, `ConceptSpaceRetention.py:72`, `PlotMaker.py:197`에 있다.
- (76줄) "'데이터 증가'는 1%…100% 10개 지점에서 서로 다른 무작위 부분집합으로 처음부터 재학습, 시드 1개" → 논문에는 지점 수와 비율이 없다(Results "Hierarchical networks converge to a stable schema…"과 Fig. 3b 범례는 "increasing amounts of data"만 쓴다). 코드 사실이다.
  - [CODE] `scripts/VariableSplitsAndReproducibility.py:160–167`: `minSplit = 0.01`, `maxSplit = 1`, `nSplits = 10`, `np.linspace` 후 2자리 반올림 → 0.01, 0.12, 0.23, 0.34, 0.45, 0.56, 0.67, 0.78, 0.89, 1.0. `nSeeds = 1`.
  - `:174–179`: `train_test_split(train_size=split, random_state=globers["randomSeed"], stratify=yAll)`. randomSeed는 `:62`에서 9다.
  - 같은 random_state라서 "서로 다른(비중첩) 부분집합"인지는 코드만으로 확정할 수 없다. "지점마다 train_size만 바꾼 stratified 부분집합(같은 seed 9)"으로 고친다.

**필드 6**
- (80줄) "파라미터뿐이다. replay와 consolidation은 없다. ENN은 전체 학습 데이터가 한 번에 필요하다." → 고친 문장:
  - replay는 원문에 0회다. sleep·replay식 공고화 절차는 없다.
  - 다만 원문은 "schema consolidation"을 ENN의 hidden 가중치 조기 고정을 가리키는 말로 쓴다(Introduction Fig. 1 범례, Results "Hierarchical networks are robust to parameter noise and feature perturbation", Results "Hierarchical schema is distillable into a concise interpretable circuit").
  - catastrophic forgetting은 Introduction의 문제 틀로만 나온다(McCloskey & Cohen 1989 인용). 망각 측정 실험은 없다.
  - "ENN은 전체 학습 데이터가 한 번에 필요하다"는 논문 문장이 아니다. Methods > Essence neural networks의 label별 그룹화와 SVM 서술에서 읽은 우리 추론이다 [PROPOSAL].

**필드 8**
- (107줄) "Zheng 2022 MTL 기록과 비교한다. Boundary cell 42개/105 trials, Event cell 36개/30 trials이다." → 수치는 맞고 단위가 불명확했다. Fig. 2h 범례(Introduction의 Fig. 2 범례): "Average boundary-aligned firing rate of Boundary (on all SB and HB trials, 42 cells, 105 trials) and Event (on all HB trials, 36 cells, 30 trials) cells". 즉 Boundary cell 42개를 SB·HB 전 trial 105개에서, Event cell 36개를 HB 전 trial 30개에서 평균한 발화율이다. early/late 구분 기준은 경계 후 220 ms다(같은 범례). 영상은 신경 기록 때 환자가 본 것이다(Results 첫 문단, Zheng et al., 2022).
- (108줄) "근거 수준은 raster와 평균 발화 산점도의 정성적 유사와 B→E AND 게이트 가설" → 위치: raster는 Fig. 2f–g, 평균은 Fig. 2h, 은닉 뉴런과의 비교는 Fig. 5a(Results "Distinct populations of hidden neurons segregate into sequential layers in hierarchical models"). AND 게이트는 Discussion이다. 원문에 correlation, similarity, cosine이 0회라서 "적합도 통계 없음"은 사실이다(집계).
- (109줄) "계층 순서를 시간 지연에 대응시키는 것은 가정(저자 인정)" → 위치: Discussion "we additionally have to make assumptions regarding the relationship of temporal separation to layer ordering".
- (110줄) "Miconi & Kay 2025와 'qualitatively different'" → 위치: Discussion "…which is qualitatively different from schemata associated with accelerated transfer learning between closely related tasks … (Miconi & Kay, 2025)".

#### 2.2 MICONI25 필드 3 (W3.txt:217–226, 쪽은 proof PDF 쪽)

- "완전연결 RNN 200 tanh 유닛" → Methods "Network organization"(p.10): "containing n = 200 neurons (Fig. 1)", "the fully connected recurrent network acts according to the following equations", Eq.(2) r(t) = tanh(x(t)).
- "코드상 학습 파라미터 약 88.6k개" → 재현 수식: 입력 차원 37 = (2·15+1)+4+2다([CODE] `simple.ipynb` 코드 셀 2, `:61` `cs=15`, `:155` `ADDINPUT=4`, `:156` `NBSTIMBITS=2*cs+1`, `:157` `outputsize=2`, `:158`). 파라미터는 i2h 37·200+200 = 7,600, w 40,000, alpha 40,000, etaet 1, DAmult 1, h2DA 402, h2o 402, h2v 201(`:91–99`)이다. 합계 88,607이다. 논문 식의 파라미터(W_in, W_rec, A, W_out, W_mod, η)에는 value head(h2v)와 DA head의 2유닛 구성이 없다.
- "입력은 항목 2개(각 15비트)+reward+이전 응답" → 고친 문장:
  - 15비트 이진벡터는 Results(p.3) "stimuli are high-dimensional binary vectors (size = 15 …)"에 있다.
  - reward 입력은 Methods "Task settings"(p.11)에서 "reward signal registered by the network"와 step 3 "external feedback (reward)"로 확인된다.
  - "이전 응답" 입력과 go bit, bias, 에피소드 시계 입력은 논문 본문·supplement에 서술이 없다(검색 0). 코드뿐이다: [CODE] 코드 셀 2 `:338`(go), `:340`(bias), `:341`(numstep/eplen), `:342`(reward), `:346`(이전 행동 원핫).
  - ±1 코딩은 [CODE] `:238`(`randint(2, size=cs)*2−1`)이다.
- "출력은 2-way softmax, 스칼라 m(t), 코드에는 value head" → Eq.(3)–(4)(p.10) 및 "o(t) … probability distribution over the two possible responses", "m(t) is the (scalar-valued) neuromodulatory output". value head와 2-unit DA 구성은 [CODE] `:97–99`.
- "P(t) 200×200, 항목별 가소성 계수 A 200×200, 음수도 가능" → 논문은 "Wrec and A are the base weights and plasticity parameters … of the recurrent connections"(p.10)라고만 쓴다. 200×200은 n=200과 Hadamard 곱(Eq.1)에서 읽은 것이다 [PROPOSAL]. 음수 가능은 [CODE] `:93–94`(`.01*(2*rand−1)`, `requires_grad=True`)다.
- "H(t)와 활성은 매 trial 리셋, P(t)는 에피소드 시작에 리셋, main.ipynb 학습은 3번째 에피소드마다 리셋" → 논문 Methods "Task settings"(p.11) "we reset neural activations x(t), r(t) and Hebbian eligibility traces H(t) at the start of each trial (but not plastic weights P(t))". "Synaptic plasticity"(p.10) "P(t) is initialized to 0 at the beginning of each episode". Fig. 1d 범례(p.2) "Plastic weights are reset between episodes". Supp Note 3(supplement p.5) "we only reset plastic weights P(t) every third episode". 코드는 `main.ipynb` 코드 셀 2 `:81`(`nbepsbwresets = 3`), `:345`(`numepisode % nbepsbwresets == 0`)다. `simple.ipynb`에는 이 변수가 없다.
- "trial은 4 step" → Fig. 1c 범례(p.2)와 Methods "Task settings"(p.11): stimulus(step 1), response(2), reward(3), delay(4).
- "에피소드는 30 trial(인접쌍 20 + 전체쌍 10)" → Fig. 1d 범례(p.2), Results(p.3). 코드 `simple.ipynb` 코드 셀 2 `:65–67`.
- "목록 길이 논문 4~9 / 코드 range(4,9)=4~8, 시험은 8 항목" → Results(p.3) "between four and nine (inclusive); all results below use eight items". 코드 `simple.ipynb` `:59`와 `main.ipynb` `:64`(`range(4,9)` = 4~8)다.

#### 2.3 SWAMI23 (reports/W6.txt, 쪽은 NeurIPS PDF 쪽)

**필드 3**
- (29줄) "GINC는 토큰당 50 clone(ablation 10)" → 고친 문장:
  - §4.1 "Training"(p.5) "We train a single CSCG with 50 clones on the GINC dataset". 10 clone ablation은 Fig. 3B 캡션(p.6)과 Appendix C Table 1(p.15)이다.
  - "토큰당"은 CSCG 정의(§2.1, p.2 "Multiple values of z can result in the same observed x")에서 읽은 해석이다 [PROPOSAL].
- (30줄) "LIALT는 overallocation ratio 0.1/0.3/1.0/3.0" → §4.2 "Training"(p.7) "allocates its number of clones proportionally to the number of distinct contexts … 'overallocation ratio'". 비율 값은 Fig. 5와 Table 4–9의 행이다(Appendix D.3, p.18–19).
- (31줄) "N_latent와 vocab 크기는 원문에 없다" → 수정:
  - LIALT 토큰 vocabulary는 676개다(§4.2 "Training dataset", p.6 "a vocabulary of 676 tokens, created by random pairings of uppercase letters").
  - GINC vocabulary 크기와 학습된 CSCG의 N_latent 값은 숫자가 없다. N_latent는 §2.1(p.2)에 기호로만 나온다.
- (32줄) "test 시 T와 C 고정, E의 일부 행만 학습. E가 fast, T가 slow" → 위치: §2.2(p.2) "relearning just the emission matrix", "only performing local updates", §2.2.1 "We call this process fast rebinding", Algorithm 1(p.3)의 입력은 grounded schema {T, C, E0}이고 출력은 E^rb다. "T가 slow"는 원문 용어가 아니다 [PROPOSAL].

**필드 4**
- (34줄) "GINC 100 full-batch iteration, ε=1e-2" → §4.1(p.5) "100 full-batch EM iterations using a pseudocount [6] of ε = 10^−2". ε는 원문이 pseudocount라 부른다.
- (34줄) "LIALT 500 iteration + Viterbi 10회, ε=1e-6" → §4.2 "Training"(p.7) "500 EM iterations and a pseudocount of ε = 10^−6 … we run 10 iterations of Viterbi training".
- (34줄) "BPTT와 curriculum은 없습니다" → 유지(원문에서 BPTT, curriculum 0회).
- (35줄) "p_surprise(LIALT 0.1, dax 1/16)" → LIALT는 §4.2(p.8) "ε = 10^−6 and p_surprise = 0.1"이고 dax는 §4.3(p.9) "Algorithm 1 with ε = 10^−6 and p_surprise = 1/16"이다.
- (35줄) "해당 행만 EM으로 갱신(App.A 식), 완성은 max-product MAP(Alg.2)" → Algorithm 1 Step 5(p.3), Appendix A "Locally updating the emission matrix with the transition matrix fixed"(p.13). 완성은 §2.2.2(p.4) "performing MAP inference … We run the max-product algorithm"이고 Appendix B Algorithm 2(p.14)다.

**필드 7**
- (42줄) "GINC 모델 1개, (k,n) 칸당 2500 prompt" → §4.1(p.5) "with 2500 prompts for each setting (k, n)".
- "50 clone, k=10에서 0.971–0.978(±0.006)" → Appendix C Table 1(p.15)이 맞다. 50 clone 열, k=10 행의 n=0,1,2,4,8,16,32,64 값은 0.975, 0.977, 0.971, 0.974, 0.977, 0.977, 0.978, 0.978이고 괄호는 모두 0.006이다. 본문 Fig. 3B(p.6)가 "numerical values are reported in Appendix C, Table 1"이라고 연결한다.
- "10 clone에서 0.674–0.713(±0.018)" → 같은 표 k=10, 10 clone 열: 0.684, 0.705, 0.674, 0.713, 0.690, 0.689, 0.712, 0.690. 괄호는 0.018이다.
- "k=3은 0.44–0.53" → 같은 표 k=3, 50 clone 열 0.441–0.534. n=32 칸은 표에 "0.441 (0.0219)"로 인쇄되어 있다(원문 표기 이상).
- (43줄) "13개 알고리즘, instruction 5종, demonstration 20개, test 각 100 prompt" → §4.2 "Training dataset"(p.6) "13 list and matrix algorithms … each algorithm has five different instructions … followed by 10 input-output examples … For each instruction, the dataset contains 20 demonstrations". test는 §4.2(p.7) "Each test set contains 100 prompts"다. W6이 쓴 "13×5×20=1300은 유도값"은 맞다.
- (44줄) "1-EM, ratio 0.1/0.3/1.0/3.0: instruction형 0.00/0.20(0.08)/0.54(0.10)/0.89(0.06), example형 0.00/0.09/0.49/0.91" → Appendix D.3.1 "After a single EM iteration", Table 4(p.18, 본문 Fig. 5 [left] p.7)이다. 행: 0.1 → 0.00 (0.00)/0.00 (0.00), 0.3 → 0.20 (0.08)/0.09 (0.06), 1.0 → 0.54 (0.10)/0.49 (0.10), 3.0 → 0.89 (0.06)/0.91 (0.06).
- (45줄) "EM 수렴 시 ratio 3.0에서 instruction 0.89, example 0.93" → Appendix D.3.2 "After EM convergence", Table 7(p.19) 3.0행 0.89 (0.06)/0.93 (0.05). 같은 표 0.3행은 0.16 (0.07)/0.11 (0.06)이다.
- (47줄) "가장 약한 과제는 matrix roll columns(instruction 0.17(0.15))" → 유지+위치: Table 5(1-EM, instruction, p.18)와 Table 8(수렴, p.19)의 ratio 3.0열 0.17 (0.15). 네 개 per-task 표(13행씩) 모두 ratio 3.0에서 matrix roll columns가 최저다(example형은 0.50 (0.18), Table 6과 9).
- (47줄) "과제별 SE로 역산하면 과제당 n이 약 4–11개" → 우리 계산 n = p(1−p)/SE²이다. 예: 0.75 (0.22) → 약 3.9, 0.60 (0.15) → 약 10.7. 원문이 n을 쓰지는 않는다 [PROPOSAL].

**괄호값과 ±의 정의**
- Table 1(Appendix C, p.15), Table 4, Table 7(Appendix D.3, p.18–19): 캡션이 "averaged (with 95% confidence intervals)", "with 95% confidence intervals"다. 따라서 `0.974 (0.006)`과 `0.20 (0.08)`의 괄호값은 95% 신뢰구간의 폭이다. 원문은 "반폭"이라고 쓰지 않지만 정규근사 반폭 1.96·√(p(1−p)/n)와 맞는다: GINC 0.974, n=2500 → 0.0062이고, LIALT 0.20, n=100 → 0.078, 0.89, n=100 → 0.061이다. W6의 "±0.006"은 이 괄호값(95% CI 폭)이다.
- Table 5, 6, 8, 9(per-task, p.18–19): 캡션이 "with standard errors"다. `0.17 (0.15)`의 괄호값은 표준오차다.
- 따라서 W6 보고에서 `0.20(0.08)`류는 95% CI(Table 4, 7)이고 `matrix roll columns 0.17(0.15)`는 표준오차(Table 5, 8)다. 같은 표기라도 의미가 다르다. 표본 수는 GINC 칸당 2500 prompt, LIALT 세트당 100 prompt이며 학습 seed 수는 원문에 없다.

#### 2.4 범례 점검

제안 범례 "필드 1–10·12는 별도 표기가 없으면 [LITERATURE] (위치 병기), 필드 11은 [PROPOSAL]"은 W1, W3, W6에는 그대로 달 수 없다. 우리 산술·추론·코드 독해·그림 판독 문장이 표시 없이 섞여 있다. 수정 제안: "필드 1–10·12는 별도 표기가 없으면 [LITERATURE] (위치 병기). '내 산술/내 추론/추정'은 [PROPOSAL], '코드:'는 [CODE], '(그림 판독)'은 [FIGURE-READ]로 구분. 필드 11은 [PROPOSAL]".

아래 목록은 키워드(추정, 해석, 내 산술, 내 추론, 코드, 판독 등) 스캔과 직접 읽기를 합친 것이라 전수는 아니다. 줄번호는 reports/ 파일 기준이다.

- **W1 SPENS24**: 현 범례 부적합.
  - 67줄 "Shapes3D … trainable 약 1.18M. 내 산술" → [PROPOSAL]
  - 75줄 "코드는 logit을 √d로 나눈다 … β_eff=0.18" → [CODE]+산술
  - 110줄 "7,840 = 10클래스×784픽셀이며 픽셀을 독립 표본으로 취급했다" → [PROPOSAL]
  - 114줄 "(내 산술) … 추론 검정이 아니다" → [PROPOSAL]
  - 119줄 "SI Fig.S1(18 list)을 눈으로 세면 … 'often'은 과장일 수 있다" → [FIGURE-READ]+[PROPOSAL]
  - 163, 164줄(필드 12) "판단(측정 안 함)", "(내 추론)" → [PROPOSAL]
- **W1 HWU20**: 현 범례 부적합.
  - 240, 247, 260, 276, 367줄 코드 독해 → [CODE]
  - 256줄 "(내 산술)", 299줄 "내 산술로 … 망각을 없애지 못한다", 362줄 "기대 0 비율은 1−e^{−P}≈0.26" → [PROPOSAL]
  - 307줄 "추측적 mapping이다(p.181-182)" → 원문이 직접 그렇게 썼는지 확인 전에는 [PROPOSAL]
  - 359–360줄 "e_boost: Table 1은 1000, 코드는 2000 … 내 추론" → [CODE]+[PROPOSAL]
  - 365줄 "후자가 맞아 보인다", 382줄 "(로봇 응용 추정)" → [PROPOSAL]
- **W3 ELDER26**: 현 범례 부적합.
  - 59줄 "hybrid다", 60줄 "activity, attractor, latent 분포가 아니다" → [PROPOSAL]
  - 59줄의 Fig3b,c HL 값 → [FIGURE-READ]
  - 64–65줄 "'plastic'은 학습 가능하다는 뜻", "제약이 아니라 결과" → [PROPOSAL]
  - 73줄 "내 해석은 …" → 기표시이므로 [PROPOSAL]로 통일
  - 76줄 "시드 1개이고 순차 갱신이 아니다" → [CODE]
  - 80줄 "ENN은 전체 학습 데이터가 한 번에 필요" → [PROPOSAL]
  - 86–92줄 N2, N3, N7 "(그림 판독)" → [FIGURE-READ]
  - 99–100줄 → 기표시 "판독값", "추정" 유지
  - 102–104줄 → 파일명으로 [CODE]임이 드러나지만 표시 필요
  - 108–110줄 "정성적 유사와 … 가설" 평가 → [PROPOSAL]
  - 119줄 "반대 방향이며, 저자는 이를 논의하지 않는다" → [PROPOSAL]
  - 121–126줄(필드 10) → "코드:" 기표시 유지
- **W3 MICONI25**: 현 범례 부적합.
  - 212–216줄 "위치는 둘", "연속 형태이고 이산 graph는 없다" → [PROPOSAL]
  - 218–223줄, 249–250줄 코드 독해 → [CODE]
  - 255줄 "병합이다. 분할은 없다. 명시적 novelty gate는 없다" → [PROPOSAL]
  - 264–273줄 "(그림 판독)" → [FIGURE-READ]
  - 276–279줄 "쌍당 약 71회(2000/28)로 추정한다" → [PROPOSAL]
  - 284줄, 288–292줄 평가 문장 → [PROPOSAL]
- **W5 SPECTRUM26**: 범례 거의 적합. 95줄 "문헌 종합과 재해석이다. 증거 수준은 질적이고 …"은 평가라서 [PROPOSAL]로 표시하고, 나머지는 쪽 번호가 붙어 있다. 64줄은 이미 [OPEN]이다.
- **W6 SWAMI23**: 현 범례 부적합.
  - 25줄 "hybrid", 26줄 "slot은 같은 관측을 내는 clone 집합" → [PROPOSAL]. 원문의 slot은 템플릿에서 새 토큰이 binding되는 자리다(§1, Discussion p.10). 그림 라벨(p.3)에서 clone 묶음으로 그려진다.
  - 32줄 "E가 fast, T가 slow" → [PROPOSAL]
  - 38줄 "assimilation은 anchor 보호, accommodation은 E 행 rebinding … novelty gate 역할" → [PROPOSAL]. 원문에 assimilat, accommodat, novelty가 0회다.
  - 46줄 "이항 CI로 확인", 47줄 "SE로 역산" → 우리 계산이라 [PROPOSAL]
  - 50줄 "인용 수준의 정성적 비유뿐" → [PROPOSAL]
- 이미 위치 병기가 필요한 W6 필드 3·4·7은 위 2.3에서 채웠다.

### 3. 과제 C

**TEM20 "schema 0회" 재집계**
- 센 대상: 정규식 `sch[eé]m\w*`, 줄바꿈 하이픈 제거 후, 다섯 종류.
  - TEM20/fulltext.txt(Europe PMC XML 텍스트, 156,405자, Highlights·본문·STAR Methods·그림 범례·참고문헌 포함)
  - TEM20/supp_fulltext.txt(6,807자)
  - download/ Cell VoR PDF(pdftotext, 39쪽)
  - download/ Document S1 PDF(Tables S1–S4)
  - download/ bioRxiv v2 PDF(pdftotext)
- 결과(fulltext.txt와 Cell VoR PDF가 같다):
  - 독립 단어 `schema`와 `schemas`는 전부 0회다.
  - `schemata`는 1회다. 참고문헌 [56] Lewis P.A., Durrant S.J. (2011) "Overlapping memory replay during sleep builds cognitive schemata", Trends Cogn Sci 15:343–351이다(Cell PDF에서는 15쪽 참고문헌, [56]은 XML 번호). 본문 Discussion은 "(Foster and Wilson, 2006; Lewis and Durrant, 2011; Liu et al., 2019)"로 인용한다.
  - 다른 철자형은 schematic 9, schematics 2, schematically 3(도식 뜻)이고 scheme 1회는 "a learning scheme similar to the wake sleep algorithm"이다(Cell PDF 13쪽).
- supp_fulltext.txt와 Document S1은 `schem*` 0회다. bioRxiv v2는 schema·schemata 0회(schematic 8, schematics 2, schematically 3, scheme 1)다.
- 교체 문장: "TEM20 본문·STAR Methods·그림 범례·supplement에서 독립 단어 schema/schemas는 0회. 참고문헌 [56] Lewis & Durrant 2011 제목에 schemata 1회(Discussion에서 인용). schematic(s)/schematically는 도식, scheme은 방식의 뜻".

**CHU25 쪽수** (DBLP는 Anubis 봇 챌린지라 조회하지 못했고 우회하지 않았다)

| 출처 | 쪽수 |
|---|---|
| NeurIPS proceedings 논문 페이지 meta(`citation_firstpage`/`citation_lastpage`)와 BibTeX(W2) | 7103–7121 |
| DOI `10.52202/085713-0243`이 해석되는 proceedings.com 페이지 | 7922–7940 (19 pages) |
| Crossref | 7922–7940 |
| OpenAlex | first_page 7922, last_page 7940 |
| 논문 PDF | 19쪽, 쪽번호 메타데이터 없음 |

- Crossref와 proceedings.com의 이웃 논문은 연속이다(-0242: 7877–7921, -0244: 7941–7967). NeurIPS 사이트 값 한 곳만 다르다.
- 미해결로 둔다. 두 값을 출처와 함께 적는다. 참고로 DOI 등록기관 쪽 값이 7922–7940이다.

**MN 대응표** (MICONI25 수치표 T1–T10 → 통합용 MN1–MN10)

| 새 ID | 원 ID | 내용 |
|---|---|---|
| MN1 | T1 | meta-training 약 50%→90~95% (Fig1f, 30 run) |
| MN2 | T2 | 상징 거리·end-anchor (Fig2a) |
| MN3 | T3 | list-linking (Fig3a,b; 본문 "**T3**" 별도 설명도 MN3) |
| MN4 | T4 | massed presentation (Supp Note 9) |
| MN5 | T5 | 고정 random W_in (Supp Note 6) |
| MN6 | T6 | 스칼라 α (Supp Note 10) |
| MN7 | T7 | W_out 또는 W_in 교체 (Supp Note 13) |
| MN8 | T8 | toy model corr (Supp Note 2) |
| MN9 | T9 | 재코딩 표상 상관 (Fig7, Supp Note 12) |
| MN10 | T10 | passive 해 (Extended Data Fig1) |

MICONI25 claim ID M1–M3과 ELDER26 수치 ID N1–N8과는 겹치지 않는다.

**ELDER26 주장표(E1–E5), 필드 10 자리로 옮길 원문 (W3.txt 145–164줄 그대로)**

```
#### 주장표

| 주장 | 판정 | 위치 | 근거 한 줄 |
|---|---|---|---|
| E1 | CONFIRMED(정의), 범위 한정 | Intro 정의문, Abstract | 정의가 일치한다. 다만 "새 데이터"는 같은 과제의 더 많은 샘플로 처음부터 재학습한 것이다. |
| E2 | CONFIRMED | Intro, Methods "Essence neural networks" | layer-wise 비gradient SVM 학습이다. ENN은 Blazek & Lin 2021에서 온 기존 기법이다. |
| E3 외부 요약 ("상위 입력 표현 개선, 하위 핵심 판단 구조 보존") | 내용 CONFIRMED (상위=upstream/입력 쪽, 하위=downstream/출력 쪽일 때). 상위를 "더 높은 층(출력 쪽)"으로 읽으면 WRONG | Abstract, Results, Fig1·Fig3 범례 | 논문 어휘가 아니라 번역어다. |
| E3 우리 기록 ("상위 schema circuit 안정, upstream representation이 새 데이터 반영") | 내용 CONFIRMED. 단 schema 쪽에 붙인 "상위"는 논문의 downstream과 반대 | 동일 | 두 기록이 "상위"를 반대 의미로 쓴 것이므로 논쟁은 용어 문제이고 어느 쪽도 사실이 틀리지 않다. |
| E4 | CONFIRMED | Methods Backprop, Fig3–5, Sup S3–S10 | 동일한 2×3 tanh 구조로 sklearn MLP와 명시적으로 비교한다. |
| E5 | 수치 CONFIRMED(본문에 있음). ±의 의미 NOT-FOUND, 분모 PARTIAL | Results(Fig3 앞), Sup S3 | 조건과 분모는 위 N1에 정리했다. |

**E3 근거 인용**
- 용어 빈도: upstream 9회, downstream 6회, input layer 5회, "hidden layer(s)" 19회. higher는 생물학 문장에서 1회뿐이고 lower·upper는 0회다.
- Abstract: "a hierarchical learning algorithm creates an invariant schema circuit whose weights remain fixed following sparse initial training, with additional data serving to refine the upstream representation."
- Results: "Additional data solely refines input layer weights".
- backprop은 '"cognitive" layers downstream of the input layer'가 요동친다고 쓴다.
- Fig1 범례: "Downstream schema consolidation enables modular refinement of upstream hyperplanes".
- 코드로 확인한 층 대응: IL=`coefs_[0]`, HL1=`layers[1]`, HL2=`layers[2]`다.
- 해석: **고정되는 것은 downstream hidden layers(HL1, HL2), 갱신되는 것은 upstream 입력층 가중치(IL)다.**
- 고정 시점은 단일 예시 run에서 두 번째 지점(12%, 약 107 clips)부터다. 입력 가중치 분포가 넓어지는 것 외에 정확도 향상은 보이지 않았다.
```

**SPECTRUM26 유형**
- PDF 머리말(fulltext.txt 3줄과 65줄 러닝 헤더)은 "Perspective"다.
- PubMed publication type은 "Journal Article"(D016428)과 "Review"(D016454) 두 개다. OpenAlex type은 review다.
- 두 값을 모두 적는다.

### 4. 최종 검증 명령 출력

1) `for d in */ …` (실행 0.34초):
```
CHU25/ OK
ELDER26/ OK
GAP-ALMA/ OK
GAP-LCNET/ OK
GAP-MEDCRP/ OK
GAP-NESTED/ OK
GAP_SEARCH/ OK
GAP-WHATHOW/ OK
GOUDAR23/ OK
HWU20/ OK
KUMAR26/ OK
META/ OK
MICONI25/ OK
SPECTRUM26/ OK
SPENS24/ OK
STRUCTK25/ OK
SWAMI23/ OK
TEM20/ OK
```
(18개 폴더, 실패 0건)

2) STRUCTK25/fulltext.txt:
```
file sha256: fac2773e55390c00acf58009384a567f3626d37ad37390c7956064d9315a60f7
browser H : fac2773e55390c00acf58009384a567f3626d37ad37390c7956064d9315a60f7
MATCH
wc -l -w -m -c:   1362  14449 111957 112612
```

3) `python3 -I -c 'import json…' */access.json`:
```
json ok 16 files
```
추가 확인: STRUCTK25/access.json은 status "fulltext", words 14449, chars 111957, 브라우저 해시와 파일 해시 일치, attempted_routes 13, pages null이다. 폴더 밖 .md는 0개다(code/ 제외).

### 5. 미해결·불확실

- STRUCTK25는 `<article>.innerText`라서 머리글·추천 블록·참고문헌 링크 텍스트(Article / Google Scholar)가 섞여 있다. 오프셋은 access.json `fulltext_scope`에 기록했다. 표 셀은 공백 정규화했고 체크 표시는 LaTeX `\(\checkmark \)`로 나온다. 그림 이미지는 보지 않았다. 페이지는 동적이므로 재캡처하면 달라질 수 있어 해시를 고정했다.
- 참고문헌 목록은 전수 파싱해 169개 개수와 CR 키만 대조했고, 각 항목의 서지 정확성은 확인하지 않았다(위 오류 3건은 눈에 띈 것만).
- 과제 B의 범례 점검은 키워드 스캔과 직접 읽기를 합친 것이라 전수가 아니다. W1과 W5·W6는 줄 단위 전체 정독이 아니고, W3는 ELDER26/MICONI25 절을 읽었다.
- ELDER26: svm_multiplier가 실제로 무엇을 곱하는지는 코드 의미를 확정하지 않았다. 데이터 증가 부분집합의 중첩 여부도 미확정이다.
- MICONI25: "P(t) 200×200"은 n=200과 Eq.(1)에서 읽은 것이다. A의 음수 가능은 초기화·requires_grad로 읽은 것이고 학습 후 부호 분포는 확인하지 않았다.
- SWAMI23: 괄호값이 95% CI 반폭이라는 것은 캡션("95% confidence intervals")과 정규근사 재계산의 일치로 본 것이다. 원문이 "반폭"이라고 명시하지는 않는다.
- CHU25 쪽수는 미해결이다. DBLP는 봇 챌린지로 조회하지 못했다.
- TEM20의 참고문헌 번호 [56]은 Europe PMC XML의 번호다. Cell PDF는 번호 없는 알파벳순 목록이다.
- STRUCTK25/extraction.json은 W5의 WebFetch판이라 이제 구판이다. 새 보고로 대체할지는 통합 단계에서 정해야 한다.
- 하위 worker 스폰 실패(세션 한도)로 B·C는 직접 처리했다. `_scripts/B2`, `_scripts/B3`의 중단 잔여 스크립트는 정리하지 않았다.

산출물 경로:
- `fcl-sbl-fulltext-20261111/STRUCTK25/fulltext.txt`
- `fcl-sbl-fulltext-20261111/STRUCTK25/tables_from_springer_html.txt`
- `fcl-sbl-fulltext-20261111/STRUCTK25/access.json`
- `fcl-sbl-fulltext-20261111/STRUCTK25/SHA256SUMS.txt`
- `fcl-sbl-fulltext-20261111/_scripts/structk25/assemble_from_transcript.py`
- `fcl-sbl-fulltext-20261111/_scripts/structk25/update_access.py`
