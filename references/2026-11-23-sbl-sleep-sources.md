# 2026-11-23 SBL·Sleep-time 선별 문헌 — 1차 출처 대조

**범위:** 2026-11-23 완료된 독립 SBL 및 Sleep-time 주간 보고에서 FCL/Melete 설계에 직접 연결되는 10개 항목. 외부 보고의 수치와 해석은 discussion-import/저자 주장으로 두고, 아래 **원문 URL·공개 시점·초록**만 독립 확인했다. 전문 정독/코드 재현 **NOT RUN**. 새로 '발견'한 과거 논문을 11월 신간으로 세지 않는다.

| ID | 공식 원문 / 연도·판본 | 분류와 확인한 범위 |
|---|---|---|
| S162 | [Deng et al., Early Learning Shapes Later Directions Of Representation Change](https://arxiv.org/abs/2609.36081); **2026-09-28 v1, 10-01 v2**; [저자 코드](https://github.com/YuantaoDeng/latent-scaffold) | neural-continuous **adjacent**, not direct SBL. arXiv abstract/versions, 4 encoders·2 datasets, scaffold constraint 반례 확인. 코드 미실행 |
| S163 | [Goo et al., SchemaMem](https://arxiv.org/abs/2609.33436); **2026-09-27 v1** | continuous neural recurrent state, *schema-indexed*은 관계적 일반 schema와 구분. arXiv 초록 및 선택 HTML 부분; 수치 재현 아님 |
| S164 | [Dong et al., Symmetry-Aware Schema–Session Decoupled LoRA Adaptation](https://doi.org/10.3390/sym18060953); **2026-06-01**, Symmetry 18(6):953 | neural continuous shared/session adapters for **session-aware** continual KGC; 학술지 본문 §3–4 일부 확인. oracle session ID 제공, rank 8; task-free 선택 아님 |
| S165 | [Yu et al., A Neuro-symbolic Framework under Statistical Relational Learning](https://pubmed.ncbi.nlm.nih.gov/43043738/); **2026-11-17**, IEEE TPAMI online ahead of print, DOI [10.1109/TPAMI.2026.3755075](https://doi.org/10.1109/TPAMI.2026.3755075); [2023-09-16 preprint / 2025-02-22 v2](https://arxiv.org/abs/2309.08931) | **HYBRID** neural continuous representations + discrete symbolic predicates/FO rules; PubMed journal metadata/abstract, arXiv earlier abstract; TPAMI 전문·코드 미확인 |
| A72 | [Liu et al., MemFolder](https://arxiv.org/abs/2611.26427); **2026-11-19 v1** | adjacent external agent memory; arXiv abstract verified. Compression vs fact recovery, not parametric continual schema |
| A73 | [Yang et al., Forget Freely, Grep Later / GrepMem](https://arxiv.org/abs/2611.25123); **2026-11-18 v1** | adjacent append-only source log + grep; arXiv abstract checked; cost/accuracy author claims |
| A74 | [Jayaram et al., How Much Should an Agent Remember?](https://arxiv.org/abs/2611.26361); **2026-11-19 v1** | adjacent text guideline consolidation; arXiv abstract + IAAI 2027 oral comment checked. model-dependent memory budget |
| A75 | [Yue et al., Replay, Don't Resample](https://arxiv.org/abs/2611.24059); **2026-11-18 v1** | adjacent RL specialist-policy distillation; arXiv abstract checked. 1/7 compute is authors' conditional result |
| E15 | [Zeng et al., The Resolution Hypothesis](https://arxiv.org/abs/2611.23068); **2026-11-17 v1** | self-evolution evaluation; arXiv abstract checked, 7×6, 10M+ calls are authors' conditions; no neural schema training demonstrated |
| E16 | [Tan et al., Evolve Where It Matters / SkillPlumber](https://arxiv.org/abs/2611.25429); **2026-11-19 v1** | procedural instruction self-evolution, external natural-language skills; arXiv abstract checked; not continuous schema |

**다른 보고의 범위:** Sleep-time의 LaFlash·CAIMS 등 HBF/serving 논문은 이번 neural SBL 동기화에 이관하지 않았다. 직접 관련 판단이 새로 생기면 출처를 유지한 별도 컴퓨트 노트에서 검토한다. 기존 SBL bibliography/TEM/CSCG/S-HAI의 분류와 읽기 범위는 바꾸지 않았다.

**원문 확인:** 2026-11-23에 공식 arXiv landing/abstract 및 선택 HTML, PubMed TPAMI metadata/abstract, Symmetry publisher 본문 일부를 확인. 학술지 DOI full text 접근 실패나 arXiv 이전 판본을 2026-11 신규 원문으로 오인하지 않는다. 원저자 수치·논문 상태의 독립 실험 검증 없음.

## 2026-11-24 보충 — 이전 Sleep-time 보고의 recurrent architecture 두 편

기존 10개 선별 범위에 대한 과거 기록은 유지한다. 추가 근거 및 읽은 범위는 [recurrence 비용 통제](../research/2026-11-24-recurrence-cost-controls.md) 참조.

| ID | 원문 / 공개일 | 확인 범위 |
|---|---|---|
| S166 | [Huang et al., Latent Feedback Is a Compute and Data Amplifier](https://arxiv.org/abs/2611.20404v1), v1 2026-11-16 | 11/24 arXiv 초록 및 HTML §1–4, §5 일부·표 발췌; [저자 코드 링크](https://github.com/ifm-ai/LoRM), 실행 안 함. Token recurrence, not continual schema |
| S167 | [Jin et al., Late Entry in Looped Language Models](https://arxiv.org/abs/2611.24576v1), v1 2026-11-18 | 11/24 arXiv 초록, HTML 그림 1 설명, 실험·한계·concurrency 부록 발췌. Depth recurrence decode, not continual schema |

두 논문 모두 기존 주간 보고에서 재선별한 preprint이며, 새 발표 또는 Melete 실험 결과가 아니다.
