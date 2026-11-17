# 델타 설계 반영 감사 자료 (2026-11-17)

종합은 [2026-11-17-design-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review.md)에 있다. 이 폴더에는 감사에 쓴 원장과 편집 블록 원문, 점검 결과를 공개용으로 정리한 사본을 둔다. 11-12 감사의 자료 폴더 안내 [README.md](/home/jimmy/repos/full-continual-learning/research/2026-11-12-design-audit/README.md)와 같은 방식이며 바뀐 점은 다음과 같다.

- 호스트 작업 경로는 `(검토 작업 폴더)`로 바꿨다.
- 사용자 공유 링크 카드는 `T1…`로만 부른다. 카드 id·앱 이름·공유 단축 링크는 싣지 않았고 대응표도 공개하지 않는다.
- 계정·잔액·상품 내부 식별자·키와 키 파일 경로는 싣지 않았다. 가격·사양·region은 2026-11-17 조회 시점의 공개 정보다.
- private Melete 저장소 경로는 `melete@1d95136:<경로>` 형식이다(11-12 감사와 같다).

| 파일 | 내용 |
|---|---|
| [ledger-delta.json](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/ledger-delta.json) | 원장 434항목과 머리 정보(기준 커밋, 필드 설명, 판정 기준, 원장별 집계). 필드: id, source, introduced_in, date, provenance, label, claim, quote, status, design_locations, judgment_note, edit_ids(+worker, ledger, PEND 보조 필드) |
| [ledger-delta.tsv](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/ledger-delta.tsv) | 같은 원장을 한 줄씩 평탄화한 표 |
| [edits-applied.tsv](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/edits-applied.tsv) | 편집 블록 105개와 통합 담당(W6) 편집 16개의 처리 결과: applied / modified(무엇을 왜) / skipped(이유) |
| [catalog-additions.tsv](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/catalog-additions.tsv) | references/catalog.tsv에 더한 33행의 최종 ID와 후보 id의 대응, 제외·합친 후보 |
| [W1-math-check.txt](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/W1-math-check.txt) | docs/13 §7.1–7.5 수학 점검: 문서 진술·직접 유도·빠진 조건·판정, 부록에 numpy 점검 코드와 출력 |
| [W1-summary.txt](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/W1-summary.txt) | W1 핵심 발견 10개, 사용자 확인 요청, 남은 OPEN |
| [W2-crud-controller-map.txt](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/W2-crud-controller-map.txt) | 두 가지 '삭제' 판정과 용어안, CRUD 대응표, controller 사다리, low-rank expert 대 CMS·NMM |
| [W2-experiment-placement.tsv](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/W2-experiment-placement.tsv) | 실험 A–E·CU·D·R의 phase 배치표(10행 × 11열) |
| [W2-experiment-placement.txt](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/W2-experiment-placement.txt) | 배치표의 설명, F01–F21 확인, 계산 규모 표기 규칙 |
| [W2-ali-paper-check.txt](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/W2-ali-paper-check.txt) | Ali 공동논문 제안 초안의 등급 상한 점검 16항목 |
| [W2-summary.txt](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/W2-summary.txt) | W2 요약과 사용자 결정 후보 CR1–CR8 |
| [W3-summary.txt](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/W3-summary.txt) | W3 주제별 판정(Sleep-time·SoMem·증거 연계 read·과장·Tian 중복·카탈로그 누락)과 위험 |
| [W4-papers.txt](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/W4-papers.txt) | 사용자 공유 링크 카드에서 논문을 확정한 결과: 식별자·확인 수준·읽은 범위·중복 여부(카드는 T1–T6) |
| [W5-public-docs.txt](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/W5-public-docs.txt) | runcrate 공개 문서에서 확인한 운영 사실과 확인하지 못한 것 |
| [W5-assumptions.tsv](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/W5-assumptions.tsv) | 모델 사양(공식 config)·가정(낙관/중앙/비관)·공식·GPU 사양 출처 |
| [W5-workload.tsv](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/W5-workload.tsv), [W5-workload-phase-totals.tsv](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/W5-workload-phase-totals.tsv) | phase × 모델 × 작업별 FLOPs·메모리·GPU-시간·비용(P10/P50/P90)과 phase 합계. 모두 ESTIMATE / NOT RUN |
| [W5-tiers.tsv](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/W5-tiers.tsv), [W5-tiers-cost-per-valid-experiment.tsv](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/W5-tiers-cost-per-valid-experiment.tsv), [W5-tiers-hypotheses.tsv](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/W5-tiers-hypotheses.tsv), [W5-tiers-sensitivity.tsv](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/W5-tiers-sensitivity.tsv) | tier 선택, 유효 실험 1건의 총비용, 받은 가설의 가격 목록 검증, MFU 가정 민감도(id 열 없음) |
| [W1-edits.txt](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/W1-edits.txt), [W2-edits.txt](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/W2-edits.txt), [W3-edits.txt](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/W3-edits.txt), [W4-edits.txt](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/W4-edits.txt), [W5-edits.txt](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/W5-edits.txt) | 워커별 편집 블록 원문(105개). 블록 형식: FILE·SECTION·OP·ANCHOR·ANCHOR_COUNT·LABEL·LEDGER·OVERTURNS·NEW_TEXT |

**반영 상태.** 편집 블록의 OP 값은 두 가지다. `INSERT_AFTER_LINE`은 ANCHOR가 든 줄 뒤에 삽입하고 `REPLACE_SUBSTRING`은 ANCHOR를 NEW_TEXT로 바꾼다. 블록 105개 중 86개는 그대로 적용했고 15개는 고쳐 적용했고 4개는 합치거나 중복이라 제외했다. 고치거나 합친 블록은 edits-applied.tsv의 note에 이유가 있다. 블록 본문은 반영 전 초안이므로 최종 문장은 docs/ 본문이 기준이다. W3·W4의 후보 행 TSV는 catalog.tsv에 들어갔으므로 catalog-additions.tsv가 대응을 대신한다. W4의 skill·도구 카드 판정표와 카드 분류표는 공개하지 않는다.

**원장 읽는 법.** status는 감사 시점(편집 반영 전)의 판정이다. 판정 기준과 원장별 집계는 ledger-delta.json의 머리 정보에 있다. 편집 블록이 말하는 '없다·반영돼 있지 않다'는 기준 커밋 280dc9a의 상태다.
