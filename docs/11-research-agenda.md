# 11. 후속 가설·불확실성·연구 질문

## 1. Pretraining과 alignment 가설

**사용자 가설:** LLM은 대량 데이터에서 하나의 schema를 학습했고, post-training/RL alignment는 이를 여러 sub-schema로 분화하는 기능을 만들었을 수 있다.

이 가설을 보존하되 현재 사실로 채택하지 않는다. 하나의 parameter set은 여러 조건부 기능을 표현할 수 있다. 전체 지식 체계를 하나의 schema라고 정의하면 반증 가능성이 약해진다. [S26 Function Vectors, S24 Task Schema and Binding]

경쟁 가설:

| 가설 | 관찰할 변화 |
|---|---|
| Access/routing | 기존 기능을 문맥에 맞게 더 잘 선택 |
| Specialization | 기능적 부분의 분리와 전문화 |
| New structure | 이전에 없던 표현/연산의 형성 |
| Output policy | 내부 구조보다 말투·선호·응답 정책 변화 |

같은 base의 Base→SFT→DPO/RL checkpoint를 비교하고 비슷한 token·compute의 control을 둔다. 역할/표면 교차 전이, causal patching/lesion, selective impairment, 새로운 binding을 평가한다. cluster 수 증가, rotation에 민감한 시각화만으로 분화를 주장하지 않는다. 이 연구는 MVP의 선행 조건이 아니다.

## 2. Schema의 물리적 단위

한 schema가 MLP 하나인지, low-rank subspace인지, recurrent trajectory인지, 여러 모듈의 조합인지 열린 문제다. 여러 표현을 비교하되 재사용/전이/수정/보존 기능을 공통 평가한다. Neural manifold와 symbolic role 구조는 설명 수준이 다를 수 있다.

## 3. 표현 보호와 확장

기존 저차원 표현이 예외에 필요한 구분을 억제할 수 있다. 반대로 모든 입력에서 전체 weights를 고치면 안정된 구조가 사라질 수 있다. 보호·국소 수정·rank expansion·schema branch/split을 후보로 두고 F05/F06에서 비교한다. 논의된 근거: curriculum unlearning [S19], invariant schema [S25], recurrent scaffold [S23].

## 4. 통찰의 운영적 정의

현재 문제를 더 오래 생각한 사실이 아니라 새로운 관계·표현·적용 조건을 형성하고 새로운 사례에서도 재사용하는 변화다. 동일 정답의 암기, self-consistency, 반복된 confidence 증가는 충분하지 않다. Reconstruction에서 relational generalization으로 넘어가는 경계가 핵심이다.

## 5. Rhythm 필요성

Event/readiness controller에 oscillator를 더해야 어떤 이득이 있는가? 지연이 가변적이거나 여러 속도의 process가 상호작용하는 환경에서 추가 가치가 있을 수 있으나 아직 제안이다. 유효한 event-only baseline과 비교한다. 동기적 stage ID와 동치인지 검토한다.

## 6. LLM과 개인 경험의 관계

Base LLM에도 재사용 가능한 구조와 ICL이 있을 수 있다. Melete의 문제는 그 구조를 개인의 새 경험으로 지속 갱신하고, 현재 문맥에 적합하게 사용하고, 장기 보존과 수정의 균형을 맞추는 것이다. ‘schema가 없는 LLM에 최초로 schema를 넣는다’로 차별성을 과장하지 않는다.

## 7. 우선 읽을 연구 연결

- TEM/transformer–hippocampal relation → 구조와 내용의 분리.
- Goudar/Chu/Yoshida/Boboeva → subspace·attractor·manifold·low-rank scaffold.
- LCNet/S-HAI/latent cause → 맥락 선택과 binding; continuous와 discrete 구분.
- GNM → 선택적 write의 학습 가능성.
- Episodic CLS LLM/Spens → 저장/재구성과 판단/통합의 차이.
- Loop/MoD/MoR/AttnRes/MoDA → 계산 배분과 이번 사고의 표현 재사용.
- HOPE/Titans/Sleep → 빠른 상태와 여러 시간척도의 학습.

전체 링크와 확인 수준은 [문헌 목록](../references/README.md)에 있다.

## 8. 검증 없이 주장하지 않을 것

하나의 universal brain switch, schema=특정 Hz, biological state의 완전 재현, 신경망 모든 부분공간의 의미 해독, 범용 AGI, 통합 모델의 미실행 속도 이득, 기존 Melete보다 나은 실제 사용자 성능, 삭제 요구가 모든 consolidated weights에서 완전 제거됨.
