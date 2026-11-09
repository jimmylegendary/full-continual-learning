# 07. 실행 상태·시계·cache·schema 저장 계약

상태: **설계 요구와 proposal**. 이 저장소가 runtime을 구현했다고 의미하지 않는다.

## 1. 시계와 정체성

| 필드 | 의미 | 금지되는 혼동 |
|---|---|---|
| experience/root ID | 외부 관측/사용자 정정의 출처 | 같은 입력의 loop를 새 root로 생성 |
| token position | 실제 token sequence 위치 | recursion마다 문맥 길이를 증가 |
| recursion index | 같은 관측에 대한 내부 계산 깊이 | 미래 관측 횟수 |
| optimizer step | 실제 update 수행 | forward 호출 수 |
| level clock | 각 CMS memory의 schedule/통합 준비 | 모든 level의 동일 의미 시계 |
| schema version | 적용할 학습 상태 | 항상 최신이 가장 적합함 |
| parameter/representation version | hidden space의 의미 | shape가 같으면 호환됨 |
| wall time | 실제 latency | FLOPs나 loop 수와 동일 |

## 2. Read/write 분리

추론은 committed snapshot을 기준으로 시작한다. Request-local working state에서 허용된 계산·fast update를 수행하고 evidence-bound change를 만든다. commit 전 같은 root의 영향, budget, source/revision, 삭제 상태, 관련 feedback을 검증한다.

이것은 기본 proposal이며 synchronous write의 유일한 허용 구현은 아니다. 다만 어떤 구현이든 read snapshot, write version, concurrency conflict, retry/idempotency가 명시돼야 한다.

마지막에 한 번 commit해도 임시 상태에서 같은 입력을 무제한 학습했다면 과대 반영은 남는다. temporary learning budget과 evidence budget을 따로 둔다. Generated interpretation은 학습 신호로 사용할 수 있지만 독립 observed root로 승격하지 않는다.

## 3. Recursion과 cache

재귀 weight 공유와 KV 공유는 독립적인 설계 선택이다. token i의 depth r가 어떤 parameter version에서 계산됐는지 추적한다. MoD/MoR로 skip된 depth state는 존재하지 않거나 마지막 유효 state를 가리키며 이를 명시한다.

최소 검사:

- 같은 sequence prefix를 두 번 처리해도 의도치 않은 memory double-write가 없어야 한다.
- 내부 loop 중 token position이 임의 증가하지 않아야 한다.
- autoregressive mask가 미래 token/depth 상태를 노출하지 않아야 한다.
- depth read는 존재하고 허용된 source만 참조해야 한다.
- weight update 이후 stale cache를 계속 쓸 때 의미적 정합성이 검증되어야 한다.
- speculative decoding/rollback과 windowed cache의 제한을 숨기지 않는다.

## 4. 학습 귀속

Eligibility에는 event ID, 활성 schema/경로, 관측 시점, 목표, 해석 origin, 의존 state version을 연결한다. 피드백이 늦게 도착해도 현재 활성 schema가 아니라 원래 관련 사건으로 귀속한다.

Read frequency에 따라 association을 강화하는 경우, 그 강화와 사실 validity를 별도로 기록한다. 단순 조회가 많아졌다고 진실성이나 외부 증거가 증가하지 않는다.

## 5. 외부화 단위

Schema 하나가 tensor 하나일 것이라고 가정하지 않는다. 여러 layer의 delta/adapters/fast states/읽기 조건을 묶은 artifact일 수 있다. 처음에는 기능적으로 검증된 bundle 단위로 저장한다.

권장 manifest 항목:

```text
artifact_id, schema_family, parent_versions, source_root_ids
base_model_revision, encoder_revision, tokenizer_revision
layer_bindings, parameter_shapes, norm/adapter_contract
slow_weights_or_deltas, fast_weights
optimizer_moments, update_counters, consolidation_state
applicability, confidence_calibration, validation_scope
serialization_format, content_hashes, replay_recipe
retention_policy, deletion_dependencies, migration_status
```

Read-only 복원과 이어서 학습할 복원은 필요한 state가 다르다. 정확한 session 재개에는 KV·position·budget 등 일시적 상태도 별도 bundle로 필요하다.

## 6. Version 의미

버전은 가장 최신의 하나만 선택하는 일렬 교체가 아니라 특정 source/조건/학습 상태의 lineage다. A→B→A에서 이전 A가 유효할 수 있다. 잘못된 과거 사실과 과거에는 유효했던 상태 변화는 다르게 처리한다.

Base encoder가 바뀌면 기존 schema latent의 좌표 의미도 바뀔 수 있다. shape 일치는 호환성 증거가 아니다. migration은 재인코딩, adapter, replay/distillation 등의 후보이며 별도 평가한다. 병합 후에는 개별 source 삭제가 완벽히 가능한지 검증 없이 약속하지 않는다.

## 7. 검색과 residency

검색용 embedding/key는 schema의 전체 의미나 적합성 판정을 대신하지 않는다. retrieval visibility와 applicability를 분리한다. Hot schema는 resident, cold artifact는 offload 후보로 두되 복사·deserialization·cache warmup 비용을 측정한다.

Multi-user 환경에서는 fast state, eligibility, optimizer state가 사용자를 넘어 섞이지 않게 해야 한다. shared slow model로 어떤 개인 정보를 통합할지 별도 동의·정책이 필요하다. 최초 MVP에서 광범위 개인 DB/native 권한을 자동 활성화하지 않는다.

## 8. 최소 상태 회귀

같은 입력의 재전송, 같은 ID의 다른 payload, interrupted update, restart, branch rollback, source 삭제, offload/reload, 모델 revision mismatch, concurrent writes를 검사한다. 저장·해시 검사 통과와 판단 효용 통과를 별도 보고한다.
