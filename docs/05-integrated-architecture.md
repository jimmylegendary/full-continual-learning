# 05. 통합 System ONE 아키텍처와 retrofit 경로

**USER 최종 방향:** pretrained LLM의 sequence layer를 Titan-Llama 계열로, FFN을 CMS로 점진적 전환한다. 같은 core를 재귀적으로 실행하고 문맥별 schema 판단으로 빠른 답·rapid update·깊은 사고를 조절한다. 최종적으로 외부 schema offload/versioning/retrieval을 지원한다.

아래 조합은 연구 제안이다. 기존 논문 하나가 이 전체를 구현하거나 검증한 것은 아니다. 핵심 문헌은 [A01–A18](../references/README.md).

## 1. 각 재료의 역할

| 재료 | 제공하는 것 | 제공한다고 가정하면 안 되는 것 |
|---|---|---|
| Titans | 입력의 관계를 neural memory fast weights에 저장/읽기 [A01] | KV 정확도만으로 추상 schema 형성 |
| Titan-Llama | pretrained sequence path retrofit, segmented attention+NMM [A04] | 전 층 전환·장기 사용자 state 운영의 자동 완성 |
| Nested Learning/HOPE | 학습 과정을 여러 optimization level/context flow로 조직 [A02] | update frequency가 의미적 추상화 수준이라는 등식 |
| CMS | 여러 갱신 시간척도의 기억 [A02] | slow level은 forward에서 실행되지 않는다는 해석 |
| Sleep | fast→slow consolidation, Knowledge Seeding, Dreaming [A03] | 코드/아키텍처 자체의 development evolution과 동일 |
| Looped Transformer | shared weights로 effective depth 증가 [A06,A07] | 한번도 반복 학습하지 않은 모델을 그냥 재호출하면 개선 |
| MoD | depth별 token 계산 배분 [A08] | 문맥 수준 schema 이해의 직접 대체 |
| MoR | recursive sharing + adaptive token depth + cache 정책 [A09] | 임의 pretrained 모델의 무학습 전환 |
| Depth-Attention | 이전 layer/loop의 표현 선택적 재사용 [A10] | persistent experience memory와 동일 |
| Attention Residuals/MoDA | residual/block 또는 sequence+depth KV의 선택 [A11,A12] | MoDA와 2024 MoD가 같은 방법이라는 해석 |
| Rhythm-inspired control | read/write/compute/consolidate의 시간적 조율 가설 | biological Hz를 token interval에 직접 매핑 |

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

후보 입력: 현재/과거 hidden state, memory prediction, 구조 적합성, observed/generated 구분, source reliability, prediction residual, epistemic/aleatoric uncertainty, goal, 비용 예산. 이들 모두를 사용할 필요는 없으며 ablation으로 최소 구조를 찾는다.

익숙한 schema라도 긴 관계 합성은 deep compute가 필요할 수 있다. 처음 보는 이름의 binding은 적은 update로 충분할 수 있다. 따라서 novelty→frequency 하나의 단조 함수로 제어하지 않는다. 무정보 ambiguity에서는 추가 관측·보류가 정답일 수 있다.

## 5. CMS 점진 전환의 기능 보존 제안

기존 FFN F0를 느린 기반으로 보존하는 이행 후보:

    F_CMS(h) = F0(h) + sum_j g_j(h) B_j sigma(A_j h)

B_j=0으로 초기화하면 이 FFN 모듈의 초기 출력은 F0와 같다. A_j/gate까지 모두 0으로 만들어 새 분기의 gradient를 막지 않는다. 이후 서로 다른 update·protection·activation 정책으로 새 기억을 학습한다. 이 식은 원본 HOPE의 정확한 구조식이 아니라 프로젝트 proposal이다.

모든 FFN이 CMS 계약 아래로 전환되어도 원래 pretrained weights를 내부 기반으로 계승할 수 있다. 원래 FFN을 완전히 제거하려면 distillation·압축으로 추가 이전한다. 여러 F0를 직렬 복제하는 것은 함수 보존이 아니다: F0(F0(h)) != F0(h).

Nested Learning에는 pretrained MLP 초기화와 추가 학습 논의가 있다. 이것을 무학습 swap 성공 또는 필요한 최소 token 수의 근거로 읽지 않는다. [A02]

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

## 11. Sleep가 만들어야 할 변화

경험의 복원·보존 외에 새 관계 공유 사례에서 짧은 loop가 기능을 수행하도록 학습한다. 검증된 deep trajectory의 distillation, replay에서 조건·관계 재조합, adaptation-after-replay objective가 후보다. Generated curriculum은 외부 사실의 새 관측으로 세지 않는다. 같은 데이터·총 계산량의 replay/teacher baseline으로 원인을 분리한다.
