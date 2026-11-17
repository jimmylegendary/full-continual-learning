# docs/17 아인슈타인 테스트(경험 조건부 발견 시험)의 부록: 색인·새 참고문헌·조사 출처 (2026-11-18)

**상태 라벨:** 설계 작업 기록의 부록(PROPOSAL / OPEN / NOT RUN)이다. [17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md) 초안 끝의 세 부록을 공개 문서에서 떼어 이곳에 둔다. 초안 원문이므로 가칭(DC-·F-NEW-·NEW-로 시작하는 번호)을 그대로 두었고, 최종 번호는 [id-map.tsv](/home/jimmy/repos/full-continual-learning/research/2026-11-18-blueprint-et-design/id-map.tsv)와 [2026-11-18-blueprint-et-design.md](/home/jimmy/repos/full-continual-learning/research/2026-11-18-blueprint-et-design.md)의 대응표에 있다. 작성일 2026-11-18.

## 부록 A. 색인

### A.1 소유 정의 위치

이 문서가 소유하는 정의(공유 정의의 소유자 표 기준)가 있는 절이다. 발견 수준 L0–L5와 가설 H-DISCOVER는 마스터 결정의 문장을 그대로 옮긴 것이며 소유는 결정이다.

| 소유 정의 | 절 번호 | 절 제목 |
|---|---|---|
| ET 운영 정의(W(≤T0), P_pre, P_post, W_delta, T0, t_c, T1) | §2.3 | 운영 정의: 경험 조건부 발견 시험(ET) |
| 「입력」의 두 해석과 기본 선택 | §2.4 | 「입력」의 두 해석과 기본 선택 |
| ET 단 정의(ET-0~ET-4와 ET-3p), phase 대응 | §3.1 | 사다리 |
| 단별 등급 상한과 쓸 수 있는 문구·없는 문구 | §3.2 | 단별 등급 상한과 쓸 수 있는 문구·없는 문구 |
| stream 항목 schema | §6.1 | 항목 schema |
| 입력 tier A·B·C | §6.2 | 입력 tier A·B·C |
| stream 규모 추정 | §6.6 | 규모 추정 (ESTIMATE) |
| 대조 stream CS0~CS4 | §7.6 | 대조 stream |
| 발견 곡선 지표 | §8.4 | 발견 곡선 지표 |
| 대상별 rubric(형식, Einstein 1905 네 구성요소) | §9.2, §9.3 | rubric의 형식, Einstein 1905 rubric 초안 |
| 통과 기준의 형식 | §10.1 | 판정 문장의 형식 |
| 발견 수준 L0–L5(마스터 결정 문장) | §9.1 | 발견 수준 척도 L0–L5 |
| H-DISCOVER(마스터 결정 문장) | §2.6 | 가설 H-DISCOVER |

### A.2 이 초안이 정의한 ID

| 종류 | ID |
|---|---|
| 기호 | T0, W(≤T0), P_pre, P_post, W_delta, t_c, T1, checkpoint k, `L_in(c,k)`, `L_sys(c,k)`, `x_in` |
| 누설 | 누설도 0~3, 누설 변형 LV0 LV1 LV2, 누설 어휘 사전, `leak_by_component` |
| 새로움 | Nv0 Nv1 Nv2 |
| 대조 stream | CS0 없음, CS1 순서 섞기, CS2 같은 시기 비발견자, CS3 무관한 인물, CS4 핵심 입력 제거, 핵심 입력 집합 K |
| 관찰 채널 | S 자발, E0 중립 probe, E1 주제 probe, E2 과제 probe |
| 통과 조건 | PC-1~PC-10(§10.1), ET-3p 계약 EC-1~EC-7(§10.3) |
| 위험 | RSK-1~RSK-13(§12.1. 초안에서는 R1~R13) |
| rubric 구성요소 | E1905-LQ, E1905-BM, E1905-SR, E1905-ME |
| 객관 하위 과제 | OS-LQ-1~3, OS-BM-1~3, OS-SR-1~3, OS-ME-1~3 |
| 명령(가칭) | `fcl et init`, `audit`, `feed`, `probe`, `score`, `curve`, `compare`, `seal`, `verdict` |
| stream 칸 | `item_id`, `stream`, `type`, `date_lo`, `date_hi`, `date_basis`, `source_id`, `source_cite`, `source_class`, `input_tier`, `origin`, `leak_by_component`, `leak_flags`, `inherent_level`, `language`, `translation_ref`, `license`, `render`, `construction_note` |

### A.3 남의 정의를 가리킨 곳

| 가리킨 정의 | 소유 | 이 문서의 위치 |
|---|---|---|
| 긴장 원장(BF-F1), 발견 flow | docs/16 | §8.7 |
| suite S-B(ET-0), suite S-C(ET-1), P0 대조군과 arm 목록, host 재현 규모, 지시를 따르지 못하는 base에서 NP-0을 돌리는 방법 | docs/18 | §3.1, §2.3, §7.7, §9.1, §11.3 |
| 결과 등급 0–5와 문구 규칙, evaluator 분리, 봉인·사전 명세, 중단·전환 조건, UJ0·UJ6, P1-T07·T14 | docs/09 | §3.2, §7.4, §9.5, §10, §11 |
| family F01–F24, 인과적 개입, 통계와 결과 상태 | docs/08 | §8.3, §8.7, §9.6, §10 |
| 통찰의 운영적 정의 | docs/11 §4 | §2.6, §9.1 |
| 시계와 read·write 분리, 생성물과 관측의 분리 | docs/07 §1–§2 | §3.1, §6.1, §8.1 |
| H-SAMPLE, H-COMPUTE | docs/01 §4 | §2.6 |
| 비용, 같은 장치 규칙, runcrate 위치 규칙 | docs/15 | §6.6, §11.3 |
| 논문 주장 Ck-n | docs/19 | §13 |
| 마스터 결정 MD-1118-A~P | 조사 기록 | 전반 |

### A.4 가칭 목록

사용자 결정 후보(11개):

| 가칭 | 한 줄 |
|---|---|
| DC-W2a-01 | 「입력」의 해석: 학습자(L) 기본, 동반 AI(C)는 변형 |
| DC-W2a-02 | 대상 묶음, T0, 원문 「1904」의 읽기(Y1·Y2) |
| DC-W2a-03 | 입력 tier의 주 판정 단위 |
| DC-W2a-04 | closed-loop(모의 인물) 도입 |
| DC-W2a-05 | 판정 x축과 머리 결과 채널 |
| DC-W2a-06 | 채점자 구성(사람 2인 이상 맹검) |
| DC-W2a-07 | P6 등급 상한(3, 4는 OPEN) |
| DC-W2a-08 | 「아인슈타인 테스트 통과」 문구 금지와 최소 수준 [L*] |
| DC-W2a-09 | stream·rubric·probe 공개 범위와 사료 저작권 |
| DC-W2a-10 | stream 구성에 현대 LLM을 쓰는 범위 |
| DC-W2a-11 | W_delta 투입 방식 |

새 평가 family(4개): F-NEW-W2a-a 발견 곡선(용량–반응), F-NEW-W2a-b 입력 내재 대비 초과, F-NEW-W2a-c 핵심 입력 제거와 stream 특이성, F-NEW-W2a-d 오염·누설 probe.

새 참고문헌(5개): NEW-W2a-01~05(부록 B).

### A.5 통합 때 확인할 것

- docs/09: 표 §3.2가 ET 단별 상한의 기준이다. docs/18·docs/09·docs/19는 값을 복제하지 말고 이 표를 가리킨다. P6 상한 제안은 3이다(DC-W2a-07).
- 대상 묶음 절(§5.3)의 한 줄 자리는 조사 기록의 추천 묶음과 데이터 계획 요약으로 바꾼다. §2.3의 T0 설명과 §5.1의 잠정안, §9.4의 대상 표를 추천 결과와 맞춘다.
- 이 문서의 stream 규모 표(§6.6)는 같은 이름의 TSV에서 계산했다. docs/18의 P0 실행 행렬(ET-0 세계 수, arm 수)과 맞춘다. TSV는 조사 기록의 부록으로 옮기는 것을 제안한다.
- 절 번호 참조(§n.n)는 이 초안의 번호다. 문서 사이의 참조가 바뀌면 이 색인으로 맞춘다.

## 부록 B. 새 참고문헌

catalog.tsv의 8열 형식이다(id, title, category, date_note, url, code_url, status, note). id는 통합 때 catalog의 최종 번호(S47부터)로 바꿨고 괄호에 가칭을 남겼다. 앞의 네 편은 DOI를 레지스트리에서 해석하지 않았고 서지를 2차 출처의 목록에서 가져왔으므로 통합 때 status를 needs-resolution으로 낮췄다. 새 category 값은 필요하지 않다. 네 편은 ET rubric의 근거가 되는 역사적 1차 문헌이라 evaluation으로 둔다.

| id | title | category | date_note | url | code_url | status | note |
|---|---|---|---|---|---|---|---|
| S47 (가칭 NEW-W2a-01) | Über einen die Erzeugung und Verwandlung des Lichtes betreffenden heuristischen Gesichtspunkt | evaluation | 1905년 게재(접수 3월 18일). Annalen der Physik 17권으로 표기됨(2차 출처) | https://doi.org/10.1002/andp.19053220607 | | needs-resolution(통합 때 낮춤: DOI를 해석하지 않았다) | E1905-LQ rubric의 근거 1차 문헌. 서지와 DOI는 2차 출처(백과 문서)의 목록에서 가져왔고 DOI의 해석은 하지 않았다. 본문은 공개 영어 번역(Wikisource)을 조회해 엔트로피의 부피 의존식, 양자 표현, 광전 관계, Stokes 규칙, 이온화를 확인했다. 정독하지 않았다 |
| S48 (가칭 NEW-W2a-02) | Über die von der molekularkinetischen Theorie der Wärme geforderte Bewegung von in ruhenden Flüssigkeiten suspendierten Teilchen | evaluation | 1905년 게재(접수 5월 11일). 권 표기가 17권과 322권으로 갈린다(2차 출처가 불일치를 지적) | https://doi.org/10.1002/andp.19053220806 | | needs-resolution(통합 때 낮춤: DOI를 해석하지 않았다) | E1905-BM rubric의 근거. 서지와 DOI는 2차 출처에서 가져왔고 해석하지 않았다. 확산 계수와 평균 제곱 변위 식은 총설(NEW-W2a-05)의 해당 줄로 확인했다. 논문 속 수치 예는 확인하지 못했다 |
| S49 (가칭 NEW-W2a-03) | Zur Elektrodynamik bewegter Körper | evaluation | 1905년 게재(접수 6월 30일). Annalen der Physik 17권 891–921쪽으로 표기됨(2차 출처) | https://doi.org/10.1002/andp.19053221004 | | needs-resolution(통합 때 낮춤: DOI를 해석하지 않았다) | E1905-SR rubric의 근거. 서지와 DOI는 2차 출처에서 가져왔고 해석하지 않았다. 본문은 공개 영어 번역(Fourmilab)을 조회해 두 가정, 동시성의 정의, 변환식, 귀결, 절 구성을 확인했다. 정독하지 않았다 |
| S50 (가칭 NEW-W2a-04) | Ist die Trägheit eines Körpers von seinem Energieinhalt abhängig? | evaluation | 1905년 게재(접수 9월 27일). Annalen der Physik 18권 639–641쪽으로 표기됨(2차 출처) | https://doi.org/10.1002/andp.19053231314 | | needs-resolution(통합 때 낮춤: DOI를 해석하지 않았다) | E1905-ME rubric의 근거. 서지와 DOI는 2차 출처에서 가져왔고 해석하지 않았다. 본문은 공개 영어 번역(Fourmilab, 1923년 영역판 기반이라 표기가 1920년대 관례)을 조회해 논증과 방사성 물질 언급을 확인했다. 정독하지 않았다 |
| S51 (가칭 NEW-W2a-05) | Albert Einstein: His Annus Mirabilis 1905 | evaluation | arXiv 식별자(physics/0701240, 0701)상 2007년 1월 제출. 제목은 검색 결과의 표기 | https://arxiv.org/abs/physics/0701240 | | metadata-checked | 총설. 브라운 운동 절에서 확산 계수 식과 평균 제곱 변위의 관계가 나오는 줄만 확인했고 전체를 읽지 않았다. 저자와 게재 정보는 확인하지 못했다 |

## 부록 C. 조사 출처

접근일은 모두 2026-11-18이다. 검색어는 논문 제목과 주제어만 썼다. §4의 보도·시간캡슐 모델·참고 영상은 이 초안이 새로 조사한 것이 아니라 2차 정보의 요약이며 조사 기록의 소관이다.

| URL | 접근일 | 읽은 범위 | 확인 수준 |
|---|---|---|---|
| https://en.wikipedia.org/wiki/Annus_Mirabilis_papers | 2026-11-18 | 논문 4편의 독일어 제목, 서지, 접수일과 게재일, DOI, 한 줄 요지의 조회 결과 | 2차 출처 확인. 이 페이지가 Annalen의 권 표기(17, 18)와 DOI의 권(322, 323)이 다르다고 스스로 지적함. 서지의 확정은 조사 기록 |
| https://en.wikisource.org/wiki/Translation:On_a_Heuristic_Point_of_View_about_the_Creation_and_Conversion_of_Light | 2026-11-18 | 절 제목, 엔트로피의 부피 의존식과 확률 논증, 양자 표현, 광전 관계, Stokes 규칙, 이온화(조회 요약) | 번역 본문 조회. 정독 아님. 번역이 학술판과 다를 수 있다는 경고가 있음 |
| https://www.fourmilab.ch/etexts/einstein/E_mc2/www/ | 2026-11-18 | 질량–에너지 논문의 논증 구조, 질량 감소 `L/c²`, 방사성 물질 언급(조회 요약) | 번역 조회. 1923년 영역판 기반의 판이며 표기가 현대 관례로 바뀜 |
| https://www.fourmilab.ch/etexts/einstein/specrel/www/ | 2026-11-18 | 특수상대성 논문의 두 가정, 동시성 정의, 변환식, 귀결, 절 제목(조회 요약) | 번역 조회. 정독 아님 |
| https://arxiv.org/pdf/physics/0701240 | 2026-11-18 | 브라운 운동 절의 확산 계수 식과 평균 제곱 변위 관계가 나오는 줄 | 총설의 해당 줄만. 전체를 읽지 않았다 |
| 저장소 문서(docs/08, docs/09 §1.4·§2·§3·§4·§5 P1, docs/11 §4, docs/01 §4, docs/07 §1–§2, research/2026-11-17-design-review.md의 영상 기록 줄) | 2026-11-18 | 위 범위 | 저장소 기록 |

확인하지 못한 것: 브라운 운동 논문의 수치 예(입자 크기와 분당 변위). 1904년에 완결된 같은 주제의 논문의 유무. W 선행 목록의 날짜(Wien, Planck, 광전 현상 관측, 동시대의 Lorentz 변환 관련 문헌 등)와 같은 시기 비발견자 후보의 사료.
