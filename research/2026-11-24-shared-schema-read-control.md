# 2026-11-24 — 공유 기억과 조건부 Read의 비용 대조

**ARCHIVE / LITERATURE (selected primary text checked) / PROPOSAL / OPEN / NOT RUN.** 11/23 Sleep-time 주간 보고의 접근 가능한 대화 검색 요약에서 Chorus 제목을 회수했다. 이번에 독립 보고 원문 재조회는 404로 실패했으므로 원 보고의 문장·수치를 복원하지 않는다. 기존 [기억 공고화 선별](2026-11-23-sleep-time-melete-selected.md) 및 [objective/routing 대조](2026-11-24-objective-and-routing-controls.md)에 없는 공유 기억의 조건부 read 비용 비교를 보충한다.

## LITERATURE — Chorus의 실제 범위

Chung & Du, [Chorus: Shared N-gram Embeddings with Layer-wise Adaptation](https://arxiv.org/abs/2611.23386v2), v1 2026-11-17, v2 2026-11-19. [HTML v2](https://arxiv.org/html/2611.23386v2), [논문에 표시된 코드](https://github.com/dualverse-ai/chorus). 토큰 및 고정 해시 bigram/trigram 주소로 연속 벡터를 찾아 공유하고, 삽입되는 층의 hidden state로 채널별 가중치를 만든 뒤 층별 projection을 통해 attention value에 넣는다. 즉 **이산 주소, 연속 벡터, 조건부 사용**이며 문맥에서 추상적인 schema 자체를 발견하거나 경험마다 expert를 생성·갱신·폐기하는 방법은 아니다.

저자 결과(§1, Fig. 1): ClimbMix, 20.7M backbone, 9개 층, 곡선의 각 점당 seed 1개. Chorus 1.2B table parameter가 Engram/FactorEngram 9.6B table보다 validation BPB가 낮다(논문 표현 87% 작은 table). 이는 전체 모델이나 peak memory의 87% 절감이 아니다. §3.2 Table 2의 1.2B table optimizer-state는 Ember 35.7 MiB(FP32 state), AdamW 4.47 GiB(BF16 state), 약 99.2% 절감으로 보고되며 전체 학습 메모리나 학습 FLOPs의 감소율이 아니다. Appendix D는 최대 133M backbone까지만 실험했으며 downstream 이득이 reasoning보다 언어 예측/지식 회상에 집중되었다고 명시한다.

2026-11-24 공식 arXiv 판본 이력·초록, HTML §1, §2 lookup/layer-wise adaptation, §3.2 Table 2 발췌 및 Appendix D 확인. 전체 전문/부록 정독, 코드 접근·실행, 독립 재현 **NOT RUN**.

## PROPOSAL / OPEN — Melete의 Read/Activate와 저장 예산 대조

- 같은 schema 후보 집합과 데이터 순서에서 (i) depth별 별도 저장, (ii) 공유 expert의 고정 read, (iii) 공유 expert의 context/depth-conditioned read를 진단 비교한다. 먼저 expert content와 update policy를 고정한 read-only 진단으로 조건부 사용의 기여를 분리한 뒤, end-to-end CRUD 후보를 비교한다. 고정 해시 n-gram/연속 embedding은 필요한 경우 lexical memory 진단 기준으로만 쓰며 neural schema의 정의를 바꾸지 않는다.
- Ali A의 동일 목표 품질 비교에서 unique persistent expert bytes, read adapter/gate parameter bytes, index/optimizer/replay/version bytes, resident 및 offloaded bytes, activation·lookup traffic 및 forward/backward/online/Sleep FLOPs를 따로 기록한다. 공유 저장에 따른 절감과 optimizer 선택에 따른 절감 및 read 연산 비용을 별도 대조한다.
- Ali B에서 표면 어휘를 바꾼 구조 공유 사례와 동일 어휘의 관계 반전 사례를 함께 사용한다. lexical 회상, 구조 전이, 잘못된 공유로 인한 interference 및 새 경험 뒤 필요한 표본·계산을 분리한다. 답변용 read와 학습용 read, offload와 delete, in-place Update/Create는 기존 정의대로 유지한다.

이것은 구현 또는 gate 확정이 아니다. 단일 통합 System ONE, continuous neural schema, 단계별 실행 가능한 전체 MVP와 self-evolution 방향을 유지한다. CAIMS 같은 하드웨어 검색과 dLoop 같은 diffusion 전용 생성 가속은 기존 선별 경계를 유지하며 이관하지 않는다. 최근 검색에서 신규 직접 USER 정정은 확보되지 않았다.

연결: [Ali A/B/C](2026-11-22-ali-abc-evaluation.md), [평가](../docs/08-evaluation.md), [schema lifecycle](../docs/14-schema-lifecycle-crud-and-joint-paper.md), [참고문헌](../references/2026-11-23-sbl-sleep-sources.md).
