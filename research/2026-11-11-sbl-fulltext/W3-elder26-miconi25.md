# ELDER26, MICONI25 — 가소성 수준 schema와 지식 재조립

> 2026-11-11 SBL 원문 검토 워크플로에서 worker가 쓴 보고를 마스터가 원문 대조로 검수해 옮겼다. 종합은 [2026-11-11-sbl-fulltext-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext-review.md)에 있다.
>
> `fcl-sbl-fulltext-20261111/...` 경로는 저장소 밖 호스트 작업 폴더다. 원문은 저작권 때문에 저장소에 넣지 않았다. 판본과 해시는 [evidence.json](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/evidence.json)에 있다.
>
> 표기: 필드 1–10·12는 별도 표기가 없으면 원문 사실(LITERATURE, 위치 병기)이다. 일부 문장은 우리 산술·추론(PROPOSAL), 코드 독해(CODE), 그림 판독(FIGURE-READ)인데 표시가 빠져 있다. 그 목록은 [W7-remediation.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/W7-remediation.md) §2.4에 있다. 필드 11은 PROPOSAL이다.
>
> 정정: MICONI25 수치표 ID를 MN1–MN10으로 바꿨다(TEM20 주장 ID와의 충돌 방지). ELDER26 "데이터 증가" 문장을 코드 기준으로 고쳤다. ELDER26의 주장표는 필드 10이 아니라 "주장표" 절에 있고, 필드 10 자리에는 코드와 논문 차이가 있다. ELDER26 필드 3·4·6·8과 MICONI25 필드 3의 위치 보완·정정은 [W7-remediation.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/W7-remediation.md) §2.1–2.2에 있다.

---

### W3 보고: ELDER26 + MICONI25

산출물은 각 폴더의 `fulltext.txt`, `supp_fulltext.txt`, `access.json`, `extraction.json`, `SHA256SUMS.txt`다.
- ELDER26: `fcl-sbl-fulltext-20261111/ELDER26/fulltext.txt`, `fcl-sbl-fulltext-20261111/ELDER26/supp_fulltext.txt`, `fcl-sbl-fulltext-20261111/ELDER26/access.json`, `fcl-sbl-fulltext-20261111/ELDER26/extraction.json`, `fcl-sbl-fulltext-20261111/ELDER26/SHA256SUMS.txt`
- MICONI25: `fcl-sbl-fulltext-20261111/MICONI25/fulltext.txt`, `fcl-sbl-fulltext-20261111/MICONI25/fulltext_columns.txt`, `fcl-sbl-fulltext-20261111/MICONI25/fulltext_preprint_v3.txt`, `fcl-sbl-fulltext-20261111/MICONI25/supp_fulltext.txt`, `fcl-sbl-fulltext-20261111/MICONI25/supp_fulltext_preprint_v3.txt`, `fcl-sbl-fulltext-20261111/MICONI25/access.json`, `fcl-sbl-fulltext-20261111/MICONI25/extraction.json`, `fcl-sbl-fulltext-20261111/MICONI25/SHA256SUMS.txt`
- 코드: `code/bdENN`, `code/TransitiveInference`. 읽기만 했고 실행하지 않았다. `git status`는 둘 다 clean이다.

**결론**
- **E3**: 사실 불일치가 아니라 "상위/하위" 용어가 반대로 쓰인 것이다. 논문에서 고정되는 쪽은 downstream hidden layers, 갱신되는 쪽은 upstream input-layer 가중치다.
- **ELDER26 한계**: 이 불변성은 ENN(SVM, 일회성 학습)을 더 큰 부분집합으로 처음부터 다시 학습할 때 나온 결과다. 순차 학습, 새 과제, 새 클래스 실험은 없다.
- **E5**: 62.3±3.8 / 56.1±4.7은 본문에 있다. ±의 정의는 없다.
- **MICONI25**: M1은 PARTIAL, M2는 CONFIRMED, M3는 CONFIRMED이되 단서가 붙는다.

---

### 1. ELDER26

#### 접근 증거
- **route**: Springer 하이브리드 OA(CC BY-NC-ND)를 찾았지만 PDF 경로는 모두 봇월이었다.
  - Springer PDF: Client Challenge HTML
  - PMC PDF: JS stub
  - Europe PMC 렌더: 403
- 전문은 Europe PMC `fullTextXML`(PMC13588848)에서 확보했다. 본문, Methods, Data Availability가 모두 들어 있다.
- supplement PDF는 Springer static-content에서 받았다. md5가 PMC XML에 적힌 값과 일치한다.
- Fig1~5 PNG는 Springer media 서버에서 받아 직접 읽었다.
- **url**: https://doi.org/10.1007/s10827-026-00940-x
- **version**: VoR.
  - received 2025-12-05, revised 2026-05-26, accepted 2026-06-18, epub 2026-06-30 (`version_date`)
  - 2026-09-29 정정은 NIH grant 번호만 바꾼다.
- **preprint**: bioRxiv v1 2025-02-04 (10.1101/2025.01.30.635821). 제목이 다르고 이후 버전은 없다. XML과 supplement로 전문 대조했다.
- **pages**: null. VoR은 XML만 확보했고 PDF는 못 받았다. supplement PDF는 10쪽이다.
- **words**: fulltext 6,179, supp 368 (캡션뿐).
- **읽은 범위**: Abstract, Intro, Results 4절, Discussion, Methods 전체, supplement 10쪽(그림 S1,S3–S7,S9,S10은 이미지로 확인, S2·S8은 캡션만), 본문 Fig1~5 이미지.
- **sha256 앞 16자리**

| 파일 | sha16 |
|---|---|
| fulltext.txt | 40bb809b933bc181 |
| supp_fulltext.txt | 2259e9c41fc24038 |
| VoR XML | b2c56eb4e53f56ac |
| supp PDF | 7b611475ebeae0dc |
| Fig1 | 91edabbcec3d2a7b |
| Fig2 | 3a23dfa3e64d4321 |
| Fig3 | 70a35474504d16f5 |
| Fig4 | 6323f8c02c0254cb |
| Fig5 | bbb5a12a0a0b6061 |
| preprint XML | 23e279982a51b8c3 |
| preprint supp zip | ca7c53b9ebc73813 |
| openalex json | 4c9e7c038364844a |
| biorxiv api json | c2ef84d6ca92743d |

#### 필드 1~12
1. **서지**
   - Elder, Zheng, Shimelis, Rutishauser, Lin. J Comput Neurosci 2026. PMCID PMC13588848.
   - 코드는 https://github.com/jre411/bdENN, commit 8aee36c2…(2025-02-04), LICENSE 없음. README는 preprint v1을 가리킨다.
2. **schema 정의와 위치**
   - [LITERATURE] 정의 (Intro): "a schema … as a subcircuit whose network parameters remain invariant despite decreasing training loss".
   - 위치는 하위(downstream) 은닉층 가중치다. HL1은 differentia→subconcept 3×3, HL2는 subconcept→concept 3×3이다.
   - 형태는 hybrid다. 상류(IL, 4×512→3)는 연속값이고 하류는 거의 디지털이다. Fig3b,c에서 max 정규화 후 HL1 ∈ {−1,0,1}, HL2 ∈ {−0.5,1}이다. Discussion은 "effectively digital 'AND'"라고 쓴다.
   - activity, attractor, latent 분포가 아니다.
3. **구조**
   - 고정된 ImageNet VGG-16(keras 3.5.0, GAP) → 프레임 4장 × 512 = 2048 → 2×3 tanh → 3 클래스(NB/SB/HB).
   - ENN과 MLP의 구조는 동일하다.
   - fast/slow 구분은 없다. 제목의 "plastic"은 학습 가능하다는 뜻이다.
   - 불변성은 제약이 아니라 결과로 나온다.
4. **학습 규칙** (outer loop와 within-lifetime 구분 대상 없음)
   - ENN은 비gradient, layer-wise다. 단계는 아래와 같다.
     - class별 Ward 군집화
     - differentia: 쌍별 linear SVM, C=15
     - subconcept: differentia 출력(mult 8, tanh로 거의 ±1 포화)에 대한 SVM, C=1000, margin_ratio=inf
     - concept: SVM
   - 뉴런은 y = w·x + b, 활성화는 tanh다. 가중치가 ±1e-4·max|w| 안이면 같은 값으로 맞추는 `equalize_weights`가 기본 경로에 들어 있다.
   - 코드상 `num_subclasses=3`은 `hiddenLayerSize`를 그대로 넘긴 값이며 클래스 수와 같다. 내 해석은 클래스당 subconcept 1개이고 differentia는 C(3,2)=3개라는 것이다.
   - backprop 기준선은 sklearn 1.5.2 `MLPClassifier`(adam, max_iter 10000, 나머지 기본값)다. `VariableTrainingData.py`는 max_iter=1000을 쓴다.
   - within-lifetime plasticity와 meta-learning은 없다.
   - "데이터 증가"는 [CODE] 1%…100% 10개 지점에서 train_size만 바꾼 stratified 부분집합(같은 seed 9)으로 처음부터 재학습한 것이다. 논문은 지점 수와 비율을 적지 않는다(W7 보완 보고 §2.1). 시드 1개이고 순차 갱신이 아니다.
5. **형성/선택/적용/개정**
   - 이론 서술만 있다. subconcept 입력 가중치는 군집이 새로 생기거나 합쳐지거나 갈라지지 않는 한 불변이라고 쓴다(Intro, Fig1 범례).
   - accommodation(군집 생성·병합·분할)은 실험하지 않았다. novelty gate도 없다.
6. **지속성**: 파라미터뿐이다. replay와 consolidation은 없다. ENN은 전체 학습 데이터가 한 번에 필요하다.
7. **수치와 분모**

| ID | 수치 | 위치 | 분모 / 조건 |
|---|---|---|---|
| N1 | ENN 62.3±3.8% vs BP 56.1±4.7% | Results(Fig3 범례 앞), Sup S3 | 아래 별도 설명 |
| N2 | hidden-2 ≥5개에서 MLP 0.63–0.64 > ENN 0.57–0.58. 3개일 때만 ENN 0.62 > MLP 0.55 | Sup S5 | 크기별 80/20 분할 20회 (그림 판독) |
| N3 | 증강 2664 clips: ENN 0.55–0.65, MLP 0.2–0.65 이봉 | Sup S6 | 85/15 분할 100회 |
| N4 | 혼동행렬: ENN SB .51 / HB .52, BP SB .46 / HB .39 | Sup S4 | 분할 횟수 미명시 |
| N5 | 가중치 노이즈 견고성 | Fig4a,c,d, S7 | 아래 별도 설명 |
| N6 | 특징 제거 | Fig4b | 아래 별도 설명 |
| N7 | 50-feature 회로: ENN ~0.45→0.91, LogReg →0.79, BP →0.71 (학습 44→799) | Fig4f | 아래 별도 설명 |
| N8 | 발화 유사도 | Fig5, S9, S10 | 50/50 분할 20회, 클래스당 30 clips. 은닉 뉴런을 클래스 평균 발화로 가르는 데 필요한 hyperplane 수: 50 network에서 ENN ≈10 vs BP ≈25 (SD, 50 trials) |

   - **N1**
     - 조건은 3-class 경계 검출, 85/15 분할, 2×3 tanh이고 "converged networks with 100% training accuracy"다.
     - 클립 수는 본문 Results가 978, Methods가 888이다. repo의 프레임 3552장(=888×4)과 Sup S6의 2664(=3×888)가 888을 지지한다.
     - "multiple splits"의 횟수는 문장에 없다. Fig3c 캡션과 코드는 10,000회다.
     - 코드(`sFig1.py`)의 필터는 MLP **test** accuracy > 0.4이고 ENN 배열에도 같은 인덱스를 쓴다. training 100%는 확인하지 않는다.
     - S3에서 BP 약 3.5k개가 0.33 근처에 몰려 제외된다. 총 개수는 명시되지 않았고, 이 수치는 히스토그램 판독값이다.
     - ±는 정의되지 않았다. S3 폭과, test 133~134 clips에서의 이항 SD(4.2/4.3점)를 보면 split 간 SD에 가깝다. 이는 추정이다.
     - 통계검정은 없다.
   - **N5**: 코드(`NoiseInjection.py`)는 split 1개(`random_state=42`)에서 ENN 1개와 MLP 1개를 학습하고 노이즈만 10,000번 뽑는다. 곱셈 노이즈 W+W·noise·N(0,1)를 1층 가중치(layer index 1)에 넣고, 노이즈 전 정답이던 test 샘플로만 평가한다. 캡션의 "10000 splits"와 어긋난다.
   - **N6**: 코드(`ParameterRobustness.py`)는 80/20 분할 1000회를 쓴다. 정확도는 **전체 데이터(train+test)**로 계산하며, 시작값 0.92는 0.8·1.0+0.2·0.62와 맞는다.
   - **N7**: 코드(`bdENC.py`)는 100 trials × 10 크기를 쓰고 평가는 `xAllSparse,yAll`, 즉 888 clips 전체다. preprint Sup S5 캡션에는 "evaluated on the entire dataset (train and test splits)"가 있는데 VoR Fig4f 캡션에는 없다.
   - 축소 실험(큰 네트워크, 증강)은 정확도를 올리지 못했다고 본문이 직접 쓴다.
8. **신경과학 대응**
   - Zheng 2022 MTL 기록과 비교한다. Boundary cell 42개/105 trials, Event cell 36개/30 trials이다.
   - 근거 수준은 raster와 평균 발화 산점도의 **정성적 유사**와, B→E AND 게이트라는 기계론적 가설이다.
   - 계층 순서를 시간 지연에 대응시키는 것은 가정이다(저자 인정). 적합도 통계는 없다.
   - Discussion은 이 schema가 Miconi & Kay 2025의 schema와 "qualitatively different"라고 구분한다.
9. **저자가 밝힌 한계와 보이지 않은 것**
   - 저자 한계: feed-forward만 다룸, 4-frame 입력은 시간 연속성이 없음, 단일 모달.
   - 보이지 않은 것:
     - 이전 과제 망각 측정은 없다. Intro와 preprint의 "catastrophic forgetting" 틀에도 불구하고 그렇다.
     - 새 클래스나 분포 이동은 없다.
     - 전체 특징 held-out 학습곡선도 없다.
     - ENN vs BP 차이의 검정이 없다.
     - sample-efficiency와 compute 증거도 없다.
   - 생물학 예시 방향: Intro의 예시는 감각 입력이 안정화되고 higher-order 표현이 가소적이라는 것이다. ENN 모델(입력 쪽이 갱신, 출력 쪽이 고정)과 반대 방향이며, 저자는 이를 논의하지 않는다.
10. **코드와 논문 차이**
    - 코드: Fig3c는 `VariableSplitsAndReproducibility.py`가 루프 전에 `nSplits = 1000`으로 덮어써서 저장된 10,000 중 처음 1000 split만 쓴다.
    - 코드: Fig3c의 MLP는 `random_state=42` 하나로 한 번 만들어 계속 `fit`한다. sklearn은 `_fit`마다 같은 seed로 재초기화한다. 이 줄은 로컬 sklearn 1.9.1 소스로 확인했고, 논문이 쓴 1.5.2도 동일하다고 가정했다. 그래서 분석이 바꾼 것은 데이터 분할뿐인데, 본문은 "random initialization"에도 민감하다고 쓴다.
    - 코드: Fig3b의 범례 "sparse/low/all"은 훈련 비율 12%/45%/100%에 해당한다.
    - 코드: ENN은 무작위 초기화가 없다(SVM+Ward). seed 간 재현성은 구성상 보장된다.
    - 코드: `inputs/boundaryEmbeddings.npy`, 라벨, `fJie/*.mat` 신경 기록이 repo에 없다. 하드코딩된 HPC 경로를 읽고 `commonFunctions.py`는 import 때 `loadNeuron`을 호출한다. 임베딩 생성 스크립트도 없다.
    - 코드: VoR에서 추가된 Sup S5, S6, S10에 대한 코드와 데이터도 repo에 없다.
11. **FCL 연결 [PROPOSAL]**
    - DQ1: 연속 경계 특징 위에 얹은 양자화된 하류 논리(hybrid weight-space schema).
    - DQ3: "군집 위상 변화"(생성/병합/분할)를 assimilation과 accommodation을 가르는 트리거로 쓴다. 논문은 이를 시험하지 않았다.
    - DQ7/DQ8에서 가져올 측정: 층별 가중치 drift 대 데이터량, split 간 가중치 분포, 정답 샘플의 곱셈 노이즈 retention, 특징 제거 곡선, hyperplane 수. Fig4b,f의 전체 데이터 정확도는 쓰지 않는다.
    - 시도할 실험: gradient 학습 네트워크에서 소량 학습 후 하류를 동결하고 held-out 정확도 손실을 본다. 이어서 중간에 새 클래스를 넣어 어떤 가중치가 바뀌는지 기록한다.
    - 실패 모드:
      - 불변성이 학습 규칙이 아니라 SVM 구성과 weight equalize에서 나온다.
      - Fig3c 막대로 보면 HL1은 행마다 {+1,−1,0}, HL2는 {1,−0.5,−0.5}로 보인다. 즉 3-class 배선이어서 데이터와 무관할 가능성이 높다.
      - 배치 재학습이라 스트리밍이 안 된다.
      - 정확도가 낮고(3-class 62%) 큰 네트워크에서는 MLP가 낫다.
      - Fig4b,f 평가에 학습 데이터가 섞여 있다.
    - H-SAMPLE, H-COMPUTE 증거는 없다. Melete 계보의 learned-vs-fixed 이득도 여기서 보여지지 않는다.
12. **재현**
    - 연산량은 작다(888×2048 SVM). 원 연구는 BioHPC에서 10,000 split을 돌렸다.
    - 데이터는 PNG 3552장(2.9GB)뿐이고 임베딩과 신경 기록이 없다.
    - 프레임워크는 sklearn 1.5.2, keras 3.5.0(VGG16)이다.
    - ENN과 MLP는 CPU로 충분하다. VGG-16로 1080×1920 프레임 3552장을 처리하는 것은 12GB RTX 5070 Ti에서 batch 1이면 가능하리라 추정한다(미실행). 임베딩 스크립트와 경로는 재작성이 필요하다.

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

---

### 2. MICONI25

#### 접근 증거
- **route**: VoR(Nature Neuroscience)은 유료다. 랜딩 페이지는 abstract, 그림 제목, code availability뿐이고 PMC에도 없다.
  - 주 전문은 저자 홈페이지의 Springer 조판 proof PDF(`thomasmiconi.github.io/NN.pdf`)다. 공식 코드 repo의 NN.pdf와 sha256이 같다.
  - 보조 전문은 bioRxiv v3(Europe PMC JATS, PMC10402151)다.
  - supplement는 VoR ESM1, ESM2를 Springer static-content에서 받았고, preprint supplement PDF는 Europe PMC zip에서 복구했다.
- **url**: https://doi.org/10.1038/s41593-024-01852-8
- **version**: accepted_manuscript(조판 proof).
  - Received 2023-09-04, Accepted 2024-11-15, "Published online: xx xx xxxx".
  - VoR은 2025-01-15 온라인, Nat Neurosci 28(2):406–414.
  - preprint: v1 2023-07-28(제목 "transitive inference … learning neural networks"), v2 2023-09-02, v3 2023-09-04(제목 "An active neural mechanism …").
- **VoR 차이**
  - proof의 abstract, 본문 그림 8개 제목, code-availability 문장은 VoR 랜딩 페이지와 동일함을 확인했다.
  - 조판·교정·Extended Data 번호의 차이는 확인할 수 없다.
  - VoR supplement에만 있는 노트(preprint supplement에는 없음): S2 toy model, S6 frozen W_in, S10 scalar α, S12 유사도, S13 행렬 교체.
- **pages**: 14(proof). 보조 PDF는 VoR supp 23쪽, Reporting Summary 3쪽, preprint supp 12쪽이다.
- **words**: fulltext 10,479. supp(ESM1+ESM2) 7,205. preprint 10,864.
- **읽은 범위**: proof 전체(본문, Methods, Extended Data 범례, 참고문헌은 훑음). 본문 Fig1과 Fig3은 이미지로 봤고 나머지 그림은 범례와 본문으로 읽었다. VoR supp 전체, preprint v3 전문과 supp A–H, 코드(`simple.ipynb` 전체, `main.ipynb`의 parameter, network, list-linking 분기, `toymodel.py`).
- **sha256 앞 16자리**

| 파일 | sha16 |
|---|---|
| fulltext.txt | 0f1fd0d1bd7c6f7e |
| supp_fulltext.txt | 16dfb50f6cf1f1f3 |
| fulltext_columns.txt | ed70436bc155514d |
| fulltext_preprint_v3.txt | d7285826d3c35b6a |
| supp_fulltext_preprint_v3.txt | 5296fd442ec29f6b |
| NN.pdf (proof) | cb2564c4743ff4ef |
| 랜딩 HTML | 6f6ca226051e4f6c |
| VoR ESM1 | 9f49bce2a69d579e |
| VoR ESM2 | 8696550e955f56da |
| preprint v3 XML | 030723a4fb3962fc |
| preprint v3 supp PDF | ae580bda41e3ba5c |
| openalex json | 862dcb382a4a73d3 |
| biorxiv api json | 8c188fbe50fca3d8 |
| europepmc search json | dd60fdc11a986fb3 |

#### 필드 1~12
1. **서지**
   - Miconi (ML Collective/Astera), Kay (Columbia). Nat Neurosci 2025. DOI 10.1038/s41593-024-01852-8.
   - 코드는 https://github.com/ThomasMiconi/TransitiveInference, commit fbdebf06…(2025-05-28), LICENSE 없음.
   - 환경은 Python 3.10, PyTorch 2.4.1, Colab(Reporting Summary)이다.
2. **schema 정의와 위치**
   - 형식 정의는 없다. "schemas"는 첫 문단에서 relational memory, cognitive maps와 나란히 나올 뿐이다.
   - 작동상의 위치는 둘이다.
     - 인스턴스: fast weight P(t) 200×200이 각 항목을 결정 축 w_out 위에 rank 비례로 배치한다(Fig4b).
     - 알고리즘: 느린 구조 파라미터(W_in, W_rec, A, W_out, W_mod, η)에 학습 절차가 들어 있다.
   - 연속 형태이고 이산 graph는 없다.
3. **구조**
   - 완전연결 RNN 200 tanh 유닛이다. 코드상 학습 파라미터는 약 88.6k개다.
   - 입력은 항목 2개(각 15비트)+reward+이전 응답이다. 코드에는 논문에 없는 'go' 비트, bias, 에피소드 시계 입력이 더 있고 비트는 ±1 코딩이다.
   - 출력은 2-way softmax, 스칼라 neuromodulator m(t), 코드에는 value head도 있다.
   - 에피소드 안에서 바뀌는 것은 P(t)(재귀 연결만)뿐이다. 항목별 가소성 계수 A는 200×200이고 음수도 가능하다.
   - 전부 느린(outer) 파라미터인 것은 W_in, W_rec, W_out, W_mod, A, η, m의 스칼라 배수다.
   - H(t)와 활성은 매 trial 리셋한다. P(t)는 에피소드 시작에 리셋한다(본문, `simple.ipynb`). `main.ipynb` 학습은 3번째 에피소드마다 리셋한다(`nbepsbwresets=3`, Supp Note 3).
   - trial은 4 step이다: 자극, 응답, reward 입력, delay.
   - 에피소드는 30 trial로, 인접쌍 20 + 전체쌍 10이다.
   - 목록 길이는 논문 4~9 / 코드 `range(4,9)`=4~8이다. 시험은 8 항목이다.
4. **학습 규칙 (원형 그대로)**

   논문 Methods:
   ```
   (1) x(t) = W_in i(t) + (W_rec + A ⊙ P(t)) r(t−1)
   (2) r(t) = tanh(x(t))
   (3) o(t) = Softmax(W_out r(t))
   (4) m(t) = W_mod r(t)      [m은 스칼라]
   (5) H(t+1) = η x(t) r(t−1)ᵀ + (1−η) H(t)
   (6) P(t+1) = P(t) + m(t) H(t)
   (7) η≈1이면 P(t+1) ≈ P(t) + m(t) x(t−1) r(t−2)ᵀ
   ```
   코드(`simple.ipynb`, `RetroModulRNN.forward`):
   ```
   hactiv = tanh( i2h(inputs) + (w + alpha ⊙ pw) @ hidden )
   m = DAmult·( tanh(h2DA(hactiv))[0] − tanh(h2DA(hactiv))[1] )
   pw ← clip(pw + m·et, ±50)
   et ← (1−η) et + η·tanh( hactiv ⊗ hidden )
   ```
   - **within-episode(inner)**: gradient가 없다. P(t)는 위 식으로만 쓰이고 m(t)는 네트워크가 스스로 만든다.
   - **outer loop(meta-learning)**
     - 최적화 대상은 에피소드 총 보상(마지막 10 trial 가중)이고, A2C와 BPTT를 쓴다. 학습 변수는 W 행렬, A, η, m의 스칼라 배수다.
     - 목적식(Suppl Eq.8): `J = Σ_t [ β1(t) π_t(a_t) StopGrad(V−v̂) + β2 H(π_t) − β3 (V−v̂)² ]`. 인쇄된 식에는 코드가 쓰는 log가 빠져 있다. β1은 처음 20 trial은 1, 마지막 10 trial은 4다. H는 Shannon 엔트로피가 아니라 제곱합이다.
     - 코드: γ=0.9, value 계수 0.1, `entropy` 항 0.1·Σsoftmax², Adam lr 1e-4, grad clip 2.0. 배치 32 에피소드 / 업데이트, 30000 업데이트, 처음 100 에피소드는 step 없음.
5. **형성/선택/적용/개정**
   - 사이클: step3에서 reward와 무관한 음의 m(t)가 두 항목의 쌍 결합을 만들고, step4에서 오류 선택적 m(t)(오답 음수, 정답 0 근처)가 reinstate된 항목을 결정 축 방향으로 이동시킨다.
   - 오답 중심 가소성이라 한 쌍을 반복해도 표상이 깨지지 않는다(Supp Note 9).
   - 보이지 않은 이웃에 대한 전이는 그 이웃이 이전에 짝지어진 적이 있을 때만 일어난다(Supp Note 4).
   - list-linking은 두 1-D 순서를 합치는 병합이다. 분할은 없다. 명시적 novelty gate는 없다.
6. **지속성**
   - 시험 시 gradient 갱신은 없다. P(t)가 trial 사이를 유지한다.
   - 학습은 3 에피소드마다 리셋하고 이전 목록 쌍 25%를 섞는다. 그 결과 이전 목록 쌍 정확도는 >70%다(Supp Note 3).
   - replay와 sleep은 없다. 단 trial 안에 미니 reinstatement가 있다.
7. **수치와 분모**

| ID | 수치 | 위치 | 분모 / 조건 |
|---|---|---|---|
| MN1 | meta-training: 약 50% → 약 90~95% (마지막 10 trial). 2개 run은 더 낮음 | Fig1f (그림 판독) | 30 run |
| MN2 | 상징 거리 효과와 end-anchor 효과 | Fig2a | 2000 에피소드를 200씩 10 subset으로 나눠 중앙값과 IQR. 평가는 trial 21~30이며 feedback과 가소성이 계속됨 |
| MN3 | list-linking | Fig3a,b | 아래 별도 설명 |
| MN4 | massed presentation | Supp Note 9 | 영향이 작다 (2000 run, DE 20 trial 추가) |
| MN5 | 고정 random W_in | Supp Note 6 | 성능과 list-linking 유지 (run 수 미명시) |
| MN6 | 스칼라 α | Supp Note 10 | 30 run 중 active 해 0개, 전부 passive 또는 실패 |
| MN7 | W_out 또는 W_in 교체 | Supp Note 13 | 2000 run, chance |
| MN8 | toy model: corr(값, rank) −0.77±0.17 (이웃 갱신 있음) vs −0.57±0.22 (없음) | Supp Note 2 | 1000 에피소드, 8 항목, Mann-Whitney p<1e−90 |
| MN9 | 재코딩 표상과 원표상의 상관 \|corr\|<0.1. step1→2 유사도 보존 평균 0.21 (SD 0.17, 범위 −0.34~0.78, 12% 음수) | Fig7 본문, Supp Note 12 | 2000 에피소드. Fig7은 DE 136 / ED 142 에피소드 |
| MN10 | passive 해: transitive inference는 가능, list-linking은 chance 이하 | Extended Data Fig1 | 2/30 run |

   - **MN3**
     - 설계는 10(인접 ABCD)+10(인접 EFGH)+4(D/E)+1 test trial이다. 2000 run이고 코드는 `bs=4000`이다.
     - 대부분의 쌍은 90~100%다. 연결쌍 이웃인 CD는 약 48%, EF는 약 62%이고 CE·CF는 약 58~60%다(그림 판독).
     - sham(EF 한 번)은 CE처럼 충돌하는 쌍에서 chance보다 훨씬 낮다.
     - test가 run당 1 trial이라 쌍당 약 71회(2000/28)로 추정한다. 오차 막대는 200씩 10 subset에서 나온다.
   - 비교 기준선: 읽은 본문과 supplement에서 non-plastic RNN이나 표준 meta-RL RNN 기준선은 찾지 못했다.
8. **신경과학 대응**
   - 행동 패턴을 원숭이(Brunamonti 등, Treichler & van Tilburg 1996 Table 2)와 인간(Nelli 2023) 데이터에 눈으로 대조한다. 상징 거리, end-anchor, 연결쌍 이웃의 낮은 성능, cross-list rank 전이다.
   - reinstatement를 hippocampal replay와 retrieval-mediated learning에 비유한다. 저자가 직접 밝힌 차이는 고정 시점에 자극으로 유발된다는 점이다.
   - 근거 수준은 행동 패턴의 정성적 유사와 모델에 대한 기계론적 주장이다. 신경 데이터 적합은 없다.
9. **한계와 보이지 않은 것**
   - 저자 한계: 응답은 단일 통과의 model-free reflex이고, 재코딩은 추가 제약(과제 간섭 최소화)을 받을 수 있다.
   - 보이지 않은 것:
     - 같은 네트워크 안에서 reinstatement를 제거하는 인과 실험이 없다. 근거는 probe 상관, active vs passive 네트워크 비교, 비신경 toy model이다.
     - 기계론 해부는 대표 네트워크 1개에서 했다. 나머지 고성능 run이 비슷하다는 서술은 run별 통계 없이 주장만 있다.
     - 재코딩 벡터는 저자가 설계한 최적화로 찾은 가설 probe다(Supp Note 8).
     - 순서 관계만 다뤘고 트리나 그래프는 없다. 표면 유사도 조작도 없고 목록은 최대 8항목이다.
     - 장기 망각 분석이 없다.
10. **주장표**

| 주장 | 판정 | 위치 | 근거 한 줄 |
|---|---|---|---|
| M1 | **PARTIAL** | Abstract 예시 vs Fig3a, Results | 아래 별도 설명 |
| M2 | CONFIRMED | Abstract, Methods 식 1~7, Supp Note 5 | 재귀 연결의 Hebbian trace 가소성을 스스로 만든 스칼라 neuromodulator가 gate한다. outer는 A2C와 BPTT, inner는 gradient 없음. |
| M3 | CONFIRMED + 단서 | Figs 6~8, Supp Notes 4, 8, 12 | 재코딩된 코드로 reinstate하고, 보이지 않은 이웃(C,F 강, B,G 약)의 step-2 표상이 step4에 이동한다. 단서는 상관 기반이고, 네트워크 1개이며, 이웃은 이전에 같이 제시된 항목이라는 점이다. |

   - **M1 판정 이유**
     - 논문의 실제 설계는 ABCD+EFGH(4+4)이고 연결쌍은 D>E다. meta-training 목록은 4~9개(코드 4~8개)다.
     - abstract 예시(A>B>C, D>E>F, C>D)와 다르다.
     - 연결쌍은 한 번이 아니라 **4 trial** 제시한다. 앞서 10+10 인접쌍 trial을 거치고 1 trial로 시험한다.
11. **FCL 연결 [PROPOSAL]**
    - DQ1: 느린 파라미터(학습하는 방법)와 빠른 파라미터(인스턴스 기하)로 나눈다. 고정 읽기 축과의 정렬로 구조를 읽어낸다.
    - DQ2/DQ3: 학습된 스칼라 neuromodulator는 맥락별 선택적 갱신 controller로 볼 수 있다. 쓰기 단계마다 서로 다른 gate가 작동한다. 항목별 가소성 계수 A가 필수다(스칼라 α는 active 해 0/30). Titans/HOPE에는 학습된 파라미터군별 inner learning rate와 쓰기 gate로 옮길 수 있다.
    - DQ4: 3시간 척도(trial 활성, 에피소드 fast weight, outer)와 정답 직후 내부 학습 창(미니 replay)이다. 수면형 consolidation은 없다.
    - DQ5: 응답은 단일 recurrent 통과이고 학습은 delay 구간의 deliberate 단계다. 숙고 결과를 fast weight에 써서 이후 판단을 단일 통과로 만드는지가 H-COMPUTE 유사 실험이다.
    - DQ6: H-SAMPLE 유사다. 목록 하나를 20 trial로 학습한다. 단 평가 구간에도 feedback이 계속되고, 깨끗한 post-learning probe는 list-linking의 25번째 trial뿐이다.
    - DQ7/DQ8: 차용할 평가:
      - 상징 거리와 end-anchor 곡선
      - linked vs sham
      - withheld-neighbor counterfactual(Supp Note 4)
      - 결정 축 정렬 probe
      - 행렬 교체 대조(Supp Note 13)
      - frozen W_in 소거, 스칼라 α 소거
    - 실패 모드:
      - 가소성 파라미터화를 바꾸면 해가 뒤집힌다(2/30 passive).
      - 120 step BPTT와 RL outer loop는 LLM 깊이와 길이로 확장되지 않는다.
      - fast weight는 에피소드마다 리셋된다.
      - random 이진 항목이라 표면 유사도 강건성은 검증할 수 없다.
      - 순서 관계만 다룬다.
      - 기계론 분석이 네트워크 1개이고 compute 증거는 없다.
12. **재현**
    - 네트워크는 약 89k 파라미터다. README는 30000 업데이트가 Colab에서 수 시간이라고 쓴다. 평가는 2000~4000 에피소드를 한 번에 돌린다(pw 4000×200×200 floats = 640MB).
    - 파일: `simple.ipynb` 셀2 = 완전한 meta-training, `main.ipynb` = EVAL 그림, list-linking, massed, 3 에피소드 리셋, `addons/toymodel.py`, `addons/TI_FrozenWin.ipynb`.
    - 12GB RTX 5070 Ti에서 가능하다고 추정한다(BPTT 저장 수 GB, 미측정). CPU는 가능하지만 느리다.
    - repo의 `.dat`는 pickle이라 `torch.load`하지 않았다.

#### 코드와 논문 차이 (MICONI25)
- 식 4: m(t)는 논문에서 선형 `W_mod r(t)`, 코드에서는 두 tanh 유닛의 차에 `DAmult`를 곱한 값이다.
- 식 5: Hebbian trace는 논문에서 x(t)(활성화 전), 코드에서는 r(t)=tanh(x)이고 외적에 tanh를 한 번 더 건다.
- 목록 길이는 논문 4~9, 코드 `range(4,9)`로 4~8이다.
- 마지막 10 trial 손실 배수는 논문 ×4, 코드 `testlmult=3.0`이다. Methods 본문은 "last ten episodes"라고 쓴다.
- 논문에 없는 항목: pw ±50 clip, 최종 plastic weight에 L2 1e-4(`lpw`), 'go'·bias·시계 입력.
- 업데이트 단위는 논문에서 "에피소드마다", 코드에서는 32 에피소드마다 한 번이다(Fig1 범례의 "30,000 episodes"와 어긋남).
- 논문 Fig1d와 Methods는 plastic weight를 에피소드마다 리셋한다고 쓰지만, Supp Note 3은 전체 학습에서 3번째마다 리셋한다고 쓴다. preprint도 동일한 불일치를 갖는다.
- list-linking 평가의 코드는 `bs=4000`(논문 2000 run). sham 쌍은 코드에서 인덱스(1,2)=BC, 논문에서는 EF다.
- 정책 gradient는 trial의 4 step 모두에 적용된다. 응답 step만 쓰는 편이 더 낫지만 논문에는 쓰지 않았다는 저자 주석이 있다.

---

### 3. 자체 점검
- **sha256sum -c**
  - ELDER26: 13개 전부 OK
  - MICONI25: 14개 전부 OK
- **access.json**: 두 파일 모두 15개 고정 키가 전부 있고 여분 키는 없다. `supplementary`는 {obtained,url,note}, `code`는 {url,commit,license,local_path}이다. `extraction.json`은 둘 다 유효한 JSON이다.
- 수정 흔적: `/tmp` 임시 파일은 삭제했다. 실패한 봇월 응답과 잘린 zip은 `download/`에서 지웠고 `attempted_routes`에 기록했다.
- **불확실·미해결**
  1. ELDER26 VoR 조판 PDF는 못 받았다(pages null). Fig3b, 4, S3~S6의 수치는 그림 판독값이다. S3 히스토그램의 총 개수는 명시되지 않았다.
  2. ELDER26의 978 vs 888은 repo 프레임 수와 Sup S6의 2664=3×888로 888이 맞다고 추정할 뿐, 저자에게 확인하지 않았다.
  3. ELDER26의 ±가 SD라는 것은 S3 폭과 이항 SD로 추정한 것이다.
  4. ELDER26 코드는 preprint 시점이다. Fig3c와 Fig4 캡션이 코드와 어긋나는 점은 커밋되지 않은 재실행 때문일 수 있다.
  5. MICONI25의 VoR 조판본은 읽지 못했고 proof를 읽었다. Extended Data Fig1~3과 본문 Fig2, 4~8은 범례와 본문으로만 확인했다. Fig3a의 쌍별 수치와 쌍당 약 71회는 판독과 설계에서 추정한 것이다.
  6. MICONI25 preprint v1·v2의 전문은 못 받았다. bioRxiv가 429(Cloudflare 1015)를 반환했다.
  7. MICONI25 코드와 논문 차이가 결과에 주는 영향은 모른다. 두 repo 모두 실행하지 않아 어떤 수치도 재현하지 않았다.
