# 출처·대화 아카이브

## 범위

이 저장소는 현재 확보 가능한 논의의 연구 내용을 주제별로 이관한다. 완전한 채팅 raw export가 아니라 원문이 확보된 부분과 재구성을 구분한다.

| 자료 | 형태 | Git에 보존한 방식 |
|---|---|---|
| 현재 세션 사용자 연구 요청 | 현재 대화 원문 | `user-statements.md` |
| 현재 세션 assistant 설명 | 공개 답변 내용 | `docs/`의 상세 재구성; 논점·수식·수치·정정 보존 |
| 22쪽 뇌과학 PDF | 부분 원문, p11 답변 누락 | 연구 발화 발췌·13개 이론표 재구성·전체22개 원문 참고 링크 |
| Phase-0 ZIP | 실제 확보된 기존 산출물 | `experiments/phase0/`의 원본 코드·수치 요약·hash·조건·한계 |
| 2026-11-09 SBL 보고 | 현재 대화의 주간 보고 | `research/2026-11-09-sbl-tracking.md` |
| 주간 추적 지시 | 사용자 지시 | `research/TRACKING_POLICY.md` |

## PDF 원자료

파일명: `neuroscience_conversation_available_originals(1).pdf`.
작성일 표기: 2026-10-31, 총22쪽.

- p1: 부분본·누락 범위 공지.
- p2–10: 기억 version/update/use와 과거 기억의 재사용.
- p11: 익숙함·다층 이해 질문; 긴 assistant 답변 미확보.
- p12–19: CLS/SBL 등13개 이론·회로와 통합 해석.
- p20: PDF·이메일 전송 요청. 개인 이메일은 공개 문서에서 제외.
- p21–22: 22개 원문 참고 링크.

PDF에 실제 내장된 `preserved_messages.json`, `preserved_transcript_utf8.txt`를 추출해 확인했다. 연구 원문 발췌는 [neuroscience-origin.md](neuroscience-origin.md)에 있다. 이메일을 제거한 전체 **확보 부분** 전사는 별도 다운로드 source-backup에 포함한다. 해당 전사를 Git에 모두 게시했다고 주장하지 않는다. 원본 PDF의 Content Credentials는 연구 내용이 아니므로 이관 대상에서 제외했다.

## 별도 원본 백업

게시 응답의 source-backup ZIP에는 기존 Phase-0 ZIP 전체와 공개용 redacted PDF 전사, 이번 검증 receipt가 포함된다. Git에는 큰 per-task raw 결과를 복제하지 않고 정확한 source hashes, 실행 코드, 결과 요약을 보존한다. 이 구분은 [Phase-0 manifest](../experiments/phase0/archive-manifest.json)에도 명시한다.

## 인용 원칙

사용자 의도에는 U-Txx, 참고문헌에는 N/R/S/A/E 식별자를 쓴다. 파일 작성일과 이번 실행일은 다르다. 논문에서 제안한 것, 대화에서 추론한 것, 실험으로 확인한 것을 구분한다. 누락된 PDF 답변·이전 세션·비공개 추론을 새로 만들어 채우지 않는다.
