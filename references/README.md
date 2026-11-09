# 참고문헌·공식 구현 전체 목록

원천 데이터: [catalog.tsv](catalog.tsv). `N`=기억/인지, `R`=리듬/가소성, `S`=SBL·표상·평가, `A`=아키텍처, `E`=자동 연구/진화. 논문과 관련 공식 코드 URL을 한 record에 연결한다. TSV는 GitHub에서 표로 열거나 프로그램으로 읽을 수 있다.

## 확인 수준

- `metadata-checked`: 이번 이관에서 공식 arXiv/학회/저널 metadata를 확인했다. 전체 본문 수치의 독립 재검증은 아니다.
- `official-search-checked`: 공식 원문 검색 결과에서 제목/식별자 확인.
- `discussion-import`: 이전 대화/PDF의 참고문헌과 보고를 보존. 이번 작업에서는 재확인하지 않았다.
- `needs-resolution`: 대화에서 언급됐지만 제목/고정 URL의 정확한 대응이 아직 필요하다. 이름·DOI를 만들어 채우지 않는다.

**모든 항목을 읽고 재현했다는 목록이 아니다.** 이 저장소는 자료의 존재/metadata, 원 논문 주장, Melete로의 설계 추론, 실제 재현을 분리한다. 날짜도 최초 공개/개정/게재를 나누며 과거 답변의 최신 상태를 현재 최신이라고 자동 확정하지 않는다.

## 핵심 읽기 경로

### 이론

- N11 [Complementary Learning Systems](https://pubmed.ncbi.nlm.nih.gov/7624455/)
- N12 [Schemas and Memory Consolidation](https://pubmed.ncbi.nlm.nih.gov/17412951/)
- N23 [Schema 정의 검토](https://pubmed.ncbi.nlm.nih.gov/24280650/)
- N07 [Latent-cause memory modification](https://elifesciences.org/articles/23763)
- N03 [기억 전환 회로](https://doi.org/10.1038/s41593-026-02280-6)
- N21/S01 [Tolman–Eichenbaum Machine](https://pmc.ncbi.nlm.nih.gov/articles/PMC7707106/)

### Continuous schema

- S03 [Goudar: population subspace](https://doi.org/10.1038/s41593-023-01293-9)
- S05 [Sequence attractor schema](https://proceedings.nips.cc/paper_files/paper/2025/hash/0a88e621aacf222d3a91d8065c40e4d9-Abstract-Conference.html)
- S06 [Sleep의 dimensionality reduction](https://doi.org/10.64898/2026.05.27.728344)
- S07 [Hippocampo-neocortical compressive RAG](https://doi.org/10.1038/s41467-026-74357-6)
- S23 [Low-rank recurrent schema](https://www.biorxiv.org/content/10.64898/2026.04.10.717706v1.full)
- S24 [Task Schema and Binding](https://arxiv.org/abs/2512.17325)

### 통합 모델의 재료

- A01 [Titans](https://arxiv.org/abs/2501.00663)
- A02 [Nested Learning / HOPE](https://arxiv.org/abs/2512.24695)
- A03 [Language Models Need Sleep](https://arxiv.org/abs/2606.03979)
- A04 [Titan-Llama](https://arxiv.org/abs/2610.19210), [저자 fork](https://github.com/sarahpannn/titans-pytorch)
- A06 [Looped Transformers](https://arxiv.org/abs/2502.17416), A07 [Recurrent Depth](https://arxiv.org/abs/2502.05171)
- A08 [MoD](https://arxiv.org/abs/2404.02258), A09 [MoR](https://arxiv.org/abs/2507.10524)
- A10 [Depth-Attention](https://aclanthology.org/2026.emnlp-main.2085/), A11 [AttnRes](https://arxiv.org/abs/2603.15031), A12 [MoDA](https://arxiv.org/abs/2603.15619)
- A13 [Retrofitted Recurrence](https://arxiv.org/abs/2511.07384), A14 [ETD](https://arxiv.org/abs/2510.07358), A15 [Relaxed Recursive Transformers](https://arxiv.org/abs/2410.20672)

## 분류 규칙

`neural-continuous`, `symbolic`, `discrete-latent`, `hybrid`, `neuroscience`, `adjacent-mechanism`, `evaluation`, `evolution`을 구별한다. 표현과 지속학습은 별도다. Neural activation patching은 세션 간 학습을 자동 의미하지 않고, 확률적 graph는 continuous neural schema와 같지 않다.

S-HAI의 다중 grounding을 다중 schema 생성으로, Spens의 narrative Mistral+xRAG+LoRA와 별도 GPT-2 실험을 한 모델의 통합 성과로 바꾸지 않는다. CLS episodic adapter를 곧바로 추상 schema로 부르지 않는다.

## 재생성

`python tools/export_references.py`는 TSV에서 JSON/BibTeX를 생성한다. TSV의 일부 제목은 PDF의 설명형 표제이며 `note`에서 이를 명시한다. 저자·DOI·venue를 확실히 모르면 가짜 metadata를 넣지 않는다. 생성 BibTeX는 문헌관리 초안으로, 출판 제출 전 공식 citation과 대조해야 한다.
