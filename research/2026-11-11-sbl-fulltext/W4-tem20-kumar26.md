# TEM20, KUMAR26 — 구조/내용 분리와 one-shot binding

> 2026-11-11 SBL 원문 검토 워크플로에서 worker가 쓴 보고를 마스터가 원문 대조로 검수해 옮겼다. 종합은 [2026-11-11-sbl-fulltext-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext-review.md)에 있다.
>
> `fcl-sbl-fulltext-20261111/...` 경로는 저장소 밖 호스트 작업 폴더다. 원문은 저작권 때문에 저장소에 넣지 않았다. 판본과 해시는 [evidence.json](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/evidence.json)에 있다.
>
> 표기는 본문 첫머리의 범례를 따른다. 정정: TEM20 필드 2의 "schema 0회"를 재집계 결과로 바꿨다([W7-remediation.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/W7-remediation.md) §3).

---

## W4 보고: TEM20 + KUMAR26 (구조/내용 분리·one-shot binding)

범례: 필드 1–10과 12는 별도 표기가 없으면 [LITERATURE] (위치 병기)입니다. 내 추론은 [PROPOSAL], 원문만으로 판단 불가한 것은 [OPEN]으로 표기합니다. KUMAR26의 페이지 번호는 arXiv v5 PDF 기준입니다.

수행 내용
- 두 논문 원문 전체를 읽고, 공식 코드 2개를 clone해 읽기 전용으로 감사했습니다. 코드는 실행하지 않았고 repo는 수정하지 않았습니다.
- 모든 다운로드는 각 ID의 `download/`에 두었고, 추출 스크립트는 `_scripts/W4/`에 있습니다. 스크립트는 `python3 -I`로만 실행했습니다.
- 산출물
  - TEM20: `fcl-sbl-fulltext-20261111/TEM20/fulltext.txt`, `fcl-sbl-fulltext-20261111/TEM20/supp_fulltext.txt`, `fcl-sbl-fulltext-20261111/TEM20/access.json`, `fcl-sbl-fulltext-20261111/TEM20/extraction.json`
  - KUMAR26: `fcl-sbl-fulltext-20261111/KUMAR26/fulltext.txt`, `fcl-sbl-fulltext-20261111/KUMAR26/supp_fulltext.txt`, `fcl-sbl-fulltext-20261111/KUMAR26/access.json`, `fcl-sbl-fulltext-20261111/KUMAR26/extraction.json`
  - 코드: `fcl-sbl-fulltext-20261111/code/generalising-structural-knowledge`, `fcl-sbl-fulltext-20261111/code/schema4one`

---

### A. TEM20

#### 접근 증거
- **route**
  - Europe PMC fullTextXML(VoR 본문 + STAR Methods)에서 fulltext.txt를 만들었습니다. `jats2txt.py`로 MathML을 선형화했습니다.
  - Oxford ORA의 Elsevier VoR PDF(39 pp)로 수식을 교차확인했습니다.
  - supplement(Document S1 = Tables S1–S4)는 ScienceDirect ARS CDN에서 받았습니다. md5 `f46f035d…`가 PMC XML 기록과 일치합니다.
- **url**: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7707106/fullTextXML
- **version**: Cell 183(5):1249–1263.e23, VoR.
  - received 2019-10-14, revised 2020-06-11, accepted 2020-10-13, epub 2020-11-11, ppub 2020-11-25.
  - version_date=2020-11-25, vor_or_preprint=VoR.
  - bioRxiv 770495 v1(2019-09-16)·v2(2019-09-24)는 교차참조용으로만 받았고, VoR과 exhaustive diff는 하지 않았습니다.
- **pages**: null (XML 유래라 쪽수 없음. ORA VoR PDF는 39 pp)
- **words**: fulltext 23,761(참고문헌 92건 포함), supp 632
- **읽은 범위**
  - Highlights·Summary·Introduction·Results 14절·Discussion 전체
  - STAR Methods 전체(Task details부터 Quantification까지)
  - Tables S1–S4 전체
  - 그림 패널은 Fig 3·4 페이지 이미지만 열람했고, 나머지는 캡션 기준입니다.
- **sha256 앞 16자**

| 파일 | sha256[:16] |
|---|---|
| fulltext | 54d8fcd271ec9ecf |
| supp | e336120a3da314de |
| XML | 29b2bbd3331106e1 |
| ORA VoR PDF | 5b0ec921e2cd3eed |
| mmc1 | 00cdc6f3cf09664b |
| bioRxiv v2 | d8271ae18f5ea9ab |
| openalex | 3d36105684e934fc |
| EPMC meta | 9988e3c014107c9a |
| bioRxiv API | a1af9b58c65043e9 |

- **차단된 경로**
  - Cell 공식 PDF 403, UCL 403, europepmc.org 파일 403(Cloudflare)
  - PMC bin은 JS proof-of-work 페이지라 우회하지 않았습니다.
  - Europe PMC supplementaryFiles 500, PMC OA service 404
  - 전체 목록은 access.json에 있습니다.

#### 필드 1–12
**1 서지**
- 공식 제목을 확인했습니다: "The Tolman-Eichenbaum Machine: Unifying Space and Relational Memory through Generalization in the Hippocampal Formation". bioRxiv 제목은 "generalisation" 철자입니다.
- 저자: Whittington, Muller, Mark, Chen, Barry, Burgess, Behrens.
- DOI 10.1016/j.cell.2020.10.024, PMID 33181068, PMC7707106. 동료심사 완료, CC BY.
- 코드: github.com/djcrw/generalising-structural-knowledge, commit `fa5d533ceb6f958e890d3f1cd83e777d090ef871`(2022-09-29). LICENSE 없음(GitHub API license=null).

**2 schema 정의와 위치**
- 본문·STAR Methods·그림 범례·supplement에서 독립 단어 schema/schemas는 0회입니다. 참고문헌 [56] Lewis & Durrant 2011 제목에 schemata가 1회 있고 Discussion이 이를 인용합니다. schematic(s)/schematically는 도식, scheme은 방식의 뜻입니다(재집계, W7 보완 보고 §3).
- 자체 개념어는 structural knowledge, structural abstraction, cognitive map입니다.
  - "Separating structural codes (the transition rules of the graph) from sensory codes allows generalization over environments sharing the same structure." (Fig 2A)
- 위치는 이렇습니다.
  - 구조는 느린 가중치에 있습니다. g의 action-conditioned recurrent transition W_a이고, 연속·분산 코드이며 이산 객체는 없습니다.
  - 내용은 p(=g와 x의 conjunction)와 Hebbian M(빠른 가중치)에 있습니다.
- 즉 "구조 코드"이며 controller가 아닙니다.

**3 아키텍처**
- 변수는 g(MEC형), p(해마형), x(LEC형, one-hot→two-hot 압축→지수 필터), M(Hebbian), a(주어진 action)입니다. 스트림은 5개입니다.
- 크기(Table S2):

| 변수 | 총 개수 | 스트림별 |
|---|---|---|
| g | 120 | 30, 30, 24, 18, 18 |
| g-down | 40 | 10, 10, 8, 6, 6 |
| p | 400 | 100, 100, 80, 60, 60 |
| x_f | 50 | - |
| x_c | 10 | - |
| x | 45 | - |

  - 표의 g-down "Total=120"은 합계 40과 맞지 않아 오기로 보입니다.
  - 4-lap 과제는 g 18/18/15/15/15, p 60/60/50/40/40입니다.
- 고정/학습
  - W_repeat·W_tile(외적 conjunction 타일링)은 고정입니다.
  - M은 경사 학습 대상이 아니지만 BPTT가 그 안을 통과합니다.
  - W_a, MLP, w_x, w_p, α^f는 backprop으로 학습합니다.
- fast = M, slow = W입니다.
  - M은 스트림 간 상삼각 구조이고, attractor 반복은 5/4/3/2/1입니다(큰 스케일 먼저).
- GNN이 아니고 RL도 아닙니다(행동은 주어집니다).

**4 학습 규칙**
- **외부 루프**
  - ELBO 대리손실 L=Σ(L_x(CE)+L_p+L_g(MSE))를 씁니다. x를 세 경로로 예측하는 보조손실과 memory loss가 붙습니다.
  - BPTT 25(4-lap은 100), Adam lr 1e-3→1e-4.
  - 2D 기준 200–300 환경 ≈ 50,000 업데이트(25 step당 1회).
  - λ·η는 낮게 시작해 0.9999/0.5로 올립니다. 미방문 노드 손실은 마스킹합니다.
- **평생 내(within-lifetime) 가소성**
  - 쓰기: `M_t=λM_{t−1}+η(p_t−p̂_t)(p_t+p̂_t)^T`
  - 검색: attractor `h_τ=f_p(κh_{τ−1}+M h_{τ−1})`, 5회
  - 새 환경마다 M=0으로 리셋합니다. 추론용 M^x는 별도 행렬입니다.
  - "backprop must learn how to use Hebbian learning" (STAR). 또 "Backprop … slow 'outer loop' … Hebbian learning is the fast 'inner loop'".
- 코드에만 있는 것: grad clip_by_norm 2, Hebbian ±1 clip, p에 L1 정규화(0.02), κ=0.8, batch 16 환경, lr 9.4e-4→8e-5.

**5 형성/선택/적용/수정**
- 구조는 outer loop에서만 형성됩니다.
- 구조 선택·생성·병합·분리가 없고, 환경 경계는 프로토콜이 줍니다(M 리셋). novelty/familiarity gate도 없습니다.
- [PROPOSAL] 쓰기식의 (p−p̂) 항 때문에 이미 예측되는 경험은 write가 0에 가깝습니다. 즉 암묵적 prediction-error 비례 쓰기입니다. 식에서 도출한 내 해석이며 논문은 novelty gating이라 부르지 않습니다.
- 구조 불일치 시 수정 실험은 없습니다. "Structural remapping"은 예측으로만 언급됩니다.
- 학습된 신뢰도 가중이 하나 있습니다. g 추정에서 path-integration과 memory 검색을 precision-weighted로 결합합니다(STAR Inference architecture, 코드 p2g).

**6 지속성**
- 파라미터(W)만 환경 간 지속됩니다. M은 환경 내 fast weights이며 리셋됩니다.
- 환경 내 장기 기억은 Fig 3E에 있습니다.
- replay·consolidation 구현은 없습니다. Discussion은 wake-sleep과 replay를 유비로만 언급합니다.

**7 과제·결과·분모**
- 과제 (STAR Task details, Simulation details)
  - transitive inference: 순서 직선, 4/5/6 states, action=(방향, 크기) 2차원
  - social hierarchy: family tree, 관계 10종, 3–4 level = 15/31 states, sensory 45
  - 2D 그래프: square 64/81/100/121, hex 61/91/127
  - 4-lap(Sun et al. 2020): 루프 n=4 laps × l=8, 4번째 lap 첫 상태가 reward
- 결과는 전부 그림(Fig 3)입니다.
  - link inference vs 방문 횟수(학습 분위별), 첫 재방문 추론, 방문한 node 비율 vs edge 비율, 기억 유지
  - 수치표가 없고, 독립 학습 네트워크/seed 수와 음영 정의가 "원문에 없음"입니다.
  - 비교 baseline이 없습니다. ablation은 서술만 있고 데이터가 없습니다. 예: 비대칭 구조는 "정확도 영향 없음, 학습속도 개선"이라고만 적혀 있습니다.
- 신경 데이터 검정
  - Barry 2012(쥐 7마리): 보수 기준 115쌍 r=0.322, p<0.01(permutation 5000회). 자유 기준 255쌍 r=0.63, p<0.05.
  - Chen 2018(쥐 아닌 mouse 4마리): 64쌍 r=0.273, p<0.05. 자유 기준 148쌍 r=0.544.
  - 모델 r=0.31, 데이터 0.27–0.32.
  - grid-grid 상관구조 보존: 동물 1마리(grid 15개) r=0.55, 1마리(13개) r=0.95. place cell은 r=0.31(p=0.035)과 r=0.16(p=0.21).
- 파생 관찰(Table S3·S4에서 내가 계산)
  - 115쌍 = 108(동물1)+5+2, 64쌍 = 40+6+18입니다. 쌍이 독립이 아니고 한 마리가 지배합니다.
  - Table S4에 p>0.05 셀이 있습니다: D1 grid-0 perm1 p=0.0776, D2 MinDist p=0.0524/0.058.
  - 이는 STAR의 "significant correlations for all combinations"와 어긋납니다. Table S4 캡션은 "trending"이라고만 합니다.

**8 신경과학 대응과 근거 수준**
- g↔MEC: grid·band·border·object-vector cell이 출현합니다. 정성적 유사성입니다(Fig 4–5).
- p↔해마: place·landmark cell과 remapping입니다.
- x↔LEC: 근사 Laplace 변환입니다.
- place–grid 상대 위치 보존은 기존 두 데이터셋에 대한 통계 검증(상관 + permutation)입니다. 인과 증거는 아닙니다.
- 4-lap의 해마 세포 유형은 정성 비교와 ESR 상관 vs shuffle입니다. MEC lap 세포는 예측일 뿐이며, 해당 논문에 EC 기록은 없습니다.
- 저자: "It is not a biophysically realistic model." 계산 수준 모델입니다.

**9 한계와 비주장**
- 저자 명시
  - noise-free 과제만 다룹니다.
  - 감각 상관을 의도적으로 제거했습니다(노드마다 i.i.d. 무작위 배정).
  - 비생체물리 모델입니다.
  - 해마 단독 binding은 단순화입니다.
- 원문이 보이지 않은 것
  - 새 구조 계열로의 전이, 구조 불일치, 구조 선택
  - 서로 다른 구조 간 surface 유사성에 대한 견고성
  - W의 순차 학습 시 retention과 간섭
  - replay·consolidation(M→W)
  - 자연어·실세계 관계 데이터
  - seed 변동, 비분해 baseline과의 비교, 적응적 계산량
  - learned structure vs given structure ablation (Melete 선례와 관련해 부재)

**10 주장 검증표**

| 주장 | 판정 | 위치 | 한 줄 사유 |
|---|---|---|---|
| T1 구조 vs 개별 경험 표현 분리 | CONFIRMED | Fig 2A–D; STAR Principles·Generative model; Fig 4A–H | g는 환경 간 일반화(grid형, 상관구조 보존), p/M은 감각 결합·remap. 단 분리는 아키텍처 prior(고정 W_repeat/W_tile)와 학습 분포가 만든 것이며 비구조 데이터에서 발견된 것이 아닙니다. |
| T2 관계 recurrent 표현 재사용 + 해마 attractor 메모리가 현재 환경 binding | CONFIRMED | Results Model Training; STAR Memories·Simulation details | 동일 W를 재사용하고 환경마다 M을 0으로 리셋합니다. 매 step Hebbian 쓰기, 고정 5회 attractor 검색입니다(Ba et al. 2016식 fast weights). |
| T3 비공간 관계 문제 적용 | CONFIRMED(범위 한정) | Results 'TEM Generalizes…'; STAR Task details | 과제: transitive inference, social hierarchy, 4-lap(Sun et al.), (+2D). 모두 합성·noise-free·one-hot 입력에 action이 주어지는 과제이고, 자연어형 관계 과제는 없습니다. |

**11 FCL 연결 [PROPOSAL]**
- **DQ1**: "느린 전이 연산자(latent state, action-conditioned) + (state⊗content) conjunction 위 fast Hebbian memory"라는 분해 템플릿입니다. System ONE에서는 slow weights/CMS가 구조, Titans형 fast memory가 binding에 해당합니다. 분해 prior는 직접 주입해야 합니다.
- **DQ2**: schema 선택은 TEM에 없습니다. 검색 품질로 분산을 정하는 precision-weighted 결합이 라우팅 신호의 원형입니다.
- **DQ3**: TEM의 (p−p̂) 쓰기, λ forget, η write rate는 Titans의 surprise·decay와 대응됩니다. 기본 게이트 baseline으로 쓸 수 있습니다. accommodation(불일치 시 W 수정)은 부재라 우리 확장이 됩니다. 실패 모드는 잘못된 구조가 조용히 내용을 binding하는 것입니다.
- **DQ4**: BPTT(바깥)/Hebbian(안쪽) 두 시간척도와 학습된 다중 스케일 필터(α^f)까지입니다. Sleep·consolidation은 TEM에 없고 HOPE/CMS 쪽에서 가져와야 합니다.
- **DQ5**: attractor 반복 수(5/4/3/2/1)가 스케일별 정지 스케줄의 원형입니다. 효과 데이터가 없으므로 adaptive halting은 직접 검증해야 합니다.
- **DQ6**: 프로토콜을 차용합니다. 첫 재방문 link inference probe, 방문 node vs edge 비율 곡선, 학습 분위별 learning-to-learn 곡선입니다. surface 유사성 견고성은 TEM에서 검증되지 않았으므로 confound 대조군을 추가해야 합니다.
- **DQ7**: M 리셋으로 간섭을 구조적으로 회피할 뿐입니다. 구조 계열을 바꿀 때 W의 retention은 미검증입니다.
- **DQ8**: link-inference 정확도, node-vs-edge 효율, 기억 유지 곡선, 구조 유닛(상관구조 보존) vs 내용 유닛(remap) 표현 검정을 차용할 수 있습니다.
- **실패 모드**
  - 메모리 쓰기를 통과하는 BPTT(25–100 step)는 LLM 규모로 비용이 큽니다.
  - 분리가 학습 환경 간 내용의 무작위화에 의존합니다.
  - 외적 메모리 용량은 p=400에 한정됩니다.
  - 구조 불일치 처리가 없습니다.

**12 재현/프로토타입**
- **논문↔코드 대응**(`tem_tf1/tem_model.py`)
  - Hebbian 쓰기: `hebbian()` L906–942, `final_hebbian` L381–397
  - attractor: L802–831
  - g 전이: `g2g` L682–710, `get_transition` L730–742. gen/inf가 같은 변수 스코프를 공유합니다.
  - 손실: L312–363
  - 환경별 M 리셋: `run_tem.py` L125
  - link-inference probe는 10환경마다 실행합니다(L113).
  - 하이퍼파라미터: `parameters.py` L90–172
  - tf2는 같은 설정을 정리한 판이며(lr 9.4e-4→8e-5, λ=0.9999, attractor 5/4/3/2/1, clip norm 2) tf1을 별도로 대조하지는 않았습니다.
- **논문–코드 불일치**
  - 4-lap 과제에서 reward 상태의 prediction loss를 ×n_states로 가중합니다(`tem_model.py` L163–166, `parameters.py` L31). 논문 본문에는 없습니다.
  - lr: 논문 1e-3→1e-4, 코드 9.4e-4→8e-5.
  - 에피소드 길이: 논문 ~2000–5000 step, 코드 2500–6000(+jitter).
  - grad clip, Hebbian clip, L1 정규화는 논문 손실 절에 없습니다.
  - Table S2 합계 오기도 같은 종류의 불일치입니다.
- LICENSE 없음.
- 실행성 [PROPOSAL/추정, 미실행]: 모델이 작습니다(g=120, p=400, Hebbian A는 16×400×400 float, 약 10 MB). CPU로 충분합니다. 비용은 25-step 순차 전개 × attractor 5회에서 나오므로 GPU 이득이 적습니다. TF1.9/2.3 바이너리는 RTX 50계열(Blackwell)을 지원하지 않으므로 CPU 또는 PyTorch 포트(README가 `jbakermans/torch_tem` 언급, 미감사 [OPEN])를 써야 합니다.

---

### B. KUMAR26

#### 접근 증거
- **route**
  - latest arXiv v5 PDF(70 pp)에서 fulltext.txt를 만들었습니다(`pdftotext -layout`).
  - supp_fulltext.txt는 같은 PDF의 pp.60–70(Supplementary Figures S1–S8)을 따로 추출한 사본입니다. fulltext.txt와 내용이 중복됩니다.
  - **J Neurosci VoR는 paywall이라 읽지 못했습니다.** 본문 페이지는 abstract + significance + login/purchase만 보입니다.
  - PDF URL 3종은 모두 HTML abstract 페이지로 redirect되고, journal supplement URL은 403입니다.
  - Europe PMC는 레코드는 있으나 inPMC=N, hasPDF=N입니다.
- **url**: https://arxiv.org/pdf/2106.03580v5
- **전 버전 (arXiv abs 페이지 + API, UTC)**

| 버전 | 일시 | 크기 | 쪽수 | 비고 |
|---|---|---|---|---|
| v1 | 2021-06-07 13:03:51 | 1,470 KB | 16 pp | 제목 "One-shot learning of paired associations by a reservoir computing model with Hebbian plasticity" |
| v2 | 2023-03-04 08:26:26 | 3,508 KB | 47 pp | 제목이 최종 제목으로 변경. "Major revisions from version 1 preprint" |
| v3 | 2023-08-27 12:39:02 | 3,767 KB | 48 pp | "Minor revisions from version 2" |
| v4 | 2024-09-10 03:37:18 | 5,840 KB | 50 pp | "Minor revisions in discussion" |
| v5 | 2026-10-20 12:14:19 | 9,425 KB | 70 pp | "Major revisions. 7 figures, 8 supplementary figures" |

- 저널: J Neurosci Early Release, 2026-10-26 표기, e1803242026(볼륨/이슈/쪽수 미부여), DOI 10.1523/JNEUROSCI.1803-24.2026, PMID 42933903. 페이지 URL 경로는 `early/2026/10/22`입니다.
- version_date=2026-10-20, vor_or_preprint=preprint, pages=70.
- **words**: fulltext 22,319, supp 2,357.
- **VoR와 v5의 차이**
  - 저널 페이지의 abstract(1,469자)와 Significance Statement(795자), acknowledgement가 v5와 문자 단위로 동일합니다(대시/아포스트로피 정규화 후 difflib 1.0000).
  - 그래서 v5가 accepted manuscript일 가능성이 높지만 이는 추론입니다. 본문·그림·supplement의 VoR 차이는 배제할 수 없습니다 [OPEN].
- **읽은 범위**
  - v5: Abstract, Significance, Introduction, Methods 전체, Results 전체, Discussion, Supplementary Figures 캡션 S1–S8.
  - 텍스트 레이어에서 지수가 깨진 Table 1·Eq.45·p37의 값은 페이지 이미지로 확인했습니다.
  - v1은 abstract·intro·methods 2.1–2.6을 읽었습니다.
  - v2–v4는 abstract·절 제목·키워드 빈도·선택 문맥만 비교했고 전문을 읽지 않았습니다.
- **sha256 앞 16자**

| 파일 | sha256[:16] |
|---|---|
| fulltext | 5d8a4680274b9774 |
| supp | 2c9714db42b286ba |
| v1 PDF | a04e46d179834b3b |
| v2 PDF | 9f7e5cf835f0ef71 |
| v3 PDF | f094642bbd587fe4 |
| v4 PDF | 31b3113192947d7c |
| v5 PDF | da1a993a60626d2d |
| abs v5 HTML | 5118b48939e85791 |
| API xml | ad351e6c5beb26c7 |
| openalex | e3b54d3a7202b428 |
| EPMC search | 99206c915411bbd0 |
| JN landing(abstract-only) | 631a759fc6ca49fa |
| JN figures-data | 3b31735fdc28bd4e |

  - 나머지 abs 페이지 해시는 `SHA256SUMS.txt`에 있습니다.

#### 필드 1–12
**1 서지**
- 최종 제목: "One-shot learning of paired association navigation with biologically plausible schemas".
- 저자: Kumar, Tan, Libedinsky, Yen, Tan.
- 코드: github.com/mgkumar138/schema4one, commit `46fd71881d73cc3b2d1c5b979419dfd3d0abc094`(2026-05-19). LICENSE 없음.

**2 schema 정의와 위치**
- Intro(p3): "Schemas are knowledge structures or frameworks that describe relationships among stimuli, actions, and outcomes…".
- Fig 1 legend(p22): "A schema is a framework that describes relationships between information and actions… conceptualized as a computation in Marr's sense".
- 즉 schema = Marr 계산 수준의 모듈(알고리즘 + 신경 구현)입니다. 구조 코드 하나가 아니라 **모듈 묶음**입니다.

| 모듈 | 성격 | 위치 |
|---|---|---|
| LEARN METRIC REPRESENTATION | 구조 코드 | place→X,Y 좌표 뉴런 가중치(2차원, 연속) |
| LEARN FLAVOR-LOCATION | 메모리(binding) | reservoir/FF→goal 뉴런(X, Y, recall value) readout 가중치 |
| NAVIGATE | controller(관계 계산: vector subtraction) | 고정 2×128 MLP 가중치 |
| WM gating | 메타 제어 | reservoir→gating 유닛 가중치. "candidate fourth schema… did not formalize it at the computational level" (p12) |

- Foster et al. (2000)의 3개 schema를 계승했습니다.
- 저자 자신의 견해(p50): "Schema acquisition may be better conceptualized as the gradual emergence of structured mechanisms that enable fast learning, rather than as a discrete system or switch."

**3 아키텍처**
- 입력: place cell 49개(7×7, σ=0.267 m, 아레나 1.6 m), one-hot cue 18차원(gain 3).
- reservoir: N=1024(논문) / 코드 기본값 1000. λ=1.5, 연결확률 0.1, 입력 U[-1,1], recurrent 가중치 고정.
- readout: actor 40-뉴런 ring attractor, critic 1, goal 3, gating 2, bump attractor 54.
- NAVIGATE: 입력 5(현재 X,Y / goal X,Y / recall value), 출력 40. backprop으로 사전학습한 뒤 고정합니다.
- 비교 agent: actor-critic(무 schema), symbolic schema agent(key-value 행렬), neural schema agent(reservoir + EH 또는 LMS), hybrid(β^control 0.3/0.4/0.9), meta-RL A2C RNN(N=256).

**4 학습 규칙 (outer loop vs 평생 내 가소성 분리)**
- **Outer loop(주 agent)**
  - NAVIGATE의 오프라인 supervised backprop 사전학습입니다(20 epoch, MSE, p11).
  - 하이퍼파라미터 grid search입니다. 학습률, τ_c, β^control, Ω_ACh를 "minimize the latency over the initial MPA sessions and maximize the visit ratios for OPA and 6NPA"로 골랐습니다(p19). **평가지표로 튜닝했고** 튜닝 seed 수는 원문에 없습니다.
  - meta-RL(A2C+BPTT, 200 epoch, lr 1e-4, γ=0.99)은 비교 baseline이며 주 agent가 아닙니다.
- **평생 내 가소성**(학습되는 시냅스는 0으로 초기화)
  - 좌표: path-integration TD 오차 `δ=p(t)−p(t−Δt)−ã(t)`, eligibility trace(τ_e=1000 ms), `ΔW=η_PI e δ`, η_PI=0.01 (Eq 7–9).
  - cue→goal: 보상 변조 4-factor exploratory Hebbian `ΔW=η r (g^noisy−g) M(t) Θ[R]` (Eq 18–23). `M(t)=1 if P̂<P`, P는 −제곱오차. 비교용으로 reward-modulated LMS(Eq 19)도 있습니다.
  - 삭제: ACh 변조 시냅스 억제 `ΔW=η r g (−Ω_ACh)` (Eq 25). 상시 tonic이며 Ω_ACh는 DMP 5e-4, 그 외 5e-5입니다.
  - critic/actor: TD 오차 `δ^TD`(Eq 35–38). critic은 two-factor, actor는 three-factor입니다. τ_c는 3000 ms(장애물 없음) 또는 10000 ms(장애물)입니다.
  - WM gate: `ΔW=η_gate r π δ^DA`, η_gate=1e-4 (Eq 45, 이미지로 확인). softmax β=2이고 WTA·곱셈 게이트는 알고리즘으로 구현했습니다.
  - Table 1(이미지 확인): η_critic 1e-4~2e-4, η_actor 5e-6~1e-4.
- "gradual then one-shot"에서 gradual은 outer loop가 아니라 **평생 내 느린 가소성**입니다.

**5 형성/선택/적용/수정**
- **형성**
  - 좌표 표현은 온라인으로 서서히 수렴합니다. 단독 시험은 20회 × 300 s 무작위 탐색입니다(Fig 2A, S1A).
  - 연합은 보상이 있었던 단 1 trial에 기록됩니다.
  - gate 정책은 약 6+ session에 걸쳐 학습됩니다(Fig 7C).
- **선택**
  - 여러 schema 중 선택은 없습니다.
  - 제어 조정은 고정 하이퍼파라미터 β^control(Fig S5에서 탐색)과 recall value < 0.6이면 NAVIGATE 출력을 억제하는 임계값뿐입니다. ACC 조정은 Discussion의 제안일 뿐 구현되지 않았습니다.
- **수정**
  - 오류·낡은 연합은 ACh 억제로 cue 특이적으로 삭제하며 다른 연합은 보존합니다(Fig 2D의 Cue 4). ACh가 없으면 perseveration이 나옵니다(p30).
  - 목표가 이동한 DMP는 1 trial 후 다시 기록합니다.
  - place cell remap(NM)에서는 좌표 코드가 무효가 되어 약 20 session에 걸쳐 **재학습**합니다(Fig S2, S4). 불일치 탐지나 빠른 수정은 없습니다.
- novelty gating은 구현되지 않았습니다(Fig 7F는 분석일 뿐). assimilation/accommodation 용어와 schema 병합·분리는 없습니다.

**6 지속성**
- 연합은 readout **가중치**(parameter 변화)에 저장되며 trial과 session을 넘어 지속됩니다.
- reservoir 상태는 trial마다 재무작위화됩니다(코드 `agent.state_reset`→`rec.reset`).
- bump attractor는 cue를 trial 내 **활성**으로만 유지합니다.
- replay·consolidation은 없습니다. Discussion이 열린 문제로 둡니다.

**7 과제·결과·분모**
- **프로토콜**
  - 1.6 m 아레나, session = 6 trial(cue 6개 각 1회).
  - Stage 1 = 20 session(장애물판 50)이고, probe는 session 2/9/16(장애물판 2/18/36)입니다.
  - Stage 2 = 새 쌍을 1 session 학습 후 probe입니다. OPA / 2NPA / 6NPA / NM(place cell shuffle) 조건이 있습니다.
  - 12NPA는 12쌍 각 1 trial입니다. visit ratio chance는 16.7%(12쌍은 8.3%)입니다.
- **표본**
  - n=720(Fig 3·5), n=480(Fig 4·6·7)
  - Fig 2C는 30회, Fig S3 30 seed, Fig S5 100 seed, Fig S7 30 seed.
  - Cohen's d=t/√n이고 p는 임계값으로만 보고합니다.
  - 본문의 "±" 정의는 원문에 없습니다. 그림 범례는 Fig 3–7이 95% CI, Fig 2C/S3/S5/S7이 SE입니다.
- **DMP(Fig 3)**: Trial 1→2 latency savings(session 5–9) = actor-critic −2.5±8 s, symbolic 56±9 s, neural 57±8 s.
- **MPA(Fig 5)**
  - Stage 1 latency(session 20): AC 25±1.6, symbolic 46±2.6, neural 67±2.9 s.
  - one-shot d(chance 대비):

| 조건 | symbolic | neural | AC |
|---|---|---|---|
| 2NPA | 4.0 | 2.6 | −0.71 |
| 6NPA | 2.5 | 5.2 | −0.22 |

  - NM에서는 모든 agent가 chance입니다.
  - 20 session 재학습 후 새 6쌍(6NPANM)에서는 schema agent가 다시 one-shot을 보입니다.
- **12NPA 용량**
  - AC 1.9±0.17, symbolic 11.6±0.12.
  - neural reservoir EH는 128유닛 3.5±0.11 → 1024유닛 7.8±0.16입니다.
  - 2048유닛은 3.9±0.17이다가, η_goal을 7.5e-5→5e-5로 낮추면 8.7±0.18입니다.
- **장애물**
  - 단일 목표: 순수 schema agent는 장애물을 못 넘고(Fig 4), hybrid와 AC는 넘습니다.
  - MPA+장애물(Fig 6): session 50 latency AC 117±5, neural 91±3, AC-symbolic 141±7, AC-neural 79±4, symbolic 343±9 s.
  - Stage 2 one-shot은 hybrid만 보입니다. 2NPA d는 1.28(AC-symbolic)과 0.44(AC-neural), 6NPA d는 1.51과 0.59입니다.
- **작업기억(Fig 7)**
  - 방해 자극 없음: latency 56±3 s, PS1→PS3 d=3.90, OPA d=4.56.
  - 방해 자극 1/2개, gating 가소성 off: latency 133±6 / 178±7 s. 2NPA d=0.07/0.05, 6NPA d=−0.39/−1.09.
  - 방해 자극 1/2개, gating 가소성 on: latency 71±4 / 87±5 s. 2NPA d=0.45/0.78, 6NPA d=1.46/1.83.
  - gating 활성은 PS1 ~0.45, PS2부터 cue 중 ~0.5, cue 제거 후 ~0.1입니다.
- **meta-RL(Fig S7–S8)**: symbolic 메모리 + 고정 place cell일 때만 one-shot이 나타나고, place cell을 shuffle하면 사라집니다(30 seed).
- **EH vs LMS**
  - 작은 크기에서는 LMS가 낫고, 큰 크기에서는 EH가 따라잡습니다.
  - 에이전트 이동 중 recall value는 LMS ~0.95, EH ~0.61이고 목표 근처에서 1.08로 오릅니다(Fig S1B). 즉 신경 recall은 place 입력의 영향을 받습니다.

**8 신경과학 대응과 근거 수준**
- 좌표 뉴런 ↔ coordinate-like tuning(LaChance 2019, Lever 2009): 정성적입니다.
- NAVIGATE penultimate 유닛 ↔ cue-invariant distance/angle cell(Sarel 2017): 사전학습 후의 정성적 유사성입니다.
- 모듈별 weight-change vs novelty(Fig 7F) ↔ Tse et al. 2011: 정성적입니다.
- ACh 억제 ↔ Zannone 2018: 정성적입니다.
- dopamine/RPE 게이트는 예측입니다.
- 데이터 fit은 없고, Discussion이 검증 가능한 예측 3개를 제시합니다.

**9 한계와 비주장**
- 저자 명시
  - NAVIGATE는 직선 접근만 가능합니다(p50).
  - 단조 rate-code 좌표는 해상도 한계가 있고, 좌표 뉴런 존재는 입증되지 않았습니다(p48).
  - NAVIGATE는 backprop 사전학습이며 진화·발달로 해석합니다(p49).
  - gating의 WTA·곱셈은 algorithmic입니다(p43).
  - 위계 연합, consolidation, spiking 구현은 열린 문제입니다.
- 원문이 보이지 않은 것
  - **구조(좌표) 코드는 place cell remap에 걸쳐 전이되지 않고 재학습됩니다.** TEM의 g처럼 환경 간 전이되지 않습니다.
  - 새 쌍 학습 후 기존 쌍의 retention은 보고되지 않았습니다. 코드의 2NPA 지표는 새 cue 7·8만 셉니다(`6pa_res.py` L207–211).
  - 인터페이스가 손으로 만든 것입니다(place cell, self-motion, one-hot cue, ring).
  - 단일 과제 계열(open-field 내비게이션)이며 비공간 과제가 없습니다.
  - schema 선택·병합·분리가 없고 β가 수동 튜닝입니다.
  - 평가지표로 하이퍼파라미터를 튜닝했습니다.
  - learned structure vs given structure ablation이 없습니다. 코드에는 `learnxy` 플래그가 있으나 논문에 비교 결과가 없습니다.

**10 주장 검증표**

| 주장 | 판정 | 위치 | 한 줄 사유 |
|---|---|---|---|
| K1 fully neural agent | PARTIAL | Abstract; p11·p43·p49 | 주 agent는 rate 뉴런 + 국소 가소성이지만, NAVIGATE는 backprop 사전학습·고정이고 gate의 WTA·곱셈은 algorithmic이며 입력·reservoir·ring은 고정/수작업입니다. |
| K2 저차원 공간 표현 + one-shot cue→goal 메모리 + 관계 계산 neural controller | CONFIRMED(단서) | Results p23–26; Fig 1–2 | 2개 좌표 유닛, reservoir/FF + EH 또는 LMS, vector-subtraction MLP입니다. 관계 계산은 vector subtraction뿐이고 신경 recall은 근사(N=1024에서 7.8/12)입니다. |
| K3 TD + reward-modulated exploratory Hebbian | CONFIRMED(모듈별) | Eq 7–9, 20–25, 35–38, 45 | TD 규칙은 좌표·critic/actor·gate에, 4-factor EH는 cue→goal에, ACh 억제는 삭제에 씁니다. NAVIGATE(backprop)가 예외입니다. |
| K4 working-memory gating 학습 | CONFIRMED(단서) | p43–45, Fig 7; Eq 39–45 | 2개 gating 유닛을 TD 변조 Hebbian으로 학습하고 2NPA/6NPA로 전이됩니다. WTA·곱셈은 algorithmic이고 저자도 형식화하지 않았다고 밝힙니다. |
| K5 방해 자극 하 one-shot | CONFIRMED(효과 작음) | p44, Fig 7E | gating on: 2NPA d=0.45/0.78, 6NPA d=1.46/1.83(n=480). gating off는 chance 이하입니다. 방해 자극은 cue 2종·1초·trial당 1–2개뿐입니다. |
| K6 arXiv 2021→J Neurosci 2026, 제목·내용 변경 | CONFIRMED | arXiv abs v1–v5; JN early-release 페이지 | v2(2023-03-04)에서 개제목, v5(2026-10-20, 70 pp) 대개정, JN early release 2026-10-26이고 abstract·significance가 v5와 동일합니다. VoR 본문은 paywall입니다. |

버전 간 내용 변화 요약
- v1에도 symbolic 메모리, 학습된 좌표, 사전학습 neural motor controller, 4-factor EH, 12NPA가 이미 있었습니다. 'fully neural' 표현도 v1의 appendix와 discussion에 나옵니다.
- v2에서 schema 프레임과 actor-critic, 장애물, WM gating이 들어왔습니다. 'metric representation'·'path integration' 용어도 v2에서 처음 등장합니다.
- v5에서 meta-RL 비교(Fig S7–S8), n=720/480, Cohen's d, 12NPA 용량 곡선이 추가되었습니다.

**11 FCL 연결 [PROPOSAL]**
- **DQ1**: "시간척도가 다른 모듈 묶음" 패턴입니다. 느린 저차원 상태 코드(CMS 느린 수준), outcome으로 게이트되는 빠른 key-value 메모리(Titans형 fast memory), 고정·저학습률 controller입니다. 단, 이 모듈들이 비정형 데이터에서 어떻게 생기는지는 이 논문에 없습니다(Foster 2000에서 수작업 지정).
- **DQ2**: 메모리 자신의 recall 신뢰도(<0.6이면 schema 출력 억제)와 β 혼합이 학습형 context controller의 구체 원형입니다. 둘 다 논문에서 수동 설정이므로 학습화는 우리 확장입니다.
- **DQ3**: 성공 시에만 쓰고(Θ[R]) 실패 시 tonic 억제로 해당 항목만 삭제하는 쓰기·삭제 정책입니다. accommodation(좌표 재학습)은 느린 재학습뿐이고 불일치 탐지기는 없어서 공백으로 남습니다.
- **DQ4**: 한 agent 안에 느린 좌표, 빠른 메모리, 느린 gate의 세 시간척도가 있지만 sleep·replay는 없습니다.
- **DQ5**: 이분법 recall 게이트 외에 계산 깊이 제어가 없습니다. H-COMPUTE 근거로는 약합니다. 다만 "메모리 recall 신뢰도가 높으면 fast path, 아니면 deep thinking"이라는 라우팅 기준으로 쓸 여지가 있습니다.
- **DQ6**: 프로토콜을 차용합니다. stage 1 점진 학습 → stage 2 새 쌍 1회 노출 → probe(visit ratio, chance 대비 d), 12NPA식 용량 곡선(노출 1회로 학습한 쌍의 수 vs 메모리 크기)입니다. NM 조건은 surface가 바뀌어 구조 코드가 무효가 되는 음성 대조로 쓸 수 있습니다.
- **DQ7**: 고정 무작위 cue 투영으로 cue별 분리 부분공간을 만들어 간섭을 줄이는 방식(Fig S1C, 200 cue까지 완만한 용량 저하 Fig 2C)이 fast memory의 key 직교화 후보입니다. 기존 쌍의 retention은 측정되지 않았습니다.
- **DQ8**: savings(T1−T2), probe visit ratio, 12NPA 용량, 모듈별 plasticity vs novelty(Fig 7F), 표현 shuffle 하에서 meta-RL의 메모리 유무 ablation을 차용할 수 있습니다.
- **실패 모드**
  - 용량 한계(7.8/12)
  - 상태 오염 recall
  - 직선 접근 controller
  - 수동 β·임계값
  - 공간 과제 한정 증거

**12 재현/프로토타입**
- **논문↔코드 대응**(`backend/model.py`)
  - 좌표: `PositionCells` L190–226
  - EH 규칙: `GoalCells.learn_goal` L149–168, ACh 억제 `decay_goal` L170–177
  - NAVIGATE: `symbolic_motor_controller` L494–502
  - β 혼합: `ActorCells.move` L474–492
  - TD critic/actor: L504–507, L540–550
  - gate: `BumpAttractorCells` L237–307. gate는 `np.random.choice`로 고르므로 논문의 "algorithmic" 진술과 일치합니다.
  - reservoir: L553–594(고정 가중치)
  - NM의 place cell shuffle: `flip_pcs` L630–634
  - `6pa/6pa_res.py` 프로토콜은 논문과 일치합니다(trsess=20, 평가 2 session, probe [2,9,16]).
- **논문–코드 불일치·재현 위험**
  - reservoir 크기: 논문 N=1024, `utils.py` 기본값 `nrnn=1000`이며 6pa·dmp 스크립트는 덮어쓰지 않습니다.
  - eligibility trace: 논문 τ_e=1000 ms, 코드 기본값 `xytau=200`이며 어느 실험 스크립트도 덮어쓰지 않습니다.
  - 12NPA 학습률: 논문 7.5e-5→5e-5(이미지 확인), 코드 `12pa_res.py` L230은 7.5e-6(코멘트 "5e-6")입니다. 10배 차이이며, 갱신에 tstep(20)이 곱해지는 단위 관례 가능성은 [OPEN]입니다.
  - TD 오차 scaling: 코드는 `/tstep`(L542)과 `×tstep`(L549)을 쓰고 논문 Eq 36–37에는 dt 인자가 없습니다 [OPEN, 관례 차이 가능성].
  - README 실행 규칙과 모순: 모든 실험은 repo 루트에서 실행하라고 하지만 `model.py` L468이 `'../motor_controller/…'`(cwd 상대)를 로드해 `usenmc=True`가 문서대로는 실패합니다. 수정은 `./motor_controller/…` 또는 npz 가중치(`convert_numpy.py`)를 쓰는 것입니다. TF SavedModel은 신뢰 불가 바이너리라 로드하지 않았습니다.
  - README는 Python 3.7이라 하지만 `requirements.txt`는 `tensorflow==2.12.0`입니다(Python ≥3.8 필요).
  - README 과제 목록에 session 수가 17/47로 적혀 있으나 스크립트·논문은 20/50입니다. `wkm_da_dist_res.py`라고 안내하지만 실제 파일은 `wkm_dist_da_res.py`입니다.
  - n=720/480: 스크립트 기본 `btstp`는 96(6pa)/24(dmp)/1(wkm)입니다. `gen_fig/*.py`는 로컬 Windows 경로(`D:/Ganesh_PhD/…`)의 pickle을 합치고 seed 없이 `totiter`(720/480)로 무작위 부분표본(`dmp_fig.py` L34·L51, `6pa_fig.py` L31)을 뽑습니다. repo만으로 n과 표본을 재현할 수 없습니다. `dmp_fig.py` L126–128은 t-test에 n=480을 하드코딩합니다(totiter=720).
  - 2NPA 지표는 새 cue만 셉니다.
- LICENSE 없음.
- 실행성 [PROPOSAL/추정, 미실행]: README 기준 CPU로 충분합니다(TF2.12, agent당 약 45–90분, 서버에서 96 agent 병렬). 배치 1의 순차 시뮬레이션이라 RTX 5070 Ti는 이득이 적습니다. 스모크 테스트는 `btstp=1`과 `time` 단축으로 가능하고, 전체 n=720은 CPU 클러스터 예산이 필요합니다(미측정).

---

### C. 자체 점검

**sha256sum -c** (각 폴더에서 `sha256sum -c SHA256SUMS.txt` 실행, 종료코드 0)
- TEM20: 9/9 OK
  - download 7개: biorxiv v2 PDF, biorxiv API json, europepmc XML, europepmc meta json, openalex json, ORA VoR PDF, ScienceDirect mmc1 PDF
  - `fulltext.txt`, `supp_fulltext.txt`
- KUMAR26: 18/18 OK
  - download 16개: arXiv v1–v5 PDF, abs HTML 6개, API xml, EPMC search json, openalex json, JN 페이지 HTML 2개
  - `fulltext.txt`, `supp_fulltext.txt`
- SHA256SUMS는 `download/*`, `fulltext.txt`, `supp_fulltext.txt`를 포함합니다. `access.json`·`extraction.json`은 스펙대로 해시 대상이 아닙니다.

**access.json 키**: 두 파일 모두 고정 15개 키(id, status, route, url, files, version, version_date, vor_or_preprint, vor_diff_note, pages, words, sections_read, supplementary, attempted_routes, code)가 순서대로 있습니다. TEM20은 `pages=null`(사유는 `vor_diff_note`에 기재)이고, KUMAR26의 전 버전 이력은 `version` 필드에 문자열로 넣었습니다.

**정리한 항목**: 에러 HTML이 PDF 확장자로 저장된 2개(Europe PMC supplementaryFiles 500, J Neurosci supplement 403)와, PDF와 byte-identical한 arXiv e-print 1개는 삭제했습니다. 모두 `attempted_routes`에 기록했습니다. 렌더링 PNG는 삭제했습니다(`pdftoppm -f N -l N -r 100 -png`로 재생성 가능).

**불확실·미해결**
1. KUMAR26 J Neurosci VoR 본문·그림·supplement 미확보. v5의 front matter는 일치하지만 본문 일치는 미검증입니다.
2. KUMAR26 v2–v4는 abstract·절 제목·키워드 비교만 했고, v1은 일부만 읽었습니다.
3. TEM20은 그림 패널을 개별로 읽지 않았고 seed·독립 네트워크 수 정보가 없습니다. bioRxiv v2와 VoR의 exhaustive diff도 하지 않았습니다.
4. KUMAR26 본문의 "±" 정의가 불명확합니다(범례는 95% CI 또는 SE).
5. 논문–코드 불일치의 원인(KUMAR26: N 1000/1024, τ_e 200/1000, 12NPA 학습률 10배, TD dt scaling. TEM20: lr 값, grad/Hebbian clip, p L1 정규화, 4-lap reward loss 가중)은 판정 불가 [OPEN]입니다.
6. 코드는 실행하지 않아 실행성 평가는 모두 비측정 추정입니다.
7. 실행 중 호스트 자원 압박 훅이 Bash 호출 1회를 차단했습니다(재시도로 정상 진행, 데이터 손실 없음).

**근거 명령**: `curl`(OpenAlex, Europe PMC, arXiv, ORA, ARS CDN), `pdftotext -layout`, `pdfinfo`, `git clone --depth 1`, `git rev-parse HEAD`, `sha256sum -c`, `python3 -I jats2txt.py`·`make_access.py`(`_scripts/W4/`). 스크래치 텍스트는 `_scripts/W4/work/`에 있습니다.
