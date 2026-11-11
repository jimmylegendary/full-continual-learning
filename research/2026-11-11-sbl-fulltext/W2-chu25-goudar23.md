# CHU25, GOUDAR23 — RNN 동역학 schema

> 2026-11-11 SBL 원문 검토 워크플로에서 worker가 쓴 보고를 마스터가 원문 대조로 검수해 옮겼다. 종합은 [2026-11-11-sbl-fulltext-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext-review.md)에 있다.
>
> `fcl-sbl-fulltext-20261111/...` 경로는 저장소 밖 호스트 작업 폴더다. 원문은 저작권 때문에 저장소에 넣지 않았다. 판본과 해시는 [evidence.json](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/evidence.json)에 있다.
>
> 표기는 본문 첫머리의 범례([L]·[P]·[O]·[A])를 따른다. CHU25 쪽수는 NeurIPS 사이트 7103–7121과 DOI 등록처·Crossref·OpenAlex 7922–7940이 충돌해 미해결이다([W7-remediation.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/W7-remediation.md) §3).

---

## W2 보고: RNN 동역학 schema (CHU25, GOUDAR23)

표기:
- [L] = LITERATURE. 위치를 병기한다. p.는 본문 PDF 쪽, S-는 supplement.
- [P] = PROPOSAL, [O] = OPEN.
- [A] = 내가 공식 코드, 배포 데이터, 그림에서 직접 읽거나 재계산한 값이다. 논문 수치가 아니다.
- (읽음) = 그림에서 눈으로 읽은 근사값이다.
- 필드 1~10은 별도 표기가 없으면 [L]이다.

산출물 루트는 `fcl-sbl-fulltext-20261111/`이다. 하위에 `CHU25/`, `GOUDAR23/`, `code/learning-2-learn/`, `_scripts/W2/`가 있다.

### 0. 결론
- **CHU25**
  - C1·C3·C4·C8은 확인했다.
  - C2는 부분 확인이다. τ=1, Δt=1이라 시뮬레이션은 사실상 이산시간이다. 키워드 스포팅은 LSTM/GRU를 썼다.
  - C5는 수치가 본문에 있지만 분모와 정확도 정의가 없다.
  - C6은 부분 확인이다. r≈0.90 대 무shaping≈0.85이고, S7b는 0.80~0.85로 일치하지 않는다.
  - C7은 확인했다. 규모가 작고 수치표가 없다.
  - 공식 코드는 없다.
- **GOUDAR23**
  - G1·G2·G3 모두 확인했다.
  - meta-objective는 없지만, 문제 경계·Adam 리셋·안정화 정규화는 harness가 공급한다.
  - 공식 repo의 처리 데이터(10망)는 논문의 30망 통계와 Fig 1d 예시를 재현하지 않는다.

---

### 1. CHU25

#### 1.1 접근 증거
- **route:** 출판사 OA. NeurIPS proceedings 본문 PDF와 Supplemental zip. zip 안의 supp PDF는 `unzip -p`로 꺼냈다.
- **url:** `https://proceedings.neurips.cc/paper_files/paper/2025/file/0a88e621aacf222d3a91d8065c40e4d9-Paper-Conference.pdf`
- **version / VoR:**
  - NeurIPS 2025 camera-ready, VoR (NeurIPS 38, pp.7103–7121, DOI 10.52202/085713-0243).
  - arXiv는 없다. API 0건.
  - OpenReview(RZp2YKtg4q)는 JS 인터스티셜과 403 챌린지로 막혀 우회하지 않았다. 심사본과 리뷰는 미확보다.
- **version_date:** 본문 PDF 생성 2025-12-12, supp PDF 2025-10-17, 슬라이드 2025-11-05, neurips.cc loadDate 2025-12-02, 프로시딩 메타 게재일 2026-04-23.
- **pages / words:** 본문 19쪽(supp 15쪽), fulltext.txt 9,937 words.
- **읽은 범위:**
  - 본문 전체와 NeurIPS checklist 16문항.
  - Methods와 Supplement 전체(A~D, Tab S1~S5, Fig S1~S8).
  - Fig 2·3·4c·5·6b·S2·S4·S7은 렌더링해서 값을 읽었다.
- **파일별 sha256 앞 16자리:**

| 파일 | sha256 앞 16자리 |
|---|---|
| 본문 PDF | 732605b41b6c0639 |
| supp PDF | eccdb8f620ffb959 |
| supp zip | d6cc1e1da909af48 |
| abstract_page.html | 258802bc225dcd7e |
| neurips_virtual_poster_118017.html | 3bda91b95929f1b8 |
| neurips_slides_118017.pdf | 641522032120abd3 |
| openalex_chu25.json | 75e7ecae59754ad1 |
| arxiv_api_title_search.xml | 8bc727f22571b9f2 |
| `fcl-sbl-fulltext-20261111/CHU25/fulltext.txt` | 3eb36c79dd928662 |
| `fcl-sbl-fulltext-20261111/CHU25/supp_fulltext.txt` | 3f8c3c8053e070b3 |

- 상세는 `fcl-sbl-fulltext-20261111/CHU25/access.json`, `fcl-sbl-fulltext-20261111/CHU25/extraction.json`에 있다.

#### 1.2 필드 1~12

**1 서지**
- Chu, Hong, Zou(교신), Mi(교신). 소속은 Chongqing Univ.와 Tsinghua.
- NeurIPS 2025 main, poster 118017. 동료심사를 통과했고 리뷰 원문은 미확보다.
- 최초 공개일은 [O]다. 날짜 단서는 위 version_date뿐이다.
- 개정 흔적: 웹 초록은 "attractor-like schemas / potential to provide new insights"로 hedge되어 있고, PDF는 "attractor schemas / offering new insights"로 단정적이다. 시간 순서는 알 수 없다. 웹 메타의 저자명 "Bo Ho"는 오기로 보이고 PDF는 "Bo Hong"이다.
- 코드와 license는 없다. checklist Q5가 [No]이고 "Code is not publicly available at submission"이라고 적혀 있다 (p.15). 본문, supp, 슬라이드, 포스터 페이지, `gh search repos` 2회, 웹검색 어디에도 링크가 없다.

**2 schema 정의와 위치**
- 정의: "abstract, reusable knowledge structures"(Abstract). 두 성질로 저차원성과 compositionality를 든다. compositionality는 시험하지 않았다.
- 조작적 형태는 sequence attractor다. 위치와 구성은 다음과 같다.
  - 위치: RNN 상태공간의 고정점 사슬이고, 그 구조는 Wrec가 만든다.
  - 구성: 시퀀스당 고정점 6개(총 24개)를 저차원 manifold가 잇는다 (Fig 3d–f).
  - 합쳐짐: 보상 구조가 같은 S1a·S1b·S2a는 하나의 abstract 사슬로 수렴한다 (Fig 4g–i).
  - 새 odor 결합: 새 odor는 Win으로 기존 attractor에 결합된다 (S-Fig S4).
- 연속/이산: 상태는 연속이고 고정점은 이산이다. 시간은 이산화됐다 (C2 참조).

**3 아키텍처**
- 입력 M=96(one-hot, 값 20, 5스텝), 순환 N=200 tanh, 출력 K=18(stage 1) 또는 2(stage 2~3).
- 모든 가중치가 학습 대상이다. Fig 3d 시각화에서는 Wout를 동결했고 Fig S4에서는 일부를 동결했다.
- 빠른/느린 분리가 없는 단일망이다.
- 키워드 스포팅은 LSTM/GRU 200 units에 16-dim MFCC를 쓴다 (S-D.2).

**4 학습 규칙 (outer loop와 within-lifetime 분리)**
- 목적식은 Eq.3~5다.
  - L1 = ½Σ‖y₀:₂−ŷreward‖² + 0.5·Σ‖y₂:K−ŷclass‖²
  - L2 = L3 = ½Σ‖y−ŷreward‖² (MSE 회귀)
- Adam, batch 8, 학습률은 1e-3 / 1e-3 / 1e-4(primitive / sequence / schema) (S-A.2). 단계 전환은 loss<0.05 기준이다. BPTT를 쓴다 (p.10).
- 커리큘럼은 primitive(odor identity+reward)에서 sequence(reward만), schema(새 odor 5문제) 순서다.
- **outer vs within:**
  - meta-objective도, outer loop도 없다. "no explicit meta-learning objective" (p.5).
  - 학습은 한 번의 run 안에서 가중치 gradient step이 단계·문제를 가로질러 이어지는 것이 전부다.
  - 한 trial 안에서는 활성(상태)만 변하고 fast weight는 없다.
  - 단계 경계와 기준은 실험자가 정한다.
  - 고정점 탐색의 BPTT는 분석용이지 학습이 아니다.

**5 형성·선택·적용·수정**
- 형성: primitive attractor 16개 중 14개(87%)가 시퀀스 attractor로 이동한다 (p.8, S-Fig S5). S1a·S1b·S2a의 같은 위치 attractor가 한 점으로 수렴한다.
- 선택/novelty gate: 없다.
- 적용: Wr와 Wout를 동결하고 Win만 학습하면 약 120 trial이 걸린다. 개입 없는 미세조정은 약 280 trial이다 (읽음, S-Fig S4). 단 학습률이 다르다 (1e-3 대 1e-4).
- 불일치 경험: S2a/S2b의 P4/P5는 보상 규칙이 뒤집힌 구간이다.
  - shaped 망은 attractor 거리를 약 20으로 유지한다 (Fig 5c).
  - unshaped 망은 두 궤적을 하나로 합쳤다가 나중에 갈라야 하고, "불안정하고 수렴 실패가 잦다" (p.9).
- split/merge/revise를 수행하는 명시적 메커니즘과 구조가 바뀌는 문제를 쓴 시험은 없다.

**6 지속성**
- 가중치 변화로 단계·문제를 가로질러 유지된다.
- activation-only ICL은 없다.
- replay, consolidation, forgetting/retention 평가도 없다.
- 해마–PFC 상보 시스템은 future work로만 언급한다 (p.10).

**7 과제·기준선·수치 (분모 포함)**
- 과제는 odor-sequence다. 4 시퀀스 × 6 위치 = 24 trial type이고 odor는 16개다.
- 문제당 trial 수 (Fig 2b, 10 seeds): 약 710 → 570 → 495 → 475 → 455 (읽음).
- 시드 수는 그림마다 다르다.
  - Fig 2b: 10 seeds
  - Fig 3b: 20 seeds
  - Fig 4·5·6b·S7: 5 seeds
  - Tab S1·S2: 6 seeds
  - Tab S3·S4·S5: 4 seeds
- Fig 4c (5 seeds, stage 1+2 trial 포함, 읽음): vanilla RNN 약 395→275, GRU 약 110→68, LSTM 약 115→45. RNN은 SD 막대가 겹친다.
- Tab S2 (6 seeds, problem 1 trial): shaping 964.6±110, alternating 857.6±21, reverse 1463±54, no-shaping 1725.5±75.
- Tab S3: reward-only 1259.3±130.3. 표에는 "4 seeds"라고 적혀 있지만 행 값은 Tab S2의 6-seed 값과 같다.
- 정확도 (Sec 4.4, p.9): 99.89±0.03% 대 93.20±2.4%.
  - 99.89±0.034는 Tab S4/S5에 4 seeds로 다시 나온다.
  - 93.20은 본문에서 한 번 나올 뿐이다.
- P4/P5 정확도 (Fig 5a, 5 seeds, 읽음): unshaped 약 0.35/0.27, shaped 약 1.0. 본문은 "only 25%"라고 쓴다.
- top-3 PC 분산비("Dim. red. index")는 그림마다 값이 다르다.
  - Fig 3b: shaped 0.79→0.835 (P1), 0.86→0.88 (P5).
  - 본문: unshaped 93% 대 shaped 82.5%.
  - S7a: 0.90→0.98.
  - 따라서 저차원성이 높다고 schema가 좋은 것은 아니다. unshaped가 더 압축돼 있다.
- 키워드 스포팅 (Fig 6b, 5 seeds, 읽음): GRU 약 35→16, LSTM 약 31→21 epoch로 90% test accuracy에 도달한다.
- 고정점 분석의 망 수는 미기재다 [O]. 대표 1망이 그려져 있다.
- 분석 방법:
  - PCA: 80 trajectory × T=95 (S-B.2).
  - 고정점: 입력 I=0에서 q=½‖F(r,0)−r‖² 최소화, q<1e-7. 안정성은 Jacobian 고유값이 1 미만인지로 판정한다 (S-C.2).
  - RDM: 480 trial을 시간평균하고 PCA k=5를 거쳐 24점의 유클리드 거리를 쓴다. noise 분산은 1.5 (S-C.1, A.2).
  - CCA와 attractor tracking(매 4 epoch)도 쓴다.

**8 신경과학 대응과 증거 수준**
- 비교 대상은 쥐 OFC (Zhou et al. 2021, Nature 590:606).
  - RDM Pearson r: 본문 ">90%", Tab S1 0.902±0.02 [수치 적합 1지표].
  - 무shaping 대조는 약 0.85 (읽음). Fig 2e의 y축이 0.7에서 시작한다.
  - LSTM/GRU는 0.89/0.87과 0.906/0.87로 차이가 작다 (S-Tab S1).
- 차원 압축과 학습 가속은 정성적 유사성이다.
- CCA 교차 문제 상관 CC1 0.95, CC2 0.64, CC3 0.77 (S-C.4). 데이터 쪽 값은 그림에만 있다.
- sequence attractor는 신경 데이터로 검증하지 않은 모형 내부의 기제 주장이다.
- OFC 데이터를 어떻게 얻었는지는 원문에 없다. 인용만 있다.

**9 한계와 보이지 않은 것**
- 저자 명시: BPTT는 생물학적으로 비현실적이다. PFC만 모형화했다 (p.10).
- 논문이 보이지 않은 것:
  - 코드와 데이터 공개.
  - retention과 forgetting.
  - 구조가 바뀌는 문제.
  - surface 유사도 lure.
  - "degeneracy 감소" 주장의 unshaped CCA 대조 (Fig S6은 shaped만. 본문도 "may be"로 hedge).
  - 외부 기준선.
  - 추가 supervision(odor identity, phoneme label)의 영향 분리. Tab S3에서 identity label 유무로 1259와 965가 갈린다.
- 내부 불일치:
  - S7b의 r(약 0.80~0.85)과 Fig 2e의 0.90.
  - 같은 0.902가 시드 10/6/4개로 보고된다.
  - Fig 2b의 fit이 legend에는 "Experment Fit", 캡션에는 polynomial, 본문에는 exponential로 적혀 있다.
  - 키워드 스포팅 schema 단계가 본문에서는 "full dataset"인데 S-D.1에서는 단어당 4개 발화다.
  - Fig 4i의 x축이 약 25 problem까지 간다.

**10 주장 검증표**

| 주장 | 판정 | 위치 | 한 줄 이유 |
|---|---|---|---|
| C1 schema = sequence attractor | CONFIRMED | Abs, 4.2 p.6-7, Fig 3, S-S3/S4 | 구현이 아니라 관찰된 emergent 해석이다. 고정점과 Jacobian, 셔플 시험이 근거다. |
| C2 연속시간 RNN | PARTIAL | Eq.1, S-A.2, C.2, D.2 | 정의는 CT이지만 τ=1, Δt=1이면 x(t+1)=Wrec·tanh(x)+Win·I로 환원된다 [A, Eq.14에서 유도]. 키워드 스포팅은 LSTM/GRU다. |
| C3 primitive→sequence→schema | CONFIRMED | 3.2 p.4-5 | 문구 그대로다. |
| C4 단계별 loss+Adam | CONFIRMED | Eq.3-5, S-A.2 | CE가 아니라 MSE 회귀다. BPTT를 쓴다. |
| C5 99.89 대 93.20 | CONFIRMED (수치 일치) | 4.4 p.9, S-Tab S4/S5 | task는 odor-sequence 보상 예측이다. 정확도 정의와 측정 시점, 93.20의 분모가 없다. [O] |
| C6 OFC 상관 | PARTIAL | 4.1 p.5-6, Fig 2e, S-Tab S1, S7b | r≈0.90이다. 무shaping 0.85, null/noise ceiling 없음, 시드 수 불일치, S7b 0.80~0.85, 데이터 출처 미기재. |
| C7 keyword spotting | CONFIRMED | 4.5, Fig 6, S-D | 4개 TIMIT 단어, LSTM/GRU, 5 seeds, 수치표 없음. shaped 쪽 epoch에 사전단계가 포함되는지 불명 [O]. |
| C8 새 규칙이 아니라 curriculum | CONFIRMED | 4.1 p.5, 5 p.10 | 표준 BPTT+Adam이다. 새 curriculum 알고리즘은 향후 과제로만 언급한다. |

C6 세부는 다음과 같다.
- 지표: 24×24 RDM의 Pearson r. 비교에 쓴 원소가 상삼각인지 전체인지는 미기재다 [O].
- 값: 위 필드 8.
- 출처: Zhou 2021 인용만 있다.

**11 FCL 연결 [PROPOSAL 전부]**
- **DQ1·DQ2**
  - 변환 코어(루프 블록 또는 Titans 상태전이)를 동결하고 임베딩/adapter만 학습시켜 새 surface에 적응시킨다.
  - Win-only 대 full 미세조정의 샘플 수를 비교한다. 원 실험은 학습률이 달라 LR을 맞춰야 한다.
- **DQ3**
  - 같은 surface 단서에 반대 출력이 요구되는 문맥 쌍(P4/P5)을 contingency-reversal 스위트로 만든다.
  - 문맥 간 표상 거리를 감시한다 (Fig 5c의 약 20 대 0 붕괴).
  - 먼저 합치고 나중에 가르는 순서가 실패 모드다. 저차원성만 보상하면 안 된다.
- **DQ5**
  - "입력 0으로 수렴까지 반복" 탐침(S-C.3)은 recurrent depth의 수렴 기반 halting 후보다. 논문에는 없는 응용이다.
- **DQ6·DQ8**
  - 새 surface의 연속 문제에서 trial-to-criterion 곡선 (5문제에서 −36%)을 H-SAMPLE 하니스로 쓴다.
  - 문제 수를 늘리고, 구조가 다른 surface 유사 lure를 추가해야 한다.
  - RDM-참조 상관은 oracle 구조 RDM과 행동 지표를 함께 본다. 약 0.85 대 0.90의 낮은 민감도 때문이다.
- **DQ7**
  - 논문에 없으므로 이전 문제 재평가를 직접 설계해야 한다.
- **실패 모드**
  - τ=1 tanh RNN의 zero-input 고정점이 transformer로 이식된다는 보장이 없다.
  - 경계와 기준이 harness 공급이다.
  - 추가 supervision이 shaping 이득을 섞는다.
  - Melete 계보 교훈: "고정 무작위 순환 + 학습 입력/출력" 기준선이 없다. 학습된 attractor의 필요성은 증명되지 않았다.

**12 재현·프로토타입**
- 규모: N=200 RNN. Intel i9-14900K CPU에 32GB RAM, GPU 없음, 학습 1회 약 30분, 튜닝 200회 (checklist Q8).
- RTX 5070 Ti는 불필요하다. 이유는 소형이고 순차적이라서다.
- 코드가 없어 "코드 ↔ 수식" 매핑은 해당 없다.
- 병목:
  - 시퀀스 구조는 Fig 1c-d를 읽어 복원해야 한다 (간격이 "5-10 균등"인지 "고정"인지도 모호하다).
  - 쥐 OFC RDM 데이터는 확보 경로 미상이다.
  - TIMIT는 LDC 라이선스다.

---

### 2. GOUDAR23

#### 2.1 접근 증거
- **route:**
  - 정식 제목은 "Schema formation in a neural population subspace underlies learning-to-learn in flexible sensorimotor problem-solving"로 확인했다. 요청문의 "..."를 채운 것이다.
  - 본문은 PMC 저자 수락본(NIHMS2033356, PMC11559441)이다. NCBI efetch로 받은 JATS XML이고 수식은 MathML이다. 내 `python3 -I` 스크립트로 변환했다.
  - supplement는 Nature static-content MOESM1(31쪽)과 MOESM2(Reporting Summary 2쪽)다.
  - bioRxiv v1/v2는 Wayback 스냅샷으로 받았다. 직접 접근은 Cloudflare 1015(429)로 막혔다.
- **VoR:** 유료라서 nature.com에서는 초록, data/code availability, 참고문헌만 보였다. 본문은 accepted manuscript다. VoR과의 편집 차이는 배제할 수 없다 [O].
- **version_date:** received 2021-09-02, accepted 2023-02-27, online 2023-04-06(Nat Neurosci 26(5):879–890), PMC XML 날짜 2024-11-14, bioRxiv v1 2021-09-02, v2 2022-08-02.
- **pages / words:** pages는 null이다. 본문이 XML이라 쪽수가 없다. 동반 PDF는 SI 31쪽, v1 80쪽, v2 87쪽이다. fulltext.txt는 13,028 words이고 참고문헌과 Fig 1~8 캡션을 포함한다.
- **읽은 범위:**
  - 본문 전체와 Methods 전체(수식 포함).
  - supp는 Note 1.1.1~1.1.3, Discussion 1.2.1~1.2.2, Methods 1.3.1, Supp Fig 1~10 캡션. Supp Fig 2와 6은 이미지로 확인했다.
  - Fig 1·3·6은 이미지로 확인했다.
  - Reporting Summary는 글꼴이 깨져 눈으로 해독했다.
  - Extended Data, Source Data, Peer Review File은 페이지에 없다.
  - bioRxiv v1/v2는 버전 비교(핵심 수치와 초록 대조)에만 썼다.
- **파일별 sha256 앞 16자리:**

| 파일 | sha256 앞 16자리 |
|---|---|
| PMC efetch XML | 3151486228fde2c6 |
| nature_article_page.html | 22b65aec259feb0f |
| MOESM1 | 454b3a7bddb1ff6f |
| MOESM2 | b2049a2612252a12 |
| Fig1 / Fig3 / Fig6 png | f3380e3c5a009895 / 71798e8a2634684e / 758dfc32389193d0 |
| bioRxiv v1 | 379c2c49624bc718 |
| bioRxiv v2 | 1b6c5082ed624b11 |
| biorxiv_api json | c4c9377dbfd9b56b |
| openalex json | d85cb5b5d8b94d98 |
| `fcl-sbl-fulltext-20261111/GOUDAR23/fulltext.txt` | 0e1fa52b125fd783 |
| `fcl-sbl-fulltext-20261111/GOUDAR23/supp_fulltext.txt` | 70d93b953b2738d3 |

- 상세는 `fcl-sbl-fulltext-20261111/GOUDAR23/access.json`, `fcl-sbl-fulltext-20261111/GOUDAR23/extraction.json`에 있다.
- 시도하고 막힌 경로는 PMC PDF(proof-of-work 인터스티셜), Europe PMC REST(500 ×2), Europe PMC render(Cloudflare 403)다. 우회하지 않았다.
- **버전 비교 (본문 검색 기준):**
  - v1 / v2 / accepted의 핵심 수치는 모두 같다. τ=47.52±26.22, a=21.33±3.85, 2.36±0.18차원, 88.54±3.16%, 7.98±1.48.
  - v2 초록은 accepted와 거의 같다. v1은 제목이 "Elucidating the neural mechanisms of Learning-to-Learn"이고 초록 프레이밍이 다르다.
  - "meta-learning" 언급이 8회에서 17회로, "Reptile"이 0회에서 7회로 늘었다. Reptile 비교는 개정에서 추가됐다.

#### 2.2 필드 1~12

**1 서지**
- Goudar, Peysakhovich, Freedman, Buffalo, Wang. Nat Neurosci 26(5):879–890. DOI 10.1038/s41593-023-01293-9.
- 코드: `https://github.com/xjwanglab/learning-2-learn`, commit `1478e3b06adb1df72aaa50dc5c9b20b0d838fbd9`, MIT.
- 심사: 익명 심사자 감사문만 있다. 심사 파일은 없다.

**2 schema 정의와 위치**
- 심리학 정의를 따른다. 신경 기질은 집단 활동의 저차원 decision subspace/manifold다 (Results 2).
  - mean decision 성분: 시간 구조, 조건 독립.
  - residual decision 성분: 응답 선택.
  - 이 둘이 합쳐진 decision subspace(m=4 PC)가 문제 간에 공유된다.
- 가중치가 아니라 활동 부분공간이 schema다. 가중치는 vector field를 바꾼다.
- 연속적이다. 고정점이나 attractor 주장은 없고 궤적과 vector field를 쓴다.
- "schema 형성"과 "structure learning"(schema를 효율적으로 쓰는 법을 배우는 것)을 구분한다 (S-Disc 1.2.2).

**3 아키텍처**
- N=100 softplus rate unit, τ=100 ms, Δt=1 ms, OU 잡음.
- 입력 11개(10차원 정규직교 자극 + fixation), 출력 3개(fixation, 응답 1, 응답 2). trial은 2초다.
- W_in, W_rec, W_out, 편향, r0 전부 학습 대상이고 문제 간에 값을 유지한다.
- 단일망이고 모듈 분리가 없다. 3개 시간척도(trial 내 활동, 문제 내 가중치, 문제 간 누적)는 과제 구조에서 창발한다 (Fig 8).

**4 학습 규칙 (outer vs within)**
- trial마다(batch 1) BPTT와 Adam (lr 1e-4, β1=0.3, β2=0.999)을 쓴다. Adam moment는 문제마다 리셋한다.
- 손실은 마스크된 cross-entropy에 다음 정규화를 더한다.
  - W_in L2 1e-4, W_out L2 0.1.
  - W_rec 상위 k=10 특이값 패널티(β=0.1).
  - homeostatic rate 항(β_r=5e-4, 설정값 h는 문제 1의 마지막 50 trial에서 고정).
- 기준은 50 trial 평균 오차 < 0.005다.
- **outer vs within:**
  - outer loop가 없다. 저자도 "Reptile에 가장 가깝지만 명시적 outer loop는 없다"고 쓴다 (S-Disc 1.2.1).
  - 가중치 변화가 문제를 가로질러 무한히 누적된다.
  - harness가 공급하는 것:
    - 문제 경계(Adam 리셋, 새 자극쌍, 기준 기반 전환).
    - 손으로 정한 안정화 정규화. 작은 β_Wrec는 후반 문제에서 불안정하고 큰 β_Wrec는 효율을 떨어뜨렸다고 서술한다 (Methods).
    - 문제 1에서 고정한 homeostatic 설정값.
  - BPTT는 trial 내 시간 신용할당용이다.

**5 형성·선택·적용·수정**
- 형성: 첫 문제 이후 decision/stimulus 부분공간이 생긴다.
- 적용: 새 자극은 기존 decision 표상에 사상된다.
  - weight-driven VFC는 기존 표상이 새 자극으로 왜곡되는 것을 막는 방향(orthogonal 성분)으로 쓰인다 (Fig 5b).
  - 이는 새 경험을 기존 schema 안에서 처리하면서 schema를 보호하는 assimilation에 해당한다.
- 구조 변경 (2→3 mapping, Fig 3d, 읽음): naive 3-mapping 약 5100, 2→3 약 2000, 3→3 약 750 trial이다. 부분 이전이다.
- novelty gate와 schema 생성/병합/분할은 없다.

**6 지속성**
- 모두 파라미터 변화다. activation-only ICL은 없다. replay와 consolidation도 없다.
- 재학습 savings (S-Fig 2, 10망, 읽음):
  - 초기: novel 약 70~83 대 repeat 약 55~60 (직전 문제는 약 22).
  - 중기: 약 25 대 12~17.
  - 후기: 약 21 대 10~17.
- 이 savings만이 유일한 retention 근거다. 이전 문제의 zero-shot 성능이나 망각 측정은 없다.

**7 과제·결과 (분모 포함)**
- 과제: 지연 sensorimotor 연합. 자극 2개를 응답 2개에 대응시키는 문제를 약 1,000개 연속 학습한다.
- 학습 가속 곡선:
  - 문제 1은 수천 trial이다 (약 3000, Fig 3c. 예시망 약 3200, Fig 1d).
  - 문제 2는 수백 trial이다.
  - [A] 배포 처리 데이터 10망: 문제 2는 255±255(s.d.), 문제 2~51 평균 98.6±25.5, 마지막 50문제 평균 20.7±7.4.
- 지수 fit l(p)=s·exp(−(p−1)/τ)+a (Fig 1e):
  - 30망, 문제 2부터 fit.
  - τ=47.52±26.22 문제, a=21.33±3.85 trial (mean±s.d.).
  - Fig 1d 예시망의 τ는 73 문제다.
- 유사도 (Fig 1f, 10망 × 자극쌍 50개, 읽음): 문제 3의 trial 수가 코사인 유사도 0에서 약 175, 0.5에서 약 76, 1에서 약 7이다.
- 공유 decision subspace (Fig 2b, 첫 50문제, 10망):
  - 2.36±0.18차원(participation ratio), 집단 분산의 88.54±3.16%.
  - stimulus 표상은 7.98±1.48차원이다.
  - 다른 50문제 묶음에서도 "정량적으로 비슷하다"고만 쓰고 수치는 없다.
- manifold 교란 (Fig 3c, 10망 × 교란 50회, 읽음): 두 번째 문제 trial 수는 frozen readout 약 350, S→S 약 450, D→S 약 3300이다. 문제 1은 약 3000이다.
- 가중치 변화 (S-Fig 6b, 읽음): ΔW_rec(Frobenius)가 frozen readout에서 약 0.12, D→S에서 약 1.5다. weight-driven VFC는 약 1.5 대 12.5다.
- 가중치 변화량과 trial의 관계 (Fig 6a): 예시망 R²=0.7이고 10망 violin은 약 50~82%(읽음)다. [A] 배포 데이터는 0.703±0.051 (범위 0.618~0.798, 첫 500문제)이다.
- 가중치 변화량의 문제 간 감소 (Fig 6b):
  - ΔW_rec, ΔCurrent, VFC가 문제 약 1000에서 약 0.42~0.46으로 줄어든다 (첫 그룹 대비, 읽음).
  - [A] 배포 데이터는 마지막 그룹/첫 그룹 비가 0.52 / 0.57 / 0.59이고 망 간 편차가 크다 (0.36~1.09). 논문 그림의 0.42와 정확히 일치하지 않는다.
  - [A] 대비: trial 수는 약 4.8배 줄지만 ΔW_rec는 약 1.9~2.4배만 준다.
- 분석 방법:
  - demixing: 문제 평균 궤적을 센터링 없이 PCA한 뒤 m=4 PC (최소 98% 분산)를 쓴다.
  - 차원은 participation ratio로 잰다.
  - VFC 분해(Eq.4~9)에서는 병렬 성분과 직교 성분을 나눈다.
  - 대조: S→S 교란, 가중치 동결 조건, 하이퍼파라미터 스윕(10망/설정).
  - 비교 기준선은 첫 문제(naive망)이고 외부 meta-learning 기준선은 없다.

**8 신경과학 대응과 증거 수준**
- 대상은 원숭이 PFC 시각운동 연합학습이다.
  - 근거 문헌 Cromer 2011은 잘 훈련된 원숭이가 15~20 trial에 학습한다는 보고다.
  - "지수적 학습-학습" 원숭이 데이터는 "Peysakhovich et al., unpublished"다.
- 신경 데이터 적합이 아니다. 정성적 유사성과 검증 가능한 예측 4개를 제시하는 수준이다. VFC는 모형 내부의 기제 주장이다.

**9 한계와 보이지 않은 것**
- 저자 명시:
  - blank-slate 초기화는 발달 경험과 다르다.
  - 학습 알고리즘이 비생물학적이지만 결과는 학습 규칙에 의존하지 않을 수 있다고 쓴다.
  - 다른 가소성 형태는 배제하지 못했다.
- 논문이 보이지 않은 것: 실제 신경 데이터, 생물학적으로 그럴듯한 규칙에서의 재현, 망각·간섭 측정, 구조-유사도 분리(Fig 1f 외), 수백 문제 미만에서의 효과.
- S-Note 1.1.1: 기본 설정에서는 순환 가소성이 입력 가소성보다 효율적이다. 그러나 입력 활동 ×10과 W_in gain 0.05로 재조정하면 동결-순환 망도 완전 가소 망과 비슷해진다. "순환 가소성이 필요하다"고 읽으면 안 된다.

**10 주장 검증표**

| 주장 | 판정 | 위치 | 한 줄 이유 |
|---|---|---|---|
| G1 공유 저차원 decision manifold | CONFIRMED | Results 2, Fig 2, Methods | 문제 평균 demixing으로 얻은 2.36차원, 분산 88.5%다. subspace는 망별 구성상 m=4로 정의되고, 재사용은 Fig 3에서 인과 시험한다. |
| G2 재사용으로 가중치 변화량 감소 | CONFIRMED | Results 3·5, Fig 6, S-Fig 6b | 재사용을 막으면(D→S) 약 8~12배 큰 변화가 필요하다. 문제 간에는 ΔW_rec 약 2배 감소, trial 약 5배 감소, R²≈0.7이다. |
| G3 명시적 meta-learning 없음 | CONFIRMED | Results 1, Methods, S-Disc 1.2.1 | meta-objective는 없다. 저자가 Reptile에 가장 가깝다고 인정한다. 경계와 정규화는 harness가 공급한다. |

G2 해석 주의점은 다음과 같다. [P] Adam은 step 크기가 정규화돼 있어, ΔW 크기와 trial 수의 상관이 일부 기계적일 수 있다.

**11 FCL 연결 [PROPOSAL 전부]**
- **DQ1·DQ8**
  - 재학습 없이 같은 구조의 문제 ≥50개에 걸쳐 은닉 상태를 문제 평균한 뒤 PCA(demixing)하고 participation ratio와 설명 분산을 측정한다.
  - 읽기 층(lm_head 또는 probe)을 회전하거나 동결하는 D→S 대 S→S 교란으로 재사용의 인과성을 시험한다.
- **DQ6·H-SAMPLE**
  - 지수 fit의 (τ, a)와 "trial-to-criterion 대 자극 코사인 유사도" 곡선(Fig 1f)을 측정 프로토콜로 쓴다.
  - 단 이 곡선은 이 망이 surface 유사도에 크게 의존한다는 뜻이다 (유사도 1에서 약 7, 0에서 약 175 trial). 구조는 같고 surface만 다른 lure와 구조는 다르고 surface만 비슷한 lure를 별도로 추가해야 한다.
- **DQ3·DQ7**
  - 갱신량을 "방어(직교)" 성분과 "생산(병렬)" 성분으로 나눠 기록하고, selective-update 컨트롤러를 방어 비중으로 평가한다.
  - 구조 변경 시험으로 2→3 mapping을 쓸 수 있다 (약 5100 → 2000 → 750).
  - 망각은 논문에 없으므로 savings 외에 이전 문제 재평가를 직접 설계해야 한다.
- **DQ4**
  - 3개 시간척도(trial 내 / 문제 내 / 문제 간 누적)를 각각 로깅한다. Sleep은 "새 문제 없이 누적만 하기"로 시험해 볼 수 있다. 논문에는 없다.
- **DQ5**
  - 해당 내용이 없다. 근거 없이 주장하지 않는다.
- **실패 모드**
  - 시간상수 약 48~73 문제, 수백 문제 이상이 필요하다.
  - 안정성에 손으로 정한 정규화가 필요하다.
  - 문제 경계는 harness가 공급한다.
  - Melete 계보 교훈: "고정 구조" 기준선이 없고, S-Note 1.1.1이 보이듯 학습된 순환의 필요성은 입력 척도에 좌우된다.

**12 재현·프로토타입과 코드 감사 (읽기 전용, 실행 안 함)**
- 규모: N=100, batch 1, 문제당 2000 스텝 BPTT, 문제 약 1000개. 환경은 Python 2.7, Numpy 1.16.5, TensorFlow 1.15, 분석은 Matlab이다 (Reporting Summary).
- 총 실행시간은 논문에 없다 [O].
- **CPU:** 이론상 가능하다. TF 1.x 정적 그래프에 2000 스텝을 for문으로 전개하는 구조다 (network.py L170).
- **RTX 5070 Ti:** 소형이고 batch 1이라 이득이 없다. TF 1.15는 Blackwell 시대 이전이라 이식도 비현실적이다.
- [A] train.py에 `disable_eager_execution`이 없어 TF2에서는 placeholder 때문에 실패할 가능성이 높다 [P: PyTorch 포팅이나 패치 권장].
- [A] 배포 데이터: `data/`가 비어 있고 pre-trained 데이터는 Google Drive 링크라 가져오지 않았다. `results/`에 처리된 .mat이 있다.
- 코드와 논문 수식의 매핑:

| 논문 | 코드 |
|---|---|
| Eq.(2) 누설 softplus RNN, OU 잡음 | network.py L140-153 (`call`), L156-192 (`unroll`) |
| softmax 읽기, CE(마스크 100 ms), 정규화 항 | network.py L234-312, 마스크는 train.py L173-175 |
| Adam β1=0.3, 문제별 moment 리셋 | network.py L310, L357-358, train.py L392 |
| 과제 생성(정규직교, fixation 1/√10) | train.py L140-177, L214-225 |
| 기준 0.005, 50 trial | train.py L301-318 |
| homeostatic 설정값 | train.py L333-336 |
| manifold 교란(k=4) | train.py L63-115, L338-371 |
| VFC, ΔW_rec 노름 | analysis/figs5and6.m L17-200 |
| 지수 fit | analysis/fig1.m (시간상수 범위 5~200) |
| manifold 교란 도표 | analysis/fig3.m |

- 논문과 코드의 차이:
  - [A] 코드는 gradient clipping(전역 노름 1)을 쓰는데 Methods에 없다 (network.py L318-320).
  - [A] 코드는 trials = len(perf)−50으로 센다. NaN이나 20000 trial 초과 시 실패 처리하는 규칙도 논문에 없다 (train.py L301-318).
  - [A] β_Wrec: 논문은 0.1, 코드의 `l2_wR`은 0.001이다. 논문 수식에 1/N(N=100)이 붙어 있어 같은 값이다.
  - [A] 배포 처리 데이터는 10망이다 (TC 37.9±16.1, AS 22.7±2.8). 논문은 30망(47.5±26.2, 21.3±3.9)이다. Fig 1d 예시의 "Time const.=73"도 배포 fits의 예시망(시간상수 24.1)과 다르다. 이유는 확인 불가다 [O].
  - [A] fig2.m, fig7.m은 상세히 읽지 않았다. 분석 스크립트는 Fig 1·2·3·5/6·7만 있고 4와 8은 도식이다.

---

### 3. 자체 점검

**sha256sum -c** (최종 재검증):
- CHU25: 10줄 모두 OK
- GOUDAR23: 13줄 모두 OK

**access.json 필수 키**:
- 15개 키가 두 파일 모두 존재한다.
- GOUDAR23은 `pages_note` 키가 추가돼 있다.
- CHU25의 `code`는 null이다.
- GOUDAR23의 `code`는 {url, commit, license, local_path}다.

**미해결·불확실**
- CHU25
  - OpenReview 심사본·리뷰 미확보.
  - 정확도의 정의·시점, 93.20의 분모.
  - 무shaping 기준선의 학습률.
  - OFC 데이터 확보 방식, RDM 비교 원소.
  - S7b 대 Fig 2e의 불일치.
  - 키워드 스포팅의 "full dataset" 대 4 발화.
  - shaped epoch에 사전단계가 포함되는지 여부.
  - 그림 읽음 값은 모두 근사다.
- GOUDAR23
  - VoR과 accepted manuscript의 편집 차이.
  - 원숭이 데이터는 unpublished다.
  - repo 처리 데이터와 논문 수치의 불일치 원인.
  - Fig 6b 끝값 0.52 대 0.42.
  - pre-trained 데이터는 Google Drive 링크라 미확보.
  - 총 실행시간 미기재.

**프로세스 메모**
- 호스트 I/O 압박으로 Bash 훅이 호출 1건을 차단했다. 대기 후 경량 명령으로 재개했다.
- 일부 `python3 -I` 호출을 cwd가 download/ 안인 상태에서 실행했다. `-I` 격리 모드였고 파일은 데이터로만 읽었다. download 폴더에는 .py/.pth 파일이 없고, 소스 repo는 git status가 깨끗하다.
- 코드는 실행하지 않았다. pip install도 하지 않았다.
- 보조 스크립트는 `_scripts/W2/`에 있다 (`jats_to_text.py`, `mat5_min.py`, `audit_l2l_results.py` 등).
- 코드 clone: `fcl-sbl-fulltext-20261111/code/learning-2-learn`
