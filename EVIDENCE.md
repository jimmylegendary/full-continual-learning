# 증거 수준과 아카이브의 범위

정리일: 2026-11-09. 이 저장소의 1차 산출물은 연구 문서와 출처 정리다.

## 무엇을 근거로 정리했는가

1. 현재 대화에서 보이는 사용자 발화, assistant의 공개 답변, 논문/코드 링크, 정정 이력.
2. 사용자가 업로드한 `neuroscience_conversation_available_originals(1).pdf` (22쪽). 파일 스스로 전체 대화가 아닌 부분본임을 밝힌다. p11의 긴 답변은 누락돼 있다.
3. PDF에 실제 내장된 `preserved_messages.json`과 `preserved_transcript_utf8.txt`.
4. Library에서 실제 확보한 `Melete_SBL_Research_and_Phase0_20261103.zip` (811,283 bytes), 8개 내부 파일.
5. 이 게시 작업에서 확인한 핵심 공식 문헌 metadata/검색 결과. 모든 논문의 본문·코드·실험을 재검증한 것은 아니다.

## 원자료 해시

- PDF SHA-256: `2e0d607e9338f48066c0d66d4dcaf43e0462875c399295ea66019f5518837317`
- Phase-0 ZIP SHA-256: `a0581ee2cc86964fa7612b24d03bfe493660a71863d1c4f09825d9b91c641e39`
- Original `probe.py`: `372ff6efdd5e5226e6067a3d9e86c2329d743a196ed306dc295d635a4215abc2`
- Original `results.json`: `b55365218445817ec032cf5bfc63bc2805e46f2c771c77e12f7d5a52d85b0cb5`
- Original `verification.json`: `bff8f9ffe97fe0efb2bd08e3ba590d712da05c6eac2b88f28bb1a5b084c51284`

## 확인 깊이의 의미

- `metadata-checked`: 이번 게시에서 공식 arXiv/학회/저널 metadata를 확인. 숫자와 기전의 전면 재검증 아님.
- `official-search-checked`: 공식 원문을 가리키는 검색 결과에서 identity를 확인. 원문 전체 독해 아님.
- `discussion-import`: 이전 답변/PDF에 있는 내용과 URL을 보존. 이번 게시에서 재확인하지 않음.
- `needs-resolution`: 논문명이 있으나 안정된 식별자/URL을 추가 확보해야 함.
- `artifact-available`: 실제 로컬 원파일을 확보하고 내용/해시를 읽음.

URL fetch 실패는 논문 부존재를 뜻하지 않는다. 검색에서 다른 사이트를 찾았다고 공식 원문을 전부 읽었다고 하지 않는다. ‘Ali가 최근 관심 있다’는 사용자의 전달 내용은 architecture의 효용 근거가 아니며 독립 확인한 사실로 기록하지 않는다.

## 원문과 재구성

`docs/`는 주제별 재구성·설계 명세다. `sources/user-statements.md`는 현재 대화의 핵심 연구 요청 원문을 보존한다. 첨부 PDF의 연구 원문과 참고 링크는 별도로 보존하며 개인정보를 제거한 부분을 명시한다.

현재 대화의 모든 assistant 답변을 문자 단위로 export한 자료는 제공되지 않았다. 이를 완전한 raw transcript라고 주장하지 않는다. 빠진 PDF 답변, 불러올 수 없는 이전 세션, 비공개 chain-of-thought를 새로 만들어 채우지 않는다.

## 과거 보고와 현재 실행

주간 보고의 논문 수치, 기존 Melete N/J 단계 결과, Phase-0 결과는 원래 보고의 범위로 귀속한다. 특히 Phase-0의 24D/두 3D covariance 실험은 current integrated model이 아니다. 실제 코드·결과 파일이 확보됐다는 것과 이번 게시에서 전체 실험을 재실행했다는 것은 다르다.

별도 `VALIDATION.md`가 기록하는 문서 링크/JSON/소스 검사와 수치 감사만 이번 실행으로 표시한다. 모델/GPU 학습, 통합 runtime, 전체 SBL 이론의 입증을 주장하지 않는다.

## 공개 범위

공개 저장소에는 연구와 무관한 개인 이메일, 사내 자료, credential, 개인 profiling을 추가하지 않는다. 업로드 PDF 원본과 ZIP 원본은 해시로 식별한다. 원자료를 가공한 연구 문서는 수정 내역을 기록한다. 외부 논문 전문·그림·third-party code를 무단 복제하지 않는다.

## 날짜

분석 기준 날짜와 자료 작성일, 논문 최초 공개일, 최신 개정일, 학회 연도를 분리한다. 과거 답변의 2026-11-02/03은 과거 기록이다. 자동화 일정이나 과거 조사 날짜를 현재 날짜로 다시 표기하지 않는다.
