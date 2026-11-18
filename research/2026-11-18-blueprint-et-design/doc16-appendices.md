# docs/16 이상 청사진의 부록: 색인·새 참고문헌·조사 출처 (2026-11-18)

**상태 라벨:** 설계 작업 기록의 부록(PROPOSAL / OPEN / NOT RUN)이다. [16-ideal-blueprint.md](../../docs/16-ideal-blueprint.md) 초안 끝의 세 부록을 공개 문서에서 떼어 이곳에 둔다. 초안 원문이므로 가칭(DC-·F-NEW-·NEW-로 시작하는 번호)을 그대로 두었고, 최종 번호는 [id-map.tsv](../../research/2026-11-18-blueprint-et-design/id-map.tsv)와 [2026-11-18-blueprint-et-design.md](../../research/2026-11-18-blueprint-et-design.md)의 대응표에 있다. 작성일 2026-11-18.

## 부록 A. 색인

### A.1 소유 정의 위치

| 소유 정의 | 절 번호 | 절 제목 |
|---|---|---|
| feature 상세(BF-*) | §3, §6 | 「3. feature 목록」, 「6. feature 상세」(6.1~6.8) |
| flow FL-1~FL-6 | §5 | 「5. 동작 flow FL-1 ~ FL-6」 |
| 경로 이름(fast / learn / deep / hold) | §2.1 | 「2.1 경로 이름: fast / learn / deep / hold」 |
| CRUD 판정 이름(read / update / branch / create / hold / evict) | §2.2 | 「2.2 CRUD 판정 이름: read / update / branch / create / hold / evict」 |
| feature × phase 해상도 표 | §4 | 「4. feature × phase 해상도 표」(4.1~4.8) |

### A.2 이 초안이 정의한 ID

| 종류 | ID |
|---|---|
| feature 32개 | BF-A1 BF-A2 BF-A3 / BF-B1 BF-B2 BF-B3 BF-B4 BF-B5 / BF-C1 BF-C2 BF-C3 / BF-D1 BF-D2 BF-D3 BF-D4(추가) / BF-E1 BF-E2 BF-E3 BF-E4 / BF-F1 BF-F2 BF-F3 BF-F4 BF-F5 / BF-G1 BF-G2 BF-G3 BF-G4 / BF-H1 BF-H2 BF-H3 BF-H4 |
| flow 6개 | FL-1 입력 1건 처리(각성), FL-2 불일치와 조절, FL-3 깊이, FL-4 Sleep, FL-5 발견, FL-6 상태 |
| 경로 4개 | fast, learn, deep, hold |
| CRUD 판정 6개 | read, update, branch, create, hold, evict |
| 이 문서 안의 OPEN | OP16-1 ~ OP16-9 |
| 해상도 표의 칸 표기 | `NP: … / 학습: …`, 「NP 유지」, 「학습: 없음」, 「학습: 유지」, 「뼈대」 |

### A.3 남의 정의를 가리킨 곳

| 가리킨 정의 | 소유 문서 | 이 초안에서 가리킨 곳 |
|---|---|---|
| ET 단 ET-0~ET-4·ET-3p, 입력 tier A/B/C, stream 항목 schema, 대상별 rubric, 발견 수준의 채점 | docs/17 | §2.3, §3 목록의 경계, §4.1 BF-A1 P6, §6.6 BF-F5 |
| NP-0 / NP-1 / NP-2의 상세, suite S-A~S-D, V0-n, UJ0 | docs/18 | §2.5, §4 칸 읽는 법, §6 P0 비모수 대역 열, §8.2 |
| phase 정의·종료 gate·결과 등급 상한, UJ6, 결정표 | docs/09 | §1.1, §1.4, §4 머리, §4.8의 BF-H4 예외, §8.3, §9.2 |
| 논문 주장 Ck-n | docs/19 | §2.5, §7.2, §7.4 |
| 비용·token·GPU-시간 | docs/15 | §1.1, DC-W1-05 |
| 발견 수준 L0–L5와 H-DISCOVER의 문장 | 마스터 결정 MD-1118-N([2026-11-18-blueprint-et-design.md](../../research/2026-11-18-blueprint-et-design.md)) | §2.3 |
| 헌장 U01–U12, 중심 명제 H-SAMPLE·H-COMPUTE | docs/01 | §7.3, §7.4 |
| 결과 등급·문구 규칙, capability × phase 표 | docs/09 | §4, §8.3 |
| 평가 family F01–F24와 후보 상태 | docs/08 | §8.2 |

### A.4 가칭 목록

| 가칭 | 한 줄 요약 | 위치 |
|---|---|---|
| DC-W1-01 | feature 목록에 BF-D4를 더한 것의 수용(32개 / 31개) | §9.2 |
| DC-W1-02 | hold 경로를 P1의 규칙형 controller v0에도 넣을지 | §9.2 |
| DC-W1-03 | CRUD 판정에서 branch와 create를 나눠 쓸지 | §9.2 |
| DC-W1-04 | 발견 feature 묶음과 H-DISCOVER를 헌장에 올릴지 | §9.2 |
| DC-W1-05 | 발견 feature의 학습 모듈을 P3–P4에 둘지, P5 이후로 미룰지 | §9.2 |
| DC-W1-06 | BF-H4를 P0부터 얇게 둘지(「모든 phase에 모든 feature」의 예외) | §9.2 |
| DC-W1-07 | 기존 문서의 용어를 BF·FL 이름에 맞춰 개정할지 | §9.2 |
| F-NEW-W1-a | 새 평가 family 후보 「긴장 보존과 지연 해소」 | §8.2 |
| NEW-W1-nn | 없음(새 참고문헌을 추가하지 않았다) | 부록 B |

### A.5 링크 대상 중 아직 없는 문서

이 초안이 링크로 가리키지만 통합 때 새로 생기는 파일이다: docs/17-einstein-test.md, docs/18-poc-nonparametric.md, docs/19-paper-plan.md, research/2026-11-18-blueprint-et-design.md, sources/sync/2026-11-18-discussion.md.

## 부록 B. 새 참고문헌

이 초안은 새 참고문헌을 추가하지 않는다. 방법과 문헌은 기존 [catalog.tsv](../../references/catalog.tsv)의 ID로만 가리켰고 확인 수준은 catalog의 status를 따랐다. catalog에 없는 방법(예: hidden-state kNN 기억, CRP식 사전)은 이 문서에서 이름만 쓰고 문헌으로 옮기지 않았으며, 그 조사와 catalog 추가는 선행 연구 조사(docs/19의 근거)와 조사 기록이 맡는다. 형식만 남긴다.

| id | title | category | date_note | url | code_url | status | note |
|---|---|---|---|---|---|---|---|
| (없음) | | | | | | | |

## 부록 C. 조사 출처

이 초안은 웹 조사나 외부 URL 접근을 하지 않았다. 아래는 읽은 저장소 문서와 범위다. 확인 수준은 모두 「저장소 본문 직접 읽음」이며 외부 논문·사료의 확인이 아니다. 읽지 않은 절은 그렇게 적었다.

| URL(저장소 문서) | 접근일 | 읽은 범위 | 확인 수준 |
|---|---|---|---|
| [AGENTS.md](../../AGENTS.md), [SYNC_POLICY.md](../../SYNC_POLICY.md), [README.md](../../README.md) | 2026-11-18 | 전문 | 저장소 본문 직접 읽음 |
| [01-intent-and-charter.md](../../docs/01-intent-and-charter.md) | 2026-11-18 | 전문 | 같음 |
| [04-rhythms-and-orchestration.md](../../docs/04-rhythms-and-orchestration.md) | 2026-11-18 | 전문 | 같음 |
| [05-integrated-architecture.md](../../docs/05-integrated-architecture.md) | 2026-11-18 | 전문 | 같음 |
| [06-mathematical-framework.md](../../docs/06-mathematical-framework.md) | 2026-11-18 | §1–§6. §7–§11은 읽지 않음 | 같음 |
| [07-state-and-storage.md](../../docs/07-state-and-storage.md) | 2026-11-18 | 전문 | 같음 |
| [08-evaluation.md](../../docs/08-evaluation.md) | 2026-11-18 | §2·§2-1·§2-2(family 표 전체). §1·§3–§9는 읽지 않음 | 같음 |
| [09-roadmap.md](../../docs/09-roadmap.md) | 2026-11-18 | §1–§4-1 전문, §5는 phase별 목표·데모·종료 gate 줄, §6·§6-1 표, §10의 D-01~D-14 표와 결정 후보 단락. §7–§9·§11은 읽지 않음 | 같음 |
| [11-research-agenda.md](../../docs/11-research-agenda.md) | 2026-11-18 | §4 | 같음 |
| [12-melete-lineage.md](../../docs/12-melete-lineage.md) | 2026-11-18 | §1, §4, §5 | 같음 |
| [13-schema-decomposition-and-interference.md](../../docs/13-schema-decomposition-and-interference.md) | 2026-11-18 | 머리, §1–§3, §5–§6, §9–§11. §4·§7–§8은 읽지 않음 | 같음 |
| [14-schema-lifecycle-crud-and-joint-paper.md](../../docs/14-schema-lifecycle-crud-and-joint-paper.md) | 2026-11-18 | §1–§7 앞부분. §7 뒤쪽·§8–§10은 읽지 않음 | 같음 |
| [user-statements.md](../../sources/user-statements.md) | 2026-11-18 | 전문(U-T01~U-T14) | 같음 |
| [2026-11-schema-user-verbatim.md](../../sources/sync/2026-11-schema-user-verbatim.md), [2026-11-16-discussion.md](../../sources/sync/2026-11-16-discussion.md), [2026-11-17-discussion.md](../../sources/sync/2026-11-17-discussion.md) | 2026-11-18 | 전문 | 같음 |
| [ledger-melete.json](../../research/2026-11-12-design-audit/ledger-melete.json) | 2026-11-18 | M-B04-02, M-B04-03, M-B08-01, M-B08-02 네 항목 | 같음 |
| [2026-11-12-design-audit.md](../../research/2026-11-12-design-audit.md), [2026-11-17-design-review.md](../../research/2026-11-17-design-review.md) | 2026-11-18 | 앞은 §5(사용자 확인 목록), 뒤는 §7.2–§7.3 | 같음 |
| [catalog.tsv](../../references/catalog.tsv) | 2026-11-18 | 133행의 id·title·category·status, 인용한 ID의 note | 같음 |
