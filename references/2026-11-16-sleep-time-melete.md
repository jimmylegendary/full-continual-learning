# 2026-11-16 Sleep-time 조사에서 선별한 FCL 인접 참고문헌

**읽기·검증 범위:** 독립 Sleep-time 주간 자동화의 보고 내용을 이관하되, 아래 8편은 2026-11-16 공식 arXiv 초록·버전 이력·제목·첫 저자를 재확인했다. 전부 arXiv preprint로 취급한다. PDF 전문·부록·공식 코드는 미독·미실행이다. 보고 수치를 독립 재현으로 표시하지 않는다.

| ID | 원문 / 첫 저자 | 최초 제출 및 확인 버전 | 분류 |
|---|---|---|---|
| ST26-01 | [MAPE](https://arxiv.org/abs/2611.17068) / Xinheng Ding | 2026-11-12 v1 | External agent memory program evolution; **not neural schema** |
| ST26-02 | [MIRIX-2.0](https://arxiv.org/abs/2611.12068) / Wei-Chieh Huang | 2026-11-09 v1 | External structured/episodic/procedural memory; **not parametric continual learning** |
| ST26-03 | [CAMP-II](https://arxiv.org/abs/2611.14009) / Lirui Luo | 2026-11-10 v1, 11-12 v2 | File-based memory I/O policy learning |
| ST26-04 | [Continual-ARC](https://arxiv.org/abs/2611.14505) / Daniel Lenton | 2026-11-10 v1, 11-11 v2 | Evaluation of retained skills versus memory retrieval |
| ST26-05 | [MemCredit](https://arxiv.org/abs/2611.15600) / Quanjiang Guo | 2026-11-11 v1 | Counterfactual external memory selection |
| ST26-06 | [MaLoRA](https://arxiv.org/abs/2611.14397) / Ziqing Xu | 2026-11-10 v1 | Parametric low-rank adaptation; restricted near-orthogonal linear classification theorem |
| ST26-07 | [LoRA capacity utilization](https://arxiv.org/abs/2611.17191) / Tomohiro Sawada | 2026-11-12 v1 | Effective rank and learning–forgetting of parametric adapters |
| ST26-08 | [Evolving Infra](https://arxiv.org/abs/2611.12304) / Hao Kang | 2026-11-09 v1, 11-12 v2 | Agent-aware inference/KV cache serving, not HBF validation |

**상태:** All items — arXiv metadata/abstract verified; fulltext NOT READ; independent model reproduction NOT RUN. 각 항목을 **continuous neural schema**, **discrete latent schema**, **external memory**, **parametric learning** 중 잘못 분류하지 않는다. [연구 연결 기록](../research/2026-11-16-sleep-time-melete-integration.md).

**OPEN (2026-11-17 검토, 공식 arXiv abs 페이지 재열람):** ST26-01~08의 제목·첫 저자·최초 제출일은 위 표와 일치한다. 차이는 다음과 같다. (1) ST26-04 Continual-ARC는 v3(2026-11-15)가 현재 표시되며 위 표와 '상태' 문장의 'v1, v2'는 최신 버전이 아니다. (2) 일부 표제가 줄여 적혀 있다. ST26-01은 arXiv 표제에 'MAPE:' 접두가 없고(초록이 MAPE로 명명), ST26-03은 '…: Unlocking the Memory Potential of Pre-trained File Operations for Long-Horizon Tasks via On-Policy Distillation', ST26-05는 '… for Decision-Time Memory in Long-Horizon Web Agents', ST26-06은 '…: Robustness to Catastrophic Forgetting and Adapter Merging', ST26-07은 '… for Mitigating the Learning-Forgetting Trade-off'까지가 표제다. (3) 연구 기록의 'MAPE 최대 12%p'는 초록의 'absolute accuracy gain of up to 12%'를 옮긴 표기다. (4) 일부 arXiv 페이지에 코드 링크가 표시된다(ST26-01, 02, 04, 07, 08; 저장소 내용과 실행은 확인하지 않았다). 한편 2026-11-16 보충 선별의 WikiTrace(arXiv:2611.14320)와 HiVe-Mem(arXiv:2611.12872)은 이 파일의 표에 없고 [2026-11-16-memory-evidence-read-supplement.md](/home/jimmy/repos/full-continual-learning/research/2026-11-16-memory-evidence-read-supplement.md)와 manifest에만 있다.

## 2026-11-17 추가 선별 (기존 ST26-01~08과 중복 없음)

| ID | 원문 / 저자 | 최초 공개와 검증 수준 | 표현·직접 관련성 |
|---|---|---|---|
| ST26-09 | [SoMem — Can LLM Agents Organize Their Own Memory?](https://arxiv.org/abs/2611.11929) / Zichuan Fu 외 7명; [공식 코드](https://github.com/Qi202/SoMem) | **2026-11-09 v1**; 2026-11-17 공식 arXiv 초록·일부 본문·저자 링크 및 코드 저장소 존재 확인 | External linked-document memory, evidence and derived retrieval views. **Not continuous neural schema** |
| ST26-10 | [Recursive memory for prediction and generation](https://arxiv.org/abs/2611.13760) / Pengbin Feng, Chunlei Meng | **2026-11-10 v1**; 2026-11-17 공식 arXiv 초록·일부 본문 확인 | Finite-state recurrent prediction/generation capacity theory. **Not schema training or LLM forgetting theorem** |

두 항목은 2026-11-16 독립 Sleep-time 주간 보고에서 추가 회수한 **이전 발표 자료**다. 원문 PDF 전체·부록·코드 실행·성능 재현은 수행하지 않았다. [상세 검토와 Melete 가설](../research/2026-11-17-sleep-time-melete-selected-addendum.md).
