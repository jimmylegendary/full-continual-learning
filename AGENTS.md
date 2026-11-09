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
