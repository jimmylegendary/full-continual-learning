# 2026-11-17 FCL 관련 Sleep-time 조사 보충 — SoMem와 recursive state capacity

## 범위와 증거 수준

**ARCHIVE / discussion-import:** 2026-11-16 독립 「Sleep-time Compute 주간 동향」(조사 기간 2026-11-09~15)의 접근 가능한 결과에서, 이미 선별한 8편 및 WikiTrace/HiVe-Mem 보충과 구별되는 두 연구를 추가 선택했다. 새로 출판된 11월 17일 논문이 아니라 **11월 9~10일 최초 공개된 이전 보고의 미반영 항목**이다. 완전한 주간 보고 원문·모든 대화 로그를 확보했다고 주장하지 않는다.

**LITERATURE / official-source checked (2026-11-17):** 공식 arXiv 공개 페이지의 저자·초록·최초 공개일과 내용의 일부를 확인했다. SoMem은 공식 페이지가 안내한 GitHub 저장소의 존재를 확인했다. 이번에 PDF 전문·부록 전체를 정독하거나 코드/성능을 재현하지 않았다. 정량 결과는 원 저자 보고값이다. 모두 사전심사 상태를 단정하지 않는 **arXiv preprint**로 분류한다.

**NOT RUN:** Melete/System ONE 구현, GPU 학습·평가·serving 실행, 외부 메시지 발송 0회.

## 1. 외부 근거를 보존하면서 조직을 바꾸는 SoMem

- **논문:** [Can LLM Agents Organize Their Own Memory?](https://arxiv.org/abs/2611.11929), Zichuan Fu, Junjia Qi, Wenlin Zhang, Yimin Deng, Shirong Wang, Jinyang Li, Xian Wu, Xiangyu Zhao. **2026-11-09 최초 공개(v1)**.
- **공식 코드:** [Qi202/SoMem](https://github.com/Qi202/SoMem). 공개 저장소 존재만 확인했으며 clone·실험하지 않았다.
- **표현:** 가중치가 동결된 agent의 **외부 연결 문서(Source/Topic/Core 및 파생 View)**. Continuous latent schema나 neural parametric continual learning이 아니다.
- **형성/수정/읽기:** 새 interaction 원본을 Source로 보존하고, agent가 Topic 문서를 재조직하며, runtime은 근거 링크의 유효성을 검사하고 Graph·Timeline·Recent view를 재구성한다. Query는 단계별 검색·읽기와 원본 근거 확인을 포함한다.
- **저자 초록 수치:** LoCoMo **+2.66 percentage points**, BEAM-100K **+3.10 pp**, LongMemEval-S **+2.00 pp** (각각 저자가 비교한 가장 강한 baseline 대비). FCL schema update의 학습·망각·총비용 개선 수치가 아니다.
- **한계:** 발표의 외부 memory 성공은 새로운 과제의 parametric schema 형성, 구조 전이, low-rank expert 간섭 제어를 보여주지 않는다.

**PROPOSAL — Melete 연결:** schema artifact의 `원본 경험 → 파생 해석/근거 → expert version → 읽기 index` 계보를 명시한다. 신경 상태의 in-place update와 검색용 view 재구성을 다른 연산으로 구분하고, update 후 stale index·근거 손실·추론 회귀를 평가한다. 기존 [WikiTrace/HiVe-Mem 보충](2026-11-16-memory-evidence-read-supplement.md)과는 **원본 근거를 보존하면서 재조직된 문서에 대한 접근 view를 재구축하는 정책**이라는 점을 별도 비교군으로 둔다.

## 2. Recurrence의 읽기 충분성과 상태 갱신 충분성은 다르다

- **논문:** [Recursive memory for prediction and generation](https://arxiv.org/abs/2611.13760), Pengbin Feng, Chunlei Meng. **2026-11-10 최초 공개(v1)**, arXiv preprint (stat.AP).
- **표현:** 고정 크기의 recurrent/state-space 상태 및 유한 상태 관찰자·생성기. Schema를 직접 정의하거나 학습한 논문이 아니다.
- **핵심 조건부 결과:** 양의 전이확률을 가진 알려진 HMM에서 미래 사건 질의를 상대 오차 \(\varepsilon\)로 응답하는 상태는 \(O(\log(1/\varepsilon))\) 비트로 충분할 수 있다. 반면 자기 출력 토큰으로 상태를 결정적으로 갱신하는 **unifilar 생성기**의 장기 연쇄 생성(총 오차 예산 고정)에서는 특정 2-state 사례의 필요 상태가 \(\Theta(\log(T/\varepsilon))\)로 커진다. 비공개 내부 난수/숨은 상태를 허용하거나 token당 평균 손실로 예산을 바꾸면 시간 길이 \(T\)에 대한 추가 항이 사라질 수 있다.
- **해석 경계:** 이 결과는 정의된 확률원천, 상태 종류, 오차 척도, update 제약에 의존한다. **모든 LLM의 fixed-size memory 불가능성이나 전체 schema 저장 용량 하한을 증명하지 않는다.** 학술지 최종 게재나 외부 재현은 확인하지 않았다.
- **코드:** 공식 arXiv 페이지에 ancillary computational files가 표시되지만, 이번 실행에서 재현 또는 별도 저자 GitHub 구현 검증은 하지 않았다.

**OPEN (2026-11-17 검토, arXiv 페이지와 HTML 본문 대조):** (1) 사건 질의 결과의 오차 척도는 log-확률(곱셈) 오차이고, 위의 로그 크기 결과는 2-state 사례에서 Θ(log(1/ε))로 서술되며 일반 상태에는 별도 상계가 주어진다. 생성 하한 Θ(log(T/ε))는 nondegenerate 2-state 모형에 대한 것이고, 예산은 길이 T 이하 모든 단어에 대한 uniform 오차이거나 길이 T 전체 예측의 expected total KL(token당 평균이 아님)이며, 하한은 가중치(갱신 규칙)가 고정되고 상태 갱신이 결정적인 모형을 전제한다(비공개 상태는 범위 밖). 비공개 상태를 허용하거나 token당 KL 예산을 쓰면 T 의존이 사라진다고 논문이 직접 서술한다. §6.3은 자기회귀 모델에 대한 적용을 가정을 단 조건부로만 논의하고 §6.4는 2-state를 넘는 확장을 열린 문제로 둔다. 논문에는 schema·continual learning·forgetting 논의가 없다. (2) 여기서 recursive는 token 시계 위의 상태 재귀(recurrent update)이며 [07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md) §1의 recursion index(같은 관측에 대한 내부 계산 깊이)가 아니다. (3) 아래 §3의 연결 서술은 **제안**이며 docs/05·08·14에는 280dc9a 기준으로 반영돼 있지 않았다([14-schema-lifecycle-crud-and-joint-paper.md](/home/jimmy/repos/full-continual-learning/docs/14-schema-lifecycle-crud-and-joint-paper.md) §10은 8건만 가리킨다). 이 검토가 후보를 07 §5·§7, 08 F24(F-CI)·§4, 09 P2·P4, 05 §11의 주석으로 넣었다. 반영 후보는 [07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md) §5, [08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md)의 F-CI, [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md) P2·P4의 후보 readout이다.

**PROPOSAL — Melete 연결:** persistent schema artifact가 현재 예측에 충분하더라도, 이후의 관측/자체 생성 결과로 계속 수정할 수 있는 **update-sufficient state**인지는 별도 문제다. Shared recursive core·CMS·Titan fast state·Delete/Retain에서 다음을 구분한다.

1. 고정된 질문에 대한 현재 read 정확도.
2. 긴 continuation 동안 state를 갱신한 뒤의 read 정확도와 복구 가능성.
3. 같은 오차 기준에서 state bits/precision·active bytes·external storage·update FLOPs와 retrieval cost.
4. 실제 사용자 경험에 의한 외부 관측 업데이트와 모델의 자기 생성 토큰을 이용한 내부 상태 업데이트.

**OPEN / 반증 실험:** 동일한 현재 질의 정확도로 state를 압축한 두 모델이 긴 연쇄 생성·관측 후 같은 성능을 유지하는가? Read-sufficient, update-sufficient, snapshot+retrieval을 통제된 생성과 재방문 과제에서 비교한다. 결과를 schema 간섭/망각의 입증으로 포장하지 않는다.

## 3. 기존 연구·설계에 대한 연결

[Schema CRUD / Ali 공동논문 설계](../docs/14-schema-lifecycle-crud-and-joint-paper.md)의 **Delete/Retain**은 표현 크기뿐 아니라 미래 갱신에 필요한 상태를 평가한다. **Read/Activate**는 근거 조회와 expert activation, 검색 index 재구성을 구분한다. [통합 모델](../docs/05-integrated-architecture.md)의 recursive/depth state는 외부 지속 schema의 버전 상태와 동일시하지 않는다. [평가](../docs/08-evaluation.md)에서는 query accuracy뿐 아니라 continuation integrity와 storage/compute amortization을 추가 후보 지표로 둔다.

본 기록은 기존 [8편 Sleep-time 선별](2026-11-16-sleep-time-melete-integration.md)과 [2편 evidence-read 보충](2026-11-16-memory-evidence-read-supplement.md)을 수정하거나 중복 주장하지 않는 **추가 선별**이다. 서로 다른 benchmark 결과를 직접 비교하지 않는다.
