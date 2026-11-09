# SBL 전용 주간 추적 정책

기존 Sleep-time Compute 추적과 독립적으로, **SBL을 AI 모델의 근간 이론·학습 원리·아키텍처로 삼는 연구**를 한국어로 보고한다. 현재 문서는 정책의 보존이며 자동화 생성/수정 명령은 아니다.

## 범위

Continuous latent schema를 우선 심층 분석한다. Symbolic schema(규칙·관계·프로그램·이산 구조), neural/continuous, discrete latent/structured probabilistic, hybrid를 나눈다. Continuous와 continual을 혼동하지 않는다. Hybrid에는 어느 부분이 symbolic/latent인지 표시한다.

Schema를 중심 이론으로 명시한 직접 연구와 cognitive map·latent-cause·world model·meta/continual learning 등 인접 연구를 구분한다. 일반 RAG·embedding search·DB schema·JSON schema를 이름만으로 포함하지 않는다. CSCG/Hidden Schema Networks/S-HAI는 이산 잠재 구조임을 표시한다.

## 시간과 신규성

현재 날짜와 직전 성공 보고를 확인한다. 첫 실행은 최근 7일 우선. 최초 공개, 중요한 개정, 학회 게재, 공식 코드 공개를 구분한다. 과거 중요 자료를 새로 발견한 경우 신규 발견한 이전/기초 연구로 따로 보고한다. 의미 있는 변화가 없으면 반복하지 않는다. 새 연구가 없으면 없다고 보고하며 관련 없는 memory 논문으로 채우지 않는다.

## 각 논문의 필드

제목, 저자, 최초일, 개정일, venue/심사 상태, 공식 URL, code revision/라이선스, schema 정의와 표현 위치, 형성/선택/적용/수정, frozen/trainable 모듈, ICL vs 세션 간 지속 상태, benchmark/baselines, 정량 결과와 denominator, ablation, 실패/한계, 접근 깊이.

실제 뇌 실험, 계산모델, Melete로의 해석은 별도다. 초록만 읽었거나 원문/코드 접근이 막히면 명시한다. 보고되지 않은 수치는 추정해서 채우지 않는다.

## Melete 평가 관점

동일 구조의 새 과제에 대한 표본 효율, 표면 유사성에 속지 않는 전이, mismatch 시 수정/분리/전환, 보존과 망각, 동일 정확도의 추론 비용·지연, 경험 후 quality–compute 변화.

## 보고 순서

핵심 변화 → latent/neural 우선 심층 → symbolic → hybrid/adjacent → Melete 가설과 검증 → 다음 추적.

외부 메일 발송이나 저장소 변경을 추적 task에 암묵적으로 포함하지 않는다. 이번 저장소 게시 권한은 현재 사용자의 명시적 요청에 따른 별도 작업이다.

## 초기 baseline

2026-11-02 대화 기준: TEM, transformer–hippocampal models, Goudar subspace, LCNet, Chu attractor, Yoshida sleep manifold, Spens compressive RAG, Kumar schemas, Hippoformer, S-HAI, IP2-RSNN/capacity allocation, Hidden Schema Networks, schema-learning/rebinding, Schema Networks, Schema for ICL, The schema spectrum. 식별자는 [catalog](../references/catalog.tsv)에 있다.

S-HAI v3의 다중 grounding과 단일 schema를 구분한다. Spens의 narrative Mistral+xRAG+LoRA와 별도 GPT-2 구조추론 실험을 섞지 않는다. 과거 기록의 최신 버전을 이후 보고에서 재확인한다.
