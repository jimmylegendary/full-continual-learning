# SBL 신경망 구현 논문 11편 원문 검토 — 2026-11-11

상태: **LITERATURE 검토 + PROPOSAL**. 이번 작업은 논문 원문을 읽고 외부 요약을 검증한 것이다. 모델 구현·학습·성능 검증은 하지 않았다. 코드는 읽기만 했고 실행하지 않았다.

계기: 사용자가 ChatGPT 조사 요약("뇌과학의 schema를 신경망 아키텍처와 학습 메커니즘으로 구현한 연구들")을 공유하고, 세부 논문을 **원문 전체로 읽어** 생각의 시작점으로 삼자고 요청했다(USER, 2026-11-11).

## 0. 요약

- 대상 11편 모두 원문(본문·Methods·부록) 기준으로 읽었다. 판본·분량·확보 경로는 [§1](#1-범위와-방법)에 있다.
- **외부 요약은 대체로 맞지만 고칠 곳이 있다.**
  - Chu: "연속시간 RNN"은 사실상 이산시간이다.
  - Elder: 고정되는 층과 갱신되는 층의 방향을 "상위/하위"라는 말로 거꾸로 적기 쉽다.
  - Hwu: novelty가 바꾸는 것은 학습률이 아니라 replay 횟수다.
  - Kumar: "fully neural"은 부분적으로만 맞다.
  - Miconi: 초록의 예시와 실제 실험 설계가 다르다.
  - Swaminathan: "LLM에서도 같은 기제"라는 부분은 저자들의 추측이다.
- **가장 중요한 공통 관찰:** 이번에 읽은 11편 어디에서도 **학습된 schema 구조가 같은 예산의 고정·무구조 대조보다 낫다는 직접 비교**를 찾지 못했다. 여러 편은 그런 대조가 없고, 일부는 오히려 단순 대조가 비슷하거나 낫다. Melete J1에서 얻은 교훈(학습된 graph의 추가 가치 미입증)과 같은 방향이다.
- **"schema가 학습을 바꾼다"는 기제는 조각으로만 구현돼 있다.** 바꾸는 대상이 논문마다 다르다.
  - 무엇을 저장하나: Spens
  - 얼마나 replay하나: Hwu
  - 어느 슬롯을 다시 묶나: Swaminathan
  - 쓰기 크기: TEM
  - 언제·어디에 쓰나(학습된 neuromodulator): Miconi
- **잘 측정되지 않은 것:** 망각·보존, 표면 유사성과 구조의 분리, 같은 품질의 추론 계산량. 특히 우리 H-COMPUTE를 직접 시험한 논문은 없다.
- **갭 주장**("schema를 스스로 발견·형성·수정·통합하고 그 schema가 학습 규칙을 제어하는 범용 지속학습 아키텍처는 없다")은 검색 범위 안에서 반례를 찾지 못했다. 단 이는 범위에 한정된 결론이다([§6](#6-갭-주장-판정)).

## 1. 범위와 방법

| ID | 논문 | 읽은 판본 | 분량 |
|---|---|---|---|
| SPENS24 | Spens & Burgess, *A generative model of memory construction and consolidation*, Nat Hum Behav 8:526–543 (2024) | 출판사 OA VoR + SI | 18,075단어 |
| HWU20 | Hwu & Krichmar, *A neural model of schemas and memory encoding*, Biol Cybern 114:169–186 (online 2019-11-04) | 저자 호스팅 VoR + ESM, bioRxiv v1 대조 | 11,418단어 |
| CHU25 | Chu, Hong, Zou, Mi, *Shaping Sequence Attractor Schema in Recurrent Neural Networks*, NeurIPS 2025 | proceedings VoR + supplement | 9,937단어 |
| GOUDAR23 | Goudar et al., *Schema formation in a neural population subspace underlies learning-to-learn in flexible sensorimotor problem-solving*, Nat Neurosci 26:879–890 (2023) | PMC accepted manuscript + SI (VoR 유료) | 13,028단어 |
| ELDER26 | Elder et al., *Hierarchical learning creates invariant schema within plastic neural networks*, J Comput Neurosci 54:503–514 (2026) | Europe PMC VoR XML + supplement | 6,179단어 |
| MICONI25 | Miconi & Kay, *Neural mechanisms of relational learning and fast knowledge reassembly in plastic neural networks*, Nat Neurosci 28:406–414 (2025) | 저자 공개 조판 proof + VoR supplement, bioRxiv v3 대조 | 10,479단어 |
| TEM20 | Whittington et al., *The Tolman-Eichenbaum Machine*, Cell 183:1249–1263 (2020) | Europe PMC VoR XML + VoR PDF + Tables S1–S4 | 23,761단어 |
| KUMAR26 | Kumar et al., *One-shot learning of paired association navigation with biologically plausible schemas*, J Neurosci 2026 early release e1803242026 | arXiv v5(2026-10-20, 70쪽). VoR 유료 | 22,319단어 |
| SWAMI23 | Swaminathan et al., *Schema-learning and rebinding as mechanisms of in-context learning and emergence*, NeurIPS 2023 | proceedings VoR + supplement, arXiv v1 TeX 대조 | 10,989단어 |
| STRUCTK25 | Yu, Yan, Jin, *Structural knowledge: from brain to artificial intelligence*, Artif Intell Rev 58:264 (2025) | Springer VoR HTML 본문 + 표 1–5. curl이 봇 차단에 막혀 사용자 브라우저에서 렌더링한 텍스트를 받았고, 브라우저가 계산한 해시와 일치한다 | 14,449단어 |
| SPECTRUM26 | Samiei, Precup, Richards, *The schema spectrum: Emergent structures and levels of abstraction in AI and the brain*, Neuron 114:1898–1907 (2026) | 저자 사이트 corrected proof, 저자 원고 v2 대조 | 8,019단어 |

방법:
- 논문을 6묶음으로 나눠 worker가 정독했다. 리더 검증과 보완 worker의 재확인을 거쳤고, 마스터가 핵심 주장 일부를 원문에서 다시 찾아 대조했다.
- 각 논문에 대해 다음 12항목을 채웠다.
  1. 서지
  2. schema 정의·위치
  3. 구조
  4. 학습 규칙(바깥 루프와 생애 내 가소성 구분)
  5. 형성·선택·수정
  6. 지속성
  7. 수치와 분모
  8. 신경 대응
  9. 한계
  10. 외부 요약 주장 판정
  11. FCL 연결
  12. 재현성
- 원문 파일과 추출 본문은 저작권 때문에 저장소에 넣지 않았다. 호스트 작업 폴더 `fcl-sbl-fulltext-20261111/`에 보존돼 있다. 저장소에는 판본·경로·SHA-256만 [evidence.json](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/evidence.json)으로 남겼다.
- 논문별 상세 기록은 [README.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/README.md)에서 시작한다.

## 2. 외부 요약 검증 결과

판정: CONFIRMED(원문과 일치) / PARTIAL(일부만 맞거나 단서 필요) / WRONG / NOT-FOUND.

| 논문 | 외부 요약의 주장 | 판정 | 원문 기준 정정·단서 |
|---|---|---|---|
| SPENS24 | 해마 = Modern Hopfield Network, 피질 schema = VAE 연속 잠재분포, 공고화 = replay 기반 teacher–student | CONFIRMED | replay는 noise cue 10,000개를 MHN에 한 번 넣어 만든 고정 집합이다. 저자는 VAE를 "illustrative"라고 명시한다. 학습된 schema 대 고정 특징의 비교는 없다 |
| SPENS24 | schema = 여러 경험의 공통 생성적 확률 구조, 코드 공개 | CONFIRMED | 데이터셋 하나를 일괄 학습한다. 코드는 있으나 LICENSE가 없다 |
| HWU20 | 해마+mPFC indexing, representation stream | CONFIRMED | 공개 코드에서는 mPFC→vHPC 가중치가 학습되지 않는다 |
| HWU20 | 친숙·새로움 neuromodulation이 부호화를 조절 | CONFIRMED(정밀화) | 조절 대상은 학습률이 아니라 공고화 epoch 수다(Eq.10). 고정 epoch 조건도 새 연합을 학습한다. 저자도 neuromodulator가 빠른 학습에 필수가 아니라고 쓴다(§4.4) |
| HWU20 | context gating으로 간섭 억제, schema 일치 경험을 더 빨리 학습, catastrophic forgetting과 연결 | PARTIAL | 망각은 줄지만 남는다. 새 schema는 기존 schema보다 빨리 배우지 않는다. 지속학습 baseline이 없는 toy 과제다 |
| CHU25 | schema = RNN sequence attractor, primitive→sequence→schema 단계 학습, 각 단계 Adam | CONFIRMED | attractor는 설계된 모듈이 아니라 관찰된 창발 구조다. 손실은 MSE 회귀다 |
| CHU25 | 연속시간 RNN | PARTIAL | τ=1, Δt=1이라 사실상 이산시간이다. keyword spotting은 LSTM/GRU로 했다 |
| CHU25 | shaping 적용 99.89% 대 미적용 93.20% | CONFIRMED(수치) | 본문에 99.89±0.03 대 93.20±2.4로 나온다. 정확도 정의와 93.20의 분모는 없다 |
| CHU25 | 표상 기하가 쥐 OFC와 높은 상관 | PARTIAL | r≈0.90, shaping 없는 망도 ≈0.85다. 다른 그림(S7b)은 0.80–0.85로 일치하지 않는다 |
| CHU25 | 새 학습 규칙이 아니라 curriculum으로 창발 | CONFIRMED | 공식 코드는 없다(checklist에 "No"). unshaped 망이 오히려 더 저차원이었다 |
| GOUDAR23 | 공유 저차원 decision manifold, 재사용으로 가중치 변화량 감소, 명시적 meta-learning 없음 | CONFIRMED | 문제 경계·Adam 리셋·안정화 정규화는 실험 틀이 공급한다. 학습 속도가 자극의 표면 유사도에 크게 의존한다 |
| ELDER26 | schema = 학습이 진행돼도 핵심 연결이 변하지 않는 하위 회로, ENN 계층 학습 | CONFIRMED | ENN은 층별 SVM 구성이다. "새 데이터"는 같은 과제의 더 큰 부분집합으로 처음부터 다시 학습한 것이고 순차 학습이 아니다 |
| ELDER26 | "상위 입력 표현 개선, 하위 핵심 판단 구조 보존" | CONFIRMED(용어 주의) | 고정되는 쪽은 출력 쪽 hidden layer(HL1·HL2)다. 갱신되는 쪽은 입력 쪽 가중치(IL)다. 우리 11-09 기록의 "상위 schema circuit"은 같은 사실을 반대 어휘로 적은 것이다 |
| ELDER26 | backprop과 비교, 62.3±3.8% 대 56.1±4.7% | CONFIRMED(수치) | ±의 정의는 없다. 3-class 과제이고 hidden이 커지면 MLP가 낫다 |
| MICONI25 | A>B>C, D>E>F 학습 후 C>D 하나로 전체 순서 통합 | PARTIAL | 실제 설계는 ABCD+EFGH이고 연결쌍 D>E를 4 trial 제시한다. 초록 예시와 다르다 |
| MICONI25 | neuromodulated plasticity RNN을 meta-learning으로 학습 | CONFIRMED | 바깥 루프는 A2C+BPTT, 안쪽은 gradient 없는 Hebbian trace다. 연결마다 다른 가소성 계수가 필수다(단일 스칼라로 바꾸면 active 해가 0/30) |
| MICONI25 | 과거 표현을 재활성화해 제시되지 않은 항목 관계까지 수정 | CONFIRMED(단서) | 상관 분석과 대표 네트워크 1개에 근거한다 |
| TEM20 | 구조 표현과 개별 경험 표현 분리, recurrent 구조 + 해마 attractor 기억, 비공간 관계 과제 | CONFIRMED | 논문은 "schema"라는 말을 쓰지 않는다(structural knowledge). 구조는 바깥 루프에서만 형성되고, 빠른 기억 M은 환경마다 0으로 리셋된다 |
| KUMAR26 | fully neural agent | PARTIAL | 관계 계산 모듈(NAVIGATE)은 backprop으로 사전학습한 뒤 고정한다. gating의 WTA·곱셈은 알고리즘 구현이다 |
| KUMAR26 | 저차원 공간 표현 + one-shot 연합 기억 + controller, TD + 보상 변조 Hebbian, WM gating 학습, 방해 자극 하 one-shot | CONFIRMED(단서) | 구조(좌표) 코드는 place cell remap에 걸쳐 전이되지 않고 약 20 session 재학습한다. 하이퍼파라미터를 평가 지표로 튜닝했다 |
| KUMAR26 | arXiv 2021 → J Neurosci 2026 | CONFIRMED | v1은 제목과 내용이 다른 reservoir 논문이다. v5(2026-10-20)가 early release(2026-10-26)와 초록이 같다 |
| SWAMI23 | schema template / CSCG, schema learning + rebinding이 ICL 기제 | CONFIRMED(CSCG 한정) | rebinding은 학습에서 창발한 것이 아니라 설계된 test-time 알고리즘이다 |
| SWAMI23 | LLM에서도 같은 기제 | NOT-FOUND | 저자 표현은 "We conjecture"다. transformer 실험은 없다 |
| STRUCTK25 | 뇌 schema를 AI 모델로 연결한 연구를 체계적으로 정리 | PARTIAL | 분류 체계로 조직된 서술형 리뷰다. 검색·선정 프로토콜이 없다. cognitive map 쪽 비중이 크다 |
| SPECTRUM26 | schema는 분리된 기억 객체가 아니라 분산 표현의 추상화 수준 스펙트럼 | CONFIRMED | 최종본은 "not a distinct set of mnemonic objects"로 요약보다 강하게 쓴다. 데이터와 측정법이 없는 Perspective다 |

서지 정정:
- HWU20은 online 2019-11-04이고 호는 2020년이다.
- KUMAR26은 아직 권·호가 없는 early release다.
- CHU25의 쪽수는 BibTeX 7103–7121과 Crossref 7922–7940이 충돌한다(미해결).
- 우리 카탈로그의 TEM20 공식 제목은 "...Unifying Space and Relational Memory through Generalization in the Hippocampal Formation"이다.

## 3. 논문별 요지 (LITERATURE)

각 논문을 네 항목으로 정리했다: schema가 있는 곳, 학습 방식, 보인 것, 보이지 않은 것.

**SPENS24**
- **schema가 있는 곳:** VAE의 가중치와 연속 latent.
- **학습 방식:** 사건을 MHN에 한 번에 저장한다. MHN을 noise로 구동해 replay 집합을 만들고, 그 집합으로 VAE를 backprop 학습한다.
- **확장 모델:** VAE가 잘 재구성하지 못한 요소만 해마 흔적에 예외로 저장한다.
- **보인 것:** 학습할수록 latent에서 의미 정보를 해독하기 쉬워진다. boundary extension·DRM 거짓기억 같은 schema 왜곡을 정성적으로 재현한다.
- **보이지 않은 것:** 다중 seed, 연속 공고화, schema 수정, 고정 특징 대비 이득.

**HWU20**
- **schema가 있는 곳:** mPFC에서 경쟁 학습으로 이긴 뉴런 하나(이산 id)와 그것이 고르는 고정 희소 gating mask. 이산 id와 연속 가중치의 hybrid다.
- **학습 방식:** 전부 생애 내 학습이다. 해마 인덱스가 피질 가중치의 학습 목표를 고정해 준다. 새로움×친숙도가 공고화 epoch 수를 정한다.
- **보인 것:** Tse 2007 쥐 실험 양상의 정성적 재현. 새로움 신호가 있으면 같은 결과를 더 적은 총 epoch로 낸다(13,875 대 고정 1,600 epoch 조건 33,600).
- **보이지 않은 것:** 지속학습 baseline, schema 분할·병합, 큰 과제.

**CHU25**
- **schema가 있는 곳:** RNN 상태공간의 고정점 사슬(sequence attractor). 같은 구조의 시퀀스들이 하나의 추상 사슬로 수렴한다.
- **학습 방식:** 바깥 루프는 없다. 단계별 curriculum을 BPTT+Adam으로 이어서 학습한다.
- **보인 것:** 새 문제의 학습 trial이 약 710에서 455로 준다(5문제, 10 seed). shaping이 뒤집힌 보상 구간을 안정적으로 처리한다.
- **보이지 않은 것:** 코드, 망각, 구조가 바뀌는 문제, 고정 순환망 대조.

**GOUDAR23**
- **schema가 있는 곳:** 가중치가 아니라 집단 활동의 저차원 decision subspace(2.36±0.18차원, 분산 88.5%). 문제 간에 공유된다.
- **학습 방식:** trial마다 BPTT+Adam. 명시적 meta-objective는 없다.
- **보인 것:** 약 1,000개 문제를 거치며 첫 문제 수천 trial에서 마지막 약 20 trial로 준다. 지수 시간상수는 47.5±26.2문제다. subspace 재사용을 막으면 가중치 변화가 약 8–12배 커진다.
- **보이지 않은 것:** 망각 측정, 표면과 구조의 분리.
- **주의:** 입력 척도를 바꾸면 순환 가중치를 동결한 망도 완전 가소 망과 비슷해진다(Supp Note 1.1.1).

**ELDER26**
- **schema가 있는 곳:** 출력 쪽 hidden layer의 거의 이산적인 AND형 배선. 입력 쪽 연속 특징 위에 얹혀 있다.
- **학습 방식:** gradient를 쓰지 않는 층별 SVM 구성. 데이터 양을 바꿔 처음부터 다시 학습한다.
- **보인 것:** 데이터를 늘려도 출력 쪽 가중치가 일정하다. 작은 망에서는 backprop MLP보다 정확도가 높다.
- **보이지 않은 것:** 순차 학습, 새 클래스, 망각.
- **주의:** 불변성은 SVM 구성과 가중치 균등화(`equalize_weights`)에서 나왔을 가능성이 있다.

**MICONI25**
- **schema가 있는 곳:** 느린 파라미터에는 "배우는 방법"이 있다. 에피소드 안에서 쓰이는 fast weight P(t)에는 항목의 순서 기하가 있다.
- **학습 방식:** 바깥 루프는 meta-RL(A2C+BPTT)이다. 안쪽 루프는 네트워크가 스스로 만든 스칼라 neuromodulator m(t)가 연결별 가소성 계수 A와 Hebbian trace로 쓰기를 gate한다.
- **보인 것:** 두 목록을 연결쌍 하나로 이어 붙이는 list-linking. 과거 항목 표현을 재활성화해 직접 보지 않은 이웃까지 옮긴다.
- **보이지 않은 것:** 재활성화를 제거하는 인과 실험, 장기 망각, 순서 외 구조.

**TEM20**
- **schema가 있는 곳:** 느린 가중치 W_a의 action 조건 전이 규칙(구조 코드).
- **학습 방식:** 바깥 루프는 BPTT다. 안쪽 루프는 Hebbian fast memory M이다. 예측 오차 (p − p̂)에 비례해 쓰고, 환경마다 리셋한다.
- **보인 것:** 같은 구조의 새 환경에서 첫 재방문 링크를 추론한다. grid·place 세포 유사 표상과 실제 기록 데이터의 상관이 보인다.
- **보이지 않은 것:** 구조 선택·수정, 비분해 baseline, retention.

**KUMAR26**
- **schema가 있는 곳:** 모듈 묶음이다. 느린 좌표 코드, 보상으로 쓰는 빠른 cue→goal 연합, 고정 controller, WM gate로 이뤄진다.
- **학습 방식:** 생애 내 TD와 보상 변조 Hebbian. 실패한 연합은 ACh 억제로 해당 cue만 지운다.
- **보인 것:** 새 연합을 한 번 노출만으로 학습한다(chance 대비 d 2.5–5.2). 용량 곡선(12쌍 중 7.8)도 보였다.
- **보이지 않은 것:** 환경 간 구조 전이, 기존 연합의 retention.

**SWAMI23**
- **schema가 있는 곳:** CSCG의 잠재 전이 그래프 T(느림). 관측 방출 E(빠름)가 slot 역할을 한다.
- **학습 방식:** 오프라인 EM으로 구조를 배운다. prompt마다 surprise 임계값으로 확신 있게 맞은 위치(anchor)는 보호하고 틀린 위치만 다시 묶는다.
- **보인 것:** CSCG 안의 ICL. 용량에 따라 성능이 단조 증가한다(GINC 0.97, LIALT 0.89–0.93).
- **보이지 않은 것:** transformer 실험, baseline, 지속학습.

**STRUCTK25** — 구조 지식(cognitive map·schema)의 신경 기질·계산 모델·AI 응용을 분류한 서술형 리뷰다. Methods와 검색·선정 프로토콜이 없다.
- **schema 모델 분류:** 명시적(TEM, SMP, CSCG 등 11개)과 암묵적(Goudar·Driscoll의 manifold, Yang·Dubreuil의 subpopulation 등 4개)으로 나눈다(§3.2.2, Table 3). 분량은 cognitive map 쪽이 더 크다.
- **뇌 쪽 서술(§2.2, Fig. 3b):**
  - mPFC가 입력과 기존 schema의 일치도를 감지한다. 일치하면 MTL의 사례 기반 공고화를 억제하고 빠른 schema 갱신을 촉진한다.
  - 오류가 크면 새 schema를 만들고, 작으면 기존 schema를 미세 조정한다(§3.2.1에도 같은 서술).
- **지속학습(§5.2):** forgetting·효율적 적응·지식 융합을 열린 문제로 든다. 그러나 schema가 학습 규칙을 제어하는 연결은 다루지 않는다. 지속학습이 초점인 schema 모델은 SMART(Gao 2021) 한 행뿐이다(Table 4, 수치 없음).
- **주의:** 참고문헌·인용 오류 3건을 확인했다(W7 §1.3). 이 리뷰를 통한 2차 인용은 원논문을 보기 전에 단정하지 않는다.
- 상세: [W7-remediation.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/W7-remediation.md)

**SPECTRUM26** — schema를 별도 저장소가 아니라 분산 표현의 추상화 regime으로 보자는 Perspective다.
- fit에 따라 integration(변화 거의 없음), assimilation(작은 변화), accommodation(큰 변화·더 많은 계산)으로 나눈다. 정성적 규칙이며 데이터는 없다.

## 4. 논문을 가로지르는 관찰

하나의 통합 모델로 묶지 않는다. 각 논문이 보인 범위가 다르므로 공통으로 **확인되는 것과 비어 있는 것**만 적는다.

### 4.1 학습된 구조의 이득은 직접 비교되지 않았다

| 논문 | 학습 구조 대 고정·무구조 대조 |
|---|---|
| SPENS24 | 없음. 미학습 encoder 한 점(epoch 0)뿐이다 |
| HWU20 | 구조 없는 변형(mPFC 크기 1)이 비중첩 schema에서 gating 변형보다 높다(≈0.9–0.95 대 ≈0.65) |
| CHU25 | 고정 무작위 순환 + 학습 입출력 대조가 없다 |
| GOUDAR23 | 입력 척도를 조정하면 순환 동결 망이 완전 가소 망과 비슷하다 |
| ELDER26 | hidden이 크면 backprop MLP가 ENN보다 높다 |
| MICONI25 | 비가소 RNN·표준 meta-RL 대조가 없다. 단일 스칼라 가소성 소거는 실패했다 |
| TEM20 | 비분해 baseline과 learned vs given 구조 비교가 없다 |
| KUMAR26 | learned vs given 구조 비교가 없다. 플래그는 코드에만 있다 |
| SWAMI23 | LIALT baseline이 없다 |

[PROPOSAL] FCL의 모든 schema 기제 실험은 **같은 계산·갱신 예산의 고정/무구조/항상-갱신 대조**와 함께 판정한다. 이 리뷰와 Melete J1이 같은 쪽을 가리킨다.

### 4.2 "새로움·일치도가 학습을 바꾼다"는 다섯 가지 다른 기제다

| 논문 | 신호 | 신호가 정하는 것 | 학습률 자체 변화 |
|---|---|---|---|
| SPENS24 | 요소별 재구성 오차 > 고정 임계값 θ | 빠른 저장소에 무엇을 저장할지(예외 잔차) | 없음 |
| HWU20 | novelty × familiarity | 공고화 replay epoch 수 | 없음 |
| TEM20 | 예측 오차 (p − p̂) | Hebbian 쓰기 크기(암묵적) | 없음 |
| SWAMI23 | leave-one-out 조건부확률 < p_surprise | 어느 slot을 다시 묶고 어느 위치를 보호할지 | 없음 |
| MICONI25 | 네트워크가 스스로 만든 neuromodulator m(t) | 쓰기 시점·부호·크기. 연결별 계수 A | 학습된 값이다(meta-learned) |
| KUMAR26 | 보상 + 탐색 잡음, ACh 억제 | 성공 시 쓰기, 실패 시 해당 cue 삭제 | 없음 |
| SPECTRUM26 | schema fit(정성) | 변화량: integration ≈ 0, assimilation 작음, accommodation 큼 | 개념만 |
| CHU25·GOUDAR23·ELDER26 | 없음 | — | — |

[PROPOSAL] 우리 질문 "schema가 학습 규칙 자체를 제어하는가"는 이렇게 쪼개 시험할 수 있다.
- **무엇을** 쓰는가
- **어디에**(빠른 기억 대 느린 수준) 쓰는가
- **얼마나** 쓰는가
- **언제** 공고화하는가

Titans식 surprise 기반 쓰기는 이미 "얼마나"를 다룬다. 비어 있는 것은 **fit·친숙도에 따라 쓰는 위치와 공고화 예산을 바꾸는 것**이다.

### 4.3 느린 구조 + 빠른 결합 분해는 반복되지만, 구조를 실행 중에 고치는 논문은 없다

같은 분해가 여러 논문에서 반복된다. 각각 느린 쪽 / 빠른 쪽이다.
- TEM20: W / M
- SWAMI23: T / E
- MICONI25: 느린 파라미터 / P(t)
- KUMAR26: 좌표 코드 / cue→goal
- SPENS24: VAE / MHN
- HWU20: 피질 CHL / 해마 인덱스

이 분해는 System ONE의 CMS(느린 수준)·Titans(빠른 기억) 역할 분담과 잘 맞는다(PROPOSAL).

그러나 공통 한계가 있다. 느린 구조는 모두 오프라인·바깥 루프에서 배우거나 아주 느리게 다시 배운다. **불일치를 만났을 때 구조를 그 자리에서 수정·분할하는 실험은 하나도 없다.**
- KUMAR26: remap 뒤 좌표를 약 20 session 재학습한다.
- TEM20: 구조 remapping을 예측으로만 말한다.
- SWAMI23: test 시 T가 고정이다.
- SPENS24: test 시 VAE가 동결된다.

accommodation은 FCL이 직접 채워야 할 공백이다.

### 4.4 잘 측정되지 않은 것

- **보존·망각:**
  - CHU25·ELDER26은 측정이 없다. TEM20은 기억을 리셋한다. KUMAR26은 기존 쌍 보존을 보고하지 않았다.
  - GOUDAR23은 재학습 savings뿐이다. MICONI25는 장기 망각이 없다.
  - HWU20만 부분 측정이 있다.
- **표면 대 구조:**
  - 구조는 같고 표면만 다르거나, 표면은 같고 구조가 다른 lure로 분리한 논문은 없다.
  - GOUDAR23은 오히려 학습 속도가 자극 코사인 유사도에 크게 의존함을 보인다(유사도 1에서 약 7 trial, 0에서 약 175 trial).
- **계산량:**
  - 같은 품질의 추론 계산을 잰 논문이 없다. HWU20의 절감도 학습 epoch다.
  - H-COMPUTE를 받치는 문헌 근거는 개념 수준뿐이다. SPECTRUM26("accommodation은 더 많은 계산")과 SWAMI23(posterior 엔트로피·1회 EM으로 충분)이 그 정도다.

### 4.5 코드는 대부분 있지만 그대로 쓰기 어렵다

| 논문 | 공식 코드 | 라이선스 | 주의 |
|---|---|---|---|
| SPENS24 | ellie-as/generative-memory | 없음 | TF 2.11. MHN β 스케일이 논문과 다르다 |
| HWU20 | fitany/SchemaNetworkBICY | 없음 | MATLAB. Table 1 값과 코드가 다르다. VoR 일부 실험 코드가 없다 |
| CHU25 | 없음 | — | — |
| GOUDAR23 | xjwanglab/learning-2-learn | MIT | TF 1.15/Python 2.7. 배포 데이터(10망)가 논문 통계(30망)를 재현하지 않는다 |
| ELDER26 | jre411/bdENN | 없음 | 임베딩·신경 데이터가 없다. VoR보다 오래된 코드다 |
| MICONI25 | ThomasMiconi/TransitiveInference | 없음 | PyTorch. 식 4·5가 코드와 다르다 |
| TEM20 | djcrw/generalising-structural-knowledge | 없음 | TF1/TF2. lr·clip이 논문과 다르다 |
| KUMAR26 | mgkumar138/schema4one | 없음 | TF 2.12. N, τ_e, 학습률이 논문과 다르다. n=720 표본을 재현할 수 없다 |
| SWAMI23 | 없음(기반 CSCG repo는 MIT이나 논문이 링크하지 않음) | — | — |

[PROPOSAL] 라이선스 없는 코드는 읽고 인용만 한다. 필요한 기제는 **논문 식에서 다시 구현**한다. 모두 소형(수백 유닛, CPU 가능)이라 재구현 비용은 작다.

## 5. FCL 설계의 시작점 (PROPOSAL)

설계 질문(DQ) 정의:
- DQ1 schema의 위치·형태
- DQ2 형성과 선택(문맥 controller·라우팅)
- DQ3 동화 대 조절, 새로움 gating, 선택적 갱신, 수정·분할·전환
- DQ4 다중 시간척도와 Sleep/replay 공고화
- DQ5 계산 깊이 제어와 "깊은 사고 → 빠른 판단"(H-COMPUTE)
- DQ6 같은 구조 새 과제의 표본 효율(H-SAMPLE)과 표면 유사성 견고성
- DQ7 보존·망각·간섭
- DQ8 빌릴 평가 패러다임

아래는 문헌이 준 출발점이다. 구현이나 채택 결정이 아니다.

1. **DQ1 — schema를 모듈이 아니라 측정 가능한 성질로 정의한다.** 문헌은 두 정의를 모두 지지한다. 하나는 느린 구조 파라미터(TEM의 W, CSCG의 T, VAE)이고, 다른 하나는 활동 subspace·attractor regime(GOUDAR23, CHU25, SPECTRUM26)이다. retrofit LLM에서는 둘 중 하나를 고르지 않고 세 측정을 schema의 조작적 증거로 쓴다.
   - 같은 구조의 문제들에 걸친 subspace 재사용(GOUDAR23 demixing·participation ratio)
   - 새 같은-구조 과제에서의 가중치·상태 변화량 감소
   - 해당 표현을 제거·교체했을 때 구조 전이만 선택적으로 사라짐(README 핵심 질문 4)
2. **DQ3 — 첫 번째 "schema-조건부 학습" 후보는 쓰기 gate를 fit과 결합하는 것이다.**
   - 선택적 갱신 마스크는 SWAMI23의 규칙에서 출발한다. 확신 있게 맞은 위치는 보호하고, 확신 있게 틀린 위치만 빠른 기억에 쓴다.
   - 더 강한 후보는 MICONI25식 학습된 neuromodulator다. 연결별 가소성 계수가 필수라는 결과가 단서다.
   - 대조군: 항상 쓰기, surprise만, 고정 무작위 gate. 같은 쓰기 예산에서 비교한다.
3. **DQ3·DQ7 — accommodation을 직접 설계해야 한다.** 구조를 그 자리에서 고치는 문헌 기제가 없다(§4.3). 출발점은 두 가지다.
   - STRUCTK25·SPECTRUM26의 정성 규칙: 오류가 크면 새 구조, 작으면 미세 조정
   - SPENS24의 "예외만 따로 저장"
   - 실패 모드는 잘못된 구조가 조용히 내용을 묶는 것(TEM20)과 schema 과적용(SPENS24의 prototype 왜곡·DRM lure)이다.
4. **DQ4 — Sleep의 첫 형태는 빠른 저장소에서 느린 수준으로 가는 teacher–student replay다(SPENS24).**
   - 자주 반복된 rebinding을 느린 가중치로 흡수한다(SWAMI23 Discussion의 제안).
   - replay 예산을 novelty×familiarity로 배분하는 방식(HWU20)을 고정 예산과 비교한다.
   - 진단으로 SPENS24의 prototype 수축·lure 침입과 HWU20의 Tse식 probe를 빌린다.
5. **DQ6 — H-SAMPLE 평가 틀은 이미 여럿 있다.**
   - GOUDAR23·CHU25의 trial-to-criterion 곡선
   - SWAMI23 LIALT의 example형(예시 1개 + 새 토큰)
   - KUMAR26의 1회 노출 용량 곡선
   - MICONI25의 list-linking·sham 대조
   - 단 GOUDAR23이 보였듯 표면 유사도가 결과를 크게 바꾸므로, **표면과 구조를 분리한 lure**를 반드시 넣는다.
6. **DQ5 — H-COMPUTE는 문헌 지지가 가장 약한, 사실상 우리 고유 가설이다.**
   - 후보 신호: CSCG posterior 엔트로피, 기억 recall 신뢰도(KUMAR26의 0.6 임계값), attractor 수렴 탐침(CHU25).
   - 그 전에 고정 깊이의 품질–계산 곡선이 먼저다(roadmap의 기존 순서와 같다).
7. **DQ7 — 보존 평가는 우리가 만든다.** 문헌에 쓸 만한 측정이 거의 없다. ABA 조건 복귀, 이전 과제의 zero-shot 재평가, savings를 함께 쓴다.
8. **공통** — 모든 기제는 §4.1의 대조와 함께 판정하고, 문헌 코드는 식에서 재구현한다(§4.5).

## 6. 갭 주장 판정

외부 요약의 결론은 "다양한 경험에서 schema를 스스로 발견·형성·수정·통합하고, 그 schema가 이후 학습 규칙 자체를 제어하는 범용 지속학습 아키텍처는 완성된 형태로 확인되지 않았다"였다.

**검색 범위**
- 기간: 2023-01-01 ~ 2026-11-11
- 쿼리: OpenAlex 26개, arXiv API 44개, Semantic Scholar 9개, 웹 검색 5개
- 선별: 고유 레코드 1,047건을 자동 선별해 제목 265건, 초록 약 42건을 읽었다. 전문은 5건을 부분적으로 읽었다.

**판정 기준(5개):**
- (i) 다양한 경험에서 재사용 구조를 스스로 발견·형성
- (ii) 경험이 어긋날 때 그 구조를 수정·분할·병합
- (iii) 그 구조가 이후 학습 규칙(무엇·어디·얼마나·언제 갱신할지)을 제어
- (iv) 순차 다과제·다영역의 일반 지속학습 평가
- (v) 구현되고 평가된 완성 형태

**결과**
- 이 범위에서 5개를 모두 만족하는 사례는 **발견되지 않았다.**
- 가장 가까운 사례는 셋이다.
  - Shan, Minni 외, *Separating the what and how of compositional computation to enable reuse and continual learning*(arXiv 2510.20709, NeurIPS 2025): 문맥 posterior가 저랭크 RNN의 계산과 학습을 gate한다. 단 task id가 입력으로 주어지고 생성 모형 계열이 손으로 정해져 있다.
  - LCNet: latent cause로 문맥을 추론한다.
  - ALMA: 메모리 설계를 오프라인에서 탐색한다.
- 셋 모두 소규모이거나 오프라인 탐색이다.

이 결론은 검색 범위와 근거 깊이에 대한 서술이다. "갭이 존재한다"는 증명이 아니다. Nested Learning/HOPE·Titans·ATLAS 같은 재료 논문은 이 기준에서 부분만 만족했다. 다만 대부분 초록 수준 판정이다.

## 7. 다음 추적 후보 (미정독)

| 후보 | 이유 | 식별자 상태 |
|---|---|---|
| Shan, Minni 외, *Separating the what and how...*, arXiv 2510.20709 (NeurIPS 2025) | 문맥 추론이 계산과 학습을 동시에 gate. 갭에 가장 가까움 | worker가 §1–4·Discussion 정독. [catalog.tsv](/home/jimmy/repos/full-continual-learning/references/catalog.tsv) S35 |
| SMART (Gao et al., 2021) | 지속학습을 직접 다루는 schema 모델(schematic memory persistence/transience) | STRUCTK25 참고문헌에서 발견. DOI 미확인 |
| Kobayashi et al. 2025, arXiv 2512.20605 | transformer 내부 schema로 계층적 행동 제어(SPECTRUM26 ref 96) | 미확인 |
| Lanzillotta, Samiei, Precup, Pascanu 2026, arXiv 2607.05609 | "To Retain or to Adapt?" 지속학습 일반화 | 미확인 |
| Stoianov et al. 2022 | generative replay와 지속학습 | STRUCTK25 참고문헌, 미확인 |
| Spens & Burgess 2026 compressive RAG ([catalog.tsv](/home/jimmy/repos/full-continual-learning/references/catalog.tsv) S07) | SPENS24의 후속. 두 실험 계열을 섞지 않고 비교 | 기존 목록 |

## 8. 미해결

- 판본 관련 미확인 사항
  - GOUDAR23·MICONI25·KUMAR26·SPECTRUM26은 VoR 조판본이 아니라 accepted manuscript·proof·preprint를 읽었다. 편집 차이는 배제하지 못했다.
  - SPENS24의 bioRxiv 판은 접근이 막혀 VoR과 대조하지 못했다.
- 정의·불일치가 미해결인 수치
  - CHU25의 정확도 정의, 93.20의 분모, 쪽수 충돌.
  - ELDER26의 ± 정의와 978 대 888 clips.
  - KUMAR26의 본문 ± 정의.
- STRUCTK25는 동적 HTML 페이지에서 받은 텍스트다. 다시 받으면 달라질 수 있어 해시를 고정했다. 그림 이미지는 보지 않았다.
- 코드는 하나도 실행하지 않았다. 재현성 평가는 정적 읽기다.
- 그림에서 읽은 수치는 근사값이다. 상세 기록에 "(읽음)"으로 표시했다.
