# docs/18 비모수 POC(P0)의 부록: 색인·새 참고문헌·조사 출처 (2026-11-18)

**상태 라벨:** 설계 작업 기록의 부록(PROPOSAL / OPEN / NOT RUN)이다. [18-poc-nonparametric.md](../../docs/18-poc-nonparametric.md) 초안 끝의 세 부록을 공개 문서에서 떼어 이곳에 둔다. 초안 원문이므로 가칭(DC-·F-NEW-·NEW-로 시작하는 번호)을 그대로 두었고, 최종 번호는 [id-map.tsv](../../research/2026-11-18-blueprint-et-design/id-map.tsv)와 [2026-11-18-blueprint-et-design.md](../../research/2026-11-18-blueprint-et-design.md)의 대응표에 있다. 작성일 2026-11-18.

## 부록 A. 색인

### 소유 정의 위치

지시문 §3-2에서 이 초안(W3)이 소유하는 정의가 이 초안의 어느 절에 있는지의 표다.

| 소유 정의 | 위치 (절 번호와 제목) |
|---|---|
| P0 제품 정의 | §2 P0 제품 정의: System ONE-NP (UJ0은 §2.1 전체 여정 UJ0) |
| NP 대역 상세 | §2.5 NP 단 정의, §3 BF feature와 비모수 대역의 대응 |
| suite S-A ~ S-D 설계 | §5 suite 설계 |
| V0 목록 | §4 검증 목록 V0 |
| P0 작업 표 | §12 P0 작업 표, 종료 gate, 절삭 순서 |
| P0 실행 행렬(세계 수, arm, checkpoint, probe) | §10 P0 실행 행렬 |
| P0 결과에 따른 분기 | §14.2 NP가 대조군을 이기지 못할 때의 해석과 다음 행동 |

### 이 초안이 정의한 ID

| 종류 | ID | 위치 |
|---|---|---|
| 검증 항목 | V0-1 ~ V0-17 | §4.1, §4.2 |
| 사용자 여정 단계 | UJ0의 ① ~ ⑭ | §2.1 |
| 사전 판정 규칙 형식 | 형식 A ~ F | §4.3 |
| 작업 | P0-T01 ~ P0-T21 | §12 |
| 실행 행렬의 행 | P0-R01 ~ P0-R16 | §10.2, §10.3 |
| arm 이름(가칭) | `np0`, `np1`, `np2`와 대조 arm | §7.1 |
| backend, 검색 key | `gguf`, `hf`, `lexical`, `hidden`, `embed` | §11.2, §2.3 |
| CLI 명령(가칭) | `fcl session`, `experience`, `ask`, `et` 등 | §2.4 |

### 남의 정의를 가리킨 곳

| 가리킨 정의 | 소유 | 이 초안의 위치 |
|---|---|---|
| BF-A1 ~ BF-H4의 ID와 이름, flow FL-1 ~ FL-6, 경로 이름(fast / learn / deep / hold), CRUD 판정 이름(read / update / branch / create / hold / evict) | docs/16 | §2.1, §2.5, §3 |
| ET 운영 정의, stream 항목 종류(READ / OBSERVE / NOTE / QUESTION / DISCUSS / TRY), 입력 tier, 대조 stream, 발견 곡선 지표, 발견 수준 L0 ~ L5와 대상별 rubric, ET 단 정의와 단별 상한·문구, 통과 기준 | docs/17 | §2.4, §5.2, §6 |
| phase 정의, 종료 gate의 로드맵 서술, 회귀 gate, UJ1, UJ6, capability × phase 표, 결정 번호(D-, N-) | docs/09 | §1.4, §2.1, §12.1, §14.3 |
| 논문 주장과 초록 | docs/19 | §3.1, §14.2 |
| token, GPU-시간, 비용 | docs/15 | §10, §11.4 |
| state 계약과 manifest 서식 | docs/07 | §2.3, §11.3 |
| 평가 family F01 ~ F24, 통계 틀, 결과 상태 | docs/08 | §4, §5, §9 |
| 실험 B와 schema 중첩 가설 | docs/13 | §5.4 |
| CRUD 생명주기, 「못 찾으면 create」의 해석(N-4) | docs/14 | §3, §4.1 |
| 통찰의 운영적 정의 | docs/11 | §3, §5.2 |
| H-DISCOVER 문장 | 지시문 MD-1118-N(docs/17이 소유) | §4.1 (문장 그대로 인용) |

### 가칭 목록

| 가칭 | 한 줄 요약 |
|---|---|
| DC-W3-01 | frozen LLM 주 모델, 복제 모델, backend와 가중치 확보 |
| DC-W3-02 | NP-2를 「비모수」 대역에 포함할지 |
| DC-W3-03 | P0 종료 gate에 sealed readout(등급 3 시도)을 포함할지 |
| DC-W3-04 | 「실제 갱신」을 「실제 비모수 state 쓰기」로 읽을지 |
| DC-W3-05 | hold 경로를 P1 controller v0에도 넣을지 |
| DC-W3-06 | P1 base 크기(135M급 유지 또는 1.7B ~ 4B급 상향) |
| DC-W3-07 | 구현 위치와 Melete 파일 이관 방식 |
| DC-W3-08 | 계열 대조의 충실도(간이판 또는 공식 구현) |
| DC-W3-09 | NP-0의 생성과 판정의 분리 방식 |
| F-NEW-W3-a | 지연 해소 불일치(긴장 보존) family |
| F-NEW-W3-b | 원리 도출과 귀결 예측 family |
| F-NEW-W3-c | 잠재 artifact 재적재와 합성 family |
| NEW-W3-01 ~ NEW-W3-06 | 새 참고문헌 6건(부록 B) |

## 부록 B. 새 참고문헌

catalog 8열(id, title, category, date_note, url, code_url, status, note) 서식이다. id는 통합 때 catalog의 최종 번호로 바꿨고 괄호에 가칭을 남겼다(같은 URL이 다른 초안에도 있는 행은 먼저 온 행으로 합쳤다). 이 초안은 전문을 읽지 않았으므로 status는 metadata-checked이고 읽은 범위는 note에 적었다. code_url은 확인하지 않아 비웠다.

| id | title | category | date_note | url | code_url | status | note |
|---|---|---|---|---|---|---|---|
| S70 (가칭 NEW-W3-01, 같은 URL의 다른 행과 합침) | Generalization through Memorization: Nearest Neighbor Language Models | adjacent-mechanism | Khandelwal, Levy, Jurafsky; arXiv v1 2019-11-01; ICLR 2020(arXiv Comments 표기) | https://arxiv.org/abs/1911.00172 | | metadata-checked | 2026-11-18 abs 페이지의 초록만 확인. LM의 embedding 공간에서 찾은 이웃과 LM 예측을 선형 보간하고 추가 학습이 필요 없다고 서술(저자 서술). NP-1 hidden-state kNN 결합의 근거 후보. 전문 미독, 재현 안 함 |
| S71 (가칭 NEW-W3-02, 같은 URL의 다른 행과 합침) | Memorizing Transformers | adjacent-mechanism | Wu, Rabe, Hutchins; arXiv v1 2022-03-16; ICLR 2022 spotlight(abs 표기) | https://arxiv.org/abs/2203.08913 | | metadata-checked | 2026-11-18 abs 페이지의 초록만 확인. 과거 (key, value) 쌍의 미분 불가능한 기억에 근사 kNN 조회를 하는 확장. 기억 쓰기 방식은 초록에 없다. 모델은 학습된 구조이므로 P0의 frozen 사용과 다르다. 전문 미독 |
| S69 (가칭 NEW-W3-03, 같은 URL의 다른 행과 합침) | In-Context Learning Creates Task Vectors | adjacent-mechanism | Hendel, Geva, Globerson; arXiv v1 2023-10-24 | https://arxiv.org/abs/2310.15916 | | metadata-checked | 2026-11-18 abs 페이지의 초록만 확인. in-context learning이 학습 set을 하나의 task vector로 압축하고 그 vector가 transformer를 조절한다는 주장. 초록에는 vector가 놓이는 공간(활성값인지 가중치인지)이 적혀 있지 않다. 전문 미독 |
| S112 (가칭 NEW-W3-04, 같은 URL의 다른 행과 합침) | In-context Vectors: Making In Context Learning More Effective and Controllable Through Latent Space Steering | adjacent-mechanism | Liu, Ye, Xing 등; arXiv v1 2023-11-11 | https://arxiv.org/abs/2311.06668 | | metadata-checked | 2026-11-18 abs 페이지의 초록만 확인. demo에 대한 forward의 latent 표현으로 vector를 만들고 latent 상태를 그 vector로 이동하며 크기로 효과를 조절한다는 서술. 전문 미독 |
| S113 (가칭 NEW-W3-05, 같은 URL의 다른 행과 합침) | Steering Language Models With Activation Engineering | adjacent-mechanism | Turner, Thiergart, Leech 등; arXiv v1 2023-08-20 | https://arxiv.org/abs/2308.10248 | | metadata-checked | 2026-11-18 abs 페이지의 초록만 확인. prompt 쌍의 중간 활성값 차이로 steering vector를 만들어 추론 중 forward에 더하고 기계 최적화가 필요 없다고 서술. 전문 미독 |
| S160 (가칭 NEW-W3-06) | A Tutorial on Bayesian Nonparametric Models | adjacent-mechanism | Gershman, Blei; arXiv v1 2011-06-14 | https://arxiv.org/abs/1106.2697 | | metadata-checked | 2026-11-18 abs 페이지의 초록만 확인. 모델 복잡도를 데이터가 정하게 하는 베이즈 비모수 방법의 개관. CRP와 Dirichlet process는 초록에 언급되지 않아 CRP 자체의 1차 출처는 확인하지 못했다(미확인). 전문 미독 |

## 부록 C. 조사 출처

접근일은 모두 2026-11-18이다. 외부 조회에는 논문 제목과 공개 페이지 주소만 썼고 계정, 사용자 이름, 비공개 경로는 쓰지 않았다. 유료 API, 인스턴스 생성, 가중치 다운로드는 하지 않았다.

| URL 또는 대상 | 접근일 | 읽은 범위 | 확인 수준 |
|---|---|---|---|
| https://huggingface.co/Qwen/Qwen3-8B | 2026-11-18 | 모델 카드 페이지: 라이선스, 파라미터 수, 문맥 길이, 지식 마감 표기 여부(없음), 가중치 형식 | 공식 모델 카드 확인. 실행 호환성은 NOT RUN |
| https://huggingface.co/Qwen/Qwen3-8B-Base | 2026-11-18 | 모델 카드 페이지: 학습 단계(Pretraining), 라이선스, 파라미터 수, 문맥 길이, 지식 마감 표기 여부(없음) | 공식 모델 카드 확인 |
| https://huggingface.co/HuggingFaceTB/SmolLM2-135M | 2026-11-18 | 모델 카드 페이지: 크기 3종, 구조, 라이선스, 사전학습 token, 가중치 형식, 지식 마감 표기 여부(없음) | 공식 모델 카드 확인 |
| https://arxiv.org/abs/2310.15213 (S26) | 2026-11-18 | abs 페이지의 초록 | metadata-checked 수준. catalog 기록(discussion-import)은 그대로 둔다 |
| https://arxiv.org/abs/2310.15916 | 2026-11-18 | abs 페이지의 초록 | metadata-checked |
| https://arxiv.org/abs/2311.06668 | 2026-11-18 | abs 페이지의 초록 | metadata-checked |
| https://arxiv.org/abs/2308.10248 | 2026-11-18 | abs 페이지의 초록 | metadata-checked |
| https://arxiv.org/abs/1911.00172 | 2026-11-18 | abs 페이지의 초록 | metadata-checked |
| https://arxiv.org/abs/2203.08913 | 2026-11-18 | abs 페이지의 초록 | metadata-checked |
| https://arxiv.org/abs/1106.2697 | 2026-11-18 | abs 페이지의 초록 | metadata-checked |
| host의 llama.cpp 빌드(빌드 11446) | 2026-11-18 | `--help` 출력의 옵션 목록과 빌드에 포함된 실행 파일 목록. 모델 실행은 하지 않았다 | 직접 확인(옵션과 실행 파일의 존재만). 성능과 호환성은 NOT RUN |
| host의 Python 패키지 목록 | 2026-11-18 | torch, transformers 등의 설치 여부 확인 | 직접 확인 |
| Melete 저장소의 고정 커밋 1d95136c3a64580ec25bc588c96c191eecb85b41 | 2026-11-18 | 비공개 저장소의 파일 목록, 모듈 머리글, 함수 이름. 코드 내용과 상수는 옮기지 않았다 | ARCHIVE. 재실행·재검증 안 함 |
| 이 저장소의 문서 | 2026-11-18 | [09-roadmap.md](../../docs/09-roadmap.md) 전체(§10까지), [08-evaluation.md](../../docs/08-evaluation.md) §1 ~ §8, [13-schema-decomposition-and-interference.md](../../docs/13-schema-decomposition-and-interference.md) §1 ~ §5와 §10, [14-schema-lifecycle-crud-and-joint-paper.md](../../docs/14-schema-lifecycle-crud-and-joint-paper.md) §1 ~ §8, [11-research-agenda.md](../../docs/11-research-agenda.md) §1 ~ §4, [07-state-and-storage.md](../../docs/07-state-and-storage.md) §1 ~ §2, [12-melete-lineage.md](../../docs/12-melete-lineage.md), [15-compute-plan.md](../../docs/15-compute-plan.md) §4.1·§5.1·§7.4, [catalog.tsv](../../references/catalog.tsv) | 저장소 문서로서 읽음 |
