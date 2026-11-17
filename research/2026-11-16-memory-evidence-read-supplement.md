# 2026-11-16 추가 교차 검토: evidence-linked / multimodal memory retrieval

## 근거와 범위

**ARCHIVE (부분 회수):** 독립 Sleep-time Compute 주간 조사 대화에서 이전 8편 선별 기록에 포함되지 않은 **WikiTrace**와 **HiVe-Mem** 두 연구를 발견했다. 자동화 본문 전체는 이 실행에서 재확보하지 못했고, 선별 후보는 접근 가능한 이전 대화의 주제별 검색 요약을 통해 확인했다. 이후 **각 논문의 공식 arXiv 초록·저자·최초 제출일을 이번 실행에서 별도로 검증**했다. 기존 [8편 교차검토](2026-11-16-sleep-time-melete-integration.md)를 바꾸지 않는다. **11월 16일 신규 발표가 아니라 11월 9~10일 공개된 자료의 추가 선별**이다.

**LITERATURE / abstract-verified:** 아래 정량 내용은 원 저자의 주장으로서 원문 전체/부록의 독립 정독이나 실행 검증을 뜻하지 않는다. **NOT RUN:** 모델 실험, GPU, 코드 실행, 성능 재현 모두 수행하지 않았다. 두 연구의 external agent memory를 continuous neural schema 학습이나 세션 간 parametric continual learning으로 재분류하지 않는다.

## 새로 선별한 두 논문

| 논문 / 최초 제출 | 표현과 학습 범위 | 초록에서 확인한 결과·한계 | 링크 |
|---|---|---|---|
| **WikiTrace: Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents.** Yukyeong Lee, Yumin Choi, Jinheon Baek, Sung Ju Hwang. **2026-11-10**, arXiv 2611.14320 v1 | **External agent memory**, 경험 교훈–근거 요약–원본 trajectory의 연결. Neural schema를 직접 학습하거나 기존 LLM 가중치를 지속 수정했다는 증거가 아님 | 관련 교훈이 잘못되거나 문맥에 맞지 않을 때 오히려 기존에 풀던 과제의 성능을 악화시키는 memory-induced degradation에 대응. 부족·충돌·실패 경험의 교훈에 대해 원본 근거를 재검토하며, 저자는 **5개 agent benchmark**에서 개선을 보고. 정확한 수치/ablation은 이번 초록 확인 범위에 없음 | [공식 arXiv](https://arxiv.org/abs/2611.14320), [공개 저자 코드](https://github.com/yukyeongleee/wikitrace) |
| **HiVe-Mem: Interleaving Horizontal Memory Expansion and Vertical Evidence Composition for Multimodal Agents.** Haozhen Zhang 외 7인. **2026-11-09**, arXiv 2611.12872 v1 | **External multimodal episodic memory + trainable evidence selector**. Text/visual anchor 관계로 episode 후보 확장; 요약·캡션·이미지·원본 이력 중 필요한 증거 형태 선택. 지속적 neural schema update가 아님 | 저자 초록은 **3개 multimodal memory benchmark**에서 성능 개선과, 가장 효율적인 비교 multimodal baseline 대비 **토큰 사용량 약 90% 감소**를 보고. Melete의 학습·지연·총비용 개선과 동일시할 수 없음 | [공식 arXiv](https://arxiv.org/abs/2611.12872) |

두 항목 모두 공개 **arXiv preprint**로 취급한다. 학회 채택을 추정하지 않는다. WikiTrace의 공개 GitHub 저장소 존재는 확인했지만 설치·재현하지 않았다. HiVe-Mem의 저자 인증된 코드·태그·재현 가능성은 검증하지 않았다.

## Melete 연결: 설계 가설과 반증 실험 (PROPOSAL / OPEN)

### Read / Activate: 잘못된 기억의 선택 자체가 성능 회귀를 만들 수 있다

- Schema retrieval key가 유사하다고 schema artifact를 그대로 신뢰하지 않는다. 필요한 경우 **원본 관측→파생 교훈→schema version**의 증거 계보를 확인하는 별도 Read 경로를 후보로 둔다.
- 같은 expert pool을 고정하고 **no-memory / schema-only / 근거 확인 가능한 schema / oracle selector**를 비교한다. 동일 accuracy에서 query-time 근거 토큰, 재적재 지연, p50/p95, 기존에 풀던 과제에서의 회귀율을 분리 측정한다.
- External evidence를 프롬프트로 다시 읽는 행위와 low-rank expert를 활성화하는 행위는 서로 다른 연산이며 토큰/저장/계산 비용을 나눠 보고한다.

### Update / Create, Delete / Retain: 변경의 출처와 가역성을 보존한다

- 생성된 해설·교훈을 독립된 관측으로 승격하지 않는다. Source provenance, 신뢰도, 사용 맥락과 버전 의존성을 기록해 **오염된 교훈의 잘못된 write/promotion**을 검사한다.
- Offload된 원본 경험, 압축된 요약, neural schema의 파라미터 상태, 삭제된 source를 구분한다. 출처 연결이 단절된 압축과 실제 비가역 폐기는 다른 비용을 만든다.
- HiVe-Mem의 관계 기반 후보 확장과 요청별 evidence granularity는 **Read 비교군**으로 참고한다. Graph 기반 외부 검색이 곧 연속 schema나 neural consolidation이라는 뜻은 아니다.

### 검증의 기준

관계 공유의 새 개체/수치, 표면 유사하지만 구조가 반전된 문제, ABA 재방문, 잘못 생성된 교훈이 섞인 경험 흐름에서 **기억 선택의 실패, schema 내용의 손상, 잘못된 write, 근거 재검토의 비용**을 구분한다. Schema 원인효과는 여전히 parameter intervention/lesion과 controlled update로 확인해야 한다.

## 이번 선별에서 제외한 인접 자료

**TreeAgent**([arXiv:2611.13946](https://arxiv.org/abs/2611.13946), 2026-11-10)는 JSON/HTML/YAML의 계층형 입력을 잘라 읽는 외부 memory agent 관련 연구이므로 neural schema의 직접 근거로 세지 않았다. 제목이 불명확한 다른 Recursive Memory 언급은 논문 버전·범위가 확인되지 않아 이관하지 않았다. 원 자동화 보고 전체가 확보됐다고 주장하지 않는다.

**OPEN (2026-11-17 검토):** 위 '제목이 불명확한 다른 Recursive Memory 언급'이 [2026-11-17-sleep-time-melete-selected-addendum.md](/home/jimmy/repos/full-continual-learning/research/2026-11-17-sleep-time-melete-selected-addendum.md)의 arXiv:2611.13760(Recursive memory for prediction and generation)과 같은 대상인지는 원 보고를 확보하지 못해 확인할 수 없다. 같은 대상이라고 가정하지 않는다. TreeAgent(arXiv:2611.13946)는 공식 abs에서 표제 'TreeAgent: Structure-Aware Memory Agent for Processing Long Hierarchical Data', 2026-11-10 v1임을 확인했다. HiVe-Mem arXiv 페이지의 Comments에 코드 링크(github.com/ViktorAxelsen/HiVe-Mem)가 표시된다(저장소 내용·실행 미확인이므로 위 '코드 미검증'은 유지한다). WikiTrace 페이지에는 ACL Rolling Review(2026-10 cycle) 심사 중이라는 저자 표기가 있다(채택이 아니다).

관련: [Schema CRUD·Ali 공동연구안](../docs/14-schema-lifecycle-crud-and-joint-paper.md), [평가 명세](../docs/08-evaluation.md), [동기화 기록](../sources/sync/manifest.json).
