# 09. 단계별 MVP: 작은 통합 모델에서 전체 구조로

**USER:** objectives·수치 verification·negative feedback·operation policy를 먼저 정하고 단계적으로 작동하는 제품을 만든다. Self-evolving 개발 방식은 유지한다. **PROPOSAL:** 아래 phase 번호와 세부 gate는 논의를 통합한 제안이며 개별 수치 승인이나 실제 구현 완료를 의미하지 않는다.

## 1. 최종 아키텍처를 작은 범위로 먼저 연결

| 단계 | 구현/산출물 | 다음 단계의 근거 | 완료로 부르면 안 되는 것 |
|---|---|---|---|
| P0 연구 계약 | 용어·state clocks·source boundary·baselines·평가 split·budget | 누수/인과성/표본 단위 감사 | 2026-11-03 선형 실험만으로 통합 P0 전체 완료 |
| P1 얇은 통합 모델 | 작은 pretrained 모델 일부에 Titan sequence path+CMS FFN, 실제 입력/저장/재시작 | 원래 능력 보존과 실제 memory 사용 | 분리된 module 테스트만 통과 |
| P2 recursive computation | 같은 core의 1/2/4/... 반복, 중간-depth 출력·causal cache | 반복이 필요한 과제에서 quality–compute 개선 | 동일 입력 재호출 또는 무의미한 loop 증가 |
| P3 schema/controller | 문맥 관계 판단+token routing+선택적 update+halting | 구조 전이와 적정 불확실성, 동일 품질의 비용 감소 | 쉬운 사례만 골라낸 평균 depth 감소 |
| P4 experience+Sleep | binding/수정/ABA/replay/통합/deep-to-shallow 학습 | 경험 후 새 사례의 관측 수·총 계산 감소, 이전 조건 유지 | 저장/재구성 성공을 판단 효용으로 해석 |
| P5 전체 retrofit 확대 | sequence/FFN 전환 범위를 단계적으로 증가 | 각 전환 뒤 품질·state·성능 회귀 통과 | 부분 layer 결과를 all-layer 성공으로 확대 |
| P6 schema 외부화 | offload/version/retrieval/migration/delete | 재적재 후 판단과 후속 학습의 일관성 | tensor shape/hash만 확인 |

P1–P4는 얇은 수직 경로 안에서 반복할 수 있다. 연구용 작은 합성 모델과 실제 consumer의 역할을 구분한다. 모든 단계를 설계 문서만으로 동결하지 말고 다음 phase의 구체 파일/함수 계획은 선행 결과에 따라 작성한다.

## 2. 첫 integrated MVP의 최소 사용자 여정

세션 시작 → 관계 경험 입력 → schema/binding 상태의 변경 관찰 → 새로운 역할/개체의 질문 → 실제 모델 응답 → 반례/정정 → 최초 과제 재평가 → A조건 재방문 → 상태 저장 → 프로세스 재시작 → 동작 유지 → 해당 source의 수정/삭제 처리.

단순 task라도 이 경계를 실제로 연결한다. mock-only 테스트를 E2E 증거로 쓰지 않는다. 다만 full consumer 연결 전 실패 원인을 분리하는 kernel 연구를 허용하고, 연구 구현을 효용 gate 통과로 혼동하지 않는다.

## 3. 초기 실행 순서 제안

1. 유효한 vanilla checkpoint와 입력·응답 baseline을 pin한다.
2. sequence memory와 FFN wrapper의 변경을 하나씩 적용하여 원래 동작 보존 범위를 확인한다.
3. state/clock/cache 계약을 먼저 테스트한다.
4. 고정 depth의 실제 recursive 경로를 학습한다.
5. 관계 전이와 few-shot adaptation 과제를 넣고 memory의 추가 이득을 확인한다.
6. 그 위에 adaptive controller와 선택적 쓰기를 학습한다.
7. 실제 경험 이후와 Sleep 이후의 quality–compute 곡선을 분리한다.
8. 검증된 범위만 늘리고 외부화한다.

초기에는 원논문 전체 규모를 재현할 의무가 없다. 반대로 이름만 같은 간이 구현을 원본 HOPE 재현이라고 부르지 않는다. 설계 차이와 생략된 학습을 기록한다.

## 4. 중단·전환 조건

현재 recipe의 비용과 품질이 baseline을 넘지 못하면 원인을 분리한다. 방법을 확장하기 전에 학습 목표, 데이터 식별성, representation capacity, reader/interface, 계산 예산 중 어떤 병목인지 구분한다. 같은 test를 반복해서 보고 새 candidate를 최적화하지 않는다.

같은 조건에서 단순한 pooled/linear/text 방법이 낫다면 그 후보를 유지한다. 제품에 효용이 있어도 neural schema의 독자 기여가 미입증이면 두 상태를 분리 보고한다. 불리한 결과를 이론 전체의 반증으로 확대하지 않되 기준을 낮춰 성공으로 바꾸지도 않는다.

## 5. 지속적으로 유지할 자산

실패 사례/negative controls, data generators, source/recipe lineage, state compatibility tests, regression suite, actual cost ledger, reference catalog, specification/decision log. 테스트 수·문서량·커밋량을 연구 진전의 대표 지표로 쓰지 않는다.

## 6. 기존 phase와의 관계

초기 Melete의 N0–N5, J0–J5, P1–P4 및 11월 3일 외부 fast-model 중심 P0–P5는 역사적 계획이다. 현재 phase는 사용자가 통합 System ONE으로 정정한 이후의 조직이다. 옛 PASS/FAIL 및 실행 산출물을 새로운 phase의 완료로 이식하지 않는다. [계보](12-melete-lineage.md)
