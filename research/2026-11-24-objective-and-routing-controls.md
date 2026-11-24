# 2026-11-24 — objective-only / external routing 대조 보충

**ARCHIVE / LITERATURE (selected primary text checked) / PROPOSAL / OPEN / NOT RUN.** 11/23 SBL 주간 보고(cf2a13f1-5a60-832b-a5f2-ae489225b19e) 전체와 Sleep-time 주간 보고(ba80ff6c-c93c-8332-b32f-968bbee0c1c6)의 접근 가능한 본문을 재검토했다. 기존 11/23 선별 기록 및 [recurrence 보충](2026-11-24-recurrence-cost-controls.md)에 없는 두 비교 기준을 추가한다. 새 사용자 정정이나 새 통합 모델의 검증이 아니다.

## LITERATURE — 서로 다른 효율 개선 경로

- **NextLat (Teoh et al.)**: [arXiv v6](https://arxiv.org/abs/2511.05963v6), [HTML](https://arxiv.org/html/2511.05963v6), [저자 표시 코드](https://github.com/JaydenTeoh/NextLat). 최초 2025-11-08, v5 2026-11-11, **v6 2026-11-18**. SBL 보고의 최초 공개일은 맞지만 이번 주 개정도 공식 submission history에서 확인했다. NeurIPS 2026 채택은 arXiv 저자 Comments 표기이며 학회 proceedings를 별도 확인한 것은 아니다. Transformer hidden state와 실제 다음 토큰을 입력으로 작은 latent dynamics MLP가 다음 hidden state를 예측하도록 보조 학습한다. §3.2는 teacher-forced 다단계 rollout과 stop-gradient target을 사용한다. 이는 연속 latent의 예측적 조직화이고, 지속 expert CRUD나 세션 간 기억 학습은 아니다. §6은 latent 공간 구조 자체의 분석 부족, objective/optimizer 민감도, 큰 모델에서 multi-step/KL의 필요성 미확인을 인정한다. 최대 3.3배는 FineWeb-Edu validation에서 speculative decode의 저자 보고(§4.4 Fig. 8), 프롬프트 내 draft 길이 고정 조건이며 continual learning 효율이 아니다.
- **AnyS1 (Li et al.)**: [arXiv v1 2026-11-18](https://arxiv.org/abs/2611.23751v1), [HTML](https://arxiv.org/html/2611.23751v1), [프로젝트](https://middle-chunjie.github.io/AnyS1/). 공개 skill 1,000여 개에서 선택지 열거 가능한 결정을 추출하고, 격리 환경의 trajectory를 통해 별도의 4B 선택 모델을 훈련한다. 낮은 신뢰도는 외부 System-2로 넘긴다. 초록의 episode cost 75–91% 감소는 세 unseen benchmark에서 uncompiled System-2 대비 저자 보고다. §4.1–4.2 Table 2: SOPBench/ALFWorld/WebShop, DeepSeek-V4.1-Flash 계열 비교에서 workflow 컴파일만 한 All-S2도 76–86% 절감(평균 81%), AnyS1 warm은 86–91%(평균 89%). API list price와 self-hosted L4 serving throughput 기반 비용이며 총 offline 학습비 절감이 아니다. Warm threshold는 benchmark당 50 unlabeled dev run으로 맞추고 cold는 별도 조건이다. 사용자 확정 방향과 달리 외부 두 모델 구조이므로 **오직 외부 효율 비교 사례**로 분류한다.

읽은 범위: NextLat arXiv metadata/abstract, HTML §3.2–3.3, §4.4/§5.1/§6 및 부록 F 일부; AnyS1 metadata/abstract, HTML §4.1–4.2의 조건과 Table 2 발췌. 위 연구 수치는 저자 결과이며 전체 전문/부록 정독, 코드 실행, 학회 채택 독립 확인, FCL 실험 재현은 NOT RUN.

## PROPOSAL / OPEN — Ali A/B에서 추가 복잡성의 가치 분리

1. 기본 Transformer(NTP), 동일 backbone + next-latent auxiliary loss를 **objective-only 진단군**으로 둔다. 기존 Transformer/HOPE/Melete 주 비교는 유지한다. 같은 고유 경험과 데이터 순서, extra supervision, 목표 품질까지의 optimizer FLOPs, 추가 MLP/activation/rollout 비용 및 storage를 장부에 적는다. B의 unseen structural transfer를 objective만 바꾼 모델에서도 측정하여 Melete 고유 schema lifecycle의 추가 기여와 구별한다. 압축 표현의 존재, 효과적 rank 감소, 경험 이후 표본 효율은 서로 다른 측정이다.
2. AnyS1의 컴파일/위임 분해에서 착안하여 단일 통합 Melete 내부에서 모든 사례에 동일 깊이를 쓰는 기준, 동일 구조의 고정 정책, context-conditioned depth/activation, 잘못된 schema일 때 깊은 처리의 회복을 별도 진단한다. 같은 관측/출력 품질에서 activation coverage, 잘못된 빠른 결정률, confidence calibration, fallback/reprocessing 비용, offline compilation/학습비를 기록한다. 외부 dual-model 구조를 채택하거나 새로운 MVP gate를 확정하지 않는다.
3. 위 통제에서 품질/비용 이득이 남아야 CRUD의 독립 기여를 주장할 후보가 된다. 원본/파생 state, answer read/learning read, offload/delete를 기존대로 구분하며 self-evolution·단계별 실행 가능한 MVP 방향을 유지한다. 실험군 수와 통과 기준은 OPEN.

연결: [Ali A/B/C](2026-11-22-ali-abc-evaluation.md), [평가](../docs/08-evaluation.md), [통합 구조](../docs/05-integrated-architecture.md), [lifecycle](../docs/14-schema-lifecycle-crud-and-joint-paper.md), [보충 문헌](../references/2026-11-23-sbl-sleep-sources.md).

**범위:** 주간 보고에서 hardware-only 항목과 diffusion-only 반복 사례는 별도 직접 관련 근거가 생기기 전에는 이관하지 않는다. Sleep-time 본문 후반은 retrieval truncation이 있어 복원하지 않았다. 최근 대화 검색에서 새 직접 사용자 연구 정정은 발견되지 않았다.
