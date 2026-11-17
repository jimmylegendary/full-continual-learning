# 선행 연구 지형과 논문별 차별점: 2026-11-18 조사 기록의 부록 (W2b)

**상태 라벨:** 이 문서는 **조사 기록**이다. 외부 문헌의 내용은 **LITERATURE**이고 읽은 범위를 확인 수준으로 적었다(본문 정독이 아니라 arXiv 초록 페이지·서지 레지스트리·공식 페이지 수준이다). 「우리가 다르게 주장하는 것」과 「반드시 보여야 하는 대조 실험」은 **PROPOSAL**이며 [19-paper-plan.md](/home/jimmy/repos/full-continual-learning/docs/19-paper-plan.md)의 주장 Ck-n과 판정 규칙이 확정하기 전의 후보다. 이 조사로 실행한 학습·GPU·유료 API·모델 다운로드는 0회(**NOT RUN**)다. 작성: 2026-11-18.

## 한눈에 보기

**무엇을 했나.** 저장소의 참고문헌 catalog(133행)에 없는 선행 연구 약 140건을 1차 출처(arXiv 초록 페이지, DOI 레지스트리, 학회·학술지 공식 페이지)에서 열어 제목·저자·날짜·초록 요지를 확인했다. 2025–2026년 연구를 먼저 보았고 2026-10~11 preprint가 많다(심사 전이다). 그 결과를 (1) 논문별 차별점 표(PAPER-0, 0b, 1–6), (2) P0 대조군 후보, (3) 발견 benchmark와 AI 과학자 시스템, (4) 지속학습·test-time 학습 비교 대상, (5) 통찰·유추·schema 이론, (6) 투고처 후보로 정리했다.

**논문별로 차별점이 서는 곳과 이미 선행이 있는 곳(확인한 범위에서).**

| 논문 | 차별점이 설 수 있는 곳 | 이미 선행이 있어 새롭다고 쓰면 안 되는 것 |
|---|---|---|
| PAPER-0 | 구조 전이(표면/구조 2×2)·A→B→A 간섭·wrong-schema swap 인과 개입을 같은 예산 대조와 함께 한 CLI 흐름에서 끝까지 도는 것 | 비모수 군집 기억, 갱신·분기·새 schema 생성 판정 자체, 통찰·전략·개념 기억, steering vector 기억 |
| PAPER-0b | 인물 경험 stream의 시간순 투입·checkpoint 발견 곡선·대조 stream 특이성·입력 내재 수준·항목별 사후 편향 감사를 한 절차로 묶는 것 | 반사실·변환으로 암기를 막는 법칙 발견 benchmark, 진행적 정보 공개, 컷오프 이후 분할, 시간 정합 모델 |
| PAPER-1 | 같은 base에서 NP arm을 영구 대조로 둔 retrofit의 구조 전이·망각 평가 | 기억 모듈 retrofit(Titans 계열), 메모리 slot 갱신의 망각 감소 |
| PAPER-2 | 경험으로 익숙해진 구조가 같은 품질을 더 얕은 깊이로 내는지(깊이×schema 상호작용) | looped·recurrent depth, 적응형 test-time 계산 배분 |
| PAPER-3 | 쓰기·읽기·깊이를 한 모델 안의 학습 controller가 정하고 규칙형 v0·항상-쓰기와 같은 예산으로 비교 | 외부 텍스트 기억 controller, 비모수 Bayesian expert 증설 |
| PAPER-4 | 가중치 수준 Sleep의 잠복 효과, versioned schema의 외부화·재적재 호환 | sleep-time 사전 계산, 텍스트 기억의 야간 통합, 생성적 재생 |
| PAPER-5 | 더 큰·시간캡슐 base에서 학습 모듈이 같은 예산의 NP arm을 이기는지 | retrofit 증류, 기억 표현의 오프라인 학습 |
| PAPER-6 | 봉인 역사 대상에서 stream 특이적 발견 곡선(ET-4) | 시스템 수준 AI 과학자의 발견 주장, 시간캡슐 언어모델 자체 |

**이 조사가 설계에 주는 것 6가지.**

1. **P0의 새로움을 좁혀야 한다.** 2026-06~10 사이 agent 기억 연구가 비모수 군집(Bayesian Cheatsheet S52)과 갱신·대체·맥락 분기·새 schema 생성 판정과 version·provenance(MINDSET S53)까지 왔다. 「CRP식 생명주기」나 「못 찾으면 create」를 새롭다고 쓰면 안 된다. 서는 곳은 구조 전이의 인과 개입 평가와 경로 선택·Sleep·source 삭제를 한 제품에서 끝까지 도는 것이다.
2. **NP-1(잠재 artifact)은 약해질 수 있다는 증거가 이미 있다.** steering을 기억으로 쓰면 저장된 사실은 거의 쓰이지 않는다는 보고(S54)와 추상 개념에는 불변 선형 표현이 없다는 보고(S55)가 있다. PAPER-0은 NP-1이 실패하는 판(negative-result판)을 사전에 함께 준비한다.
3. **ET의 빈칸은 stream 설계다(확인한 범위에서).** 법칙·가설 발견 benchmark는 많지만 한 인물의 경험 stream을 시간순으로 넣고 checkpoint마다 발견 곡선을 얻고 대조 stream으로 특이성을 보는 설계는 보지 못했다. 가장 가까운 것은 진행적 정보 공개(S56)와 출판 이전 서지 복원(S57)이다. 「보지 못했다」는 「없다」가 아니다.
4. **누수 통제의 방향은 선행과 같다.** 시간 정합 언어모델(S58)과 오염 감사(S59, S60)가 같은 문제를 다룬다. 외부 증거가 컷오프를 지켜도 모델이 컷오프 이후 사실을 회상한다는 보고가 있어 MD-I의 「시스템 안 모든 생성·판정·검색은 시간캡슐 모델만」과 같은 방향의 근거가 된다.
5. **aha 자기보고 신호는 통찰의 증거로 쓰지 않는다.** 추론 중 aha 전환은 드물고 정확도를 거의 올리지 못한다는 분석(S61)이 [11-research-agenda.md](/home/jimmy/repos/full-continual-learning/docs/11-research-agenda.md) §4의 통찰 정의와 같은 방향이다.
6. **투고처.** ICML 2027 전체 논문 마감은 2027-01-22(공식 Dates 페이지), ICLR 2027은 2026-09-25에 이미 마감, NeurIPS는 2026년부터 Datasets and Benchmarks 트랙을 Evaluations and Datasets 트랙으로 개칭했고 2027 공지는 확인하지 못했다. 상시 접수 TMLR는 기술적 정확성 중심이다(§6).

**한계.** 본문 정독이 없다(세 편만 PDF 발췌 페이지를 일부 읽었다). 초록 요지는 열람 도구의 요약을 거쳤고 저자 보고 수치는 그대로 옮기지 않거나 「저자 보고」로 표시했다. 2026-06 이후 preprint는 심사 전이다. 목록에서 제목만 보고 열지 못한 후보는 §7에 「미확인」으로 모았다.

## 0. 읽는 법과 확인 수준

| 표기 | 뜻 |
|---|---|
| LITERATURE | 외부 문헌에 귀속되는 주장. 이 문서에서는 초록 수준이다 |
| PROPOSAL | 이 저장소의 설계 제안. 확정이 아니다 |
| OPEN | 사용자 결정이나 추가 확인이 필요하다 |
| NOT RUN | 실행하지 않았다 |

| 확인 수준(catalog status) | 이 조사에서의 뜻 |
|---|---|
| metadata-checked | arXiv 초록 페이지에서 제목·저자·v1 날짜·초록 요지를 확인했거나, DOI·도서 레지스트리 레코드에서 서지를 확인했다. 본문은 읽지 않았다 |
| official-search-checked | 검색 결과로 제목·식별자만 확인했다 |
| needs-resolution | 서지가 확정되지 않았다. url이 비어 있다 |
| 공식 페이지 확인 | 학회·학술지 공식 페이지에서 날짜·분량을 읽었다(§6, 부록 C) |

catalog status의 전문 정독 표시는 쓰지 않았다(본문을 읽지 않았다). 「확인한 범위에서 보지 못했다」는 부정 증명이 아니다. 논문 제출 전에 §1의 선행 연구를 다시 조회하는 절차를 둔다(DC-W2b-03).

## 1. 논문별 차별점 표

논문의 논지 후보는 마스터 결정 MD-B(phase별 제품과 ET 단), MD-J, MD-N을 따른다. 주장 번호 Ck-n과 판정 규칙은 [19-paper-plan.md](/home/jimmy/repos/full-continual-learning/docs/19-paper-plan.md)가 소유하므로 여기서는 쓰지 않는다. 표의 「우리가 다르게 주장하는 것」은 그 논문의 논지에서 선행 연구와 갈라지는 지점의 후보이고, 「반드시 보여야 하는 대조 실험」은 그 차별점을 보이는 데 빠지면 안 되는 대조다. 모든 대조는 같은 base 모델·같은 token·호출·저장 예산에서 돈다(MD-F). phase와 ET 단의 대응은 MD-B 표를 따른다.

### 1-1. PAPER-0 (P0(NP), ET-0 판정 · ET-1·ET-3p 탐색)

**논지 후보.** frozen 공개 가중치 LLM 위에서 gradient 학습 0회로, 조건별로 분해되고 생명주기를 가진 schema 형태의 비모수 기억이 같은 예산의 사례·검색·요약 기억보다 구조 전이·간섭·계산 경로에서 낫다(최대 등급 3, 외부 frozen LLM 대역이며 최종형이 아니다).

| 가장 가까운 선행 연구 | 그 연구가 보인 것(초록 수준) | 우리가 다르게 주장하는 것(PROPOSAL) | 반드시 보여야 하는 대조 실험 |
|---|---|---|---|
| Bayesian Cheatsheet S52 | LLM이 자기 반성으로 만든 추론 행동의 embedding을 hierarchical Dirichlet process 혼합으로 군집화하고 posterior 예측으로 검색한다. 새 행동이 충분히 새로우면(novelty 기준) component를 만들고 KL 기준으로 병합하며 Gibbs 재적합으로 재배정한다. 수학·물리 추론 세트(AIME 2025·Omni-MATH·PhysReason)에서 기존 기억 모듈보다 낫다고 보고(저자 보고). 폐기(discard) 기제는 한계로 남겼다. 코드 링크는 확인하지 못함(본문 일부 열람) | 군집이 아니라 조건(잠재 원인)별 분해와 read·update·branch·create·hold·evict 생명주기, version, source 삭제 계약. 평가는 표면/구조 2×2 전이와 A→B→A 간섭 | 같은 LLM·예산에서 (a) 군집 기억 arm (b) 생명주기 없는 평면 schema (c) 사례 검색. 구조 전이에서 우리 arm이 (b)(c)와 구분되는지. 군집 arm은 같은 계약으로 재구현해야 한다(원 구현 미확인) |
| MINDSET S53 | LLM 호출 없는 로컬 controller(손으로 맞춘 energy 목적함수)가 새 episode를 강화·대체(supersession)·맥락 분기·새 schema 생성 중에서 고른다. 원 대화 episode는 보존하고 provenance로 연결된 versioned schema를 둔다. LoCoMo 700문항과 LongMemEval(S29) knowledge-update 78문항에서 평가(본문 일부 열람) | 같은 종류의 4종 결정과 version·provenance가 구조 전이 이득과 인과 개입(wrong-schema swap)으로 평가되고 경로 선택(fast·learn·deep·hold)·Sleep·source 삭제 계약과 한 흐름에 묶인다. 생명주기 판정·version·provenance 자체가 새롭다고는 주장하지 않는다 | MINDSET식 판정(평면 저장+같은 4종 결정) arm을 두 번째 대조로 둔다. 조건이 충돌한 뒤 A→B→A 재방문 정확도, 오분기·오갱신 사례 분리 보고 |
| 통찰·전략·개념 기억 묶음: ExpeL S62, Dynamic Cheatsheet S63, ReasoningBank S64, ACE S65, ArcMemo S66 | 자연어 통찰·전략·교훈·playbook·개념 수준 추상을 누적하고 검색해 가중치 없이 개선(ReasoningBank는 실패 경험도 증류, ArcMemo는 ARC-AGI에서 개념 수준 기억) | 저장 단위가 통찰 문장이 아니라 구조 관계와 적용 조건을 가진 schema이고, 효과가 기억 때문임을 wrong-schema swap으로 인과적으로 보인다. 평가는 과제 점수가 아니라 표면은 다르고 구조가 같은 새 사례다 | 통찰 기억 arm(ExpeL·Dynamic Cheatsheet식)·개념 기억 arm(ArcMemo식)·요약 기억 arm·oracle schema(진단 상한). 저장된 추상이 오류를 재생산하는지(S67) 점검하는 anti-persistence arm |
| 잠재(activation) 기억 묶음: NPM S68, steering as memory S54, function vectors S26, task vector S69 | NPM은 대조 경험에서 증류한 steering vector로 절차 기억을 저장해 명시 지시 baseline과 비슷한 성능을 보고. 반면 steering 기억 연구는 frozen LLM 곁에 gist 키로 게이트하는 학습 없는 활성화 기억을 두고, 선택적이지만 저장된 사실은 거의 쓰이지 않고 질문과 무관한 내용만 남는다고 보고(사전 등록 연구, 2B·9B 두 모델, 본문 일부 열람). 이 연구는 기억 하나씩만 시험했고 여러 기억의 간섭은 한계로 남겼다. 추상 개념(previous·next)에는 불변 선형 표현이 없다는 보고(S55) | schema를 version이 있는 artifact로 저장·재적재·합성하고 hidden-state kNN key–value 결합 기억을 더하며, 여러 기억이 한 저장소에 있을 때의 간섭(A→B→A)을 측정한다. 실패할 수 있음을 사전에 명시하고 NP-1이 성립하지 않으면 그 사실을 보고한다(MD-O) | NP-0(텍스트) 대 NP-1(잠재) 대 kNN 단독. steering 강도 창(strength window) 스캔. 135M급 base에서 NP-1 성립 여부 |
| hidden-state kNN 기억: kNN-LM S70, Memorizing Transformers S71 | hidden-state 키로 과거 문맥·key-value를 검색해 추가 학습 없이(또는 비미분 기억으로) LM을 개선 | 검색 단위가 token 문맥이 아니라 구조 관계를 담은 schema artifact. 표면 유사에 끌리는지 2×2의 표면×구조 교차로 가른다 | kNN 단독 arm이 표면은 같고 구조가 다른 사례(lure)에서 어떻게 실패하는지 |
| 검색·그래프 기억 묶음: HippoRAG 2 S72, A-MEM S73, Mem0 S74, MemGPT S75 | 그래프·Zettelkasten식 연결·추출-통합-검색 기억이 RAG보다 사실·연상 기억 과제에서 낫다고 보고(비모수 지속학습을 표방) | 사실 회상이 아니라 구조 전이와 간섭·삭제 평가. 예산 일치(token·호출·저장) | dense RAG arm, 그래프 기억 arm. LongMemEval(S29)·MemoryAgentBench(S30)류 회상 지표는 보조로만 쓴다 |

**차별점이 약해지는 조건.** (i) MINDSET식 평면 판정 arm이 구조 전이에서 우리 arm과 비슷하면 생명주기·분해의 효용 주장은 서지 못한다. (ii) NP-1이 steering 기억처럼 저장물을 쓰지 못하면 잠재 artifact 주장은 negative로 낸다. (iii) 군집 arm을 원 구현이 아닌 재구현으로 돌리므로 그 차이를 한계로 적는다.

### 1-2. PAPER-0b (ET 절차·benchmark 논문, 선택)

**논지 후보.** 경험 조건부 발견 시험(ET)의 운영 정의(입력 tier A/B/C, 대조 stream, 발견 곡선, 누수·사후 편향 감사), ET-0·1 benchmark, 공개 시간캡슐 모델 위 ET-3p 절차 실행. 발견 여부는 주장하지 않고 절차·채점·누수 감사가 끝까지 도는지를 보인다(탐색, 등급 2 이하).

| 가장 가까운 선행 연구 | 그 연구가 보인 것(초록 수준) | 우리가 다르게 주장하는 것(PROPOSAL) | 반드시 보여야 하는 대조 실험 |
|---|---|---|---|
| Einstein test 제안과 공개 시간캡슐 모델 | 「W2c 조사 기록」이 소유한다. 여기서는 재서술하지 않는다. 공개된 실행 절차(protocol)가 없다는 비판은 보도 기준이었으나, W2c가 학술 의견 글(CACM, 2026-05)이 절차 골격을 제시하고 기술 사양은 일부러 비웠다는 것을 직접 확인했다([et-targets-research.md](/home/jimmy/repos/full-continual-learning/research/2026-11-18-blueprint-et-design/et-targets-research.md) §5). 이 조사에서 직접 연 것은 1913년 컷오프 7B급 모델(TypewriterLM)의 arXiv 초록 페이지뿐이다 | 개념 시험을 실행 가능한 운영 정의로 만든다(입력 tier·대조 stream·곡선·감사) | W2c가 확인한 시간캡슐 모델의 컷오프 누수 probe 결과를 인용한다 |
| NewtonBench S76, LLM-SRBench S77 | 반사실 법칙 이동(NewtonBench)과 친숙한 방정식의 비친숙 변환·합성 문제(LLM-SRBench)로 암기를 억제. 최상위 방법도 기호 정확도가 낮다고 보고 | ET-1 재분장은 역사 원형의 구조를 보존하고 이름·상수·표면을 바꾸며 오염 probe를 붙인다. 평가 단위가 단발 문제 해결이 아니라 경험 stream의 누적 효과(용량–반응)다 | 같은 모델의 기억 없음·평면 기억 arm, 원 사례를 알아보는지 재는 오염 probe, 변환 기반 재분장과의 비교(선택) |
| SciGame S78, SciLaws-Bench S79 | 문헌에서 원형·반사실 환경 쌍을 만들고 prior-only 프로토콜로 사전 지식과 증거를 가름. 컷오프 이후 논문의 temporal collection. 발표된 방정식의 구조 변형(parallel world)으로 회상을 차단하고 적합도가 곧 타당성은 아니라고 보고 | ET-2(컷오프 이후 실제 사례)와 같은 방향이지만 입력이 환경 질의가 아니라 인물 stream이고 시간순 checkpoint로 곡선을 얻는다 | prior-only와 같은 「입력 stream 없음」 arm, 적합도가 아닌 예측 기반 하위 과제 |
| ProjectionBench S56, Reconstruction S57 | 논문의 기술적 세부를 단계적으로 공개하며 가설을 평가(원 결론의 원자 주장 유사도). 출판 이전 서지만으로 아이디어를 복원하고 시간 인용 컷오프·익명 참조 ID·고정 서지로 누출을 막음 | 가장 가까운 stream형 설계. 차이는 인물 경험의 시간순 입력, 입력 내재 수준 채점, 대조 stream 특이성, 핵심 입력 제거, 중립 probe 작성 규칙 | 정보 공개량–발견 수준 곡선(용량–반응), stream 섞기·무관 인물·핵심 입력 제거, 입력 자체의 정답 누설도 채점 |
| 재발견·가설 benchmark 묶음: FIRE-Bench S80, MOOSE-Chem S81, ResearchBench S82, IdeaForecastBench S83, HypoArena S84 | 최근 연구의 재발견, 컷오프 이후 논문 사용, 영감 검색·가설 구성·순위 분해, 이후 논문 예측, 결론 전 불확정 증거에서의 가설 집합 | 연구 질문이 주어지는 단발 과제가 아니라 stream 끝까지 발견 수준(L0–L5)의 곡선. 사료 항목의 날짜 필터와 사후 편향 감사 | 연구 질문을 직접 주는 baseline(입력은 있으나 기억 구조 없음)과 stream 투입 arm의 곡선 비교 |
| 시간 정합·오염 감사: ChronoBERT S58, 시점 정합 LM S85, 미래 기억 감사 S59, 시간 오염 측정 S60, Chronologic S86 | 각 시점에 쓸 수 있던 text만으로 학습한 모델, 컷오프 이후 사실의 회상(외부 증거가 컷오프를 지켜도), 시간 정합 모델과의 같은 항목 비교, 역사 문맥 표현 benchmark | 이 감사를 ET 절차의 필수 단계(MD-I: 누수 감사·오염 probe·현대 임베딩 금지)로 표준화한다 | 시간캡슐 모델의 컷오프 이후 회상 probe, 검색 경로가 현대 임베딩을 쓰지 않는다는 점검 |

**차별점이 약해지는 조건.** stream형 평가가 이미 있다면(목록에서 열지 못한 후보 포함, §7) 「stream 설계가 빈칸」이라는 문장을 약화해야 한다. 논문 제출 전 재조회한다.

### 1-3. PAPER-1 (P1, 소형 retrofit)

**논지 후보.** 소형 pretrained 모델(135M급 후보)에 NMM(Titans식 기억)·CMS 분기를 retrofit하고 규칙형 controller v0로 쓰는 전체 제품이, 같은 계산·쓰기 예산의 고정·무구조·항상-갱신 대조보다 구조를 공유하는 새 사례에서 표본·계산 효율이 높다(최대 등급 2, 3은 별도 안).

| 가장 가까운 선행 연구 | 그 연구가 보인 것(초록 수준) | 우리가 다르게 주장하는 것(PROPOSAL) | 반드시 보여야 하는 대조 실험 |
|---|---|---|---|
| Titans A01, Titan-Llama A04, Nested Learning A02(catalog) | test-time 기억 모듈, 기존 LLM에 외부 신경 기억을 retrofit, 중첩 학습·CMS | 검증 대상이 장기 문맥 LM이 아니라 구조를 공유하는 새 사례의 표본·계산 효율과 망각(2×2). 같은 base의 NP arm을 영구 대조로 둔다 | full·fixed·flat·always·noctl·ctx·base 7 arm과 P0의 NP arm |
| ATLAS A39, LaCT A40 | 현재·과거 token으로 기억을 최적화하는 고용량 기억, 2K–1M token 대청크 test-time training | 기억 갱신의 목적을 LM 성능이 아니라 schema 형성의 효용으로 잡고 token·experience·optimizer 시계를 구분한다 | 같은 쓰기 예산에서 갱신 단위(chunk) 변화에 따른 항상-갱신 대조 |
| Memory Layers at Scale A41, Sparse Memory Finetuning A42, 표현 drift 비교 A43 | key-value 기억층, 새 지식에 크게 활성화되는 slot만 갱신해 LoRA·full finetuning보다 망각이 작다고 보고. 기억만 갱신하면 drift가 작지만 새 과제 습득이 약하다는 보고 | 가장 가까운 「slot 갱신 대 low-rank 갱신」 비교. schema 분리(조건별)와 구조 전이 측정은 별개의 기여다 | LoRA 갱신 arm, 메모리 slot 갱신 arm, 같은 쓰기 예산 |
| test-time training: TTT layers A18(catalog), 추론 중 갱신 A44, SEAL A45, TTT-Discover E06 | 추론 중 파라미터 갱신으로 few-shot·ARC·발견을 개선. SEAL은 자기 finetuning 데이터를 생성 | 갱신 시계를 구분하고 같은 갱신 예산에서 비교한다. 모델은 소형 retrofit이다 | 항상-갱신 arm(TTT식), 고정 arm |
| low-rank 지속학습: O-LoRA A46, LoRA Learns Less A47, InfLoRA A34(catalog) | 과제별 직교 부분공간, LoRA는 덜 배우고 덜 잊음 | 사용자 해법(low rank expert의 in-place update, 못 찾으면 create)은 P1에서 NMM·CMS 형태로 구현된다 | 단일 low-rank 대 분리 expert(flat 대 structured) |
| 비모수 라우팅+모수 adapter: CaLLM A48, Latent-LoRA A49, Factorized Skill Memory A50, TILA-CT A51 | 입력을 프로토타입에 맞춰 adapter를 고르는 비모수 라우팅, GMM 기반 gradient-free 라우팅, 주소 지정 망각이 실행 망각보다 먼저 온다는 보고 | context gating을 한 모델 안 CMS 분기·controller로 학습하고 NP 라우팅을 영구 대조로 둔다 | 프로토타입 매칭 라우팅 arm 대 학습 gating, 주소 실패와 실행 실패의 분리 진단(wrong-schema swap) |

**차별점이 약해지는 조건.** 필요한 결과 등급(3)이 P1 상한(2)보다 높은 주장은 MD-P의 두 안(등급 3 조건을 채우는 작업을 P1에 더하기 / pilot 문구 논문)을 [19-paper-plan.md](/home/jimmy/repos/full-continual-learning/docs/19-paper-plan.md)가 나란히 쓴다.

### 1-4. PAPER-2 (P2, 구조 family × depth)

**논지 후보.** 경험으로 익숙해진 구조는 같은 품질을 더 얕은 깊이로 내고, 깊이–품질 곡선이 schema 가용성과 상호작용한다(H-COMPUTE의 P2판, 최대 등급 3).

| 가장 가까운 선행 연구 | 그 연구가 보인 것(초록 수준) | 우리가 다르게 주장하는 것(PROPOSAL) | 반드시 보여야 하는 대조 실험 |
|---|---|---|---|
| Looped Transformers A06, Recurrent Depth A07, MoR A09, Retrofitted Recurrence A13, Adaptive Loops and Memory A17(catalog) | 반복 깊이·적응 깊이로 추론이 좋아짐 | 깊이의 효용이 학습된 schema에 조건부라는 상호작용(깊이×schema) | 같은 FLOPs에서 고정 깊이 대 적응 깊이, schema 유무 |
| Ouro A52, Hierarchical Reasoning Model A53, Tiny Recursive Model A54 | 잠재 looping 사전학습, 작은 재귀 모델이 ARC류 과제에서 강하다는 보고(저자 주장) | 구조 family 중 재귀형을 같은 격자에서 비교하되 경험 이후의 계산 절감을 주장 | 같은 파라미터·FLOPs에서 loop 대 depth 대 폭 |
| compute-optimal test-time 계산 A55 | 프롬프트별로 test-time 계산을 적응 배분하면 파라미터 확장보다 효과적일 수 있다는 분석 | 배분 신호가 난이도 추정이 아니라 익숙함(schema 적합)이다 | 난이도 기반 배분 대 익숙함 기반 배분(같은 총 계산) |
| Coconut A56 | 마지막 hidden state를 다음 입력으로 되먹이는 연속 잠재 추론 | continuous latent 우선 원칙과 이어지는 깊이 형태 | token CoT 대 잠재 반복 |

**차별점이 약해지는 조건.** 깊이의 이득이 schema 유무와 무관하게 나오면 「깊이×schema 상호작용」은 서지 못하고 일반적인 깊이 이득 논문이 된다.

### 1-5. PAPER-3 (P3, 학습된 controller·선택적 write·accommodation)

**논지 후보.** 한 모델 안에서 학습된 controller가 규칙형 v0보다 같은 쓰기·계산 예산에서 선택적 write와 accommodation(분기·create)을 더 잘한다(최대 등급 3).

| 가장 가까운 선행 연구 | 그 연구가 보인 것(초록 수준) | 우리가 다르게 주장하는 것(PROPOSAL) | 반드시 보여야 하는 대조 실험 |
|---|---|---|---|
| Janus A57, Memory-R1 S87, MINDSET S53 | 후보 기억 갱신을 받아들일지 판정하는 plug-in, RL로 학습한 Memory Manager(add·update·delete·no-op), LLM 없는 4종 결정 controller | 외부 텍스트 기억이 아니라 모델 내부 상태(schema·CMS)의 write를 같은 모델이 학습한다(U05). 판정 대상이 구조 이득과 망각이다 | 규칙형 controller v0, 항상-쓰기, 학습 controller, 외부 텍스트 controller arm(P0 NP arm과 같은 계약) |
| OMCE S88, Self-RAG S89, MemRL S90 | 사용 방식 router(contextual bandit), 필요할 때만 검색, episodic memory에 런타임 RL | 쓰기·읽기·깊이 세 결정을 한 controller가 정한다 | 읽기만 학습 대 쓰기까지 학습 |
| CN-DPM A58, N07 latent-cause(catalog), Bayesian Cheatsheet S52 | Bayesian 비모수로 expert를 늘림, 잠재 원인 추론 | 「못 찾으면 create」의 판정(N-4)에서 학습된 판정이 CRP·우도 규칙보다 나은가 | P0의 CRP 규칙 대 학습 controller |
| GRACE A59, WISE A30(catalog), EM-LLM A60 | 이산 key-value 편집 codebook, 지식 편집, surprise 기반 episode 경계 | accommodation을 기존 schema 구조의 변경과 분기로 구분한다 | 편집식(가중치 불변) 대 구조 변경 |
| SciValidityBench S91 | 정확히 기억한 사실도 쓰기에는 무효일 수 있다는 관점의 평가 | Read 선택과 오선택(F23)을 유효성 판단과 연결 | 유효성 인지 read 대 유사도 read |

**차별점이 약해지는 조건.** 학습 controller가 규칙형 v0와 같은 예산에서 이기지 못하면 「학습 모듈은 같은 예산의 NP보다 나을 때만 필요하다」(MD-D)에 따라 negative-result판으로 낸다.

### 1-6. PAPER-4 (P4, Sleep·세션 간 경험·외부화)

**논지 후보.** 가중치 수준 Sleep 통합이 이후 성능과 저장 크기를 개선하고, 외부화된 versioned schema가 세션을 넘어 호환되며 삭제가 전파된다(ET-1 잠복 효과, ET-2).

| 가장 가까운 선행 연구 | 그 연구가 보인 것(초록 수준) | 우리가 다르게 주장하는 것(PROPOSAL) | 반드시 보여야 하는 대조 실험 |
|---|---|---|---|
| Language Models Need Sleep A03, SoMem S36(catalog), Sleep-time Compute A61 | 수면식 자기 수정·통합, 외부 근거 기반 기억 재조직, 질의 전에 컨텍스트 추론을 미리 계산해 test-time 계산 절감(저자 보고) | schema 수준 Sleep(군집·병합·추상화·재조합·자가 검사)의 효과를 이후 구조 전이와 저장 크기로 잰다 | Sleep 없음, sleep-time 사전 계산(텍스트), 같은 계산 예산 |
| DCPM S92, Hippo S93, Use and Disuse S94 | 낮에 belief 개정을 쓰고 밤에 schema·의도·교차 도메인 패턴을 유도, 같은 과제의 시도들을 비교해 재사용 결정을 추출·충돌 해소, 의도 구조 통합과 오래 안 쓴 이력의 추상화 | Sleep을 학습 모듈로 바꾸고 효용을 잠복 효과(ET-1)와 저장 크기로 잰다. 텍스트 Sleep-NP는 영구 대조 | 텍스트 Sleep-NP 대 학습 Sleep, 같은 계산 예산 |
| Deep Generative Replay A62, 수면 유사 재생 A63, S06(catalog) | 재생으로 재앙적 망각을 줄임 | 재생과 통합·재조합을 구분한다 | replay-only 대 consolidation 대 consolidation+재조합 |
| 외부화: S-LoRA A32(catalog), LoraHub A64, Text-to-LoRA A65, Cartridges A66, KV-Skill S95 | adapter·KV 아티팩트의 서빙·조합·생성·오프라인 학습 | version·호환성 계약·삭제 전파가 핵심이다 | reload 후 같은 응답, wrong-version swap, 삭제 후 효과 소멸 |

**차별점이 약해지는 조건.** Sleep의 이득이 저장된 생성물의 오류 고정(S67)으로 상쇄되면 근거 연결과 자가 검사 없이는 주장하지 않는다.

### 1-7. PAPER-5 (P5, 더 큰·시간캡슐 base retrofit, 실제 consumer; 뼈대)

**논지 후보.** 학습 모듈이 같은 예산의 NP arm보다 나을 때만 필요하다(MD-D)는 판정을 더 큰 base·시간캡슐 기반 retrofit과 실제 consumer 과제에서 확인한다(ET-3, 최대 등급 4). 실험 설계는 W5·W3·W4의 결정 대기 항목이다.

| 가장 가까운 선행 연구 | 그 연구가 보인 것(초록 수준) | 우리가 다르게 주장하는 것(PROPOSAL) | 반드시 보여야 하는 대조 실험 |
|---|---|---|---|
| Titan-Llama A04, Retrofitted Recurrence A13(catalog), Mamba in the Llama A67 | 기존 LLM에 기억·재귀·선형 RNN을 이식·증류하는 retrofit | 규모를 키워도 retrofit의 효용이 같은 예산 NP보다 큰지 | 같은 base에서 NP arm 재실행 |
| 시간캡슐 언어모델 | 「W2c 조사 기록」이 소유한다(모델 목록·지식 마감·형식은 W2c가 확인) | retrofit 대상 base로서의 가능성(hook·형식)은 W2c·W3가 확인한다 | 시간캡슐 base에서 NP 대 retrofit |
| Cartridges A66, Sparse Memory Finetuning A42 | 배포 지향 기억 표현의 오프라인 학습, 연속 학습의 망각 감소 | 외부화 포맷과 consumer 접점에서 비교 | 같은 consumer 과제의 NP 대 학습 모듈 |
| agent 기억 시스템(Mem0 S74, A-MEM S73, MemGPT S75) | 실서비스형 장기 기억 | 실제 consumer 과제에서의 대조 | LongMemEval(S29)·MemoryAgentBench(S30)류 과제에서 같은 예산 비교 |

### 1-8. PAPER-6 (P6(ET), 역사 ET 최종; 뼈대)

**논지 후보.** T0까지의 세계 지식을 가진 시간캡슐 기반에서, 한 인물의 경험 stream을 schema로 쌓고 미해결 불일치를 보존했다가 재조합·재구조화하는 시스템의 발견 곡선이 기억 없음·평면 기억·대조 stream과 구별된다(H-DISCOVER, 봉인 주력 대상, 최대 등급은 W2a·W4가 정한다). 「탐색」은 등급 2 이하로만 보고한다(MD-A).

| 가장 가까운 선행 연구 | 그 연구가 보인 것(초록 수준) | 우리가 다르게 주장하는 것(PROPOSAL) | 반드시 보여야 하는 대조 실험 |
|---|---|---|---|
| Einstein test 제안·시간캡슐 모델과 그 발견 시험 결과 | 「W2c 조사 기록」이 소유한다. GPT-1900의 평가는 저자가 인상 기반이라고 밝힌 것이며 재발견의 성패를 정량으로 판정한 결과가 아니라는 것을 W2c가 1차 출처(블로그·모델 카드)에서 확인했다 | 인물 stream·입력 tier·발견 곡선으로 시험을 운영 정의화 | 봉인 대상 전에 pilot 대상에서 개발(dev/test 분리) |
| 제한 지식 모델의 개념 발견 S96, 학습 데이터 추적 S97, 개념 재편 기하 S98 | 0의 발견 시험(소형 모델은 실패, 언어 사전학습이 필요 예시를 줄임), monofact와 발견 능력의 연관 주장, 문서 embedding 기하를 개념 재편 관측량으로 사용 | 인물 stream의 곡선과 rubric(L0–L5)으로 재구조화를 잰다 | 대조 stream(없음·섞기·같은 시기 비발견자·무관 인물·핵심 입력 제거) |
| 경쟁 설명·표현 구성: ULTRADISCOVERY S99, Contrastive Discovery S100, LAMB S101 | 표현 구성(새 개체·변수 도입)이 병목이라는 보고, 경쟁 설명 집합 위의 실험 채점, 경쟁 가설을 잠재 상태로 유지 | 긴장 원장(BF-F1)과 재구조화(BF-F4)를 stream 곡선에서 본다 | 가설 집합 유지 대 단일 가설 추적, 긴장 원장 제거 |
| AI 과학자 시스템: Kosmos E07, Co-Scientist E08, AI Scientist-v2 E09, Station E10 | 시스템 수준의 자율 발견·재발견 주장(검증은 대부분 저자 보고, 독립 재현은 확인하지 못함) | 판정 대상이 일반 발견 능력이 아니라 봉인 역사 대상의 발견 곡선 | 같은 시간캡슐 기반의 기억 없음·평면 기억 arm |
| Illusion of Insight S61 | aha 전환은 드물고 정확도를 거의 올리지 못한다는 분석 | 자기보고 신호가 아니라 rubric과 객관 하위 과제로 채점한다 | 맹검 채점자·일치도, 입력 내재 수준(되풀이 대 초월) 대조 |

## 2. frozen LLM 위의 기억·경험 학습 방법 (P0 대조군 후보)

MD-F의 대조군(기억 없음, 전체 이력 long-context, dense RAG, 요약 기억, 통찰·전략 기억 계열, 개념 기억 계열, 생명주기 없는 평면 schema, controller 없음, Sleep 없음, wrong-schema swap, oracle schema)에 대응하는 문헌 후보다. 최종 구성은 [18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md)가 정한다. 방법 이름은 위에서 확인한 것만 썼다. 모두 가중치를 갱신하지 않는 방법이거나 그렇지 않으면 표에 따로 적었다.

| 계열 | 확인한 방법 | 저장 대상과 갱신 | P0 대조 arm 후보(MD-F 대응) | 주의 |
|---|---|---|---|---|
| 기억 없음 / 전체 이력 long-context | 방법 이름 없음(기준선). 평가 문헌은 LongMemEval S29, MemoryAgentBench S30(catalog) | 없음 / 이력 전체를 컨텍스트에 넣음 | 「기억 없음」「전체 이력 long-context」 | long-context는 컨텍스트 한계와 비용을 함께 보고한다 |
| dense RAG·검색 기억 | Generative Agents S102, MemGPT S75, Mem0 S74, A-MEM S73, HippoRAG 2 S72 | 자연어 경험·기억 노트를 embedding으로 검색, 일부는 연결·갱신(A-MEM)과 graph(HippoRAG 2) | 「dense RAG」 | ET-3 이상에서는 현대 embedding이 누수 경로다(MD-I). 시간캡슐 모델의 hidden state나 어휘 기반 검색을 쓴다 |
| 요약 기억 | RAPTOR S103, MemGPT의 요약 계층 | 재귀적 요약 트리, 추상 수준별 검색 | 「요약 기억」 | 요약은 생성물이므로 관측 증거와 분리한다(F20·F21) |
| 통찰·전략 기억 | ExpeL S62, Reflexion S104, Dynamic Cheatsheet S63, ReasoningBank S64, ACE S65, Agent Workflow Memory S105, Buffer of Thoughts S106, Voyager S107, Hippo S93, STRATA S108 | 통찰·교훈·playbook·workflow·사고 템플릿·skill 코드를 누적하고 검색. 일부는 병합·충돌 해소·pruning | 「통찰·전략 기억 계열」 | 저장된 추상이 오류를 재생산한다는 보고(S67)가 있어 anti-persistence arm을 대조로 둔다. S37(catalog)은 기억이 성능을 떨어뜨리는 경우를 다룬다 |
| 개념 기억 | ArcMemo S66, SCALE S109, Mental Model Management S110, Bayesian Cheatsheet S52 | 개념 수준 추상, 개념 가설의 계층 표현, mental model 덩어리와 연산자, 추론 행동의 비모수 군집 | 「개념 기억 계열」 | 개념 기억과 우리 schema의 차이는 조건별 분해·생명주기·구조 전이 평가다(§1-1) |
| 생명주기·갱신 판정 기억 | MINDSET S53, Janus A57, Memory-R1 S87, Memory as Belief S111, SciValidityBench S91 | 강화·대체·분기·생성, 갱신 수용 여부, add·update·delete·no-op, 기억 가치의 belief, 유효성 판단 | 「생명주기 없는 평면 schema」의 대조(이들의 단순화) | MINDSET의 4종 결정과 versioned schema가 CRUD·version과 가장 가깝다(본문 일부 열람). 우리 생명주기의 새로움 주장은 이 선행을 인용해 좁힌다 |
| 잠재(activation) 기억 | function vectors S26(catalog), task vector S69, in-context vector S112, activation addition S113, NPM S68, KV-Skill S95, Cartridges A66(학습 필요) | steering·task vector, 외부 operator, 오프라인 학습한 KV cache | NP-1 arm | 한계 증거: steering 기억은 저장된 사실을 거의 쓰지 못함(S54), 추상 개념의 불변 표현 없음(S55), 잠재 task 표현은 생산적 규칙에서만 ICL을 대체(S114). task vector의 성분 분해(S115)와 형성 조건(S116)은 NP-1 진단 도구 후보다 |
| kNN 기억 | kNN-LM S70, Memorizing Transformers S71, EM-LLM A60, GRACE A59 | hidden-state key를 가진 비미분 key-value 기억, surprise 기반 episode, 이산 편집 codebook | NP-1의 hidden-state kNN 결합 기억 | EM-LLM·GRACE는 시간캡슐 모델에 hook을 걸 수 있는 형식인지 W3가 확인한다 |
| Sleep·오프라인 정리 | Sleep-time Compute A61, DCPM S92, Hippo S93, Use and Disuse S94, A03·S36(catalog) | 질의 전 사전 계산, 야간 schema 유도, 시도 비교와 병합, 오래 안 쓴 이력의 추상화 | 「Sleep 없음」 대 Sleep-NP | Sleep-NP의 재조합 후보는 생성물이다. 관측과 섞지 않는다 |
| controller·선택적 사용 | Self-RAG S89, OMCE S88, MemRL S90, Routed Continual Learning A68 | 필요할 때만 검색, 사용 방식 router, 런타임 RL, 학습 방식과 상태 군집 라우팅 | 「controller 없음(항상 fast·항상 deep)」 | 규칙형 controller와 학습형 controller는 PAPER-0과 PAPER-3에서 갈린다 |
| 평가·위험 | Memory-Centric Continual Learning S117, 기억 survey S118, Continual AutoResearch E11 | 기억은 검색 품질이 아니라 미래 행동 개선으로 평가, 지속 상태가 효율은 올리나 최종 해를 항상 올리지는 않음 | 지표 설계 참고 | 「경험을 보유」와 「경험을 잘 사용」은 별개라는 보고는 P0의 지표 분리(저장 대 사용)와 맞는다 |

**대조군 구현 출처.** 초록 페이지에서 코드 링크를 확인한 방법: Dynamic Cheatsheet, ReasoningBank, ArcMemo, Buffer of Thoughts, HippoRAG 2, A-MEM(평가·시스템 저장소 둘), MemRL, Sleep-time Compute, GRACE, KV-Skill. 확인하지 못한 방법: Bayesian Cheatsheet, MINDSET, NPM, Janus, OMCE. 코드 링크 확인은 재현 가능성이나 라이선스 확인이 아니다(전수 미확인). 같은 base·같은 예산 대조를 위해 같은 계약(interface)으로 재구현하는 안과 원 구현을 외부 앵커로 쓰는 안은 DC-W2b-01이다.

## 3. 발견 benchmark와 AI 과학자 시스템

각 항목이 무엇을 재는지, 지식 마감·오염을 어떻게 다루는지, 우리 ET와의 차이를 적었다. ET의 정의와 rubric은 [17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md)가 소유한다. 「차이」 칸은 이 조사에서 확인한 범위의 비교이며 「없다」의 증명이 아니다.

### 3-1. 역사 재발견 전통과 고전 발견 시스템

| 이름 | 재는 것·한 것 | 지식 마감·오염 통제 | 우리 ET와의 차이 |
|---|---|---|---|
| BACON 계열: Scientific Discovery S119 | 측정 데이터에서 정량 법칙을 재발견하는 발견 프로그램(내용은 검색 결과 수준) | 해당 없음(데이터에서 규칙을 탐색하는 프로그램) | 데이터 규칙 탐색이다. 인물 경험 stream과 개념 도입은 다루지 않는다 |
| 문헌 기반 발견 S120 | 서로 인용하지 않는 두 문헌을 이어 가설을 도출(어유와 레이노 증후군 사례) | 해당 없음(문헌 연결 방법) | 문헌 연결 가설이다. 인물의 사고 stream과 수준 rubric은 없다 |
| AI Feynman S121, SRBench S122 | symbolic regression으로 방정식 재발견, 14+7개 방법을 252개 문제에서 비교 | 해당 없음(LLM 이전 방법) | 모델이 닫힌 꼴 방정식을 찾는다. ET는 원리의 수정·개념 도입을 본다 |

### 3-2. 방정식·법칙 발견 benchmark

| 이름 | 재는 것 | 지식 마감·오염 통제 | 우리 ET와의 차이 |
|---|---|---|---|
| LLM-SR E12, LLM-SRBench S77 | 방정식을 프로그램으로 보고 LLM+진화 탐색, 239문제(LSR-Transform·LSR-Synth) | 비친숙 변환·합성 문제로 암기 억제 | ET-0·1이 같은 방향(재분장·합성)을 쓰되 평가가 stream 누적 효과 |
| NewtonBench S76 | 12개 물리 영역 324 과제, 시뮬레이션을 능동 탐색해 법칙 발견 | 반사실 법칙 이동으로 암기 억제 | 환경 질의형이고 기억 구조 비교는 없다 |
| SciLaws-Bench S79, SciGame S78 | 6개 학문 118문제(parallel world), 원형·반사실 환경 쌍, prior-only 프로토콜 | 반사실·구조 변형, 컷오프 이후 논문 | prior-only가 우리 「입력 stream 없음」 대조와 같다 |
| LongChang S123 | 법칙이 바뀐 세계에서 이상 현상을 알아채고 새 법칙을 찾는지(질문 없이) | 바뀐 물리로 회상 차단 | 이상 현상 인식은 발견 수준 L1(긴장 인식)과 같은 지점. 우리는 stream과 곡선이 다르다 |
| Unsatz S124, ClosureBench S125, ExplorationBench S126 | 모델 구조를 직접 선택(미관측 실험 예측으로 채점), 증거 충실도·mechanism 통찰·실험 효과 채점, 알려진 사실과 충돌하는 세계의 탐색 | 시뮬레이션·낯선 세계 | 채점 축(증거 충실도·예측)은 우리 객관 하위 과제로 빌릴 수 있다 |

### 3-3. 가설·아이디어 생성과 재발견

| 이름 | 재는 것 | 지식 마감·오염 통제 | 우리 ET와의 차이 |
|---|---|---|---|
| MOOSE-Chem S81, ResearchBench S82 | 영감 검색·가설 구성·순위 분해, 화학 논문 51편 | 2024년 이후 논문 사용 | 입력은 논문 묶음이고 인물 stream·checkpoint 곡선이 없다 |
| ProjectionBench S56, Reconstruction S57 | 정보를 단계적으로 공개하며 가설 평가, 출판 이전 서지로 아이디어 복원 | 시간 인용 컷오프·익명 ID·고정 서지 | 우리 설계와 가장 가깝다. 대조 stream·입력 내재 수준·핵심 입력 제거가 없다 |
| HypoArena S84, IdeaForecastBench S83, 예측 한계 S127 | 결론 전 불확정 증거에서 가설 집합 생성(988 사례), 생성한 아이디어를 이후 논문과 대조, 추론이 예측으로 이어지지 않음 | 이후 논문·rolling episode | 예측은 L4(새 예측 도출)와 연결된다 |
| MechHypoBench S128, AgentIdeaBench S129, Si 등 S130, BrainBench S131 | mechanism 가설 생성, 아이디어 평가(독창성 불변), 100명 이상 인간 평가, 신경과학 결과 예측 | 시기별 분할 또는 인간 평가 | 채점자 설계(맹검·일치도) 참고 |
| Contrastive Discovery S100 | 가설 대 부정이 아니라 상호 배타적 경쟁 설명 집합 위에서 실험 채점 | 시뮬레이션 | 긴장 원장(BF-F1)의 경쟁 설명 보존과 같은 방향 |
| FIRE-Bench S80, OpenFrontiers S132 | 최근 연구의 재발견(연구 질문만 제시), Lean 4로 채점하는 수학 재발견(closed-book·frozen-retrieval·live-web) | FIRE-Bench는 최근 고영향 연구를 쓰지만 컷오프 처리는 초록에서 확인하지 못함. OpenFrontiers는 접근 조건(closed-book 등)으로 구분 | 질문이 주어지는 과제다. closed-book 조건이 우리 시간캡슐 설정과 닮았다 |

### 3-4. 환경·데이터 기반 발견

| 이름 | 재는 것 | 지식 마감·오염 통제 | 우리 ET와의 차이 |
|---|---|---|---|
| DiscoveryWorld S133 | 텍스트 가상 환경 120개 과제, 과제 완료·관련 행동·발견한 설명 지식 | 합성 환경 | 설명 지식 채점은 rubric 설계 참고 |
| DiscoveryBench S134, ScienceAgentBench S135, 과학 발견 평가 S136 | 데이터셋에서 가설 탐색·검증, 논문 기반 데이터 과제를 Python 프로그램으로, 시나리오 기반 프로젝트 성과 | 실제 논문 과제 | 데이터 분석 능력이 중심이다 |
| BoxingGym S137, Station E10 | 실험 설계와 모델 발견, 개방형 다중 agent 환경에서 ICLR 구두 논문 기준 재발견 | BoxingGym은 합성 환경, Station은 논문 기준 사후 채점 | 시스템 수준 비교(저자 보고 수준) |

### 3-5. 지식 마감 이후 분할과 시간 정합

| 이름 | 하는 것 | 우리 ET와의 관계 |
|---|---|---|
| LiveCodeBench S138, LiveBench S139 | 컷오프 이후 공개된 문제를 계속 수집해 오염을 줄임 | ET-2(컷오프 이후 실제 사례)의 설계 선례 |
| ChronoBERT S58, 시점 정합 LM S85 | 각 날짜에 쓸 수 있던 text만으로 학습해 lookahead bias를 피함(금융 사례) | 시간캡슐 기반(ET-3·4)의 원리와 같다 |
| 미래 기억 감사 S59, 시간 오염 측정 S60, Chronologic S86 | 외부 증거가 컷오프를 지켜도 컷오프 이후 사실을 회상, 시간 정합 모델과 같은 항목 비교, 1831–1930 문맥 표현 평가 | 누수 감사·오염 probe 절차의 직접 선행 |
| 컷오프 이후 분할을 쓰는 발견 평가 | MOOSE-Chem(2024년 1월 이후), ResearchBench(2024년 이후), SciGame의 temporal collection | ET-2의 분할 선례 |

### 3-6. AI 과학자 시스템과 발견 지향 학습

| 이름 | 한 것(초록 수준, 저자 보고) | 우리와의 차이 |
|---|---|---|
| AI Scientist-v2 E09, Agent Laboratory E13 | 가설·실험·논문 작성을 잇는 agent, 3편 중 1편이 workshop 심사 기준을 넘었다는 주장 | 우리 판정 대상은 논문 생산이 아니라 발견 수준 곡선 |
| Co-Scientist E08, Kosmos E07 | 가설 생성·비판·진화, 자율 데이터 기반 연구(보고서 진술 79.4% 정확은 독립 평가의 저자 보고) | 독립 재현은 확인하지 못했다 |
| TTT-Discover E06, DiscoveryRSI E14, Continual AutoResearch E11 | 단일 문제 RL로 가중치 갱신, 가치 있는 가설의 정의와 재귀 자기 개선, 지속 상태의 효과 | 가중치 갱신이 있다. P0는 가중치 학습 0회의 NP 대조 |
| AlphaEvolve E01(catalog) | 코드 진화 탐색 | 이미 catalog에 있다 |

### 3-7. 통찰·발견 분석

| 이름 | 한 것 | 우리와의 관계 |
|---|---|---|
| Illusion of Insight S61 | 1M+ 추론 trace에서 aha 전환은 드물고 정확도를 거의 올리지 못함 | aha 자기보고 신호를 통찰 증거로 쓰지 않는다 |
| 0의 발견 S96, monofact S97 | 제한 지식 모델이 개념(0)을 발견하는지, 학습에서 한 번 본 사실과 발견 능력의 연관 | 제한 지식 설정의 선례 |
| 개념 재편 기하 S98, ULTRADISCOVERY S99 | 문서 embedding 기하로 개념 재편 측정, 표현 구성(새 개체·변수 도입)이 병목 | 재구조화(BF-F4) 지표 후보 |

### 3-8. 종합: 빌릴 것과 ET가 메우려는 틈

| 빌릴 설계 | 어디서 | ET에서의 자리 |
|---|---|---|
| 반사실·구조 변형·변환 | NewtonBench, LLM-SRBench, SciLaws-Bench | ET-1 재분장의 점검 대조 |
| prior-only 프로토콜 | SciGame | 「입력 stream 없음」 대조 stream |
| 진행적 정보 공개, 출판 이전 서지 | ProjectionBench, Reconstruction | checkpoint probe와 누수 통제 |
| 시간 정합 모델과 오염 감사 | ChronoBERT, 미래 기억 감사 | MD-I 누수 감사 |
| 증거 충실도·mechanism 통찰·예측 채점 | ClosureBench, DiscoveryWorld, Unsatz | rubric과 객관 하위 과제 |
| 경쟁 설명 집합 | Contrastive Discovery | 긴장 원장 |

확인한 범위에서 위 문헌들이 함께 다루지 않은 조합은 (a) 인물 경험 stream의 시간순 투입과 checkpoint 곡선, (b) 대조 stream의 특이성 검사, (c) 입력 내재 수준을 이용한 되풀이와 초월의 구분, (d) 항목별 날짜·누설도 사후 편향 감사의 표준 절차다. 이것은 「새롭다」의 주장이 아니라 「이 조사에서 함께 보지 못했다」는 기록이다.

## 4. 지속학습·모듈·low-rank expert·test-time 학습·기억 구조 (P1–P4 비교 대상)

catalog에 없는 최근 것만 새로 넣었다. 이미 있는 이웃은 catalog ID로 가리킨다(A01 Titans, A02 Nested Learning, A03 Language Models Need Sleep, A04 Titan-Llama, A06–A09·A13–A17 재귀·깊이, A18 TTT layers, A20·A21 LoRA 지속학습, A26–A29 지속학습 고전, A30 WISE, A31 test-time memorization, A32 S-LoRA, A33·A34 prompt·InfLoRA, A38 BYOE, N07·S04 latent cause).

| 계열 | 확인한 방법(catalog에 없는 것) | 보인 것(초록 수준) | 비교가 필요한 논문 | catalog의 이웃 |
|---|---|---|---|---|
| test-time 기억·학습 | ATLAS A39, LaCT A40, 추론 중 갱신 A44, SEAL A45, TTT-Discover E06 | 현재·과거 token에 대한 기억 최적화, 대청크 갱신, few-shot 적응, 자기 finetuning 데이터 생성(가중치 갱신), 단일 문제 RL | PAPER-1 | A01·A02·A04·A18·A31 |
| 메모리 층·slot 갱신 | Memory Layers at Scale A41, Sparse Memory Finetuning A42, 표현 drift 비교 A43 | 추가 FLOPs 없는 key-value 층, 활성화가 큰 slot만 갱신해 망각 감소, 기억만 갱신하면 drift는 작지만 습득이 약함 | PAPER-1, 3 | A30 |
| 편집·codebook | GRACE A59, EM-LLM A60 | 이산 key-value 편집, surprise 기반 episode | PAPER-3 | A30 |
| low-rank expert·지속학습 | O-LoRA A46, LoRA Learns Less A47, LoraHub A64, Text-to-LoRA A65 | 직교 부분공간, LoRA는 덜 배우고 덜 잊음, adapter 조합과 생성 | PAPER-1, 4 | A20·A21·A26–A29·A32–A34·A38 |
| 비모수 라우팅 | CaLLM A48, Latent-LoRA A49, Factorized Skill Memory A50, TILA-CT A51, Routed Continual Learning A68 | 프로토타입·GMM 기반 gradient-free adapter 선택, 주소 지정 망각과 실행 망각의 분리, 기억 자체가 라우팅 키 | PAPER-1, 3 | N07·S04 |
| 베이즈 비모수 expert | CN-DPM A58, Bayesian Cheatsheet S52 | Dirichlet process로 expert·군집을 늘림 | PAPER-0, 3 | N07·S04 |
| 재생·Sleep | Deep Generative Replay A62, 수면 유사 재생 A63, Sleep-time Compute A61 | 생성 재생, 수면 유사 재생 단계, 질의 전 사전 계산 | PAPER-4 | A03·S06·S36·R07 |
| 깊이·재귀·test-time 계산 | Ouro A52, Hierarchical Reasoning Model A53, Tiny Recursive Model A54, 계산 최적 배분 A55, Coconut A56 | 잠재 looping, 소형 재귀 모델, 적응 배분, 연속 잠재 추론 | PAPER-2 | A06–A09·A13–A17 |
| retrofit | Mamba in the Llama A67 | 기존 LLM을 혼합 모델로 증류 | PAPER-5 | A04·A13 |

**읽은 범위 밖.** 2026년 상반기~가을의 지속학습 LoRA·MoE 논문이 많다(§7의 미확인 목록). P1–P4 논문을 쓸 때 비교 대상 선정 전에 다시 조회한다.

## 5. 통찰·유추·schema 이론 (논문 주장에 직접 쓰이는 것)

catalog에는 N17(structure-mapping 요약 페이지), N19(전문가·초보자의 물리 문제 범주화), N23(memory schema 정의), N32(schema 간 연결과 새로움의 출현), S14·S24(LLM의 schema와 binding)가 이미 있다. 아래는 catalog에 없는 것이다.

| 개념·이론 | 출처와 확인 수준 | 논문 주장에서의 쓰임 | 주의 |
|---|---|---|---|
| structure-mapping 1차 논문 | Gentner 1983 N33 (서지만 확인, N17의 이론) | PAPER-0의 표면/구조 2×2: 구조 대응으로 전이하는가 | N17과 같은 이론이다. catalog N17을 보강하는 1차 출처로 둔다 |
| 표면 대 구조 유사성 | Gentner·Rattermann·Forbus 1993 N34 (서지만 확인) | 검색은 표면 유사에, 추론 건전성은 구조에 좌우된다는 구분. 사례 검색 기억이 표면 lure에 끌리는지 예측 | 초록을 읽지 않았다. 구분의 정확한 표현은 원문 확인 필요 |
| schema 유도와 유추 전이 | Gick·Holyoak 1983 N35 (서지만 확인) | 사례 수(k=1·3·10)에 따른 schema 형성과 전이의 인지과학 선행 | 초록 미확인 |
| representational change | Knoblich 등 1999 N36 (서지만 확인) | 통찰을 제약 완화·덩어리 분해로 보는 이론. 발견 수준 L2(재구성 가설)의 근거 | [11-research-agenda.md](/home/jimmy/repos/full-continual-learning/docs/11-research-agenda.md) §4의 통찰 정의와 맞춘다. 인간 문제 해결 연구를 모델 신호로 직접 옮기지 않는다 |
| 통찰의 신경과학 | Kounios·Beeman 2014 N37 (서지만 확인) | 통찰의 측정·상관에 대한 리뷰. rubric 설계의 배경 | 초록 미확인 |
| 인큐베이션 | Sio·Ormerod 2009 N38 (서지만 확인) | Sleep·잠복 효과(PAPER-4, ET-1)의 인간 선행 | 효과 방향과 크기는 메타분석 초록을 읽지 않아 미확인 |
| 이상–위기–혁명 | Kuhn 1962 N39 (서지 미확인) | 긴장 원장(BF-F1)의 과학철학적 배경 | catalog status는 needs-resolution이다 |
| LLM의 유추 | Webb 등 S140, 반사실 유추 S141, 개념 vector의 한계 S55, 유추 probing S142, ARCANA S143, 과학 해 생성 S144 | 유추 능력이 반사실에서 약하다는 반복 보고 | ET-1 재분장에 오염 probe가 필요한 이유, NP-1 개념 vector의 한계 근거 |
| 잠재 개념 추론으로서의 ICL | Xie 등 S145, N07(catalog) | schema를 잠재 개념으로 보는 설명의 문헌 지지 | 분해된 schema의 지속학습이 망각을 줄인다는 USER-HYPOTHESIS를 직접 검증한 문헌은 이 조사에서 확인하지 못했다 |
| 통찰 신호의 한계 | Illusion of Insight S61 | aha 자기보고는 통찰의 증거가 아니다 | 의미 있는 전환은 rubric과 객관 하위 과제로 채점 |
| 개념 재편·표현 구성 | 개념 재편 기하 S98, ULTRADISCOVERY S99 | 재구조화(BF-F4) 지표 후보 | 지표의 타당성은 미검증 |

**사용자 가설(schema로 LLM과 System ONE을 함께 설명)의 문헌 지지 수준.** 이 조사에서 확인한 것은 (i) LLM의 ICL을 잠재 개념 추론으로 설명하는 이론(S145), (ii) task vector·function vector가 과제 정보를 담는다는 보고, (iii) 그 vector가 입력 변화에 불변이 아니며 추상 개념에는 불변 선형 표현이 없다는 반론(S55)이다. 「schema가 분리되지 않고 엉켜 학습되어 간섭이 재앙적 망각을 낳는다」는 가설을 직접 시험한 문헌은 보지 못했다. 이 가설은 USER-HYPOTHESIS로 남고 논문별 증거 수준은 [19-paper-plan.md](/home/jimmy/repos/full-continual-learning/docs/19-paper-plan.md)가 정한다.

## 6. 투고처 후보

공식 페이지에서 직접 읽은 것만 확정 칸에 적었다. 「분량」은 공식 지침에서 읽은 범위다. 마감은 변동될 수 있으므로 제출 계획 시점에 다시 확인한다.

| 후보 | 성격 | 마감·주기(2026-11-18 열람) | 분량·형식 | 확인 수준 | 적합도 메모(결정은 W5·사용자) |
|---|---|---|---|---|---|
| ICML 2027 | 기계학습 연 1회 학회(상위) | 초록 2027-01-14, 전체 논문 2027-01-22(AoE), 1단계 탈락 통지 02-23, 최종 결정 05-03. 본회의 2027-08-02~04 | 2027 지침은 Dates 페이지에 없음(미확인). ICML 2026 지침은 본문 8쪽, 참고문헌·부록 무제한, 이중 맹검 | 공식 Dates 페이지, ICML 2026 공식 지침 | PAPER-0은 구현 전이어서 이 마감에 맞추기 어렵다(추정). 이후 phase 논문의 후보 |
| ICLR 2027 | 표현학습 연 1회 학회(상위) | 초록 2026-09-18, 전체 2026-09-25(AoE). 이미 마감 | 본문 9쪽(제출)·10쪽(rebuttal·camera-ready), 이중 맹검, 저자당 20편 상한, 상호 심사 의무, AI 사용 진술 | 공식 Author Guidelines | 다음 회차(2028) 공지는 확인하지 못함 |
| NeurIPS(본 트랙과 Evaluations and Datasets 트랙) | 연 1회 학회. Datasets and Benchmarks 트랙이 2026년에 Evaluations and Datasets 트랙으로 개칭되었다(개칭 사실은 검색 결과에 보인 공식 블로그 글 제목 기준이며 그 글은 열지 않았다) | 2026 회차는 초록 05-04, 전체 05-06, 통지 09-24(AoE). 2027 회차 공지는 확인하지 못함 | E&D 트랙: 이중 맹검 기본, Croissant 파일과 호스팅된 데이터 필수, 평가를 그 자체의 과학적 연구 대상으로 규정. 분량은 해당 페이지에 없음 | 공식 Dates·CFP 페이지(2026) | PAPER-0b(ET 절차·benchmark)의 성격에 가장 가깝다. 2027 회차 공지 후 재확인 |
| ACL Rolling Review → ACL 2027 | NLP 계열. 상시 심사 주기 후 학회에 commit | 10주 주기, 연 5회 안팎. 게시된 일정은 2026-10-12 주기까지(NAACL 2027·COLING 2027 연결). ACL 2027은 2027년 1월로만 표기(일자 없음) | 분량은 ARR 페이지에 없음(미확인) | 공식 ARR 일정 페이지 | LLM 기억·평가 논문 후보. 일자는 공지 후 확인 |
| TMLR | 저널형, 상시 접수 | 상시. 결정 목표 약 9주(보장 아님) | 분량 제한 없음(본문 12쪽 초과 시 심사 기간 연장), 이중 맹검, 평가는 주장의 기술적 정확성 중심(FAQ 요약 수준) | 공식 Author Guide·FAQ | negative-result판과 긴 평가 논문에 친화적일 수 있다 |
| COLM 2027, CoLLAs 2027, CogSci 2027 | 언어모델·평생 학습 agent·인지과학 학회 | 공식 호출문을 찾지 못함(미확인). 보조 목록 기준 추정: COLM 2027 마감 2027-03경, CogSci 2027은 2027-07 빌바오 개최(호출문 미게시), CoLLAs 2026은 2026-04에 마감했다 | 미확인 | 보조 목록만 | CoLLAs는 지속학습 주제와 맞고 CogSci는 통찰·schema 주제와 맞을 수 있다(미확인) |
| Nature Machine Intelligence | 학술지 | 미확인(투고 안내 페이지가 인증 리다이렉트로 열리지 않음) | 미확인 | 미확인 | PAPER-6 후보로 거론할 수 있으나 확인 전에는 쓰지 않는다 |

## 7. 한계·미확인·사용자 확인 대기

**읽은 범위.** 모든 항목은 arXiv 초록 페이지 또는 서지 레지스트리 수준이다. 본문의 수치·방법 세부·부록은 읽지 않았다. 초록 요지는 열람 도구의 요약을 거쳤으므로 인용 전에 원문으로 대조한다.

**목록에서 제목만 본 후보(미확인).** 아래는 검색 목록에서 제목만 보았고 열지 못했다. 이름만 적는다.

| 후보(arXiv ID, 목록 제목) | 관련 논문 | 상태 |
|---|---|---|
| 2610.16297 SLDBench v2: Active Scaling Law Discovery | PAPER-0b | 미확인 |
| 2606.04751 FALSIFYBENCH: Evaluating Inductive Reasoning in LLMs with Rule Discovery Games | PAPER-0b | 미확인 |
| 2610.08312 CoDe-LoRA, 2605.20247 CP-MoE, 2604.16171 JumpLoRA, 2606.07500 Sparse Subspace-to-Expert Sharing | PAPER-1 | 미확인 |
| 2605.13162 Continual Fine-Tuning of Large Language Models via Program Memory, 2610.15677 Knowledge Interaction in Hypernetwork-based Continual Learning, 2609.39367 A Dynamical Theory of LoRA in Continual Learning | PAPER-1, 4 | 미확인 |
| 2602.01992 Emergent Analogical Reasoning in Transformers | PAPER-0 | 미확인 |
| 2609.33244 ActiveMem, 2610.41056 Accept Changes, Reject Attacks, 2610.01415 Beyond Memory, 2610.35089 Learning to Remember | PAPER-0, 3 | 미확인 |

**접근하지 못한 1차 출처.** 학술지 페이지 3곳(Project MUSE는 검증 챌린지, 출판사 페이지는 403, PubMed는 쿠키 안내 페이지만 열림)은 서지를 DOI 레지스트리(Crossref)와 도서 레지스트리(Open Library)로 대신 확인했다. 한 건의 레지스트리 조회는 호출 제한(429)에 걸려 간격을 두고 다시 조회했다. Nature Machine Intelligence 투고 안내는 인증 리다이렉트로 열지 못했다.

**어긋남과 정정(근거와 함께 보고).**

| 항목 | 작업 지시의 배경 메모(2차 출처) | 조사 결과 | 조치 |
|---|---|---|---|
| TypewriterLM의 제목 | TypewriterLM(arXiv 2606.02991)을 「Pretraining Language Models on Historical Text」로 서술 | arXiv 초록 페이지의 제목은 「A Language Model from 1913: Pretraining on Historical Text」이고 EMNLP 2026 채택 표기가 있으며 7.24B·1913 컷오프로 표시됨 | W2c가 같은 제목을 확인했고 통합 때 반영했다. 이 문서는 모델 이름만 쓴다 |
| 1840 컷오프 고전 중국어 모델 | 배경 메모의 시간캡슐 목록에 없음 | arXiv 2610.16201의 초록 페이지가 983M급 모델과 컷오프 탐침을 서술하고 모델 공개는 「예정」으로 표시됨(공개물 없음) | W2c 참고용. 이 문서는 인용하지 않았다 |
| Kuhn 1962 | 도서 레지스트리의 첫 출판 연도가 판본별로 다르게 표시됨 | 검색 결과는 1962 초판(University of Chicago Press)을 표시 | catalog에서는 needs-resolution으로 둔다 |

**사용자 결정 후보(가칭, 번호는 W7·W4가 붙인다).**

| 가칭 | 결정 | 선택지 | 추천 | 비용 발생 | 결정자 |
|---|---|---|---|---|---|
| DC-W2b-01 | P0 대조군의 구현 출처 | (a) 같은 계약(interface)으로 모두 재구현 (b) 코드가 확인된 방법은 원 구현을 외부 앵커로 1–2개 병행 (c) 원 구현만 | (a)를 기본으로 하고 (b)를 선택. 같은 예산 대조가 쉽다 | 개발 시간(W3·W6가 추정) | 사용자 |
| DC-W2b-02 | 외부 발견 benchmark 앵커 | NP arm을 공개 benchmark(예: NewtonBench·LLM-SRBench)에서 한 번 돌려 ET-0의 외부 타당도 증거를 만들지 | P0 말미에 1개. 공개 데이터 접근·라이선스 확인 뒤 | 계산 소량(W6가 추정) | 사용자 |
| DC-W2b-03 | 심사 전 preprint 의존 정책 | 제출 4주 전에 §1의 가장 가까운 선행 연구를 재조회하는 gate를 둘지 | 둔다 | 없음 | 사용자 |
| DC-W2b-04 | PAPER-0b의 투고 성격 | 평가·데이터 트랙형(예: NeurIPS의 Evaluations and Datasets) / 저널형(TMLR) / 일반 ML 본 트랙 | 2027 회차 공지 뒤 평가·데이터 트랙형을 우선 검토 | 없음 | 사용자 |

**다음 행동.** W5는 §1의 표를 [19-paper-plan.md](/home/jimmy/repos/full-continual-learning/docs/19-paper-plan.md)의 「선행 연구와 차별점」으로 가져가고 주장 Ck-n과 판정 규칙을 붙인다. W3는 §2의 대조군 후보와 구현 출처 정보를 [18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md)의 대조군 구성에 쓴다. W2a는 §3-8의 빌릴 설계 목록을 [17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md)의 누수·대조 stream 절과 맞춘다.

## 부록 A. 색인

### A-1. 소유 정의 위치

| 소유 정의(작업 분담표 기준) | 위치(절 번호와 제목) |
|---|---|
| 선행 연구 지형과 논문별 차별점 표 | §1 논문별 차별점 표(§1-1 PAPER-0 ~ §1-8 PAPER-6) |

### A-2. 이 초안이 정의한 ID

| 종류 | ID | 내용 |
|---|---|---|
| 사용자 결정 후보(가칭) | DC-W2b-01 ~ DC-W2b-04 | §7. P0 대조군 구현 출처, 외부 발견 benchmark 앵커, 심사 전 preprint 재조회 gate, PAPER-0b 투고 성격 |
| 새 참고문헌(가칭) | NEW-W2b-001 ~ NEW-W2b-140 | 부록 B. 번호가 99를 넘어 3자리로 썼다(접두 충돌을 피하려고 전부 3자리로 맞춤) |
| 새 평가 family | 없음 | 이 초안은 새 family를 제안하지 않는다 |
| 표 이름 | §1-1 ~ §1-8, §3-1 ~ §3-8 | 차별점 표와 발견 benchmark 표 |

### A-3. 남의 정의를 가리킨 곳

| 가리킨 정의 | 소유 | 이 초안에서 쓴 곳 |
|---|---|---|
| 마스터 결정 MD-A·B(ET 단, phase와 ET 단의 대응) | 마스터 결정(MD-1118-A~P) | §1 머리말과 §1-1~§1-8 논지 후보 |
| MD-C·D·F·O(P0 정의·한계·대조군·대역 원칙) | 마스터 결정, 상세는 docs/18 | §1-1, §2 |
| MD-G·I·N(ET 원칙·누수 통제·발견 수준 척도) | docs/17 | §1-2, §3-8, §5 |
| MD-P와 결과 등급(docs/09 §3) | docs/09 | §1-3 |
| 통찰의 운영적 정의(docs/11 §4) | docs/11 | 한눈에 보기 5, §5 |
| CRUD와 「못 찾으면 create」(docs/14, 결정 대기 N-4) | docs/14 | §1-1, §1-5 |
| Einstein test 출처·시간캡슐 모델·대상 후보 | W2c 조사 기록 | §1-2, §1-7, §1-8 |
| H-SAMPLE·H-COMPUTE(docs/01 §4)와 H-DISCOVER(MD-N) | docs/01, MD-N | §1-4, §1-8 |
| F20·F21·F23(docs/08) | docs/08 | §2, §1-5 |

### A-4. 가칭 목록

| 가칭 | 요약 |
|---|---|
| DC-W2b-01 | P0 대조군의 구현 출처(재구현 기본 / 원 구현 앵커 병행) |
| DC-W2b-02 | 외부 발견 benchmark에서 NP arm을 한 번 돌려 외부 타당도 앵커를 만들지 |
| DC-W2b-03 | 제출 4주 전 가장 가까운 선행 연구를 재조회하는 gate |
| DC-W2b-04 | PAPER-0b의 투고 성격(평가·데이터 트랙형 / 저널형 / 일반 ML) |
| NEW-W2b-001 ~ NEW-W2b-140 | 부록 B의 새 참고문헌 140건 |

### A-5. §1 표에서 직접 인용한 새 참고문헌(catalog 우선 반영 후보)

S52, S53, S54, S55, S56, S57, S58, S59, S60, S61, S62, S63, S64, S65, S66, S67, S68, S69, S70, S71, S72, S73, S74, S75, S76, S77, S78, S79, S80, S81, S82, S83, S84, S85, S86, A39, A40, A41, A42, A43, A44, A45, E06, A46, A47, A48, A49, A50, A51, A52, A53, A54, A55, A56, A57, S87, S88, S89, S90, A58, A59, A60, S91, A61, S92, S93, S94, A62, A63, A64, A65, A66, S95, A67, S96, S97, S98, S99, S100, S101, E07, E08, E09, E10 (총 84건)

### A-6. catalog 접두 제안(W7 참고, 새 접두는 만들지 않는다)

| 부록 B category | 접두 제안 | 근거 |
|---|---|---|
| evaluation | S | 기존 평가 행(S29·S30·S41)이 S에 있다 |
| adjacent-mechanism(agent 기억류) | S | 기존 agent 기억 행(S36–S42)이 S에 있다 |
| adjacent-mechanism(모델 구조·지속학습·TTT·깊이) | A | 기존 구조·지속학습 행이 A에 있다 |
| neural-continuous(steering·task vector) | S | function vector S26이 S에 있다 |
| evolution | E | 자동 연구·진화 행이 E에 있다 |
| neuroscience(인지과학 고전) | N | 기존 인지 행이 N에 있다 |
| symbolic | S | 기존 symbolic 행이 S에 있다 |

### A-7. 남의 초안에서 본 불일치

이 단계에서는 다른 워커의 초안을 읽지 않았다. 작업 지시와 조사 결과의 어긋남은 §7의 표에 적었다.

## 부록 B. 새 참고문헌

[catalog.tsv](/home/jimmy/repos/full-continual-learning/references/catalog.tsv)의 8열 형식이다(id, title, category, date_note, url, code_url, status, note). id는 통합 때 catalog의 최종 번호로 바꿨고 괄호에 가칭을 남겼다. 모든 행은 본문 정독 표시가 아닌 status 값을 쓴다. url이 빈 행은 needs-resolution이다. catalog의 기존 133행과 arXiv ID로 대조해 중복이 없음을 확인했다.

| id | title | category | date_note | url | code_url | status | note |
|---|---|---|---|---|---|---|---|
| S52 (가칭 NEW-W2b-001) | Test-Time Adaptation of Reasoning Strategies with Bayesian Nonparametric Memory | adjacent-mechanism | 2026-10-05 v1 | https://arxiv.org/abs/2610.06516 |  | metadata-checked | Bayesian Cheatsheet: hierarchical Dirichlet process 혼합으로 추론 행동을 군집화하고 posterior 예측으로 검색. 수학·물리 추론 세트에서 기존 기억 모듈보다 낫다고 보고. 초록과 본문 발췌 페이지(방법·실험·한계 일부) 확인, 전문 미정독 (첫 저자 Ramji) |
| S53 (가칭 NEW-W2b-002) | MINDSET: Energy-based Memory Evolution for Long Conversational Agents | adjacent-mechanism | 2026-10-06 v1 | https://arxiv.org/abs/2610.08586 |  | metadata-checked | MINDSET: LLM 없는 로컬 controller가 새 episode를 강화·대체·맥락 분기·새 schema 생성 중에서 고른다. LoCoMo·LongMemEval 지표. 초록과 본문 발췌 페이지(방법·실험·한계 일부) 확인, 전문 미정독 (첫 저자 Dutta) |
| S54 (가칭 NEW-W2b-003) | What Survives When Activation Steering Is Used as Memory | neural-continuous | 2026-10-10 v1 | https://arxiv.org/abs/2610.14958 | https://github.com/vedant-jumle/Seahorse | metadata-checked | steering vector를 기억으로 쓸 때 무엇이 남는가: 선택성은 높으나 저장된 사실은 거의 쓰이지 않고 질문과 무관한 내용만 남는다는 보고. 초록과 본문 발췌 페이지(방법·실험·한계 일부) 확인, 전문 미정독 (첫 저자 Jumle) |
| S55 (가칭 NEW-W2b-004) | Analogical Reasoning Inside Large Language Models: Concept Vectors and the Limits of Abstraction | neural-continuous | 2025-03-05 v1 | https://arxiv.org/abs/2503.03666 |  | metadata-checked | LLM 활성화의 function vector는 입력 변화에 불변이 아니며 일부 개념은 불변 head가 있으나 previous·next 같은 추상 개념은 불변 선형 표현이 없다고 보고. 초록 페이지만 확인, 본문 미정독 (첫 저자 Opielka) |
| S56 (가칭 NEW-W2b-005) | ProjectionBench: Evaluating Scientific Hypothesis Generation in LLMs Under Progressive Information Disclosure | evaluation | 2026-05-28 v1 | https://arxiv.org/abs/2605.30284 |  | metadata-checked | ProjectionBench: 논문의 기술적 세부를 단계적으로 공개하며 가설을 생성시키고 원 결론의 원자 주장과의 의미 유사도로 채점. 초록 페이지만 확인, 본문 미정독 (첫 저자 Lew) |
| S57 (가칭 NEW-W2b-006) | Reconstruction: A Blind Benchmark for Recovering Research Ideas from Pre-Publication Bibliographies | evaluation | 2026-08-17 v1 | https://arxiv.org/abs/2608.16645 |  | metadata-checked | Reconstruction: 출판 이전 서지만으로 연구 아이디어를 복원하는 blind benchmark. 시간 인용 컷오프·익명 참조 ID·고정 서지로 누출을 막는다. 초록 페이지만 확인, 본문 미정독 (첫 저자 Chen) |
| S58 (가칭 NEW-W2b-007) | Chronologically Consistent Large Language Models | evaluation | 2025-02-28 v1 | https://arxiv.org/abs/2502.21206 |  | metadata-checked | ChronoBERT·ChronoGPT: 각 시점에 쓸 수 있던 text만으로 학습해 lookahead bias를 피하는 시간 정합 언어모델(금융 사례). 초록 페이지만 확인, 본문 미정독 (첫 저자 He) |
| S59 (가칭 NEW-W2b-008) | Auditing Future-Memory Use in Point-in-Time Language Agents | evaluation | 2026-10-13 v1 | https://arxiv.org/abs/2610.18602 |  | metadata-checked | Point-in-time agent가 외부 증거는 컷오프를 지켜도 컷오프 이후 사실을 회상한다는 감사 보고. 기억 접근·검색 배분·최종 출력을 따로 감사하라고 제안. 초록 페이지만 확인, 본문 미정독 (첫 저자 Ye) |
| S60 (가칭 NEW-W2b-009) | Reading or Remembering? Measuring Temporal Contamination in Language Models | evaluation | 2026-11-16 v1 | https://arxiv.org/abs/2611.21554 |  | metadata-checked | 시간 오염 측정: 모델이 읽는 중인지 기억하는 중인지 구분하려면 시간 정합 모델과 같은 항목으로 비교하라고 제안. 초록 페이지만 확인, 본문 미정독 (첫 저자 Arunkumar V) |
| S61 (가칭 NEW-W2b-010) | The Illusion of Insight in Reasoning Models | evaluation | 2026-01-02 v1 | https://arxiv.org/abs/2601.00514 |  | metadata-checked | Illusion of Insight: 추론 중 aha 전환은 드물고 학습으로 늘지 않으며 정확도를 거의 올리지 못한다는 분석(1M+ trace). 초록 페이지만 확인, 본문 미정독 (첫 저자 d'Aliberti) |
| S62 (가칭 NEW-W2b-011) | ExpeL: LLM Agents Are Experiential Learners | adjacent-mechanism | 2023-08-20 v1; AAAI 2024 (per arXiv) | https://arxiv.org/abs/2308.10144 |  | metadata-checked | ExpeL: 훈련 과제에서 자연어 통찰을 추출하고 추론 때 통찰과 경험을 회상. 가중치 갱신 없음(AAAI 2024 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Zhao) |
| S63 (가칭 NEW-W2b-012) | Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory | adjacent-mechanism | 2025-04-10 v1 | https://arxiv.org/abs/2504.07952 | https://github.com/suzgunmirac/dynamic-cheatsheet | metadata-checked | Dynamic Cheatsheet: black-box LM에 전략·통찰을 누적하는 지속 기억을 주어 추론 중 학습. 초록 페이지만 확인, 본문 미정독 (첫 저자 Suzgun) |
| S64 (가칭 NEW-W2b-013) | ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory | adjacent-mechanism | 2025-09-29 v1; ICLR 2026 (per arXiv) | https://arxiv.org/abs/2509.25140 | https://github.com/google-research/reasoning-bank | metadata-checked | ReasoningBank: 성공과 실패 경험에서 재사용 가능한 추론 교훈을 증류하고 memory-aware test-time scaling을 더함(ICLR 2026 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Ouyang) |
| S65 (가칭 NEW-W2b-014) | Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models | adjacent-mechanism | 2025-10-06 v1; ICLR 2026 (per arXiv) | https://arxiv.org/abs/2510.04618 |  | metadata-checked | ACE(Agentic Context Engineering): 컨텍스트를 생성·반성·큐레이션으로 진화하는 playbook으로 취급(ICLR 2026 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Zhang) |
| S66 (가칭 NEW-W2b-015) | ArcMemo: Abstract Reasoning Composition with Lifelong LLM Memory | adjacent-mechanism | 2025-09-04 v1 | https://arxiv.org/abs/2509.04439 | https://github.com/matt-seb-ho/arc_memo | metadata-checked | ArcMemo: 풀이 trace에서 증류한 재사용 가능한 개념 수준 기억. ARC-AGI에서 기억 없음 대비 상대 7.5% 향상(저자 보고). 초록 페이지만 확인, 본문 미정독 (첫 저자 Ho) |
| S67 (가칭 NEW-W2b-016) | More Memory, Worse Agents: Error Reproduction and Anti-Persistence in LLM Agents | adjacent-mechanism | 2026-10-19 v1 | https://arxiv.org/abs/2610.27406 |  | metadata-checked | 저장된 추상이 오류를 스스로 재생산한다는 분석과 Anti-Persistence(지침을 필요할 때 재구성하고 쓴 뒤 폐기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Wang) |
| S68 (가칭 NEW-W2b-017) | Neural Procedural Memory: Empowering LLM Agents with Implicit Activation Steering | neural-continuous | 2026-06-29 v1 | https://arxiv.org/abs/2606.29824 |  | metadata-checked | Neural Procedural Memory: 절차 기억을 대조 경험에서 증류한 steering vector로 저장하는 훈련 불필요 방법. 초록 페이지만 확인, 본문 미정독 (첫 저자 Zhao) |
| S69 (가칭 NEW-W2b-018) | In-Context Learning Creates Task Vectors | neural-continuous | 2023-10-24 v1; Findings of EMNLP 2023 (per arXiv) | https://arxiv.org/abs/2310.15916 |  | metadata-checked | ICL이 학습 집합을 하나의 task vector로 압축한다는 관점(EMNLP 2023 Findings 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Hendel) |
| S70 (가칭 NEW-W2b-019) | Generalization through Memorization: Nearest Neighbor Language Models | adjacent-mechanism | 2019-11-01 v1; ICLR 2020 (per arXiv) | https://arxiv.org/abs/1911.00172 |  | metadata-checked | kNN-LM: 사전학습 LM과 hidden-state 키 기반 kNN 모델을 보간해 추가 학습 없이 개선(ICLR 2020 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Khandelwal) |
| S71 (가칭 NEW-W2b-020) | Memorizing Transformers | adjacent-mechanism | 2022-03-16 v1; ICLR 2022 spotlight (per arXiv) | https://arxiv.org/abs/2203.08913 |  | metadata-checked | Memorizing Transformers: 과거 key-value의 비미분 기억에 근사 kNN 검색을 붙인 attention(ICLR 2022 spotlight 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Wu) |
| S72 (가칭 NEW-W2b-021) | From RAG to Memory: Non-Parametric Continual Learning for Large Language Models (HippoRAG 2) | adjacent-mechanism | 2025-02-20 v1; ICML 2025 (per arXiv) | https://arxiv.org/abs/2502.14802 | https://github.com/OSU-NLP-Group/HippoRAG | metadata-checked | HippoRAG 2: Personalized PageRank 기반 graph 기억으로 비모수 지속학습을 표방(ICML 2025 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Jimenez Gutierrez) |
| S73 (가칭 NEW-W2b-022) | A-MEM: Agentic Memory for LLM Agents | adjacent-mechanism | 2025-02-17 v1; NeurIPS 2025 (per arXiv) | https://arxiv.org/abs/2502.12110 |  | metadata-checked | A-MEM: Zettelkasten식 색인·연결과 새 기억이 기존 기억을 갱신하는 agentic 기억(NeurIPS 2025 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Xu) |
| S74 (가칭 NEW-W2b-023) | Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory | adjacent-mechanism | 2025-04-28 v1 | https://arxiv.org/abs/2504.19413 |  | metadata-checked | Mem0: 추출·통합·검색 기반 장기 기억과 graph 변형. 초록 페이지만 확인, 본문 미정독 (첫 저자 Chhikara) |
| S75 (가칭 NEW-W2b-024) | MemGPT: Towards LLMs as Operating Systems | adjacent-mechanism | 2023-10-12 v1 | https://arxiv.org/abs/2310.08560 |  | metadata-checked | MemGPT: 운영체제식 계층 기억으로 가상 컨텍스트 관리. 초록 페이지만 확인, 본문 미정독 (첫 저자 Packer) |
| S76 (가칭 NEW-W2b-025) | NewtonBench: Benchmarking Generalizable Scientific Law Discovery in LLM Agents | evaluation | 2025-10-08 v1; ICLR 2026 (per arXiv comments) | https://arxiv.org/abs/2510.07172 |  | metadata-checked | NewtonBench: 12개 물리 영역 324개 과제, 반사실 법칙 이동으로 암기를 억제하고 시뮬레이션 시스템을 능동 탐색해 법칙을 발견. 초록 페이지만 확인, 본문 미정독 (첫 저자 Zheng) |
| S77 (가칭 NEW-W2b-026) | LLM-SRBench: A New Benchmark for Scientific Equation Discovery with Large Language Models | evaluation | 2025-04-14 v1; ICML 2025 (oral, per arXiv comments) | https://arxiv.org/abs/2504.10415 | https://github.com/deep-symbolic-mathematics/llm-srbench | metadata-checked | LLM-SRBench: LSR-Transform(친숙한 방정식을 낯선 꼴로 변환)과 LSR-Synth(합성 문제)로 암기를 억제하는 방정식 발견 benchmark. 초록 페이지만 확인, 본문 미정독 (첫 저자 Shojaee) |
| S78 (가칭 NEW-W2b-027) | SciGame: Let Agents Play the Scientific Discovery Games in the Real and Counterfactual World | evaluation | 2026-10-27 v1 | https://arxiv.org/abs/2610.37919 |  | metadata-checked | SciGame: 문헌에서 원형과 반사실 환경 쌍을 만들고 prior-only 프로토콜과 모델 컷오프 이후 논문의 temporal collection을 둔다. 초록 페이지만 확인, 본문 미정독 (첫 저자 Zhao) |
| S79 (가칭 NEW-W2b-028) | Can LLMs Discover Scientific Laws in Real and Parallel Worlds? | evaluation | 2026-09-01 v1 | https://arxiv.org/abs/2609.01552 |  | metadata-checked | SciLaws-Bench: 6개 학문 118문제. 발표된 방정식의 구조 변형을 시뮬레이터 질의로 복원하는 parallel-world 설정. 적합도가 높아도 과학적 타당성은 보장되지 않는다고 보고. 초록 페이지만 확인, 본문 미정독 (첫 저자 Huang) |
| S80 (가칭 NEW-W2b-029) | FIRE-Bench: Evaluating AI Agents on the Rediscovery of Scientific Insights | evaluation | 2026-02-02 v1 | https://arxiv.org/abs/2602.02905 |  | metadata-checked | FIRE-Bench: 최근 고영향 ML 연구의 확립된 발견을 연구 질문만으로 재발견하게 하는 평가. 최강 agent도 F1 50 미만. 초록 페이지만 확인, 본문 미정독 (첫 저자 Wang) |
| S81 (가칭 NEW-W2b-030) | MOOSE-Chem: Large Language Models for Rediscovering Unseen Chemistry Scientific Hypotheses | evaluation | 2024-10-09 v1; ICLR 2025 (per arXiv comments) | https://arxiv.org/abs/2410.07076 |  | metadata-checked | MOOSE-Chem: 가설 발견을 영감 검색·구성·순위로 분해하고 2024년 1월 이후 화학 논문 51편으로 재발견을 평가. 초록 페이지만 확인, 본문 미정독 (첫 저자 Yang) |
| S82 (가칭 NEW-W2b-031) | ResearchBench: Benchmarking LLMs in Scientific Discovery via Inspiration-Based Task Decomposition | evaluation | 2025-03-27 v1; ACL 2026 Findings (per arXiv comments) | https://arxiv.org/abs/2503.21248 |  | metadata-checked | ResearchBench: 영감 기반 과제 분해(영감 검색·가설 구성·순위). 사전학습 중복을 줄이려고 2024년 이후 논문만 사용. 초록 페이지만 확인, 본문 미정독 (첫 저자 Liu) |
| S83 (가칭 NEW-W2b-032) | Can Large Language Models Forecast What Researchers Study Next? | evaluation | 2026-09-01 v1; EMNLP 2026 (per arXiv) | https://arxiv.org/abs/2609.00747 |  | metadata-checked | IdeaForecastBench: 생성한 아이디어 순위 목록을 이후 논문과 대조하는 rolling episode(EMNLP 2026 채택 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Li) |
| S84 (가칭 NEW-W2b-033) | Before the Action: Benchmarking LLMs on Prospective Hypothesis Discovery | evaluation | 2026-07-17 v1 | https://arxiv.org/abs/2607.15766 | https://github.com/SKYLENAGE-AI/HypoArena | metadata-checked | Prospective Hypothesis Discovery와 HypoArena: 결론이 나오기 전 불확정 증거에서 검증 가능한 가설 집합을 만드는 능력(988 사례). 초록 페이지만 확인, 본문 미정독 (첫 저자 Zhong) |
| S85 (가칭 NEW-W2b-034) | Scaling Point-in-Time Language Models | evaluation | 2026-05; NBER Working Paper 35247 | https://www.nber.org/papers/w35247 |  | metadata-checked | Point-in-time 언어모델 scaling: 날짜별로 걸러낸 1조 token으로 최대 4B 모델을 학습. NBER 워킹페이퍼라 DOI 레코드로 서지를 확인했다 (첫 저자 Kelly) |
| S86 (가칭 NEW-W2b-035) | Chronologic: Measuring Language Models' Ability to Represent the Past | evaluation | 2026-09-19 v1 | https://arxiv.org/abs/2609.23178 |  | metadata-checked | Chronologic: 1831–1930 영어 문맥을 언어모델이 얼마나 표현하는지 재는 benchmark. 생성 과제가 판별 과제보다 어렵다고 보고. 초록 페이지만 확인, 본문 미정독 (첫 저자 Underwood) |
| A39 (가칭 NEW-W2b-036) | ATLAS: Learning to Optimally Memorize the Context at Test Time | adjacent-mechanism | 2025-05-29 v1 | https://arxiv.org/abs/2505.23735 |  | metadata-checked | ATLAS: 현재와 과거 token으로 기억을 최적화하는 고용량 장기 기억 모듈. 초록 페이지만 확인, 본문 미정독 (첫 저자 Behrouz) |
| A40 (가칭 NEW-W2b-037) | Test-Time Training Done Right (LaCT) | adjacent-mechanism | 2025-05-29 v1 | https://arxiv.org/abs/2505.23884 |  | metadata-checked | LaCT: 2K–1M token 대청크 test-time training으로 하드웨어 효율을 높이고 fast-weight 상태를 키움. 초록 페이지만 확인, 본문 미정독 (첫 저자 Zhang) |
| A41 (가칭 NEW-W2b-038) | Memory Layers at Scale | adjacent-mechanism | 2024-12-12 v1 | https://arxiv.org/abs/2412.09764 |  | metadata-checked | Memory Layers at Scale: 추가 FLOPs 없이 파라미터를 늘리는 학습 가능한 key-value 기억층. 초록 페이지만 확인, 본문 미정독 (첫 저자 Berges) |
| A42 (가칭 NEW-W2b-039) | Continual Learning via Sparse Memory Finetuning | adjacent-mechanism | 2025-10-16 v1 | https://arxiv.org/abs/2510.15103 |  | metadata-checked | Sparse Memory Finetuning: 새 지식에 크게 활성화되는 기억 slot만 갱신해 full finetuning·LoRA보다 망각이 작다고 보고. 초록 페이지만 확인, 본문 미정독 (첫 저자 Lin) |
| A43 (가칭 NEW-W2b-040) | Representation Drift in Continual Learning: LoRA versus N-gram Memory | adjacent-mechanism | 2026-10-10 v1 | https://arxiv.org/abs/2610.14921 |  | metadata-checked | LoRA 갱신 대 N-gram 기억 갱신의 표현 drift 비교: 기억만 갱신하면 drift가 작지만 새 과제 습득이 약하고 저장된 과제끼리 간섭. 초록 페이지만 확인, 본문 미정독 (첫 저자 Wu) |
| A44 (가칭 NEW-W2b-041) | The Surprising Effectiveness of Test-Time Training for Few-Shot Learning | adjacent-mechanism | 2024-11-11 v1 | https://arxiv.org/abs/2411.07279 |  | metadata-checked | ARC 등 few-shot 추론에서 추론 중 임시 파라미터 갱신(test-time training)의 효과. 초록 페이지만 확인, 본문 미정독 (첫 저자 Akyurek) |
| A45 (가칭 NEW-W2b-042) | Self-Adapting Language Models (SEAL) | adjacent-mechanism | 2025-06-12 v1 | https://arxiv.org/abs/2506.10943 |  | metadata-checked | SEAL: LLM이 스스로 finetuning 데이터와 갱신 지시(self-edit)를 생성하고 RL로 학습(가중치 갱신 있음). 초록 페이지만 확인, 본문 미정독 (첫 저자 Zweiger) |
| E06 (가칭 NEW-W2b-043) | Learning to Discover at Test Time | evolution | 2026-01-22 v1; arXiv (ICML 2026 spotlight page seen in search, not opened) | https://arxiv.org/abs/2601.16175 | https://github.com/test-time-training/discover | metadata-checked | TTT-Discover: 단일 시험 문제에서 RL로 가중치를 갱신하며 발견하는 방식(가중치 갱신이 있는 대조 계열). 초록 페이지만 확인, 본문 미정독 (첫 저자 Yuksekgonul) |
| A46 (가칭 NEW-W2b-044) | Orthogonal Subspace Learning for Language Model Continual Learning (O-LoRA) | adjacent-mechanism | 2023-10-22 v1; EMNLP 2023 Findings (per arXiv) | https://arxiv.org/abs/2310.14152 |  | metadata-checked | O-LoRA: 과제마다 이전 과제와 직교하는 저rank 부분공간에서 학습해 replay 없이 망각을 줄임(EMNLP 2023 Findings 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Wang) |
| A47 (가칭 NEW-W2b-045) | LoRA Learns Less and Forgets Less | adjacent-mechanism | 2024-05-15 v1; TMLR Aug 2024 (per arXiv) | https://arxiv.org/abs/2405.09673 |  | metadata-checked | LoRA는 목표 영역에서 덜 배우지만 영역 밖 성능을 더 보존한다(TMLR 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Biderman) |
| A48 (가칭 NEW-W2b-046) | CaLLM: Continual Adaptation of LLMs via Non-Parametric Adapter Routing | adjacent-mechanism | 2026-10-27 v1; CoLLAs 2026 main track (per arXiv) | https://arxiv.org/abs/2610.36994 |  | metadata-checked | CaLLM: 입력을 과제 무관 embedding으로 투영해 가장 가까운 프로토타입의 adapter로 보내는 비모수 adapter 라우팅(CoLLAs 2026 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Celik) |
| A49 (가칭 NEW-W2b-047) | Latent-LoRA: Compact Latent-Space Adapters with Gradient-Free Routing for Continual Learning | adjacent-mechanism | 2026-07-26 v1 | https://arxiv.org/abs/2607.23837 |  | metadata-checked | Latent-LoRA: frozen embedding 위 GMM으로 gradient 학습 없는 adapter 선택과 SVD 제약 저rank adapter. 초록 페이지만 확인, 본문 미정독 (첫 저자 Rahimi Azghan) |
| A50 (가칭 NEW-W2b-048) | When Skills Remain But Access Fails: Factorized Skill Memory for Continual Skill Internalization | adjacent-mechanism | 2026-10-11 v1 | https://arxiv.org/abs/2610.15492 |  | metadata-checked | Factorized Skill Memory: 지속 skill 학습에서 주소 지정 망각이 실행 망각보다 먼저 나타남. 가소적 Address Memory와 frozen LoRA executor로 분리. 초록 페이지만 확인, 본문 미정독 (첫 저자 Qiu) |
| A51 (가칭 NEW-W2b-049) | Self-Indexing Latent Memories for Access-Aware Continual Instruction Tuning of LLMs | adjacent-mechanism | 2026-11-08 v1 | https://arxiv.org/abs/2611.11684 |  | metadata-checked | TILA-CT: replay 없이 과제마다 잠재 기억과 adapter를 두고 기억 자체를 라우팅 키로 사용. 초록 페이지만 확인, 본문 미정독 (첫 저자 Dixit) |
| A52 (가칭 NEW-W2b-050) | Scaling Latent Reasoning via Looped Language Models (Ouro) | adjacent-mechanism | 2025-10-29 v1 | https://arxiv.org/abs/2510.25741 |  | metadata-checked | Ouro: 잠재 공간 looping을 사전학습에 넣은 looped LM. 1.4B·2.6B가 12B급과 겨룬다는 저자 주장. 초록 페이지만 확인, 본문 미정독 (첫 저자 Zhu) |
| A53 (가칭 NEW-W2b-051) | Hierarchical Reasoning Model | adjacent-mechanism | 2025-06-26 v1 | https://arxiv.org/abs/2506.21734 |  | metadata-checked | Hierarchical Reasoning Model: 느린 계획 모듈과 빠른 계산 모듈의 27M 재귀 모델. 초록 페이지만 확인, 본문 미정독 (첫 저자 Wang) |
| A54 (가칭 NEW-W2b-052) | Less is More: Recursive Reasoning with Tiny Networks | adjacent-mechanism | 2025-10-06 v1 | https://arxiv.org/abs/2510.04871 |  | metadata-checked | Tiny Recursive Model: 2층 7M 파라미터 재귀 모델이 ARC-AGI에서 HRM보다 일반화(저자 보고). 초록 페이지만 확인, 본문 미정독 (첫 저자 Jolicoeur-Martineau) |
| A55 (가칭 NEW-W2b-053) | Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters | adjacent-mechanism | 2024-08-06 v1 | https://arxiv.org/abs/2408.03314 |  | metadata-checked | 프롬프트별로 test-time 계산을 compute-optimal하게 배분하면 파라미터 확장보다 효과적일 수 있다는 분석. 초록 페이지만 확인, 본문 미정독 (첫 저자 Snell) |
| A56 (가칭 NEW-W2b-054) | Training Large Language Models to Reason in a Continuous Latent Space (Coconut) | adjacent-mechanism | 2024-12-09 v1; COLM 2025 (per arXiv) | https://arxiv.org/abs/2412.06769 |  | metadata-checked | Coconut: 마지막 hidden state를 다음 입력 embedding으로 되먹이는 연속 잠재 공간 추론(COLM 2025 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Hao) |
| A57 (가칭 NEW-W2b-055) | The Past Is Prologue: A Plug-in Controller for Selective Updates in Sequentially Evolving LLM Memory | adjacent-mechanism | 2026-06-30 v1 | https://arxiv.org/abs/2606.31121 |  | metadata-checked | Janus: 후보 기억 갱신을 받아들일지 이전 기억을 유지할지 판정하는 method-agnostic plug-in controller. 초록 페이지만 확인, 본문 미정독 (첫 저자 Chen) |
| S87 (가칭 NEW-W2b-056) | Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning | adjacent-mechanism | 2025-08-27 v1 | https://arxiv.org/abs/2508.19828 |  | metadata-checked | Memory-R1: RL로 학습한 Memory Manager가 add·update·delete·no-op를 고르고 Answer Agent가 검색된 기억으로 추론. 초록 페이지만 확인, 본문 미정독 (첫 저자 Yan) |
| S88 (가칭 NEW-W2b-057) | Evolving Memory, Learning to Meta-Control: Test-Time Adaptation for Experience-augmented LLM Agents | adjacent-mechanism | 2026-11-01 v1; submitted to ACL Rolling Review Oct 2026 (per arXiv) | https://arxiv.org/abs/2611.01747 |  | metadata-checked | OMCE: 경험 기억을 갱신하고 contextual-bandit router로 DIRECT·EPISODE·GUIDE·DISTILL 사용 방식을 학습(ACL Rolling Review 제출 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Zhao) |
| S89 (가칭 NEW-W2b-058) | Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection | adjacent-mechanism | 2023-10-17 v1 | https://arxiv.org/abs/2310.11511 |  | metadata-checked | Self-RAG: 필요할 때만 검색하고 반성 token으로 자기 출력을 비판하도록 학습. 초록 페이지만 확인, 본문 미정독 (첫 저자 Asai) |
| S90 (가칭 NEW-W2b-059) | MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory | adjacent-mechanism | 2026-01-06 v1 | https://arxiv.org/abs/2601.03192 | https://github.com/MemTensor/MemRL | metadata-checked | MemRL: 가중치 갱신 없이 episodic memory에 런타임 RL을 적용하고 2단계 검색으로 잡음을 거른다. 초록 페이지만 확인, 본문 미정독 (첫 저자 Zhang) |
| A58 (가칭 NEW-W2b-060) | A Neural Dirichlet Process Mixture Model for Task-Free Continual Learning (CN-DPM) | adjacent-mechanism | 2020-01-03 v1; ICLR 2020 (per arXiv) | https://arxiv.org/abs/2001.00689 |  | metadata-checked | CN-DPM: Bayesian 비모수로 신경망 expert를 늘리는 task-free 지속학습(ICLR 2020 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Lee) |
| A59 (가칭 NEW-W2b-061) | Aging with GRACE: Lifelong Model Editing with Discrete Key-Value Adaptors | adjacent-mechanism | 2022-11-20 v1; NeurIPS 2023 (per arXiv) | https://arxiv.org/abs/2211.11031 | https://www.github.com/thartvigsen/grace | metadata-checked | GRACE: 이산 key-value codebook으로 잠재 공간에 국소 편집을 쓰는 평생 모델 편집(NeurIPS 2023 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Hartvigsen) |
| A60 (가칭 NEW-W2b-062) | Human-inspired Episodic Memory for Infinite Context LLMs (EM-LLM) | adjacent-mechanism | 2024-07-12 v1; ICLR 2025 (per arXiv) | https://arxiv.org/abs/2407.09450 |  | metadata-checked | EM-LLM: surprise 기반 경계로 token을 episode로 묶고 유사도와 시간 인접성으로 검색(ICLR 2025 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Fountas) |
| S91 (가칭 NEW-W2b-063) | The Right Fact, the Wrong Decision: SciValidityBench for Scientific Agent Memory | evaluation | 2026-10-26 v1 | https://arxiv.org/abs/2610.34767 |  | metadata-checked | SciValidityBench: 정확히 기억한 사실도 쓰기에는 무효일 수 있다는 관점으로 과학 agent 기억의 유효성 판단을 평가. 초록 페이지만 확인, 본문 미정독 (첫 저자 Pan) |
| A61 (가칭 NEW-W2b-064) | Sleep-time Compute: Beyond Inference Scaling at Test-time | adjacent-mechanism | 2025-04-17 v1 | https://arxiv.org/abs/2504.13171 | https://github.com/letta-ai/sleep-time-compute | metadata-checked | Sleep-time Compute: 질의가 오기 전에 컨텍스트에 대한 추론을 미리 계산해 test-time 계산을 줄임(약 5배는 저자 보고). 초록 페이지만 확인, 본문 미정독 (첫 저자 Lin) |
| S92 (가칭 NEW-W2b-065) | Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving LLM Agents | adjacent-mechanism | 2026-06-08 v1 | https://arxiv.org/abs/2606.09483 |  | metadata-checked | DCPM: 낮에 belief 개정을 기록하고 밤에 schema·의도·교차 도메인 패턴을 유도하는 이중 과정 기억. 초록 페이지만 확인, 본문 미정독 (첫 저자 Fei) |
| S93 (가칭 NEW-W2b-066) | Hippo: Training-Free Agent Self-Evolution via Hippocampal Replay | adjacent-mechanism | 2026-10-17 v1 | https://arxiv.org/abs/2610.24453 |  | metadata-checked | Hippo: 같은 과제의 여러 시도를 비교해 재사용 결정을 추출하고 중복 병합·충돌 해소. 가중치 갱신 없음. 초록 페이지만 확인, 본문 미정독 (첫 저자 Song) |
| S94 (가칭 NEW-W2b-067) | Use and Disuse: Intent-Structured Experience Consolidation for Memory and Learning in LLM Agents | adjacent-mechanism | 2026-10-08 v1 | https://arxiv.org/abs/2610.12124 |  | metadata-checked | Use and Disuse(Hippocam): 중첩 intent 구조로 경험을 통합하고 오래 쓰지 않은 이력을 추상화. 초록 페이지만 확인, 본문 미정독 (첫 저자 Zeng) |
| A62 (가칭 NEW-W2b-068) | Continual Learning with Deep Generative Replay | adjacent-mechanism | 2017-05-24 v1; NIPS 2017 (per arXiv) | https://arxiv.org/abs/1705.08690 |  | metadata-checked | Deep Generative Replay: 생성 모델이 이전 과제 표본을 만들어 새 학습과 섞는다(NIPS 2017 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Shin) |
| A63 (가칭 NEW-W2b-069) | Sleep-like unsupervised replay reduces catastrophic forgetting in artificial neural networks | adjacent-mechanism | 2022-12; Nature Communications 13 | https://doi.org/10.1038/s41467-022-34938-7 |  | metadata-checked | Sleep-like unsupervised replay: 수면 유사 재생 단계가 인공신경망의 재앙적 망각을 줄인다. 서지는 Crossref 레코드로 확인했고 초록은 읽지 않았다 (첫 저자 Tadros) |
| A64 (가칭 NEW-W2b-070) | LoraHub: Efficient Cross-Task Generalization via Dynamic LoRA Composition | adjacent-mechanism | 2023-07-25 v1; COLM 2024 (per arXiv) | https://arxiv.org/abs/2307.13269 |  | metadata-checked | LoraHub: LoRA 모듈을 동적으로 조합해 보지 못한 과제에 일반화(COLM 2024 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Huang) |
| A65 (가칭 NEW-W2b-071) | Text-to-LoRA: Instant Transformer Adaption | adjacent-mechanism | 2025-06-06 v1; ICML 2025 (per arXiv) | https://arxiv.org/abs/2506.06105 |  | metadata-checked | Text-to-LoRA: 과제 설명 text에서 hypernetwork가 한 번의 forward로 LoRA adapter를 생성(ICML 2025 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Charakorn) |
| A66 (가칭 NEW-W2b-072) | Cartridges: Lightweight and general-purpose long context representations via self-study | adjacent-mechanism | 2025-06-06 v1 | https://arxiv.org/abs/2506.06266 |  | metadata-checked | Cartridges: 코퍼스별 작은 KV cache를 오프라인으로 학습해 긴 컨텍스트 프롬프트를 대체(self-study). 초록 페이지만 확인, 본문 미정독 (첫 저자 Eyuboglu) |
| S95 (가칭 NEW-W2b-073) | KV-Skill: Forging Expertise in the Model's Native Language | neural-continuous | 2026-08-05 v1 | https://arxiv.org/abs/2608.05475 | https://github.com/shawnzhg/KV-Skill | metadata-checked | KV-Skill: 과제 지식을 외부 operator로 압축해 frozen LM이 가벼운 인터페이스로 읽게 한다. 프롬프트 text 추가 없음. 초록 페이지만 확인, 본문 미정독 (첫 저자 Han) |
| A67 (가칭 NEW-W2b-074) | The Mamba in the Llama: Distilling and Accelerating Hybrid Models | adjacent-mechanism | 2024-08-27 v1; NeurIPS 2024 (per arXiv) | https://arxiv.org/abs/2408.15237 |  | metadata-checked | Mamba in the Llama: Llama3-8B-Instruct를 attention 투영을 재사용해 선형 RNN 혼합 모델로 증류(NeurIPS 2024 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Wang) |
| S96 (가칭 NEW-W2b-075) | Nothing from Something: Can a Language Model Discover 0? | evaluation | 2026-06-15 v1 | https://arxiv.org/abs/2606.17289 |  | metadata-checked | Can a Language Model Discover 0: 단순 산술에서 0의 발견을 시험. GPT-2급 모델은 실패하고 언어 사전학습이 필요한 예시 수를 줄인다. 초록 페이지만 확인, 본문 미정독 (첫 저자 Zeng) |
| S97 (가칭 NEW-W2b-076) | Tracing the Scientific Discovery Capacity of LLMs to Their Training Data | evaluation | 2026-11-02 v1 | https://arxiv.org/abs/2611.03617 |  | metadata-checked | LLM의 발견 능력이 학습 데이터의 monofact(한 번만 본 사실)와 관련된다는 주장과 재료과학·유전체 실험. 초록 페이지만 확인, 본문 미정독 (첫 저자 Uzunoglu) |
| S98 (가칭 NEW-W2b-077) | Geometric Signatures of Conceptual Reorganization: A Counterfactual Embedding Framework for Detecting Scientific Revolutions | evaluation | 2026-09-14 v1 | https://arxiv.org/abs/2609.14917 |  | metadata-checked | 문서 embedding 기하를 개념 재편의 관측량으로 쓰는 counterfactual ablation 틀. 역사 사례 5건으로 시험. 초록 페이지만 확인, 본문 미정독 (첫 저자 Ntounis) |
| S99 (가칭 NEW-W2b-078) | ULTRADISCOVERY: Abductive Exploration in an Interconnected, Epistemically Open Universe | evaluation | 2026-10-02 v1 | https://arxiv.org/abs/2610.03092 |  | metadata-checked | ULTRADISCOVERY: 발견은 증거 수집이 아니라 설명이 서술되는 표현의 구성이라는 관점. agent는 빠진 개체를 도입하거나 변수를 다시 쓰지 못한다고 보고. 초록 페이지만 확인, 본문 미정독 (첫 저자 Li) |
| S100 (가칭 NEW-W2b-079) | Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations | evaluation | 2026-11-10 v1; NeurIPS 2026 accepted (per arXiv) | https://arxiv.org/abs/2611.14514 |  | metadata-checked | Contrastive Discovery: 가설과 그 부정만 비교하지 않고 상호 배타적 경쟁 설명 집합 위에서 실험을 채점(NeurIPS 2026 채택 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Liu) |
| S101 (가칭 NEW-W2b-080) | LAMB: Latent Multi-Hypothesis Beliefs for Long-Horizon Large Language Agents | adjacent-mechanism | 2026-10-18 v1 | https://arxiv.org/abs/2610.26955 |  | metadata-checked | LAMB: 경쟁하는 가설을 이산 텍스트가 아닌 잠재 상태로 유지하는 순환 신념 틀. 초록 페이지만 확인, 본문 미정독 (첫 저자 Ding) |
| E07 (가칭 NEW-W2b-081) | Kosmos: An AI Scientist for Autonomous Discovery | evolution | 2025-11-04 v1 | https://arxiv.org/abs/2511.02824 |  | metadata-checked | Kosmos: 최대 12시간 자율 데이터 기반 연구 agent. 보고서 진술의 79.4%가 정확했다는 독립 평가는 저자 보고. 초록 페이지만 확인, 본문 미정독 (첫 저자 Mitchener) |
| E08 (가칭 NEW-W2b-082) | Accelerating scientific discovery with Co-Scientist | evolution | 2025-02-26 v1; Nature 2026 (per arXiv comments) | https://arxiv.org/abs/2502.18864 |  | metadata-checked | Co-Scientist(Gemini 기반 다중 agent): 가설을 생성·비판·토너먼트로 진화시킴. 읽은 시점의 arXiv 제목을 적었다(Nature 2026 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Gottweis) |
| E09 (가칭 NEW-W2b-083) | The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search | evolution | 2025-04-10 v1 | https://arxiv.org/abs/2504.08066 | https://github.com/SakanaAI/AI-Scientist-v2 | metadata-checked | AI Scientist-v2: 가설·실험·논문 작성을 잇는 agent 시스템. 3편 중 1편이 workshop 심사 기준을 넘었다는 저자 주장. 초록 페이지만 확인, 본문 미정독 (첫 저자 Yamada) |
| E10 (가칭 NEW-W2b-084) | Can AI Agents Make Open-Ended Scientific Discovery? Evidence from Station | evolution | 2026-10-06 v1 | https://arxiv.org/abs/2610.08927 |  | metadata-checked | Station: 개방형 다중 agent 환경에서 ICLR 구두 논문 3편의 기준을 재발견하는 정도를 보고(초록 수준). 초록 페이지만 확인, 본문 미정독 (첫 저자 Du) |
| S102 (가칭 NEW-W2b-085) | Generative Agents: Interactive Simulacra of Human Behavior | adjacent-mechanism | 2023-04-07 v1 | https://arxiv.org/abs/2304.03442 |  | metadata-checked | Generative Agents: 자연어 경험의 memory stream과 reflection·planning. 초록 페이지만 확인, 본문 미정독 (첫 저자 Park) |
| S103 (가칭 NEW-W2b-086) | RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval | adjacent-mechanism | 2024-01-31 v1 | https://arxiv.org/abs/2401.18059 |  | metadata-checked | RAPTOR: 재귀적으로 embedding·군집·요약해 만든 트리에서 추상 수준별로 검색. 초록 페이지만 확인, 본문 미정독 (첫 저자 Sarthi) |
| S104 (가칭 NEW-W2b-087) | Reflexion: Language Agents with Verbal Reinforcement Learning | adjacent-mechanism | 2023-03-20 v1 | https://arxiv.org/abs/2303.11366 |  | metadata-checked | Reflexion: 피드백에 대한 언어적 반성을 episodic buffer에 저장해 가중치 없이 개선. 초록 페이지만 확인, 본문 미정독 (첫 저자 Shinn) |
| S105 (가칭 NEW-W2b-088) | Agent Workflow Memory | adjacent-mechanism | 2024-09-11 v1 | https://arxiv.org/abs/2409.07429 |  | metadata-checked | Agent Workflow Memory: 과거 경험에서 재사용 가능한 workflow를 유도해 web agent를 안내. 초록 페이지만 확인, 본문 미정독 (첫 저자 Wang) |
| S106 (가칭 NEW-W2b-089) | Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models | adjacent-mechanism | 2024-06-06 v1; NeurIPS 2024 spotlight (per arXiv) | https://arxiv.org/abs/2406.04271 | https://github.com/YangLing0818/buffer-of-thought-llm | metadata-checked | Buffer of Thoughts: 사고 템플릿 meta-buffer와 buffer-manager(NeurIPS 2024 spotlight 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Yang) |
| S107 (가칭 NEW-W2b-090) | Voyager: An Open-Ended Embodied Agent with Large Language Models | adjacent-mechanism | 2023-05-25 v1 | https://arxiv.org/abs/2305.16291 |  | metadata-checked | Voyager: Minecraft agent가 실행 가능한 code skill 라이브러리를 키우며 평생 학습. 초록 페이지만 확인, 본문 미정독 (첫 저자 Wang) |
| S108 (가칭 NEW-W2b-091) | STRATA: Self-Maintaining Structured Experience Graphs for Self-Evolving Language Agents | adjacent-mechanism | 2026-10-14 v1 | https://arxiv.org/abs/2610.19386 |  | metadata-checked | STRATA: skill·workflow·meta-framework 3층 경험 graph를 pruning과 contrast edge로 스스로 유지. 초록 페이지만 확인, 본문 미정독 (첫 저자 Zhu) |
| S109 (가칭 NEW-W2b-092) | SCALE: Small-Model-First Concept Abstraction with LLM-Guided Experience Internalization | adjacent-mechanism | 2026-11-09 v1 | https://arxiv.org/abs/2611.12120 |  | metadata-checked | SCALE: 소형 모델이 일상 예측을 맡고 예측 오류가 LLM 반성을 유발하며 검증된 개념 가설을 계층 표현으로 내재화. 초록 페이지만 확인, 본문 미정독 (첫 저자 Su) |
| S110 (가칭 NEW-W2b-093) | Mental Model Management: An Operator-Based Framework for LLM Memory | adjacent-mechanism | 2026-08-16 v1 | https://arxiv.org/abs/2608.15451 |  | metadata-checked | Mental Model Management: 지식을 압축된 mental model 덩어리로 저장하고 추출·검색·갱신·재조직·불일치 검사 연산자를 둔다. 초록 페이지만 확인, 본문 미정독 (첫 저자 Kramer) |
| S111 (가칭 NEW-W2b-094) | Memory as Belief: Bayesian Evolution of Memory for Self-Evolving LLM Agents | adjacent-mechanism | 2026-10-18 v1 | https://arxiv.org/abs/2610.25119 |  | metadata-checked | Memory as Belief(BEAM): 기억의 가치를 문맥 의존 belief로 보고 실행 피드백으로 개정. 초록 페이지만 확인, 본문 미정독 (첫 저자 Xu) |
| S112 (가칭 NEW-W2b-095) | In-context Vectors: Making In Context Learning More Effective and Controllable Through Latent Space Steering | neural-continuous | 2023-11-11 v1 | https://arxiv.org/abs/2311.06668 |  | metadata-checked | In-context vectors: 시연을 잠재 공간 vector로 증류해 프롬프트를 늘리지 않고 잠재 상태를 이동. 초록 페이지만 확인, 본문 미정독 (첫 저자 Liu) |
| S113 (가칭 NEW-W2b-096) | Steering Language Models With Activation Engineering | neural-continuous | 2023-08-20 v1 | https://arxiv.org/abs/2308.10248 |  | metadata-checked | Activation Addition: 프롬프트 쌍의 활성화 차이로 만든 steering vector를 forward 중 더해 출력을 조향. 초록 페이지만 확인, 본문 미정독 (첫 저자 Turner) |
| S114 (가칭 NEW-W2b-097) | Rules Amortize, Pairings Don't: Linguistic Structure Determines What Latent Task Representations Can Replace In-Context Learning | neural-continuous | 2026-09-30 v1; NeurIPS 2026 Workshop LP4FM (per arXiv) | https://arxiv.org/abs/2610.00526 |  | metadata-checked | 잠재 task 표현이 ICL을 대체하는 범위는 언어 구조가 결정한다: 생산적 규칙은 대체되고 임의 쌍(antonym 등)은 절반 수준에서 정체(NeurIPS 2026 workshop 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Jhingran) |
| S115 (가칭 NEW-W2b-098) | Task Vectors Can Be Linearly Decomposed into Interpretable and Controllable Components | neural-continuous | 2026-10-30 v1 | https://arxiv.org/abs/2610.41743 |  | metadata-checked | task vector를 Task Recognition·Task Learning·잔여 성분으로 선형 분해하고 계수 최적화로 개입. 초록 페이지만 확인, 본문 미정독 (첫 저자 Horiba) |
| S116 (가칭 NEW-W2b-099) | Task Vectors in In-Context Learning: Emergence, Formation, and Benefit | neural-continuous | 2025-01-16 v1 | https://arxiv.org/abs/2501.09240 |  | metadata-checked | ICL의 task vector가 생기는 조건과 약하게 또는 비국소로 인코딩되는 경우, TVP-loss 제안. 초록 페이지만 확인, 본문 미정독 (첫 저자 Yang) |
| A68 (가칭 NEW-W2b-100) | Routed Continual Learning | adjacent-mechanism | 2026-10-28 v1 | https://arxiv.org/abs/2610.38796 |  | metadata-checked | Routed Continual Learning: 지속학습을 학습 방식과 상태 군집을 고르는 routing 문제로 보고 LLM router가 기존 또는 새 경험 군집에 배정. 초록 페이지만 확인, 본문 미정독 (첫 저자 Philip) |
| S117 (가칭 NEW-W2b-101) | Memory-Centric Continual Learning for AI Agents | adjacent-mechanism | 2026-10-21 v1 | https://arxiv.org/abs/2610.29357 |  | metadata-checked | Memory-Centric Continual Learning: 기억은 검색 품질이 아니라 미래 행동 개선으로 평가해야 한다는 분류·평가 프로토콜 제안. 초록 페이지만 확인, 본문 미정독 (첫 저자 Li et al. (28 authors)) |
| S118 (가칭 NEW-W2b-102) | Memory in the Age of AI Agents | adjacent-mechanism | 2025-12-15 v1 | https://arxiv.org/abs/2512.13564 |  | metadata-checked | agent 기억 survey: 형태(token·parametric·latent), 기능(factual·experiential·working), 동역학(형성·진화·검색)으로 분류. 초록 페이지만 확인, 본문 미정독 (첫 저자 Hu) |
| E11 (가칭 NEW-W2b-103) | From AutoResearch to Continual AutoResearch: Do Agents Learn Across Tasks? | evolution | 2026-11-03 v1 | https://arxiv.org/abs/2611.05108 |  | metadata-checked | Continual AutoResearch: agent의 지속 상태가 연구 효율은 올리지만 최종 해의 질을 일관되게 올리지는 못한다는 보고. 초록 페이지만 확인, 본문 미정독 (첫 저자 Qin) |
| S119 (가칭 NEW-W2b-104) | Scientific Discovery: Computational Explorations of the Creative Processes | symbolic | 1987; MIT Press 357 pp | https://openlibrary.org/isbn/0262121166 |  | metadata-checked | BACON 계열 발견 프로그램의 법칙 재발견을 다룬 단행본(Langley·Simon·Bradshaw·Zytkow). 서지는 Open Library 레코드로 확인했고 내용 요약은 검색 결과 수준이다(출판사 페이지는 403) (첫 저자 Langley) |
| S120 (가칭 NEW-W2b-105) | Fish Oil, Raynaud's Syndrome, and Undiscovered Public Knowledge | symbolic | 1986; Perspectives in Biology and Medicine 30(1):7-18 | https://doi.org/10.1353/pbm.1986.0087 |  | metadata-checked | Swanson의 문헌 기반 발견(서로 인용하지 않는 두 문헌을 이어 가설 도출). 서지는 Crossref 레코드로 확인했고 초록은 검색 결과 수준이다(학술지 페이지는 접근 불가) (첫 저자 Swanson) |
| S121 (가칭 NEW-W2b-106) | AI Feynman: a Physics-Inspired Method for Symbolic Regression | symbolic | 2019-05-27 v1; Science Advances 6:eaay2631 (2020) | https://arxiv.org/abs/1905.11481 | https://github.com/SJ001/AI-Feynman | metadata-checked | AI Feynman: 신경망 적합과 대칭·분리가능성·합성성을 쓰는 재귀 symbolic regression. Feynman 강의 방정식 100개 회복(저자 보고). 초록 페이지만 확인, 본문 미정독 (첫 저자 Udrescu) |
| S122 (가칭 NEW-W2b-107) | Contemporary Symbolic Regression Methods and their Relative Performance (SRBench) | evaluation | 2021-07-29 v1; NeurIPS 2021 Datasets and Benchmarks (per arXiv) | https://arxiv.org/abs/2107.14351 |  | metadata-checked | SRBench: 14개 symbolic regression 방법과 7개 ML 방법을 252개 회귀 문제에서 비교하는 재현 가능한 평가 플랫폼. 초록 페이지만 확인, 본문 미정독 (첫 저자 La Cava) |
| E12 (가칭 NEW-W2b-108) | LLM-SR: Scientific Equation Discovery via Programming with Large Language Models | evolution | 2024-04-29 v1; ICLR 2025 (oral, per arXiv) | https://arxiv.org/abs/2404.18400 | https://github.com/deep-symbolic-mathematics/LLM-SR | metadata-checked | LLM-SR: 방정식을 프로그램으로 보고 LLM이 골격을 제안하고 진화 탐색과 데이터 적합으로 정제. 초록 페이지만 확인, 본문 미정독 (첫 저자 Shojaee) |
| S123 (가칭 NEW-W2b-109) | Can LLMs Uncover Hidden Physical Laws through Free Exploration? | evaluation | 2026-10-27 v1 | https://arxiv.org/abs/2610.37649 |  | metadata-checked | LongChang: 물리 법칙이 바뀐 시뮬레이션 세계에서 LLM이 이상 현상을 스스로 알아채고 바뀐 법칙을 찾는지 시험(발견율 낮음, 초록 보고). 초록 페이지만 확인, 본문 미정독 (첫 저자 Yang) |
| S124 (가칭 NEW-W2b-110) | Unsatz: Evaluating Scientific Discovery Without a Given Ansatz | evaluation | 2026-10-31 v1 | https://arxiv.org/abs/2611.03713 |  | metadata-checked | Unsatz: 주어진 ansatz 없이 모델 구조를 직접 고르게 하고 미관측 실험 예측으로 채점. 구조 발견이 병목이라고 보고. 초록 페이지만 확인, 본문 미정독 (첫 저자 Ji) |
| S125 (가칭 NEW-W2b-111) | Beyond Equation Search: Conjecture-Guided Discovery with SCOPE and ClosureBench | evaluation | 2026-10-13 v1 | https://arxiv.org/abs/2610.18938 |  | metadata-checked | SCOPE와 ClosureBench: 다중 과학자 agent의 conjecture 추적과 60개 closure 발견 과제. 증거 충실도·mechanism 통찰·실험 효과도 채점. 초록 페이지만 확인, 본문 미정독 (첫 저자 Hu) |
| S126 (가칭 NEW-W2b-112) | ExplorationBench: Measuring AI Systems' Exploration in Verifiable Alien Worlds | evaluation | 2026-09-24 v1 | https://arxiv.org/abs/2609.30199 |  | metadata-checked | ExplorationBench: 알려진 사실과 충돌하는 실행 가능한 낯선 세계에서 탐색을 재고 회상만으로는 풀 수 없게 한다. 초록 페이지만 확인, 본문 미정독 (첫 저자 Zhang) |
| S127 (가칭 NEW-W2b-113) | Scientific reasoning does not reliably translate into scientific forecasting in frontier AI | evaluation | 2026-05-21 v1 | https://arxiv.org/abs/2605.22681 |  | metadata-checked | 과학적 추론이 과학적 예측으로 이어지지 않는다는 보고: 미래 진전의 mechanism은 추론하나 실현 가능성 판단은 우연 수준. 초록 페이지만 확인, 본문 미정독 (첫 저자 Wu) |
| S128 (가칭 NEW-W2b-114) | From Scientific Observations to Mechanisms: Benchmarking Hypothesis Generation by AI Scientists | evaluation | 2026-10-04 v1 | https://arxiv.org/abs/2610.05197 |  | metadata-checked | MechHypoBench: 관측 데이터에서 mechanism 가설을 만드는 AI 과학자 평가. 생성 가설과 실제 mechanism 사이 큰 격차 보고. 초록 페이지만 확인, 본문 미정독 (첫 저자 Xie) |
| S129 (가칭 NEW-W2b-115) | AgentIdeaBench: Benchmarking Scientific Ideation in the Agent Era | evaluation | 2026-09-07 v1 | https://arxiv.org/abs/2609.07611 | https://github.com/HKUST-KnowComp/AgentIdeaBench | metadata-checked | AgentIdeaBench: 정적 참고 논문 대 능동 검색 탐색의 아이디어 생성 비교(33개 모델). 독창성은 바뀌지 않았다고 보고. 초록 페이지만 확인, 본문 미정독 (첫 저자 Mo) |
| S130 (가칭 NEW-W2b-116) | Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers | evaluation | 2024-09-06 v1 | https://arxiv.org/abs/2409.04109 |  | metadata-checked | LLM이 생성한 연구 아이디어가 전문가 아이디어보다 새롭다고 판정됐고 실행 가능성은 약간 낮았다는 100명 이상 대상 인간 연구. 초록 페이지만 확인, 본문 미정독 (첫 저자 Si) |
| S131 (가칭 NEW-W2b-117) | Large language models surpass human experts in predicting neuroscience results | evaluation | 2024-03-04 v1; Nature Human Behaviour (per arXiv comments) | https://arxiv.org/abs/2403.03230 |  | metadata-checked | BrainBench: 신경과학 결과 예측 benchmark. LLM이 전문가보다 낫다고 보고(Nature Human Behaviour 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Luo) |
| S132 (가칭 NEW-W2b-118) | OpenFrontiers: A Collection of Open Research Problems and a Benchmark for Scientific Rediscovery | evaluation | 2026-10-27 v1 | https://arxiv.org/abs/2610.37739 |  | metadata-checked | OpenFrontiers: 열린 연구 문제 12,151개와 Lean 4로 채점하는 수학 재발견 benchmark 200문제. closed-book·frozen-retrieval·live-web 조건 비교. 초록 페이지만 확인, 본문 미정독 (첫 저자 Yao) |
| S133 (가칭 NEW-W2b-119) | DiscoveryWorld: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents | evaluation | 2024-06-10 v1; NeurIPS 2024 Benchmark Track (spotlight, per arXiv) | https://arxiv.org/abs/2406.06769 | https://github.com/allenai/discoveryworld | metadata-checked | DiscoveryWorld: 텍스트 기반 가상 환경의 120개 발견 과제. 과제 완료·관련 행동·발견한 설명 지식을 채점(NeurIPS 2024 Benchmark Track). 초록 페이지만 확인, 본문 미정독 (첫 저자 Jansen) |
| S134 (가칭 NEW-W2b-120) | DiscoveryBench: Towards Data-Driven Discovery with Large Language Models | evaluation | 2024-07-01 v1 | https://arxiv.org/abs/2407.01725 | https://github.com/allenai/discoverybench | metadata-checked | DiscoveryBench: 실제 264개와 합성 903개 과제로 데이터 기반 가설 탐색·검증을 평가. 초록 페이지만 확인, 본문 미정독 (첫 저자 Majumder) |
| S135 (가칭 NEW-W2b-121) | ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery | evaluation | 2024-10-07 v1; ICLR 2025 (per arXiv) | https://arxiv.org/abs/2410.05080 |  | metadata-checked | ScienceAgentBench: 동료 심사 논문 44편의 102개 데이터 기반 과제를 Python 프로그램으로 평가(ICLR 2025). 초록 페이지만 확인, 본문 미정독 (첫 저자 Chen) |
| S136 (가칭 NEW-W2b-122) | Evaluating Large Language Models in Scientific Discovery | evaluation | 2025-12-17 v1 | https://arxiv.org/abs/2512.15567 |  | metadata-checked | 시나리오 기반 과학 발견 benchmark: 문항 정확도와 프로젝트 단위 성과를 함께 채점. 초록 페이지만 확인, 본문 미정독 (첫 저자 Song) |
| S137 (가칭 NEW-W2b-123) | BoxingGym: Benchmarking Progress in Automated Experimental Design and Model Discovery | evaluation | 2025-01-02 v1 | https://arxiv.org/abs/2501.01540 |  | metadata-checked | BoxingGym: 10개 확률 모델 환경에서 실험 설계와 모델 발견을 평가. 초록 페이지만 확인, 본문 미정독 (첫 저자 Gandhi) |
| S138 (가칭 NEW-W2b-124) | LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code | evaluation | 2024-03-12 v1 | https://arxiv.org/abs/2403.07974 |  | metadata-checked | LiveCodeBench: 모델 컷오프 이후에 공개된 대회 문제를 계속 수집하는 오염 없는 평가. 초록 페이지만 확인, 본문 미정독 (첫 저자 Jain) |
| S139 (가칭 NEW-W2b-125) | LiveBench: A Challenging, Contamination-Limited LLM Benchmark | evaluation | 2024-06-27 v1; ICLR 2025 spotlight (per arXiv) | https://arxiv.org/abs/2406.19314 |  | metadata-checked | LiveBench: 문제를 주기적으로 갱신하고 객관 정답으로 채점해 오염을 제한하는 benchmark(ICLR 2025 spotlight 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 White) |
| E13 (가칭 NEW-W2b-126) | Agent Laboratory: Using LLM Agents as Research Assistants | evolution | 2025-01-08 v1 | https://arxiv.org/abs/2501.04227 |  | metadata-checked | Agent Laboratory: 인간 아이디어를 문헌 조사·실험·보고서로 잇는 LLM agent 프레임워크. 초록 페이지만 확인, 본문 미정독 (첫 저자 Schmidgall) |
| E14 (가칭 NEW-W2b-127) | DiscoveryRSI: Recursively Learning to Discover Valuable Hypotheses | evolution | 2026-10-16 v1 | https://arxiv.org/abs/2610.23839 | https://github.com/Gen-Verse/DiscoveryRSI | metadata-checked | DiscoveryRSI: 가치 있는 검증 가능 가설을 정의하고 다중 agent 진화 탐색과 재귀 자기 개선을 적용. 초록 페이지만 확인, 본문 미정독 (첫 저자 Zhong) |
| N33 (가칭 NEW-W2b-128) | Structure-mapping: A theoretical framework for analogy | neuroscience | 1983; Cognitive Science 7(2):155-170 | https://doi.org/10.1016/s0364-0213(83)80009-3 |  | metadata-checked | Gentner의 structure-mapping 이론 1차 논문. catalog N17은 같은 이론의 요약 페이지를 가리킨다. 서지는 Crossref 레코드로 확인, 초록은 읽지 않았다 (첫 저자 Gentner) |
| N34 (가칭 NEW-W2b-129) | The Roles of Similarity in Transfer: Separating Retrievability From Inferential Soundness | neuroscience | 1993; Cognitive Psychology 25(4):524-575 | https://doi.org/10.1006/cogp.1993.1013 |  | metadata-checked | 표면 유사성은 검색을, 구조 유사성은 추론 건전성을 좌우한다는 전이 연구. 서지만 확인 (첫 저자 Gentner) |
| N35 (가칭 NEW-W2b-130) | Schema induction and analogical transfer | neuroscience | 1983; Cognitive Psychology 15(1):1-38 | https://doi.org/10.1016/0010-0285(83)90002-6 |  | metadata-checked | Gick와 Holyoak: 유추 사례에서 schema를 유도하면 전이가 촉진된다는 고전 연구. 서지만 확인 (첫 저자 Gick) |
| N36 (가칭 NEW-W2b-131) | Constraint relaxation and chunk decomposition in insight problem solving | neuroscience | 1999; JEP:LMC 25(6):1534-1555 | https://doi.org/10.1037/0278-7393.25.6.1534 |  | metadata-checked | 통찰 문제 해결의 representational change 이론: constraint relaxation과 chunk decomposition. 서지만 확인 (첫 저자 Knoblich) |
| N37 (가칭 NEW-W2b-132) | The Cognitive Neuroscience of Insight | neuroscience | 2014; Annual Review of Psychology 65(1):71-93 | https://doi.org/10.1146/annurev-psych-010213-115154 |  | metadata-checked | 통찰의 인지신경과학 리뷰(Annual Review of Psychology). 서지만 확인 (첫 저자 Kounios) |
| N38 (가칭 NEW-W2b-133) | Does incubation enhance problem solving? A meta-analytic review | neuroscience | 2009; Psychological Bulletin 135(1):94-120 | https://doi.org/10.1037/a0014212 |  | metadata-checked | 인큐베이션 효과의 메타분석(Psychological Bulletin). 서지만 확인 (첫 저자 Sio) |
| N39 (가칭 NEW-W2b-134) | The Structure of Scientific Revolutions | neuroscience | 1962; University of Chicago Press (later eds 1970/1996/2012) |  |  | needs-resolution | 이상 현상에서 위기와 혁명으로 가는 과학 변화 서술(Kuhn, University of Chicago Press, 1962 초판). 검색 결과로만 확인했고 레지스트리 메타데이터의 첫 출판 연도가 판본마다 달라 서지 미확인으로 둔다 (첫 저자 Kuhn) |
| S140 (가칭 NEW-W2b-135) | Emergent Analogical Reasoning in Large Language Models | adjacent-mechanism | 2022-12-19 v1; Nature Human Behaviour 2023 (per arXiv) | https://arxiv.org/abs/2212.09196 |  | metadata-checked | LLM의 창발적 유추 추론: GPT-3가 Raven식 유추 문제를 zero-shot으로 풀었다는 보고(Nature Human Behaviour 2023 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Webb) |
| S141 (가칭 NEW-W2b-136) | Using Counterfactual Tasks to Evaluate the Generality of Analogical Reasoning in Large Language Models | evaluation | 2024-02-14 v1 | https://arxiv.org/abs/2402.08955 |  | metadata-checked | 반사실 유추 과제로 LLM 유추의 일반성을 평가: 사람은 유지되고 GPT 모델은 크게 떨어진다. 초록 페이지만 확인, 본문 미정독 (첫 저자 Lewis) |
| S142 (가칭 NEW-W2b-137) | When Models Know More Than They Say: Probing Analogical Reasoning in LLMs | evaluation | 2026-04-04 v1 | https://arxiv.org/abs/2604.03877 |  | metadata-checked | 표면 단서와 구조 단서가 어긋나는 유추에서 probing이 prompting보다 낫다는 분석(수사적 유추 한정). 초록 페이지만 확인, 본문 미정독 (첫 저자 McGovern) |
| S143 (가칭 NEW-W2b-138) | ARCANA: A Benchmark for Abstraction and Analogical Reasoning | evaluation | 2026-10-21 v1 | https://arxiv.org/abs/2610.29271 | https://github.com/density-11/arcana-test | metadata-checked | ARCANA: 실세계 대상과 추상 grid 변환을 잇는 far-analogy benchmark. 사람은 안정적이나 LLM은 격차. 초록 페이지만 확인, 본문 미정독 (첫 저자 Chen) |
| S144 (가칭 NEW-W2b-139) | Unlocking LLM Creativity in Science through Analogical Reasoning | adjacent-mechanism | 2026-05-11 v1 | https://arxiv.org/abs/2605.11258 |  | metadata-checked | 유추 추론으로 과학 해 생성의 mode collapse를 줄이고 다양성을 높인다는 보고(저자 주장). 초록 페이지만 확인, 본문 미정독 (첫 저자 Shen) |
| S145 (가칭 NEW-W2b-140) | An Explanation of In-context Learning as Implicit Bayesian Inference | adjacent-mechanism | 2021-11-03 v1; ICLR 2022 (per arXiv) | https://arxiv.org/abs/2111.02080 |  | metadata-checked | ICL을 잠재 개념에 대한 암묵적 Bayesian 추론으로 설명(ICLR 2022 표기). 초록 페이지만 확인, 본문 미정독 (첫 저자 Xie) |

## 부록 C. 조사 출처

**방법.** 후보 발굴은 주제어 검색(alphaXiv 후보 검색 10회, 웹 검색 13회, 일부 논문은 PDF 발췌 열람 3회)으로 했고 검색어에는 논문 제목과 주제어만 썼다. 발굴된 항목마다 1차 출처(arXiv 초록 페이지, DOI·도서 레지스트리, 공식 페이지)를 직접 열어 확인했다. 열람 도구가 반환한 초록 요약은 원문 대조 전 단계이므로 인용 전에 다시 본다.

### C-1. 부록 B 문헌

| id | URL | 접근일 | 읽은 범위 | 확인 수준 |
|---|---|---|---|---|
| S52 | https://arxiv.org/abs/2610.06516 | 2026-11-18 | arXiv 초록 페이지와 PDF 발췌 페이지(방법·실험·한계 일부) | metadata-checked |
| S53 | https://arxiv.org/abs/2610.08586 | 2026-11-18 | arXiv 초록 페이지와 PDF 발췌 페이지(방법·실험·한계 일부) | metadata-checked |
| S54 | https://arxiv.org/abs/2610.14958 | 2026-11-18 | arXiv 초록 페이지와 PDF 발췌 페이지(방법·실험·한계 일부) | metadata-checked |
| S55 | https://arxiv.org/abs/2503.03666 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S56 | https://arxiv.org/abs/2605.30284 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S57 | https://arxiv.org/abs/2608.16645 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S58 | https://arxiv.org/abs/2502.21206 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S59 | https://arxiv.org/abs/2610.18602 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S60 | https://arxiv.org/abs/2611.21554 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S61 | https://arxiv.org/abs/2601.00514 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S62 | https://arxiv.org/abs/2308.10144 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S63 | https://arxiv.org/abs/2504.07952 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S64 | https://arxiv.org/abs/2509.25140 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S65 | https://arxiv.org/abs/2510.04618 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S66 | https://arxiv.org/abs/2509.04439 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S67 | https://arxiv.org/abs/2610.27406 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S68 | https://arxiv.org/abs/2606.29824 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S69 | https://arxiv.org/abs/2310.15916 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S70 | https://arxiv.org/abs/1911.00172 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S71 | https://arxiv.org/abs/2203.08913 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S72 | https://arxiv.org/abs/2502.14802 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S73 | https://arxiv.org/abs/2502.12110 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S74 | https://arxiv.org/abs/2504.19413 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S75 | https://arxiv.org/abs/2310.08560 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S76 | https://arxiv.org/abs/2510.07172 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S77 | https://arxiv.org/abs/2504.10415 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S78 | https://arxiv.org/abs/2610.37919 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S79 | https://arxiv.org/abs/2609.01552 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S80 | https://arxiv.org/abs/2602.02905 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S81 | https://arxiv.org/abs/2410.07076 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S82 | https://arxiv.org/abs/2503.21248 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S83 | https://arxiv.org/abs/2609.00747 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S84 | https://arxiv.org/abs/2607.15766 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S85 | https://www.nber.org/papers/w35247 | 2026-11-18 | NBER 워킹페이퍼 페이지(서지·초록) | metadata-checked |
| S86 | https://arxiv.org/abs/2609.23178 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A39 | https://arxiv.org/abs/2505.23735 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A40 | https://arxiv.org/abs/2505.23884 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A41 | https://arxiv.org/abs/2412.09764 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A42 | https://arxiv.org/abs/2510.15103 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A43 | https://arxiv.org/abs/2610.14921 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A44 | https://arxiv.org/abs/2411.07279 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A45 | https://arxiv.org/abs/2506.10943 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| E06 | https://arxiv.org/abs/2601.16175 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A46 | https://arxiv.org/abs/2310.14152 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A47 | https://arxiv.org/abs/2405.09673 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A48 | https://arxiv.org/abs/2610.36994 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A49 | https://arxiv.org/abs/2607.23837 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A50 | https://arxiv.org/abs/2610.15492 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A51 | https://arxiv.org/abs/2611.11684 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A52 | https://arxiv.org/abs/2510.25741 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A53 | https://arxiv.org/abs/2506.21734 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A54 | https://arxiv.org/abs/2510.04871 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A55 | https://arxiv.org/abs/2408.03314 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A56 | https://arxiv.org/abs/2412.06769 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A57 | https://arxiv.org/abs/2606.31121 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S87 | https://arxiv.org/abs/2508.19828 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S88 | https://arxiv.org/abs/2611.01747 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S89 | https://arxiv.org/abs/2310.11511 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S90 | https://arxiv.org/abs/2601.03192 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A58 | https://arxiv.org/abs/2001.00689 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A59 | https://arxiv.org/abs/2211.11031 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A60 | https://arxiv.org/abs/2407.09450 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S91 | https://arxiv.org/abs/2610.34767 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A61 | https://arxiv.org/abs/2504.13171 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S92 | https://arxiv.org/abs/2606.09483 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S93 | https://arxiv.org/abs/2610.24453 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S94 | https://arxiv.org/abs/2610.12124 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A62 | https://arxiv.org/abs/1705.08690 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A63 | https://doi.org/10.1038/s41467-022-34938-7 | 2026-11-18 | DOI 레지스트리 레코드(서지만) | metadata-checked |
| A64 | https://arxiv.org/abs/2307.13269 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A65 | https://arxiv.org/abs/2506.06105 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A66 | https://arxiv.org/abs/2506.06266 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S95 | https://arxiv.org/abs/2608.05475 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A67 | https://arxiv.org/abs/2408.15237 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S96 | https://arxiv.org/abs/2606.17289 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S97 | https://arxiv.org/abs/2611.03617 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S98 | https://arxiv.org/abs/2609.14917 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S99 | https://arxiv.org/abs/2610.03092 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S100 | https://arxiv.org/abs/2611.14514 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S101 | https://arxiv.org/abs/2610.26955 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| E07 | https://arxiv.org/abs/2511.02824 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| E08 | https://arxiv.org/abs/2502.18864 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| E09 | https://arxiv.org/abs/2504.08066 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| E10 | https://arxiv.org/abs/2610.08927 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S102 | https://arxiv.org/abs/2304.03442 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S103 | https://arxiv.org/abs/2401.18059 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S104 | https://arxiv.org/abs/2303.11366 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S105 | https://arxiv.org/abs/2409.07429 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S106 | https://arxiv.org/abs/2406.04271 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S107 | https://arxiv.org/abs/2305.16291 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S108 | https://arxiv.org/abs/2610.19386 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S109 | https://arxiv.org/abs/2611.12120 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S110 | https://arxiv.org/abs/2608.15451 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S111 | https://arxiv.org/abs/2610.25119 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S112 | https://arxiv.org/abs/2311.06668 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S113 | https://arxiv.org/abs/2308.10248 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S114 | https://arxiv.org/abs/2610.00526 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S115 | https://arxiv.org/abs/2610.41743 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S116 | https://arxiv.org/abs/2501.09240 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| A68 | https://arxiv.org/abs/2610.38796 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S117 | https://arxiv.org/abs/2610.29357 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S118 | https://arxiv.org/abs/2512.13564 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| E11 | https://arxiv.org/abs/2611.05108 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S119 | https://openlibrary.org/isbn/0262121166 | 2026-11-18 | 도서 레지스트리 레코드(서지만) | metadata-checked |
| S120 | https://doi.org/10.1353/pbm.1986.0087 | 2026-11-18 | DOI 레지스트리 레코드(서지만) | metadata-checked |
| S121 | https://arxiv.org/abs/1905.11481 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S122 | https://arxiv.org/abs/2107.14351 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| E12 | https://arxiv.org/abs/2404.18400 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S123 | https://arxiv.org/abs/2610.37649 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S124 | https://arxiv.org/abs/2611.03713 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S125 | https://arxiv.org/abs/2610.18938 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S126 | https://arxiv.org/abs/2609.30199 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S127 | https://arxiv.org/abs/2605.22681 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S128 | https://arxiv.org/abs/2610.05197 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S129 | https://arxiv.org/abs/2609.07611 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S130 | https://arxiv.org/abs/2409.04109 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S131 | https://arxiv.org/abs/2403.03230 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S132 | https://arxiv.org/abs/2610.37739 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S133 | https://arxiv.org/abs/2406.06769 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S134 | https://arxiv.org/abs/2407.01725 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S135 | https://arxiv.org/abs/2410.05080 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S136 | https://arxiv.org/abs/2512.15567 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S137 | https://arxiv.org/abs/2501.01540 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S138 | https://arxiv.org/abs/2403.07974 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S139 | https://arxiv.org/abs/2406.19314 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| E13 | https://arxiv.org/abs/2501.04227 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| E14 | https://arxiv.org/abs/2610.23839 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| N33 | https://doi.org/10.1016/s0364-0213(83)80009-3 | 2026-11-18 | DOI 레지스트리 레코드(서지만) | metadata-checked |
| N34 | https://doi.org/10.1006/cogp.1993.1013 | 2026-11-18 | DOI 레지스트리 레코드(서지만) | metadata-checked |
| N35 | https://doi.org/10.1016/0010-0285(83)90002-6 | 2026-11-18 | DOI 레지스트리 레코드(서지만) | metadata-checked |
| N36 | https://doi.org/10.1037/0278-7393.25.6.1534 | 2026-11-18 | DOI 레지스트리 레코드(서지만) | metadata-checked |
| N37 | https://doi.org/10.1146/annurev-psych-010213-115154 | 2026-11-18 | DOI 레지스트리 레코드(서지만) | metadata-checked |
| N38 | https://doi.org/10.1037/a0014212 | 2026-11-18 | DOI 레지스트리 레코드(서지만) | metadata-checked |
| N39 | (없음) | 2026-11-18 | 검색 결과(제목·출판 정보만) | needs-resolution |
| S140 | https://arxiv.org/abs/2212.09196 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S141 | https://arxiv.org/abs/2402.08955 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S142 | https://arxiv.org/abs/2604.03877 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S143 | https://arxiv.org/abs/2610.29271 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S144 | https://arxiv.org/abs/2605.11258 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |
| S145 | https://arxiv.org/abs/2111.02080 | 2026-11-18 | arXiv 초록 페이지(제목·저자·v1 날짜·초록 요지) | metadata-checked |

### C-2. 공식 페이지(투고처, 일정·분량)

| 출처 | URL | 접근일 | 읽은 범위 | 확인 수준 |
|---|---|---|---|---|
| ICML 2027 일정 | https://icml.cc/Conferences/2027/Dates | 2026-11-18 | 마감·통지·개최일(분량은 페이지에 없음) | 공식 페이지 확인 |
| ICML 2026 저자 지침 | https://icml.cc/Conferences/2026/AuthorInstructions | 2026-11-18 | 분량·익명·참고문헌 규정 | 공식 페이지 확인(2026 회차) |
| ICLR 2027 저자 지침 | https://iclr.cc/Conferences/2027/AuthorGuidelines | 2026-11-18 | 마감·분량·익명·저자 상한 | 공식 페이지 확인 |
| NeurIPS 2026 일정 | https://neurips.cc/Conferences/2026/Dates | 2026-11-18 | 본 트랙·E&D 마감과 통지 | 공식 페이지 확인 |
| NeurIPS 2026 본 트랙 CFP | https://neurips.cc/Conferences/2026/CallForPapers | 2026-11-18 | 분량 미기재, 핸드북 참조 | 공식 페이지 확인 |
| NeurIPS 2026 Evaluations and Datasets CFP | https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets | 2026-11-18 | 범위·익명·필수 산출물 | 공식 페이지 확인 |
| NeurIPS 2026 E&D 트랙 소개 글 | https://blog.neurips.cc/2026/03/23/introducing-the-evaluations-datasets-track-at-neurips-2026/ | 2026-11-18 | 검색 결과의 제목만 봄(열지 않음) | official-search-checked 수준 |
| ACL Rolling Review 일정 | https://aclrollingreview.org/dates | 2026-11-18 | 주기·commit 일정 | 공식 페이지 확인 |
| TMLR 저자 안내 | https://jmlr.org/tmlr/author-guide.html | 2026-11-18 | 분량·익명·심사 단계 | 공식 페이지 확인 |
| TMLR FAQ | https://jmlr.org/tmlr/faq.html | 2026-11-18 | 12쪽 기준 심사 기간·결정 목표·평가 기준 | 공식 페이지 확인 |
| COLM 2027·CogSci 2027·CoLLAs 2027 | (공식 호출문을 찾지 못함) | 2026-11-18 | 보조 목록의 추정 일정만 봄 | 미확인 |

### C-3. 서지 레지스트리와 접근하지 못한 페이지

| 출처 | URL | 접근일 | 결과 |
|---|---|---|---|
| Crossref 레코드 조회 | https://api.crossref.org/works | 2026-11-18 | DOI 서지 확인(한 번 429, 재조회 성공) |
| Open Library 레코드 | https://openlibrary.org/isbn/0262121166.json | 2026-11-18 | 도서 서지 확인 |
| Project MUSE 논문 페이지 | https://muse.jhu.edu/article/403510 | 2026-11-18 | 검증 챌린지만 표시됨, 읽지 못함 |
| PhilArchive 레코드 | https://dc2.philarchive.org/rec/LANSDC | 2026-11-18 | 403, 읽지 못함 |
| MIT Press 도서 페이지 | https://mitpress.mit.edu/9780262620529/scientific-discovery/ | 2026-11-18 | 403, 읽지 못함 |
| PubMed 레코드 | https://pubmed.ncbi.nlm.nih.gov/3797213/ | 2026-11-18 | 쿠키 안내만 표시됨, 읽지 못함 |
| Nature Machine Intelligence 투고 안내 | https://www.nature.com/natmachintell/submit/article | 2026-11-18 | 인증 리다이렉트, 읽지 못함 |
