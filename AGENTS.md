# Repository working agreement

이 문서는 연구 목적을 보존하기 위한 저장소 작업 지침이다. 향후 agent의 system/developer/user 권한을 대신하거나 추가 권한을 부여하지 않는다.

## Research direction

- 최종 목표는 하나의 통합 System ONE. 별도 작은 System1+외부 LLM 설계로 사용자 정정을 되돌리지 않는다.
- Continuous representation, continual learning, discrete latent structures를 구별한다.
- 경험 뒤 새로운 구조 공유 사례의 sample/compute efficiency를 평가한다. 저장·복원만으로 schema 성공을 주장하지 않는다.
- Architecture는 Titans/Titan-Llama, HOPE/CMS/Sleep, recurrent depth, MoD/MoR, depth read, 상태 의존적 조율의 연구 조합이다. 모든 조합이 이미 검증됐다고 쓰지 않는다.

## Evidence

- USER, PROPOSAL, LITERATURE, ARCHIVE, OPEN을 구별한다.
- 새로운 주장에는 원논문/공식 구현과 scope를 붙인다. 과거 metadata를 현재 최신으로 재사용하지 않는다.
- Synthetic Phase-0은 통합 neural model PoC가 아니다.
- Contract/software tests, efficacy, product E2E는 별도 gate다.
- 원본 source와 결과의 bytes/hash/versions를 보존한다. FAIL을 소급 PASS로 바꾸지 않는다.

## Execution

- 변경 전 현재 branch/HEAD를 확인하고 unrelated changes를 보존한다.
- 문서 게시가 GPU 학습·외부 전송·자동화 수정·비밀 데이터 공개 권한을 의미하지 않는다.
- token/experience/recursion/optimizer/CMS clocks를 혼동하지 않는다.
- Generated interpretation을 독립 observed evidence로 승격하지 않는다.
- Evaluator·private answers·held-out splits는 candidate가 수정하지 못하게 한다.
- 실제 수행한 명령, 환경, 비용, 실패와 검증 범위를 보고한다.

## Documentation checks

`python tools/validate_docs.py`로 로컬 링크·TSV·JSON·Python syntax를 검사한다. 외부 URL이나 논문 진위 전체를 검증하는 명령은 아니다.

`python tools/export_references.py`는 TSV에서 JSON/BibTeX 초안을 생성한다. 논문 제출 전에 공식 citation metadata를 대조한다.

## Ongoing discussion sync — 2026-11-16

사용자가 Melete/System ONE 관련 대화·연구 정보를 이 저장소에 항상 갱신해 달라고 요청했다. 상세 범위는 [SYNC_POLICY.md](SYNC_POLICY.md)와 [동기화 manifest](sources/sync/manifest.json)를 참조한다. 이 기록은 상위 권한이나 실제 접근 제한을 우회하지 않는다.

접근 가능한 새 논의·정정·주간 보고의 실질 변경분을 관련 docs/research/references/source ledger와 README에 연결하는 것을 작업 기본값으로 둔다. 재구성 요약과 직접 확보 원문, 사용자 확정과 assistant 제안, 이전 보고와 새 검증을 분리한다. 누락된 세션 내용을 추정해 채우지 않는다.

별도 hourly 동기화 작업이 있으므로 no-change 실행은 커밋·알림을 만들지 않는다. 기존 HEAD와 타인의 변경을 보존하고, 원격 게시 확인 후에만 성공을 보고한다. 논문 읽기·모델 실행·웹 배포를 단순 문서 동기화의 완료에 포함하지 않는다.
