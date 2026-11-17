# 이상 청사진·비모수 POC·단계별 계획·아인슈타인 테스트 설계: 조사 기록 (2026-11-18)

**상태 라벨:** 설계 작업 기록. 새 설계 문장은 PROPOSAL·OPEN이고 계산 수치는 ESTIMATE / NOT RUN이다. 구현·학습·GPU 실행·비용 지출은 0회다. 작성일 2026-11-18.

**요청 (USER, 2026-11-18):** 원문은 [2026-11-18-discussion.md](/home/jimmy/repos/full-continual-learning/sources/sync/2026-11-18-discussion.md)의 「사용자 원문」 블록에 있다(U-T15). 요청은 7개다.

**답 (요청 7개).**

| 요청 | 결과 | 어디 |
|---|---|---|
| 청사진 | 이상형 System ONE의 feature 32개(8그룹), flow 6개(FL-1~FL-6)와 전체 그림, feature × phase(P0–P6) 해상도 표(칸마다 NP 대역과 학습 모듈을 구분), 사용자 요구 대응표. P0(NP)는 요청된 POC 대역이며 최종형이 아니다. 전부 PROPOSAL이다 | [16-ideal-blueprint.md](/home/jimmy/repos/full-continual-learning/docs/16-ideal-blueprint.md) |
| POC 검증 | P0(NP) = System ONE-NP. gradient 학습 0회, frozen 공개 가중치 LLM과 비모수 schema 기억(NP-0 텍스트, NP-1 잠재, 선택 NP-2). 검증 V0-1~V0-17, suite S-A~S-D, 작업 P0-T01~T21, 실행 행렬 R01~R16(ESTIMATE). 전부 NOT RUN이다 | [18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md), [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md)의 P0(NP) 절 |
| 단계별 구현 | phase 7개 P0(NP)–P6(ET). 매 phase 종료는 실제 `fcl` CLI와 실제 의존성으로 끝까지 도는 전체 제품(UJ0–UJ6)이고 앞 phase 시나리오는 회귀 gate다. 결과 등급 상한과 점진적 해상도 자체 점검표, 결정 D-15~D-47을 더했다 | [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md) |
| 단계별 논문 | PAPER-0, 0b, 1–6. 영어·한국어 작업 제목, 반증 가능한 주장 50개(C0-1~C6-4), 초록 초안(결과는 자리표시자), negative-result판, 투고 후보, docs/14 Ali 공동논문 초안과의 대응 | [19-paper-plan.md](/home/jimmy/repos/full-continual-learning/docs/19-paper-plan.md) |
| runcrate 실험 계획 | P0 실행 행렬의 token·GPU-시간·비용(P10 / P50 / P90, ESTIMATE), 시간캡슐 기반 확보 3안, 시간캡슐 retrofit과 ET run, P1 base 크기 비교, 논문별 「PAPER-k 묶음표」, 2026-11-18 상품 목록 반영. 인스턴스 생성과 비용 지출은 0회다 | [15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md)의 2026-11-18 갱신 |
| 실험 설계(환경·증명·대조·data) | 논문별 설계 표 5줄(실험 환경, 학습 data, test data, 비교 대조, 객관 증명). P0는 「학습 없음」과 기억에 넣는 경험 data를 적었다. 판정 규칙은 형식과 확정 시점만 쓰고 임계값은 dev pilot 뒤 사용자가 승인한다 | [19-paper-plan.md](/home/jimmy/repos/full-continual-learning/docs/19-paper-plan.md), [18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md) §4–§11, [17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md) §10 |
| 아인슈타인 테스트 | 운영 정의 「경험 조건부 발견 시험」(ET), 사다리 ET-0~ET-4(+ET-3p)와 단별 등급 상한·문구, stream 설계와 입력 tier, 누수·사후 편향 통제, 발견 곡선, rubric, 대상 추천(주력 Einstein 1905, pilot Planck 1900·Chadwick 1932, 대안 일반상대성 1915·Turing 1936), 공개 시간캡슐 모델 현황 | [17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md), 부록 [et-targets-research.md](/home/jimmy/repos/full-continual-learning/research/2026-11-18-blueprint-et-design/et-targets-research.md) |

## 1. 방법

- **범위.** 새 문서 4개(docs/16–19), 개정 문서 2개(docs/09·15), 이 기록, 출처 기록·사용자 진술 목록·manifest·README·참고문헌 catalog의 좁은 추가다. 구현·학습·GPU 실행·비용 지출은 하지 않았다.
- **입력 커밋.** d1b855f(= 원격 main, 2026-11-18). 작업은 별도 worktree의 branch `design/2026-11-18-blueprint`에서 했고 push·fetch·rebase·병합은 하지 않았다. 원격 main은 작업 중 움직이지 않았다(조회 기록만 했다).
- **작업 지시.** 마스터 agent가 작업 지시문(저장소 밖의 지시. 사용자 원문, 배경 사실, 마스터 결정, 역할별 수용 항목을 담았다)과 마스터 결정 MD-1118-A~P(아래 §2)를 정했다. 이 결정은 AI agent의 설계 뼈대이며 사용자 결정이 아니다. 조사 결과가 뼈대와 어긋나면 워커가 혼자 고치지 않고 근거와 함께 보고하게 했고, 대상 추천(MD-H)만 조사로 수정하게 했다. 지시문의 배경 사실 중 외부 조사 요약은 마스터가 빠른 웹 검색으로 본 2차 출처였고, 담당 워커가 1차 출처로 확인해 틀린 것을 고쳤다(W2c가 10건, [et-targets-research.md](/home/jimmy/repos/full-continual-learning/research/2026-11-18-blueprint-et-design/et-targets-research.md) §7).
- **역할 9개와 순서.** 작업 지시문의 9개 역할을 워커 6명이 나눠 맡았다. 1단계 W1·W2a·W2b·W2c·W3가 초안을 쓰고, 2단계 W4·W5·W6이 1단계 초안을 읽고 쓰고, 3단계 W7이 통합했다. 단계 순서는 역할별 완료 표시 파일과 공용 시계로 지켰다. 같은 단계의 워커는 서로의 초안을 읽지 못하게 했고, 어긋남은 소유자 기준(지시문 §3-2)으로 W7이 맞췄다.

| 역할 | 맡은 일 | 산출 | 상태 |
|---|---|---|---|
| W1 | 이상 청사진 | docs/16 | COMPLETE |
| W2a | ET 절차 설계 | docs/17 | COMPLETE |
| W2b | 선행 연구 지형과 논문별 차별점 조사 | related-work.md(부록) | COMPLETE |
| W2c | ET 대상·시간캡슐 기반 모델·사료 조사 | et-targets-research.md(부록) | COMPLETE |
| W3 | P0 비모수 POC 설계와 검증 계획 | docs/18 | COMPLETE |
| W4 | 로드맵 개정 | docs/09(기존 줄 보존, 보충만) | COMPLETE |
| W5 | 단계별 논문 계획 | docs/19 | COMPLETE |
| W6 | 계산 계획 갱신 | docs/15(기존 줄 보존, 보충만) | COMPLETE |
| W7 | 통합: 저장소 반영, 정합, 검증, 커밋 | 이 기록과 출처·참고문헌·README | 이 기록 |

워커 6명이 나눈 방식은 W1 / W3 / W2a→W4 / W2b→W5 / W2c→W6 / W7이다. 뒤 역할은 앞 역할의 완료 표시를 기다려 시작했다.

- **저장소 쓰기.** 저장소에 쓴 것은 W7뿐이다. 새 문서는 초안 폴더에서 .txt로 완성해 복사했고, 기존 문서(docs/09·15)는 초안의 사본에서 기존 줄을 지우지 않고 「2026-11-18 개정」 보충만 더하는 방식으로 고쳤다. 기존 파일의 이동·이름 변경·삭제는 없다.
- **검증 도구와 한계.** 문서 검사는 `tools/validate_docs.py`와 같은 검사를 하되 절대 링크를 worktree로 바꿔 해석하는 wrapper(저장소 밖)로 돌렸다. 공개 안전성은 추가된 줄만 보는 검사 스크립트 2개(통합 담당용, 마스터용)로 확인했다. mermaid는 정적 점검만 했고 실제 parser 검사는 마스터가 브라우저로 한다.

## 2. 마스터 결정 MD-1118-A~P

작업 지시문의 §2를 공개용으로 옮긴 것이다. 모두 마스터 agent의 설계 결정이고 PROPOSAL이다. 사용자가 말한 것은 [2026-11-18-discussion.md](/home/jimmy/repos/full-continual-learning/sources/sync/2026-11-18-discussion.md)의 원문뿐이다. 사용자 확인이 필요한 해석은 §6에 올렸다.

| ID | 결정 | 내용 |
|---|---|---|
| MD-1118-A | 최종 목표와 사다리 | 최종 목표는 아인슈타인 테스트다. 운영 정의는 「경험 조건부 발견 시험」(ET)이다. ET는 마지막 phase에만 두지 않고 P0부터 가장 얇은 형태로 넣어 phase마다 해상도를 올린다. ET-0 합성 미시 발견 세계(누수 0, 객관 채점, 대량). ET-1 재분장(re-skin)한 역사 원형 사례(실제 발견의 구조를 보존하고 이름·상수·표면을 바꾼다, 오염 probe 부착). ET-2 공개 모델의 지식 마감 이후에 나온 실제 사례(실제 텍스트, 소수). ET-3 시간캡슐 기반 모델 + 개발용(pilot) 역사 대상으로 해상도가 둘이다. ET-3p(미리보기)는 무학습 NP 시스템을 공개 시간캡슐 모델에 얹어 절차를 처음부터 끝까지 한 번 돈다(절차·채점·누수 감사가 도는지 확인하는 것이 목적이고 발견 여부는 주장하지 않는다). ET-3(정식)은 System ONE을 시간캡슐 모델에 retrofit해서 돈다. ET-4는 시간캡슐 기반 모델 + 봉인된 주력 대상 묶음이며 최종 판정이다. 「탐색」은 결과 등급 2 이하로만 보고하고 「발견했다」·「확증」 문구를 쓰지 않는다는 뜻이다 |
| MD-1118-B | phase 구성 | P0(신설, 비모수 POC) → P1–P5(기존, 조정) → P6(신설, 역사 ET 최종). 모든 phase는 같은 `fcl` 제품의 해상도를 올린 것이고 phase마다 독립 논문 1편(PAPER-0~6)을 낸다. 대응은 아래 표를 기본으로 했다. 이름 규칙: 새 phase는 처음 나올 때 「P0(NP)」, 「P6(ET)」로 쓰고 2026-11-03 계획의 이름은 「옛(11-03) P0」처럼 쓴다. 「P1은 MVP」와의 관계: P0(NP)가 뼈대와 전체 여정을 먼저 세우고 P1이 첫 학습 해상도가 되는 해석이며, 사용자 원문의 순서(POC를 먼저 하고 그 뒤에 단계별로 구현한다)에 맞춘 것이므로 사용자 확인 항목이다 |
| MD-1118-C | P0의 정의: System ONE-NP | gradient 학습은 0회다. 고정(frozen) 공개 가중치 LLM과 비모수 schema 기억으로 전체 flow(입력 → 인식 → 경로 선택 → 계산 → 출력 → 결과 → 쓰기 → Sleep → 발견)를 실제 CLI에서 끝까지 돈다. 이상형 feature마다 같은 계약(interface)의 비모수 대역(stand-in)을 두고 이후 phase가 대역을 학습 모듈로 하나씩 바꾼다. NP-0(필수)은 텍스트 artifact schema(구조화 기록과 임베딩, frozen LLM이 추상화와 정합 판정). NP-1(필수 arm)은 잠재 artifact schema(frozen LLM activation에서 function/task vector를 추출·저장·주입하고 hidden-state kNN key–value로 결합 기억). NP-2(선택 arm)는 닫힌 꼴 선형 expert(고정 특징 위의 Delta/RLS·ridge, backprop은 없지만 파라미터는 있어 「비모수」에 넣을지는 사용자 결정 후보). 생명주기는 CRP식 사전과 정합도 우도로 read / update / branch / create / hold / evict를 판정하고, 보존 예산 아래 eviction을 두며 source 삭제 계약을 지킨다. controller는 규칙형(fast / learn / deep에 hold 추가). Sleep-NP는 오프라인 군집·병합·추상화, 재조합 후보 생성, 저장된 근거에 비춘 자가 검사. 깊이는 NP에서 숙의 반복 수·생성 token·LLM 호출 수로 잰다. NP-0의 추상화와 Sleep의 재조합 후보는 frozen LLM이 만든 생성물이므로 관측 증거와 섞지 않는다(docs/07 §1–2, F20·F21을 NP arm에도 적용) |
| MD-1118-D | P0의 한계와 지위 | P0는 사용자가 요청한 POC이고 외부 frozen LLM을 쓰는 대역이다. 최종형이 아니다(U05, docs/05 §3, docs/09 §1.3). 가중치 수준의 schema 형성, 간섭 해소, 통합 모델의 내부 depth 효율은 P0로 주장하지 않는다. P0의 NP arm은 이후 모든 phase의 영구 대조군이고, 학습 모듈은 같은 예산의 NP보다 나을 때만 필요하다고 주장한다. P0는 mock이나 조사 단계가 아니라 실제 LLM·실제 저장·실제 CLI로 도는 완결 제품이다 |
| MD-1118-E | P0 검증 suite | suite S-A는 조건부 판단 세계(자연어 렌더링, docs/09 P1-T06의 세계 생성기 설계와 docs/08의 관련 family를 재사용). suite S-B는 미시 발견 세계(ET-0, 원형 4종: 숨은 변수·새 개념 도입 / 먼 영역에서의 유추 전이 / 두 이론의 충돌을 공통 가정의 수정으로 통합 / 분류 체계의 빈칸 예측, 지표는 docs/11 §4의 통찰 정의와 F13·F16을 먼저 재사용). suite S-C는 재분장 역사 사례(ET-1, 탐색). suite S-D(선택)는 frozen LLM 내부의 schema 중첩 관찰 분석(Base 대 post-training 변형 비교, docs/13의 가설의 무학습 관찰판). ET-3p run은 suite가 아니라 P0 끝의 실제 실행 1회다 |
| MD-1118-F | P0 대조군 | 모두 같은 frozen LLM과 같은 token·호출·저장 예산을 쓴다. 기억 없음, 전체 이력 long-context, dense RAG, 요약 기억, 통찰·전략 기억 계열, 개념 기억 계열, 생명주기 없는 평면 schema, controller 없음(항상 fast / 항상 deep), Sleep 없음, wrong-schema swap(인과 개입), oracle schema(진단 상한). 문헌의 방법 이름은 실제로 확인한 것만 쓴다. docs/09 §3의 「고정·무구조·항상-갱신」 대조는 NP에서 「기억 없음·평면 기억·항상 쓰기」로 대응시킨다 |
| MD-1118-G | ET 운영 정의의 원칙 | W(≤T0)는 T0까지의 모든 연구 결과(동료 연구 포함)이며 시간캡슐 기반 모델의 사전학습 지식이 맡는다. P_pre(≤T0)는 대상 인물이 그때까지 했을 법한 입력(형성기), P_post(T0..T1)는 연구기 입력이며 발견 진술 자체는 뺀다. 「입력」은 그 인물이 우리 시스템을 자기 AI로 썼다면 넣었을 법한 것(READ / OBSERVE / NOTE / QUESTION / DISCUSS / TRY)이고 그 인물이 겪은 경험의 stream과 같은 것으로 본다. 두 해석(인물의 경험을 받는 학습자 / 인물과 대화하는 동반 AI)의 차이와 기본 선택은 문서에 밝히고 사용자 확인 대기로 올린다. 시간순으로 넣고 checkpoint마다 중립 probe로 발견 정도를 채점해 「어떤 data까지 넣었을 때 발견이 나오는가」의 곡선을 얻는다. 입력 tier는 A(날짜 있는 1차 사료만), B(+회고 자료의 조심스러운 재구성), C(+사료 제약 아래 합성한 「했을 법한」 입력). 입력 내재 수준을 같은 rubric으로 채점해 시스템 출력이 입력의 되풀이인지 넘어선 것인지 구분한다. 사후 편향 감사(항목마다 날짜가 t 이하인 출처, 정답 누설도 채점, 누설 항목을 뺀 실험)와 대조 stream(없음, 순서 섞기, 같은 시기 비발견자, 무관한 인물, 핵심 입력 제거)을 둔다. 기본은 open-loop이고 closed-loop는 OPEN이다. T0 이후의 세계 지식 W(T0..t)는 기반 모델을 다시 학습하지 않고 System ONE의 지속학습 입력으로 넣는 안을 기본으로 검토한다 |
| MD-1118-H | ET 대상 추천(잠정안, 조사로 수정) | 공개 시간캡슐 모델의 지식 마감에 맞춰 고르는 쪽을 기본으로 했다. 주력 후보 Einstein 1905(T0 = 1900 말, 기반 후보 pre-1900 공개 모델), 후보 일반상대성 1915(T0 = 1911–1913, 마감 1913 공개 모델), 후보 1930년 이후의 발견(마감 1929–1946 공개 모델), 후순위 이른 시기 대상(자체 사전학습이 필요하며 ET-1 재료로는 사용). 개발용(pilot) 대상과 봉인된 주력 대상을 나누고, 최종 추천은 기준표(직관 의존도, 날짜 있는 과정 기록의 양과 신뢰도, 지식 마감이 맞는 공개 시간캡슐 모델, T0 이전 corpus 확보, 채점 객관성, 누수 통제 가능성, 언어, 저작권)로 정한다. 조사 결과는 [17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md)와 이 기록의 부록에 있다 |
| MD-1118-I | 누수 통제 원칙 | 현대 LLM은 역사적 발견을 이미 알므로 ET-0·1·2에서는 같은 frozen LLM 안의 arm 사이 상대 효과만 주장하고, 「발견했다」는 절대 주장은 시간캡슐 기반(ET-3·4)에서만 한다. ET-1에는 모델이 원 사례를 알아보는지 재는 오염 probe를 붙인다. ET-3p·ET-3·ET-4에서 시스템 안의 모든 생성·판정·검색은 시간캡슐 모델만 쓴다(현대 임베딩 모델도 누수 경로이므로 검색은 시간캡슐 모델의 hidden state나 어휘 기반 방법으로 한다). 현대 모델은 시스템 밖(채점 보조, stream 구성 보조)에서만 쓰고 사람이 누수를 감사하며, stream 구성에 쓰면 입력 tier C 표시와 누설도 채점을 붙인다. 시간캡슐 모델 자체의 누수(후대 판본·주석·OCR 메타데이터, 현대 모델로 만든 SFT data)를 점검 항목으로 둔다 |
| MD-1118-J | 논문 | phase마다 1편이다. 영어 제목과 초록(결과 자리는 대괄호 자리표시자), 한국어 제목과 요약을 쓴다. 주장은 반증 가능하게 쓰고 실험·지표·대조·판정 규칙에 연결한다. 가설이 틀렸을 때의 논문(negative-result판)도 준비한다. docs/14의 Ali 공동논문 초안과의 대응을 표로 밝힌다. 외부 발송·연락은 범위 밖이다. 선택 논문 PAPER-0b(ET 절차·benchmark 논문)는 계획만 쓰고 낼지는 사용자 결정이다. 문구는 docs/09 §3의 등급별 규칙을 따르고 초록은 필요 등급을 채워 PASS한 경우의 문장으로 쓰되 등급에 못 미치면 pilot 문구나 negative-result판으로 바꾼다. 상세도는 PAPER-0·0b·1은 실험 설계까지 자세히, PAPER-2·3은 중간, PAPER-4·5·6은 제목·논지·주장의 형식·초록 뼈대와 목표·gate·선택지·결정 대기 항목까지다 |
| MD-1118-K | 구현 위치(제안, 사용자 결정) | 공개 저장소의 `fcl/` 패키지에 두고 Melete에서 파일 단위로 골라 옮긴다. 옮기기 전에 비공개 내용을 점검한다 |
| MD-1118-L | 사용자 결정 번호 | 워커는 가칭 DC-Wn-nn으로 후보를 냈고, 최종 번호(D-15부터)는 W4와 통합 담당이 붙였다. 대응표는 §4 |
| MD-1118-M | P0 검증 항목의 최소 집합 | schema 형태 기억 대 사례·검색 기억(2×2 표면/구조), 분해 대 단일 기억(A → B → A 재방문), context gating(Read)과 wrong-schema swap, 생명주기(in-place update 대 create, version 되돌리기, eviction, source 삭제 계약), 익숙함 기반 경로 선택(H-COMPUTE의 NP판), 적은 사례의 성급한 일반화와 수정(H-SAMPLE의 NP판), 관심·수준 admission(흘려듣기), Sleep-NP, 발견(ET-0)과 입력량에 대한 용량–반응, 잠재 artifact(NP-1)의 저장·재적재·합성, (선택) suite S-D 관찰 분석, ET-3p(절차가 끝까지 도는가, 결과 주장 없음) |
| MD-1118-N | 공통 척도와 가설 | 발견 수준: L0 없음 / L1 긴장 인식 / L2 재구성 가설 / L3 원리 진술과 핵심 관계의 유도(정량) / L4 원리에서 새 예측을 도출(역사적 발견의 예측과 일치) / L5 논문 수준의 체계화. H-DISCOVER(PROPOSAL): 「T0까지의 세계 지식을 가진 기반 위에서, 한 인물의 경험 stream을 schema로 쌓고 미해결 불일치를 보존했다가 재조합·재구조화하는 시스템은, 같은 기반에 같은 자료를 기억 없이 또는 평면 기억으로 준 경우보다 (i) 더 적은 입력에서 (ii) 더 높은 발견 수준에 이르고, (iii) 그 차이는 stream의 내용에 특이적이다(대조 stream에서는 나오지 않는다).」 헌장 docs/01 §4의 두 중심 명제에 없는 세 번째 명제이므로 헌장 개정이 아니라 PROPOSAL·OPEN으로 표기한다 |
| MD-1118-O | 대역 교체 원칙과 base 일치 규칙 | 모든 phase에 모든 feature가 있고 형태가 NP 대역이거나 학습 모듈일 뿐이다. capability 표의 칸은 NP 대역과 학습 모듈을 구분해 쓴다. 모든 비교는 같은 base에서 하고 NP arm은 그 phase의 base 모델로 다시 돈다. base의 언어 능력이 필요한 NP-0이 작은 base에서 성립하지 않으면 그 사실을 보고하고 NP-1을 대조로 쓴다. P0는 주 모델(8B급) 말고도 P1 base급(135M급)에서 NP-1 arm이 성립하는지를 계획에 넣는다. P1 base를 135M급으로 둘지 1.7B–4B급으로 올릴지, hold 경로를 P1 controller v0에도 넣을지는 비용과 함께 결정 후보다 |
| MD-1118-P | 등급 상한 | P0의 최대 결과 등급은 주장 단위로 3이다. docs/09 §3의 「실제 갱신」은 P0에서 「실제 비모수 state 쓰기」로 읽는다(OPEN, 사용자 확인). suite S-A·S-B의 개별 주장이 봉인 manifest·fresh locked cohort·같은 예산 대조·구조 family 2종 이상·사전 명세 seed·독립 검토를 모두 채울 때만 3을 시도하고 그 밖의 P0 주장은 2 이하다. ET-1·ET-3p는 탐색이다. ET 단별 상한과 문구는 [17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md)의 표 하나가 정한다. 논문의 핵심 주장에 필요한 등급이 phase 상한보다 높으면 두 안을 나란히 쓴다(그 phase에 등급 3 조건을 채우는 작업을 더하거나, pilot 문구의 논문으로 낸다) |

MD-1118-B의 phase와 ET 단 대응(기본안. 개정 로드맵이 바꾼 곳은 [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md)가 기준이다).

| phase | 제품 한 줄 | ET (판정 대상) | ET (탐색·회귀) |
|---|---|---|---|
| P0 | System ONE-NP: frozen LLM + 비모수 schema 기억, 무학습 | ET-0 | ET-1, ET-3p |
| P1 | 소형 모델 retrofit(NMM·CMS), 규칙형 controller v0 | ET-0 (학습 arm 대 NP arm) | ET-3p 회귀 |
| P2 | 구조 family × depth | ET-0 깊이 곡선 | ET-1 |
| P3 | 학습된 controller, 선택적 write, accommodation | ET-1 | ET-2 |
| P4 | Sleep, 세션 간 경험, 외부화 | ET-1 잠복 효과, ET-2 | ET-3(pilot 대상) |
| P5 | 더 큰 모델·시간캡슐 기반 retrofit, 실제 consumer | ET-3 | 없음 |
| P6 | 역사 ET 최종 | ET-4 | 없음 |

## 3. 조사한 출처와 확인 수준

외부 조회는 공개 웹 페이지(공식 논문·저널·학회 페이지, 모델 카드, 저자 블로그, 공식 저장소 README, 보도)만 썼다. 검색어는 논문 제목과 주제어만 썼다. 전문 정독(fulltext-read)은 한 건도 없고 코드 실행·재현도 없다. 접근이 막힌 보도(유료 기사, 차단된 서버)는 요약 수준으로만 확인했고 원문을 읽었다고 쓰지 않았다. 항목별 URL·접근일·읽은 범위·확인 수준은 각 부록의 「조사 출처」에 있다.

| 영역 | 담당 | 읽은 것 | 확인 수준 | 위치 |
|---|---|---|---|---|
| Einstein test의 출처·판본·비판, 참고 영상 | W2c | 잡지 인터뷰 기사, 2026-02 발언 보도, 2026-05·2026-10 보도, 학술 의견 글(CACM 2쪽 전문), 비판 글, Talkie 보고서의 재인용. 참고 영상은 존재와 제목만 | 학술 의견 글은 직접, 보도는 요약, 영상 내용은 미확인(needs-resolution) | [et-targets-research.md](/home/jimmy/repos/full-continual-learning/research/2026-11-18-blueprint-et-design/et-targets-research.md) §5 |
| 시간캡슐 언어모델 현황 | W2c | GPT-1900 계열 블로그와 모델·데이터 카드, TypewriterLM 논문 v2 일부와 HF 메타데이터, Talkie-1930 보고서·카드·README, Ranke-4B README·사전 공개 노트 앞부분·HF API, TimeCapsuleLLM, 그 밖 2종은 목록 수준 | 대부분 직접, 일부 부분 열람, 2종은 2차 | [et-targets-research.md](/home/jimmy/repos/full-continual-learning/research/2026-11-18-blueprint-et-design/et-targets-research.md) §1 |
| ET 대상 후보와 데이터 계획 | W2c | 후보 16개, 추천 5개의 W(≤T0)·W(T0..t)·인물 사료·비발견자 사료 | 역사 일반지식과 백과 열람 수준. 개별 사료 열람은 미확인 | [et-targets-research.md](/home/jimmy/repos/full-continual-learning/research/2026-11-18-blueprint-et-design/et-targets-research.md) §2–§4 |
| Einstein 1905 논문 4편 | W2a | 백과 문서의 서지, 공개 영어 번역 본문 조회(정독 아님), 총설의 해당 줄 | 2차와 번역 조회. 서지의 DOI는 해석하지 않음 | doc17-appendices.md |
| 선행 연구 140건과 투고처 | W2b | arXiv 초록 페이지, DOI·도서 레지스트리, 학회·학술지 공식 페이지. PDF 발췌 3건 | metadata-checked 수준. 2026-06 이후 preprint는 심사 전 | [related-work.md](/home/jimmy/repos/full-continual-learning/research/2026-11-18-blueprint-et-design/related-work.md) |
| frozen LLM 후보와 NP 문헌 | W3 | 모델 카드 3종, arXiv 초록 7건, host의 llama.cpp 도움말과 Python 패키지 설치 여부(로컬 확인), 비공개 Melete 저장소의 고정 커밋 파일 목록·머리글(읽기 전용) | 카드 직접, 초록 수준, 로컬 확인 | doc18-appendices.md |
| 계산 입력 | W6 | Qwen3-4B 설정 파일, 2026-11-17 공개 입력표, runcrate 상품 목록의 종류·가격(공개 열만) | 직접 | doc15-appendices.md |
| 저장소 문서 | W1·W3·W4·W5 | docs/01–15, 2026-11-12·17 기록, 사용자 진술 원문 | 저장소 본문 | 각 부록 C |

새 참고문헌은 163행을 [catalog.tsv](/home/jimmy/repos/full-continual-learning/references/catalog.tsv)에 더했다. status는 metadata-checked 150 / official-search-checked 6 / needs-resolution 7이다(needs-resolution에는 DOI를 해석하지 않은 Einstein 1905 논문 4편을 낮춰 넣은 것이 포함된다). 같은 URL의 가칭 5개는 먼저 온 행으로 합쳤다. 기존 133행과 URL 또는 arXiv 번호가 겹친 행은 없었다.

## 4. 가칭 → 최종 번호 대응

워커는 가칭(DC-Wn-nn, F-NEW-Wn-a, NEW-Wn-nn)으로 후보를 냈고 통합 담당이 최종 번호를 붙였다. 대응 전부는 [id-map.tsv](/home/jimmy/repos/full-continual-learning/research/2026-11-18-blueprint-et-design/id-map.tsv)에 있고(가칭, 최종, 정의된 곳, 메모) 아래는 요약이다. 공개 문서(docs/09·15–19)에는 최종 번호만 쓰고, 부록의 초안 원문에는 가칭을 남겼다(참고문헌 표는 최종 번호와 가칭을 함께 적었다).

### 4.1 사용자 결정 후보(가칭 54개 → 번호 36개)

D-15~D-38은 로드맵 개정 담당(W4)이 붙였고, W2b·W5·W6의 후보는 통합 담당이 D-39~D-47로 이었다. 기존 번호(N-5, N-6, N-11, D-11, D-20, D-22, D-29, D-38)와 겹치는 후보는 새 번호를 만들지 않았다.

| 최종 번호 | 가칭 | 합친 내용 |
|---|---|---|
| D-11 | DC-W1-06 | 새 행 없음. 외부 consumer 접점을 P0부터 얇게 둘지는 D-11에 합침 |
| D-16 | DC-W3-02 | NP-2를 「비모수」에 포함할지 |
| D-17 | DC-W3-04 | 「실제 갱신」의 P0 해석 |
| D-18 | DC-W3-03 | P0 종료 gate에 sealed readout 포함(D-07의 P0판) |
| D-19 | DC-W3-01 | frozen LLM 주 모델·복제 모델·backend |
| D-20 | DC-W3-06, DC-W6-04 | P1 base 크기 / P1 base 크기. D-20에 합침 |
| D-21 | DC-W1-02, DC-W3-05 | hold 경로. DC-W3-05와 한 행(추천이 달라 양쪽을 적음) / hold 경로. DC-W1-02와 한 행 |
| D-22 | DC-W3-08, DC-W3-09, DC-W2b-01 | NP 대조군의 충실도. DC-W3-09와 한 행 / NP-0의 생성·판정 분리. DC-W3-08과 한 행 / P0 대조군의 구현 출처. D-22(NP 대조군의 충실도)에 합침 |
| D-23 | DC-W3-07 | 구현 위치와 Melete 파일 이관 |
| D-24 | DC-W1-01, DC-W1-07 | feature 목록(BF-D4 포함)과 용어 개정 범위를 한 행으로 합침(DC-W1-07과) / DC-W1-01과 한 행 |
| D-25 | DC-W1-03 | branch와 create의 분리. N-4와 구분 |
| D-26 | DC-W1-04 | 발견 feature 묶음과 H-DISCOVER를 헌장에 올릴지. N-8과 묶을 수 있음 |
| D-27 | DC-W1-05 | 발견 feature의 학습 모듈을 둘 phase |
| D-28 | DC-W2a-02, DC-W2c-01, DC-W2c-02 | 대상 묶음·T0·원문 「1904」의 읽기를 한 행으로 합침(DC-W2c-01·02와) / ET 대상 묶음 / 주력의 기반 checkpoint와 T0 |
| D-29 | DC-W2c-03, DC-W2c-07, DC-W6-03 | TypewriterLM 라이선스. 시간캡슐 확보 방식과 한 행 / 시간캡슐 모델 공개 상태의 재점검 주기. 결정자는 마스터였으나 합치며 사용자로 적음 / 시간캡슐 기반 확보 안. D-29에 합침 |
| D-30 | DC-W2a-01 | 「입력」의 해석(학습자 L / 동반 AI C) |
| D-31 | DC-W2a-03, DC-W2a-05 | 입력 tier의 주 판정 단위. DC-W2a-05와 한 행 / 판정 x축과 머리 결과 채널. DC-W2a-03과 한 행 |
| D-32 | DC-W2a-04, DC-W2a-11 | closed-loop 도입. DC-W2a-11과 한 행 / W_delta의 투입 방식. DC-W2a-04와 한 행 |
| D-33 | DC-W2a-06 | ET 채점자 구성 |
| D-34 | DC-W2a-07, DC-W2a-08 | P6의 등급 상한. DC-W2a-08과 한 행 / 「통과」 문구와 최소 수준. DC-W2a-07과 한 행 |
| D-35 | DC-W2a-09, DC-W2c-06 | 사료 공개 범위·저작권. DC-W2c-06과 한 행 / 사료 접근 비용. DC-W2a-09와 한 행 |
| D-36 | DC-W2a-10, DC-W2c-04 | stream 구성에 현대 LLM. DC-W2c-04와 한 행 / 독일어 사료의 처리. DC-W2a-10과 한 행 |
| D-37 | DC-W2c-05 | 참고 영상의 정체 |
| D-38 | DC-W5-01, DC-W5-02 | PAPER-0b를 낼지와 시점. W4가 만든 D-38(논문 전략)에 합침 / PAPER-1의 필요 등급과 phase 상한의 어긋남 처리. D-38에 합침 |
| D-39 | DC-W2b-02 | 외부 발견 benchmark 앵커 |
| D-40 | DC-W2b-03, DC-W2b-04 | 제출 4주 전 선행 연구 재조회 gate. DC-W2b-04와 한 행 / PAPER-0b의 투고 성격. DC-W2b-03과 한 행 |
| D-41 | DC-W5-05, DC-W5-11 | 사전 등록(manifest hash)의 공개 시점. DC-W5-11과 한 행 / preprint 공개 시점. DC-W5-05와 한 행 |
| D-42 | DC-W5-03, DC-W5-04 | phase마다 1편 고정. DC-W5-04와 한 행 / PAPER-0의 범위. DC-W5-03과 한 행 |
| D-43 | DC-W5-06 | 핵심 주장 FAIL일 때 negative-result판을 낼지 |
| D-44 | DC-W5-07 | 논문 공개물의 범위 |
| D-45 | DC-W5-10 | 제목의 「Einstein」과 「통과」 문구. D-34와 함께 본다 |
| D-46 | DC-W6-01 | P0 서빙 방식과 보조 run의 모델 크기. D-19와 함께 본다 |
| D-47 | DC-W6-05 | 자체 사전학습용 다중 GPU 노드와 월 약정 |
| N-5 | DC-W5-09 | 실험 B(Base와 post-training)의 배치. 기존 N-5에 합침 |
| N-6 | DC-W5-08 | Ali 공동논문과 PAPER-3·4의 관계. 기존 N-6(Ali 제안문 수정안의 승인·발송 여부·축 추가)에 합침 |
| N-11 | DC-W6-02 | P0 클라우드 비용 상한과 FCL 전용 키·예산. 기존 N-11(과 D-04)에 합침 |

### 4.2 새 평가 family 후보(가칭 8개 → F25~F31)

[16-ideal-blueprint.md](/home/jimmy/repos/full-continual-learning/docs/16-ideal-blueprint.md)의 가칭과 [18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md)의 가칭이 같은 후보로 보여 하나로 합쳤다. 이 후보들은 docs/08에 등록하지 않았고(docs/08은 고치지 않았다) 등록은 사용자 결정이다(N-5와 연결).

| 최종 번호 | 가칭 | 정의된 곳 | 한 줄 |
|---|---|---|---|
| F25 | F-NEW-W1-a, F-NEW-W3-a | docs/16 §8.2 / docs/18 §5.5 | 긴장 보존과 지연 해소. docs/18 §5.5의 F-NEW-W3-a와 같은 후보를 합침 |
| F26 | F-NEW-W2a-a | docs/17 §8.7 | 발견 곡선(용량–반응) |
| F27 | F-NEW-W2a-b | docs/17 §8.7 | 입력 내재 대비 초과 |
| F28 | F-NEW-W2a-c | docs/17 §8.7 | 핵심 입력 제거와 stream 특이성 |
| F29 | F-NEW-W2a-d | docs/17 §8.7 | 오염·누설 probe |
| F30 | F-NEW-W3-b | docs/18 §5.5 | 원리 도출과 귀결 예측 |
| F31 | F-NEW-W3-c | docs/18 §5.5 | 잠재 artifact 재적재와 합성 |

### 4.3 새 참고문헌(가칭 168개 → catalog 번호 163개)

새 접두는 만들지 않았다. 접두는 references/README.md의 분류(N 기억·인지, S SBL·표상·평가, A 아키텍처, E 자동 연구·진화)와 W2b의 제안(평가·agent 기억·steering·발견 benchmark는 S, 모델 구조·지속학습·test-time 학습·깊이·모델 카드는 A, AI 과학자·발견 시스템은 E, 인지과학 고전은 N)을 따랐다. R(리듬·가소성)은 쓰지 않았다. category 값은 기존 9개 안에서 골랐다.

| 출처 초안 | 가칭 범위 | 가칭 수 | catalog에 더한 행 | 최종 번호 | 같은 URL로 합친 가칭 |
|---|---|---|---|---|---|
| W2a | NEW-W2a-01~05 | 5 | 5 | S47~S51(5행) | 0 |
| W2b | NEW-W2b-001~140 | 140 | 140 | N33~N39(7행), S52~S145(94행), A39~A68(30행), E06~E14(9행) | 0 |
| W2c | NEW-W2c-01~16 | 16 | 16 | S146~S159(14행), A69~A70(2행) | 0 |
| W3 | NEW-W3-01~06 | 6 | 1 | S160 | 5 |
| W6 | NEW-W6-01 | 1 | 1 | A71 | 0 |

## 5. 정합 점검 기록

소유자 기준(작업 지시 §3-2)으로 문서 사이를 맞췄다. 고친 것, 일치를 확인한 것, 맞추지 못해 OPEN으로 둔 것을 [consistency.tsv](/home/jimmy/repos/full-continual-learning/research/2026-11-18-blueprint-et-design/consistency.tsv)에 문서·위치·내용·기준 문서로 남겼고 아래에 옮겼다. 뜻을 바꾸는 수정은 하지 않았다.

| 문서 | 위치 | 무엇을 | 기준 문서 |
|---|---|---|---|
| docs/17 | §2.3 T0 행, §5.3, §6.4 | [고침] 주력 Einstein 1905의 T0를 기반 GPT-1900의 마감 1900-01-01로 맞추고 MD-1118-H 잠정안(1900년 말)과의 차이를 적음. 기반 마감과 대상 연표의 틈 문장을 일반 규칙으로 고침 | 조사 기록 et-targets-research.md §3-3·§4-1 |
| docs/17 | §3.2 5항, §4 표 4행, §12.1 RSK-11 | [고침] 「GPT-1900에서 재발견은 대부분 실패」, 「Ranke-4B 공개」, 판본 (b)가 신문 인물 기사 인용 보도뿐이라는 서술, 「공개된 실행 절차가 없다」를 W2c가 1차 출처에서 확인한 내용으로 바꿈 | 조사 기록 et-targets-research.md §5·§7 정정 2·3·6·7 |
| docs/17 | §5.3, §5.1 말미 | [고침] 대상 묶음 자리를 W2c의 추천 묶음(주력·pilot·대안)과 데이터 계획 요약, 달라진 점으로 채움. 대상 ID TG-nn을 이 절에서 정의 | 조사 기록 et-targets-research.md §3–§4 |
| docs/17 | §9.4 | [고침] rubric 상태표의 행을 추천 대상(TG-02, TG-06, TG-03, TG-07)에 맞춤 | 조사 기록 et-targets-research.md §4 |
| docs/17 | §6.6 | [고침] ET-3p run 수(일반 식 1 / 6 / 36)와 docs/18 R15의 arm과 stream 조합 수(1 / 11 / 14)가 다른 이유를 출처와 함께 병기 | docs/18 §6.3 |
| docs/17 | §4, §5.2, §8.5, §12.1, §13 | [고침] 위험 ID R1~R13을 RSK-1~RSK-13으로 바꿈(P0 실행 행렬 run ID R01~R16, catalog의 R 접두 번호와 겹침) | docs/18 §10, references/catalog.tsv |
| docs/17 | §8.7 | [고침] 새 평가 family 후보를 F26~F29로 번호를 붙이고 F25(긴장 보존과 지연 해소, docs/16·18)와 연결 | docs/16 §8.2, docs/18 §5.5 |
| docs/18 | §11.1 시간캡슐 모델 3행 | [고침] 확인 수준을 W2c의 1차 확인(예시 모델·크기·마감·라이선스·형식)으로 갱신 | 조사 기록 et-targets-research.md §1 |
| docs/15 | §6.7 ET-3p run | [고침] R15가 이미 docs/17의 ET-3p 규모(330 / 900 / 2,400항목)를 입력으로 쓰는데 「R15는 60 / 150 / 400항목, docs/17 규모는 6배」라는 서술과 6배 확대 행이 있었다. 한 행으로 정리(공개 TSV tc-retrofit-et.tsv도 같게) | docs/18 §6.3, 실행 행렬 R15 |
| docs/15 | §6.7 민감도 표, p0-sensitivity.tsv | [고침] 서버형 + 4B급 행의 한 값(과금 시간의 P10)을 이웃 칸과 같은 정수 자릿수로 반올림 | docs/15 §6.7 |
| docs/09 | §10 결정표 | [고침] W2b·W5·W6의 후보를 D-39~D-47로 잇고 D-20·D-22·D-29·D-38·N-5·N-6·N-11에 합친 것을 적음. 「2026-11-18 갱신」 비용 주석을 11-17 비용 수치 아래에 더함 | docs/15 §6.7–§6.11, id-map.tsv |
| docs/09 | P6(ET) 절 종료 gate (4) | [고침] 「PAPER-6 주장」을 C6-1~C6-4로 맞춤 | docs/19 §10 |
| docs/16 17 18 19 15 | 결정 후보 표, 머리, 본문 | [고침] 가칭 DC-Wn-nn을 D-번호(또는 N-번호)로, F-NEW-*를 F25~F31로, NEW-W*를 catalog 번호로 바꾸고 「가칭」 서술 문장을 고침 | id-map.tsv |
| references/catalog.tsv | S47~S50 | [고침] status를 needs-resolution으로 낮춤. 서지와 DOI를 2차 출처의 목록에서 가져왔고 DOI를 해석하지 않았다 | references/README.md 확인 수준 |
| related-work.md | §1 표, §7 | [고침] W2c가 확인한 내용(학술 의견 글의 절차 골격, GPT-1900 평가의 성격, TypewriterLM의 제목)을 반영 | 조사 기록 et-targets-research.md §5·§7 |
| docs/16 17 18 19 | 끝 | [고침] 초안 끝의 부록 세 개를 떼어 research 폴더로 옮기고 포인터 한 줄을 둠 | 작업 지시 W7 |
| docs/09 16 17 18 19 | H-DISCOVER, L0–L5 | [확인] H-DISCOVER 문장이 docs/16·17·18·19에 글자 그대로 있고 L0–L5가 docs/16·17에서 같다 | 마스터 결정 MD-1118-N |
| docs/09 17 19 | phase와 ET 단 대응, 단별 상한 | [확인] P0~P6의 ET 단 대응과 ET-3p 상한 1·ET-3 상한 2·ET-4 상한 3이 같다. docs/17 §3.2가 기준 | docs/17 §3.1·§3.2 |
| docs/09 16 18 19 | feature 수, 경로·CRUD 판정 이름 | [확인] feature 32개(BF-D4 포함), fast·learn·deep·hold, read·update·branch·create·hold·evict가 같다 | docs/16 §2.1·§2.2·§3 |
| docs/09 15 16 17 18 19 | ID와 절 참조 | [확인] BF·FL·V0·P0-T·UJ·ET·PAPER·Ck-n·suite·NP·TG·D가 소유 문서에 정의돼 있고 문서 사이의 절 참조가 모두 실제 제목을 가리킨다 | 각 소유 문서 |
| docs/15 이외 | token·GPU-시간·비용 | [확인] 비용 수치는 docs/15에만 있다. docs/09 §10에는 11-17 수치와 그 갱신 주석만 있다(수치 복제 없음) | docs/15 |
| docs/09 18 | P5 범위와 rag arm | [OPEN] P5에 시간캡슐 기반 retrofit이 더해져 범위가 커졌다(P5를 둘로 나눌지는 P4 종료 재검토). docs/18의 NP 비교는 dense RAG arm이 필요한데 docs/09 §4는 RAG를 P5에서 처음 둔다. P1 arm 7개는 바꾸지 않았다 | docs/09 §5 P4 종료 gate, §11 |
| docs/16 18 | F25 | [OPEN] 같은 후보를 docs/16 §8.2와 docs/18 §5.5가 각자 서술한다. 번호는 합쳤으나 서술은 합치지 않았다 | docs/16 §8.2 |
| docs/09 | D-21 hold 경로 | [OPEN] docs/16은 P1부터 포함(a), docs/18은 np0-nohold 결과를 본 뒤 결정하고 기본은 미포함(b)을 제안했다. 행에 양쪽을 적었다 | docs/09 §10 D-21 |
| docs/19 | PAPER-0의 범위 | [OPEN] 주장 14개가 한 편에 넓다. 계획은 한 편으로 쓰고 분리는 D-42 | docs/19 §3 |

개정한 기존 문서는 기존 줄을 한 줄도 지우거나 고치지 않았다. docs/09는 머리 상자 개정 주석, §1.2·§1.3·§1.4·§3·§4 보충, P0(NP)·P6(ET) 절, P1–P5 조정 주석, §6·§7·§8·§9 보충, §10의 새 결정 표와 비용 갱신 주석, 점진적 해상도 자체 점검표, §11 변경 기록 행을 더했다. docs/15는 머리 갱신 안내, §0·§1·§3 보충, §4.7(오늘 상품 목록), §5.4, §6.7(P0), §6.8(시간캡슐 기반 확보 3안), §6.9, §6.10, §6.11(PAPER-k 묶음표), §7 끝, §10-1(결정 후보와 요약 표), OPEN-18~24, §12 변경 기록 행을 더했다. 각 개정 담당의 변경 요약과 부록은 doc09-appendices.md, doc15-appendices.md에 있다.

## 6. 사용자 결정 대기

비용이 드는 선택은 결정 전에 실행하지 않는다. 이번 작업으로 해소된 결정은 없다. 아래 새 결정은 전부 OPEN이고 추천은 PROPOSAL이다. 번호와 내용의 기준은 [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md) §10이다.

### 6.1 이번 작업에서 새로 생긴 결정 D-15~D-47 (33개)

| ID | 결정(요약) | 비용 발생 | 결정자 |
|---|---|---|---|
| D-15 | phase 구성과 「P1은 MVP」 해석(§1.4 보충 주석) | 없음 | 사용자 |
| D-16 | P0의 NP 단 범위: NP-2(닫힌 꼴 선형 expert, 파라미터가 있다)를 「비모수」 대역에 포함할지 | 구현 공수 | 사용자 |
| D-17 | §3 등급 2의 「실제 갱신」을 P0에서 「실제 비모수 state 쓰기」로 읽을지(§3 보충 주석) | 없음 | 사용자 |
| D-18 | P0 종료 gate에 sealed readout(등급 3 시도)을 포함할지(D-07의 P0판) | runcrate 대량 readout(승인 시. 15-compute-plan.md) | 사용자 |
| D-19 | P0의 frozen LLM 주 모델·복제 모델·backend와 가중치 확보 | HF 가중치(8B bf16 약 16GB)와 시간캡슐 모델 다운로드, runcrate(D-04, N-… | 사용자 |
| D-20 | P1 base 크기를 135M급으로 둘지 P0·시간캡슐 모델급(1.7B–4B급)으로 올릴지(D-01의 선택지 (a)–(d)에 상향 안을 더하는 질문) | 상향 시 P1 학습 비용 증가(15-compute-plan.md) | 사용자 |
| D-21 | hold 경로를 P1 controller v0에도 넣을지(D-14와 연결) | (a)는 P1 공수 소폭(임계값 하나와 trace 필드) | 사용자 |
| D-22 | NP 대조군의 충실도와 NP-0의 생성·판정 분리 | 공식 구현 사용과 별도 판정 모델은 구현·계산 비용 | 사용자(NP-0 분리는 설계 담당 제안, 사용자 확인) |
| D-23 | 구현 위치와 Melete 파일 이관 방식 | 이관 공수 | 사용자 |
| D-24 | 이상 청사진의 feature 목록에 BF-D4(응답 형성과 불확실성 표현)를 더한 것의 수용과 기존 문서(docs/05·07·13·14) 용어의 개정 범위 | (b)는 문서 공수 | 사용자(승인), 설계 담당(세부) |
| D-25 | CRUD 판정에서 branch와 create를 나눠 쓸지(14-schema-lifecycle-crud-and-joint-paper.md §3의 「새 expert 할당 또는… | 없음 | 사용자 |
| D-26 | 발견 feature 묶음과 가설 H-DISCOVER를 헌장에 올릴지(N-8의 U13 질문과 한 번에 묶을 수 있다) | 없음 | 사용자 |
| D-27 | 발견 feature(긴장 원장·재조합·후보 원리·통찰 사건·보고)의 학습 모듈을 어느 phase에 둘지 | P3·P4 공수와 계산(15-compute-plan.md) | 사용자 |
| D-28 | ET 대상 묶음(주력·pilot·대안과 묶음의 대상 수), 주력의 기반 checkpoint와 T0, 원문 「1904」의 읽기 | 없음(후속 실행 비용은 docs/15) | 사용자 |
| D-29 | 시간캡슐 기반 모델의 확보 방식(P5–P6), 모델별 라이선스 확인, 공개 상태의 재점검 주기 | (a) 가중치 다운로드, (b)·(c) 사전학습과 corpus 전처리 비용(15-compute-pl… | 사용자 |
| D-30 | ET의 「입력」을 경험을 받는 학습자(L)로 읽을지 대화하는 동반 AI(C)로 읽을지(17-einstein-test.md §2.4) | 없음 | 사용자 |
| D-31 | ET 판정의 사전 명세 선택: 입력 tier의 주 판정 단위, 용량–반응의 판정 x축, 머리 결과 채널(dev pilot 뒤 확정) | 없음 | 사용자(dev pilot 뒤 확정) |
| D-32 | T0 이후 세계 지식(W_delta)의 투입 방식과 모의 인물(closed-loop) 도입 | 모의 인물을 도입하면 현대 LLM 호출 비용 | 사용자 |
| D-33 | ET 채점자 구성 | 사람 채점자의 시간과 보상 | 사용자 |
| D-34 | P6의 등급 상한과 「아인슈타인 테스트 통과」 문구, 판정의 최소 수준 | 4를 시도하면 기반과 사료 확보 비용이 늘어난다 | 사용자 |
| D-35 | ET 사료의 접근·공개 범위·저작권 | 사료 이용 허가·편집판 구독 비용이 있을 수 있다(규모 미확인) | 사용자 |
| D-36 | stream 구성에 현대 LLM과 번역을 쓰는 범위 | 호출 비용 | 사용자 |
| D-37 | 참고 영상의 정체 확인 | 없음 | 사용자 |
| D-38 | 논문 전략: 동반 논문 PAPER-0b(ET 절차·benchmark 논문)를 낼지, 논문 핵심 주장에 필요한 등급이 phase 상한보다 높을 때의 처리 | (a)는 해당 phase의 공수·계산 증가 | 사용자 |
| D-39 | 외부 발견 benchmark 앵커: NP arm을 공개 benchmark(예: NewtonBench·LLM-SRBench) 한 곳에서 한 번 돌려 ET-0의 외부 타당도… | 계산 소량(이 run은 15-compute-plan.md의 실행 행렬에 아직 없다) | 사용자 |
| D-40 | 투고 준비 정책: (i) 제출 4주 전에 가장 가까운 선행 연구를 다시 조회하는 gate(2026-06 이후 preprint는 심사 전이다) (ii) PAPER-0b의 투… | 없음 | 사용자 |
| D-41 | 외부 공개의 시점: 사전 등록(manifest hash)과 preprint | 없음 | 사용자 |
| D-42 | 논문 단위 정책: phase마다 1편으로 고정할지, PAPER-0의 범위(주장이 넓다) | 없음 | 사용자 |
| D-43 | 핵심 주장이 FAIL일 때 negative-result판 논문을 낼지 | 작성 시간 | 사용자 |
| D-44 | 논문 공개물의 범위 | 없음 | 사용자 |
| D-45 | 논문 제목에 「Einstein」을 쓸지와 「통과」 문구 정책(D-34와 함께 본다) | 없음 | 사용자 |
| D-46 | P0 대량 readout의 서빙 방식과 보조 run의 모델 크기(D-19의 모델 선택과 함께 본다) | 있음(금액은 15-compute-plan.md §6.7) | 사용자 |
| D-47 | 자체 사전학습용 다중 GPU 노드와 월 약정(D-29에서 소형·중형 자체 사전학습을 고를 때만 해당) | (b)에서 있음(15-compute-plan.md §6.8) | 사용자 |

### 6.2 기존 번호에 합쳐진 후보

| 후보의 내용 | 합친 번호 | 이유 |
|---|---|---|
| Ali 공동논문과 PAPER-3·4의 관계, 제안문 수정안 승인, 발송 여부 | N-6 | 같은 결정이다. 이 작업은 발송하지 않았다 |
| 실험 B(Base와 post-training)를 P5와 PAPER-5에 둘지 | N-5 | 실험 B의 채택 질문에 포함된다 |
| P0의 클라우드 비용 상한과 FCL 전용 키·예산 | N-11(과 D-04) | credential gating 5항목 결정과 같다 |
| 외부 consumer 접점을 P0부터 얇게 둘지 | D-11 | 연결 대상·방식·시점과 같은 질문이다 |
| 시간캡슐 기반 확보 안, P1 base 크기, P0 대조군의 구현 출처, PAPER-0b와 등급 불일치 | D-29, D-20, D-22, D-38 | 같은 결정이다 |

### 6.3 사용자 확인이 필요한 해석

사용자가 말하지 않은 것을 결정처럼 쓰지 않았다. 아래는 문서가 기본 선택을 적고 사용자 확인으로 올린 해석이다.

| 해석 | 기본 선택(PROPOSAL) | 번호 |
|---|---|---|
| 원문의 순서(POC 먼저, 그 뒤 단계별 구현)와 「P1은 MVP」의 관계 | P0(NP)가 뼈대와 전체 여정을 먼저 세우고 P1이 첫 학습 해상도 | D-15 |
| 「non parameter」의 범위 | gradient 학습이 없는 NP-0·NP-1만 「비모수」 주장에 넣고 NP-2(파라미터가 있음)는 선택 | D-16 |
| docs/09 §3 등급 2의 「실제 갱신」 | P0에서는 「실제 비모수 state 쓰기」 | D-17 |
| 「아인슈타인이라면 했을 법한 입력」의 뜻 | 인물의 경험 stream을 받는 학습자(L)가 기본, 대화하는 동반 AI(C)는 변형 | D-30 |
| 원문의 「1901~1904」·「1904년 발견」과 역사의 1905 | 사용자 원문을 고치지 않고 구성요소별 발견 시점으로 T1을 정의. 「1904」는 오기(Y1)인지 입력 구간의 끝(Y2)인지 | D-28 |
| 대상 인물·발견·T0 | 추천 묶음은 PROPOSAL이며 사용자가 고른 것이 아니다 | D-28 |
| 「증면」 | 「증명」으로 읽었다. 원문은 고치지 않았다 | [2026-11-18-discussion.md](/home/jimmy/repos/full-continual-learning/sources/sync/2026-11-18-discussion.md) |

이 밖에 2026-11-17 검토의 기존 결정(D-01, D-04, D-05, D-09, D-12, D-14, N-1~N-11)과 2026-11-12 감사 §5의 사용자 확인 #1~#19는 이번 요청으로 바뀌지 않았고 대기 중이다.

## 7. 통합하지 못한 것

| 항목 | 이유와 다음 행동 |
|---|---|
| mermaid의 실제 parser 검사 | 정적 점검(첫 줄과 라벨 규칙)만 했다. 마스터가 브라우저에서 mermaid.parse로 검사한다 |
| 원본 `tools/validate_docs.py` 검사 | 문서가 main checkout의 절대 경로로 링크해 worktree에서는 wrapper로만 돌렸다. 병합 뒤 main checkout에서 마스터가 돌린다 |
| docs/08에 F25~F31 등록 | docs/08은 고치지 않았다. 등록은 사용자 결정(N-5) |
| F25의 서술 병합 | 번호는 합쳤으나 docs/16 §8.2와 docs/18 §5.5의 서술은 각자 둔다(OPEN) |
| docs/09 P1–P5 종료 gate의 판정 대상 주장 번호 | P6만 C6-1~C6-4로 맞췄다. P1–P5의 gate는 기존 본문이 가리키는 그대로이고 보충 행도 「위 행 그대로」로 썼다 |
| docs/15의 계산 스크립트 보관 | 스크립트는 저장소에 넣지 않았고 공개 TSV 15개는 이 폴더에 두었다. 스크립트를 둘지는 docs/15의 OPEN-24(=OPEN-16)다 |
| 문서 분량 | 새 문서가 가이드(400–700줄)보다 길다. 각 담당이 줄일 후보 절을 제안했으나 줄이지 않았다(내용 손실 방지) |
| 시간캡슐 모델의 실제 확인 | 내려받기·실행·hook·과제 수행 능력은 NOT RUN이다. Ranke-4B 가중치 공개, TypewriterLM 라이선스, 참고 영상 내용은 미확인이다 |
| Einstein 1905 rubric의 일부 | 「W 선행」 목록과 날짜, 같은 시기 비발견자 사료의 개별 확인은 미확인이다. 그 밖 대상의 rubric은 형식만 있다(작업 지시의 범위) |
| 백서 갱신 | 하지 않았다. 백서는 2026-11-12 기준 그대로다 |


## 8. 이 작업으로 성립하지 않는 것 (NOT RUN)

- 구현, 모델 학습(gradient 학습 포함), GPU 실행, 클라우드 인스턴스 생성·종료, 비용 지출, runcrate API 호출, 유료 API, 큰 모델·corpus 다운로드는 0회다. 키 파일은 열지 않았다. 백서 재생성·배포, 외부 발송(Ali 제안문 포함), push·fetch·rebase·병합도 하지 않았다.
- 문서의 모든 계산 수치(token, GPU-시간, 비용, 규모)는 ESTIMATE이고 측정이 아니다. 모든 실험은 NOT RUN이다. 초록의 결과 칸은 자리표시자이며 실행한 결과가 아니다.
- 판정 규칙은 형식과 확정 시점만 정했다. 임계값, seed 수, 최소 효과는 정하지 않았다(dev pilot의 분산으로 봉인 전에 정하고 사용자가 승인한다. D-05).
- 문헌 조사는 공개 웹 페이지(공식 논문 페이지, 저자·기관 게시물, 보도)에서 제목·저자·날짜·초록·일부 본문을 읽은 수준이다. 전문 정독(fulltext-read)은 없고 코드 실행·재현도 없다. 확인 수준은 항목별로 적었다(§3).
- 시간캡슐 모델은 내려받거나 실행하지 않았다. 기반 모델의 수학·물리 능력, instruction 판 유무, 변환 가능성은 공개 문서에서 읽은 범위이며 실측이 아니다.
- 사용자 결정은 하나도 대신하지 않았다. 마스터 결정(MD-1118-A~P)과 문서의 추천은 PROPOSAL이다. 「설계해」·「써서 준비해둬」는 비용 승인이 아니다.
- 백서는 갱신하지 않았으므로 2026-11-12 기준 그대로다.

## 9. 검증 결과

| 검사 | 결과 |
|---|---|
| 문서 검사(저장소 검사기와 같은 검사, worktree wrapper) | errors 0 (파일 219, markdown 69, 로컬 링크 1,118, 참고문헌 296) |
| JSON | sources/sync/manifest.json 파싱 성공. 기존 항목 12개와 최상위 칸은 그대로이고 항목 1개를 끝에 더함 |
| catalog와 TSV | catalog.tsv 296행(기존 133 + 새 163), 8열, ID 유일, 기존 행 삭제 0, export_references.py 성공(임시 사본에서 실행했고 생성물은 커밋하지 않음). 이 폴더의 TSV 19개는 열 수가 일정 |
| 삭제·이름 변경과 기존 줄 보존 | 삭제·이름 변경 0. docs/09와 docs/15는 지워진 기존 줄 0(보충만 더함) |
| 공개 안전성 | 통합 담당용 검사(추가된 줄만, 커밋 전 index)와 마스터용 독립 검사(같은 내용의 임시 커밋)에서 hard hits 0. 로컬 경로·작업 폴더 이름·Melete 로컬 경로·이메일·IP·키·잔액·상품 id·카드 id·앱 이름 없음 |
| mermaid | 블록 10개(docs/16 7, docs/17 2, docs/18 1). 첫 줄과 라벨 규칙의 정적 점검에서 이상 없음. 실제 parser 검사는 병합 뒤 마스터가 한다 |
| 사용자 원문 | sources/sync/2026-11-18-discussion.md의 원문 블록이 원문 파일과 바이트 단위로 같다(2,080바이트) |
| 새 문서의 머리 | docs/16–19 모두 첫 단락이 상태 라벨이고 날짜 2026-11-18이 있다 |
| 내용 점검 | BF 32개, FL-1~FL-6, ET-0~ET-4와 ET-3p, V0-1~V0-17, suite S-A~S-D, UJ0·UJ6, PAPER-0·0b·1~6, D-15~D-47, 「PAPER-k 묶음표」가 있다. 문서에 남은 가칭 0 |
| 원격 main | 작업 시작과 끝에 조회한 원격 main은 d1b855f로 같다. main checkout의 작업 트리와 HEAD는 그대로다 |


## 10. 마스터 검증과 수정 (2026-11-18)

통합 커밋 뒤에 마스터가 문서를 직접 읽고 아래를 고쳤다. 내용(설계 판단, 수치, 결정 번호)은 바꾸지 않았고 표기만 고쳤다.

| 항목 | 고친 것 |
|---|---|
| 이름 충돌 | docs/17의 판정 조건 P1~P10을 PC-1~PC-10으로, 누설 변형 V0·V1·V2를 LV0·LV1·LV2로, ET-3p 계약 C-1~C-7을 EC-1~EC-7로, 대조 stream C0~C4를 CS0~CS4로 바꿨다. phase 이름(P0–P6), 검증 항목(V0-n), 논문 주장(Ck-n)과 구분하려는 것이다. docs/09·18·19와 부록의 인용도 함께 고쳤다 |
| 번호 치환 잔재 | docs/18 한눈에 보기의 결정 번호 범위, docs/18 §4의 새 family 번호, docs/15 변경 기록의 결정 번호, 조사(와·과, 이·가) 4곳 |
| 초안 문구 | docs/18 §10의 입력표 위치를 exec-matrix.tsv 링크로 바꿨다 |
| 수치 설명 | docs/18 §10.5에 host 종료 gate 시간의 점 값(14.3시간)과 계산 계획의 표본 P50(약 19.2시간)의 관계를 적었다. 두 값은 그대로다 |
| 인용 표기 | docs/19 한눈에 보기의 USER 인용을 원문과 글자 그대로 맞췄다. 요약 표현을 원문 인용처럼 낫표에 넣은 4곳을 풀어 썼다 |
| 그대로 둔 것 | 참고 영상의 공개 제목과 URL은 조사 출처로 남겼다. docs/18 §14.3과 docs/19 §13에서 한 결정 번호가 두 행에 나오는 곳은 그대로 두었다. 기준은 docs/09 §10이다 |

**병합 뒤 검사 (2026-11-18, main checkout).** `python3 tools/validate_docs.py` 결과는 errors 0이다(files 219, markdown 69, local links 1,120, reference records 296). `unresolved_reference_ids`는 10개다. 기존 3개(N29–N31)에 이번 작업의 needs-resolution 7개(S47–S50, N39, S156, S157)가 더해졌다. 오류가 아니라 URL이나 서지를 1차 출처로 확정하지 못했다는 표시다. mermaid 블록 10개는 mermaid parser로 parse를 확인했다(브라우저 렌더링은 확인하지 않았다). 추가된 줄의 공개 안전성 검사는 hits 0이다.
