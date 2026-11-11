# SPECTRUM26, STRUCTK25 — 리뷰·관점 논문

> 2026-11-11 SBL 원문 검토 워크플로에서 worker가 쓴 보고를 마스터가 원문 대조로 검수해 옮겼다. 종합은 [2026-11-11-sbl-fulltext-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext-review.md)에 있다.
>
> `fcl-sbl-fulltext-20261111/...` 경로는 저장소 밖 호스트 작업 폴더다. 원문은 저작권 때문에 저장소에 넣지 않았다. 판본과 해시는 [evidence.json](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/evidence.json)에 있다.
>
> 표기: 필드 1–10·12는 별도 표기가 없으면 원문 사실(LITERATURE, 위치 병기)이다. 일부 문장은 우리 산술·추론(PROPOSAL), 코드 독해(CODE), 그림 판독(FIGURE-READ)인데 표시가 빠져 있다. 그 목록은 [W7-remediation.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/W7-remediation.md) §2.4에 있다. 필드 11은 PROPOSAL이다.
>
> 정정: STRUCTK25 절의 WebFetch 기반 구판을 삭제하고 원문 기준 재작성본([W7-remediation.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/W7-remediation.md) §1)으로 대체했다. §0 표의 STRUCTK25 열과 §3 자체 점검의 STRUCTK25 항목은 보완 전 상태다. SPECTRUM26 유형은 PDF 머리말 Perspective, PubMed 유형 Journal Article·Review다.

---

## W5 최종 보고: SPECTRUM26 (원문 확보), STRUCTK25 (원문 정독은 W7 보완 보고 §1로 대체)

루트: `fcl-sbl-fulltext-20261111/`. 변경한 곳은 `STRUCTK25/`, `SPECTRUM26/`, `_scripts/W5/`뿐이고 git은 건드리지 않았다.

### 0. 한눈에 보기

| 항목 | STRUCTK25 | SPECTRUM26 |
|---|---|---|
| status | **partial**: 원문 파일 미확보. Springer가 curl을 JS "Client Challenge"로 차단했다. WebFetch(소형 모델이 HTML을 읽고 응답, 인용 ≤~125자)로만 읽었다. | **fulltext**: 저자 사이트에서 받은 Elsevier "Corrected proof" 10쪽 |
| 유형 | narrative taxonomic survey. systematic review 아님. | Neuron **Perspective** (PDF 머리말). PubMed 유형은 "Review", OpenAlex 유형은 review. 실험·데이터 없음. |
| 저자 확인 | Yingchao Yu, Yuping Yan(공동 제1저자), Yaochu Jin(교신) | Mandana Samiei, Doina Precup, Blake A. Richards(전원 교신) |
| 주장 판정 | SK1 **PARTIAL** | SP1 **CONFIRMED** |

- 9편 인용 여부(R2) 요약
  - STRUCTK25가 인용: HWU20(표 3과 참고문헌에만), GOUDAR23, TEM20, SWAMI23.
  - SPECTRUM26이 인용: SPENS24만.
- 두 리뷰는 서로 인용하지 않는다(R4).

---

### 1. SPECTRUM26

#### 접근 증거
- **route**: cell.com, ScienceDirect 모두 Cloudflare 403(`cf-mitigated: challenge`). PMC/Europe PMC(`inPMC N`)와 arXiv/OSF(0건)에도 사본이 없다. 저자 사이트 `mandanasmi.github.io`의 `neuron-final.pdf`를 확보했다.
- **url**: https://mandanasmi.github.io/data/Papers/Neuron/neuron-final.pdf
- **version**
  - pdfinfo Subject가 "Neuron, Corrected proof", Creator는 Elsevier다. 하단에 "Neuron 114, June 3, 2026"이 찍혀 있다.
  - PDF CreationDate는 2026-05-28이다.
  - PubMed 이력: received 2025-10-27 / revised 2026-03-13 / accepted 2026-05-08. issue 날짜는 2026-06-03.
- **vor_or_preprint = VoR**
  - 근거 1: PDF Summary가 PubMed 게재 초록과 885자 정규화 동일하다(프로그램 검사).
  - 근거 2: 쪽수 1898–1907이 PubMed와 같다.
  - cell.com에서 받은 것이 아니므로 사소한 사후 교정 가능성은 배제하지 못한다.
- **보조 파일**: `Neuron_v2.pdf`(저자 LaTeX 원고, 18쪽, 2026-03-25)는 버전 비교용이다.
- **pages 10 / words 8019** (`fulltext.txt`는 `-layout`이라 2단이 섞여 있다. 읽기용 `fulltext_reading_order.txt` 7835 words를 추가했다.)
- **읽은 절**: Summary에서 Conclusion까지, 참고문헌 1–100 전부, Fig 1–3. Fig 1과 3은 이미지까지 확인했다. Methods와 Supplement는 없다(Perspective).
- **sha256 앞 16자리**
  - `author_neuron-final.pdf` 373112c61a390835
  - `author_Neuron_v2.pdf` b8aab07c89850648
  - `fulltext.txt` bb219e03d6e1e511
  - `fulltext_author_manuscript_v2.txt` 9f2599e6e1afaea8
  - `fulltext_reading_order.txt` a97335f4a76717d8
  - `pubmed_42235490.xml` edc62febabe08fd5
  - `openalex_work.json` 4f75e9a74394b449
  - `europepmc_search.json` 4fe147a705adacea
  - 나머지는 `fcl-sbl-fulltext-20261111/SPECTRUM26/SHA256SUMS.txt`에 있다.
- **v2와 최종본 차이** (수동 비교)
  - 최종본 Summary가 더 강하다: "schemas are **not** a distinct set of mnemonic objects" (v2는 "less a distinct set").
  - v2에는 Summary 문장 2개가 더 있고, Google/DeepMind 소속이 달려 있다.
  - 최종본에는 FRQNT 사사가 추가되었고 참고문헌 서지가 정정되었다.
  - 본문 구조, Fig 1–3, 참고문헌 100개는 동일하다.

#### 필드 1–12 (쪽수는 저널 쪽. PDF 1쪽 = p.1898)
1. **서지**
   - Neuron 114(11):1898–1907, DOI 10.1016/j.neuron.2026.05.007, PMID 42235490.
   - 코드와 데이터는 없다.
   - 펀딩: NSERC, CIFAR, FRQNT.
2. **schema 정의와 위치**
   - [LITERATURE p.1898] "abstract mental structures representing prior knowledge ... that alter how we learn new information."
   - [LITERATURE] 저자 입장: schema는 별개의 기억 객체가 아니라 "conceptual tool"이다.
   - 위치는 분산 네트워크의 high-probability activation pattern 또는 attractor다(p.1900–1902). LLM에서는 "activation patterns ... map to high-probability sequences"(p.1902)다.
   - 연속(스펙트럼) 쪽이다. Fig 3(p.1903)은 Schematic–Semantic–Autobiographical–Episodic을 Abstract↔Detailed 축에 놓는다.
   - Fig 1은 slot과 placeholder 비유를 써서 3개 regime을 이산 라벨로 그린다.
   - [OPEN] "추상화 수준"의 측정법은 없다.
3. **아키텍처**
   - 자체 아키텍처는 없다. 다루는 것은 다음과 같다.
     - symbolic frames/scripts(Minsky, Schank & Abelson)
     - harmony theory와 ART
     - Drescher의 constructivist schema mechanism
     - CLS(fast hippocampus / slow neocortex)
     - Spens & Burgess generative model(fast "hippocampus"가 neocortical generative model을 teach)
     - transformer LLM(ICL = activation, fine-tuning = weights)
4. **학습 규칙** (수식 없음)
   - outer loop: LLM pretraining이 "predict high-probability words"다(p.1902).
   - within-lifetime: ICL은 "changes to internal activation vectors ... with no parameter changes"다. refs 78, 79는 ICL을 gradient descent로 해석한다(p.1901).
   - fine-tuning은 weight를 바꾸고 기존 지식을 덮어쓸 수 있다(refs 88, 89).
   - 유일한 규칙형 서술(p.1902 "Lessons", Fig 2):
     - integration은 시냅스 변화가 "almost no".
     - assimilation은 변화가 "few"이고 recall 왜곡이 생긴다.
     - accommodation은 "large updates"로 기존 패턴을 바꾸거나 새 패턴을 만든다.
5. **형성·선택·적용·개정**
   - fit 기반 3단계(p.1899, Fig 1): integration(high fit), assimilation(medium), accommodation(low). accommodation은 "requiring more time and computation"이다.
   - Fig 1 캡션: "The requirement for additional computation and learning increases from integration to accommodation."
   - LLM 대응(p.1901, 유추): integration ≈ ICL, assimilation ≈ knowledge conflict의 confirmation bias/hallucination("Arguably"), accommodation ≈ fine-tuning.
   - 신경 대응(p.1900): PFC가 integration, hippocampus/MTL과 신경조절물질이 accommodation. novelty 탐지는 신경조절물질 몫이다(p.1903).
   - schema 생성은 언급하나, merge·split과 알고리즘은 없다.
6. **지속성**
   - ICL은 activation-only다. "LLMs will not store that information permanently unless they update their parameters"(p.1901).
   - schematization은 "averaging over many unique experiences"로 추상 관계를 배우는 과정이라고 한다(p.1903). 기억을 neocortex로 옮기는 것이 아니다.
   - replay와 sleep은 참고문헌 제목 수준이다. Spens & Burgess의 generative reconstruction이 언급된다.
7. **과제·결과**
   - 없음. 실험, baseline, ablation, seed 모두 없다.
   - 근거는 기존 LLM 현상과 신경과학 문헌에서 끌어온 유추다.
8. **신경과학 대응**
   - 문헌 종합과 재해석이다. 증거 수준은 질적(qualitative)이고, 예측은 가설로만 제시된다.
   - 영역 차이는 "more abstract representations를 다루기 때문"일 수 있다고 재해석한다(p.1903).
9. **한계, 미제시**
   - 저자 진술
     - "not entirely novel"(p.1903).
     - "none of this is unique to schemas, per se"(p.1902).
     - LLM은 "something akin to schemas"(p.1901).
     - 현재 모델은 schema를 "may not use them effectively"(p.1904).
   - 미제시: 데이터, 추상화·fit 지표, 인간과 LLM schema의 정량 비교, 학습 알고리즘, 명시적 schema 모듈이 열등하다는 검증.
10. **클레임 표**

| ID | 주장 | 판정 | 위치 | 이유 |
|---|---|---|---|---|
| SP1 | schema는 별개 기억 객체가 아니라 추상화 수준의 연속 스펙트럼, 분산 표현 | **CONFIRMED** | p.1898, 1902, 1903, 1904 "continuous spectrum rather than a hard line" | 본문에 그대로 있다. 단 개념 제안이며 측정이 없다. ChatGPT 요약("필요 없이")보다 최종본이 더 강하다("not a distinct set"). |
| SP1a | integration/assimilation/accommodation ↔ ICL/knowledge conflict/fine-tuning | PARTIAL | p.1899, 1901, 1902 | 정성 유추("Arguably"). 검증이 없다. |
| SP1b | LLM이 schema를 가진다 | PARTIAL | p.1901–1902 | 완곡한 표현("akin"). |
| SP1c | schema가 이후 학습을 제어하는 메커니즘 제시 | PARTIAL | p.1902 | fit에 따른 변화량이라는 질적 규칙뿐이다. |
| SP1d | 신규 데이터로 검증 | WRONG | 전체 | 데이터가 없다(과대 해석 방지용 항목). |

11. **FCL 연결 [PROPOSAL]** (이 논문은 position paper라서 FCL 메커니즘이 작동한다는 증거가 아니다)
   - **DQ1**
     - schema를 별도 저장소가 아니라 공유 표현의 regime/subspace와 fit 통계로 정의하는 근거가 된다.
     - 실패 양상: 지칭할 대상이 없어 revise/split/switch를 걸 곳이 없다.
     - Melete의 "learned graph 부가가치 미입증"과 방향은 일치하지만 이 논문이 시험한 것은 아니다.
   - **DQ2/DQ3**
     - fit 점수로 3-regime을 가르는 context-controller를 둔다. 출력은 {activation-only, fast update, slow update}다.
     - p.1902 변화량 규칙을 selective-update gate로 쓴다.
     - 실험: always-update 대 fit-gated를 비교해 retention, 신규 task 샘플 수, mismatch 때의 왜곡률을 잰다.
     - 실패 양상: 표면은 같고 구조는 다른 입력이 integration으로 분류되어 왜곡된다(논문의 false recall에 해당).
   - **DQ4**
     - p.1903은 schematization을 multi-episode 통계 추출로 본다. Sleep은 이 관점에서 accommodation-regime 에피소드와 생성 샘플로 slow layer를 학습시키는 쪽이 맞다. 미검증이다.
   - **DQ5 (H-COMPUTE)**
     - "accommodation은 더 많은 computation"(p.1899)이 개념적 근거다.
     - halting/depth controller를 fit에 연결하면, "deep thinking → fast judgment"는 Sleep 이후 accommodation 사례가 integration으로 이동하는 현상이 된다. 논문은 이를 주장하거나 시험하지 않는다.
   - **DQ6 (H-SAMPLE)**
     - 같은 구조의 task는 integration regime이라 샘플이 적게 든다는 예측이 나온다. 경험 전후 sample-to-criterion 곡선으로 시험한다.
   - **DQ7**
     - fine-tuning 덮어쓰기(refs 88, 89)가 forgetting baseline이다.
     - p.1904는 외부 non-parametric bank보다 "rapidly wiring new synaptic connections"를 선호한다. 시퀀스 층의 test-time fast-weight 방향을 지지한다.
   - **DQ8**
     - Fig 3의 4단계를 따라 추상화 수준별 retention probe를 만든다.
     - 표면 유사와 구조 유사를 분리한 전이 probe도 만든다.
12. **재현/프로토타입**
    - 재현할 코드와 데이터가 없다.
    - [PROPOSAL] fit-gated 실험은 소형 pretrained LM + LoRA/fast-weight와 합성 same-structure task로 RTX 5070 Ti 12GB에서 가능해 보인다. toy RNN은 CPU로 된다. 실제 비용은 [OPEN].

#### R1–R4 (SPECTRUM26)
- **R1 정의와 분류축**
  - 정의는 필드 2와 같다.
  - 분류축은 4개다.
    - fit: integration/assimilation/accommodation (Fig 1)
    - 추상화: schematic↔episodic (Fig 3)
    - 계보: symbolic / connectionist / LLM
    - 기질: PFC / MTL-hippocampus / 신경조절물질
- **R2 구현 후보 (우리 목록에 없는 것)**
  - ref 96 Kobayashi et al. 2025 (arXiv 2512.20605): transformer의 내부 "schemas"로 hierarchical behavioral control(p.1904). Richards 그룹의 논문이고 DQ2/DQ5에 가장 가깝다.
  - ref 68 Anand & Precup 2023 (continual RL).
  - refs 88(Wu et al.)과 89(Biderman et al.): forgetting baseline.
  - ref 97 Kim et al. 2023(분리 메모리 모듈)과 refs 98–100(NEC, memory-augmented NN survey, RAG): 저자들이 반대하는 쪽의 대조군.
  - refs 78, 79: ICL ≈ gradient descent.
  - refs 61–65: harmony theory, ART, Drescher.
  - refs 73–75: "schema discovery"라는 이름이 붙은 LLM 연구인데 데이터 스키마 의미라 혼동하면 안 된다.
- **R3 열린 문제**
  - 명시 절이 없다.
  - 결말부(p.1904)는 neuroscience 실험이 "schema 보유"를 가정하지 말고 상세↔추상 정도를 측정하라고 제안한다.
  - AI에 대해서는 "현재 모델은 schema가 있으나 효과적으로 쓰지 못할 수 있다"고 한다.
  - continual learning에서 schema가 이후 학습 규칙을 제어한다는 구체 메커니즘은 [OPEN]이다. 있는 것은 fit→변화량 규칙(p.1902)뿐이다.
- **R4** 두 리뷰는 서로 인용하지 않는다. 자세한 내용은 STRUCTK25 R4에 있다.

---

### 2. STRUCTK25

이 절의 WebFetch 기반 구판은 삭제했다. 원문(브라우저에서 확보한 VoR HTML 본문과 표 1–5) 기준으로 다시 쓴 보고와 구판 대비 변경 목록은 W7 보완 보고 §1에 있다. 판정은 SK1 PARTIAL, SK2·SK3 NOT-FOUND로 유지됐다.

### 3. 자체 점검

`sha256sum -c`: 두 폴더 모두 전 항목 OK.
- SPECTRUM26: 18개 파일 OK. `download/` 15개와 `fulltext.txt`, `fulltext_author_manuscript_v2.txt`, `fulltext_reading_order.txt`.
- STRUCTK25: 13개 파일 OK. `download/` 11개와 `webfetch_evidence.txt`, `crossref_refs_parsed.txt`. 이 폴더에는 `fulltext.txt`가 없다.

`access.json` 고정 15개 키는 두 파일 모두 존재한다. STRUCTK25는 `pages`/`words`가 null이라 보조 키 `pages_null_reason`, `words_null_reason`을 추가했다. `attempted_routes`는 SPECTRUM26이 13개, STRUCTK25가 12개다.

산출물 링크
- `fcl-sbl-fulltext-20261111/SPECTRUM26/access.json`
- `fcl-sbl-fulltext-20261111/SPECTRUM26/extraction.json`
- `fcl-sbl-fulltext-20261111/STRUCTK25/access.json`
- `fcl-sbl-fulltext-20261111/STRUCTK25/extraction.json`

#### 불확실하거나 미해결인 것 (우선순위순)
1. **STRUCTK25 원문 파일 미확보.**
   - Springer가 curl을 차단했다.
   - 같은 Springer 주소를 curl로 다시 시도하고 Wayback 조회까지 묶은 명령 하나는 하네스 권한 분류기가 "Unauthorized Access"로 실행 전에 거부했다.
   - 이후 Springer curl 경로와 Wayback 경로는 재시도하지 않았고 우회도 하지 않았다.
   - 해결안: 마스터나 Jimmy가 PDF를 `STRUCTK25/download/`에 두면 pdftotext 추출, 해시, 인용 재검증이 가능하다. 브라우저 기반 취득을 승인해도 된다.
2. STRUCTK25의 모든 인용과 숫자는 WebFetch 소형 모델의 재서술이다(인용 ≤~125자).
   - 수치와 인용은 PDF로 재확인하기 전까지 "WebFetch 보고"로 다뤄야 한다.
   - 소형 모델이 덧붙인 "인용이 주장을 뒷받침하지 않는 듯하다"는 지적들은 검증하지 못해 채택하지 않았다.
3. HWU20은 STRUCTK25 본문 0회이고 Table 3 행과 참고문헌에만 있다. Table 5와 그림 캡션은 읽지 못했다.
4. SPECTRUM26은 cell.com이 아니라 저자 사이트의 corrected proof다. VoR 판정은 추정이다(Summary가 PubMed 초록과 동일하다는 근거).
5. SPECTRUM26 v2와 최종본은 수동 비교만 했다. 문장 단위 diff 스크립트는 잡음이 커서 결론에 쓰지 않았다. 소스는 `_scripts/W5/diff_versions.py`다.
6. SPECTRUM26 `fulltext.txt`는 `-layout`이라 2단이 섞여 있다. 읽기용으로 `fulltext_reading_order.txt`를 따로 만들었다.
7. KUMAR26, MICONI25의 정체와 날짜는 제가 독립적으로 알지 못한다. 공개된 정보로는 참고문헌 일치 여부만 확인했다.
8. 범위 밖 참고: SPECTRUM26 저자 홈페이지에 같은 그룹의 arXiv 2607.05609 "To Retain or to Adapt? Generalizing Continual Learning"(Lanzillotta, Samiei, Precup, Pascanu, 2026-07)이 있다. 읽지 않았고, 이 논문 반입이 필요하면 마스터가 결정할 사항이다.
