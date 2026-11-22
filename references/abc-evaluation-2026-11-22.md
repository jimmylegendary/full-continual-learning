# A/B/C 비교 실험의 보충 참고문헌

확인: 2026-11-22 (Asia/Seoul). [연구 제안](../research/2026-11-22-ali-abc-evaluation.md)의 근거다. 논문 결과는 Melete의 결과가 아니다. 아래 확인 범위를 넘어서 전문 정독·독립 재현했다고 주장하지 않는다. 기존 catalog의 과거 확인 기록은 보존한다.

| 출처 | 직접 확인한 범위 | 이번 설계에 쓰는 내용 |
|---|---|---|
| [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017 | arXiv 공식 초록·서지 | Transformer는 아키텍처 제안이다. 공통 예측 목적 아래에서 서로 다른 구조를 비교할 수 있다는 연구 구분 |
| [Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories, v2](https://arxiv.org/html/2606.03979v2), 2026-07-10 | HTML의 §3.2–3.3, §4.1 Table 3, Appendix B.5 등 관련 절 | Transformer에도 Sleep 적용; 계산 비용과 목표 품질 비용의 구분; capacity 확장을 포함한 저장 비용 기록 |
| [The Tolman–Eichenbaum Machine](https://pmc.ncbi.nlm.nih.gov/articles/PMC7707106/), Cell 2020, DOI 10.1016/j.cell.2020.10.024 | 공개 원문의 검색 인덱스 발췌에서 task·high-level algorithm 관련 부분 확인. 직접 페이지 open은 접근 확인 화면 | 다음 sensory observation 예측, 관계 구조와 감각 binding의 구분, 미경험 transition/loop closure와 새 환경 전이 평가 |
| [DiscoverPhysics: Benchmarking LLMs for Out-of-the-Box Scientific Thinking, v2](https://arxiv.org/html/2605.26087v2), 2026-08-31 | HTML 초록·§3.1–3.3·§4 관련 실험·§5 한계 | 반사실 물리 세계, 공통 randomized 관측과 능동 실험의 분리, 법칙 코드·held-out trajectory 검증 |
| [LLM-SRBench: A New Benchmark for Scientific Equation Discovery with Large Language Models](https://proceedings.mlr.press/v267/shojaee25a.html), ICML 2025 | PMLR 공식 초록·서지 | 알려진 식의 암기를 줄이는 transformed/synthetic 문제. 식 발견의 작은 출발점 |

DiscoverPhysics의 22개 세계는 curated 법칙이며 trajectory가 실행 시 생성된다. 이미 공개된 세계를 새 미공개 법칙처럼 취급하지 않는다. 해당 benchmark의 explanation judge·threshold를 Melete에 자동 채택하지 않고 객관 예측·동치류·개입 검증과 우리의 prospective gate를 구분한다.

TEM에서 빌리는 것은 구조 전이의 평가 논리다. 그 논문을 장기 망각 방지나 같은 품질의 추론 계산 절감이 이미 입증됐다는 근거로 쓰지 않는다. Sleep의 표에 Transformer가 있다는 사실도 특정 HOPE 재현이나 Melete의 이득을 증명하지 않는다.

기존 [아인슈타인 테스트 설계](../docs/17-einstein-test.md)의 시간캡슐 모델 후보 및 corpus provenance는 이번에 새로 감사하지 않았다. 현대 pretrained 모델을 prompt만으로 시대 제한한 결과와 검증된 시대 제한 기반의 결과는 구분한다.
