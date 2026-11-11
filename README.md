# Full Continual Learning — Melete / System ONE

**경험이 다음에 무엇을 이해하고, 얼마나 생각하며, 무엇을 어떻게 배울지까지 바꾸는 하나의 모델.**

이 저장소는 Melete를 출발점으로 논의한 schema-based learning(SBL), 지속학습, 빠른 적응, 가변 깊이 추론, 뇌 리듬에서 영감을 얻은 조율, 기존 LLM의 점진적 retrofit을 통합하는 연구 기반이다. 정리 기준일: **2026-11-12**(설계 반영 감사와 로드맵 재구성).

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
| [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md) | 점진적 해상도 로드맵: P1 MVP(실제 `fcl` CLI·소형 retrofit 모델·규칙형 controller v0·대조군·망각/표면 평가)부터 P5까지, capability × phase 표, 결과 등급과 상한, 열린 결정 D-01–D-14 |
| [Self-evolution와 운영 정책](docs/10-evolution-policy.md) | 독립 evaluator, 후보 계보, 예산, 승격, 실패 기록 |
| [후속 가설과 미해결 질문](docs/11-research-agenda.md) | pretraining/alignment, schema 분화, insight |
| [기존 Melete와 이관 경계](docs/12-melete-lineage.md) | H1–H5와 이전 실험을 어떻게 보존할지 |
| [주간 SBL 조사 기록](research/2026-11-09-sbl-tracking.md) | 대화에서 보고된 최신 연구와 수치의 출처 상태 |
| [2026-11-11-sbl-fulltext-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext-review.md) | 신경망 SBL 구현 11편 원문 검토: 외부 요약 정정, 공통 공백, FCL 설계의 시작점 |
| [2026-11-12-design-audit.md](/home/jimmy/repos/full-continual-learning/research/2026-11-12-design-audit.md) | 설계 반영 감사: 사용자 진술 202개 포함 325항목 원장, 반영 판정, 설계 문서 편집 70개, 사용자 확인·열린 결정·남은 문헌 정독 |
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
