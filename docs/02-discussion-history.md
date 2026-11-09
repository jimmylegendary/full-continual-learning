# 02. 논의의 발전, 정정, 보존할 논점

이 문서는 현재 확보한 대화의 **주제별 재구성**이다. 발화 전체의 문자 단위 transcript는 아니다. 정확한 날짜가 없는 발화에 임의 날짜를 붙이지 않는다. 사용자 원문 발췌는 [사용자 요구 원문](../sources/user-statements.md), 22쪽 PDF의 원문 범위는 [출처 안내](../sources/README.md)를 본다.

## T01. 최초 Melete의 의미

단순 사실 회수 대신 경험·조건·목표·판단·행동·결과·예외·정정 이력을 보존하고, 모델이나 도구가 바뀌어도 조건부 판단 방식을 이어가는 개인 기억이다. 새 기술 검토에는 작은 실험을 선호하고 장애에는 우선 복구하는 두 패턴을 ‘신중하다/행동 우선’ 한 문장으로 평균내지 않는다.

처음에는 Frozen LLM에 외부 neural memory의 working graph/frame를 전달하는 방향이었다. 경험→패턴→현재 문제 해석→필요 부분만 깊은 사고→예상 밖 경험으로 수정이라는 장기 목적이 있었다.

## T02. 구조를 사람이 고정하기보다 AI가 개선하게 할 것인가

사용자는 vec2text의 효과와 직접 설계의 불확실성 때문에 작은 시작점에서 evolutionary하게 고도화하는 접근을 제안했다. 필수 구성은 objectives, 수치 verification/benchmark, negative feedback/evolution, operation policy였다.

논의에서는 (a) 실제 경험에 의한 memory state 학습, (b) AI가 architecture·code·update policy를 개선하는 개발 진화, (c) 진화 절차 자체의 개선을 분리했다. 복잡성 증가는 목표가 아니라 비용을 정당화할 효과가 있을 때 허용하는 결과다. 평가기는 후보와 독립되어야 하며 dev 성능을 올리기 위해 정답·split·채점기를 바꾸면 안 된다.

## T03. 기억 버전·스위치·다층 이해

첨부 PDF는 기억의 업데이트와 행동에 사용할 기억 선택이 다를 수 있다는 논의에서 출발한다. 과거 사건, 현재의 기대, 현재 질문의 인출을 분리했다. 2020년에 맛있었던 식당이 2026년에 달라졌다고 과거 사건이 틀린 기억이 되지는 않는다.

사용자는 익숙한 것과 연결해 배우는 과정, 개인마다 다른 익숙함, 개념을 여러 층위로 분해해 관계를 찾는 능력을 강조했다. 분해 자체보다 역할·관계·원리로 다시 묶고 새 사례에 대응시키는 과정이 중요하다고 정리했다.

친숙성(전에 봄), 이해/구조 재사용(아는 관계와 연결), 숙련/자동화(노력 감소)를 구분했다. PDF는 두 번째 긴 답변이 누락된 **부분 원문**이므로 그 답변을 복원한 것처럼 취급하지 않는다.

## T04. Schema가 중심 개념이라는 재정의

경험은 사건·결과, schema는 재사용할 관계와 조건, 직관은 그 구조가 빠르게 활성화되어 나오는 잠정 판단으로 구분했다. 이미 있는 구조가 새 학습에 필요한 자유도를 줄인다는 가설을 제시했다.

사용자의 ‘LLM에는 schema가 없다’는 직관은 목적의 표현으로 보존하되 과학적 사실로 채택하지 않는다. ICL/function vectors 등은 LLM 내부 재사용 표상의 반례다. 부족함은 특정 사용자의 새 경험이 세션 간 유지되고 수정되며 다음 학습을 바꾸는 경로의 부재로 더 정확히 쓸 수 있다.

## T05. SBL 문헌과 표현 형식의 분류

Symbolic, continuous neural, discrete latent/structured probabilistic, hybrid를 구분했다. latent가 continuous라는 뜻은 아니다. CSCG/Hidden Schema Networks/S-HAI의 확률값이 실수라는 이유로 연속 schema로 분류하지 않는다. continuous representation과 continual learning은 직교 축이다.

직접 SBL 연구와 cognitive map/latent-cause/world model 등 인접 연구를 분리하고, 일반 memory/RAG 논문을 이름만으로 SBL에 포함하지 않는다. 최초 공개일, 개정일, 학회 연도, 코드 상태를 각각 기록한다. 추적 대상 전체는 [문헌 목록](../references/README.md)에 보존한다.

## T06. Titans + HOPE + Sleep을 SBL 재료로 사용

사용자는 neural memory의 빠른 업데이트, CMS의 여러 시간척도, Sleep의 통합을 schema 형성·활용·rapid learning·빠른 판단으로 사용하자고 제안했다. 이를 위해 이론과 수식, 실험 PoC까지 원했다.

학습에는 외부 사람이 붙인 정답이 없을 수 있지만 다음 관측·과제 결과·정정·reward 등 학습 신호는 필요하다. self-generated 설명을 독립 사실 검증으로 승격하지 않는다. KV reconstruction과 실제 판단 개선의 목적함수를 구분한다.

이 시점의 합성 Phase-0은 low-dimensional prior를 학습해 few-shot 회귀를 개선하는 실험이었다. 모델별 비교·oracle·negative control을 갖지만 언어 이해, 자율 schema 수 발견, 기억 전환, Sleep, neural update, 추론 지연을 입증하지 않았다.

## T07. 중요한 사용자 정정: 별도 System 1이 아니라 통합 모델

초기 제안에는 작은 외부 fast predictor와 별도 LLM fallback이 있었다. 사용자는 최종 구조가 **System ONE 통합 HOPE + recursive forward**임을 명확히 했다.

기존 LLM의 sequence layer는 Titan-Llama, FFN은 CMS로 점진적 전환하고 나중에 외부 schema offload/versioning/retrieval을 붙인다. schema 판단 MLP/구조도 처음부터 전제한다. 따라서 별도 작은 모델을 최종 목표로 되돌리는 것은 정정 전 해석으로의 퇴행이다.

이 정정 후 대표 PoC는 ‘경험 후 새 관계 공유 사례에서 동일 정확도에 필요한 loop와 총 계산량 감소’로 바뀌었다. 이전 covariance 실험은 진입 근거일 뿐 통합 모델의 PoC로 이름을 바꾸지 않는다.

## T08. 입력의 낯섦, 학습량, 계산량의 구분

익숙한 규칙의 긴 합성은 많은 계산이 필요할 수 있고, 낯선 이름의 binding은 적은 학습만 필요할 수 있다. controller는 schema 선택·쓰기 정책·추가 계산의 가치·종료 판단을 따로 출력할 수 있어야 한다.

같은 입력을 여러 번 loop한 횟수와 새로운 경험의 수가 다르다. 기억 재조회, gradient step, token position, optimizer clock, 통합 시점도 분리한다. 원 Titan 코드의 token position 전진과 state write를 recursive depth에 그대로 적용하지 않는다.

## T09. 뇌파와 CMS의 본질적 재검토

사용자는 감정·노력·집중·수면·익숙함에 따라 여러 주파수가 동시에 또는 순차적으로 나타날 수 있다는 직관에서 고정 token 주기를 넘어 탐구하자고 했다.

논의에서는 주파수, 진폭/power, burst, 상대 위상, 영역 간 coupling, eligibility를 분리했다. EEG/LFP는 시냅스 변경 횟수의 계측기가 아니다. 높은 주파수=빠른 학습=단기기억, 낮은 주파수=느린 학습=장기기억의 등식도 채택하지 않는다.

공학적 전환은 읽기·활성화·학습 후보·쓰기·통합·정보 교환의 조율이다. 명시적 oscillator/phase는 가설이며 사건 기반 readiness controller보다 나은지 따로 평가한다. 디지털 동기 실행에서 단순 단계 번호와 같은 효과라면 새 원리로 과장하지 않는다.

## T10. Loop/MoD/MoR/depth attention과 6층위 의도

사용자는 이 재료들을 학습 조율과 결합해 (1) 문맥별 schema 선택·rapid update와 (2) 경험에 의한 빠르고 편향된 추론부터 깊은 사고·통찰까지 달성하고자 했다. 표면 요구에서 meta의 meta까지 의도를 이해해 달라고 했다.

핵심 정리는 경험→schema→계산 배분/학습 정책→새 경험→schema 갱신이다. Depth read는 이번 문제의 중간 표현, persistent memory는 다음 문제에도 남는 경험 구조다. 사고 도중 schema를 재선택하거나 조합할 수 있어야 한다. 토큰 단위 router만으로 문맥 수준 구조 이해를 대체하지 않는다.

## T11. 2026-11-09 주간 조사

새로운 참고점으로 schema 압축과 예외 학습, 표현 안정화와 과제 구조 형성의 시간차, selective write, episodic 재구성과 판단의 간극, 저랭크 recurrent scaffold, task schema와 binding 분리, stable schema/upstream plasticity가 제시됐다. 문헌별 수치와 한계는 [주간 보고 아카이브](../research/2026-11-09-sbl-tracking.md)에 보존한다. 과거 답변에 실린 수치를 이번 업로드에서 독립 재현한 것처럼 표시하지 않는다.

## 보존해야 할 정정표

| 이전 표현/가능한 오해 | 현재 해석 |
|---|---|
| LLM은 schema가 없다 | 구조적 표상은 존재할 수 있다. 지속되는 경험별 학습을 연구한다 |
| schema=경험=직관 | 사건, 재사용 구조, 빠른 적용을 구별한다 |
| 작은 fast 모델 + 큰 LLM이 최종 목표 | 같은 모델의 가변 계산·학습 모드가 최종 방향 |
| 느린 CMS는 덜 계산한다 | forward 참여, update 빈도, retention은 별개 |
| 내부 loop는 새 관측이다 | 사고 반복은 증거 수를 늘리지 않는다 |
| fast weight가 저장되면 schema 성공 | 새 사례 전이와 causal intervention 필요 |
| vec2text를 반드시 성공시켜야 함 | 학습된 latent interface/모델 내부 연결도 가능 |
| 뇌파를 token update period로 복제 | 상태·내용·결합·가소성의 조율이 연구 대상 |
| 깊은 loop가 통찰 | 새 구조와 이후 전이가 있어야 한다 |
| pretraining=하나의 schema, RL=분화가 사실 | 반증 가능한 별도 후속 가설 |
| 사용자가 원한 모든 수치 기준이 확정 | 수치 gate와 phase 세부는 proposal임을 표시 |
