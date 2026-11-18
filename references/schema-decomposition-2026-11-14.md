# Schema 분해·간섭 논의의 보충 참고문헌

게시일: 2026-11-14. 연결 문서: [13. Schema 정의·분해·변경 간섭](../docs/13-schema-decomposition-and-interference.md).

기존 [catalog.tsv](catalog.tsv)는 덮어쓰지 않는다. 아래 R 번호는 이 보충 문서 안에서만 사용하는 식별자다.

**OPEN (2026-11-17 검토):** (1) **식별자 충돌:** [README.md](README.md)와 [catalog.tsv](catalog.tsv)의 `R`은 리듬/가소성 계열(R01–R11)이고 [04-rhythms-and-orchestration.md](../docs/04-rhythms-and-orchestration.md)도 R01–R11을 그 뜻으로 쓴다. 이 보충의 R01–R13은 다른 문헌이므로 docs/13 본문의 [R01]은 catalog의 R01(LFP 생물물리)로 읽힐 수 있다. 인용할 때 「schema-decomposition R01」처럼 문서명을 붙이거나 접두사를 바꾼다. (2) **catalog와의 대응:** 이 보충의 R01(Goudar)은 catalog S03, R03(Function Vectors)은 S26과 같은 논문이다. R01은 catalog에서 이미 `fulltext-read`(2026-11-11 원문 검토의 GOUDAR23)이므로 아래 `discussion-import`보다 높다. R13은 블로그 글이고 같은 연구의 논문은 catalog A02(arXiv 2512.24695)이므로 주장 인용은 A02를 쓴다. R02·R04–R12는 280dc9a 기준 catalog에 없었다(이 검토가 그중 일부를 후보 행으로 올렸다). (3) R05는 제목이 적혀 있지 않아 서지가 불완전하다(링크 해시만). (4) 확인 수준 이름 `official-body-checked`는 README의 목록에 없고, 이 보충은 README의 읽기 경로에서 연결되지 않는다(루트 README와 docs/13에서만 연결). (5) R06·R08–R11의 확인 수준은 이 검토에서 재확인하지 않았다. R10(SupSup)은 arXiv 초록에서 task identity 추론과 task identity 없는 학습을 다룬다는 점만 확인했다(docs/13 §8 주석).

## 확인 수준

- `discussion-import`: 직전 대화의 제목·공식 링크·관련 주장 범위를 보존. 이번 게시에서 재정독·최신 버전 검증을 하지 않음.
- `official-search-checked`: 이번 게시에서 공식 arXiv/학회/기관 검색 결과로 제목·식별자를 확인. 전문 정독·실험 재현은 아님.
- `official-body-checked`: 이번 게시에서 공개 원문의 관련 본문을 확인. 코드 실행·재현은 아님.

실제 문헌의 결과, Melete의 해석, 제안 수식·실험은 별개다. 논문 전문·그림·저자 코드를 재배포하지 않는다.

| ID | 문헌과 공식 출처 | 확인 수준 | 관련성과 제한 |
|---|---|---|---|
| R01 | Goudar et al., *Schema formation in a neural population subspace underlies learning-to-learn* (2023). [DOI](https://doi.org/10.1038/s41593-023-01293-9) | discussion-import | 재사용되는 부분공간·동역학. 범용 LLM의 모든 schema를 분리한 결과가 아님. |
| R02 | *Toy Models of Superposition* (2022). [저자 원문](https://transformer-circuits.pub/2022/toy_model/index.html) | discussion-import | Feature superposition은 고수준 schema 중첩과 동일한 개념이 아님. |
| R03 | *Function Vectors in Large Language Models*. [arXiv](https://arxiv.org/abs/2310.15213) | discussion-import | Activation intervention과 과제 유도. 벡터 하나가 독립된 전체 프로그램이라는 증거는 아님. |
| R04 | *LIMA: Less Is More for Alignment* (NeurIPS 2023). [학회](https://papers.neurips.cc/paper_files/paper/2023/hash/ac662d74829e4407ce1d126477f4a03a-Abstract-Conference.html) | discussion-import | 적은 SFT로 기존 능력을 활용하는 관점. Schema 물리적 분리 입증이 아님. |
| R05 | Yue et al.의 RLVR 능력 경계 연구 (NeurIPS 2025). [학회](https://papers.neurips.cc/paper_files/paper/2025/hash/537d5aa768c2d534016a4d06f87bc8fb-Abstract-Conference.html) | discussion-import | 직전 답변의 원문 링크를 보존. 관찰한 모델·훈련·샘플링 범위를 넘어 모든 RL의 결론으로 확대하지 않음. |
| R06 | *ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models* (2025). [arXiv](https://arxiv.org/abs/2505.24864), [학회](https://proceedings.neurips.cc/paper_files/paper/2025/hash/1a22b912945fb7c0bdd079e792b31b6f-Abstract-Conference.html) | official-search-checked | 더 긴 RL의 능력 확장에 관한 비교. 이번에 논문 식별자 확인, 전문 재독 아님. |
| R07 | *Gradient Episodic Memory for Continual Learning* (NeurIPS 2017). [학회 원문](https://papers.neurips.cc/paper/2017/file/f87522788a2be2d171666752f97ddebb-Paper.pdf) | discussion-import | Gradient 제약과 국소 근사. 임의 장기 update의 무망각 보증으로 과장하지 않음. |
| R08 | *Gradient Projection Memory for Continual Learning* (2021). [arXiv](https://arxiv.org/abs/2103.09762) | official-search-checked | 기존 활동의 중요한 부분공간과 update 제약. 이번 식별자 확인, 전문 재독 아님. |
| R09 | *Progressive Neural Networks* (최초 공개 2016). [arXiv](https://arxiv.org/abs/1606.04671) | official-body-checked | 과거 column 고정, lateral transfer. 파라미터 증가·task 선택 한계도 함께 읽음. |
| R10 | *Supermasks in Superposition* (NeurIPS 2020). [arXiv](https://arxiv.org/abs/2006.14769), [학회](https://proceedings.neurips.cc/paper/2020/hash/ad1f8bb9b51f023cdc80cf94bb615aa9-Abstract.html) | official-search-checked | 고정 기반의 task별 mask·선택. 의미적 schema 발견과 동일시하지 않음. |
| R11 | *WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models* (NeurIPS 2024). [arXiv](https://arxiv.org/abs/2405.14768), [학회](https://proceedings.neurips.cc/paper_files/paper/2024/hash/60960ad78868fce5c165295fbd895060-Abstract-Conference.html) | official-search-checked | 원래/수정 지식의 메모리 분리와 routing·sharding. 범용 관계학습까지 검증한 것으로 확대하지 않음. |
| R12 | Locatello et al., *Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations* (ICML 2019). [PMLR](https://proceedings.mlr.press/v97/locatello19a.html) | discussion-import | 귀납적 편향과 식별성. 모든 형태의 구조 분해가 불가능하다는 주장은 아님. |
| R13 | Google Research, *Introducing Nested Learning: A new ML paradigm for continual learning*. [공식 글](https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/) | discussion-import | Context flow·최적화 수준의 관점. Schema 변경 경계와의 연결은 Melete 설계 해석. |

## 문헌과 제안의 경계

원문 결과를 넘어서는 schema artifact 계약, read/write gate 분리, schema-specific Jacobian 지표의 사용, post-training 경쟁 가설, 실험 A–E는 이 프로젝트의 **PROPOSAL**이다. 이번 문서 게시에서 구현하거나 효용을 검증하지 않았다.
