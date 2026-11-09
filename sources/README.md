# 출처·대화 아카이브

## 범위

이 저장소는 현재 확보 가능한 논의의 **연구 내용 전체를 주제별로 이관**한다. 완전한 채팅 raw export가 아니라 원문이 확보된 부분과 재구성을 구분한다.

| 자료 | 형태 | 보존 방식 |
|---|---|---|
| 현재 세션 사용자 연구 요청 | 현재 대화 원문 | `user-statements.md` |
| 현재 세션 assistant 설명 | 공개 답변 내용 | `docs/` 전체의 상세 재구성, 논점/수식/수치/정정 보존 |
| 22쪽 뇌과학 PDF | 부분 원문, p11 답변 누락 | 핵심 발화·이론표·전체 22개 primary links, embedded text의 연구 원문 |
| Phase-0 ZIP | 실제 확보된 기존 산출물 | `experiments/phase0/`, 원래 hash·조건·결과·제약 |
| 2026-11-09 SBL 보고 | 현재 대화의 주간 보고 | `research/2026-11-09-sbl-tracking.md` |
| 주간 추적 지시 | 사용자 지시 | `research/TRACKING_POLICY.md` |

## PDF 원자료

파일명: `neuroscience_conversation_available_originals(1).pdf`.
작성일 표기: 2026-10-31, 총 22쪽.

- p1: 부분본·누락 범위 공지.
- p2–10: 기억 version/update/use와 과거 기억의 재사용.
- p11: 익숙함·다층 이해에 대한 사용자 질문, 긴 assistant 답변 미확보.
- p12–19: CLS/SBL 등 13개 이론·회로 표와 통합 해석.
- p20: PDF와 이메일 전송 요청. 개인 이메일은 공개 자료에서 제외.
- p21–22: 22개 원문 참고 링크.

PDF에 `preserved_messages.json`, `preserved_transcript_utf8.txt`가 실제 내장돼 있어 추출했다. ‘Content Credentials’도 있었으나 연구 내용이 아니므로 게시 대상에서 제외한다. 원본 PDF/ZIP 해시는 [EVIDENCE](../EVIDENCE.md)에 있다.

## 출처를 인용하는 방법

문서별 사용자 의도에는 발화 식별자 U-Txx, 논문에는 N/R/S/A/E 식별자를 쓴다. 파일명 날짜는 작성일 표기이지 이 저장소의 실제 실행일이 아니다. 논문에서 제안한 것, 대화에서 추론한 것, 실험이 확인한 것을 별도로 쓴다.

공개 연구 문서에 누락을 숨기거나 원문을 추정해 복원하지 않는다. 이전 assistant의 해석도 사용자 확정으로 자동 승격하지 않는다.
