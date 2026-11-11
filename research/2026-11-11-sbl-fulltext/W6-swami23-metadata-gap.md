# SWAMI23, 11편 서지 대조, 갭 반증 탐색

> 2026-11-11 SBL 원문 검토 워크플로에서 worker가 쓴 보고를 마스터가 원문 대조로 검수해 옮겼다. 종합은 [2026-11-11-sbl-fulltext-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext-review.md)에 있다.
>
> `fcl-sbl-fulltext-20261111/...` 경로는 저장소 밖 호스트 작업 폴더다. 원문은 저작권 때문에 저장소에 넣지 않았다. 판본과 해시는 [evidence.json](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/evidence.json)에 있다.
>
> 표기: 필드 1–10·12는 별도 표기가 없으면 원문 사실(LITERATURE, 위치 병기)이다. 일부 문장은 우리 산술·추론(PROPOSAL), 코드 독해(CODE), 그림 판독(FIGURE-READ)인데 표시가 빠져 있다. 그 목록은 [W7-remediation.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/W7-remediation.md) §2.4에 있다. 필드 11은 PROPOSAL이다.
>
> 정정: SWAMI23의 LIALT vocabulary(676개)와 괄호값 정의(95% CI 또는 표준오차)를 반영했다. 필드 3·4·7의 위치 보완은 [W7-remediation.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/W7-remediation.md) §2.3에 있다. CHU25 쪽수는 미해결이다.

---

**W6 보고. SWAMI23 원문 검증, 11편 서지 대조, 갭 반증 탐색을 마쳤습니다.**

루트는 `fcl-sbl-fulltext-20261111/`입니다. 쓴 곳은 `SWAMI23/`, `META/`, `GAP_SEARCH/`, `GAP-*/`(5개), `code/MedCRP-CL`, `code/LCNet`, `_scripts/W6/`뿐입니다. 이메일 등 개인정보는 어떤 API에도 보내지 않았습니다.

### 1. SWAMI23 (Swaminathan et al., NeurIPS 2023, arXiv 2307.01201)

#### 접근 증거
- **fulltext.txt**: NeurIPS VoR PDF 20쪽, 10,989 단어를 `pdftotext -layout`으로 추출했습니다. 본문과 부록 A–D를 전부 읽었습니다.
- **arXiv**: v1만 존재합니다(2023-06-16 제출, 23쪽). TeX 원본 `rb.tex`를 전부 읽고 NeurIPS 본문과 문장 단위로 diff했습니다(`version_diff.txt`, 추출 텍스트는 `fulltext_arxiv_v1.txt`).
- **NeurIPS Supplemental**: PDF 6쪽을 `supp_fulltext.txt`로 읽었습니다. 2023-05-25 제출 단계의 부록입니다.
- **미확보**: OpenReview는 403 bot challenge라 우회하지 않았고 리뷰는 읽지 못했습니다. 그림은 캡션과 추출 텍스트만 봤습니다.
- **공식 코드**: arXiv, NeurIPS, supp 어디에도 링크가 없어서 clone하지 않았습니다. GitHub 검색에서도 공식 repo는 없었습니다.
  - base CSCG repo `vicariousinc/naturecomm_cscg`(MIT, archived)는 논문이 링크하지 않습니다. rebinding 구현이 들어 있는지는 확인하지 않았습니다.
- **버전 차이**: 알고리즘, 데이터셋, 숫자, 부록 표는 arXiv와 NeurIPS가 동일합니다. 문구는 이렇게 다릅니다.
  - 초록: arXiv "it uses"가 NeurIPS에서는 "ICL in CSCG uses"로 범위가 명시됩니다.
  - 서론: arXiv "similar mechanisms **will** exist ... and show how"가 NeurIPS에서는 "hypothesize how ... **could** exist"로 약해졌습니다.
  - Fig. 6C와 Discussion이 개정됐습니다. NeurIPS는 Appendix Fig. 12가 추가됐습니다.
  - arXiv TeX에서 Fig. 11이 Fig. 5와 같은 PDF 파일을 가리킵니다.
  - **Supplemental은 숫자가 다릅니다.** LIALT 평균이 instruction 0.02/0.10/0.52/0.88, example 0.01/0.15/0.49/0.93으로, 카메라레디(아래 7항)와 다릅니다. Supplemental에는 EM 없는 Algorithm 3(rapid binding)도 있습니다. 인용은 카메라레디 숫자를 써야 합니다.

#### 필드 1–12
1. **서지**: DOI 10.52202/075280-1253, pp. 28785–28804, Spotlight, proceedings hash 5bc3356e…, 공식 코드 없음.
2. **schema 정의**:
   - schema는 T(잠재 전이 그래프)이고, {T, C}는 ungrounded schema, {T, C, E}는 grounded schema입니다(§2.2).
   - 위치는 파라미터(전이 텐서)입니다. 이산 latent clone과 확률 가중치가 섞인 hybrid입니다.
   - slot은 같은 관측을 내는 clone 집합입니다.
3. **구조**:
   - CSCG는 결정적 emission을 갖는 HMM입니다.
   - GINC는 토큰당 50 clone(ablation 10)입니다.
   - LIALT는 overallocation ratio 0.1/0.3/1.0/3.0입니다.
   - LIALT vocabulary는 676개입니다(§4.2, p.6). GINC vocabulary 크기와 학습된 CSCG의 N_latent 값은 원문에 숫자가 없습니다(W7 보완 보고 §2.3).
   - test 시 T와 C는 고정이고, E의 일부 행만 학습됩니다. E가 fast, T가 slow입니다.
4. **학습 규칙**:
   - outer loop는 EM입니다. GINC는 100 full-batch iteration에 ε=1e-2, LIALT는 500 iteration과 Viterbi training 10회에 ε=1e-6입니다. BPTT와 curriculum은 없습니다.
   - within-prompt는 Algorithm 1입니다. leave-one-out 조건부확률 p(Xn=j|x\n)과 p_surprise(LIALT 0.1, dax 1/16)로 anchor와 rebinding 대상을 가르고, 해당 행만 EM으로 갱신합니다(App.A 식). 완성은 max-product MAP(Alg.2)입니다.
5. **형성/선택/수정**:
   - 형성은 offline EM입니다. 선택은 prompt에 대한 latent posterior입니다.
   - assimilation은 anchor 보호, accommodation은 E 행 rebinding입니다. surprise 임계값이 novelty gate 역할을 합니다.
   - T 수정, 생성, 병합, 분할은 test 시 없습니다. T를 rebinding하는 방안("through time")은 Discussion에서 제안만 합니다.
6. **지속성**: E^rb는 prompt별로 계산됩니다. 프롬프트 간 누적 여부와 replay/consolidation은 원문에 없습니다. [OPEN]
7. **과제와 숫자**:
   - **GINC**: 모델은 1개이고 prompt는 (k,n) 칸당 2500개입니다. 50 clone, k=10에서 0.971–0.978(괄호 0.006 = 95% CI, Appendix C Table 1), 10 clone에서 0.674–0.713(±0.018)입니다. k=3은 0.44–0.53으로 낮습니다. baseline은 Xie et al.의 곡선과 정성 비교일 뿐, 이 논문에서 재실행하지 않았습니다.
   - **LIALT**: 13개 알고리즘에 instruction 5종씩, instruction당 demonstration 20개(13×5×20=1300은 유도값)입니다. test는 instruction형과 example형 각 100 prompt입니다.
     - 1-EM, ratio 0.1/0.3/1.0/3.0: instruction형 0.00/0.20(0.08)/0.54(0.10)/0.89(0.06), example형 0.00/0.09/0.49/0.91. 괄호는 95% CI다(Table 4).
     - EM 수렴 시 ratio 3.0에서 instruction형 0.89, example형 0.93. 1-EM과 수렴 값이 거의 같습니다.
     - 신뢰구간(CI)은 prompt에 대한 이항 CI로 확인했습니다. 학습 seed 변동은 보고되지 않았고 baseline도 없습니다.
     - 과제별 SE로 역산하면 과제당 n이 약 4–11개입니다. 가장 약한 과제는 matrix roll columns(instruction 0.17(0.15), 괄호는 표준오차, Table 5)입니다.
   - **Dax**: 5개 prompt를 정성으로만 보였습니다.
   - ablation은 clone 수 변화(10 vs 50)와 overallocation sweep뿐입니다. n-gram이나 fixed-graph 대조는 없습니다. [OPEN]
8. **신경과학 대응**: cognitive map과 synaptic plasticity 인용 수준의 정성적 비유뿐입니다(데이터 적합 없음).
9. **한계와 비증명**:
   - 부록 D.4에 실패 예가 있습니다. instruction 회로가 delimiter 모호성으로 엉뚱한 알고리즘에 연결되는 경우와 schema를 잘못 학습한 경우입니다.
   - LLM/transformer 실험이 없습니다.
   - LIALT baseline, 학습 seed 분산, continual learning이 없습니다.
   - 필요성 ablation은 2개 prompt의 정성 비교(Fig. 6B)뿐입니다.
   - data 크기 효과(§3.4)는 가설일 뿐 실험이 없습니다.
   - 명시적 Limitations 절은 없습니다.
10. **claim 표**: 아래 표.
11. **FCL 연결 [PROPOSAL]**:
    - **DQ1**: schema를 slow 구조(FFN/CMS 저빈도)와 fast slot binding(Titans류 memory 또는 activation)으로 분해합니다.
    - **DQ2, DQ5**: 길이에 따른 latent posterior 엔트로피 감소(Fig. 3C)를 schema 모호성과 halting 신호로 씁니다. 1-EM과 수렴의 차이가 작다는 점은 반복 추론의 조기 종료 곡선(H-COMPUTE)의 모형입니다.
    - **DQ3**: "확신 있게 맞은 위치는 보호하고, 확신 있게 틀린 위치만 fast memory로 갱신"하는 선택적 갱신 마스크가 직접 이식 대상입니다.
    - **DQ4**: 자주 쓰이는 rebinding을 slow weights로 흡수하는 Sleep 과제를 설계합니다.
    - **DQ6, DQ8**: LIALT의 example형(예시 1개와 새 토큰)이 H-SAMPLE 평가 틀입니다. 구조가 호환되는 여러 schema(reverse/shift)의 혼동은 표면 유사도 시험이 됩니다.
    - **실패 모드**: 임계값 민감도, T 고정이라 switch/split 불가, delimiter 모호성입니다.
    - **Melete 선례**: 학습된 그래프 대 fixed/no-graph 대조가 없어, 학습 그래프의 부가가치는 입증되지 않았습니다. [OPEN]
12. **재현**:
    - 계산량과 N_latent가 보고되지 않았습니다. 식은 Algorithm 1, App.A, Algorithm 2로 충분하고, 데이터는 설명에서 재구성해야 합니다. [OPEN]
    - CPU 재구현은 가능해 보입니다. RTX 5070 Ti도 충분해 보이지만 상태 수를 몰라 확정할 수 없습니다. [PROPOSAL]

#### claim 검증표

| claim | 판정 | 위치와 이유 |
|---|---|---|
| SW1 schema template / CSCG | CONFIRMED (CSCG 한정) | §2.2, Fig. 4B/6A. 13개 군집과 학습된 reverse 회로. 군집은 시각화일 뿐 정량 지표 없음 |
| SW2-a CSCG에서 ICL = 회로 학습 + 문맥 검색 + rebinding | CONFIRMED | GINC 표 1, LIALT 표 4/7. 단 rebinding은 설계된 test-time 알고리즘이지 학습에서 창발한 성질이 아님 |
| SW2-b transformer와 동등한 ICL | PARTIAL | GINC는 Xie et al.와 정성 비교, LIALT는 baseline 없음 |
| SW2-c emergence | PARTIAL | 용량 4수준에서 단조 증가(표 5/6). 급격한 전이, seed 분산은 미검증. data 크기 효과(§3.4)는 NOT-FOUND |
| SW2-d LLM에서도 같은 기제 | NOT-FOUND (분석적 가설) | §6과 Fig. 8은 "conjecture". LLM 실험 없음, GPT는 참고문헌에만 등장 |
| 1-EM이면 충분 | CONFIRMED | 표 4 대 표 7 |
| Bayes 관점은 불충분 | PARTIAL | GINC와 LIALT 대비. 정성(Fig. 6B 첫 행) |
| dax 단발 흡수 | PARTIAL | 5개 정성 예시, 지표 없음 |

### 2. 서지 대조 (11편)

| ID | 우리 label | 공식값 | 판정 | 출처 |
|---|---|---|---|---|
| SPENS24 | Nat Hum Behav 2024, DOI …799-z, ellie-as/generative-memory | 8(3):526–543, online 2024-01-19, 호 2024-03, CC BY. bioRxiv v1(01-20)/v2(01-21)/v3(05-30). repo 존재(main, push 2025-03-26, license 없음), 논문이 링크 | match | Crossref, PubMed, Nature, GitHub |
| HWU20 | Biol Cybern 2020, DOI …808-7 | 114(2):169–186, **online 2019-11-04 / 호 2020-04**. VoR 구독형. bioRxiv v1 2018-10-04는 제목이 "…Memory Consolidation"으로 VoR "Encoding"과 다름 | match (연도 둘 병기) | Crossref, PubMed |
| CHU25 | NeurIPS 2025, hash 0a88e621… | 제목 "Shaping Sequence Attractor Schema in RNNs", poster, DOI 10.52202/085713-0243. **저자 "Bo Ho"(메타데이터) 대 "Bo Hong"(PDF 1쪽). 쪽수 7103–7121(BibTeX) 대 7922–7940(Crossref)**. 코드는 비공개(체크리스트), preprint 없음 | match + 2건 mismatch(쪽수는 미해결) | proceedings, Crossref, PDF |
| GOUDAR23 | Nat Neurosci 2023, DOI …293-9, xjwanglab/learning-2-learn | 26(5):879–890, online 2023-04-06, 호 2023-05. PMC 승인원고(2024-11-13 공개). bioRxiv v1 제목이 "Elucidating…"에서 v2에서 최종 제목으로 변경. 코드 repo는 vgoudar/learning-2-learn의 **fork**(MIT)이고 논문이 링크한 것이 바로 이것 | match | Crossref, PubMed, Nature |
| ELDER26 | J Comput Neurosci 2026, DOI …940-x, jre411/bdENN | 54(3):503–514, online 2026-06-30, 호 2026-09, CC BY-NC-ND. Crossref에 NIH grant 번호 정정 기록. bioRxiv 제목이 달라 preprint 연결은 OpenAlex만 주장. repo의 마지막 commit 2025-02-04가 제출(2025-12-05)과 수정(2026-05-26)보다 오래돼 VoR와 어긋날 수 있음 | match (repo는 stale) | Crossref, PubMed, PMC |
| MICONI25 | Miconi&Kay Nat Neurosci 2025, DOI …852-8, ThomasMiconi/TransitiveInference | 28(2):406–414, online 2025-01-15, 호 2025-02. 구독형, bioRxiv v1–v3(제목 2회 변경). repo 존재, 논문이 링크, 설명에는 "2024"로 오기 | match | Crossref, PubMed, Nature |
| TEM20 | Cell 2020, DOI …024, PMC7707106, djcrw/generalising-structural-knowledge | 183(5):1249–1263.e23, online 2020-11-11, 호 2020-11-25, CC BY. bioRxiv v1(2019-09-16)/v2(09-24). repo 존재, PMC 본문이 링크 | match | PubMed, PMC, Crossref |
| KUMAR26 | J Neurosci 2026, DOI …2026, arXiv 2106.03580, mgkumar138/schema4one | **early release, 권/호 없음**, article e1803242026. online 2026-10-26(PubMed/Crossref)이고 URL 경로는 2026/10/22. 현재 접근 제한(Crossref 라이선스 2027-04-26 시작). **arXiv v1–v5**: v1(2021-06-07)은 제목과 내용이 전혀 다름("reservoir computing model with Hebbian plasticity", 코드는 Oneshot_Reservoir), v2부터 최종 제목, v5 2026-10-20은 70쪽에 schema4one 링크 | match (버전 주의) | PubMed, arXiv v1–v5, GitHub |
| SWAMI23 | NeurIPS 2023, arXiv 2307.01201 | NeurIPS 36 main track Spotlight, pp. 28785–28804, arXiv v1만 존재 | match | proceedings, arXiv, Crossref |
| STRUCTK25 | AI Review 2025, DOI …11270-2 | 58(9), art. 264, online 2025-06-04, accepted 2025-05-12, CC BY-NC-ND. preprint 없음. **호 날짜는 Springer 접근 불가라 확인 못 함**(권 58로 2025 추정) | match (호 날짜 unverifiable) | Crossref, OpenAlex |
| SPECTRUM26 | Neuron 2026, DOI …05.007 | 114(11):1898–1907, 호 2026-06-03, Review, 구독형. received 2025-10-27, accepted 2026-05-08. **online 날짜는 publisher 페이지(403)라 독립 확인 불가**. preprint 없음 | match (online unverifiable) | PubMed, Crossref |

- **Springer Client Challenge와 ScienceDirect 403(bot wall)**은 우회하지 않았습니다(HWU20, ELDER26, STRUCTK25, TEM20, SPECTRUM26). 위 값은 Crossref, PubMed, Europe PMC, OpenAlex 교차확인입니다.
- 산출물은 `META/metadata.json`(필드별 checks 포함)과 `META/fetch_log.txt`입니다.

### 3. 갭 탐색

**범위**: 2023-01-01~2026-11-11. OpenAlex는 title/abstract boolean 26쿼리와 recency 2쪽 5건, arXiv API 44쿼리, Semantic Scholar 9쿼리(5건 HTTP 429, 1건 0 hit), WebSearch 5쿼리입니다. dedup 후 고유 레코드 1047건을 키워드 rubric으로 자동 screening했고, flag된 265건의 제목을 모두 읽었습니다. 초록은 약 42건, 전문은 5건(부분)을 읽었습니다.

**seed 존재 확인**: 아래 seed는 모두 존재를 확인했습니다. 초록만 읽은 것은 별도로 표시했습니다.
- Nested Learning/HOPE는 arXiv 2512.24695(NeurIPS 2025)입니다.
- Titans(2501.00663), ATLAS(2505.23735), SEAL(2506.10943), sparse memory finetuning(2510.15103), Transformer²(2501.06252), TTT(2407.04620), Larimar(2403.11901), MemoryLLM(2402.04624)은 초록만 읽었습니다.
- COIN 후속이나 latent-cause 기반 CL 네트워크는 직접적인 것이 없었습니다. 가장 가까운 것은 LCNet, HOLMES, what/how입니다.
- CSCG 후속 중에 schema 제어 갱신을 다룬 CL 연구는 없었습니다(초록 수준).

**후보 표**: M=met, P=partial, N=not, U=unclear. *는 초록만으로 판정한 것입니다.

| 후보 | i | ii | iii | iv | v | 깊이 |
|---|---|---|---|---|---|---|
| WHATHOW 2510.20709 (NeurIPS25) | P | P | M(협소) | P | P | 전문(§1–4, Disc.) |
| MEDCRP 2605.20297 (ICML26) | P | N | M(협소) | M(단일 영역) | M | 전문(§1–4, App.H) |
| LCNET 2312.08519 (SciRep24) | P | P | P | P | P | 전문(VoR 본문, Methods LCI) |
| ALMA 2602.07755 | P | P | P | P | M | 전문(초록, §1, §3, 한계) |
| NESTED/HOPE 2512.24695 | N | N | P | P | M | 전문 일부(§8, §9.1 + 전체 keyword scan) |
| DNH (Frontiers AI 2026) | N | M* | P* | M* | M* | 초록 |
| SCoL 2605.07076 | N | N | M* | P* | M* | 초록 |
| AutoHebb 2610.40757 | N | N | M* | P* | M* | 초록 |
| CAM 2510.05520 (NeurIPS25) | P* | P* | N* | P* | M* | 초록 |
| HOLMES 2603.19139 | M* | P* | U* | N* | P* | 초록 |
| MemCoE 2605.00702 | P* | U* | P* | P* | M* | 초록 |
| SEAL | N* | N* | M* | U* | M* | 초록 |
| sparse memory FT | N* | N* | M* | P* | M* | 초록 |
| Titans/ATLAS | N* | N* | U* | N* | M* | 초록 |
| T² / TTT / Larimar / MemoryLLM | N* | N* | P* | N~P* | M* | 초록 |
| ReasoningBank/ACE/AWM/DC | P* | P* | N* | P* | M* | 초록 |
| meta-plasticity 2306.01690 | N* | N* | M* | M* | P* | 초록 |
| ACL (Kirsch&Schmidhuber) 2312.00276 | N* | N* | P* | M* | M* | 초록 |
| fast-weight bank (Zenodo, 미심사) | N* | P* | P* | N* | P* | 초록 |

**전문 5건의 핵심 근거** (`GAP-*/access.json`의 `sections_read`에 읽은 범위가 있습니다):
- **WHATHOW**: task id가 입력으로 주어지고 hand-specified 생성모델 계열입니다. 새 context는 on-the-fly로 생기고, F와 M epoch은 구분이 안 돼 학습기가 병합합니다(Fig. 2). context posterior가 저랭크 RNN 성분의 계산과 학습을 gating합니다(Eq. 3–5). 6개 과제, 5 seed, baseline은 Adam/EWC/OWP 등입니다. 코드는 "public repository"라고만 하고 URL이 없습니다.
- **MEDCRP**: CRP와 가능도로 CLIP 텍스트 임베딩에서 task를 군집하고(K=5 대 물리 modality 4), 군집마다 LoRA를 하나씩 배정하고 EWC는 군집 내부에서만 적용합니다. 16개 순차 과제에서 Dice 73.3±1.0, forgetting 4.1±0.8입니다(±의 정의는 표 캡션에 없고, Fig. 3 음영은 4개 task 순서에 대한 std). 병합은 사후 분석일 뿐 모든 병합이 성능을 떨어뜨립니다(App. H). 새 군집 생성만 있고 재배정, 분할, 병합 기제는 Algorithm 1에 없습니다. 코드는 MIT이고 clone했습니다(`code/MedCRP-CL`, HEAD c668f14).
- **LCNET**: sticky CRP로 latent cause를 추론하고 context vector는 랜덤입니다. 공유 네트워크는 매 관측으로 갱신되므로 갱신 제어는 암묵적입니다. 소규모 모의실험 3건입니다. 코드는 MIT이고 clone했습니다(`code/LCNet`).
- **NESTED**: 전체 텍스트에서 schema/assimilation/accommodation 개념이 없습니다(1 hit는 참고문헌 제목). 레벨과 갱신 빈도는 설계 시 고정입니다. 학습률 η_t와 decay α_t는 입력으로부터 생성됩니다(Eq. 79–97). CL 평가는 Llama-3 3B/8B 기반 class-incremental(CLINC/Banking/DBpedia)과 CTNL입니다.
- **ALMA**: Meta Agent가 오프라인으로 memory 설계(DB schema 포함)를 탐색합니다. 설계는 도메인별 학습이며 저자들이 온라인 학습을 한계로 인정합니다. 4개 도메인, 3-run s.e.입니다.

**범위 한정 결론**: 검색 범위 X 안에서 (i)–(v)를 모두 met로 만족하는 사례는 **발견되지 않음(not found)**이며, (i)와 (ii)를 함께 met로 만족하는 사례도 없었습니다. (i)–(v) 전부 partial 이상인 사례는 전문 확인 3건(WHATHOW, LCNET, ALMA)입니다. 모두 소규모 RNN, 인지모형 수준 네트워크, offline text-memory 설계 탐색이라는 한계가 있습니다. 이 결론은 검색 범위와 근거 깊이에 대한 서술이며, 갭이 존재한다거나 존재하지 않는다는 주장이 아닙니다.

산출물은 `GAP_SEARCH/search_log.json`(쿼리 89건의 날짜, hit, screened, 실패 기록 포함), `screening.json`, `candidates.json`입니다.

### 4. Self-check

- **sha256sum -c**: SWAMI23 17 OK, META 150 OK, GAP_SEARCH 82 OK, GAP-WHATHOW 5 OK, GAP-MEDCRP 9 OK, GAP-LCNET 9 OK, GAP-NESTED 4 OK, GAP-ALMA 4 OK (전부 FAILED 0).
- **access.json**: 6개 모두 고정 key 15개가 있고, 목록에 적힌 파일이 디스크에 모두 존재합니다.
- **미확정/미해결**:
  1. CHU25의 쪽수 충돌과 저자 오기, SPECTRUM26의 online 날짜, STRUCTK25의 호 날짜, KUMAR26의 online 날짜(10-22 대 10-26)와 VoR의 코드 링크는 미해결입니다.
  2. ELDER26의 preprint↔VoR 연결은 OpenAlex만 주장합니다.
  3. SWAMI23의 OpenReview 리뷰는 못 읽었습니다.
  4. SWAMI23의 Fig. 2 회로가 학습된 것인지 손으로 만든 것인지, E^rb 지속 여부, 그림 시각 검증, arXiv HTML 미파싱(TeX를 사용)이 남아 있습니다.
  5. 갭 탐색은 Semantic Scholar 5건 429 실패, arXiv 구문 쿼리가 좁은 점(일부 0 hit)이 한계입니다.
  6. 갭 후보 대부분은 초록 기반 판정(*)이고, 전문 5건도 부분 정독입니다.
  7. MedCRP arXiv v1은 비교하지 않았습니다.
  8. 2026년 논문은 검색된 텍스트로만 판단했습니다.
  9. OpenAlex 무키 공유 예산이 약 670/1000 남았습니다.
  10. IO pressure hook이 명령 1건을 차단했으나 재시도로 해소되어 결과에는 영향이 없습니다.
