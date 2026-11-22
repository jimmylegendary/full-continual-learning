# 2026-11-22 논의: Ali의 지적과 A/B/C 비교 실험

## 출처와 범위

**USER:** 아래는 현재 대화에서 직접 확보한 사용자 메시지 전문이다. 기록 날짜는 2026-11-22 (Asia/Seoul)이며 Ali 미팅의 실제 날짜는 제공되지 않았다. Ali 발언의 독립 녹취가 아니라 사용자가 전한 지적과 사용자의 실험 제안이다. 이전 세션 전체를 복구한 자료가 아니다.

상시 FCL 연구 기록 동기화 요청에 따라 보존한다([SYNC_POLICY.md](../../SYNC_POLICY.md)). 구현·모델 학습·유료 실험을 실행한 기록이 아니다.

## 사용자 원문

```text
Ali와의 미팅에서 지적한게 있음
inductive bias는 좋지... 근데 이걸 어케 증명하냐는거야
- transformer보다 뭐가 더 나은데? Transformer는 심플하지. 다음토큰 예측. 근데 melete는?
- 그럼 그 성능을 달성하기위해 얼마나 많은 정보를 학습해야함?

이게 주요 지적임
관련하여
- transformer/hope(sleep)/melete 이렇게 3가지를 놓고 실험하는게 필요
- 실험으로는
A. Basic test
1. 동일양의 정보 입력 시 성능차이가 어떻게 되나?
2. 1번할때 매 turn마다 비용은 어떻게 되나?
3. 1번외에 transformer/hope의 성능이 무너지는 turn까지 지속 시 melete의 성능은 유지되나?

B. Schema test
0. Benchmark들에서 environment와 knowledge를 구분
1. Environment와 knowledge를 pair로 hope/melete에게 주고 추론을 시키고 이후 environment만 순서대로 줬을 때 성능 비교

C. Bias test
- 이건 사실 제대로 측정이 어려울듯
- 하지만 이전에 논의한것처럼 Einstein test나 이와 유사한 테스트 benchmark를 만들고 trajectory도 모두 포함하게 만들어서 특정 시점까지의 지식을 학습하고, 이후 trajectory만 줬을때 transformer/melete 에서 유의미한 무언가를 추론할 수 있는지 확인하기. 이건 Einstein test이면 상대성이론을 추론하는 것이고, 다른 test이면 그에 상응하는 무언가를 추론하는 것
```

## 반영 지도

| 사용자 요청 | 연구 제안의 반영 |
|---|---|
| 세 대표 모델의 비교 | [A/B/C 설계](../../research/2026-11-22-ali-abc-evaluation.md) §2; B/C에도 세 군을 유지하는 것은 assistant 제안 |
| 같은 정보, 성능에 필요한 정보량 | 같은 원천 stream, 정보/노출/추가 감독 장부, Q(N), N*(q), C*(q) |
| 매 turn 비용 | online 지연, Sleep 포함 누적 비용, setup과 운영 비용, storage 증가 |
| 기준선 붕괴 이후의 유지 | 공통 horizon과 지속 실패 정의; 현재/유효 과거/전이 분리 |
| environment와 knowledge pair | B0 정의와 B1 인출; B2–B5 구조/조합/부적합/복귀는 assistant 제안 |
| 경험 trajectory를 통한 발견 | 기존 ET 설계를 유지하면서 공통 관측/능동 실험, 입력 감독 수준과 객관 예측 판정 보완 |

연구 제안의 수식, 목표치 결정 방식, baseline 세부 조건, 실행 순서는 **PROPOSAL**이며 사용자가 확정한 것이 아니다. 실제 수치 threshold는 아직 없고 모델 비교는 **NOT RUN**이다. 문헌 근거는 [보충 참고문헌](../../references/abc-evaluation-2026-11-22.md)에서 확인 수준별로 분리한다.
