# 03. SBL·인지·기억의 이론 기반

이 문서는 업로드된 뇌과학 대화 PDF와 후속 논의의 이론을 정리한다. 실험 사실, 계산이론, 제품 가설은 다른 증거 수준이다. [참고문헌](../references/README.md)의 N/S 식별자를 사용한다. PDF의 14–18쪽 이론 표가 원자료의 핵심 조직이다.

## 1. Schema의 운영적 정의

여러 경험에 걸쳐 재사용되며 새로운 사례의 예측·판단·학습에 필요한 정보와 계산을 줄이는 **조건부 관계 구조**. 하나의 벡터, graph node, MLP, 특정 시냅스 집합과 일대일 대응한다고 가정하지 않는다.

**PROPOSAL ([2026-11-11-sbl-fulltext-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext-review.md#5-fcl-설계의-시작점-proposal) 출발점 1):** retrofit LLM에서는 schema를 모듈이 아니라 측정 가능한 성질로 다룬다. 조작적 증거는 세 가지다: 같은 구조의 문제들에 걸친 활동 subspace 재사용(GOUDAR23의 demixing·participation ratio), 새 같은-구조 과제에서의 가중치·상태 변화량 감소, 해당 표현을 제거·교체했을 때 구조 전이만 선택적으로 사라짐. 구현이나 채택 결정이 아니다.

**LITERATURE (TEM20·SWAMI23·SPENS24·GOUDAR23·CHU25·SPECTRUM26, 원문 검토 §5 출발점 1):** 문헌은 느린 구조 파라미터(TEM20의 W, SWAMI23의 CSCG T, SPENS24의 VAE)와 활동 subspace·attractor regime(GOUDAR23, CHU25, SPECTRUM26)이라는 두 정의를 모두 지지한다. **OPEN:** 어느 쪽이 retrofit LM에 맞는지는 문헌에 우열 증거가 없다.

**LITERATURE (CHU25, W2-chu25-goudar23.md:138-141):** 본문 기준으로 unshaped 망이 shaped 망보다 더 저차원이었다(top-3 PC 분산비 93% 대 82.5%, 그림마다 값이 다르다). **PROPOSAL:** 저차원성·압축 자체를 구조 형성의 증거로 보지 않는다. **ARCHIVE (S20, 2026-11-09-sbl-tracking.md:19-23):** 11-09 기록의 가설 A도 같은 방향이며 확인 깊이는 official-search-checked다.

경험은 관측·행동·결과의 사건이다. Schema는 공통 관계와 적용 조건이다. 직관은 관련 구조가 빠르게 활성화되어 형성하는 잠정 판단이다. 많은 경험의 단순 빈도, 익숙한 문자열, 높은 certainty만으로 유효한 schema를 정의하지 않는다. [N23,N24]

‘정답 없는 학습’은 외부 gold label 없이 관측을 예측하거나 피드백에서 배우는 것을 포함한다. 학습 신호가 전혀 없는 최적화를 뜻하지 않는다. 구조 학습은 경험학습의 중요한 부분이지만 모든 사건 기억·기술·가치 학습을 무조건 schema라고 부르지 않는다.

## 2. 원자료에서 다룬 13개 이론·회로

| 항목 | 질문과 원리 | Melete로 옮길 가설 | 한계 |
|---|---|---|---|
| CLS | 빠른 사건 기억과 안정적인 공통 구조 학습의 보완 [N11,N12] | fast state와 slow consolidation | 해마=항상 빠름, 피질=항상 느림은 절대 법칙 아님 |
| SBL | 기존 지식이 새 정보의 조직·통합을 돕는다 [N12,N13,N23] | 관련 schema가 sample efficiency 향상 | schema에 맞지 않는 것도 학습 가능. **LITERATURE (HWU20, W1-spens24-hwu20.md:278,342,350):** 신경망 구현에서도 새 연합은 epoch을 늘린 조건에서 빨리 배웠지만 새 schema는 기존 schema보다 빨리 배우지 않았음 |
| Hippocampal match–mismatch | 대상이 익숙해도 관계/순서의 예측 위반 감지 [N14] | relation novelty와 표면 novelty 분리 | 단일 임계값이 모든 학습을 제어한다고 보지 않음 |
| Retrieval-mediated integration | 관련 과거 기억을 새 학습의 재료로 재활성화 [N02] | 여러 경험을 연결한 새 관계 형성 | raw 과거 파일을 그대로 복사한다는 주장은 아님 |
| Reconsolidation | 일부 재활성화 조건에서 기억이 가소적으로 변함 [N04,N05] | read 이후 선택적 revision | 모든 read가 overwrite는 아님 |
| Latent-cause inference | 같은 원인 수정과 다른 상황 분리를 구별 [N07] | accommodation/split/switch | 계산모델이지 특정 회로의 알고리즘 확정 아님 |
| Familiarity/recollection | 이전 접촉의 느낌과 맥락 회상을 구별 [N15,N16] | 친숙함과 이해·정확도 분리 | 해마/주위 피질의 완전 분업에는 논쟁 |
| Structure-mapping | 표면이 달라도 역할과 관계를 대응 [N17] | 역할 재결합·관계 전이 | 비유의 적용 범위를 확인해야 함 |
| Chunking/expertise | 여러 요소를 의미 있는 단위와 원리로 조직 [N18,N19] | 다층 추상화와 계산 절약 | 분해만 하고 재조직하지 않으면 부족 |
| Automaticity | 연습으로 의식적 통제 부담 감소 [N20] | 경험 후 동일 품질의 계산 감소 | ‘해마가 사고를 끈다’는 단일 스위치 아님 |
| TEM/cognitive map | 감각 내용과 재사용할 구조를 분리·결합 [N21,S01] | latent scaffold와 빠른 binding | 공간 실험을 범용 언어 성공으로 확대하지 않음. **LITERATURE (TEM20, W4-tem20-kumar26.md:72-73,112,117-120,175):** 논문은 schema라는 말을 쓰지 않고(structural knowledge) 구조와 내용의 분리는 고정 W_repeat/W_tile 같은 아키텍처 prior와 학습 분포가 만든 것이며 구조는 바깥 루프에서만 형성되고 빠른 기억 M은 환경마다 0으로 리셋되고 구조 선택·수정 실험은 없음 |
| vmPFC→MEC 조직화 | 맥락·시간에 따른 기억 연결/분리의 회로 조절 [N22] | shared/isolated memory 선택 | 특정 생쥐 실험의 범위 |
| MS→MEC 기억 선택 | 업데이트 전후 기억의 행동 표현 전환 [N03] | learn와 use 분리, ABA 재사용 | universal memory version controller 아님 |

## 3. 구체 예시

- **개별 사건 vs 기대:** 예전 식당 경험은 보존하면서 주방장 변경 뒤 현재 기대를 수정할 수 있다. 과거 질문에는 이전 경험, 현재 의사결정에는 최신 조건, 원인 분석에는 둘 다 사용한다.
- **새 관계:** A–B와 B–C를 서로 다른 때 배운 뒤 A–C를 추론한다. 현재 입력뿐 아니라 재활성화한 기억이 학습 재료다.
- **상황 분리:** 공사 중 길이 느려진 것과 평소 길이 영구적으로 느려진 것을 다르게 처리한다.
- **다층 이해:** 장애 사례를 사건, 요소와 역할, 관계, 적용 조건, 일반 원리로 재표현한다. 다른 시스템에서 표면 이름이 달라도 같은 관계를 찾을 수 있어야 한다.
- **원리 분류:** 에너지 보존을 적용할 문제를 경사면/스프링이라는 외형보다 공통 원리로 묶는 것과 유사한 전이를 평가한다.

## 4. 실제 뇌에서 표현된다는 말의 네 수준

1. 인지적 내용: 역할·관계·절차·예상.
2. 물리적 기반: 신경세포, 시냅스, 회로 특성.
3. 활성 상태: 집단 발화, 시간적 궤적, 맥락 의존적 패턴.
4. 분석 언어: 벡터, 부분공간, manifold, attractor.

세포군의 활동을 벡터로 분석한다고 뇌가 같은 좌표축의 배열을 저장하는 것은 아니다. 시냅스 기반과 continuous representation은 배타적 대안이 아니다. 연속 공간 안에 이산적인 안정 상태나 전이 구조가 공존할 수 있다. [S03,S05,N25–N30]

관찰 범위: 이야기의 공통 사건 구조에 대한 fMRI, 추상 맥락의 인간 단일 뉴런 기하학, 원숭이의 decision/stimulus subspace, 생쥐 회로 조작은 서로 다른 증거다. 상관·pseudo-population·제한 과제 결과를 뇌 전체의 범용 코드로 확대하지 않는다.

**LITERATURE (CHU25, W2-chu25-goudar23.md:152-153,171; 원문 검토 §2):** 모형과 쥐 OFC의 표상 기하 상관은 r≈0.90이지만 shaping 없는 망도 약 0.85이고, 다른 그림(S7b)은 0.80–0.85로 값이 일치하지 않는다. **PROPOSAL (W2-chu25-goudar23.md:208):** 뇌 데이터와의 상관을 schema 형성의 PASS gate로 쓰지 않고 oracle 구조 RDM과 행동 지표를 함께 본다.

## 5. Schema 처리의 기능적 루프

입력/목표 → 관련 구조 활성화 → 현재 대상의 binding → 기대/판단 → 관측과 비교 → 유지·수정·전환·분리·조합 → 미래 사용.

이것은 고정 직렬 뇌 회로도가 아니다. 빠른 관측 학습과 offline replay가 모두 가능하고, 사고 도중 적용 schema를 바꿀 수 있다. 하나의 novelty scalar만으로 모든 선택을 정하지 않는다.

## 6. 표현 방식과 학습 지속성의 분리

| 표현 | 예 | 반드시 따로 물을 것 |
|---|---|---|
| 명시적 symbolic | 규칙·graph·프로그램 | 규칙 형성과 검증, 온라인 수정 여부 |
| discrete latent | CSCG, 확률적 hidden-state graph | 보이지 않는 변수라고 연속 공간은 아님 |
| continuous neural | weights, distributed activations, manifold, dynamics | activation에만 있는지 파라미터/저장 상태에 남는지 |
| hybrid | neural representation + 이산 context inference | 어떤 부분이 연속/이산/고정/가변인지 |

연속 확률값, softmax, Gumbel-Softmax를 쓴다고 schema 자체가 연속 신경 구조가 되는 것은 아니다. ICL의 context 적응, 세션 간 state 보존, slow weight 학습도 구별한다.

**USER (U-T05):** schema를 symbolic으로 두는 것과 latent space에 표현하는 것을 구분해서 보고하되 후자에 더 관심이 있다. **PROPOSAL:** 이 문서군의 1차 대상은 continuous latent schema, 곧 학습 가능한 파라미터·fast state·활성 상태에 놓인 재사용 가능한 관계·조건·계산 구조다. symbolic graph/program schema와 discrete latent는 비교군과 경계 사례로 쓴다([08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md)의 명시적 graph/program schema 비교군). 이 우선순위는 설계 기본값이며 이산 구조의 필요성을 배제하지 않는다. continuous representation은 continual learning이 아니므로 세션 간 state 보존과 slow weight 학습은 따로 검증한다. **OPEN:** hybrid 구현에서는 어느 부분이 연속·이산·고정·가변인지 구현마다 표시한다.

**PROPOSAL:** 읽은 논문은 위 표의 어느 칸인지 논문별로 따로 분류하며, 아래 분류 라벨(연속·hybrid·이산)은 우리의 정리이고 ELDER26·SWAMI23의 hybrid는 W7-remediation.md:341,362에서 PROPOSAL로 표시됐다. **LITERATURE (SPENS24·GOUDAR23·SPECTRUM26·HWU20·ELDER26·SWAMI23, 원문 검토 §3 "schema가 있는 곳"):** SPENS24는 VAE 가중치와 연속 latent(W1-spens24-hwu20.md:69), GOUDAR23은 가중치가 아니라 집단 활동의 저차원 decision subspace(W2-chu25-goudar23.md:281), SPECTRUM26은 분산 표현의 추상화 수준 스펙트럼이며 추상화의 측정법이 없다(W5-spectrum26-structk25.md:72-76). HWU20은 이긴 mPFC 뉴런 1개의 이산 id와 고정 희소 mask와 연속 가중치(W1-spens24-hwu20.md:238-242), ELDER26은 입력 쪽 연속 특징 위에 얹힌 출력 쪽 거의 디지털한 AND형 배선(W3-elder26-miconi25.md:70-71), SWAMI23은 CSCG의 잠재 전이 그래프 T이며 rebinding은 학습에서 창발한 것이 아니라 설계된 test-time 알고리즘이다(W6-swami23-metadata-gap.md:36-37,88, 원문 검토 §2).

**ARCHIVE (S18·S27, 2026-11-09-sbl-tracking.md:80-84; 확인 깊이 official-search-checked):** symbolic/discrete 비교점으로 graph schema(S18, latent graph·slot·transition이며 continuous neural이 아님)와 agentic program induction(S27, persistent executable program)을 둔다. S27의 ARC-AGI-3 향상 보고는 특정 harness·평가 범위이며 neural schema의 증거가 아니다.

## 7. 문헌을 적용하는 기준

TEM, Goudar의 neural subspace, Chu의 sequence attractor, Yoshida의 manifold/replay, Spens의 generative consolidation, Kumar의 one-shot binding은 서로 다른 역할을 보여준다. 하나의 논문이 형성·선택·수정·rapid learning·연속 운영·속도 이득을 모두 입증했다고 합치지 않는다. 상세 카탈로그는 [참고문헌](../references/README.md), 최신 보완은 [주간 조사](../research/2026-11-09-sbl-tracking.md)를 본다.

**LITERATURE (11편 전체, [2026-11-11-sbl-fulltext-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext-review.md#4-논문을-가로지르는-관찰) §4.1):** 원문으로 읽은 11편 어디에서도 학습된 schema 구조가 같은 예산의 고정·무구조 대조보다 낫다는 직접 비교를 찾지 못했다. HWU20은 구조 없는 변형(mPFC 크기 1)이 비중첩 schema에서 gating 변형보다 높았고(≈0.9–0.95 대 ≈0.65, 그림 판독, W1-spens24-hwu20.md:311), GOUDAR23은 입력 척도를 조정하면 순환 가중치를 동결한 망도 완전 가소 망과 비슷했으며(W2-chu25-goudar23.md:364), ELDER26은 hidden이 크면 backprop MLP가 더 높았다(W3-elder26-miconi25.md:98). SPENS24는 미학습 encoder 한 점(epoch 0)뿐이고(W1-spens24-hwu20.md:119), CHU25·TEM20·KUMAR26·SWAMI23·MICONI25에는 고정 무작위 순환·비분해·learned-vs-given·LIALT baseline·비가소 RNN 같은 대조가 없다.

**ARCHIVE (Melete N0–N5 기록, [12-melete-lineage.md](/home/jimmy/repos/full-continual-learning/docs/12-melete-lineage.md):22):** Melete에서도 root budget이 같은 trained graph 대 frozen graph의 추가 개선은 0.48%(대략 95% 구간 −3.07~4.04%)로 독립 기여가 입증되지 않았다.

**PROPOSAL (원문 검토 §4.1):** FCL의 모든 schema 기제 실험은 같은 계산·갱신 예산의 고정/무구조/항상-갱신 대조와 함께 판정한다([08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md) §4).

**USER (2026-11-11, 원문 검토 서두):** 외부 SBL 요약의 세부 논문을 원문 전체로 읽고 생각의 시작점으로 삼자는 요청에 따라, 위에서 든 문헌 중 Yoshida를 뺀 다섯 편(TEM·Goudar·Chu·Spens·Kumar)에 Hwu·Elder·Miconi·Swaminathan과 리뷰·관점 2편(STRUCTK25·SPECTRUM26)을 더한 11편(구현·모형 9편, 리뷰·관점 2편)을 원문으로 다시 읽었다. 외부 요약의 정정, 학습된 구조와 고정·무구조 대조의 비교 부재, "새로움이 학습을 바꾼다"의 서로 다른 구현 형태는 [2026-11-11-sbl-fulltext-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext-review.md)에 정리했다.

**LITERATURE (HWU20·CHU25·ELDER26·KUMAR26·MICONI25·SWAMI23, [2026-11-11-sbl-fulltext-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext-review.md#2-외부-요약-검증-결과) §2):** 외부 요약(ChatGPT 조사 요약)을 원문과 대조해 정정한 여섯 가지다. **PROPOSAL:** 이 표현들은 설계 근거로 다시 쓰지 않는다.

- **LITERATURE (HWU20, W1-spens24-hwu20.md:19-23):** novelty·familiarity가 바꾸는 것은 학습률이 아니라 공고화 replay epoch 수다.
- **LITERATURE (CHU25, W2-chu25-goudar23.md:25,182):** "연속시간 RNN"은 τ=1, Δt=1이라 사실상 이산시간이다.
- **LITERATURE (ELDER26, W3-elder26-miconi25.md:21,175):** 고정되는 쪽은 출력 쪽 hidden layer(HL1·HL2)이고 갱신되는 쪽은 입력 쪽 가중치(IL)다.
- **LITERATURE (KUMAR26, W4-tem20-kumar26.md:381-382,397):** "fully neural"은 부분적으로만 맞다(NAVIGATE는 backprop 사전학습 뒤 고정, gating의 WTA·곱셈은 알고리즘 구현).
- **LITERATURE (MICONI25, W3-elder26-miconi25.md:313-316):** 초록의 예시와 달리 실제 설계는 ABCD+EFGH이고 연결쌍 D>E를 4 trial 제시한다.
- **LITERATURE (SWAMI23, W6-swami23-metadata-gap.md:91):** "LLM에서도 같은 기제"는 저자들이 "We conjecture"라 쓴 추측이며 transformer 실험은 없다.
