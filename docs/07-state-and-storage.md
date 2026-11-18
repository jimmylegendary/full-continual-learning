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

**USER (B14, 2026-10-12):** 익숙하면 hit한 구조를 compile해 완결된 working frame을 만든다. 매 turn 출력이 frame과 맞지 않으면 이번 입력·출력·내부 출력으로 학습한 뒤 최초 query로 다시 검색해 frame을 재구성하고 중단 지점부터 재개한다.

**PROPOSAL:** 이를 통합 모델의 상태 계약으로 옮긴다.
- 읽기 기록: 한 요청의 schema 읽기가 어떤 요소(layer 결합·fast state·depth source)를 어떤 순서로 읽었는지 기록한다. 이 기록은 이후 write와 독립이다.
- 갱신 후 재개: 요청 중 학습이 일어나면 새 root를 만들지 않고 같은 root와 같은 최초 입력으로 다시 읽는다. 재개 위치(token position t, recursion index r)와 무효화한 cache를 기록한다.
- 이중 write 방지: 재개 때 이미 반영한 증거를 다시 쓰지 않는다.
- 재현: 같은 입력의 재읽기는 원래 읽기 결과를 재현할 수 있어야 하며 차이는 갱신으로 설명할 수 있어야 한다.

**ARCHIVE:** Melete는 working graph를 snapshot으로 compile하고 선택 node/edge·전역 상태·context·encoder parameter의 의존성을 각각 추적하며, 낮은 compatibility에서 갱신한 뒤 최초 query로 재compile해 중단 지점에서 재개하는 것을 basis로 유지했다 ([2026-10-15-neural-judgment-roadmap.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/superpowers/plans/2026-10-15-neural-judgment-roadmap.md)). 이 닫힌 loop는 좁은 합성 scene에서만 실행됐고 일반 효용은 검증되지 않았다 ([2026-10-12-neural-workflow-feedback.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/implementation/records/2026-10-12-neural-workflow-feedback.md)).

## 4. 학습 귀속

Eligibility에는 event ID, 활성 schema/경로, 관측 시점, 목표, 해석 origin, 의존 state version을 연결한다. 피드백이 늦게 도착해도 현재 활성 schema가 아니라 원래 관련 사건으로 귀속한다.

Read frequency에 따라 association을 강화하는 경우, 그 강화와 사실 validity를 별도로 기록한다. 단순 조회가 많아졌다고 진실성이나 외부 증거가 증가하지 않는다.

**USER (B14, B09):** 조회 trajectory에서 hit한 경로는 모두 연결 강화한다. 검색할 때 시냅스가 강화되는 시나리오를 학습 방식으로 정리한다.

**PROPOSAL:** 조회 구동 강화(read-driven strengthening)를 허용하는 경우 다음을 계약으로 둔다.
- 강화를 네 가지로 구분해 기록한다. 접근성(조회·활성 trace), 연합(고찰·사용으로 달라지는 연결), compatibility(등록 관측의 귀속), parameter plasticity(write gate에 따라 M·reader·updater가 바뀐 정도)다.
- 접근성·연합은 학습된 관심에 영향을 줄 수 있으나 사실 validity와 독립 증거 수를 바꾸지 않는다.
- 같은 root의 반복 조회에 대한 포화 상한과 감쇠를 사전에 명시한다.
- 강화 전후 값을 hit 경로와 함께 기록한다.
- 자기증폭(조회가 늘수록 더 자주 선택돼 오판이 고착되는 현상)을 직접 측정하고 독립 반례 뒤 회복 여부를 본다.
- 강화를 끈 대조군과 같은 예산으로 비교한다.

**ARCHIVE:** Melete v0.2는 강화를 접근성·연합·compatibility·parameter plasticity로 구분했고 ([experience-system.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/design/experience-system.md) §5), 이후 hit 강화와 사실 validity의 분리·포화·감쇠·반복 안정성 평가·자기증폭 직접 측정을 요구 사항으로 유지했다 ([neural-basis.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/design/neural-basis.md)). 효용은 입증되지 않았다.

**OPEN:** 강화의 단위(파라미터 국소 경로·fast state·외부 key)는 [11-research-agenda.md](11-research-agenda.md) §2의 schema 물리 단위가 정해질 때 정한다.

## 5. 외부화 단위

Schema 하나가 tensor 하나일 것이라고 가정하지 않는다. 여러 layer의 delta/adapters/fast states/읽기 조건을 묶은 artifact일 수 있다. 처음에는 기능적으로 검증된 bundle 단위로 저장한다.

**PROPOSAL (2026-11-17 검토; [13-schema-decomposition-and-interference.md](13-schema-decomposition-and-interference.md) §3):** docs/13 §3의 schema artifact $(\phi,B,C,D,Q)$ 다섯 성분과 아래 manifest의 대응은 다음과 같다. φ ↔ `slow_weights_or_deltas`·`fast_weights`·`parameter_shapes`·`norm/adapter_contract`, B(개체·역할 binding 인터페이스) ↔ 대응 필드 없음(`layer_bindings`는 layer 부착 정보로 다른 뜻), C ↔ `applicability`·`confidence_calibration`·`validation_scope`(검색 key는 §7에서 따로 다룬다), D ↔ `base_model_revision`·`encoder_revision`·`tokenizer_revision`(`parent_versions`는 계보이지 의존이 아니다), Q ↔ `optimizer_moments`·`update_counters`·`consolidation_state`·`source_root_ids`·`replay_recipe`. manifest에만 있는 필드는 `retention_policy`·`deletion_dependencies`·`migration_status`·`serialization_format`·`content_hashes`다. 「다른 schema의 의존 버전」을 담을 필드는 현재 없다(OPEN). 이는 설명용 대응이며 manifest 서식을 바꾸지 않는다.

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

**PROPOSAL / OPEN (2026-11-17 검토): 읽기 충분 상태와 갱신 충분 상태.** 위 구분을 한 걸음 더 나눈다. (i) 현재 질의에 답하는 데 충분한 상태(read-sufficient)와 (ii) 이후 외부 관측이나 모델 자신이 만든 token으로 계속 갱신해도 읽기 성능을 유지·복구할 수 있는 상태(update-sufficient)는 서로 다른 요구이며, 같은 현재 질의 정확도가 (ii)를 보장하지 않는다. 동기는 고정 크기 recurrent 상태의 필요 용량을 조건부로 분석한 [Recursive memory for prediction and generation](https://arxiv.org/abs/2611.13760)(Feng·Meng, arXiv preprint, 2026-11-10 v1)이다. 이 논문은 알려진 양의 전이 HMM에서 미래 사건 질의에 필요한 상태가 오차 ε에 대해 로그 크기일 수 있지만, 자기 출력 token으로 상태를 결정적으로 갱신하는 생성기의 긴 연쇄 생성에서는 nondegenerate 2-state 사례에서 길이 T에 대한 항이 더해진다고 보고한다. 이 결과는 유한 상태 HMM 모형, 고정된 갱신 규칙, 결정적 갱신과 오차 척도(사건 질의는 log-확률 오차, 생성은 단어별 오차 또는 총 KL 예산)에 의존하며 LLM·System ONE의 fast state나 CMS level 일반의 하한이 아니고 schema 용량의 하한도 아니다. 논문은 schema와 continual learning을 다루지 않으므로 이 결과의 적용 가능성은 OPEN이다. **시계 주의:** 논문의 T는 token(또는 경험) 시계의 길이이며 §1의 recursion index(같은 관측에 대한 내부 계산 깊이)가 아니다. 두 시계를 섞지 않는다. bundle의 `validation_scope`에는 읽기 충분성만 검증했는지 갱신 뒤 읽기 보존까지 검증했는지를 구분해 적는다(제안). 측정 후보는 [08-evaluation.md](08-evaluation.md)의 F-CI이며 **NOT RUN**이다. 상세와 출처: [2026-11-17-sleep-time-melete-selected-addendum.md](../research/2026-11-17-sleep-time-melete-selected-addendum.md).

## 6. Version 의미

버전은 가장 최신의 하나만 선택하는 일렬 교체가 아니라 특정 source/조건/학습 상태의 lineage다. A→B→A에서 이전 A가 유효할 수 있다. 잘못된 과거 사실과 과거에는 유효했던 상태 변화는 다르게 처리한다.

Base encoder가 바뀌면 기존 schema latent의 좌표 의미도 바뀔 수 있다. shape 일치는 호환성 증거가 아니다. migration은 재인코딩, adapter, replay/distillation 등의 후보이며 별도 평가한다. 병합 후에는 개별 source 삭제가 완벽히 가능한지 검증 없이 약속하지 않는다.

**PROPOSAL (2026-11-17 검토; [13-schema-decomposition-and-interference.md](13-schema-decomposition-and-interference.md) §9.2):** 확정된(committed) schema 상태를 직접 덮어쓰지 않고 새 version으로 쓴 뒤 보호 family 회귀를 통과하면 승격하는 경로(copy-on-write)를 후보로 둔다. 작업 중 상태의 제자리 갱신은 §2의 request-local working state가 이미 맡는다. version에는 수정(같은 조건의 오류 교정)·분기(다른 조건의 구조 공존)·조합(여러 구조 병용)을 구별해 기록한다. 의존 버전(encoder·backbone·다른 schema)이 바뀌면 shape가 같아도 의미가 바뀔 수 있으므로 소비자가 새 version으로 옮기기 전에 호환성을 검사한다. schema 단위 복사량과 이동 검사 비용은 측정하지 않았다.

**OPEN (2026-11-17 검토):** 위 migration 후보 중 adapter의 인접 사례로 서로 다른 모델 계열 사이에서 KV cache를 변환하는 학습된 mapper가 있다([Swarm Telepathy](https://arxiv.org/abs/2610.15095), LITERATURE, 본문 부분 정독). 이 연구가 다루는 것은 한 번의 handoff에서 LLM 사이의 문맥 cache 변환이며, 저장된 schema·fast state가 base encoder 교체 뒤에도 유효한지는 다루지 않는다. 저자가 밝힌 대로 모델 쌍마다 mapper를 학습해야 한다. 따라서 이 방식의 성공이나 shape·hash 일치를 migration 호환성의 증거로 쓰지 않고, 필요하면 P5 migration 비교 후보로만 둔다([09-roadmap.md](09-roadmap.md) §9 대응표의 P6 schema 외부화 행).

## 7. 검색과 residency

검색용 embedding/key는 schema의 전체 의미나 적합성 판정을 대신하지 않는다. retrieval visibility와 applicability를 분리한다. Hot schema는 resident, cold artifact는 offload 후보로 두되 복사·deserialization·cache warmup 비용을 측정한다.

**PROPOSAL / NOT RUN (2026-11-17 검토): 증거 계보와 색인 재구축.** 한 schema 읽기가 의존하는 계보를 원본 관측(source/root, §1) → 파생 해석·교훈(generated, §2에 따라 observed로 올리지 않음) → schema version·artifact(§5) → 읽기용 색인·view로 기록해 읽기 시점에 거꾸로 확인할 수 있게 하는 경로를 후보로 둔다. in-place neural update 뒤의 색인·view 재구축은 파라미터 갱신과 다른 연산이므로 stale index, 근거 손실, 추론 회귀를 따로 검사하고 비용도 나눠 보고한다. 외부 agent memory 연구(SoMem arXiv:2611.11929, WikiTrace arXiv:2611.14320, MIRIX-2.0 arXiv:2611.12068)는 근거 링크와 view 재구성을 외부 문서에서 구현한 인접 선행이며 neural schema 지속학습의 근거가 아니다(arXiv preprint, 저자 초록 수준). 출처 연결이 끊긴 압축과 되돌릴 수 없는 폐기는 다른 비용을 만든다. 상세: [2026-11-16-memory-evidence-read-supplement.md](../research/2026-11-16-memory-evidence-read-supplement.md), [2026-11-17-sleep-time-melete-selected-addendum.md](../research/2026-11-17-sleep-time-melete-selected-addendum.md).

**USER (B01, 2026-09-27):** 사용자는 eviction·forgetting·memory revision에는 아직 아이디어가 없다고 밝혔다. 설계가 채워야 할 열린 문제다.

**PROPOSAL:** 위 residency는 저장 위치(resident/offload)의 정책이고 eviction은 fast state에서 무엇이 빠지는가의 정책이다. 둘을 분리한다.
- 망각은 decay α와 L_forget로 표현하되 어떤 정보가 얼마나 약해졌는지를 level별로 기록한다.
- eviction은 fast state가 용량을 넘을 때 후보를 고른다. 기준 후보는 최근 사용, 독립 증거 수, 적용 조건의 중복, 보호 family와의 연관이다.
- eviction은 폐기가 아니라 offload·재구성 가능 상태로의 이동을 기본으로 한다. source 삭제(철회·재구성)는 §8의 최소 상태 회귀를 따르고, 용량 정책으로서의 압축·통합·폐기(기능적 망각/보존)는 아래 용어 구분과 [08-evaluation.md](08-evaluation.md) §2-2의 제안 family F22를 따른다.
- 평가는 [08-evaluation.md](08-evaluation.md)의 F10(consolidation)과 보호 family의 회귀로 한다.

**ARCHIVE:** Melete v0.2는 active eviction을 'canonical 경험을 지우지 않고 현재 active set에서 내려놓음'으로 정의하고 consolidation·deletion·graph replay와 구분했다 ([experience-system.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/design/experience-system.md) §11).

**OPEN:** 기준 후보 중 무엇이 쓰기 gate의 학습 가능한 신호가 되는지는 정하지 않았다.

**PROPOSAL (2026-11-17 검토, 용어 구분):** 새 문서 [14-schema-lifecycle-crud-and-joint-paper.md](14-schema-lifecycle-crud-and-joint-paper.md) §4는 용량 예산 아래의 Delete/Retain을 다루고, 이 계약과 [09-roadmap.md](09-roadmap.md) P1-T13은 source 삭제를 다룬다. 같은 '삭제'라는 말이 다른 두 일을 가리키므로 아래처럼 구분한다. 사용자의 Delete는 "무한히 증가하는 지식에 대해서 망각의 비용을 어떻게 치뤄야할지"이며([2026-11-16-discussion.md](../sources/sync/2026-11-16-discussion.md), **USER**) 아래 표의 '기능적 망각/보존' 줄에 해당한다.

| 용어 | 뜻 | 평가 | 보장의 상한 |
|---|---|---|---|
| eviction·offload | 활성 집합이나 GPU에서 내려 외부로 옮긴다. 내용은 남고 재적재할 수 있다(위 bullet) | F12, cold/warm-load 비용 | 위치만 바뀐다. reload 뒤 판단·후속 학습의 일관성을 잰다 |
| 기능적 망각/보존 (Delete/Retain) | 예산 아래 압축·통합·버전 정리·폐기를 골라 기능 손실과 재접근·재학습 비용을 치르는 정책 | Efficacy: [08-evaluation.md](08-evaluation.md) F10·F12·제안 F22, 보호 family | P4부터 정책, P5에서 압축·폐기. 기능 손실 추정기는 미검증. 무제한 무망각은 주장하지 않는다 |
| source 삭제 (철회·재구성) | source 원장에서 한 경험을 철회하고 committed snapshot에서 남은 source를 같은 순서로 재생해 state를 재구성한다. provenance 철회이며 용량 정책이 아니다 | Contract·Product(§8 삭제 동등, UJ1 ⑨) | P1은 fast state 한정. 통합(Sleep)·압축 뒤에는 '측정만'. '삭제 완전 보장'은 쓰지 않는다 |

쓰기 규칙: 새 글에서 '삭제' 단독 표기는 source 삭제만 뜻한다. CRUD의 D는 'Delete'로 쓰고 첫 등장에 '기능적 망각/보존'을 병기한다. schema·artifact를 없애는 동작은 '폐기'라고 쓴다. 통합·압축·폐기는 replay 재구성의 전제(원장과 직전 snapshot)를 줄이므로 보존 정책은 source 삭제의 보장 범위를 좁힌다. 매니페스트의 `retention_policy`와 `deletion_dependencies`가 이 두 축을 각각 담는다. eviction 기준 후보에 '없어졌을 때의 기능 손실'([14-schema-lifecycle-crud-and-joint-paper.md](14-schema-lifecycle-crud-and-joint-paper.md) §4)을 더할 수 있으나 쓰기 gate의 신호로 쓸지는 위 OPEN을 따른다.

Multi-user 환경에서는 fast state, eligibility, optimizer state가 사용자를 넘어 섞이지 않게 해야 한다. shared slow model로 어떤 개인 정보를 통합할지 별도 동의·정책이 필요하다. 최초 MVP에서 광범위 개인 DB/native 권한을 자동 활성화하지 않는다.

## 8. 최소 상태 회귀

같은 입력의 재전송, 같은 ID의 다른 payload, interrupted update, restart, branch rollback, source 삭제, offload/reload, 모델 revision mismatch, concurrent writes를 검사한다. 저장·해시 검사 통과와 판단 효용 통과를 별도 보고한다.
