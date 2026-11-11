# 설계 반영 감사 자료 (2026-11-12)

종합은 [2026-11-12-design-audit.md](/home/jimmy/repos/full-continual-learning/research/2026-11-12-design-audit.md)에 있다. 이 폴더에는 감사에 쓴 원장과 편집 초안을 공개용으로 정리한 사본을 둔다. 바뀐 경로는 다음과 같다.

- 호스트 작업 경로는 `(감사 작업 폴더)`로 바꿨다.
- private Melete 저장소 경로는 `melete@1d95136:<경로>`로 바꿨다. 이는 고정 커밋 `1d95136c3a64580ec25bc588c96c191eecb85b41` 기준이다.

| 파일 | 내용 |
|---|---|
| [ledger-fcl.json](/home/jimmy/repos/full-continual-learning/research/2026-11-12-design-audit/ledger-fcl.json) | FCL 시기 원장 177항목(U-T01–U-T11, docs/01·02, README). 필드: id, source_refs, source, date, quote, kind, label, status, design_locations, note, superseded_by, gap_edit_ids |
| [ledger-melete.json](/home/jimmy/repos/full-continual-learning/research/2026-11-12-design-audit/ledger-melete.json) | Melete 시기 원장 148항목(B01–B20, H1–H5, M-REC, J0/J1·neural-basis 교훈). 필드는 위와 같다 |
| [W1-gaps.txt](/home/jimmy/repos/full-continual-learning/research/2026-11-12-design-audit/W1-gaps.txt) | FCL 원장의 PARTIAL·MISSING을 닫는 편집 블록 G1-01–G1-19와 사용자 확인 목록 |
| [W2-gaps.txt](/home/jimmy/repos/full-continual-learning/research/2026-11-12-design-audit/W2-gaps.txt) | Melete 원장의 편집 블록 G2-01–G2-30, H1–H5 계승/대체 표, 사용자 확인 목록 |
| [W3-literature-edits.txt](/home/jimmy/repos/full-continual-learning/research/2026-11-12-design-audit/W3-literature-edits.txt) | 11-11 원문 검토·11-09 주간 조사를 설계 문서로 옮긴 편집 블록 L03-01–L11-08 |
| [W3-summary.txt](/home/jimmy/repos/full-continual-learning/research/2026-11-12-design-audit/W3-summary.txt) | 문헌 통합 범위표, 숫자 대조표, 애매한 편집 목록 |
| [W4-notes.txt](/home/jimmy/repos/full-continual-learning/research/2026-11-12-design-audit/W4-notes.txt) | 새 로드맵의 설계 판단 근거와 열린 결정 D-01–D-14 |

**반영 상태.** 편집 블록의 OP 값에 따라 처리가 다르다.

- `INSERT_AFTER_LINE`·`REPLACE_SUBSTRING` 블록 70개는 마스터가 검수해 docs/01·03–08·10–12에 넣었다. 수정한 내용은 종합 문서 §4에 있다.
- `ROADMAP_REQUIREMENT` 블록은 새 [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md)가 받았다.
- `LITERATURE_HANDOFF` 블록 중 11-11·11-09 문헌분은 W3 편집이 다뤘다. 나머지는 종합 문서 §6.2의 남은 일이다.

원장의 `status`는 감사 시점(반영 전)의 판정이다. 편집 블록 본문은 반영 전 초안이므로, 마스터 수정이 들어간 최종 문장은 docs/ 본문이 기준이다.
