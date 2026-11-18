# 05. 통합 System ONE 아키텍처와 retrofit 경로

**USER 최종 방향:** pretrained LLM의 sequence layer를 Titan-Llama 계열로, FFN을 CMS로 점진적 전환한다. 같은 core를 재귀적으로 실행하고 문맥별 schema 판단으로 빠른 답·rapid update·깊은 사고를 조절한다. 최종적으로 외부 schema offload/versioning/retrieval을 지원한다.

아래 조합은 연구 제안이다. 기존 논문 하나가 이 전체를 구현하거나 검증한 것은 아니다. 핵심 문헌은 [A01–A18](../references/README.md).

## 1. 각 재료의 역할

| 재료 | 제공하는 것 | 제공한다고 가정하면 안 되는 것 |
|---|---|---|
| Titans | 입력의 관계를 neural memory fast weights에 저장/읽기 [A01] | KV 정확도만으로 추상 schema 형성 |
| Titan-Llama | pretrained sequence path retrofit, segmented attention+NMM [A04] | 전 층 전환·장기 사용자 state 운영의 자동 완성 |
| Nested Learning/HOPE | 학습 과정을 여러 optimization level/context flow로 조직 [A02] | update frequency가 의미적 추상화 수준이라는 등식 |
| CMS | 여러 갱신 시간척도의 기억 [A02]. **LITERATURE (NESTED, W6-swami23-metadata-gap.md:153; 전문 일부 정독):** 레벨과 갱신 빈도는 설계 시 고정이고 학습률 η_t와 decay α_t는 입력으로부터 생성되며(Eq. 79–97) schema·assimilation·accommodation 개념은 없음 | slow level은 forward에서 실행되지 않는다는 해석 |
| Sleep | fast→slow consolidation, Knowledge Seeding, Dreaming [A03] | 코드/아키텍처 자체의 development evolution과 동일 |
| Looped Transformer | shared weights로 effective depth 증가 [A06,A07] | 한번도 반복 학습하지 않은 모델을 그냥 재호출하면 개선 |
| MoD | depth별 token 계산 배분 [A08] | 문맥 수준 schema 이해의 직접 대체 |
| MoR | recursive sharing + adaptive token depth + cache 정책 [A09] | 임의 pretrained 모델의 무학습 전환 |
| Depth-Attention | 이전 layer/loop의 표현 선택적 재사용 [A10] | persistent experience memory와 동일 |
| Attention Residuals/MoDA | residual/block 또는 sequence+depth KV의 선택 [A11,A12] | MoDA와 2024 MoD가 같은 방법이라는 해석 |
| Rhythm-inspired control | read/write/compute/consolidate의 시간적 조율 가설 | biological Hz를 token interval에 직접 매핑 |

**LITERATURE (TEM20·SWAMI23·MICONI25·KUMAR26·SPENS24·HWU20, [2026-11-11-sbl-fulltext-review.md](../research/2026-11-11-sbl-fulltext-review.md#4-논문을-가로지르는-관찰) §4.3):** 원문 6편에서 같은 분해가 반복된다. 느린 쪽 / 빠른 쪽이 TEM20은 W / M, SWAMI23은 T / E, MICONI25는 느린 파라미터 / fast weight P(t), KUMAR26은 좌표 코드 / cue→goal 연합, SPENS24는 VAE / MHN, HWU20은 피질 CHL / 해마 인덱스다.

**LITERATURE (TEM20·KUMAR26, W4-tem20-kumar26.md:175,284):** 이 분해가 데이터에서 발견된 것은 아니다. TEM20의 분리는 고정 W_repeat/W_tile 같은 아키텍처 prior와 학습 분포가 만들었고, KUMAR26의 모듈 묶음은 Foster 외 2000의 schema 세 개를 이어받았으며 관계 계산 controller(NAVIGATE)는 backprop 사전학습 뒤 고정이다(W4-tem20-kumar26.md:291). 단 SWAMI23의 "T는 느리고 E는 빠르다"는 원문 용어가 아니라 우리의 정리다(W7-remediation.md:296).

**PROPOSAL (원문 검토 §4.3):** 이 분해는 System ONE의 CMS(느린 수준)·Titans(빠른 기억) 역할 분담과 잘 맞는다. 위 논문들이 CMS나 Titans를 쓴 것은 아니며 이 대응은 문헌의 발견이 아니라 우리가 구조 prior로 주입하는 해석이다.

**ARCHIVE (S24, 2026-11-09-sbl-tracking.md:72):** "FFN=모든 schema, sequence=모든 binding"의 일반 법칙은 주장하지 않고 CMS/Titan 역할 분담의 후보 가설로만 쓴다.

## 2. 한 모델 안의 네 상태

- **입력 표현:** 현재 token과 관계/목표의 context.
- **추론 작업 상태:** 현재 문제의 hidden states, 유효한 recursion별 depth bank.
- **지속 기억:** schema를 담는 weights, fast state, 느린 CMS levels, 적용 조건.
- **제어 상태:** schema 적합성, uncertainty, 선택적 write, compute budget, halting, 통합 준비도.

추론 작업 상태와 지속 기억은 구분한다. Depth attention은 이번 생각을 다시 읽는 통로이고 memory는 다음 문제에 영향을 주는 통로다. 이번 생각의 일부가 검증·학습을 거쳐 지속 기억에 들어갈 수는 있다.

## 3. 계산의 개념도

```text
입력/목표 → 입력부 → [shared Titan + CMS recurrent core] → 출력부
                         ↑            ↓
                 schema read     depth bank
                         ↑            ↓
                 persistent memory ← 선택적 update
                         ↑
                    Sleep/replay

같은 내부 controller가 문맥별 schema와 토큰별 계산을 연결하고,
각 반복에서 계속 계산/빠른 학습/전환/종료를 재평가한다.
외부 저장소는 memory artifact의 검색·적재·버전 관리를 담당한다.
```

별도 fast model을 최종 제품으로 전제하지 않는다. 실험용 작은 모형·baseline·외부 teacher는 허용되지만 통합 목표를 대체하지 않는다.

## 4. Schema controller의 입력과 출력

문맥 수준 head: 어떤 관계 구조를 적용할지, 다른 schema로 바꿀지, 조합할지, 수정/분화할지.

실행 수준 head: 어떤 token/block를 처리할지, 어느 depth source를 읽을지, fast update 횟수와 강도, 종료 여부.

**PROPOSAL (2026-11-17 검토; [13-schema-decomposition-and-interference.md](13-schema-decomposition-and-interference.md) §9.1):** 두 head의 출력을 읽기 gate $g^{\mathrm{read}}$(어떤 schema 상태를 이번 계산에 쓰는가)와 쓰기 gate $g^{\mathrm{write}}$(어떤 상태를 바꾸는가)로 나눠 읽을 수 있다. 이는 [06-mathematical-framework.md](06-mathematical-framework.md) §2의 $q^-_{t,k}$(결과 이전 schema 선택)·§5의 SchemaRead와 $u_{t,r}$(쓰기 대상·허용)·$\eta_{t,r}$(강도)의 구분에 대응하며 새 필드가 아니다. 여러 schema를 읽어도 모두 수정하지 않는다. 쓰기 허용 집합의 보호는 optimizer 상태·감쇠까지 포함해야 성립한다(06 §3 주석).

**LITERATURE (KUMAR26·TEM20·SWAMI23·SPENS24, [2026-11-11-sbl-fulltext-review.md](../research/2026-11-11-sbl-fulltext-review.md#4-논문을-가로지르는-관찰) §4.3):** 읽은 11편에는 불일치를 만났을 때 구조를 그 자리에서 수정·분할하는 실험이 하나도 없다. KUMAR26은 place cell remap 뒤 좌표 코드를 약 20 session 재학습하고(W4-tem20-kumar26.md:319), TEM20은 구조 remapping을 예측으로만 말하며(W4-tem20-kumar26.md:120), SWAMI23은 test 시 T를 고정하고(W6-swami23-metadata-gap.md:44,51), SPENS24는 test 시 VAE를 동결한다(W1-spens24-hwu20.md:103).

**LITERATURE (STRUCTK25 §2.2·§3.2.1, SPECTRUM26 p.1899·1902; W7-remediation.md:54-55,103, W5-spectrum26-structk25.md:89-95):** 정성 규칙은 있다. 오류가 크면 새 schema를 만들고 작으면 기존 schema를 미세 조정하며(STRUCTK25), fit이 낮을수록 변화량과 계산이 커진다(SPECTRUM26). 둘 다 데이터와 알고리즘이 없다.

**PROPOSAL (원문 검토 §4.3·§5 출발점 3):** 문맥 수준 head의 "수정/분화" 출력은 문헌에 구현된 기제가 없어 우리가 직접 설계하고 평가해야 하는 공백이다. 구현이나 채택 결정이 아니다.

후보 입력: 현재/과거 hidden state, memory prediction, 구조 적합성, observed/generated 구분, source reliability, prediction residual, epistemic/aleatoric uncertainty, goal, 비용 예산. 이들 모두를 사용할 필요는 없으며 ablation으로 최소 구조를 찾는다.

익숙한 schema라도 긴 관계 합성은 deep compute가 필요할 수 있다. 처음 보는 이름의 binding은 적은 update로 충분할 수 있다. 따라서 novelty→frequency 하나의 단조 함수로 제어하지 않는다. 무정보 ambiguity에서는 추가 관측·보류가 정답일 수 있다.

**LITERATURE (SPENS24·HWU20·SWAMI23·MICONI25·KUMAR26·TEM20·SPECTRUM26, [2026-11-11-sbl-fulltext-review.md](../research/2026-11-11-sbl-fulltext-review.md#4-논문을-가로지르는-관찰) §4.2):** "새로움·일치도가 학습을 바꾼다"는 말은 읽은 논문에서 서로 다른 기제다. 신호가 정하는 것이 논문마다 다르다: SPENS24는 요소별 재구성 오차가 빠른 저장소에 저장할 대상을, HWU20은 novelty×familiarity가 공고화 replay epoch 수를, SWAMI23은 leave-one-out 조건부확률이 다시 묶을 slot과 보호할 위치를, MICONI25는 네트워크가 스스로 만든 neuromodulator m(t)가 쓰기 시점·부호·크기를(연결별 계수 A는 meta-learned), KUMAR26은 보상과 ACh 억제가 성공 시 쓰기와 실패 시 해당 cue 삭제를 정한다. TEM20의 예측 오차에 비례하는 Hebbian 쓰기는 암묵적 gate이며 논문은 이를 novelty gating이라 부르지 않는다(W4-tem20-kumar26.md:119). SPECTRUM26의 schema fit은 변화량만 정성적으로 말하며 데이터가 없다. 학습률 자체가 학습된 값으로 바뀌는 것은 MICONI25뿐이고 CHU25·GOUDAR23·ELDER26에는 이런 신호가 없다.

**PROPOSAL (원문 검토 §4.2):** 질문 "schema가 학습 규칙 자체를 제어하는가"는 무엇을, 어디에(빠른 기억 대 느린 수준), 얼마나, 언제 공고화하는가로 쪼개 시험한다. Titans식 surprise 기반 쓰기는 이미 "얼마나"를 다루므로 비어 있는 것은 fit·친숙도에 따라 쓰는 위치와 공고화 예산을 바꾸는 것이다.

**USER (U-T07):** 입력 문맥에 대한 schema 판단 MLP·구조를 이 과정에 넣는다. **PROPOSAL:** controller는 첫 통합 모델부터 가장 얇은 형태로 존재하고 이후 단계에서 깊어진다. 모든 버전은 같은 입출력 필드를 유지하고 채우는 정도만 늘린다.

- **v0(첫 통합 모델):** 문맥 head 하나가 K개 schema slot에 대한 q^-를 내고([06-mathematical-framework.md](06-mathematical-framework.md) §2), 실행 head는 write gate 스칼라 하나와 종료 loop 수 선택(작은 이산 격자)만 낸다. depth read와 token routing은 없다.
- **v1:** token·block 단위 계산 mask a, depth source 선택, 학습된 halting(06 §6).
- **v2:** schema 조합·분화 head, 레벨별·연결별 write 허용 u, eligibility 기반 지연 귀속(04 §4).

v0도 [07-state-and-storage.md](07-state-and-storage.md)의 상태 계약과 [08-evaluation.md](08-evaluation.md)의 대조군·보호 family 평가를 통과해야 한다. 08 §3처럼 controller를 우회하고 고정 depth로 재는 절차와 충돌하지 않는다. **OPEN:** K·loop 격자·학습 신호는 pilot에서 정한다.

**OPEN (2026-11-17 검토, 이름 정리):** 이 절의 v0/v1/v2는 학습된 controller의 사다리다. [09-roadmap.md](09-roadmap.md)의 P1 'controller v0'는 익숙함 신호의 두 임계값으로 fast·learn·deep을 고르는 규칙형이며 학습된 문맥 head가 없다. 두 'v0'는 다른 것이다. 이 절의 v0는 로드맵 P3의 학습된 controller의 첫 단계로 읽고 P1 규칙형은 'v0-rule'로 부른다. [04-rhythms-and-orchestration.md](04-rhythms-and-orchestration.md)의 'controller v1 이후'도 이 절의 번호다. 번호는 바꾸지 않는다. CRUD 관점에서는 문맥 head(q^-)가 Read, write gate와 레벨별 write 허용 u가 Update, 조합·분화 head(v2)가 Create에 대응한다([09-roadmap.md](09-roadmap.md) §4-1).

**USER (B14, 2026-10-12):** 낯선 입력에서 가장 익숙한 지점에서 시작할 수 있는지 고찰한다. 학습한 뒤 강제로 다시 구성할지, 가장 유사한 기존 pattern의 구성을 쓸지는 설계 변수이며 실험과 뇌과학으로 정한다.

**PROPOSAL:** 통합 모델에서 이 변수를 낯선 입력의 처리 경로 비교로 정의한다. 경로 A는 빠른 쓰기 뒤 같은 입력을 다시 읽고 이어 간다. 경로 B는 쓰기 없이 가장 가까운 기존 schema의 잠정 답으로 이어 간다. 경로 C는 보류하고 추가 관측을 요청한다. 경로 B의 시작점은 controller가 고르는 '가장 익숙한 지점(bridge)'이며 그 선택 규칙을 학습·ablation 대상으로 둔다. 세 경로는 같은 관측·쓰기 예산에서 [08-evaluation.md](08-evaluation.md)의 F04와 F19(가까운 새로움·먼 새로움, 후보)로 비교하고 평균 loop 감소로 판정하지 않는다.

**ARCHIVE:** Melete는 같은 질문을 낯선 query의 두 대안(write 후 최초 query 재조회·compile 대 가장 가까운 graph의 명시적 잠정 compile+write)으로 두고 먼 단서에서 억지로 confident frame을 만들지 않는 신호도 기록하기로 했다 ([2026-10-12-neural-validation.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/superpowers/plans/2026-10-12-neural-validation.md)). prototype은 두 route를 구현했으나 추가 neural 효용은 입증되지 않았다 ([2026-10-12-neural-workflow-feedback.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/implementation/records/2026-10-12-neural-workflow-feedback.md)).

**OPEN:** 경로 선택이 familiarity 단독으로 정해지는지 구조 합성 난도와 함께 정해지는지는 위 단서(novelty→frequency 단조 함수로 제어하지 않는다)를 따른다.

## 5. CMS 점진 전환의 기능 보존 제안

기존 FFN F0를 느린 기반으로 보존하는 이행 후보:

    F_CMS(h) = F0(h) + sum_j g_j(h) B_j sigma(A_j h)

B_j=0으로 초기화하면 이 FFN 모듈의 초기 출력은 F0와 같다. A_j/gate까지 모두 0으로 만들어 새 분기의 gradient를 막지 않는다. 이후 서로 다른 update·protection·activation 정책으로 새 기억을 학습한다. 이 식은 원본 HOPE의 정확한 구조식이 아니라 프로젝트 proposal이다.

**PROPOSAL (2026-11-17 검토; [13-schema-decomposition-and-interference.md](13-schema-decomposition-and-interference.md) §7.3):** $B_j=0$ 초기화의 출력 동일성은 새 분기의 기여가 정확히 0이라는, docs/13 §7.3 충분조건(읽는 모든 값·연산을 유지)의 특수한 경우다. 학습이 시작돼 $B_j\ne0$이 되면 이 보존은 gate $g_j(h)$가 보호 입력에서 0이거나 별도 검증으로 확인될 때만 주장한다. 또 $g_j$가 softmax처럼 합이 1이 되게 정규화되면 분기를 추가하는 순간 기존 분기의 가중치가 모두 줄어든다. 위 식의 $g_j$가 독립 gate인지 정규화 gate인지는 정해지지 않았다(OPEN). 수치 비결정성 때문에 「같다」는 bit 동일성이 아니라 허용오차 안에서의 동일성이다([09-roadmap.md](09-roadmap.md) P1-T10 주석).

**OPEN (2026-11-17 검토; 인접 사례는 블로그 보고이며 동료 심사가 없다):** 새 branch를 기존 모듈 옆에 두고 gate/router로 선택하는 구성에서는 새 branch가 쓸모를 얻기 전에 gate가 닫힐 수 있다. TNG의 [Bring Your Own Expert](https://huggingface.co/blog/tngtech/bring-your-own-expert-extending-moe-models-with-ne)는 이 cold-start 문제 때문에 새 expert와 router row를 가장 활성화되는 기존 expert의 것으로 초기화하고 router를 잠시 고정했다고 보고한다. 위 F_CMS의 g_j(h)가 같은 이유로 새 분기를 일찍 닫는지는 [09-roadmap.md](09-roadmap.md) §5 P1-T05 spike의 점검 항목 후보이며, 블로그의 해법을 채택한다는 뜻은 아니다. 확인한 시험은 **NOT RUN**이다.

모든 FFN이 CMS 계약 아래로 전환되어도 원래 pretrained weights를 내부 기반으로 계승할 수 있다. 원래 FFN을 완전히 제거하려면 distillation·압축으로 추가 이전한다. 여러 F0를 직렬 복제하는 것은 함수 보존이 아니다: F0(F0(h)) != F0(h).

Nested Learning에는 pretrained MLP 초기화와 추가 학습 논의가 있다. 이것을 무학습 swap 성공 또는 필요한 최소 token 수의 근거로 읽지 않는다. [A02]

**PROPOSAL (2026-11-17 검토, low-rank expert와의 관계):** 사용자는 기존 지식을 low rank expert로 두고 in place update하며 적합한 schema가 없으면 새 expert를 create한다고 했다([2026-11-16-discussion.md](../sources/sync/2026-11-16-discussion.md), **USER**). 위 F_CMS의 분기 `B_j sigma(A_j h)`는 같은 모양(기반 + gate된 low-rank 분기의 합)이지만 색인 축이 다르다. j는 갱신 시간척도(level)이고, schema expert는 문맥으로 선택·할당되는 기능 단위다([14-schema-lifecycle-crud-and-joint-paper.md](14-schema-lifecycle-crud-and-joint-paper.md) §2). P1은 fast level이 1개라 expert가 하나이므로 expert 선택은 P3 이후다. in-place update는 분기와 NMM state의 test-time write에 대응한다. NMM은 sequence 쪽 빠른 기억(binding)이며 low-rank라는 규정이 없어 expert로 읽지 않는다. Create의 가장 자연스러운 후보는 새 분기를 B=0으로 추가해 생성 순간의 함수를 보존하는 것이지만 gate·`A_j` 초기화와 선택 규칙은 미정이다(**OPEN**; 위의 'gate까지 0으로 만들지 않는다' 주의가 그대로 적용된다). low-rank가 schema의 단위라는 것은 구현 전제이고 보편 명제가 아니다([06-mathematical-framework.md](06-mathematical-framework.md) §10, [11-research-agenda.md](11-research-agenda.md) §2).

**USER (U-T07):** FFN을 CMS로 점진 교체하되 "model needs sleep의 방법으로" 한다. **OPEN:** 위 F_CMS 식은 프로젝트 proposal이다. Sleep 논문 [A03]은 [catalog.tsv](../references/catalog.tsv)에서 metadata-checked 수준이라 그 논문이 규정한 FFN→CMS 전환 절차는 이 절에 반영돼 있지 않다. 정독 뒤 (a) F_CMS와 논문 절차의 차이, (b) Knowledge Seeding·Dreaming 단계와 전환 순서의 관계를 이 절에 기록하고, 차이가 있으면 어느 쪽을 기본으로 삼을지 사용자와 확정한다. 확정 전에는 F_CMS를 "Sleep 논문 방법의 구현"이라고 부르지 않는다.

## 6. Titan-Llama의 코드 접점

대화에서 검토한 pin: `sarahpannn/titans-pytorch@c60b4efaa3a3c6df4deebd57cbccf75947b87cad`. 이 pin의 코드 검토 이력은 보존하며 최신 HEAD라고 부르지 않는다. [A04-CODE]

- `TitanDecoderLayer`가 원래 `hf_layer.mlp`를 재사용하므로 CMS wrapper의 구체 접점이 된다.
- `freeze_backbone()`의 trainable-name 규칙에 CMS가 빠지면 추가 모듈이 freeze될 수 있다. optimizer와 trainable parameters를 명시적으로 점검한다.
- `generate()` 및 기본 `generate_with_titan_memory(reset_memory=True)`는 state reset 경로를 가진다. session persistence는 별도 계약이다.
- `forward_core()`의 position 증가와 memory write는 token 시계다. 이를 recursion 시계로 그대로 재사용하지 않는다.
- segmented attention과 remaining full attention, memory state와 KV는 별도다. partial conversion 결과를 all-layer 성공으로 확대하지 않는다.
- 재시작·rollback·offload 시 weights만 저장하고 momentum/clock/cache semantics를 누락하지 않는다.

이 내용은 이전 코드 스냅숏에서 관찰한 범위다. 새 구현 착수 시 pin 기준 재검토와 실제 integration test가 필요하다.

## 7. Recurrent retrofit

전체 LLM의 한 번 forward를 1 loop로 두면 minimum path 비용은 원래 direct answer와 비슷한 수준에서 시작하고 추가 모듈 비용까지 들 수 있다. ‘매우 빠름’을 목표로 하면 입력부–작은 shared core–출력부의 단위를 먼저 설계해야 한다.

Retrofitted Recurrence [A13], ETD [A14], Relaxed Recursive Transformers [A15]는 pretrained model에서 반복 구조로 이행하는 참고다. depth별 adapter/LoRA, 중간-depth loss, deep-to-shallow distillation은 후보다. 원래 모델을 같은 입력으로 단순 반복 실행하는 것과 다르다.

System 1의 의미는 적은 유효 계산 경로, System 2는 같은 모델의 더 큰 계산 예산이다. 출력 길이가 같지 않으면 end-to-end 비교를 분리한다. [평가](08-evaluation.md)

## 8. MoD/MoR의 인과성

현재 token의 router가 아직 생성되지 않은 token을 참조하지 않도록 한다. Top-k across sequence는 학습용 routing과 autoregressive 실행을 구별해야 한다. Expert-choice와 token-choice의 선택 시점이 다르다. controller가 추론 도중 정책을 바꾸게 하려면 관측 가능한 state에 근거한 재평가를 정의한다.

Weight sharing은 KV sharing을 자동 정당화하지 않는다. recursion index, token, branch, parameter version별로 어떤 source가 존재하는지 정의한다. Skip된 token의 depth state를 무조건 존재하는 것으로 처리하지 않는다.

## 9. Depth read와 retrofit의 인터페이스

Depth-Attention의 cross-layer V mixing, AttnRes의 residual/block aggregation, MoDA의 joint sequence/depth KV는 별도 후보다. 원래 KV 구조에 의존하는 기법을 Titans로 attention을 바꾼 모델에 붙일 때 동일한 cache 절약이 유지되는지 검증한다. 먼저 ‘유효한 이전 표현을 읽는 기능’을 공통 인터페이스로 정의하고 구현을 경쟁시킨다.

Depth bank는 이전 loop의 오판도 담는다. 선택 head가 다양성·불확실성을 유지할지, stale parameter version의 표현을 어떻게 무효화할지 평가한다. 같은 root를 반복 읽는 것을 독립 confidence 상승으로 계산하지 않는다.

## 10. Vec2text에서의 전환

기존 외부 Melete는 trajectory→text reader로 frozen consumer를 편향시키려 했다. 이번 통합 모델에서는 latent read를 projection/gate/adapter로 hidden computation에 연결하는 경로가 가능해져 free-form vec2text를 필수 관문으로 두지 않는다.

그렇다고 임의 latent를 pretrained hidden space에 그냥 더하면 의미가 전달되는 것은 아니다. alignment를 학습하고 source pointer·terminal state·all-state·learned interface를 같은 정보/예산으로 비교한다. [A05,S26]

**USER (B14/H4, 2026-10-12):** 매 turn working frame의 출력 trajectory의 모든 hidden state를 vec2text로 LLM token 앞에 배치해 bias한다. 이 가설은 틀렸다고 확인되기 전까지 유지하는 basis다. B01(2026-09-27)은 vec2text 대안의 전수 검토도 요구했다.

**USER (U-T02, U-T07):** model 수정 없이 하다 보니 vec2text에 대한 기대감이 부족하다고 했고, 가장 간단하게 시작해 점점 고도화하자고 했다. 최종 구조는 기존 모델의 sequence layer를 Titan-Llama로, FFN을 CMS로 retrofit하는 통합 모델이다. 보존된 사용자 발화(U-T01–U-T11)에는 text interface가 불필요하다는 문장이 없다.

**PROPOSAL:** 위 '필수 관문으로 두지 않는다'는 U-T07의 통합 구조에서 정리자가 도출한 추론이다. 통합 모델에는 text를 전달받는 외부 frozen LLM이 없으므로 text 변환과 prefix 위치는 필수 조건이 아니다. 그러나 H4가 요구한 관측은 유지한다. terminal만 쓰는 경우와 구분되는 전체 hidden-state 전달, 같은 정보·예산의 pointer·terminal 대조다. 외부 frozen consumer용 text prefix는 강한 대조군이며 사용자 확인 전까지 보존할 후보 interface로 둔다.

**ARCHIVE:** Melete는 latent/graph 상태를 LLM에 전달하는 방법을 상징·채널 기반, latent decoder, in-model 방법, 뇌·인지 근거의 네 부분 조사로 나눠 조사했다 ([2026-09-27-readout-survey.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/research/2026-09-27-readout-survey.md)). 또한 GTR sentence vector를 대상으로 한 vec2text의 혼합 실패는 graph hidden-state space를 위해 학습한 decoder의 실패가 아니므로 H4를 기각하는 근거로 쓰지 않는다고 정리했다 ([neural-basis.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/design/neural-basis.md)). 통합 모델의 interface 대안 후보 군은 문헌으로 확인한 것만 이 절에 추가한다.

**OPEN:** text interface를 현재 필수 조건에서 내리는 결정이 사용자 의사인지 확인이 필요하다.

**LITERATURE (2026-11-17 확인, 사용자 공유 링크 경유; metadata-checked + 본문 부분 정독):** Alabdulkareem 외, [Swarm Telepathy: Prefill-Free KV-Cache Transfer Across Families](https://arxiv.org/abs/2610.15095)(arXiv v1 2026-10-10. PDF의 소속은 MIT CSAIL·MIT-IBM이고 학회 채택 표기는 확인하지 못했다)는 서로 다른 모델 계열의 두 고정 LLM 사이에서 발신 모델의 KV cache를 수신 모델의 KV cache로 옮기는 약 300M 파라미터 transformer mapper를 쌍마다 학습한다(영어 텍스트 44M token, 1 GPU-day 미만으로 보고). 수신 모델은 원문을 prefill하지 않는다. 초록의 '평균 정확도 40%·wall-clock 4배'는 KV 압축과 결합한 SwaT를 텍스트 요약과 3개 모델 쌍·5개 예산·7개 데이터셋에서 비교한 값이다. 위 'learned interface' 비교군을 text 없이 구현한 인접 사례이지만 (a) 대상이 LLM 사이의 KV cache이며 Melete식 hidden-state trajectory가 아니고, (b) 쌍마다 mapper가 필요하며, (c) 한 번의 handoff만 평가했고, (d) 저자도 cache에 담긴 정보의 감사 가능성을 후속 과제로 둔다. H4의 text/vec2text 경로를 기각하거나 '필수 아님'을 확정하는 근거로 쓰지 않는다. 재현은 **NOT RUN**이다.

## 11. Sleep가 만들어야 할 변화

경험의 복원·보존 외에 새 관계 공유 사례에서 짧은 loop가 기능을 수행하도록 학습한다. 검증된 deep trajectory의 distillation, replay에서 조건·관계 재조합, adaptation-after-replay objective가 후보다. Generated curriculum은 외부 사실의 새 관측으로 세지 않는다. 같은 데이터·총 계산량의 replay/teacher baseline으로 원인을 분리한다.

**용어 구분 (2026-11-17 검토, PROPOSAL):** 외부 agent memory의 offline 재조직(MIRIX-2.0의 AutoDream, SoMem의 Topic 재조직과 view 재구축 등)은 문서·그래프·색인을 고치는 연산이며, 위 Sleep [A03]의 Knowledge Seeding·Dreaming과 이름이 비슷해도 fast→slow 파라미터 공고화가 아니다. 앞의 것은 외부 memory 비교 정책으로, 뒤의 것은 이 절의 Sleep으로 따로 보고하고 이름만으로 합치지 않는다. 두 연구는 arXiv preprint이고 성능 수치는 원 저자 보고다([2026-11-16-sleep-time-melete-integration.md](../research/2026-11-16-sleep-time-melete-integration.md), [2026-11-17-sleep-time-melete-selected-addendum.md](../research/2026-11-17-sleep-time-melete-selected-addendum.md)). 또 같은 '재귀'라는 말이라도 Feng·Meng의 recursive memory(arXiv:2611.13760)는 token 시계 위의 상태 갱신이며 §2의 recursion(같은 관측에 대한 내부 계산 깊이)과 다르다([07-state-and-storage.md](07-state-and-storage.md) §1).

**LITERATURE (SPENS24, W1-spens24-hwu20.md:90-93,110):** 문헌의 공고화는 빠른 저장소(MHN)가 teacher, 느린 수준(VAE)이 student인 replay다. replay 집합은 noise cue 10,000개를 MHN에 한 번 넣어 만든 고정 집합이고, 새 사건과 교차하는 replay와 generative replay는 제안에 그친다.

**LITERATURE (HWU20, W1-spens24-hwu20.md:265-271,299-304):** replay 횟수는 `epochs = e_default + NM·e_boost`로 정하며, 고정 800 epoch 조건(총 16,800)과 1,600 epoch 조건(총 33,600)보다 적은 총 13,875 epoch로 같거나 더 나은 probe 값을 냈지만(그림 판독 근사) 저자도 neuromodulator가 빠른 학습에 필수는 아니라고 쓴다.

**LITERATURE (SWAMI23, W6-swami23-metadata-gap.md:51; 원문 검토 §5 출발점 4):** Discussion은 T를 시간에 걸쳐 rebinding하는 방안을 제안만 하며 실험은 없고, 원문 검토는 이를 반복된 rebinding의 느린 가중치 흡수 제안으로 요약한다.

**ARCHIVE (S22, 2026-11-09-sbl-tracking.md:50-52):** 원문 복원 후 context로 다시 제공한 iRAG의 filtered QA(Wiki 99.3%, Character 85.4%)와 원문 재구성만으로 consolidation한 직접 QA(Wiki 31%, Character 33%)는 다른 지표이며 기억 복원과 유용한 판단은 별도 학습 문제다.

**PROPOSAL (원문 검토 §5 출발점 4):** Sleep의 첫 형태는 빠른 저장소에서 느린 수준으로 가는 teacher–student replay다. replay 예산의 novelty×familiarity 배분을 같은 총 계산의 고정 예산과 비교하고, 진단으로 SPENS24의 prototype 수축·lure 침입과 HWU20의 Tse식 probe를 빌린다.
