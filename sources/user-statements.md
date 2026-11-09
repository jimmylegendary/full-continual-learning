# 사용자 연구 요구 원문

현재 대화에서의 연구 방향을 정한 발화들을 보존한다. 의미를 고치지 않았고 보기 위한 빈 줄·문단만 정리했다. 모든 assistant 답변/도구 로그를 포함한 완전한 채팅 export는 아니다. 발화 날짜가 없는 항목에는 날짜를 추정해 붙이지 않는다.

## U-T01 — Melete 회상

> 내가 만드는 melete알지? 그거 컨셉, 목적 읊어봐

## U-T02 — Self-evolution

내 github에 melete가 진행이 많이 되었잖아? 근데 만들다 보니 생각이 드는게 이 구조를 내가 만드는게 맞나? AI를 통해 self evolution하면서 개선되는 시스템을 만드는게 어떨까? 하는 생각.

지금 일단 당장 뭔가 melete구현해서 하는데 있어서도 model 수정 없이 하다보니 vec2text에 대한 부분이 잘 될거같은 기대감도 부족하기도 하고

그래서 가장 간단하게 시작할 수 있게 하고 그 방식이 점점 고도화되고 복잡해지고 개선되는 방향으로 evolutionary하게 만들고 싶은 것임

이를 위해서

- 명확한 objectives
- 숫자로 환산되는 verification(benchmark set 포함)
- negative feedback & evolution system
- operation policy

이걸 확정해서 시스템을 만들어 볼까 함

일단 이 방식 자체에 대해서 리뷰해서 의견줘봐

## U-T03 — 뇌과학 PDF를 기반으로

> 이거 읽고 우리 제품의 base 근거로 삼고싶음. 일단 읽고 이해해서 내 의도를 파악해봐

첨부: `neuroscience_conversation_available_originals(1).pdf`.

## U-T04 — Schema라는 핵심 발견

너의 설명을 듣고 보니 내가 원하던건 결국 schema based learning을 하고싶었나봐. 이게 곧 경험이자 직관이라고 생각했나봐. 기존 llm은 이런 schema가 없고 그래서 rapid learning이나 빠른 판단이 안된다고 느낀듯. 너가볼때도 melete의 핵심은 schema라고 생각해?

## U-T05 — 독립 주간 추적과 연구 질문

별도의 세션에 schema based learning을 AI model의 근간 이론으로 제시하는 논문을 앞으로 매주마다 트래킹해서 보고하도록해줘. 보고시 schema를 symbolic으로 하는거랑 latent space(continual space)에 표현하는거랑 구분해서 보고좀. 나는 후자에 더 관심이 있긴함

그리고 여기 답변에는

1. 뇌과학, 실제 뇌에서 schema는 어떻게 표현될까? 이게 symbolic? 여러 시냅스의 집합? continual space에 표현되나?
2. 새로운 경험/인지에 대해서 schema를 찾고 그걸 기반으로 답하는 과정(이 과정에는 schema를 찾기, schema에 기반한 빠른 판단 or schema에 맞지 않아서 수정 하거나 또는 맞지 않아서 이해를 하기 어려워 한다면 해당 과정은 어떻게 될지
3. SBL을 base theory로 삼고 AI model을 만들거나 구조를 제안하는 최신 근황

이렇게 리서치해서 보고해

편집 주: 후속 논의는 continuous latent space와 continual learning을 구분했다. 원래 발화의 용어는 위에 보존했다.

## U-T06 — HOPE/Titans/Sleep와 이론·PoC

google research의 논문인

- nested learning(HOPE)
- model needs sleep
- titan-llama(논문이 언급하는 github repo와 code 공개되어 있음)

이걸 보면 schema based learning, rapid learning, 뇌 스위치 선택 설 적용해서 하는거 될까?

experience learning이란 근본적으로 schema learning이라고 생각하는데... 정답이 없고 경험에 최적화 하는 학습인거잖아? 물론 이론적으로 그렇다 하더라고 해당 architecture, framework를 어떻게 사용하느냐에 따라 달라질 수 있겠지만 나는 그걸 schema based learning으로 써보는건 어떨까 싶어서

달성해야할 목표는

- schema가 형성되고 활용 가능
- schema based learning이 얘기하는 대부분의 이론들이 적용되고 검증됨
- rapid learning을 통해 schema에 맞는 부분으로 빠르게 학습 및 이해가 됨
- system 1/2 사고방식에서 system 1을 담당하는 부분으로서 llm대비 매우 빠르게 주어진 정보에 대해서 schema를 찾고 답변 가능해짐

내가 기존에 하던 melete의 목표이기도 한데 이제 SBL을 알게되었고 TITAN, HOPE등의 메커니즘과 결합해서 이걸 하는게 될까 싶은거지. 이론적 토대와 수학적 공식만들고 실험을 통한 poc 증명까지 하고싶음

만약 이거 이후 가능하다면 추가적으로

- LLM은 매우 많은 data를 기반으로 하나의 schema를 학습한것이고
- post training/RL을 통한 alignment는 해당 schema를 여러 sub schema로의 분화 기능을 만든 것임

이걸 증명할 수 있다면 좋겠어

물론 이렇게 한다고 하더라도 우리 최초 시작시 얘기했던것 처럼 phase나눠서 단계별 mvp 계획 및 구현, self evolving하는 방식으로 작업하는 작업방식은 그대로 적용하고

## U-T07 — 통합 System ONE 정정

내가 원래 생각한건
이상적으로는
SYSTEM ONE을 통합하는 HOPE모델을 만드는데 loop transformer처럼 recursive하게 forward를 하는것
근데 주어진 문맥에 대해서 schema를 찾고 익숙한건 매우 빠르게 schema기반 답변을 하고 익숙하지 않으면 그 정도에 따라 rapid learning을 해서 schema update하고 답변하고 더 익숙하지 않으면 정도에 따라 더 깊은 loop을 타서 답변 하는것

이런 방식으로 hope를 만들까 했음. 근데 pretraining부터 하는건 무리니까 기존 모델에

- seq layer는 titan llama로 retrofitting하고
- ffn쪽은 cms(model needs sleep의 방법으로)로 점진적 교체를 해서 모두 교체하려고 한것
- 이후 외부로 schema를 offload하고 versioning및 retrieval가능하게 해서

최종 구조를 완성하려고 했음
아 당연히 이 과정에서 입력 문맥에 대한 schema판단 mlp나 구조를 넣어서 만들어야 하고

## U-T08 — 뇌파와 고정 주기의 본질적 재고찰

HOPE의 CMS는 뇌파에서 개념을 얻어서 update주기가 다른 level을 붙혀서 구현했잖아? 이 뇌파의 개념을 좀더 딥다이브해서 본질을 파악하고 개선해보는거 필요할거같아

보통 뇌파는 인간이 어떤 감정상태? 어느정도 노력? 집중 상태? 수면상태? 이런거에 있는지에 따라 또 익숙한지 아닌지등에 따라 사용하는 뇌파가 달라지지 않나? 라는 직관적 가설에서 출발하고싶어

그런 관점에서 모든 내용이 항상 일정한 token주기로 update된다? 이러면 안되지 않나

단순히 주기가 동적인것보다 더 본질적으로
뭐 여러 주파수가 동시 또는 순차로 쓰일수도있고 어떨때는 하나의 주파수만 쓸수도있고

여튼 본질적 고민을 해보자

## U-T09 — Adaptive depth와 6층위 의도

loop transformer
mixture of depth
(2개를 결합한 Mixture of Recursion 포함)
depth attention

이런 개념들도 적용하고 싶어. Ali도 최근 관심있는 개념들이래
나는 이런 개념들과 뇌파 이론들을 결합해서 이걸 재료와 핵심 메커니즘 베이스로 사용해서 - 문맥에 따른 schema 선택/rapid learning/update와
- system one 사고(system 1 + system2)와 같이 주어진 schema에 따른 빠른, 편향된 추론과 깊은 사고/통찰

이러한 2가지의 목표를 달성할 수 있지 않을까 하고 고찰중이야
너도 저 개념들에 대한 논문포함 읽고 이해하고

1차~6차까지 나의 의도를 풍부하게 파악하고 이해해서 해당 방향으로 align해서 답해줘
1차 : 표면, 2차 태도, 3차 방법론, 4차 철학, 5차 전략, 6차 세계관 <- 이건 예시인데 이런거처럼 보이는 그대로의 의도~더 상위 수준의 meta, meta의 meta 이런식으로 암묵지들을 파악해서 답변해주길 원함

## U-T10 — 상세 트래킹 지시

후속 주간 보고의 범위·분류·초기 추적 논문·확인 경계는 [TRACKING_POLICY](../research/TRACKING_POLICY.md)에 정리한다. 현재 저장소 업로드가 자동화의 수정·추가 실행이나 외부 메일 발송을 의미하지 않는다.

## U-T11 — 이번 게시 요청

> 내 github repo에 full-continual-learning이라고 repo를 만들었는데 우리 논의 한 모든 내용(기반 이론들, references도 모두 포함)해서 해당 repo에 올려줘
