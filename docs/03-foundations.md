# 03. SBL·인지·기억의 이론 기반

이 문서는 업로드된 뇌과학 대화 PDF와 후속 논의의 이론을 정리한다. 실험 사실, 계산이론, 제품 가설은 다른 증거 수준이다. [참고문헌](../references/README.md)의 N/S 식별자를 사용한다. PDF의 14–18쪽 이론 표가 원자료의 핵심 조직이다.

## 1. Schema의 운영적 정의

여러 경험에 걸쳐 재사용되며 새로운 사례의 예측·판단·학습에 필요한 정보와 계산을 줄이는 **조건부 관계 구조**. 하나의 벡터, graph node, MLP, 특정 시냅스 집합과 일대일 대응한다고 가정하지 않는다.

경험은 관측·행동·결과의 사건이다. Schema는 공통 관계와 적용 조건이다. 직관은 관련 구조가 빠르게 활성화되어 형성하는 잠정 판단이다. 많은 경험의 단순 빈도, 익숙한 문자열, 높은 certainty만으로 유효한 schema를 정의하지 않는다. [N23,N24]

‘정답 없는 학습’은 외부 gold label 없이 관측을 예측하거나 피드백에서 배우는 것을 포함한다. 학습 신호가 전혀 없는 최적화를 뜻하지 않는다. 구조 학습은 경험학습의 중요한 부분이지만 모든 사건 기억·기술·가치 학습을 무조건 schema라고 부르지 않는다.

## 2. 원자료에서 다룬 13개 이론·회로

| 항목 | 질문과 원리 | Melete로 옮길 가설 | 한계 |
|---|---|---|---|
| CLS | 빠른 사건 기억과 안정적인 공통 구조 학습의 보완 [N11,N12] | fast state와 slow consolidation | 해마=항상 빠름, 피질=항상 느림은 절대 법칙 아님 |
| SBL | 기존 지식이 새 정보의 조직·통합을 돕는다 [N12,N13,N23] | 관련 schema가 sample efficiency 향상 | schema에 맞지 않는 것도 학습 가능 |
| Hippocampal match–mismatch | 대상이 익숙해도 관계/순서의 예측 위반 감지 [N14] | relation novelty와 표면 novelty 분리 | 단일 임계값이 모든 학습을 제어한다고 보지 않음 |
| Retrieval-mediated integration | 관련 과거 기억을 새 학습의 재료로 재활성화 [N02] | 여러 경험을 연결한 새 관계 형성 | raw 과거 파일을 그대로 복사한다는 주장은 아님 |
| Reconsolidation | 일부 재활성화 조건에서 기억이 가소적으로 변함 [N04,N05] | read 이후 선택적 revision | 모든 read가 overwrite는 아님 |
| Latent-cause inference | 같은 원인 수정과 다른 상황 분리를 구별 [N07] | accommodation/split/switch | 계산모델이지 특정 회로의 알고리즘 확정 아님 |
| Familiarity/recollection | 이전 접촉의 느낌과 맥락 회상을 구별 [N15,N16] | 친숙함과 이해·정확도 분리 | 해마/주위 피질의 완전 분업에는 논쟁 |
| Structure-mapping | 표면이 달라도 역할과 관계를 대응 [N17] | 역할 재결합·관계 전이 | 비유의 적용 범위를 확인해야 함 |
| Chunking/expertise | 여러 요소를 의미 있는 단위와 원리로 조직 [N18,N19] | 다층 추상화와 계산 절약 | 분해만 하고 재조직하지 않으면 부족 |
| Automaticity | 연습으로 의식적 통제 부담 감소 [N20] | 경험 후 동일 품질의 계산 감소 | ‘해마가 사고를 끈다’는 단일 스위치 아님 |
| TEM/cognitive map | 감각 내용과 재사용할 구조를 분리·결합 [N21,S01] | latent scaffold와 빠른 binding | 공간 실험을 범용 언어 성공으로 확대하지 않음 |
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

## 7. 문헌을 적용하는 기준

TEM, Goudar의 neural subspace, Chu의 sequence attractor, Yoshida의 manifold/replay, Spens의 generative consolidation, Kumar의 one-shot binding은 서로 다른 역할을 보여준다. 하나의 논문이 형성·선택·수정·rapid learning·연속 운영·속도 이득을 모두 입증했다고 합치지 않는다. 상세 카탈로그는 [참고문헌](../references/README.md), 최신 보완은 [주간 조사](../research/2026-11-09-sbl-tracking.md)를 본다.

2026-11-11에 이 중 신경망 구현 11편을 원문으로 다시 읽었다. 외부 요약의 정정, 학습된 구조와 고정·무구조 대조의 비교 부재, "새로움이 학습을 바꾼다"의 서로 다른 구현 형태는 [2026-11-11-sbl-fulltext-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext-review.md)에 정리했다.
