# 2026-11-24 — recurrence 비용 통제 보충 검토

**ARCHIVE / LITERATURE (selected primary text checked) / PROPOSAL / OPEN / NOT RUN.** 11/23 Sleep-time 주간 보고(run ba80ff6c-c93c-8332-b32f-968bbee0c1c6)의 이미 발표된 논문 중 기존 [기억·공고화 선별 기록](2026-11-23-sleep-time-melete-selected.md)에 미포함된 두 recurrent architecture 연구를 추가 검토했다. 새 주간 보고나 새 사용자 정정이 아니다. 11/24 공식 arXiv v1 초록과 HTML 선택 구간을 대조했다. 단일 통합 System ONE을 유지하며, 별도 소형 System1+외부 LLM으로 변경하지 않는다.

## LITERATURE — 두 가지 서로 다른 recurrence

- **Huang et al., Latent Feedback Is a Compute and Data Amplifier** ([v1 2026-11-16](https://arxiv.org/abs/2611.20404v1), [HTML](https://arxiv.org/html/2611.20404v1), [저자 표시 코드](https://github.com/ifm-ai/LoRM)). 이전 토큰의 최종 hidden state를 다음 입력에 되먹임하는 token-axis recurrence. 저자는 동일 backbone 60M–778M, 12.5–400 고유 토큰/non-embedding parameter, 1–4 epoch 조건을 비교한다. §1의 Transformer 2-epoch budget에서 12.5 UTPP는 8% 추가 compute, 100 UTPP는 15–18% 절약, 400 UTPP는 44–48% 절약을 보고한다. 초록 최대 고유 데이터 절감 47%는 동일 epoch·목표 loss 비교이며 동일 FLOPs의 동시 절감 보장이 아니다. §2의 병렬 training/prefill 반복과 autoregressive decode 비용도 분리한다. 사전학습 데이터 효율 연구이지 세션 간 schema 갱신의 입증이 아니다.
- **Jin et al., Late Entry in Looped Language Models** ([v1 2026-11-18](https://arxiv.org/abs/2611.24576v1), [HTML](https://arxiv.org/html/2611.24576v1)). token 내부 depth recurrence에서 앞 pass를 건너뛰고 깊은 KV를 활용하며, 이후 cache completion과 verification을 수행한다. 저자 보고 GSM8K, block B=8, 단일 H100: Ouro-2.6B T=4/K=2의 greedy-exact 5.2배(동일 full-depth block 대비 +26%); Huginn-3.5B T=64의 8.4배(동일 full-depth block 대비 +153%). 이는 순차 full-depth decode 대비 속도이며 BF16 reduction-order 조건이 있다. 손실 허용 모드와 exact 모드를 구분한다. 기존 checkpoint 적응 SFT 비용 및 동시 요청 증가 시 compute 포화가 한계다. KV 재사용은 지속 신경 기억/학습이 아니다.

읽은 범위: 첫 논문 초록, HTML §1–4와 §5 일부 및 관련 표 발췌; 둘째 초록, HTML 그림 1 설명, 실험/한계 및 부록 concurrency 발췌. 전체 부록·코드·모델 실행, 재현, 동료심사 확인은 NOT RUN. 수치는 모두 해당 저자 조건이다.

## PROPOSAL / OPEN — Ali A의 인과 분해

- 동일 기반에서 token-axis feedback 유무와 schema CRUD 유무를 작은 factorial diagnostic으로 분리한다. 고유 경험·재노출·optimizer FLOPs를 장부에 따로 기록하고, matched quality와 낮은 N 영역의 역효과를 보고한다. 데이터가 부족할 때의 gain을 사전학습 결과로 가정하지 않는다.
- depth-axis에서는 full loop, early exit, late entry를 동일 cache/precision/장치/배치/출력 품질에서 비교하는 후보로 둔다. 깊은 KV 완성·재실행·검증의 FLOPs, TTFT/TPOT, peak state, setup/SFT 비용, 동시성별 throughput을 포함한다. Token feedback과 loop count, CMS update clock은 서로 독립이다.
- A에서의 효율 개선이 B의 구조 전이 또는 C의 발견을 자동 증명하지 않는다. neural schema를 선택·갱신하는 효과와 recurrence만의 효과를 분리한다. 새 실험군·수치 gate는 확정하지 않으며 기존 단계별 실행 가능한 MVP 계획을 변경하지 않는다.

연결: [통합 구조](../docs/05-integrated-architecture.md), [평가](../docs/08-evaluation.md), [Ali A/B/C](2026-11-22-ali-abc-evaluation.md), [원문 목록](../references/2026-11-23-sbl-sleep-sources.md).
