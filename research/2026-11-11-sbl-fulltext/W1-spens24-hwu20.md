# SPENS24, HWU20 — 해마–피질 공고화와 schema 의존 부호화

> 2026-11-11 SBL 원문 검토 워크플로에서 worker가 쓴 보고를 마스터가 원문 대조로 검수해 옮겼다. 종합은 [2026-11-11-sbl-fulltext-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext-review.md)에 있다.
>
> `fcl-sbl-fulltext-20261111/...` 경로는 저장소 밖 호스트 작업 폴더다. 원문은 저작권 때문에 저장소에 넣지 않았다. 판본과 해시는 [evidence.json](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/evidence.json)에 있다.
>
> 표기: 필드 1–10·12는 별도 표기가 없으면 원문 사실(LITERATURE, 위치 병기)이다. 일부 문장은 우리 산술·추론(PROPOSAL), 코드 독해(CODE), 그림 판독(FIGURE-READ)인데 표시가 빠져 있다. 그 목록은 [W7-remediation.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/W7-remediation.md) §2.4에 있다. 필드 11은 PROPOSAL이다.

---

## W1 보고: SPENS24 + HWU20 (해마-피질 공고화·schema 의존 부호화)

### 0. 결론 요약
- 원문 2편을 전문으로 읽었다. SPENS24는 OA VoR와 Supplementary Information(SI)을, HWU20은 저자 호스팅 VoR와 ESM, 그리고 bioRxiv v1 대조본을 읽었다.
- 공식 코드 2건이 모두 존재한다(논문 본문의 링크). 둘 다 LICENSE가 없다. 코드는 읽기만 했고 실행·설치는 하지 않았다.
- 주장 11개 판정:
  - S1~S5(SPENS24)는 전부 CONFIRMED.
  - H1·H2는 CONFIRMED.
  - H3는 CONFIRMED이되 메커니즘을 정밀화했다. 조절 대상은 학습률이 아니라 replay epoch 수다.
  - H4·H5·H6은 PARTIAL.
- "novelty가 학습률을 바꾸는 식"은 두 논문 모두에 없다.
  - SPENS24는 재구성 오차 임계값으로 저장 대상을 고른다. VAE lr은 1e-3으로 고정이다.
  - HWU20은 Eq.9–10 `epochs = e_default + (x_novelty·x_familiarity)·e_boost`다. η_CHL 자체는 고정이다.
- 두 논문 모두 "학습된 schema가 고정·무구조 대조보다 낫다"는 증거가 없다(Melete 계보와 같은 주의).
- 논문-코드 불일치가 다수다. 특히 HWU20은 Table 1의 N_multimodal 40이 코드와 그림의 80과 다르다. VoR §4.5–4.6 실험은 코드가 미공개다.

---

### 1. SPENS24 — Spens & Burgess, Nat Hum Behav 8(3):526–543 (2024)

#### 접근 증거
- route: Nature OA VoR PDF(CC BY) `https://www.nature.com/articles/s41562-023-01799-z.pdf`
  - SI(MOESM1)와 Reporting Summary(MOESM2)는 Springer static-content에서 받았다.
  - Europe PMC JATS XML(PMC10963272)로 교차 확인했다.
- version: VoR. 2024-01-19 온라인 게재(received 2023-05-30, accepted 2023-12-05).
- pages 20: 본문 526–543이 PDF 1–18쪽이고, Reporting Summary 2쪽이 끝에 포함돼 있다. `file`은 33쪽이라 하지만 pdfinfo가 20이다.
- words: fulltext 18,075 / supp 2,734.
- 읽은 범위: 초록~Discussion, Methods 전부(Data, Basic model, Extended model, Carmichael, DRM), SI 9쪽 전부. Fig.3·5와 SI Fig.S1·S2는 이미지로 확인했다.
- 불가 경로:
  - bioRxiv v1(2023-01-20)·v2(01-21)·v3(05-30)은 HTTP 429(Cloudflare 1015)라 못 받았다. 따라서 preprint와 VoR의 차이는 알 수 없다.
  - PMC PDF는 reCAPTCHA 페이지여서 폐기했다.
- UCL accepted manuscript와 문장 단위로 비교했다. 556 vs 555문장 중 약 30개가 달랐는데, 표본은 인용 위첨자 등 형식 차이였다.
- sha256 앞 16자리:

| 파일 | sha256[:16] |
|---|---|
| nature_spens24_vor.pdf | b78a62b28775ec55 |
| supp_MOESM1_ESM.pdf | 6f9baebc2f95492b |
| supp_MOESM2_ESM.pdf | a9b713fbc8d39e24 |
| europepmc_PMC10963272_fullTextXML.xml | 54053fdbfe441cf7 |
| ucl_discovery_10186145.pdf | 205bdb93003ecaab |
| nature_spens24_article.html | aa3d76fb4b6fa364 |
| openalex_spens24.json | ae9657944dacd38f |
| biorxiv_api_details_….json | ada59062ee180ea4 |
| github_api_ellie-as_….json | a4843b996186e80f |
| fulltext.txt | 99812aa6b0efa3bd |
| supp_fulltext.txt | 5e7f7efb37917f11 |
| (aux) fulltext_from_jats_xml.txt | fe14ef31a4656b18 |
| (aux) extraction.json | f704cc90ee74f229 |
| (aux) access.json | 050a5a1b6e63cfa9 |

#### 필드 1–12
**1. 서지**
- 첫 공개: bioRxiv 2023-01-20. peer review(Gido van de Ven 외 익명 1인, p.543). 라이선스 CC BY.
- 코드: `github.com/ellie-as/generative-memory`, commit `0aaa08466af59599f8ca0c73aca94189ea7d4772`(2025-03-26), LICENSE 없음.

**2. schema 정의와 위치** [LITERATURE]
- p.527: schema는 "rules or priors (expected probability distributions) for reconstructing a certain type of stimulus"다. 구현체는 generative network(VAE)다.
- 위치는 encoder·decoder 가중치와 연속(Gaussian-regularised) 잠재변수다. 20차원이고, DRM은 300차원이다.
- 제안된 해부학 위치는 EC·mPFC·alTL이다.
- concept(범주)와 schema(재구성 방법)를 구분한다.
- 이산 schema 단위는 없다. 데이터셋당 VAE 1개이고 생성·병합·분할도 없다.

**3. 아키텍처**
- fast: continuous MHN, 데이터셋당 1개. 10,000 패턴 × 12,288차원, one-shot 저장, 학습 가중치 없음.
- slow: conv VAE.
  - Shapes3D 64×64×3, latent 20, trainable 약 1.18M. 내 산술이며 SI 층 목록 기준이다.
  - MNIST용 소형 VAE와 DRM용 dense VAE(latent 300, 어휘 4,206)도 있다.
- extended model의 MHN은 [희소 sensory 잔차 ; latent] 연결 벡터를 저장한다. 이때 VAE는 동결된다(p.538).
- 다중 VAE(EC/mPFC/alTL)는 제안만 있고 구현은 없다.

**4. 학습 규칙** (outer loop와 within-lifetime 분리)
- outer loop(meta-learning)는 없다. slow는 일반 backprop이고 fast는 one-shot 저장(학습률 없음)이다.
- MHN 갱신은 SI p.8 Eq.3 `ξ_new = X softmax(β Xᵀ ξ)`, β=20(p.537)이다.
  - 코드는 logit을 √d로 나눈다(`hopfield_models.py` L264-265). d=12,288이면 β_eff=0.18이다.
- VAE 손실은 `E[Σ_pixel mean_ch |x−x̂|] + w_KL·KL`, w_KL=1이다(p.537, `generative_model.py` L110-128).
  - 옵티마이저는 AMSGrad Adam, lr 1e-3, ≤50 epoch다.
  - batch 32와 early stopping(patience 3)은 코드에만 있다.
- 시간 순서는 엄격히 순차다.
  1. 10,000장을 MHN에 저장한다.
  2. 균일 noise cue 10,000개를 한 번만 넣어 MHN 출력을 replay 집합으로 만든다(`max_iter=10`, 매 epoch 재사용, p.537).
  3. 그 집합으로 VAE를 학습한다.
- 새 사건과 교차하는 replay는 없다. 시간 규모를 나타내는 식도 없다. "시간에 따른 의존 증가"는 곧 VAE epoch이다(Fig.3a).

**5. 형성·선택·적용·개정**
- schema가 새 기억 부호화를 바꾸는가: 그렇다. extended model에서만이다.
  - 식(`extended_model.py` L27-52): `x̂=Dec(μ_Enc(x))`, `mask_p=1[mean_c|x_pc−x̂_pc|>θ]`, `trace=[mask⊙(2x−1) ; μ_Enc(x)]`.
  - 회상은 latent를 decode한 뒤 저장된 sensory 예외로 덮어쓴다(L122-123).
  - 결과적으로 consolidation 전에도 prototype 쪽으로 왜곡된다(Fig.5a,b p.532; Fig.6 p.533).
  - θ는 0.03/0.15(Fig.5a,b), 0.01~0.2(Fig.5c), 0.2(Carmichael)다.
- 이 gating은 "저장 대상" 선택이다. 학습률 조절 식은 없다.
- Discussion p.536은 임계값이 중요도·주의·감정에 따라 달라질 수 있다고 예측만 한다. 시뮬레이션은 없다.
- assimilation/accommodation 구분과 schema revision은 없다. 시험 중 VAE도 갱신되지 않는다.
- "schema 일치 사건이 더 빨리 consolidate"는 인용된 배경일 뿐(p.527) 실험이 없다.

**6. 지속성**
- VAE 가중치의 parameter 변화로 남는다. MHN은 lookup 저장소다.
- decay·deletion·capacity는 시뮬레이션하지 않았다(p.527, p.537).
- 학습 중 latent가 불안정하다는 점을 저자가 인정한다(p.538).
- generative replay는 제안만 있고 구현은 없다(p.536, p.538).

**7. 과제·결과(분모 포함)**
- Fig.3a (p.530-531):
  - 의미 decoding 정확도 r_s(48)=0.997이다. 단일 학습 run의 50 epoch이며 계열 상관이 있다.
  - 레포 `outputs/decoding_accs.csv`(n=50): 첫 값 0.378(미학습 encoder, `on_epoch_begin` 측정), 마지막 0.827. 내가 재계산한 Spearman은 0.9970으로 논문과 일치한다.
- SI Fig.S2 (p.4):
  - 4-class SVM, 학습 예시 N=10~1,000. 단일 run, 오차막대 없음.
  - 그림에서 읽은 근사값(200개 기준): latent ≈0.855, conv4 ≈0.77, conv1 ≈0.58, 입력 픽셀 ≈0.43.
  - 무학습·무schema 대조는 epoch-0 한 점(0.378)뿐이다.
- Fig.4 (MNIST, p.531-532): 클래스 내 분산이 감소한다. paired t(7,839)=60.523, d=−0.684. 7,840 = 10클래스×784픽셀이며 픽셀을 독립 표본으로 취급했다.
- Fig.4g: 논문은 zoom 수준당 200장이라 쓰지만 notebook 4는 `range(500)`이다.
- Fig.5c (p.532-533):
  - 100장, 임계값 5개. r_s(3)=−1과 +1, "P<0.001"이다.
  - n=5일 때 |ρ|=1의 정확 순열 two-sided 최소 p는 2/120=0.0167이다(내 산술). 따라서 "P<0.001"은 t 근사값이다. 임계값이 실험자 지정이므로 단조 추세 예시이지 추론 검정이 아니다.
- Fig.6 (Carmichael): 정성적이다. notebook 3은 조건당 4개 장면, β 기본값 5를 쓴다.
- Fig.7 (DRM, p.533-534):
  - 20 list×15단어. 연관어 수 3~14에서 lure 회상 확률 r_s(10)=0.998이다. 이는 list 길이와 모델 출력의 상관이며 인간 데이터와의 적합이 아니다.
  - n마다 400 trial이다.
  - SI Fig.S1(18 list)을 눈으로 세면 lure가 0.5를 넘는 list는 약 4개(cold, chair, fruit, music)다. "often"은 과장일 수 있다.
- 정직한 대조가 부족하다: 다중 seed 없음, 학습된 schema 대 고정 특징의 ablation 없음.

**8. 신경과학 대응** [LITERATURE]
- MHN=해마, VAE latent=EC/mPFC/alTL은 mechanistic 제안이다.
- boundary extension·Carmichael·DRM은 인간 데이터와 정성적 유사성만 보인다. 정량 적합 통계는 없다.

**9. 한계와 미증명**
- 저자 명시(p.536-537):
  - 후속 항목: 연속 평생 공고화(latent 불안정, catastrophic forgetting), 순차 구조 미모델.
  - VAE는 "illustrative"이고 "not optimized"다.
- Reporting Summary: "sample sizes sufficient to give statistically significant results were chosen".
- 미증명: 다중 seed 변동, 연속 공고화, MHN capacity·간섭, schema 개정, 추론 compute, schema 일치/불일치 공고화 속도.

**10. 주장표**

| ID | 주장 | 판정 | 위치 | 근거 |
|---|---|---|---|---|
| S1 | 해마 빠른 기억=MHN | CONFIRMED | p.530, p.536-537, SI p.5-8 | "modelled as an MHN", one-shot. 단 코드의 learn()은 패턴 보관뿐이고 capacity는 미시험 |
| S2 | 피질 schema=VAE 연속 잠재분포 | CONFIRMED | p.527, p.536-537 | VAE 구현. 단 "illustrative", 다른 잠재변수 모델도 유사하리라 기대 |
| S3 | 공고화=replay 기반 teacher–student | CONFIRMED | p.537 | MHN=teacher, VAE=student. replay는 noise cue 1회 집합 |
| S4 | schema=공통 생성적 확률 구조 | CONFIRMED | p.527 | 데이터셋 하나의 10,000 사건을 일괄 학습 |
| S5 | 코드 공개 | CONFIRMED | p.539, Reporting Summary | 링크와 repo 모두 존재. README는 "four notebooks"라 하나 실제 6개+DRM notebook이다. MNIST 학습 경로와 ROCStories는 repo에 없다 |

**11. FCL 연결** (전부 [PROPOSAL])
- DQ1: schema=slow 생성 모듈(가중치+연속 latent)이고, fast 저장소에는 concept 코드와 예외 잔차를 둔다.
- DQ3: 요소별 예측오차 mask + 임계값을 fast memory(Titans류)에 쓰는 hard novelty gate로 차용할 수 있다.
  - 단 θ가 전역 고정값이므로 FCL에는 context별 θ 컨트롤러가 필요하다.
  - 학습률 조절은 빌릴 것이 없다.
- DQ4: Sleep=fast 저장소 cue-replay로 slow 학습(teacher–student). 오차가 낮아지면 fast 슬롯을 비운다(미검증).
  - 간극: 새 사건과의 interleaving이 없고 generative replay는 제안뿐이다.
- DQ6(H-SAMPLE): schema latent 위의 few-shot 곡선(Fig.S2)이 싼 진단이다. 단 random-init·no-replay 대조를 직접 추가해야 한다.
- DQ7: 저장된 latent는 slow 모듈이 갱신되면 낡는다. 재인코딩 또는 안정적 concept 층이 필요한 failure mode다.
- DQ8: schema 과적용 진단으로 prototype 수축(클래스 내 분산), boundary extension/contraction 비, Carmichael식 context 편향, DRM식 lure 침입을 차용한다.
- H-COMPUTE: [OPEN] 추론 비용이나 품질-compute 측정은 없고 trace 차원 대 오차(Fig.5c)만 있다.
- failure mode 요약:
  - 학습 중 latent drift
  - 전역 임계값
  - 틀린 schema가 prototype을 강제하는 위험(예외 저장으로만 완화)
  - MHN β 스케일 민감성

**12. 재현**
- 환경: TF 2.11 / Python 3.10.9 / TFDS. Shapes3D·MNIST는 자동 다운로드되고 ROCStories CSV는 repo에 없다.
- 규모: MHN 패턴 행렬 0.98GB(float64). replay는 10,000 cue × 10회 반복의 10,000×12,288 matvec이다.
- 판단(측정 안 함): CPU로 가능하다.
- RTX 5070 Ti(Blackwell)에서 TF 2.11 GPU 지원은 기대하지 않는다(내 추론). PyTorch 포팅이 현실적이다.
- 키 파일↔식:
  - `hopfield_models.py` L206-265: MHN
  - `end_to_end.py` L73-124: replay와 학습
  - `generative_model.py` L110-168: loss
  - `extended_model.py` L27-135: novelty mask·recall
  - `drm_modelling/`: DRM

**코드 감사 (논문-코드 불일치 상위)**
- extended MHN의 β가 논문에 없다. 코드 기본값은 100, Carmichael은 5, DRM은 100 비정규화다.
- 정규화 default=True 경로의 √d 스케일은 위 §4에 적었다.
- `softmax_unnormalized`에 `self`가 빠져 있다(L261). DRM 폴더의 복사본은 고쳐져 있다.
- decoding callback은 `on_epoch_begin`인데 논문은 epoch 종료 시점이라 쓴다.
- MNIST 복제 불가: repo는 'shapes3d'만 지원하고 MNIST는 가중치만 제공한다.
- DRM의 undisclosed 처리:
  - DRM 단어를 하나라도 포함한 story만 사용한다(`data_preparation.py` L19).
  - DRM VAE의 KL 가중치는 0.001이다.
- 기본값 `use_weights=True`라서 notebook 1은 제공된 가중치를 그대로 쓴다.
- 나머지 상세는 `fcl-sbl-fulltext-20261111/SPENS24/extraction.json`에 있다.

---

### 2. HWU20 — Hwu & Krichmar, Biol Cybern 114(2):169–186 (2020)

#### 접근 증거
- route: UCI Cognitive Robotics Lab 저자 호스팅 Springer 형식 PDF.
  - URL: `https://sites.socsci.uci.edu/~jkrichma/Hwu-Krichmar2020_Article_ANeuralModelOfSchemas.pdf`
  - ESM1은 Springer static-content에서 받았다. VoR 대조를 위해 bioRxiv v1(Wayback 스냅샷 20260920211003)을 전문으로 읽었다.
- version: VoR(저자 호스팅본). 2019-11-04 온라인(received 2019-04-21, accepted 2019-09-24). pages 18, words fulltext 11,418 / supp 94.
- 불가 경로:
  - Springer 본 페이지는 bot wall(Client Challenge)이다. 저자 호스팅본과 Springer 본이 동일하다고 가정한다(메타데이터와 쪽수는 일치).
  - bioRxiv 직접은 429였다. OA는 아니며 PMC에도 없다. 공식 preprint는 v1 하나뿐이다.
- 읽은 범위: 초록, §1~§5.6 전부, Table 1, Algorithm 1, ESM Fig.S1. Fig.5-7, 10-15는 이미지로 확인했다.
- sha256 앞 16자리:

| 파일 | sha256[:16] |
|---|---|
| uci_author_…Article_ANeuralModelOfSchemas.pdf | 1cd49f48cd3bcb31 |
| springer_ESM1_…MOESM1_ESM.pdf | e86b53cfaf8455e3 |
| biorxiv_434696_v1.pdf | 0575d706bb89b189 |
| …v1_wayback_20260920211003.pdf.gz | 76223a50ed5b943e |
| openalex_hwu20.json | 3a0b252cc1b52b43 |
| europepmc_search_vor_doi.json | 3f5c04ba7c26057d |
| europepmc_search_preprint_doi.json | 63e67f50d78c8f52 |
| semanticscholar_hwu20.json | a88d300122785c7d |
| biorxiv_api_details_434696.json | b5dcb6bcb06fd6fc |
| wayback_availability….json | 1cdedf78bb9dea3f |
| github_api_fitany_SchemaNetworkBICY.json | 35ece1d57ebb074b |
| github_api_users_fitany_repos.json | 5f81394c34eef9c1 |
| github_api_orgs_UCI-CARL_repos.json | ec32344def3cd9b0 |
| fulltext.txt | 33a7d7d2bd2d71d1 |
| supp_fulltext.txt | f4809b5b2b855aaa |
| (aux) fulltext_preprint_v1.txt | ed81c2ef3e17baa0 |
| (aux) extraction.json | f337efea7cdb83ba |
| (aux) access.json | 5ae5470ce0a2e678 |

#### 필드 1–12
**1. 서지**
- 첫 공개: bioRxiv v1 2018-10-04. 제목이 "…Memory **Consolidation**"이었다가 VoR에서 "…**Encoding**"으로 바뀌었다.
- 후원: US Air Force/DARPA, Toyota, HRL.
- 코드: `github.com/fitany/SchemaNetworkBICY`(논문 §3.5 p.176), commit `972d44844017f3ad52757dd55133d5fcbeafd078`(2019-10-10, 단일 commit "first commit"), MATLAB, LICENSE 없음.

**2. schema 정의와 위치** [LITERATURE]
- p.170: "a schema is a spatial arrangement of food wells". 입력은 5×5 이진 context pattern이다.
- schema는 세 곳에 걸쳐 있다.
  - 이긴 mPFC 뉴런 1개(10개 중 ReLU+hard WTA, Hebbian)가 이산 schema id다.
  - 그 뉴런이 vHPC를 거쳐 고르는 고정 희소 AC gating mask.
  - AC/action 가중치와 dHPC triplet 인덱스에 저장된 paired association(PA).
- 이산 id + 연속 가중치의 hybrid다. 연속 schema 공간은 없다.

**3. 아키텍처**
- indexing stream: context(25) → mPFC(10) → vHPC(5) → dHPC(40, 입력은 vHPC+cue 18+well 25). novelty/familiarity 모듈이 여기서 갈라진다.
- representation stream: cue(18)+mPFC → AC(multimodal) → action(25 wells). CHL로 학습한다.
- Table 1(p.175): N_multimodal=40. 그러나 코드(`size_multimodal=80`)와 Fig.6·ESM Fig.S1의 축은 80이다. Table 1이 논문 자체의 그림과 모순이다.
- 고정/학습:
  - vHPC→AC gating은 정적이다(w_inh=−10, 일부 0).
  - 공개 코드에서는 mPFC→vHPC도 학습되지 않는다(`explore.m` L44는 정규화만).
  - 나머지는 모두 가소성이다.

**4. 학습 규칙** (outer loop와 within-lifetime 분리)
- outer loop·meta-learning은 없다. 하이퍼파라미터는 수동 설정(Table 1)이다. 모든 학습은 within-lifetime이다.
- Eq.1 (CHL 갱신): `x_k(t)=f(W_k x_{k−1}+γ W_{k+1}ᵀ x_{k+1})`, T_s=5.
- Eq.2: `ΔW_k=η_CHL(x̂_k x̂ᵀ_{k−1} − x̌_k x̌ᵀ_{k−1})`.
  - 코드는 `lr·g`를 곱한다. lr=2, g=.001이므로 실효 0.002이고 Table 1의 η_CHL .001과 다르다.
  - preprint Eq.2는 부호가 반대(−η)였고 VoR에서 고쳐졌다(이미지로 확인).
- Eq.3-6: ReLU, hard WTA, Hebbian `ΔW=η x xᵀ`, 행 단위 정규화. mPFC는 η_pattern=1e-4, dHPC는 η_indexing=0.1.
- fast와 slow의 시점:
  - 한 trial(=Tse의 하루) = ≥600 epoch이다.
  - 매 epoch마다 indexing 단계(fast, Hebbian) → CHL free → CHL clamped → 갱신이 일어난다.
  - dHPC 인덱스가 clamped 단계에서 action 층의 target을 준다(`chl.m` L22). 이것이 teacher 역할이다.
  - 따라서 별도의 오프라인 sleep 단계는 없다. "waking과 sleeping의 구분이 없다"(p.170).
- novelty→학습량 식:
  - Eq.7 `ΔW_nov=−η_indexing x_nov x_dHPCᵀ`. 단위 활성이면 노출당 ≈0.9배로 감소한다(내 산술).
  - Eq.8 `x_fam=σ(s(W_fam x_mPFC−x_shift))`, s=200, x_shift=.03.
  - Eq.9 `NM=x_nov·x_fam`.
  - Eq.10 `epochs=e_default+NM·e_boost`. NM은 trial의 첫 e_settle=20 epoch 중 최댓값이다. 코드: `explore.m` L47-70.
  - e_default=600, e_boost=1000(Table 1). 코드는 `boost_epochs=2000;%1000`이다.
  - η_CHL은 NM으로 조절되지 않는다. 학습량은 epoch 수로 조절된다. preprint Eq.10에는 e_boost가 빠져 있었다.

**5. 형성·선택·적용·개정**
- 형성: context pattern에 대한 경쟁 Hebbian WTA다. 맞는 뉴런이 없으면 새 승자가 뽑힌다(Fig.11B p.182). 별도의 novelty 임계값이나 split/merge는 없다.
- 선택: 같은 context는 같은 승자로 간다. trial 38에서 Schema A로 돌아오면 원래 인덱스가 복귀한다.
- 적용: 승자 → vHPC → 정적 희소 억제 mask. 이 mask는 CHL clamped 단계에서만 걸린다(`chl.m` L21). free 단계(L5)와 `testSchema`는 gating이 없다.
- assimilation: 5 PA 중 2개를 교체한 familiar schema에서는 mPFC 승자가 유지된다(활동만 감소). novelty와 familiarity가 모두 높으므로 NM이 급등한다(Fig.10-11).
- accommodation: 새 schema B는 새 승자를 얻는다. familiarity≈0이므로 Eq.9에 따라 NM≈0이고 기본 600 epoch이다. B는 A와 같은 속도로 학습된다(trial 16에서 ≈0.78 대 ≈0.77, Fig.5b/7a 근사). 즉 새 schema에는 가속 이득이 없다.
- 불일치 schema: preprint 실험 3(맛 위치를 뒤섞은 schema)에서 일관 schema의 새 PA가 더 잘 학습된다(preprint Fig.8C 근사: ≈0.51 대 ≈0.31). VoR에서는 이 실험이 삭제됐고 코드(`reproduce_tse_figures_chl.m` L586-915)에는 남아 있다.

**6. 지속성**
- parameter 변화로 남는다. Fig.5d,e에서 하루 뒤 HPC lesion과 control 모두 새 PA를 유지한다. 이것이 해마 없이 가능한 공고화다.
- HPC lesion은 새 PA와 Schema B 학습을 막는다.

**7. 과제·결과** (분모: 20 simulated rats = 무작위 초기화 20개, 벡터화 실행, RNG seed 없음)
- 오차막대 정의는 논문에 없다(코드는 std/√20). 통계는 논문이 Wilcoxon rank-sum+Bonferroni, p≪.001이라 쓴다(p.176). 코드에는 `ttest`·`kstest2`·`anova1`만 있다.
- 아래 수치는 그림에서 읽은 근사값이다.
- Exp1 (Fig.5, p.177): 성능(정답 well 활동/5개 well 합, 우연 수준 0.2).
  - Schema A는 20 trial 동안 0.28에서 0.82로 오른다.
  - Probe test PT1/2/3(cued/non-cued): 0.34/0.16, 0.63/0.09, 0.77/0.05.
  - 새 PA 1 trial 후(PT4): new-cued 0.53, new-non-cued 0.18, original 0.09.
  - 논문은 이를 "약 200% 증가"라 설명한다.
  - lesion 후 Schema A: 두 군 모두 ≈0.90. PT6에서 control의 new-cued ≈0.51, HPC-lesion ≈0.08.
- Exp2 (Fig.7, p.179): Schema B(control)는 0.26에서 0.78로 오른다. HPC-lesion은 0.2에 머문다. A 재학습 시 두 군 모두 ≈0.9이므로 망각이 거의 없다.
- §4.4 flat-epoch ablation (Fig.12, p.183): 새 PA probe의 cued/non-cued/original.

| 조건 | 평균 총 epoch | cued/non-cued/original |
|---|---|---|
| 원본(neuromodulated) | 13,875 | ≈0.49/0.16/0.12 |
| flat 400 | 8,400 | ≈0.20/0.18/0.21 |
| flat 800 | 16,800 | ≈0.37/0.18/0.15 |
| flat 1600 | 33,600 | ≈0.43/0.22/0.12 |

  - 저자도 "neuromodulator는 빠른 학습에 필수가 아니다"라고 쓴다(p.179). neuromodulator는 총 epoch을 절약한다.
- §4.5 sparsity (Fig.13): schema 3개×10 trial, P를 0~1로 변화.
  - P=0은 학습이 없다.
  - P=1은 피크 ≈0.91~0.93이었다가 다음 schema 뒤 ≈0.35~0.38로 떨어진다.
  - P=0.3(전 실험의 사용값)은 A가 ≈0.65에서 ≈0.5, 다시 ≈0.42로 내려가고 B는 ≈0.66에서 ≈0.45가 된다.
  - 내 산술로 above-chance 이득의 유지율은 P=0.3에서 약 49%, P=1에서 약 21%다. 즉 gating은 상대 유지율은 높이지만 피크를 낮추고 망각을 없애지 못한다.
- §4.6 mPFC 크기 (Fig.14-15):
  - 크기 1이면 비중첩 schema 셋이 모두 ≈0.9~0.95이고 망각이 0이다. 크기 3·5의 ≈0.65보다 높다. 단일 공유 mask 때문이다(p.180).
  - 중첩 schema에서는 크기 1이 A를 잃지만(≈0.9에서 ≈0.35), 크기 2~5의 최종값도 ≈0.3~0.45로 차이가 작다.

**8. 신경과학 대응**
- Tse et al. 2007 probe test 양상의 정성적 재현이다.
- 숫자는 다르다고 저자가 인정한다(p.176): 모델의 original-well dig time은 우연 수준보다 훨씬 낮고, 모델은 Schema A를 ≈0.9 유지하나 쥐는 ≈0.5다(p.180).
- neuromodulator=novelty×familiarity를 LC/BF/VTA에 대응시키는 것은 추측적 mapping이다(p.181-182).
- HPC의 광범위한 억제가 근거가 약하다는 점도 저자가 인정한다(p.172).

**9. 한계와 미증명**
- 저자 명시:
  - "numerical results varied"(p.176)
  - 원래 버전 CHL을 단순화해 사용(p.171)
  - 후속: 분산 mPFC 부호화와 thalamus(p.184), 경로계획 없음(p.185)
- 미증명:
  - baseline 학습기(무gating CHL/backprop, EWC)와 표준 continual-learning 벤치마크가 없다.
  - toy 과제(5×5, 5 PA/schema, ≤3 schema, one-hot cue)뿐이다.
  - VoR에는 같은 새 PA를 불일치 맥락에 두는 대조가 없다(preprint에만 있었음).
  - schema 개정·분할·병합이 없다. 연속 schema도 없다.
  - Fig.13-15에는 통계·오차막대가 없다. 오차막대 정의와 seed도 명시가 없다.
  - lesion 결과는 구조상 필연이다. dHPC 없이는 clamped target이 없어 CHL 갱신이 0이다(`chl.m` L20-25).
  - 추론 compute 측정이 없고 절감은 학습 epoch뿐이다.

**10. 주장표**

| ID | 주장 | 판정 | 위치 | 근거 |
|---|---|---|---|---|
| H1 | 해마+mPFC indexing | CONFIRMED | 초록 p.169, §3.1 p.171-172 | "two processing streams of indexing and representation". 단 코드에서 mPFC→vHPC 인덱스는 학습되지 않고 고정 무작위 hash다 |
| H2 | representation stream | CONFIRMED | §3.2 p.172 | cue+mPFC→AC→action, CHL, dHPC가 clamp |
| H3 | 친숙/새로움 neuromodulation으로 부호화 조절 | CONFIRMED(정밀화) | §3.3 p.172-174 Eq.7-10 | NM=novelty×familiarity가 replay epoch 수를 정한다(학습률 아님). 필수가 아니라 epoch 절약(p.179) |
| H4 | context-dependent gating으로 간섭 억제 | PARTIAL | §3.2, §4.2, §4.5-4.6, Fig.7·13-15 | A는 B 이후에도 ≈0.9 유지(Fig.7c). 그러나 P=0.3에서 이전 schema가 ≈0.2 하락. mask 종류는 vHPC 5개로 제한. 중첩 schema는 실패. mPFC=1(단일 mask)이 비중첩에서 망각 없음 |
| H5 | schema 일치 경험을 더 빨리 학습 | PARTIAL | §4.1 p.176-177 Fig.5c, Fig.12, preprint Exp.3 | 새 PA가 1 trial에 ≈0.53. 단 "familiar AND novel → 더 많은 epoch"이라는 구성의 결과이고, flat 800~1600 epoch도 학습한다. VoR에는 불일치 대조가 없고 새 schema B는 A보다 빠르지 않다 |
| H6 | catastrophic forgetting과 연결 | PARTIAL | 초록 p.169, §4.5-4.6 | 동기와 toy 증거. 망각은 줄지만 남는다. CL baseline·벤치마크 없음. 초록의 "preventing"은 강한 표현이다 |

**11. FCL 연결** (전부 [PROPOSAL])
- DQ2: context 코드에 대한 hard-WTA 경쟁학습으로 schema id를 만들고, id→고정 희소 mask로 은닉 유닛의 선택적 갱신을 한다. 한계: mask 종류 ≤5(vHPC), 중첩 충돌(무작위 가정 시 쌍당 충돌 확률 ≈1/5, 내 산술), one-hot 이산 schema.
- DQ3: novelty(항목별 감쇠) × familiarity(schema 노출 sigmoid) 곱으로 replay·갱신 예산을 배분한다. 새 schema는 설계상 boost가 없어 accommodation이 느리다. revise/switch의 명시적 failure mode다.
- DQ4: fast 인덱스가 slow 가중치의 target을 clamp한다. 공고화 라운드당 replay 수를 gate(Eq.10)로 정한다. 논문 예에서 총 epoch 13,875 대 16,800(flat 800) 대 33,600(flat 1600)이다.
- DQ7: 희소도 P와 mask 중첩 수를 retention 진단으로 쓴다. 학습이 ungated free 단계를 통해 mask 밖 유닛을 건드린다는 점에 유의한다.
- DQ6(H-SAMPLE) [OPEN]: familiar schema가 같은 구조의 새 schema 학습을 빠르게 한다는 증거는 없다. 새 PA만 빠르다(5개 중 3개는 불변).
- DQ5/H-COMPUTE [OPEN]: 학습 epoch 절감뿐이고 추론 depth 조절은 없다.
- DQ8: Tse식 probe 설계(cued/non-cued/original well 비율)를 차용한다. fast 저장소 lesion을 test 시점에 적용해 공고화된 지식과 fast 의존을 분리한다. 총 epoch 예산 곡선도 쓴다.
- Melete 주의: 구조 없는(mPFC=1) 대조가 비중첩 schema에서 gating 변형보다 낫다(≈0.9~0.95 대 ≈0.65). 학습·gating 구조의 이득은 중첩 상황에서만, 그것도 작게 나타난다.

**12. 재현**
- MATLAB 단일 스크립트(`reproduce_tse_figures_chl.m`, 1,113줄)와 보조 .m 20개다. Statistics Toolbox 함수(`kstest2`, `anova1`, `ttest`)를 쓴다. 버전 미명시.
- 규모는 수백 뉴런이고 20 네트워크를 벡터화한다. CPU로 충분하고 GPU(RTX 5070 Ti)는 불필요하다. 실행 시간은 측정하지 않았다.
- numpy/PyTorch 포팅은 소규모다. 포팅 전에 아래 불일치 목록을 정리하고 어느 판의 실험을 재현할지 정해야 한다.
- 키 파일↔식:
  - `explore.m`: Eq.3-10
  - `chl.m`: Eq.1-2
  - `train1Schema.m`: trial 루프
  - `initializeWeights.m` L9-10: gating 행렬
  - `testSchema.m`/`testOnePA.m`: 평가

**코드 감사 (논문-코드 불일치 상위)**
- N_multimodal: Table 1은 40, 코드·그림은 80.
- CHL 스텝: 실효 0.002(Table 1 η_CHL .001).
- e_boost: Table 1은 1000, 코드는 2000(주석 `%1000`).
  - 내 추론: Fig.10B의 novelty ≤0.6이다. 그러면 600+0.6×2000=1,800이고 이는 Fig.11A 피크(≈1,700~2,100)와 총합 13,875(=12,000+≈1,800+소량)에 맞는다. 1000이면 ≤≈1,200이다.
- mPFC→vHPC 가중치(`w_context_vhipp`)는 무작위+정규화뿐이다. 학습 규칙이 없고 p.172의 서술과 모순된다.
- gating 0 위치를 복원 추출(`randi`)로 뽑는다. 기대 0 비율은 1−e^{−P}≈0.26이며 P=0.3이 정확히 반영되지 않는다.
- gating은 clamped 단계에만 걸린다. 따라서 control과 lesion의 probe test는 test 시점 회로가 다르다(`testOnePA`는 `has_hipp`일 때만 gating).
- `train1Schema.m` L16: 루프가 20 rat의 `max(floor(epochs))`까지 돈다. 모든 rat이 갱신되므로 rat별 NM 의존 학습량이 분리되지 않는다.
- Fig.9 캡션은 Exp.2 시작 시 epoch이 "크게 증가"한다고 쓰지만 p.178과 Fig.11A는 Exp.2의 NM이 낮다고 한다. Eq.8-9상 새 schema는 familiarity≈0이므로 후자가 맞아 보인다.
- 코드와 VoR:
  - VoR §4.5-4.6(3-schema 스윕 Fig.13, mPFC-크기·중첩 Fig.14-15)의 코드는 repo에 없다. repo에는 preprint식 2-schema 스윕(L917-1024)이 있다.
  - repo에는 VoR에서 삭제된 일관/불일치 실험이 있다.
  - 통계는 논문이 Wilcoxon이라 쓰지만 코드에는 `ranksum`이 없다.
  - 죽은 파라미터(`h_min`, `boost_familiarity`)가 있고 RNG seed가 없다.
  - repo는 단일 commit(accepted 2019-09-24 이후, online 2019-11-04 이전)이다.
- 나머지 상세는 `fcl-sbl-fulltext-20261111/HWU20/extraction.json`에 있다.

**VoR와 preprint v1의 차이**
- 제목이 Consolidation에서 Encoding으로 바뀌었고 초록이 재구성됐다.
- 실험 3(일관/불일치)이 삭제됐다.
- Eq.2 부호, Eq.10의 e_boost, Table 1(h_min·b 삭제)이 수정됐다.
- 3-schema 스윕과 mPFC 크기·중첩 스윕, §4.4 수치가 추가됐다.

**코드 경로 탐색 범위** (공식 링크가 있어 이 절은 보강용)
- 논문 §3.5의 링크와 GitHub API로 repo를 확인했다.
- 저자 `fitany`의 repo 14개를 조회했다. `SchemaHSR`(로봇 응용 추정)와 `SchemaProject`(2017)가 관련 repo이며 둘 다 미감사다.
- `UCI-CARL` org 23개에는 schema repo가 없다.
- ModelDB 검색 endpoint는 HTTP 500/302를 반환해 결론을 낼 수 없었다. WebSearch로도 ModelDB 항목은 발견되지 않았다.
- Springer 비공식 프록시 미러는 사용하지 않았다.

---

### 3. 산출물 경로
- SPENS24: `fcl-sbl-fulltext-20261111/SPENS24/access.json`, `fcl-sbl-fulltext-20261111/SPENS24/fulltext.txt`, `fcl-sbl-fulltext-20261111/SPENS24/supp_fulltext.txt`, `fcl-sbl-fulltext-20261111/SPENS24/extraction.json`, `fcl-sbl-fulltext-20261111/SPENS24/SHA256SUMS.txt`
- HWU20: `fcl-sbl-fulltext-20261111/HWU20/access.json`, `fcl-sbl-fulltext-20261111/HWU20/fulltext.txt`, `fcl-sbl-fulltext-20261111/HWU20/supp_fulltext.txt`, `fcl-sbl-fulltext-20261111/HWU20/extraction.json`, `fcl-sbl-fulltext-20261111/HWU20/SHA256SUMS.txt`
- 코드: `fcl-sbl-fulltext-20261111/code/generative-memory/`, `fcl-sbl-fulltext-20261111/code/SchemaNetworkBICY/` (두 repo 모두 `git status` 깨끗함)
- 스크립트: `fcl-sbl-fulltext-20261111/_scripts/W1/`

---

### 4. 자체 점검
- `sha256sum -c`:
  - SPENS24: SHA256SUMS.txt 11개 OK, aux 3개 OK.
  - HWU20: SHA256SUMS.txt 15개 OK, aux 3개 OK.
- `access.json` 필수 키 15개는 두 파일 모두 누락 0이다. supplementary·code 하위 키도 확인했다.
- `.md`는 쓰지 않았고 `.txt`와 `.json`만 만들었다. repo는 수정하지 않았다.
- 외부(ChatGPT) 원문 요약은 받지 못했다. 과제문에 적힌 주장 S1~S5, H1~H6의 문구를 기준으로 검증했다.

**불확실·미해결**
1. SPENS24 bioRxiv v1~v3는 429라 못 받았다. preprint와 VoR의 차이는 모른다.
2. HWU20 Springer 호스팅 VoR는 bot wall로 직접 대조하지 못했다. 저자 호스팅본을 VoR로 간주했다.
3. 그림에서 읽은 수치(SPENS24 Fig.S2, SI Fig.S1의 lure 약 4개, HWU20 Fig.5·7·12·13·14·15)는 근사값이다.
4. HWU20 VoR §4.5-4.6(Fig.13-15) 코드는 미공개다. 어떤 변형 코드로 만들었는지 알 수 없다.
5. 코드는 실행하지 않았으므로 모든 코드 동작 서술은 정적 읽기다. β_eff와 e_boost=2000 정합은 해석적 추정이다.
6. HWU20 Fig.9 캡션과 §4.3의 모순은 미해결이다.
7. SPENS24 Fig.4g의 N(200 대 500)과 일부 figure별 seed는 코드를 실행하지 않고는 확정할 수 없다.
8. Shapes3D의 TFDS 앞 15,000개 요인 분포와 ROCStories 입수 경로는 확인하지 않았다.
9. `SchemaHSR` repo는 읽지 않았다. ModelDB는 결론을 낼 수 없다.
