# Full Continual Learning — Melete / System ONE

**경험이 다음에 무엇을 이해하고, 얼마나 생각하며, 무엇을 어떻게 배울지까지 바꾸는 하나의 모델.**

이 저장소는 Melete를 출발점으로 논의한 schema-based learning(SBL), 지속학습, 빠른 적응, 가변 깊이 추론, 뇌 리듬에서 영감을 얻은 조율, 기존 LLM의 점진적 retrofit을 통합하는 연구 기반이다. 최신 논의 반영: **2026-11-22**([Ali 미팅 이후 A/B/C 비교 실험](research/2026-11-22-ali-abc-evaluation.md), PROPOSAL / NOT RUN). 이상 청사진·비모수 POC·단계별 계획·아인슈타인 테스트의 전체 설계 기준은 **2026-11-18**이며 이번에는 비교·판정 조건을 보완했다. 직전 기준일은 2026-11-17(델타 설계 반영 감사·계산 계획)이고 그 앞은 2026-11-12(설계 반영 감사와 로드맵 재구성)이며, 백서는 2026-11-12 기준에 머문다.

추가 논의 **2026-11-14**: [Schema 정의·분해·변경 간섭](docs/13-schema-decomposition-and-interference.md) — schema/artifact 구분, LLM과의 통합 가설, 보존의 수학적 조건, 실험 A–E 및 [보충 참고문헌](references/schema-decomposition-2026-11-14.md). 연구 제안의 문서화이며 구현·효용 검증 완료가 아니다.

> 현재 상태: **연구 의도·설계·근거·검증 계획의 아카이브**. 통합 HOPE/Titan/CMS/recursive 모델의 구현·학습·성능 검증 완료를 뜻하지 않는다. 이전 합성 Phase-0 실험은 제한된 연속 prior의 표본 효율 실험이며 통합 모델 PoC가 아니다.

## 최종적으로 합의한 방향

- **하나의 통합 System ONE**: System 1/2를 별도 모델 두 개로 고정하지 않는다. 같은 모델이 문맥과 경험에 따라 얕게 답하거나 깊게 반복한다.
- **Continuous latent schema 우선**: schema를 재사용 가능한 관계·조건·계산 구조로 학습한다. `continuous representation`과 `continual learning`은 서로 다른 축이다.
- **기존 pretrained LLM에서 시작**: sequence 쪽은 Titans/Titan-Llama 계열로, FFN 쪽은 CMS로 점진적으로 전환한다. 원본 모델을 재학습 없이 기계적으로 교체하면 된다는 뜻은 아니다.
- **학습과 사고의 결합**: looped Transformer, Mixture-of-Depths/Recursions, depth attention으로 표현 재사용과 계산 배분을 연구한다. 경험 후 새로운 사례에서 같은 정확도를 더 적은 총 계산으로 달성하는지가 핵심이다.
- **상태·내용에 따른 조율**: CMS의 갱신 주기만 동적으로 바꾸는 데 그치지 않고 읽기·활성화·학습 후보·변경·통합·정보 교환을 구분한다. 뇌파의 Hz를 token 간격에 직접 대응시키지 않는다.
- **외부 schema offload / versioning / retrieval**: 후기 단계의 목표지만 상태 단위와 호환성 계약은 처음부터 설계한다.
- **점진적 해상도 로드맵 + self-evolution**: 매 phase가 실제 CLI·실제 retrofit 모델로 전체 여정을 끝까지 도는 완결 제품이고, phase마다 같은 제품의 넓이와 깊이를 함께 올린다. 목적·수치 검증·negative feedback·운영 정책을 고정하고 구현 후보를 실험으로 개선한다.

## 읽는 순서

| 문서 | 내용 |
|---|---|
| [연구 헌장과 6층위 의도](docs/01-intent-and-charter.md) | 사용자 목표, 명시적 요구, 해석, 비목표 |
| [논의의 발전과 정정](docs/02-discussion-history.md) | 외부 기억에서 통합 System ONE까지, 폐기·보류된 해석 |
| [SBL와 뇌과학 기반](docs/03-foundations.md) | CLS, schema, familiarity, 구조대응, 기억 수정·선택 |
| [뇌 리듬과 학습 조율](docs/04-rhythms-and-orchestration.md) | 위상·burst·coupling·eligibility와 공학적 가설 |
| [메커니즘과 통합 아키텍처](docs/05-integrated-architecture.md) | Titans, HOPE/CMS, Sleep, loops, MoD/MoR, depth read |
| [수학적 연구 명세](docs/06-mathematical-framework.md) | 상태, 조건부 schema, 가소성, meta-objective, 비용 |
| [상태·시계·cache·저장 계약](docs/07-state-and-storage.md) | token/experience/loop/update 구분, rollback, offload |
| [Benchmark와 판정](docs/08-evaluation.md) | transfer, rapid learning, ABA, uncertainty, compute |
| [Ali 미팅 이후 A/B/C 비교 실험](research/2026-11-22-ali-abc-evaluation.md) | Transformer / HOPE(Sleep) / Melete의 같은 정보·목표 성능·turn 비용·장기 유지, 구조 전이와 발견 평가. 사용자 원문·문헌 확인·제안·NOT RUN 구분 |
| [09-roadmap.md](docs/09-roadmap.md) | 점진적 해상도 로드맵: P1 MVP(실제 `fcl` CLI·소형 retrofit 모델·규칙형 controller v0·대조군·망각/표면 평가)부터 P5까지, capability × phase 표, 결과 등급과 상한, 열린 결정 D-01–D-14. 2026-11-18 개정으로 P0(NP)·P6(ET)와 새 결정(D-15 이후)이 보충됐다 |
| [Self-evolution와 운영 정책](docs/10-evolution-policy.md) | 독립 evaluator, 후보 계보, 예산, 승격, 실패 기록 |
| [후속 가설과 미해결 질문](docs/11-research-agenda.md) | pretraining/alignment, schema 분화, insight |
| [Schema 정의·분해·변경 간섭](docs/13-schema-decomposition-and-interference.md) | LLM과 System ONE의 공통 설명, 표현/활성화/변경 분리, 조건부 수학 명제, 실험 A–E |
| [기존 Melete와 이관 경계](docs/12-melete-lineage.md) | H1–H5와 이전 실험을 어떻게 보존할지 |
| [15-compute-plan.md](docs/15-compute-plan.md) | 계산 계획(횡단 문서): 로드맵 P1–P5가 쓰는 계산 자원 등급·시간·비용 추정(ESTIMATE / NOT RUN), 클라우드 GPU(runcrate) 사용 방식, 결정 D-04 개정 추천(PROPOSAL, 결정 대기). 별도 인프라 phase가 아니다. 2026-11-18 갱신: P0(NP)·P6(ET)와 논문별 묶음표 |
| [16-ideal-blueprint.md](docs/16-ideal-blueprint.md) | 이상 청사진(PROPOSAL): feature 그룹과 feature별 설계, flow FL-1~FL-6, feature × phase(P0–P6) 해상도 표. P0 비모수 대역은 요청된 POC이며 최종형이 아니다 |
| [17-einstein-test.md](docs/17-einstein-test.md) | 경험 조건부 발견 시험(ET, 아인슈타인 테스트의 운영 정의): ET-0~ET-4(+ET-3p), 입력 stream과 입력 tier, 누수·사후 편향 통제, 발견 곡선, 단별 결과 등급 상한(PROPOSAL / NOT RUN) |
| [18-poc-nonparametric.md](docs/18-poc-nonparametric.md) | P0(NP) 비모수 POC 설계·검증 계획: gradient 학습 0회의 System ONE-NP, 검증 V0 목록, suite S-A~S-D, 실행 행렬(ESTIMATE / NOT RUN) |
| [19-paper-plan.md](docs/19-paper-plan.md) | 단계별 논문 계획(PAPER-0~6와 0b): 주장·제목·초록 초안(결과는 자리표시자)과 논문별 실험 설계 |
| [2026-11-18-blueprint-et-design.md](research/2026-11-18-blueprint-et-design.md) | 2026-11-18 설계 작업 기록: 방법, 조사 출처와 확인 수준, 마스터 결정, 가칭 대응표, 사용자 결정 대기, NOT RUN 선언 |
| [주간 SBL 조사 기록](research/2026-11-09-sbl-tracking.md) | 대화에서 보고된 최신 연구와 수치의 출처 상태 |
| [2026-11-11-sbl-fulltext-review.md](research/2026-11-11-sbl-fulltext-review.md) | 신경망 SBL 구현 11편 원문 검토: 외부 요약 정정, 공통 공백, FCL 설계의 시작점 |
| [2026-11-12-design-audit.md](research/2026-11-12-design-audit.md) | 설계 반영 감사: 사용자 진술 202개 포함 325항목 원장, 반영 판정, 설계 문서 편집 70개, 사용자 확인·열린 결정·남은 문헌 정독 |
| [2026-11-17-design-review.md](research/2026-11-17-design-review.md) | 델타 설계 반영 감사: 11-12 감사 이후 동기화 자료(docs/13·14, 11-16·17 기록)와 사용자 공유 링크 카드의 항목별 원장, 반영한 편집, 사용자 확인·열린 결정의 갱신 |
| [README.md](whitepaper/README.md) | 시각화 설계 백서(웹 https://fcl-system-one-whitepaper.vercel.app): 17절 본문 + 결정 브리프·직관 설명·전문가 델타·지식 그래프·피드백 원장 탐색기. **2026-11-12 기준이며 11-14 이후 자료와 11-17 검토는 반영하지 않았다** |
| [전체 참고문헌](references/README.md) | 뇌과학·SBL·아키텍처·평가·진화 문헌 및 코드 |
| [원문·출처 아카이브 안내](sources/README.md) | 대화 원문/주제별 재구성/파일 출처의 차이 |
| [증거·누락·검증 범위](EVIDENCE.md) | 확인된 것, 재확인하지 않은 것, 이번 작업의 범위 |

## 핵심 검증 질문

새로운 대상·수치·표현을 가진 **같은 관계 구조의 문제**에서:

1. 과거 경험이 새 문제의 학습에 필요한 관측 수를 줄이는가?
2. 같은 정확도를 얻는 데 필요한 loop·gradient update·총 계산량이 줄어드는가?
3. 기존 구조와 어긋나는 입력에서는 적절히 보류·수정·전환·분화하는가?
4. 학습한 표현을 제거·교체하면 그 구조를 이용한 전이가 선택적으로 사라지는가?
5. Sleep과 외부 재적재 후에도 이전 조건의 유효한 판단을 유지하는가?

낮은 reconstruction loss, 많은 테스트 통과, 좋은 latent 시각화, 정확한 원문 복원만으로 이 질문들의 PASS를 대체하지 않는다.

## 증거 표기

- **USER**: 대화에서 사용자가 명시한 방향.
- **PROPOSAL**: 대화를 정리하면서 제안된 구현·수식·수치 기준. 자동으로 확정 요구가 되지 않는다.
- **LITERATURE**: 원 논문/공식 구현에 귀속되는 주장. 문헌별 확인 깊이는 참고문헌에 명시한다.
- **ARCHIVE**: 과거 답변·실험 산출물에 기록된 내용. 이번 게시에서 새로 실행했다는 뜻이 아니다.
- **OPEN**: 미해결 또는 추가 검증이 필요한 주장.

## 보존·공개 정책

이 저장소는 공개 저장소다. 연구 내용과 참고문헌은 보존하되 개인 이메일, 인증정보, 사내 업무 자료, 관련 없는 개인 정보는 게시하지 않는다. 원 논문의 전문·그림을 무단 재배포하지 않고 공식 링크와 자체 정리를 제공한다. 사용자 업로드 PDF는 스스로 ‘부분 원문’이라고 명시한 자료이며 누락된 답변을 복원했다고 주장하지 않는다.

**전체 대화의 모든 문자·진행 메시지·도구 로그를 그대로 덤프한 저장소는 아니다.** 이용 가능한 논의의 연구 내용, 사용자 정정, 수식, 실험 결과, 참고문헌을 추적 가능한 구조로 모은 것이다. 확보된 원문과 재구성은 `sources/`에서 구분한다.

현재 별도의 소프트웨어/문서 재사용 라이선스를 선택하지 않았다. 공개 열람이 자동으로 제3자 재배포 허가를 의미하지 않으며, 외부 코드의 라이선스는 각각 확인해야 한다.

## 지속 동기화와 최근 반영 — 2026-11-16

사용자 요청에 따라 접근 가능한 Melete/System ONE 대화와 연구 보고의 변경분을 지속 반영한다. 별도 hourly 확인 작업을 설정했으며, 실시간 전체 채팅 export나 GitHub Actions 설치는 아니다. [동기화 정책](SYNC_POLICY.md)과 [반영 manifest](sources/sync/manifest.json)에 범위·한계를 기록한다.

| 추가 문서 | 내용 |
|---|---|
| [Schema 생명주기와 Ali 공동논문 제안](docs/14-schema-lifecycle-crud-and-joint-paper.md) | In-place Update/Create, 기능 손실 기반 Delete/Retain, 문맥 기반 Read/Activate, 목적함수와 실험 |
| [11/16 SBL 보고 보존](research/2026-11-16-sbl-tracking.md) | 이전 보고의 수치·한계·링크를 discussion-import로 보존; 신규성 중복 주의 |
| [영향·AGI 조건부 평가](research/2026-11-16-impact-hypotheses.md) | 증명 수준과 산업·학술 영향의 조건부 해석; 성과 주장이 아님 |
| [보충 참고문헌](references/schema-lifecycle-2026-11-16.md) | CRUD·주간 보고의 원문 링크와 확인 수준 |
| [대화 출처·사용자 원문](sources/sync/2026-11-16-discussion.md) | CRUD 질문과 지속 갱신 요청, 재구성 범위와 정정 필요 사항 |
| [Schema·LLM 간섭과 영향 질문의 USER 원문](sources/sync/2026-11-schema-user-verbatim.md) | 이전 감사 때 직접 확보하지 못했던 schema 분해 가설 및 산업·AGI 영향 질문 원문(작성 시각 미확인) |

이번 추가는 문서 동기화다. 기존 코드·로드맵·백서의 구현 상태와 효용 판정은 변경하지 않았다.

보충 선별: [증거 연계·적응형 근거 읽기 (WikiTrace / HiVe-Mem)](research/2026-11-16-memory-evidence-read-supplement.md) — 2026-11-09~10 공개된 외부 agent memory 연구의 11/16 추가 검토. Melete의 Read/Write 오적용과 provenance 대조군을 **PROPOSAL / NOT RUN**으로 기록한다.


## Sleep-time 조사와의 직접 관련 연결 — 2026-11-16

독립 주간 보고에서 Melete의 CRUD·low-rank expert·지속학습 판정에 직접 관련된 **8건만** [연구 교차 검토](research/2026-11-16-sleep-time-melete-integration.md) 및 [참고문헌·확인 범위](references/2026-11-16-sleep-time-melete.md)에 선별 기록했다. Agent 외부 memory를 neural schema 지속학습으로 동일시하지 않는다. 전체 Sleep-time 보고를 이관한 것은 아니며 성능 재현도 수행하지 않았다.


2026-11-17 보충 선별: [SoMem과 recursive state capacity](research/2026-11-17-sleep-time-melete-selected-addendum.md) — 앞선 Sleep-time 주간 보고에서 이미 공개됐던 두 연구를 추가 검토. 외부 근거 기반 memory 재조직과 recurrent 상태의 현재 예측/미래 갱신 충분성을 구분하며, [참고문헌](references/2026-11-16-sleep-time-melete.md)에 기록한다. 새로운 neural SBL 성능의 입증이 아니라 **인접 연구·실험 가설 / NOT RUN**이다.


## 델타 설계 반영 감사와 계산 계획 — 2026-11-17

사용자 요청(원문과 이번 작업의 경계는 [2026-11-17-discussion.md](sources/sync/2026-11-17-discussion.md))에 따라 2026-11-12 감사 이후 들어온 자료(ChatGPT 동기화 커밋 5개의 docs/13·14, 11-16·17 기록, 사용자 공유 링크 연구 카드)를 설계 반영 기준으로 다시 검토했다. 로드맵 P1–P5에 계산 자원을 붙이는 계획(클라우드 GPU runcrate 포함)도 세웠다.

| 추가 문서 | 내용 |
|---|---|
| [2026-11-17-design-review.md](research/2026-11-17-design-review.md) | 검토 방법·수치, 반드시 볼 10개 주제의 판정과 반영 위치, 반영한 편집, 사용자 결정 대기의 갱신 |
| [README.md](research/2026-11-17-design-review/README.md) | 이 검토의 공개 사본: 항목별 원장(JSON·TSV), 적용한 편집 목록, 정리본, 워커별 편집 블록 원문 |
| [15-compute-plan.md](docs/15-compute-plan.md) | 계산 계획(횡단 문서). 수치는 ESTIMATE / NOT RUN이고 결정은 사용자 몫 |
| [shared-links-2026-11-17.md](references/shared-links-2026-11-17.md) | 사용자 공유 링크 카드에서 확정한 논문과 확인 수준 |

이번 작업은 문서와 계획의 변경이다. 모델 학습, GPU 실행, 클라우드 인스턴스 생성, 비용 지출, 백서 재생성, 외부 발송은 0회다. 새로 들어간 설계 문장은 PROPOSAL·OPEN이고 계산 수치는 ESTIMATE / NOT RUN이다. 백서는 갱신하지 않았으므로 2026-11-12 기준이다. [SYNC_POLICY.md](SYNC_POLICY.md)는 위 증거 표기 5종에 USER-HYPOTHESIS·NOT RUN을 더해 7종을 쓰고, 이번 검토는 계산 추정에 ESTIMATE를 더했다. 이 검토가 문서에 단 주석의 '없다·반영돼 있지 않다'는 기준 커밋 280dc9a의 상태이며 편집이 들어간 뒤에는 달라질 수 있다.


## 이상 청사진·비모수 POC·단계별 계획·아인슈타인 테스트 설계 — 2026-11-18

사용자 요청(원문과 이번 작업의 경계는 [2026-11-18-discussion.md](sources/sync/2026-11-18-discussion.md))에 따라 이상 청사진, 학습 없는 비모수 POC(P0(NP)), 단계별 구현·논문 계획, runcrate 실험 계획, 아인슈타인 테스트(경험 조건부 발견 시험) 설계를 문서로 썼다. 위 읽는 순서 표의 docs/16–19와 조사 기록, 개정한 [09-roadmap.md](docs/09-roadmap.md)·[15-compute-plan.md](docs/15-compute-plan.md)가 그 결과다. 이번 작업은 문서와 계획의 변경이다. 구현, 모델 학습, GPU 실행, 클라우드 인스턴스 생성, 비용 지출, 백서 재생성, 외부 발송은 0회다. 새 설계 문장은 PROPOSAL·OPEN이고 수치는 ESTIMATE / NOT RUN이다. 백서는 갱신하지 않았으므로 2026-11-12 기준이다.


## 2026-11-23 독립 SBL / Sleep-time 보고의 FCL 관련 항목

[2026-11-23 SBL 선별 검토](research/2026-11-23-sbl-weekly-synthesis.md)와 [Sleep-time 직접 관련 선별 기록](research/2026-11-23-sleep-time-melete-selected.md)을 [원문·확인 범위](references/2026-11-23-sbl-sleep-sources.md)에 연결했다. 11/17 TPAMI hybrid 게재와 이전 연구 재발견을 구별하며, scaffold의 초기 경험 이력 편향, SchemaMem의 유지–최적화 비용, session-ID가 필요한 Schema-LoRA 기준선, 원본 보존 대비 검증된 압축과 self-evolution 평가 잡음을 [Ali A/B/C 비교](research/2026-11-22-ali-abc-evaluation.md)의 **PROPOSAL / OPEN** 대조 항목으로만 연결한다. **NOT RUN:** 모델/GPU 실행이나 연구 효용 확인은 수행하지 않았다. 기존 whitepaper는 2026-11-12 기준이다.

### 2026-11-24 recurrence 비용 통제 보충
[두 recurrent architecture 원문 보충 검토](research/2026-11-24-recurrence-cost-controls.md)는 11/23 Sleep-time 보고의 미포함 항목을 11/24 공식 초록·선택 본문에서 확인한 기록이다. Token feedback의 정보–계산 trade-off와 loop late entry의 decode 비용을 Ali A의 독립 대조 후보로 연결한다. **PROPOSAL / OPEN / NOT RUN**; 지속 schema 학습 효능이나 설계 승인이 아니다.
