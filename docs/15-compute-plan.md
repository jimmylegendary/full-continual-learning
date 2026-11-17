# 15. 계산 계획: runcrate 클라우드 GPU를 과하지도 모자라지도 않게 쓰는 방법

**상태 라벨:** 이 문서는 **PROPOSAL**과 **ESTIMATE**(계산 추정, **NOT RUN**)다. 사용자가 승인한 비용·사양·일정이 아니며, 어떤 인스턴스도 만들지 않았고 GPU·유료 API·가중치 다운로드도 쓰지 않았다. 사용자가 한 말(**USER**)은 §1에 날짜와 함께 따로 적었다. 과거 기록(**ARCHIVE**)은 이번에 재확인하지 않았다. 미해결은 **OPEN**이다. 작성: 2026-11-17.

**무엇인가.** [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md)의 P1–P5에 계산 자원을 붙이는 **횡단 문서**다. 별도의 "인프라 phase"를 만들지 않으며, 기존 phase의 데모 시나리오(UJ1–UJ5)·넓이/깊이 변화·성립하는 보장과 상한·종료 gate·미루는 것을 바꾸지 않는다. 어떤 자원을 쓰든 phase 종료 gate의 E2E는 실제 `fcl` CLI·실제 pretrained 가중치로 돌아야 하고(규칙), 이 문서는 그 일을 어디서 얼마에 돌릴지만 정한다.

**가격.** 모든 가격은 **2026-11-17 조회 시점이며 변동 가능하다.** 아래 표의 "시간당 가격"은 그날의 상품 목록 값이고 생성 시점에 마스터가 다시 확인한다.

**결정은 사용자 몫이다.** 비용은 사용자 결정 gate이며 §9(계정·예산)와 [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md) §10의 D-04가 그 자리다. 이 문서는 결정을 대신하지 않는다.

**2026-11-18 갱신.** 이 문서는 2026-11-17의 수치와 표를 그대로 두고, 2026-11-18의 새 로드맵(P0(NP)–P6(ET)과 논문 PAPER-0~6)에 맞춰 계산을 더했다. 더한 것은 「2026-11-18 갱신」 표기의 문장·표·절이다: 오늘 스냅샷(§4.7), P0·P6의 자원 배정(§5.4), P0의 frozen LLM serving과 실행 행렬 비용(§6.7), 시간캡슐 기반 확보 3안(§6.8), 시간캡슐 기반 retrofit과 ET run(§6.9), P1–P5의 ET 단·NP arm 추가분과 P1 base 비교(§6.10), **PAPER-k 묶음표**(§6.11), 결정 후보(§10-1). 모든 새 수치는 ESTIMATE이고 NOT RUN이다. phase 정의는 [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md), P0 실행 행렬은 [18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md), stream 규모와 ET 단은 [17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md)가 소유한다. 이 문서는 그 값을 입력으로 받아 token·GPU-시간·비용을 계산하고, [19-paper-plan.md](/home/jimmy/repos/full-continual-learning/docs/19-paper-plan.md)는 PAPER-k 묶음표로 이 문서를 가리킨다. 계산 자원은 여전히 별도의 인프라 phase가 아니라 phase에 붙는 횡단 자원이다.


## 0. 이번에 한 것과 하지 않은 것

| 구분 | 내용 |
|---|---|
| 읽음 | docs/05·06·07·08·09·10·13·14, 2026-11-12 설계 감사의 D-번호 근거 노트, runcrate 상품 스냅샷(2026-11-17, 별도 세션이 읽기 전용으로 조회한 결과. 인스턴스 0개), runcrate 공개 웹 문서(키 없이), 공식 모델 카드·`config.json`, NVIDIA 공식 제품 페이지·datasheet·whitepaper, Melete 기록 2건(ARCHIVE) |
| 계산함 | 작업량·메모리·시간·비용 추정(§6), tier별 유효 실험 비용(§4.5) |
| 하지 않음 | runcrate API 호출, 인스턴스 생성·종료, GPU 사용, 모델 가중치·대용량 다운로드, 유료 API, 패키지 설치. 이 문서의 모든 수치는 **NOT RUN**이다 |
| ARCHIVE(재확인 안 함) | 같은 날 다른 세션이 남긴 운영 사실: 경로에 인스턴스 이름을 넣으면 401이라 항상 id를 쓴다, '중지'는 terminate뿐이라 로컬 디스크가 지워진다, VM에서 Ubuntu 22.04·driver 570.148.08(CUDA 12.8)·Docker `--gpus`·HF 16GB 다운로드 17초를 실측했다 |


**2026-11-18 갱신: 이번에 한 것과 하지 않은 것.**

| 구분 | 내용 |
|---|---|
| 읽음 | P0 실행 행렬 16행(docs/18의 입력표)과 ET 단 stream 규모(docs/17의 입력표), runcrate 상품 스냅샷 2026-11-18(상품 목록과 인스턴스 건수만 읽음, 인스턴스 0개), 공개 모델 카드와 `config.json`(시간캡슐 모델 4종과 Qwen3-4B), 2026-11-17의 공개 입력표 |
| 계산함 | 2026-11-17 작업량 모델을 같은 가정 분포와 같은 표본(seed)으로 재현했고 공개 입력표 7개와 줄 단위로 일치했다. 오늘 가격으로 다시 계산했고, P0·시간캡슐·ET·PAPER-k 비용을 더했다 |
| 하지 않음 | runcrate API 호출, 인스턴스 생성·종료, GPU 사용, 모델 가중치와 corpus 다운로드, 유료 API. 이 문서의 새 수치는 모두 **NOT RUN**이다 |

## 1. 사용자 요구

**USER (2026-11-17):** 원문을 문장 경계에서 둘로 나눠 적는다.

- 「오늘 날짜 기준으로 다시 검토해봐. 그리고 full continual learning repo도 업데이트해서 반영.」
- 「그리고 지금 우리 host에 runcrate 사용환경 있을거야. melete를 앞으로 만들고 학습시 사용한다면 어떻게 쓸 수 있을지, 비용효율을 위해서 너무 과도한 사양이 아닌, 그렇다고 minimum으로 품질이나 효율을 떨어트리지 않으면서 쓴다면 어떻게 쓸 수 있을지 계획해봐」

**해석 (PROPOSAL):** 요구의 세 요소를 아래처럼 옮긴다.

| 사용자 말 | 이 문서의 운영 정의 |
|---|---|
| 과도한 사양이 아닌 | 연산이 아니라 메모리·운영 이유가 없는 H100급을 기본으로 쓰지 않는다 |
| minimum으로 품질·효율을 떨어트리지 않으면서 | 메모리 헤드룸 부족으로 인한 OOM 재실행, 사용자 환경에서 재현 못 하는 gate, seed·arm 축소로 인한 근거 약화는 "최소"의 비용으로 센다 |
| 비용효율 | 시간당 가격이 아니라 **유효한 실험 1건을 끝내는 총비용**(§2) |


**USER (2026-11-18):** 이번 갱신의 직접 근거는 아래 한 줄이다(원문은 [2026-11-18-discussion.md](/home/jimmy/repos/full-continual-learning/sources/sync/2026-11-18-discussion.md)).

- 「당연히 runcrate사용한 실험계획(필요한 단계에서)도 포함되어야함」

**해석 (PROPOSAL):** 새 phase P0(NP)–P6(ET)와 논문 PAPER-0~6에서 어느 일을 host에서 돌리고 어느 일을 runcrate에서 돌리는지, 그 비용을 이 문서의 같은 방법(§2의 유효 실험 1건의 총비용, §6의 P10 / P50 / P90)으로 계산한다. 계산 자원을 위한 새 phase는 만들지 않는다.

## 2. 판단 기준: 유효한 실험 1건을 끝내는 총비용

**PROPOSAL.** 시간당 가격은 판단 기준이 아니다. 기준은 **유효 실험 1건**(manifest 해시가 맞고 budget 일치 검사를 통과해 INVALID가 아닌 (arm × seed) 결과 하나)을 끝내는 데 든 총비용이다.

    유효 실험 1건의 총비용 = 시간당 가격
        x ( 인스턴스 준비 시간 / 한 인스턴스에서 묶어 돌린 run 수
            + 순수 실행 시간 x 실패·재시작·INVALID 재실행 배수 x (1 + 승인 대기·감시 공백 등 유휴 비율) )

- **준비 시간:** 환경 구성·이미지 pull·모델 다운로드·사전 점검. 부팅 자체는 과금되지 않는다(공개 문서, §7.6). 가정 0.2 / 0.35 / 0.6시간(낙관 / 중앙 / 비관).
- **실패·재시작 배수:** 1.2 / 1.3 / 1.5(ESTIMATE, 이 계획의 가정: 낙관 1.2·중앙 1.3·비관 1.5).
- **유휴:** 5 / 10 / 25%. 사람의 승인 대기와 감시 공백도 과금되는 시간이다.
- **상각:** seed 묶음을 한 인스턴스에서 순차로 돌리면 준비 비용이 나뉜다. 135M run 1건(순수 실행 약 6분)은 인스턴스당 1건이면 약 $0.6, 5건 묶음이면 약 $0.3이다(§4.5).

## 3. 한눈에 보기

**ESTIMATE / NOT RUN.** 요약 6줄과 표 하나다. 근거는 이어지는 절에 있다.

1. **연산 비용은 작다.** 135M을 P1 기반으로 고르면 P1 전체의 클라우드 비용은 P50 약 $17(P10–P90 $10–35)이고 같은 일을 노트북에서 하면 무료다. 비용이 커지는 곳은 P2(depth 격자·family 3종·seed)·P4(Sleep teacher)·P5(1–2B 모델)다.
2. **GPU 종류별 비용/FLOP은 거의 평평하다.** 소형 모델에서 추정한 유효 TFLOP-hour 단가가 GPU 종류에 따라 약 14.5–28.8 m$(중앙값 약 22 대비 −35%~+28%)로 평평하다(§4.3). 그래서 tier는 시간당 가격이 아니라 **메모리 헤드룸·vCPU/RAM·VM(이미지 고정 가능)·벽시계**로 고른다.
3. **주력은 48GB급 1장 VM**(RTX 6000 Ada 또는 L40S, 시간당 $1.23–1.39, 12 vCPU, 72–80GB RAM)이다. P1–P4 학습과 대량 readout의 기본이다.
4. **대형 tier**(A100 80GB·H100)는 세 경우에만 쓴다. (i) 학습 메모리가 48GB를 넘는 일(1.7B 전체 student 갱신 약 61GB), (ii) main tier에서 한 run이 세션 상한(6–24시간)을 넘는 연산 지배 대형 run(P5: 1.7B·1B token은 48GB급 약 30시간 대 H100 약 10시간, 비용은 비슷), (iii) 8B teacher·참고선 추론.
5. **평가(readout)는 GPU가 아니라 지연시간과 vCPU가 지배한다.** batch=1 session 평가는 CPU가 kernel을 구동하므로 GPU를 키워도 빨라지지 않고, 병렬 평가 process 수(vCPU·RAM)가 처리량을 정한다. test-time write가 요청 단위 순차 갱신이라 batch를 키우기 어렵다는 가설이 맞으면 더 그렇다(§6.5).
6. **D-04는 개정을 제안한다**(§10, OPEN). "클라우드는 P5 전까지 보류"는 근거가 약하다. 노트북 환산(노트북 사양은 AI TOPS에서 유도한 가정)으로 P2 학습만 P50 약 82시간(연속 약 3.4일, P90 약 400시간)이라 P2부터 클라우드가 실질적으로 필요하다. 그래서 (i) T04의 소액 microbenchmark를 지금 승인 요청하고 (ii) 학습·readout용 클라우드는 T04로 보정한 phase별 상한으로 따로 승인받자고 제안한다. 결정은 사용자다.

**phase별 권장 자원과 비용 범위 (SmolLM2-135M을 P1–P4 기반으로 고르는 경우의 P50, 괄호는 P10–P90).**

| phase | E2E·회귀 gate(사용자 환경) | 학습·대량 readout | 클라우드 과금 시간 h | 클라우드 비용 |
|---|---|---|---|---|
| P1 | host CPU(+노트북) | 노트북 우선, 부족하면 main 1장. T04 microbenchmark는 승인 시 2종 | 11.5 (6.5–25.4) | $17 ($10–$35) |
| P2 | host CPU | main 1장 | 63.2 (21.7–208) | $78 ($27–$255) |
| P3 | host CPU | main 1장 | 22.5 (8.7–66.2) | $28 ($11–$81) |
| P4 | host CPU | main 1장. 전체 student 1.7B·8B teacher는 large | 40.0 (11.5–127) | $54 ($15–$188) |
| P5 | host CPU + 노트북 | 두 번째·큰 모델 학습은 large, readout·서빙은 main | 69.7 (25.6–160) | $130 ($44–$395) |
| P1–P4 합계 | | | 152 (65.5–394) | $198 ($86–$516) |
| P1–P5 합계 | | | 241 (118–510) | $374 ($178–$810) |

P5에 1.7B를 두 번째 모델로 쓰면 P5는 $141–2,537(P50 $548), 360M이면 $66–791(P50 $205)이다(표 §6.4). 노트북·host 시간은 비용에 넣지 않았다. 위 합계는 "그 모델을 골랐을 때의 가상 경로"이며 선택된 계획이 아니다.


**2026-11-18 갱신: 한눈에 보기.** ESTIMATE / NOT RUN. 위 11-17 요약 6줄과 표는 그날 기준으로 그대로 두고, 아래가 새 로드맵에서 더해진 것이다. 근거는 §4.7과 §6.7~§6.11에 있다.

1. **오늘 스냅샷은 목록이 바뀌었고 가격은 거의 그대로다.** 상품 192개 → 177개(추가 31, 삭제 46, 공통 146 중 가격이 바뀐 것은 1개). 주력(48GB급 1장 VM, 시간당 $1.23)과 A100 80GB 1장 VM($1.73)은 그대로이고 H100 1장 VM의 하한만 $3.91 → $4.72로 올랐다. 어제 표를 오늘 가격으로 다시 계산해도 phase 합계(P50)의 변화는 −0.0% ~ +0.3%다(§4.7).
2. **P0는 학습이 없는데도 클라우드 비용이 P1–P4보다 크다.** frozen 8B급 LLM의 호출이 약 3.03M건, 입력 약 1.98B token, 출력 약 178M token이라서다. runcrate 비용은 P50 $864(P10–P90 $395–$2,059), 서빙 방식과 모델 크기가 레버다(서버형 $389, 4B급 $468, 둘 다 $210, §6.7). UJ0 종료 gate는 host에서 도는 것이 원칙이고 벽시계로 P50 약 19.2시간(P10–P90 11.8–31.5)이다.
3. **시간캡슐 기반은 공개 모델을 쓰는 안이 가장 싸다.** 확보 3안의 P50은 공개 모델 사용 약 $7, 소형 자체 사전학습 약 $3천, 중형 자체 사전학습 약 $4만이며 중형은 한 노드로 약 2.5개월이 걸린다(§6.8).
4. **시간캡슐 기반 retrofit(P5 식)은 기반 크기에 따라 P50 $0.8천–$3.5천이다.** ET run 자체(ET-3, ET-4)는 P50 $28–$224로 작다(§6.9).
5. **P1 base를 1.7B로 올리면 P1이 P50 약 $22 늘고 4B면 약 $56 늘지만 4B는 48GB에 안 들어간다**(§6.10). 기본은 135M 유지다.

**PAPER-k 묶음표 요약 (P10 / P50 / P90).** 상세와 가정은 §6.11이다.

| 논문 | phase | 비용 USD | 과금 시간 h |
|---|---|---|---|
| PAPER-0 | P0(NP) | $395 / $864 / $2,059 | 321 / 703 / 1,674 |
| PAPER-0b | P0 직후(선택) | $10 / $33 / $124 | 8.1 / 27.0 / 101 |
| PAPER-1 | P1 | $21 / $38 / $78 | 14.4 / 27.9 / 61.5 |
| PAPER-2 | P2 | $45 / $106 / $288 | 36.5 / 86.1 / 234 |
| PAPER-3 | P3 | $13 / $30 / $84 | 10.7 / 24.5 / 68.3 |
| PAPER-4 | P4 | $18 / $57 / $191 | 13.6 / 42.1 / 128 |
| PAPER-5 | P5 | $787 / $2,593 / $10,583 | 401 / 1,145 / 3,692 |
| PAPER-6 | P6(ET) | $230 / $1,010 / $3,661 | 100 / 444 / 1,515 |

## 4. 자원 tier 4종과 고른 상품

### 4.1 tier 개요

| tier | 자원 | 비용 | 쓰는 일 | 못 하는 일 |
|---|---|---|---|---|
| 1 | host CPU(16코어, RAM 27GB, GPU 없음, 메모리 압박이 잦음) | 무료 | 계약·자동 테스트, 세계 생성, 소규모 평가, **phase E2E·회귀 gate**(사용자 재현), 체크포인트 검증 | 학습(135M run 1건이 CPU 유효 0.2–0.5 TFLOPS 가정에서 약 10–25시간, ESTIMATE), 대량 readout 직렬 |
| 2 | 노트북 GPU(RTX 5070 Ti Laptop 12GB, SSH, 간헐적 연결, ARCHIVE) | 무료 | 개발, 짧은 spike, **P1 135M 학습의 1차 후보**(ESTIMATE: 약 20 run에 P50 약 7.7시간, P10–P90 1.7–37시간) | 360M 이상은 step당 token을 줄여야 하고 0.6B 이상은 메모리·시간상 비현실, 연결 단절 |
| 3 | runcrate 주력: 48GB급 1장 VM | 시간당 $0.8–1.4 | P1–P4의 학습·readout, microbenchmark | 학습 메모리가 48GB를 넘는 일 |
| 4 | runcrate 대형: A100 80GB·H100(·H200) | 시간당 $1.7–5.3 | 48GB를 넘는 학습, 한 run이 12시간을 넘는 연산 지배 대형 run, 8B teacher·참고선 | 소형 모델 평가의 속도 향상(지연 지배) |

### 4.2 고른 상품 (가격 2026-11-17 조회 시점, 변동 가능)

공개 열만 적는다. 같은 tier의 상품은 생성 시점에 가용한 순서로 시도한다(순위 = 표의 순서).

| 구분 | tier | GPU x 개수 | region (location) | 형태 | port_mapped | vCPU | RAM GB | 디스크 GB | USD/h |
|---|---|---|---|---|---|---|---|---|---|
| 선택 | 3 | RTX 6000 Ada x1 | us/midwest (US Midwest) | vm | false | 12 | 72 | 350 | 1.23 |
| 대안 | 3 | L40S x1 | kansascity-usa-1 (Kansas City, KS) | vm | false | 12 | 72 | 625 | 1.26 |
| 대안 | 3 | L40S x1 | desmoines-usa-1 (Des Moines, IA) | vm | false | 12 | 72 | 625 | 1.26 |
| 대안 | 3 | RTX 6000 Ada x1 | kansascity-usa-1 / desmoines-usa-1 | vm | false | 12 | 80 | 350 | 1.39 |
| 예산 대안 | 3 | RTX A6000 x1 | desmoines-usa-1 / wichita-usa-1 | vm | false | 12 | 64 | 256 | 0.82 |
| vCPU 대안 | 3 | RTX 5090 x1 | pl/1 (Gdańsk, Poland) | vm | false | 48 | 88 | 200 | 1.83 |
| 선택 | 4 | A100 80GB x1 | kansascity-usa-1 (Kansas City, KS) | vm | false | 16 | 160 | 1000 | 1.73 |
| 대안 | 4 | A100 80GB x1 | beltsville-usa-1 (Beltsville, MD) | vm | false | 16 | 160 | 1000 | 1.73 |
| 선택(연산 지배 run) | 4 | H100 x1 | us/aus/1 (Austin, TX) | container | true | 19 | 207 | 164 | 3.14 |
| 대안(비교 등급) | 4 | H100 x1 | desmoines-usa-1 (Des Moines, IA) | vm | false | 20 | 128 | 1250 | 3.91 |
| 대안(80GB 초과) | 4 | H200 NVL x1 | gb/bhx · de/fra/2 | vm | false | 15 | 267 | 1000 | 4.67 |

**왜 이것들인가 (PROPOSAL).**

- **48GB 1장 VM이 주력인 이유.** 학습 메모리는 step당 16,384 token 기준 P50–P90으로 135M 약 9–13GB, 360M 약 13–20GB, 0.6B 약 16–28GB, 1.7B 약 29–47GB다(§6.6). 24GB 카드는 0.6B의 P2·P4와 1.7B에서 부족하거나 활성 재계산(+약 33% 시간)이 필요하고, 병렬 평가 process 6–10개(각 약 2.5GB)도 여유가 작다. 48GB는 이 모든 일을 재계산 없이 담으면서 유효 TFLOP-hour 단가가 대형 GPU와 비슷하다. 이보다 큰 80GB·H100은 연산 지배 대형 run이나 80GB가 필요한 일에서만 이득이다.
- **VM을 고른 이유.** 비교 등급 run은 고정 이미지(digest)와 uv lock으로 부팅해야 하고 VM에서 Docker `--gpus`가 동작한다(ARCHIVE, 재확인 안 함). container는 이미지를 우리가 고정할 수 있는지 공개 문서에 없다(OPEN-3).
- **미국 중서부(Des Moines·Kansas City·US Midwest)를 고른 이유.** 같은 GPU 종류에서 가장 싸다(§4.4). 뉴욕은 제외한다.
- **H100 container를 '연산 지배 run'에만 쓰는 이유.** 유효 FLOP당 최저가 후보지만(1.7B·1B token run $46 대 VM $57) container·port_mapped라 이미지 digest를 고정할 수 없고 디스크가 약 160–175GB다. 비교 등급(H-COMPUTE) run은 VM을 쓰거나, container라면 한 비교의 모든 run을 같은 상품에서 돌리고 driver·torch 버전을 원장에 기록한다(§7.4).
- **CPU 전용 인스턴스(대안, OPEN).** 스냅샷에는 CPU 상품 40개가 있다(예: 28 vCPU·RAM 80GB·디스크 1.6TB가 시간당 $0.63, 8 vCPU·RAM 32GB가 $0.18). 135M급 batch=1 평가는 지연·CPU 지배라 후보가 될 수 있으나 CPU 추론이 GPU eager보다 느릴 가능성이 커서(미측정) T04 microbenchmark의 선택 항목으로만 둔다. 같은 비교 안에서는 CPU와 GPU 실행을 섞지 않는다(§7.4).

### 4.3 GPU 사양과 USD/TFLOP-hour

출처는 NVIDIA 공식 문서다. BF16은 Tensor Core **dense**(희소성 미적용)이며 FP32 누적 기준이다. m$ = milli-dollar. "유효"는 §6.5의 roofline 추정(SmolLM2-135M, 중앙 가정)이며 **실측 전에는 결론이 아니다**.

| GPU | 최저가 listing | USD/h | BF16 dense TFLOPS | BW GB/s | VRAM | m$ / peak TFLOP-h | 유효 TFLOPS(추정) | m$ / 유효 TFLOP-h(추정) |
|---|---|---|---|---|---|---|---|---|
| RTX 6000 Ada | us/midwest vm | 1.23 | 364.2 | 960 | 48GB | 3.38 | 55 | 22.4 |
| L40S | kansascity vm | 1.26 | 362.05 | 864 | 48GB | 3.48 | 51 | 24.7 |
| RTX A6000 | us/las container | 0.57 | 154.8 | 768 | 48GB | 3.68 | 34 | 16.8 |
| RTX 4090 | de/fra/3 container | 0.58 | 165.2 | 1008 | 24GB | 3.51 | 40 | 14.5 |
| RTX 3090 | de/fra/3 container | 0.41 | 71.2 | 936 | 24GB | 5.76 | 23 | 17.8 |
| RTX 5090 | us/aus/1 container | 1.15 | 209.5 | 1792 | 32GB | 5.49 | 59 | 19.5 |
| RTX PRO 6000 | us/sea/1 container | 2.28 | 503.8 | 1792 | 96GB | 4.53 | 92 | 24.8 |
| A100 80GB | kansascity vm | 1.73 | 312 | 1935 | 80GB | 5.54 | 77 | 22.5 |
| A100 40GB | calgary vm | 1.99 | 312 | 1555 | 40GB | 6.38 | 69 | 28.8 |
| H100 | us/aus/1 container | 3.14 | 989.5 | 3350 | 80GB | 3.17 | 174 | 18.1 |
| H200 | us/blt/1 container | 5.22 | 989.5 | 4800 | 141GB | 5.28 | 215 | 24.3 |
| B200 | sydney vm | 10.00 | 2250 | 8000 | 180GB | 4.44 | 409 | 24.5 |

**사양 출처.** (S1) [NVIDIA RTX Blackwell GPU Architecture 백서](https://images.nvidia.com/aem-dam/Solutions/geforce/blackwell/nvidia-rtx-blackwell-gpu-architecture.pdf) Table 3: RTX 5090 BF16(FP32 누적) 209.5 dense, 32GB GDDR7, 1792 GB/s; RTX 4090 165.2, 24GB, 1008; RTX 3090 71.2, 24GB, 936. (S2) [NVIDIA RTX PRO Blackwell GPU Architecture 백서](https://www.nvidia.com/content/dam/en-zz/Solutions/design-visualization/quadro-product-literature/NVIDIA-RTX-Blackwell-PRO-GPU-Architecture-v1.0.pdf) Table 4: RTX A6000 154.8 / 768 GB/s / 48GB; RTX 6000 Ada 364 / 960 / 48GB; RTX PRO 6000 Blackwell Workstation Edition 503.8, 96GB GDDR7, 1792 GB/s(Max-Q 438.9). (S3) [NVIDIA Ada GPU Architecture(proviz) 백서](https://images.nvidia.com/aem-dam/en-zz/Solutions/technologies/NVIDIA-ADA-GPU-PROVIZ-Architecture-Whitepaper_1.1.pdf) Table 2: RTX 6000 Ada FP16/BF16 Tensor(FP32 누적) 364.2 dense. (S4) [NVIDIA L40S 제품 페이지](https://www.nvidia.com/en-us/data-center/l40s/): BF16 362.05 / 733(sparsity), 48GB GDDR6, 864 GB/s. (S5) [NVIDIA A100 datasheet](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/a100/pdf/nvidia-a100-datasheet-nvidia-us-2188504-web.pdf): BF16 312 / 624(sparsity), 80GB, 1,935(PCIe)·2,039(SXM) GB/s. (S6) NVIDIA [H100](https://www.nvidia.com/en-us/data-center/h100/)·[H200](https://www.nvidia.com/en-us/data-center/h200/) 제품 페이지: BF16 1,979(SXM)·1,671(NVL) **with sparsity**이므로 dense는 그 절반(989.5·835.5)으로 유도했다. H100 3.35 TB/s, H200 141GB·4.8 TB/s. (S7) NVIDIA [HGX](https://www.nvidia.com/en-us/data-center/hgx/)·[DGX B200](https://www.nvidia.com/en-us/data-center/dgx-b200/) 페이지: FP16/BF16 36 PFLOPS(8 GPU, sparsity)·메모리 1,440GB·64 TB/s는 8 GPU 합계라 GPU당 2.25 PFLOPS·180GB·8 TB/s는 **유도치**다.

**확인하지 못한 것 (OPEN-9).** A100 40GB의 대역폭 1,555 GB/s는 40GB 사양서 값이며 이번에 조회하지 않았다. 상품이 어느 변종(H100 SXM/NVL/PCIe, RTX PRO 6000 Workstation/Max-Q/Server)인지는 상품 정보에 없다. L40는 제품 페이지에 BF16 수치가 없고, A10·A40·A4000·A5000·L4·V100·GH200·Gaudi2는 공식 수치를 읽지 못해 비교에서 뺐다. 노트북 GPU(RTX 5070 Ti Laptop: 12GB GDDR7, 192-bit, AI TOPS 992, [NVIDIA 노트북 비교 페이지](https://www.nvidia.com/en-us/geforce/laptops/compare/))의 BF16 약 62 TFLOPS와 대역폭 약 672 GB/s는 AI TOPS와 버스 폭에서 **유도한 가정**이다.

### 4.4 피할 상품 (스냅샷 수치로 직접 검증)

받은 가설 4개를 스냅샷으로 검증했다. 스냅샷은 192개 상품(GPU 152·CPU 40; vm 164·container 28; host_tier 전부 datacenter; container는 전부 port_mapped)이다.

| 가설 | 스냅샷 수치 | 판정 |
|---|---|---|
| A100 40GB $2.85가 A100 80GB $1.73보다 비싸다 | A100(40GB) 1장 listing 6개 1.99–4.57 USD/h(중앙 2.85), A100 80GB 15개 1.73–4.70(중앙 2.32). 최저가끼리 1.99 대 1.73, 다수 listing 2.85 대 1.73 | **검증됨.** 같은 BF16 312 TFLOPS에 메모리는 절반인데 비싸다. 40GB를 고를 이유가 없다 |
| 뉴욕에 프리미엄이 있다 | 같은 GPU의 비-뉴욕 최저 대 뉴욕: A100 1.99 대 4.57(x2.3), A100 80GB 1.73 대 4.70(x2.7), H100 3.14 대 8.57(x2.7), A6000 0.57 대 2.76(x4.8), A4000 0.22 대 1.15(x5.2), V100 0.36 대 3.35(x9.3). 비교 가능한 7종 모두 뉴욕이 비싸다(x2.3–9.3) | **검증됨.** 뉴욕은 후보에서 제외한다 |
| container는 RAM/vCPU가 적다 | RTX 4090 container vCPU 10–11·RAM 10–20GB, RTX 5090 container 7·15–30GB, RTX 3090 container 8–31·16–31GB, A6000 container 5·23–94GB. 같은 GPU의 VM은 RTX 5090 48·88GB, RTX 4090 12·70GB. 그러나 H100 container는 19·207GB로 VM(16–30·120–268GB)과 같거나 많고 H200 container는 15–47·176–251GB | **부분 검증.** GeForce·A6000 container는 RAM이 병렬 평가 process 수를 막을 만큼 적다. H100·H200 container는 아니다. GPU 종류별로 본다 |
| multi-GPU 노드는 소형 모델에 이득이 없다 | GPU당 단가: A100 80GB 1장 1.73 대 다장 1.73, RTX 6000 Ada 1.23 대 1.39, H100 3.14 대 3.91, L40S 1.26 대 2.15, A6000 0.57 대 0.82. 다장 할인이 없다 | **부분 검증.** 가격 이득은 없다. 소형 모델은 1장에 들어가 DDP 이득이 없고, 벽시계가 필요하면 독립 run을 GPU별로 병렬로 돌리면 된다. 노드의 RAM·vCPU가 큰 것은 GPU 때문이 아니라 CPU·RAM 때문이다 |

**그 밖에 피하는 것 (이유 포함).**

| 상품 | 이유 |
|---|---|
| RTX 4090 / RTX 5090 container(RAM 10–30GB, vCPU 7–11) | 병렬 평가 process(각 약 2–3GB RAM)와 HF 적재에 부족하다. 이미지 digest를 고정할 수 없을 수 있다(OPEN-3). 단 24GB·$0.58로 135M 단발 run의 비용은 가장 싸다($0.16, 5건 묶음). 48GB급($0.27) 대비 절감액이 run당 약 $0.1로 작아 이 계획은 쓰지 않는다 |
| A100 40GB(1.99–4.57) | A100 80GB가 더 싸다 |
| 뉴욕(newyork-usa-1)의 모든 상품 | 같은 GPU 대비 x2.3–9.3 |
| 다장 노드(2·4·8장) | GPU당 단가 동일, 소형 모델에 이득 없음 |
| B200 1장 $10(시드니, listing 1개) | 소형 모델은 활용률이 낮아 이득이 없고 단일 listing이라 가용성 위험 |
| GH200(Dulles) | 상품 정보에 CPU 아키텍처가 없다. Grace(Arm)이면 wheel·이미지 호환 위험(OPEN) |
| V100(BF16 하드웨어 미지원) | bf16 retrofit 학습의 비교 환경으로 부적합하다 |

### 4.5 유효 실험 1건의 총비용: GPU 종류별 비교 (ESTIMATE, 중앙 가정)

§2의 식으로 계산했다. "run 1건/인스턴스"는 준비 비용을 한 run이 다 지는 경우이고 "5건/인스턴스"는 seed 묶음으로 나눈 경우다. 학습 메모리가 카드 용량의 90%를 넘으면 활성 재계산(+33% 시간)을 넣고, 그래도 안 맞으면 뺐다. 값은 GPU별 최저가 listing(뉴욕 제외)의 시간당 가격 기준이다.

**P1 T09 run 1건 (135M, 40M token, retrofit 2층)**

| GPU | 형태 | USD/h | vCPU / RAM | run 1건/인스턴스 | 5건/인스턴스 | run 시간 h | 추정 MFU |
|---|---|---|---|---|---|---|---|
| RTX 6000 Ada | vm | 1.23 | 12 / 72GB | $0.61 | $0.27 | 0.10 | 0.15 |
| L40S | vm | 1.26 | 12 / 72GB | $0.64 | $0.29 | 0.11 | 0.14 |
| RTX A6000 | vm | 0.75 | 6 / 48GB | $0.44 | $0.23 | 0.17 | 0.22 |
| RTX 4090 | vm | 0.86 | 12 / 70GB | $0.47 | $0.23 | 0.14 | 0.24 |
| RTX 5090 | container | 1.15 | 7 / 30GB | $0.56 | $0.24 | 0.10 | 0.28 |
| A100 80GB | vm | 1.73 | 16 / 160GB | $0.79 | $0.30 | 0.07 | 0.25 |
| H100 | container | 3.14 | 19 / 207GB | $1.24 | $0.36 | 0.03 | 0.18 |
| H100 | vm | 3.91 | 20 / 128GB | $1.55 | $0.45 | 0.03 | 0.18 |
| H200 | container | 5.22 | 15 / 176GB | $2.02 | $0.56 | 0.03 | 0.22 |

**P2 depth 격자 run 1건 (360M, 200M token, retrofit 4층; 평균 r 배수 미반영)**

| GPU | 형태 | USD/h | run 1건/인스턴스 | 5건/인스턴스 | run 시간 h |
|---|---|---|---|---|---|
| RTX 6000 Ada | vm | 1.23 | $2.54 | $2.20 | 1.20 |
| L40S | vm | 1.26 | $2.75 | $2.39 | 1.28 |
| RTX A6000 | vm | 0.75 | $2.50 | $2.29 | 2.09 |
| RTX 4090 | vm | 0.86 | $2.52 | $2.28 | 1.81 |
| A100 80GB | vm | 1.73 | $2.96 | $2.47 | 0.95 |
| H100 | container | 3.14 | $2.84 | $1.96 | 0.39 |
| H100 | vm | 3.91 | $3.54 | $2.44 | 0.39 |

**P5 run 1건 (1.7B, 1B token, retrofit 14층)**

| GPU | 형태 | USD/h | 5건/인스턴스 | run 시간 h | 학습 메모리 GB |
|---|---|---|---|---|---|
| RTX 6000 Ada | vm | 1.23 | $53 | 30.21 | 34.5 |
| L40S | vm | 1.26 | $57 | 31.55 | 34.5 |
| RTX A6000 | vm | 0.75 | $63 | 58.95 | 34.5 |
| A100 80GB | vm | 1.73 | $69 | 27.88 | 34.5 |
| H100 | container | 3.14 | $46 | 10.22 | 34.5 |
| H100 | vm | 3.91 | $57 | 10.22 | 34.5 |
| H200 | container | 5.22 | $70 | 9.27 | 34.5 |
| RTX 5090 | vm | 1.83 | $137 | 52.25 | 20.3(재계산) |

**읽는 법.** (1) P1·P2 규모에서는 GPU 종류에 따른 비용 차이가 $0.3–2 수준이라 **tier 선택이 총비용을 좌우하지 않는다.** 좌우하는 것은 준비 시간의 상각(run 1건 $0.61에서 5건 $0.27로 절반 이하)이다. (2) P5 규모에서는 48GB급 VM($53)과 H100 VM($57)의 비용이 같고 벽시계만 3배 차이(30시간 대 10시간)다. 그래서 대형 tier의 이유는 비용이 아니라 **세션 상한·대기 시간**이다. (3) 32GB RTX 5090은 1.7B에서 활성 재계산이 필요해 1.6–2.6배 비싸다(container $86, VM $137 대 48GB급 $53). 소형(135M)에서는 5090이 48GB급과 같다. 5090 VM($1.83)은 vCPU 48·RAM 88GB가 장점이라 병렬 평가 process가 많을 때만 의미가 있다. (4) 이 표는 추정이다. MFU 가정이 틀리면 순위가 바뀔 수 있다(§6.5, §8).

### 4.6 runcrate 공개 문서에서 확인한 운영 사실

키 없이 공개 웹 문서만 열람했다(2026-11-17). **CONFIRMED**는 원문에 있는 것, **OPEN**은 확인하지 못한 것이다. 문서는 바뀔 수 있다.

| 항목 | 확인 결과 | 출처 |
|---|---|---|
| 과금 단위 | 대부분 초 단위, 일부 GPU는 분 단위 올림(삭제 뒤 teardown 약 30초 포함). **부팅은 과금되지 않는다.** 일부 상품은 최소 과금이 있다(스냅샷에서는 L4 1개가 60분). 인계 전에 실패한 launch는 과금되지 않는다. CONFIRMED | [pricing](https://www.runcrate.ai/pricing), [instances overview](https://www.runcrate.ai/docs/instances/overview.md) |
| 자동 종료 | CLI `--max-runtime`(5분–168시간)과 `--idle-stop`(5분–24시간, "GPU 5% 미만 + 접속자 없음"). 종료는 terminate이며 로컬 디스크가 삭제된다. 둘 다 생략하면 꺼져 있다. API 필드명은 OPEN-5. CONFIRMED(CLI) | [CLI instances](https://www.runcrate.ai/docs/cli/instances) |
| 영구 볼륨 | 10–10,000GB, 0.03 USD/GB-월, `/workspace` 마운트, terminate 뒤 유지, 한 번에 한 인스턴스에만 attach, 백업 아님. 스냅샷은 NOT STATED. vm 지원은 OPEN-4. CONFIRMED | [storage](https://www.runcrate.ai/storage), [storage overview](https://www.runcrate.ai/docs/storage/overview.md) |
| 이미지 | 템플릿(devbox·train·inference)으로 고르고 `launch_script` 옵션이 있다. 사용자 정의 이미지와 driver 선택은 NOT STATED(OPEN-3) | [compute](https://www.runcrate.ai/compute) |
| vm 대 container | 공개 문서는 container로 서술하고 상품은 vm/container를 구분한다(OPEN-1) | [instances overview](https://www.runcrate.ai/docs/instances/overview.md) |
| spot | 개념만 서술(회수 알림 2–60분). 이 계획은 쓰지 않는다(OPEN-6) | 같은 곳 |
| 데이터 전송 | NOT STATED(OPEN-7) | 열람한 모든 페이지 |
| 시작 시간 | launch→running 중앙값 4분 14초, 90%는 6분 50초 이내(449회) | [compute](https://www.runcrate.ai/compute) |
| 월 약정 | 1–12개월 선불, 최대 15% 할인, 취소 불가(스냅샷 1/3/6/12개월 5/8/11/15%) | [pricing](https://www.runcrate.ai/pricing) |
| 잔액 | 1달러 미만이면 자동 충전 시도 후 메일, 실행 중 인스턴스는 15분 뒤(또는 −10달러에 닿으면 더 일찍) 삭제될 수 있다 | [pricing](https://www.runcrate.ai/pricing) |


### 4.7 2026-11-18 스냅샷 갱신: 목록은 바뀌었고 가격은 거의 그대로다

**ESTIMATE / NOT RUN.** 스냅샷 2026-11-18의 상품 목록과 인스턴스 건수만 읽었다(잔액은 읽지 않았다). 상품은 날마다 바뀌므로 이 문서는 상품을 고정하지 않고 **선정 기준**을 적는다. 생성 시점에 이 기준을 적용해 그때 가용한 상품을 고른다. 위 §4.2의 표는 11-17 그날의 기록이고 이 문서는 상품 id를 쓰지 않는다(고른 상품의 id는 비공개 운영 메모에만 둔다).

| 항목 | 11-17 | 11-18 |
|---|---|---|
| 상품 수 | 192 | 177(GPU 139, CPU 38. vm 157, container 20) |
| 인스턴스 | 0 | 0 |
| 이동 | - | 추가 31, 삭제 46, 공통 146(가격이 바뀐 것 1) |

**선정 기준과 충족 후보 수.** 기준은 11-17의 선정 규칙(VM 우선, 뉴욕 제외, vCPU·RAM·디스크 하한)과 같다.

| 기준 | 11-17 후보 수 | 11-18 후보 수 | 11-17 하한 USD/h | 11-18 하한 USD/h |
|---|---|---|---|---|
| 48GB급 RTX 6000 Ada 1장 VM, vCPU 12 이상, RAM 64GB 이상, 디스크 250GB 이상, 뉴욕 제외 | 4 | 3 | $1.23 | $1.23 |
| 48GB급 L40S 1장 VM, 같은 조건 | 4 | 0 | $1.26 | 없음 |
| 48GB급 RTX A6000 1장 VM(예산 대안), 같은 조건 | 6 | 6 | $0.82 | $0.82 |
| A100 80GB 1장 VM, vCPU 16 이상, RAM 128GB 이상 | 2 | 1 | $1.73 | $1.73 |
| H100 1장(형태 무관) | 14 | 8 | $3.14 | $3.15 |
| H100 1장 VM | 6 | 4 | $3.91 | $4.72 |
| H100 4장 이상 노드(자체 사전학습용) | 0 | 2 | 없음 | $23.4 |
| A100 80GB 8장 VM(자체 사전학습 대안) | 4 | 5 | $13.84 | $13.84 |
| H200 1장(형태 무관) | 10 | 11 | $4.67 | $4.28 |
| CPU 인스턴스, vCPU 16 이상, RAM 64GB 이상 | 16 | 16 | $0.63 | $0.68 |

**시간당 최저가 요약.**

| 항목 | 11-17 | 11-18 | 비고 |
|---|---|---|---|
| main(48GB급 VM) 최저가 | $1.23 | $1.23 | RTX6000Ada |
| A100 80GB VM 최저가 | $1.73 | $1.73 |  |
| H100 1장 최저가(형태 무관) | $3.14 | $3.15 | container |
| H100 1장 VM 최저가 | $3.91 | $4.72 |  |
| H100 4장 이상 노드 GPU당 최저 |  | $5.85 |  |
| CPU 인스턴스(16 vCPU 이상, RAM 64GB 이상) 최저가 |  | $0.68 | 16 vCPU |

**오늘 기준을 적용한 결과(공개 열만, 같은 tier의 상품은 생성 시점에 가용한 순서로 시도한다).**

| tier | 역할 | GPU x 개수 | 위치 | 형태 | vCPU | RAM GB | 디스크 GB | USD/h |
|---|---|---|---|---|---|---|---|---|
| 3 주력(48GB급 1장 VM) | 기준 충족 후보 1 | RTX6000Ada x1 | US Midwest | vm | 12 | 72 | 350 | $1.23 |
| 3 주력(48GB급 1장 VM) | 기준 충족 후보 2 | RTX6000Ada x1 | US Midwest | vm | 12 | 72 | 350 | $1.23 |
| 3 예산 대안 | RTX A6000 VM | A6000 x1 | Des Moines, IA, United States | vm | 12 | 64 | 256 | $0.82 |
| 3 vCPU 대안 | RTX 5090 VM | RTX5090 x1 | Gdańsk, Poland | vm | 48 | 88 | 200 | $1.83 |
| 4 대형 | A100 80GB VM | A100_80G x1 | Beltsville, MD, United States | vm | 16 | 160 | 1000 | $1.73 |
| 4 대형 | H100 최저가(형태 무관) | H100 x1 | Austin, TX, United States | container | 19 | 207 | 151 | $3.15 |
| 4 대형 | H100 VM | H100 x1 | Paris, France | vm | 24 | 240 | 1000 | $4.72 |

**어제 표와 달라진 것.**

| 상품군 | 11-17 | 11-18 | 의미 |
|---|---|---|---|
| L40S 1장 VM | 4개, 하한 $1.26 | 0개 | 주력 후보 한 종류가 사라졌다. RTX 6000 Ada 1장 VM(6 → 5개, 하한 $1.23)이 남아 주력은 유지된다 |
| H100 1장 VM | 6개, 하한 $3.91 | 4개, 하한 $4.72 | 11-17의 하한 상품(Des Moines, $3.91)이 사라지고 오늘 하한은 Paris, France의 $4.72다. 비교 등급 VM run의 가격이 약 21% 오른다 |
| H100 1장 container | 8개, 하한 $3.14 | 4개, 하한 $3.15 | 유일한 가격 변경(+$0.01). 상품 수는 절반 |
| H100 2장 VM · 4장 VM | 2개 · 0개 | 0개 · 2개 | 4장 VM의 GPU당 가격은 $5.85다 |
| H200 container | 7개, 하한 $5.22 | 9개, 하한 $4.28 | 하한이 내려갔다 |
| A100 80GB 8장 VM | 4개, $13.84 | 5개, $13.84 | 자체 사전학습의 대안 노드(GPU당 $1.73) |
| B200 · GH200 | B200 VM 1개, GH200 VM 1개 | B200 container 1개($8.73), GH200 0개 | 참고만. 이 계획은 쓰지 않는다 |

**어제 표를 오늘 가격으로 다시 계산하면(같은 가정·같은 표본, 가격만 교체, P50).** 어제 표의 모든 phase에서 변화가 −0.0% ~ +0.3%다. 이 문서의 11-17 표는 그대로 두었고 변경은 필요 없다. 전체 표는 조사 기록 부록의 TSV(price-update)에 있다.

| phase | base | 11-17 가격 P50 | 11-18 가격 P50 | 변화 |
|---|---|---|---|---|
| P1 | Qwen3-1.7B | $39.8 | $39.9 | +0.1% |
| P1 | SmolLM2-135M | $17.5 | $17.5 | +0.1% |
| P2 | Qwen3-1.7B | $304.8 | $304.8 | +0.0% |
| P2 | SmolLM2-135M | $77.7 | $77.7 | +0.0% |
| P3 | Qwen3-1.7B | $92.2 | $92.2 | +0.0% |
| P3 | SmolLM2-135M | $27.6 | $27.6 | +0.0% |
| P4 | Qwen3-1.7B | $158.6 | $159.0 | +0.3% |
| P4 | SmolLM2-135M | $53.8 | $53.8 | +0.0% |
| P5 | Qwen3-1.7B | $548.2 | $549.8 | +0.3% |
| P5 | SmolLM2-135M | $130.1 | $130.2 | +0.0% |

선택 지렛대는 쓰지 않는다: 스냅샷의 상품 대부분(123 / 177)에 1개월 약정 5% 할인 항목이 있다. 약정은 승인과 환불 조건이 필요한 비용 결정이라 이 계획에 넣지 않았다(OPEN-17과 같은 항목).

## 5. phase별 자원 배정

### 5.1 원칙: gate는 사용자 환경에서, 학습과 대량 readout은 싼 곳에서

**PROPOSAL.** 두 가지를 구분한다.

1. **E2E·회귀 gate**([09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md) §5·§6의 UJ1–UJ5): 사용자가 자기 환경에서 재현할 수 있어야 한다. 그래서 **host CPU(+노트북)** 에서 돈다. 클라우드에서 만든 작은 체크포인트(수십 MB~수 GB)를 host로 가져와 실제 `fcl` CLI·실제 pretrained 가중치·실제 runtime 프로세스 재시작으로 돌린다. 클라우드 GPU에서만 도는 gate는 사용자가 재현할 수 없으므로 gate로 인정하지 않는다.
2. **학습·대량 readout**: 연산·시간이 많이 드는 일은 가장 싼 적합한 tier에서 돌린다.

**장치가 다르면 숫자가 다르다.** GPU에서 학습한 체크포인트를 CPU에서 재현하면 수치가 조금 달라진다(§7.4의 Melete J1 사례: CPU와 CUDA의 확률 차이가 1e-6 수준이었고 판단 범주는 모두 같았지만 원래의 수치 guard는 충족하지 못했다). 그래서 "재시작 전후 응답이 허용오차 안에서 같다"(P1-T10) 같은 Contract gate의 허용오차는 **장치 종류별로 선언**하고, 같은 장치에서 재시작 전후를 비교한다. OPEN-12.

### 5.2 배정표: 작으면 생기는 손해, 크면 낭비인 이유

SmolLM2-135M 기준 P50이며 비용은 클라우드 과금만이다. 근거 숫자는 §6.

| phase | 작업 | 배정 | 이보다 작으면 (품질·효율 손해) | 이보다 크면 (낭비인 이유) | 규모(P50) |
|---|---|---|---|---|---|
| P1 | T07 뼈대 E2E·T16 UJ1 E2E·회귀 gate(7 arm) | host CPU | 이미 최소(무료). 더 줄이면 단위 테스트뿐이라 규칙(실제 가중치·CLI 경로) 위반 | 클라우드 전용 gate는 사용자가 재현 불가 | host 시간 미측정(T04에서 측정) |
| P1 | T04 spike | host·노트북 실측 → 승인 시 클라우드 2종 microbenchmark | 클라우드 실측이 없으면 유효 처리율(±2배)·지연 가정이 P2 비용 범위($27–$255)에 그대로 남는다 | 3종 이상 GPU 비교는 비용/FLOP이 평평하다는 가설이 맞으면 정보 가치가 작다 | 2 인스턴스 약 3.7 h, $7.6 ($5.2–$11) |
| P1 | T09 retrofit 학습(약 20 run: 4 arm x 5 seed) + deep r=2 적응 | 노트북 우선, 부족하면 main 1장 | host CPU는 run 1건 약 10–25시간(추정)이라 20 run 불가. 노트북은 P50 약 7.7시간(P10–P90 1.7–36.8)으로 가능하나 연결 단절·시간 상한·360M(P50 약 19.1시간) 이상이 비현실. 줄이려고 seed·arm을 깎으면 sealed readout이 INCONCLUSIVE가 되기 쉽다 | H100은 run이 수 분에서 더 짧아질 뿐이고 준비 약 $1.1(0.35시간 x $3.14)이 run 비용(약 $0.3)을 넘는다 | main: 3.9 h, $4.9 |
| P1 | T12 dev eval·T15 sealed readout(약 8만 요청) | main 1장(병렬 process 6–10개) | host 직렬은 요청당 약 1초(CPU forward 약 0.08초 가정, 미측정)로 약 23시간이며 host 메모리 압박 속에서 한 대를 점유한다 | 평가는 지연·CPU 지배라 GPU를 키워도 빨라지지 않는다. vCPU가 많은 상품이 이득이다 | 약 2.2 h, $2.7 |
| P2 | UJ1·UJ2 회귀·E2E(depth 격자 소수 world) | host CPU | (이미 최소) | 위와 같음 | |
| P2 | 묶음 A spike + 묶음 D depth 격자 학습(약 25 run) | main 1장 | 노트북은 같은 학습이 P50 약 81.7시간(연속 약 3.4일, P90 약 396시간)이라 시간 상한을 넘고 12GB·단절 위험. seed·arm을 줄이면 등급 3 확증의 검정력이 약해진다 | A100·H100은 135M·360M에서 비용이 ±15% 안이고 벽시계만 줄인다. 대기가 비용보다 비쌀 때만 | 36.9 h, $45 |
| P2 | UJ2 배치 평가 + Qwen3-8B 참고선 | main 1장 | host llama.cpp 8B는 CPU로 시간~일 단위·host 점유 | 참고선은 약 0.6 h·$0.7라 더 키울 이유가 없다 | 13.8 h, $17 + $0.7 |
| P3 | teacher rollout·controller 공동 미세조정·UJ3 판정 | main 1장 | 노트북은 단절 위험, 시행착오형 신호의 시도 수가 비용(docs/06 §6) | 비용이 GPU 크기보다 **배치 평가 구현**과 시도 횟수에 좌우된다 | 18.2 h, $22 |
| P4 | Sleep v0 student 갱신(≤0.6B) | main 1장 | 48GB 미만이면 0.6B 전체 student 갱신(27GB)이 안 맞아 부분 갱신으로 바뀌고 'slow 가중치가 바뀐다'는 시험이 약해진다 | ≤0.6B에 H100은 비용이 같고 준비만 늘린다 | 15.8 h, $23 (135M) |
| P4 | Sleep(1.7B 전체 갱신 61GB)·8B teacher | large 1장(A100/H100) | 48GB에서는 불가. LoRA로 바꾸면 질문이 달라진다 | H200(141GB)은 필요 없다 | 1.7B: $124 ($24–$594) |
| P4 | UJ4 SE 대 SES readout·F12 | main 1장 | | 같음 | 15.0 h, $18 |
| P5 | 두 번째·더 큰 모델 학습(1.7B·약 1B token·retrofit 14층, 약 9 run) | large 1장 H100 | 48GB에서는 비용이 같으나 run당 약 30시간이라 세션 상한(6–24시간)을 넘어 재개가 필요하고 9 run이 직렬이면 약 11일 | H200은 80GB에 들어가는 일에서 비용이 +50% | 156 h, $491 ($91–$2,473) |
| P5 | 등급 4 readout·UJ5 서빙 soak·UJ1–UJ5 회귀 | main 1장 / 노트북 / host | 서빙 soak는 consumer가 host의 agent라 GPU 끝점 접근 경로(SSH 터널 등)가 필요하다. host CPU는 운용 지연 측정으로 부적합 | 서빙 지연을 H100으로 재면 사용자 환경(노트북·host)의 대표가 아니다 | 2.5 h, $3.1 + soak 27.6 h, $34 |

### 5.3 실험 A–E·결정적 실험의 자리

[13-schema-decomposition-and-interference.md](/home/jimmy/repos/full-continual-learning/docs/13-schema-decomposition-and-interference.md) §10의 실험 A–E와 [14-schema-lifecycle-crud-and-joint-paper.md](/home/jimmy/repos/full-continual-learning/docs/14-schema-lifecycle-crud-and-joint-paper.md) §8의 결정적 실험은 별도 phase가 아니라 기존 phase의 작업이다. 자원 규모를 가늠하는 참고다(NOT RUN).

| 실험 | 들어갈 phase | 규모 가늠 (ESTIMATE) |
|---|---|---|
| A 중첩·간섭 인과 분리(6 비교군) | P2 | arm 6종 x seed. P1 T09의 약 1.5배, main 1장 |
| B base와 post-training 분기(SFT·RL) | P5 이후 | RL은 시도 횟수가 비용이라 P3 teacher rollout 규모(수백만 rollout)가 최소다. 이 문서는 견적하지 않는다(OPEN) |
| C 용량과 지속학습 | P2–P4 | 모델 복제·adapter 대조는 같은 저장 예산이므로 학습 run 수가 arm 수에 비례 |
| D artifact 재사용·기능 보존 | P4 | 평가 위주라 계산은 작고 재색인·offload 비용이 지배 |
| E System ONE 계산 효율 | P2·P4 | §6의 P2 depth 격자·P4 SE 대 SES readout 자체다 |
| 14 §8 CU / D / R / Joint | P2–P4 | 정책 비교의 arm 수에 비례, 같은 저장 예산 대조 포함 |


### 5.4 2026-11-18 갱신: P0와 P6, 시간캡슐 기반의 자원 배정

**PROPOSAL.** §5.1의 원칙(gate는 사용자 환경에서, 학습과 대량 readout은 싼 곳에서)과 §7.4(한 비교의 run은 같은 장치·상품)를 그대로 둔다. 새로 생긴 것은 아래다.

| phase | E2E·회귀 gate(사용자 환경) | 학습·대량 readout | 이유와 한계 |
|---|---|---|---|
| P0(NP) | host CPU. UJ0 종료 gate(실행 행렬 R01–R04)가 host에서 재현돼야 한다. 벽시계 P50 약 19.2시간이며 이 처리량은 가정이다(P0-T04에서 측정). 노트북은 135M급 NP-1 성립 확인(R13, P50 약 0.53시간) | runcrate 48GB급 1장 VM. frozen 8B급 HF bf16 서빙(R05–R12, R14–R16) | 학습이 없어 메모리 부담은 작다(8B bf16 약 16.4GB). 비용은 학습이 아니라 호출 수와 서빙 처리량이 정한다. 한 비교 안의 arm은 같은 장치에서 돈다 |
| P6(ET) | host CPU. 소형 시간캡슐 기반(GPT-1900급, 1.7B–3.3B)으로 절차 전체를 재현하는 규모를 gate로 한다. 봉인 최종 판정 run은 gate가 아니다 | runcrate 48GB급 1장 VM. 시간캡슐 7B–13B급 retrofit과 ET-4 run | Talkie 13B는 bf16 약 26GB라 host RAM에 맞지 않는다. 4-bit급 변환본은 충실도가 검증되지 않았다 |
| 시간캡슐 기반 확보 | 해당 없음 | 안 1(공개 모델 사용)은 48GB급 1장. 안 2·3(자체 사전학습)은 4장 이상 노드(오늘 H100 4장 VM 또는 A100 80GB 8장 VM) | 중형 자체 사전학습은 한 노드로 약 2.5–4개월이다. 다중 노드 지원은 미확인(OPEN) |
| P1–P5의 NP arm·ET 단 | host CPU(회귀) | runcrate 48GB급 1장 VM(P1–P4는 135M 기반이라 작고, P5부터 시간캡슐 기반) | NP arm은 그 phase의 base로 다시 돈다(MD-O). 135M급에서 NP-0이 성립하지 않으면 그 사실을 보고하고 NP-1을 쓴다 |

## 6. 작업량 추정 (ESTIMATE / NOT RUN)

### 6.1 공식과 가정

모든 가정은 (낙관, 중앙, 비관) 세 값이며 정수 가정은 반올림한다. **낙관 = 그 가정의 10% 분위, 중앙 = 중앙값, 비관 = 90% 분위(나쁜 쪽 기준)** 로 읽는다. 비관값을 전부 곱하면 비현실적으로 넓어지므로 **각 가정을 이 분위 함수(구간별 보간, 배율형 가정은 로그 척도)로 독립 표본 3,000회를 뽑아 항목·phase 합계의 P10/P50/P90을 범위로 쓴다**(seed 고정, 가정끼리 독립으로 가정). 모든 가정을 중앙값으로 둔 결정론 값도 따로 계산했는데, 불확실한 배율이 여럿 곱해지면 중앙값이 올라가므로 표본 P50이 이 값보다 약 1.2–1.5배 크다.

| 항목 | 공식·가정 |
|---|---|
| 전체 학습 | FLOPs ≈ 6·N·T(P4 student 전체 갱신에 쓴다) |
| frozen base 위 retrofit | 전방 2·N_eff·T + 입력 gradient backward 2·N_eff·T·bwd + 새 모듈 6·N_new·T·omega. N_eff = 본체 + f_logit x lm head. **가정:** 기반은 얼어 있어 weight gradient가 없다. bwd = 0.5 / 1.0 / 1.5(retrofit이 상단이면 통과 층이 적어 작고, 활성 재계산을 넣으면 크다). omega = 1.5 / 2 / 3(새 모듈의 inner-loop write와 그것을 통과하는 outer gradient). f_logit = 0.1 / 0.2 / 0.5(답 token 위주 손실) |
| 새 모듈 크기 | N_new = n_retro x c x d². c = 6 / 8 / 12(NMM의 qkv·out·기억 MLP + CMS 분기). n_retro = P1 2층(docs/09: 1–2개), P2 4–8층, P5 L/4–전 층 |
| 추론 | 2·N_eff·T(+write 5%). 평가 **시간**은 FLOPs가 아니라 batch=1 지연(요청 수 x 평균 지연 / 병렬 process)이 지배한다 |
| test-time write 오버헤드 | **FLOPs 면에서 작다**(기억 MLP의 read 2p + update 6p가 NMM 층에만 걸려 전체 모델의 약 5%). **시간 면에서 크다**: chunk를 순차로 갱신하므로 retrofit layer 1개의 학습 시간을 일반 layer의 kappa = 1.5 / 3 / 6배로 가정한다(가설). 관측 1건의 write 추가 지연 10 / 20 / 40 ms(가설) |
| r=2 deep 경로 | retrofit 블록 n_blk/L를 한 번 더 적용: n_blk = 2 / 2 / 6층, L = 28–32이라 forward +6–21%. P1에서는 짧은 적응 학습(주 학습 token의 10 / 15 / 25%)만 더한다 |
| P2 depth | 배수 = 1 + (r̄-1)·(n_core/L). r̄ = 1.75 / 2 / 2.5, n_core = 4 / 6 / 8층 |
| MFU(소형 모델) | roofline식: MFU = e_gemm / (1 + t_elem/t_gemm) x sw. t_gemm = GEMM FLOPs/(peak x e_gemm), t_elem = non-GEMM HBM 왕복 bytes/대역폭. e_gemm = 0.70 / 0.55 / 0.40, sw = 1.0 / 0.85 / 0.65(eager·optimizer·데이터·로깅). §6.5 |
| 평가 지연 | forward 1회 8 / 20 / 40 ms(batch=1, HF eager는 CPU가 kernel을 구동), 답 decode 3 / 4 / 6 token, 병렬 평가 process 10 / 6 / 3개(12 vCPU) |
| 실패·재시작 배수 | 1.2 / 1.3 / 1.5 |
| 준비 시간 | 인스턴스당 0.2 / 0.35 / 0.6 시간(부팅은 과금 안 됨). 표는 각 작업 항목을 별도 인스턴스로 세므로 같은 phase의 항목을 한 인스턴스에 묶으면 실제 비용은 이보다 작다(보수적) |
| 세션 상한 | 인스턴스 1회 24 / 12 / 6시간(길수록 준비를 상각, 짧을수록 사고 손실이 작다) |

### 6.2 base 후보와 사양

공식 모델 카드·`config.json`만 확인했다(2026-11-17, 가중치 다운로드 없음). 파라미터 수는 config에서 식으로 계산했다(SmolLM2-135M은 docs/09 §10의 134,515,008과 일치).

| 후보 | 구조(config) | 파라미터 | 라이선스·언어 | retrofit 적합성 (docs/05 §6의 Titan-Llama pin 기준) |
|---|---|---|---|---|
| SmolLM2-135M | `LlamaForCausalLM`, 30층, hidden 576, FFN 1536, GQA 9/3, vocab 49,152, tied | 134.5M | Apache-2.0, 영어 중심, 2T token | 적합 1순위: Llama 블록, P1 영어 세계에 맞음, host CPU 실행 이력(ARCHIVE) |
| SmolLM2-360M | `LlamaForCausalLM`, 32층, hidden 960, FFN 2560, GQA 15/5, vocab 49,152 | 361.8M | 같은 계열 | 적합. 세계가 floor에 걸릴 때(D-01 (b)) |
| Qwen3-0.6B | `Qwen3ForCausalLM`, 28층, hidden 1024, FFN 3072, GQA 16/8, head_dim 128, vocab 151,936, QK-norm | 596M(비임베딩 0.44B) | Apache-2.0, 119개 언어(한국어 명시 없음), 36T token. base 카드 `Qwen3-0.6B-Base` 확인 | Llama 블록이 아니다(QK-norm). pin과 호환은 P1-T05 확인 필요. 한국어(D-09)와 묶인 후보 |
| Qwen3-1.7B(1B급 대표) | `Qwen3ForCausalLM`, 28층, hidden 2048, FFN 6144, GQA 16/8, vocab 151,936 | 약 1.72B | Qwen3 계열(Apache-2.0, 0.6B-Base 카드 기준) | D-01 (d) 1B급의 대표. Llama-3.2-1B는 gated라 config를 읽지 않았다 |

출처(공식 모델 카드·`config.json`, 2026-11-17 확인): [SmolLM2-135M](https://huggingface.co/HuggingFaceTB/SmolLM2-135M), [SmolLM2-360M](https://huggingface.co/HuggingFaceTB/SmolLM2-360M), [Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B), [Qwen3-0.6B-Base](https://huggingface.co/Qwen/Qwen3-0.6B-Base), [Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B). SmolLM2-135M 카드는 base와 Instruct를 명시 라벨로 구분하지 않고 Instruct가 별도 저장소라 base로 읽었다(추정). Qwen3-1.7B의 라이선스는 이번에 카드를 읽지 않아 같은 계열의 0.6B 카드 기준이다.

**2026-11-17 새 후보 점검 (OPEN).** 공식 모델 카드·config 기준이며 retrofit 호환은 P1-T05에서만 확인된다.

| 후보 | 확인한 것 | 판단 |
|---|---|---|
| Granite-4.0-350M-Base(IBM, 2025-10-28) | dense decoder-only transformer(HF 클래스는 `GraniteMoeHybridForCausalLM`, μP식 multiplier), 28층, hidden 1024, GQA 16/4, vocab 100,352, Apache-2.0, 약 15T token, 한국어 포함 12개 언어, 32K 문맥. 출처 [huggingface.co/ibm-granite/granite-4.0-350m-base](https://huggingface.co/ibm-granite/granite-4.0-350m-base) | P1 기본을 바꿀 이유는 없다(영어 합성 세계는 SmolLM2-135M으로 충분). **P5 두 번째 모델·한국어 도메인(D-09·D-12)의 유력 후보**다. Llama 클래스가 아니라 adapter 비용이 든다 |
| Qwen3.5-0.8B-Base(Qwen, 2026-02~03) | 하이브리드: Gated DeltaNet 3 : gated attention 1(6 x [3 x (GDN→FFN) → 1 x (GatedAttn→FFN)]), 24층, hidden 1024, vocab 248,320, 비전 인코더 포함, Apache-2.0, 201개 언어. 출처 [huggingface.co/Qwen/Qwen3.5-0.8B-Base](https://huggingface.co/Qwen/Qwen3.5-0.8B-Base) | **retrofit base로는 부적합**(Llama 블록·sequence layer 교체 전제와 다름). 이미 delta-rule 재귀 상태를 가진 모델이라 "비교 대상"으로만 의미가 있다. 별도 OPEN |
| Gemma 4(웹 검색 요약 기준 2026-04) | E2B(유효 2.3B)·E4B(유효 4.5B)·12B·26B A4B·31B가 있다고 검색 요약에 나온다. 공식 model card 주소는 다른 호스트로 리디렉션돼 직접 확인하지 못했다(2차 출처) | 0.3–1B급 변종을 확인하지 못했고 소형이 2B 이상이라 이번 범위 밖 |
| SmolLM3-3B | 3B(2025-07) | D-01 범위(≤1B급)보다 크다 |

판단: **소형(≤1B) 영어 P1에는 SmolLM2-135M을 바꿀 더 나은 후보를 찾지 못했다.** Granite-4.0-350M-Base는 P5의 한국어·두 번째 모델 후보로 D-12에 올린다(§10).

### 6.3 token 수 T의 도출

docs/09 §5 P1은 세계 규모를 수치로 주지 않으므로 근거 있는 범위로 둔다.

| 항목 | 값(낙관 / 중앙 / 비관) | 근거 |
|---|---|---|
| 관측 1건 token | 25 / 40 / 70 | 자연어로 렌더링한 짧은 사례 문장 가정. T06 renderer로 실측해 교체 |
| 질의+답 token | 30 / 50 / 80 | 같음 |
| 학습 episode의 관측 수 | k ∈ {1, 3, 10} 균등(평균 4.67), 평가는 k ∈ {0, 1, 3, 10}(평균 3.5) | docs/09 UJ1 ② |
| episode token | (관측 x 평균 k + 질의) x padding 1.1 / 1.15 / 1.3 → 중앙 약 274 | |
| P1 학습 episode 수/run | 32,768 / 131,072 / 524,288 | 중앙은 Melete J1의 2,048 step x batch 64 sample exposure다(ARCHIVE melete@1d95136:docs/implementation/records/2026-10-21-neural-judgment-j1-diagnostics.md §1·§6). 다른 모델 규모의 값이 아니라 **규모 감각의 기준**일 뿐이다 |
| P1 run token | 중앙 가정 약 36M, 표본 P50 약 39M | |
| seed | 3 / 5 / 10 | D-05 미정이라 범위. 학습하는 arm은 full·flat·always(+noctl) 3–4개, fixed·ctx·base는 학습하지 않음(docs/09 P1-T09). readout 요청 수는 5개 retrofit arm(fixed 포함) x seed + ctx·base 각 1회로 센다 |
| sealed readout world 수 | 64 / 128 / 384 | 95% 구간 ±5pp를 목표로 하면 독립 world 약 384(p=0.5). 질의/world 2 / 4 / 8 |
| P2 학습 token/run | 5천만 / 2억 / 8억 | recurrence 적응 학습. 원논문(Retrofitted Recurrence 등) 규모는 이번에 확인하지 않았고 docs/09 P5의 "원논문 규모 재현"은 미루는 것이다 |
| P4 replay token/run | 2천만 / 1억 / 4억 | 가정. teacher 크기: 자기 자신(0.35) / 4배 모델(0.45) / 8B급(0.20) 확률의 범주 표본. teacher 출력은 recipe 간 캐시해 seed당 1회만 계산한다고 가정 |
| P5 학습 token/run | 2억 / 10억 / 40억 | 가정 |

### 6.4 phase x 모델 표 (클라우드 과금 시간 h, USD; P10 / P50 / P90)

각 모델을 D-01에서 골랐을 때 그 모델로 P1–P5를 돌리는 가상 경로다. 노트북·host 시간은 포함하지 않았다.

| phase | SmolLM2-135M | SmolLM2-360M | Qwen3-0.6B | Qwen3-1.7B |
|---|---|---|---|---|
| P1 | 6.5 / 11.5 / 25.4 h<br>$10 / $17 / $35 | 7.6 / 15.2 / 42.0 h<br>$12 / $22 / $55 | 8.2 / 17.6 / 54.9 h<br>$13 / $25 / $71 | 11.4 / 29.9 / 115 h<br>$17 / $40 / $145 |
| P2 | 21.7 / 63.2 / 208 h<br>$27 / $78 / $255 | 31.6 / 101 / 367 h<br>$39 / $124 / $452 | 37.9 / 130 / 524 h<br>$47 / $160 / $644 | 55.0 / 215 / 960 h<br>$80 / $305 / $1,381 |
| P3 | 8.7 / 22.5 / 66.2 h<br>$11 / $28 / $81 | 13.3 / 34.3 / 93.1 h<br>$16 / $42 / $115 | 15.6 / 39.6 / 104 h<br>$19 / $49 / $128 | 29.0 / 74.9 / 206 h<br>$36 / $92 / $253 |
| P4 | 11.5 / 40.0 / 127 h<br>$15 / $54 / $188 | 16.6 / 59.7 / 199 h<br>$22 / $82 / $284 | 18.1 / 68.5 / 245 h<br>$25 / $95 / $343 | 17.6 / 66.3 / 230 h<br>$39 / $159 / $638 |
| P5 | 25.6 / 69.7 / 160 h<br>$44 / $130 / $395 | 34.0 / 97.5 / 282 h<br>$66 / $205 / $791 | 38.1 / 114 / 372 h<br>$79 / $259 / $1,079 | 62.3 / 201 / 832 h<br>$141 / $548 / $2,537 |
| P1–P4 합계 | 65.5 / 152 / 394 h<br>$86 / $198 / $516 | 100 / 247 / 632 h<br>$131 / $319 / $821 | 124 / 310 / 832 h<br>$162 / $400 / $1,065 | 188 / 480 / 1,361 h<br>$299 / $761 / $2,099 |
| P1–P5 합계 | 118 / 241 / 510 h<br>$178 / $374 / $810 | 181 / 379 / 839 h<br>$272 / $617 / $1,421 | 216 / 473 / 1,088 h<br>$331 / $784 / $1,904 | 337 / 811 / 1,991 h<br>$619 / $1,570 / $4,142 |

경로 합계(같은 표본 안에서 phase를 더한 값): P1–P4를 135M, P5를 360M으로 하면 $210 / $479 / $1,173(134 / 281 / 612 h), P5를 1.7B로 하면 $299 / $848 / $2,862(174 / 416 / 1,101 h). P2 참고선 Qwen3-8B + raw history는 0.5 / 0.6 / 0.9 h, $0.6 / $0.8 / $1.1이다(bf16 약 16.4GB라 48GB에 적재). 이 표의 "P1"에는 T04 microbenchmark(2 인스턴스, P50 약 3.7시간·$7.6, $5.2–11)가 들어 있다.

**SmolLM2-135M의 항목별(P10 / P50 / P90).**

| phase | 작업 | 주 자원 | 단위(P50) | 과금 시간 h | USD | 학습 메모리 GB(P50 / P90) |
|---|---|---|---|---|---|---|
| P1 | T04 spike(microbenchmark. 클라우드 1–2종은 비용 승인 뒤) | main | 2 인스턴스 | 2.5 / 3.7 / 5.6 | $5.2 / $7.6 / $11 | 5.2 / 6.2 |
| P1 | T09 retrofit 학습(arm x seed) | main | 20 run | 1.0 / 3.4 / 15.1 | $1.2 / $4.2 / $19 | 8.5 / 10.6 |
| P1 | T09 deep(r=2) 적응 학습(full x seed) | main | 5 run | 0.3 / 0.6 / 1.1 | $0.4 / $0.7 / $1.3 | 8.5 / 10.6 |
| P1 | T09 retrofit 학습 노트북 12GB 대안(시간만, 비용 0) | 노트북 | 20 run | 1.7 / 7.7 / 36.8 | $0 | 8.5 / 10.6 |
| P1 | T07·T12 dev eval(7 arm. 지연 지배) | main | 1.8만 요청 | 0.4 / 0.7 / 1.4 | $0.5 / $0.9 / $1.8 |  |
| P1 | T15 sealed readout(7 arm x seed x world x k) | main | 6.5만 요청 | 0.6 / 1.5 / 5.4 | $0.8 / $1.9 / $6.6 |  |
| P1 | T16 UJ1 E2E·회귀 gate(host CPU, 사용자 재현) | host CPU | 7 arm x 3 world | 0 | $0 |  |
| P2 | 묶음 A spike(recurrence retrofit 가능성) | main | 3 run | 2.4 / 4.4 / 8.5 | $3.0 / $5.4 / $10 | 8.7 / 10.8 |
| P2 | 묶음 D depth 격자 학습(arm x seed. family 3종 혼합) | main | 25 run | 7.0 / 32.5 / 161 | $8.6 / $40 / $198 | 10.5 / 13.2 |
| P2 | 묶음 D 노트북 12GB 대안(시간만, 비용 0) | 노트북 | 25 run | 17.0 / 81.7 / 396 | $0 | 10.5 / 13.2 |
| P2 | UJ2 배치 평가(family x depth x arm x seed) | main | 60.7만 요청 | 3.5 / 13.8 / 60.9 | $4.3 / $17 / $75 |  |
| P3 | controller teacher rollout((r,u) 조합 x 시행) | main | 243만 rollout | 0.6 / 1.6 / 9.4 | $0.7 / $2.0 / $12 |  |
| P3 | 학습된 controller 공동 미세조정 | main | 10 run | 1.6 / 4.0 / 10.7 | $2.0 / $4.9 / $13 | 8.6 / 10.7 |
| P3 | UJ3 controller 대 고정 depth·novelty-only·random gate 판정(층화) | main | 58.1만 요청 | 3.2 / 12.7 / 54.4 | $4.0 / $16 / $67 |  |
| P4 | Sleep v0 replay·teacher distillation(recipe x seed) | main | 27 run | 3.2 / 15.8 / 73.8 | $4.3 / $23 / $122 | 13.3 / 17.0 |
| P4 | UJ4 SE 대 SES readout·F12 offload/reload(다세션) | main | 65.3만 요청 | 3.9 / 15.0 / 64.8 | $4.8 / $18 / $80 |  |
| P5 | 더 넓은 retrofit·두 번째/더 큰 모델·자연어 도메인 학습 | large(H100) | 9 run | 4.3 / 22.1 / 109 | $13 / $69 / $341 | 9.2 / 11.3 |
| P5 | 등급 4 readout(새 fresh cohort, 2 도메인) | main | 13.0만 요청 | 0.9 / 2.6 / 10.4 | $1.1 / $3.3 / $13 |  |
| P5 | UJ5 실제 consumer 서빙 soak(latency·residency) | main | 1 run | 9.3 / 27.6 / 82.3 | $11 / $34 / $101 |  |

### 6.5 소형 모델의 활용률: 결론이 아니라 가설

**PROPOSAL / ESTIMATE.** 소형 모델은 활용률(MFU)이 낮다. 이유는 세 가지다.

1. **non-GEMM 연산이 큰 비중을 차지한다.** hidden 576–1024에서 RMSNorm·RoPE·SwiGLU·residual은 HBM을 왕복하는 연산이고 GEMM은 작다. SmolLM2-135M에서 층당 token당 non-GEMM HBM 왕복이 학습 pass 기준 약 144KB(전방 48KB + 역방향 96KB)이고 GEMM이 약 14 MFLOP(전방 + 입력 gradient)이라, 대역폭이 낮은 GDDR6 카드(960 GB/s)에서는 non-GEMM 시간(약 150 ns)이 GEMM 시간(약 70 ns)의 약 2배가 된다. 그래서 추정 MFU가 RTX 6000 Ada에서 0.15, A100에서 0.25, H100에서 0.18, RTX 5090에서 0.28이다. 모델이 커질수록 올라간다(1.7B는 0.30–0.40).
2. **새 모듈은 순차다.** NMM의 chunk 단위 inner loop는 이전 chunk의 기억 상태를 기다리므로 GPU를 채우기 어렵다. retrofit layer 1개의 시간을 일반 layer의 1.5 / 3 / 6배로 가정했다(가설, 값은 T04에서 잰다).
3. **batch=1 평가는 launch 지배다.** test-time write는 요청 단위 순차 갱신이라 한 session 안에서 batch를 키울 수 없다. 서로 다른 world·session은 독립이라 병렬 process나 session 배치로 처리량을 얻을 수 있지만, 그러려면 평가 harness가 같은 CLI·session 프로토콜 경로의 동등성을 보인 배치 실행(P1-T12 설계)을 가져야 한다(OPEN-11). 그렇지 못하면 요청 수 x 지연이 시간을 정한다. P1 sealed readout은 중앙 가정(약 5.5만 요청 x 평균 0.24초, 병렬 6개)에서 순수 실행 약 0.6시간이고 준비·재시도를 포함한 과금 시간은 약 1.2시간이다.

MFU 가정의 폭이 크므로(e_gemm 0.4–0.7, sw 0.65–1.0 → 중앙의 약 0.5–1.3배) **GPU 종류 간 순위는 실측 전에는 결론이 아니다.** 같은 이유로 H100이 소형에서 이론 FLOPS만큼 빠르지 않다(135M에서 H100의 추정 유효 TFLOPS 174는 이론 989.5의 18%).

**민감도 (ESTIMATE).** e_gemm·sw만 낙관(0.70·1.0)·비관(0.40·0.65)으로 바꿔 유효 실험 비용(§4.5와 같은 식, 5건/인스턴스)을 RTX 6000 Ada VM 대비 비율로 다시 계산했다. 순서는 거의 바뀌지 않는다. 135M run은 A6000 VM 0.82–0.92배, RTX 4090 container 0.56–0.63배, H100 container 1.24–1.45배, H100 VM 1.54–1.80배다. 360M run은 H100 container 0.88–0.90배, L40S·A100·H100 VM 1.08–1.19배다. 1.7B run은 H100 container 0.86–0.88배, H100 VM 1.07–1.10배, A100 VM 1.24–1.36배다. 즉 MFU 가정이 이 범위 안에서 틀려도 주력(48GB급 VM)을 고른 비용 손해는 대부분 ±15% 안이고, 큰 run에서 H100이 이득인 방향도 유지된다. 다만 MFU가 이 범위 밖이거나 새 모듈의 순차 비용(kappa)이 크면 달라질 수 있어 T04에서 확인한다.

### 6.6 메모리와 GPU 적합성

학습 메모리 = 가중치 2·N_total(bf16) + 새 모듈 16·N_new(fp32 master·grad·Adam) + activation(층 x token x (30d + 6·FFN) x 0.5. 기반이 얼어 weight-gradient용 입력 저장이 필요 없어 0.5를 곱함) + logits(f_logit x token x vocab x 4 x 2) + 1.5GB. step당 16,384 token 기준 P50 / P90이다.

| 모델 | P1 T09 | P2 depth 격자 | P4 Sleep(student 전체 갱신) | P5 넓은 retrofit | 맞는 GPU |
|---|---|---|---|---|---|
| SmolLM2-135M | 8.5 / 10.6 | 10.5 / 13.2 | 13.3 / 17.0 | 9.2 / 11.3 | 노트북 12GB: P1 가능(P90 10.6GB, 여유 약 1.4GB), P2는 P90에서 12GB 초과(batch 축소). 24GB 여유 |
| SmolLM2-360M | 13.3 / 15.8 | 16.4 / 20.1 | 24.4 / 24.4 | 15.2 / 18.4 | 노트북 12GB는 step당 token을 줄여야 함(8k에서 약 9GB). 24GB 가능, 48GB 여유 |
| Qwen3-0.6B | 16.3 / 21.9 | 20.7 / 27.9 | 27.0 / 27.0 | 18.2 / 24.2 | 24GB는 P1 가능, P2 P90(28GB)·P4(27GB)는 부족. 48GB 권장 |
| Qwen3-1.7B | 28.8 / 35.2 | 37.8 / 47.2 | 61.0 / 61.0 | 35.8 / 45.7 | 48GB(P1·P5, P90 46GB까지). P2 P90은 47GB로 한계(batch 축소·재계산). P4 전체 갱신 61GB는 80GB. 24GB는 활성 재계산 필수 |

**이 추정이 틀릴 수 있는 곳.** (i) vocab가 큰 Qwen3는 logits 메모리가 커서 f_logit(0.1–0.5)에 민감하다. (ii) 활성 메모리는 attention 구현·재계산 정책에 따라 2배까지 달라진다. (iii) retrofit layer의 위치(통과 층 비율 0.5–1.0). (iv) 이 표는 한 번에 한 process다. 병렬 평가 process 6–10개는 각각 추론 메모리(약 2–5GB)가 더 든다.


### 6.7 2026-11-18 갱신: P0의 작업량과 비용 (frozen LLM serving, NP-1 hook, 실행 행렬)

**ESTIMATE / NOT RUN.** P0는 gradient 학습이 0회이고 frozen 공개 가중치 LLM과 비모수 기억으로 전체 flow를 돈다([18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md)). 그래서 비용은 학습 FLOPs가 아니라 **호출 수와 서빙 처리량**이 정한다. 입력은 docs/18의 P0 실행 행렬(16행, low / base / high)이다. 이 행렬의 low / base / high를 이 문서의 P10 / P50 / P90에 대응시켜 같은 분위 함수(§6.1)로 표본을 뽑았다. 한 행의 호출 수·입력 token·출력 token은 같은 분위로 함께 움직인다(world 수가 함께 커지기 때문이다).

**공식 (frozen LLM 서빙).** prefill 처리율 = MFU_pf x 피크 FLOPS / (2N), decode 처리율(sequence 1개) = 메모리 효율 x 대역폭 / (2N 바이트), 동시 sequence c개이면 min(c x decode, prefill 처리율). 한 행의 시간 = (입력 token / prefill + 출력 token / decode) x (NP-1 hook이면 hook 배수) + (호출 수 x 호출 고정 지연 + 임베딩 호출 x 임베딩 지연) / 병렬 process 수. 과금 시간은 §6.1과 같이 재시도·유휴·준비를 곱한다. host 행은 CPU 처리율 가정으로 벽시계만 계산한다(비용 0). NP-1 hook 행은 R02(host), R12, R13(노트북), R14다.

**가정 (낙관 / 중앙 / 비관).**

| 키 | 뜻 | 값 | 근거 |
|---|---|---|---|
| pf_mfu | prefill MFU(HF eager bf16) | 0.45 / 0.33 / 0.2 | 소형 서빙 활용률은 낮다(docs/15 §6.5). mfu_inf(0.45/0.35/0.20)와 같은 폭 |
| dec_eff | decode 시 메모리 대역폭 효율(batch 1) | 0.65 / 0.5 / 0.3 | decode는 가중치 읽기가 지배. HF eager는 이론 대역폭의 일부만 쓴다(가정) |
| conc | 동시 진행 sequence 수/인스턴스 | 16 / 8 / 3 | 서로 다른 world·session은 독립이라 묶을 수 있으나 write는 순차(§6.5). 낙관 16, 비관 3 |
| t_ov | LLM 호출 1건의 CPU 측 고정 지연(s) | 0.03 / 0.08 / 0.25 | tokenize·JSON·검색·hook. §6.1의 t_call 8/20/40 ms와 달리 서빙 호출은 더 무겁다고 가정 |
| par_ov | 호출 지연을 겹치는 병렬 process 수 | 8 / 4 / 2 | 12 vCPU 기준 2–8 |
| hook | NP-1 hook(activation 추출·주입) 시 forward 배수 | 1.05 / 1.15 / 1.4 | 추출은 forward 중 복사, 주입은 forward 개입. 1.05–1.40(가정, 측정은 P0 작업) |
| emb_ms | 임베딩 호출 1건(ms, 배치 효과 포함) | 2 / 5 / 15 | 0.6B 임베딩 모델 GPU. 문장 약 100 token(가정) |
| h_pf8 | host CPU 8B Q4 prefill token/s | 100 / 60 / 30 | docs/18 §10.5의 가정(입력 100/60/30)과 같다. 실측 아님(P0-T04에서 측정) |
| h_dc8 | host CPU 8B Q4 decode token/s | 8 / 5 / 3 | docs/18 §10.5의 가정(출력 8/5/3)과 같다. 실측 아님 |
| h_pf1 | host CPU 1.7B HF prefill token/s | 300 / 150 / 60 | docs/18 §10.5의 가정(입력 300/150/60)과 같다. 실측 아님 |
| h_dc1 | host CPU 1.7B HF decode token/s | 5 / 3 / 1.5 | docs/18 §10.5의 가정(출력 5/3/1.5)과 같다. 실측 아님 |
| h_ov | host 호출 1건 고정 지연(s) | 0.05 / 0.15 / 0.4 | 프로세스·검색·JSON |
| h_emb | host 임베딩 호출 1건(s) | 0.03 / 0.08 / 0.2 | GGUF 0.6B 임베딩 가정 |

**서빙 처리량 (48GB급 1장, RTX 6000 Ada 사양, P10 / P50 / P90 중 좋은 쪽부터).**

| 모델 | 가중치(bf16) | prefill token/s | decode token/s (sequence 1개) | decode token/s (동시 진행 반영) |
|---|---|---|---|---|
| 8B급 bf16 | 16.4 GB | 9.96K / 7.38K / 4.44K | 38.0 / 29.1 / 17.5 | 474 / 210 / 77 |
| 1.7B급 bf16 | 3.4 GB | 48K / 35.6K / 21.4K | 183.4 / 140.6 / 84.3 | 2.29K / 1.01K / 372 |
| 3.3B급 bf16(GPT-1900 D34) | 6.6 GB | 24.8K / 18.4K / 11.1K | 94.8 / 72.7 / 43.5 | 1.18K / 523 / 192 |
| 7.24B급 bf16(TypewriterLM) | 14.5 GB | 11.3K / 8.35K / 5.03K | 43.1 / 33.0 / 19.8 | 537 / 238 / 87 |
| 13B급 bf16(Talkie) | 26.0 GB | 6.28K / 4.65K / 2.8K | 24.0 / 18.4 / 11.0 | 299 / 132 / 49 |

**P0 실행 행렬의 token·시간·비용 (P10 / P50 / P90, 호출·token은 low / base / high).**

| run | 내용 | 모델 | 위치 | 구분 | 호출 | 입력 token | 출력 token | 벽시계 h | 비용 USD |
|---|---|---|---|---|---|---|---|---|---|
| P0-R01 | UJ0 종료 gate: NP-0 경로 (suite S-A 소형 + Sleep) | 8B급 instruction (GGUF Q4) | host | 필수 | 573 / 1.15K / 1.72K | 237K / 592K / 1.24M | 21.2K / 53K / 111K | 2.4 / 6.1 / 14.3 | 0 |
| P0-R02 | UJ0 종료 gate: NP-1 경로 (suite S-A 소형) | 소형 HF (1.7B급 이하, CPU) | host hook | 필수 | 160 / 320 / 480 | 71.7K / 179K / 376K | 2.69K / 6.72K / 14.1K | 0.47 / 1.2 / 3.1 | 0 |
| P0-R03 | UJ0 종료 gate: 발견 run 소형 (suite S-B, 원형 4종 각 1) | 8B급 instruction (GGUF Q4) | host | 필수 | 763 / 763 / 1.53K | 366K / 458K / 1.28M | 42.8K / 53.5K / 150K | 3.7 / 6.7 / 15.9 | 0 |
| P0-R04 | UJ0 종료 gate: ET-3p 소형 (시간캡슐 모델, stream 20-40항목) | 시간캡슐 1.7B급 (CPU) | host | 필수 | 220 / 280 / 340 | 201K / 314K / 526K | 16K / 21.3K / 31.6K | 1.6 / 2.9 / 5.5 | 0 |
| P0-R05 | suite S-A dev pilot: 핵심 arm (분산 추정, 난이도 조정) | 8B급 instruction (HF bf16) | runcrate | 필수 | 19.5K / 38.9K / 77.9K | 11.3M / 28.2M / 79M | 764K / 1.91M / 5.34M | 1.5 / 4.5 / 14.0 | $3.2 / $8.9 / $27 |
| P0-R06 | suite S-A dev pilot: 절제·개입 arm | 8B급 instruction (HF bf16) | runcrate | 필수 | 130K / 260K / 520K | 46.3M / 116M / 324M | 4.01M / 10M / 28.1M | 8.0 / 23.0 / 70.3 | $15 / $44 / $138 |
| P0-R07 | suite S-B dev pilot: 발견 세계 (ET-0) | 8B급 instruction (HF bf16) | runcrate | 필수 | 79.6K / 159K / 318K | 57.6M / 144M / 403M | 5.01M / 12.5M / 35.1M | 8.7 / 26.2 / 83.3 | $17 / $51 / $161 |
| P0-R08 | suite S-A sealed readout: 핵심 arm (등급 3 시도) | 8B급 instruction (HF bf16) | runcrate | 필수 | 117K / 234K / 467K | 67.7M / 169M / 474M | 4.58M / 11.5M / 32.1M | 9.2 / 26.7 / 79.1 | $18 / $51 / $154 |
| P0-R09 | suite S-A sealed readout: 절제·개입 arm | 8B급 instruction (HF bf16) | runcrate | 필수 | 390K / 780K / 1.56M | 139M / 348M / 973M | 12M / 30.1M / 84.2M | 22.9 / 67.5 / 208 | $44 / $130 / $404 |
| P0-R10 | suite S-B sealed readout: 발견 세계 (등급 3 시도) | 8B급 instruction (HF bf16) | runcrate | 필수 | 696K / 1.39M / 2.78M | 410M / 1.02B / 2.87B | 41.7M / 104M / 292M | 69.1 / 215 / 647 | $130 / $409 / $1,263 |
| P0-R11 | suite S-C: 재분장 역사 사례 (ET-1, 탐색) | 8B급 instruction (HF bf16) | runcrate | 필수 | 26.9K / 53.9K / 108K | 29.9M / 74.8M / 210M | 1.25M / 3.12M / 8.75M | 3.1 / 8.5 / 25.8 | $6.1 / $17 / $50 |
| P0-R12 | suite S-D (선택): frozen LLM 내부 schema 중첩 관찰 | Base+post-training 쌍 (8B급 HF) | runcrate hook | 선택 | 4.8K / 9.6K / 19.2K | 1.31M / 3.28M / 9.18M | 64K / 160K / 448K | 0.20 / 0.55 / 1.7 | $0.8 / $1.5 / $3.6 |
| P0-R13 | 135M급 base 일치 확인: NP-1 성립 (V0-16) | 135M급 (HF) | 노트북 hook | 필수 | 23.4K / 46.8K / 93.7K | 10M / 25M / 70.1M | 590K / 1.48M / 4.13M | 0.18 / 0.53 / 1.5 | 0 |
| P0-R14 | NP-1 artifact 저장·재적재·합성 (V0-13, 과제 단위) | 8B급 instruction (HF bf16) | runcrate hook | 필수 | 13K / 26K / 52K | 4.89M / 12.2M / 34.2M | 307K / 768K / 2.15M | 0.77 / 2.3 / 7.1 | $1.9 / $4.7 / $14 |
| P0-R15 | ET-3p: 시간캡슐 모델 위의 NP 시스템 1회 (탐색) | 시간캡슐 3B-13B급 (HF 또는 맞춤 PyTorch) | runcrate | 필수 | 1.73K / 19.6K / 266K | 1.85M / 23.2M / 438M | 93.1K / 994K / 16.4M | 0.24 / 3.1 / 48.3 | $0.9 / $6.2 / $94 |
| P0-R16 | suite S-A 복제 모델 소규모 재현 (선택) | 다른 계열 8B급 (HF bf16) | runcrate | 선택 | 0 / 58.4K / 117K | 0 / 42.3M / 118M | 0 / 2.86M / 8.02M | 0.00 / 6.6 / 20.5 | $0.7 / $13 / $40 |

**합계.** host와 노트북은 벽시계 시간이고 비용에 넣지 않는다. host 합계는 docs/18 §10.5의 base·중간 값(약 14.3시간)과 같은 처리량 가정에서 나온 표본 분포이며, 표본 P50이 더 큰 이유는 §6.1에서 설명한 분포의 꼬리와 호출 고정 지연이 더해지기 때문이다.

| 묶음 | 시간 h | 비용 USD |
|---|---|---|
| host(UJ0 gate R01-R04, 벽시계, 비용 0) | 11.8 / 19.2 / 31.5 |  |
| 노트북(R13, 벽시계, 비용 0) | 0.18 / 0.53 / 1.5 |  |
| runcrate 필수(R05-R11, R14, R15) | 313 / 689 / 1,647 | $385 / $847 / $2,026 |
| runcrate 선택(R12, R16) | 2.1 / 12.0 / 34.3 | $2.6 / $15 / $42 |
| runcrate 합계(필수+선택) | 321 / 703 / 1,674 | $395 / $864 / $2,059 |

runcrate 행의 합계(실행 행렬 base)는 호출 약 3.03M건(low 1.48M, high 6.29M), 입력 token 약 1.98B(low 770M, high 5.93B), 출력 token 약 178M(low 69.8M, high 513M)이다.

**민감도: 서빙 방식과 frozen LLM 크기가 레버다 (runcrate 합계, 필수+선택).**

| 변형 | 과금 시간 h | 비용 USD |
|---|---|---|
| 기본 가정: HF eager, 동시 sequence 3/8/16 | 321 / 703 / 1,674 | $395 / $864 / $2,059 |
| 서버형 continuous batching: 동시 sequence x4, 호출 지연 x0.5 | 164 / 316 / 620 | $202 / $389 / $763 |
| 순차에 가까운 harness: 동시 sequence x0.5 | 500 / 1,157 / 2,843 | $616 / $1,423 / $3,497 |
| frozen LLM을 4B급으로 낮춤(8B 행만, 가중치와 token 수는 그대로) | 176 / 380 / 868 | $216 / $468 / $1,068 |
| 서버형 + 4B급 | 90 / 171 / 330 | $110 / $210 / $406 |

읽는 법. (1) 기본 가정은 HF eager 서빙이고 동시 sequence가 적다. continuous batching 서버로 바꾸면 비용이 약 45%가 된다(동시 sequence를 4배로 한 가정이며 측정이 아니다). 단 서버형 실행이 「같은 CLI·session 프로토콜·runtime 경로」와 동등함을 보이는 일(OPEN-11)과 NP-1 hook 호환이 먼저다. (2) 4B급은 주 모델(8B급)을 바꾸는 것이 아니라 복제·보조 run의 선택지다. 8B 행의 모델 크기만 반으로 두었고 호출·token 수는 그대로다. (3) 모델·서빙을 바꾸는 결정은 D-46이다.

**ET-3p run 1회 (시간캡슐 4B–13B급 HF bf16, runcrate 48GB급).** 실행 행렬의 R15는 [17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md)의 ET-3p 규모(stream 항목 330 / 900 / 2,400개, checkpoint 7 / 14 / 28, checkpoint당 probe 6개)를 입력으로 쓴다([18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md) §6.3). 아래 비용은 그 규모의 값이며 위 실행 행렬의 R15 행과 같다.

| 규모 | 과금 시간 h | 비용 USD |
|---|---|---|
| ET-3p run 1회(실행 행렬 R15 = docs/17의 ET-3p 규모) | 0.76 / 5.0 / 76.1 | $0.9 / $6.2 / $94 |

ET-3p의 host 소형판은 R04(시간캡슐 1.7B급, CPU)이고 벽시계 P50 약 2.9시간이다. 주 실행(대상 1개, 절차 전체)이 gate이고 결과 주장은 없다.


### 6.8 2026-11-18 갱신: 시간캡슐 기반 확보 3안 (P4–P6)

**ESTIMATE / NOT RUN.** 시간캡슐 기반(ET-3·ET-4)을 확보하는 안은 셋이다. 규모의 사실(크기·corpus·학습 token)은 조사 기록 [2026-11-18-blueprint-et-design.md](/home/jimmy/repos/full-continual-learning/research/2026-11-18-blueprint-et-design.md)의 시간캡슐 모델 현황표에서 가져왔고 비용은 이 문서가 계산한다.

| 안 | 내용 | 가정한 모델 |
|---|---|---|
| 1. 공개 모델 사용(기본) | 공개된 시간캡슐 모델을 받아 쓴다. 비용은 받아서 점검하는 일(누수 감사·생성 점검)과 볼륨뿐이다 | 13B 이하. 가장 큰 Talkie 13B(bf16 약 26GB)를 상한으로 센다 |
| 2. 소형 자체 사전학습 | GPT-1900 D26급(1.68B)을 22B token corpus로 1–3 epoch 처음부터 학습 | 공개 사례 앵커: GPT-1900 D26은 22B token을 2 epoch(저자 카드) |
| 3. 중형 자체 사전학습 | TypewriterLM급(7.24B)을 54B token corpus로 2.0–3.0 epoch | 공개 사례 앵커: 54B token corpus, 약 140B token 학습(논문) |

**공식.** FLOPs = 6·N·D x 보정(1.0 / 1.08 / 1.2), GPU-시간 = FLOPs / (피크 x MFU 0.45 / 0.35 / 0.25) / 3600, 과금 GPU-시간 = GPU-시간 x 재시작 1.05 / 1.2 / 1.5 x (1 + 유휴) + 인스턴스 준비 x GPU 수. 비용 = 과금 GPU-시간 x GPU당 가격 + 전처리(CPU 인스턴스) + 영구 볼륨(0.03 USD/GB-월) + 누수 감사·평가. 노드는 오늘 스냅샷에서 두 종류를 비교했다: H100 4장 VM(GPU당 $5.85)과 A100 80GB 8장 VM(GPU당 $1.73). 둘의 FLOP당 비용은 비슷하고(약 0.9배) 벽시계는 A100 노드가 약 1.6배 길다.

| 안 | 파라미터 | corpus token(정제 후) | 학습 token | 노드 | FLOPs P10 / P50 / P90 | 과금 GPU-시간 | 벽시계 일 | 비용 USD | 볼륨 GB | 전처리 CPU 시간 | 전처리 CPU 비용 USD |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1. 공개 모델 사용(기본) | 13B 이하(표 1a) | 0(받아 쓴다) | 0 | - |  | 1.9 / 3.5 / 9.3 |  | $4.0 / $7.1 / $14 | 36.0 / 36.0 / 36.0 |  |  |
| 2. 소형 자체 사전학습(GPT-1900 D26급) | 1.68B | 22B | 22B x epoch 1-3 | H100 4장 VM | 2.45e+20 / 4.66e+20 / 7.30e+20 | 267 / 531 / 958 | 2.7 / 5.3 / 9.7 | $1,609 / $3,165 / $5,647 | 362 / 440 / 537 | 0.46 / 1.20 / 3.18 h | 0.32 / 0.82 / 2.16 |
| 2. 소형 자체 사전학습(GPT-1900 D26급) | 1.68B | 22B | 22B x epoch 1-3 | A100 80GB 8장 VM | 2.45e+20 / 4.66e+20 / 7.30e+20 | 846 / 1,683 / 3,036 | 4.3 / 8.4 / 15.3 | $1,511 / $2,968 / $5,299 | 362 / 440 / 537 | 0.46 / 1.20 / 3.18 h | 0.32 / 0.82 / 2.16 |
| 3. 중형 자체 사전학습(TypewriterLM급) | 7.24B | 54B | 54B x epoch 2.0-3.0 | H100 4장 VM | 5.06e+21 / 6.52e+21 / 7.86e+21 | 5,004 / 7,399 / 11,335 | 50.2 / 74.6 / 114 | $29,371 / $43,496 / $66,566 | 1,021 / 1,271 / 1,585 | 1.14 / 2.96 / 7.80 h | 0.78 / 2.01 / 5.30 |
| 3. 중형 자체 사전학습(TypewriterLM급) | 7.24B | 54B | 54B x epoch 2.0-3.0 | A100 80GB 8장 VM | 5.06e+21 / 6.52e+21 / 7.86e+21 | 15,870 / 23,461 / 35,946 | 79.7 / 118 / 181 | $27,595 / $40,846 / $62,560 | 1,021 / 1,271 / 1,585 | 1.14 / 2.96 / 7.80 h | 0.78 / 2.01 / 5.30 |

**공개 앵커와의 비교.** TimeCapsuleLLM v2(1.22B)는 H100 117시간, 약 $341을 썼다고 저자가 적었다(RunPod). 그 corpus(112GB text)를 약 28B token(4바이트/token 가정)의 0.5 epoch로 환산하면 FLOPs가 약 1e20이고, 소형 안의 FLOPs(P50 약 4.7e20)는 그 약 4–5배다. 그래서 소형 안의 GPU-시간(H100 4장 노드 P50 약 531시간)과 이 앵커는 같은 자릿수다. Ranke-4B 사전 공개 노트는 4B 모델 checkpoint 하나를 128 GH200 약 16.5시간(약 2,100 GPU-시간)으로 학습했다고 적었다.

**결론(PROPOSAL).** 안 1이 기본이다. 안 2는 P50 약 $3,165으로 승인할 수 있는 규모이고 한 노드로 약 5.3일이다. 안 3은 P50 약 $43,496이고 한 노드로 약 74.6일이라 단일 인스턴스로는 비현실적이다. 4장 이상 노드를 여러 개 쓰는 다중 노드 실행이 가능한지는 공개 문서에서 확인하지 못했다(OPEN-22). 안 2·3은 공개 모델의 마감·누수·라이선스 때문에 ET-3·4가 막힐 때만 결정 후보가 된다(D-29).


### 6.9 2026-11-18 갱신: 시간캡슐 기반 retrofit과 ET run (P5·P6)

**ESTIMATE / NOT RUN.** retrofit 학습은 §6.1·§6.6의 P5 식을 시간캡슐 기반에 그대로 적용했다(학습 token 2억 / 10억 / 40억, run 6 / 9 / 20, retrofit layer 비율 L/4–전 층, main·A100·H100 중 최저가). 모델 구조는 공개 config를 썼다: GPT-1900 D34는 nanochat 구조로 층 34, hidden 2176, ffn 4배, head 17, vocab 32,768(FLOP 환산 본체 약 2.1B, 나머지는 value embedding), TypewriterLM은 Llama 구조 층 32, hidden 4096, ffn 14,336, GQA 32/8, vocab 32,000이다. **Talkie 13B는 구조를 확인하지 못해 층 40, hidden 5,120, ffn 13,824, vocab 65,536으로 가정했다(OPEN-21).** ET run은 docs/17의 stream 규모 표(ET-3: 항목 330 / 900 / 2,400, 축소 설계 run 54 / 225 / 510, ET-4: 항목 600 / 1,700 / 4,500, 축소 설계 run 108 / 240 / 540)에서 run마다 stream 투입 token과 checkpoint별 probe 호출을 세고, 항목마다 write 지연(0.02 / 0.05 / 0.15초), probe마다 답 생성 100 / 250 / 600 token, deep 경로 배수 1.0 / 1.3 / 2.0, 병렬 1.5–6으로 시간을 계산했다. ET run은 GPU 연산이 아니라 write·decode 지연이 지배한다.

| 기반 | 항목 | 과금 시간 h | 비용 USD |
|---|---|---|---|
| GPT-1900 D34(3.29B, FLOP 환산 본체 약 2.1B) | retrofit 학습(P5 식: 토큰 2억/10억/40억 x run 6/9/20) | 48.8 / 264 / 1,319 | $154 / $830 / $4,154 |
| GPT-1900 D34(3.29B, FLOP 환산 본체 약 2.1B) | ET-3 run 전체(축소 설계 run 수, probe 포함) | 3.1 / 22.9 / 151 | $3.9 / $28 / $186 |
| GPT-1900 D34(3.29B, FLOP 환산 본체 약 2.1B) | ET-4 run 전체(축소 설계 run 수, probe 포함) | 6.8 / 41.8 / 260 | $8.3 / $52 / $320 |
| TypewriterLM(7.24B) | retrofit 학습(P5 식: 토큰 2억/10억/40억 x run 6/9/20) | 116 / 620 / 3,116 | $365 / $1,952 / $9,815 |
| TypewriterLM(7.24B) | ET-3 run 전체(축소 설계 run 수, probe 포함) | 7.1 / 57.0 / 382 | $8.8 / $70 / $470 |
| TypewriterLM(7.24B) | ET-4 run 전체(축소 설계 run 수, probe 포함) | 16.3 / 102 / 642 | $20 / $125 / $790 |
| Talkie(13B, 구조 가정) | retrofit 학습(P5 식: 토큰 2억/10억/40억 x run 6/9/20) | 207 / 1,099 / 5,572 | $651 / $3,462 / $17,551 |
| Talkie(13B, 구조 가정) | ET-3 run 전체(축소 설계 run 수, probe 포함) | 12.6 / 102 / 692 | $16 / $125 / $851 |
| Talkie(13B, 구조 가정) | ET-4 run 전체(축소 설계 run 수, probe 포함) | 28.8 / 182 / 1,157 | $35 / $224 / $1,423 |

읽는 법. ET run 자체는 P50 $28–$224(대상 1개 기준)로 작다. 비용의 대부분은 retrofit 학습이고 이는 기반 크기와 token 가정(P5 식)이 정한다. ET-4의 대상이 둘이면 ET-4 run 비용은 2배가 된다. 4B–13B 시간캡슐 모델의 host gate는 소형판(GPT-1900급)이 맡는다(§5.4).


### 6.10 2026-11-18 갱신: P1 base 크기 비교와 P1–P5의 NP arm·ET 단 추가분

**P1 base를 135M급으로 둘 때와 1.7B–4B급으로 올릴 때(MD-O).** §6.4의 P1 항목(T04 microbenchmark, T09 학습, deep 적응 학습, dev eval, sealed readout)을 같은 가정·같은 표본으로 모델만 바꿔 다시 계산했다. Qwen3-4B의 구조는 공개 config로 확인했다(36층, hidden 2,560, ffn 9,728, GQA 32/8, vocab 151,936, Apache-2.0). NP-1 arm 추가분은 실행 행렬 R13(135M급 NP-1 성립 확인)을 그 base 크기로 다시 계산한 값이다.

| P1 base | 파라미터 | P1 과금 시간 h | P1 비용 USD | NP-1 arm 추가분 USD | 135M 대비 P50 증가 USD | 학습 메모리 GB (P50 / P90) |
|---|---|---|---|---|---|---|
| SmolLM2-135M(기본) | 135M | 6.5 / 11.5 / 25.4 | $10 / $18 / $35 | $0.6 / $1.1 / $2.5 | 0 | 8.55 / 10.6 |
| SmolLM2-360M | 362M | 7.6 / 15.2 / 42.0 | $12 / $22 / $55 | $0.7 / $1.3 / $2.9 | $4.7 | 13.3 / 15.8 |
| Qwen3-1.7B | 1721M | 11.4 / 29.9 / 115 | $17 / $40 / $145 | $1.1 / $2.3 / $6.2 | $22 | 28.8 / 35.2 |
| Qwen3-4B | 4022M | 17.7 / 57.1 / 243 | $25 / $73 / $303 | $1.6 / $4.0 / $12 | $56 | 48.0 / 56.4 |

읽는 법. 1.7B는 P50에서 약 $22, 4B는 약 $56 더 든다. 4B는 학습 메모리가 P50에서 이미 약 48GB이고 P90에서 56GB라서 48GB급 한 장에는 안 들어간다. 표의 4B 비용은 48GB급 가격으로 계산한 하한이고 실제로는 80GB급(A100 $1.73, H100)이 필요하다. 기본은 현재 로드맵의 135M급이다. 올릴지는 D-01과 연결된 결정 후보다(D-20).

**P1–P5의 NP arm과 ET 단 추가분 (P10 / P50 / P90).** NP arm은 영구 대조군이라 그 phase의 base로 다시 돈다(MD-O). 재실행 비율은 NP arm 0.5 / 1.0 / 1.0(R13 규모), ET 단 0.25 / 0.5 / 1.0(P0 dev·sealed 대비)으로 가정했다(P0가 ET-0 전체를 돌고 이후 phase는 새 arm만 더한다는 가정이며 docs/09의 phase별 ET 단 대응에 따른다). P1–P4는 135M, P5는 시간캡슐 7.1B(TypewriterLM 환산)를 대표 base로 했다. 시간캡슐 기반의 ET-3 run은 §6.9에 있다.

| phase | 항목 | base | 과금 시간 h | 비용 USD | 비고 |
|---|---|---|---|---|---|
| P1 | NP arm(np1 hook) 재실행 | base 135M | 0.45 / 0.87 / 2.0 | $0.6 / $1.1 / $2.5 | NP arm은 그 phase의 base로 다시 돈다(MD-O) |
| P1 | ET 단 추가분 | base 135M | 4.0 / 12.0 / 42.4 | $4.9 / $15 / $52 | ET-0 학습 arm 대 NP arm. ET-3p 회귀는 host(비용 0) |
| P2 | NP arm(np1 hook) 재실행 | base 135M | 0.45 / 0.87 / 2.0 | $0.6 / $1.1 / $2.5 | NP arm은 그 phase의 base로 다시 돈다(MD-O) |
| P2 | ET 단 추가분 | base 135M | 4.5 / 13.0 / 44.0 | $5.6 / $16 / $54 | ET-0 깊이 곡선 + ET-1(R11) |
| P3 | NP arm(np1 hook) 재실행 | base 135M | 0.45 / 0.87 / 2.0 | $0.6 / $1.1 / $2.5 | NP arm은 그 phase의 base로 다시 돈다(MD-O) |
| P3 | ET 단 추가분 | base 135M | 0.42 / 0.80 / 1.9 | $0.5 / $1.0 / $2.3 | ET-1 + ET-2 |
| P4 | NP arm(np1 hook) 재실행 | base 135M | 0.45 / 0.87 / 2.0 | $0.6 / $1.1 / $2.5 | NP arm은 그 phase의 base로 다시 돈다(MD-O) |
| P4 | ET 단 추가분 | base 135M | 0.42 / 0.80 / 1.9 | $0.5 / $1.0 / $2.3 | ET-1 잠복 효과 + ET-2 + ET-3 pilot 탐색(별도 행) |
| P5 | NP arm(np1 hook) 재실행 | base 7111M | 1.9 / 5.1 / 16.3 | $2.4 / $6.3 / $20 | NP arm은 그 phase의 base로 다시 돈다(MD-O) |
| P5 | ET 단 추가분 | base 7111M | 51.6 / 172 / 596 | $63 / $212 / $733 | ET-3 정식(별도 행). NP arm은 시간캡슐 기반으로 재실행 |


### 6.11 PAPER-k 묶음표 (2026-11-18)

**ESTIMATE / NOT RUN.** 논문마다 실행 수, 자원 tier, 시간, 비용이다. 논문의 실험 설계는 [19-paper-plan.md](/home/jimmy/repos/full-continual-learning/docs/19-paper-plan.md)가 소유하고, 그 표는 이 이름(PAPER-k 묶음표)으로 이 절을 가리킨다. 이 표의 실행 수는 docs/19가 아니라 docs/18의 P0 실행 행렬과 docs/09의 phase별 ET 단 대응(MD-B)을 근거로 잡았다. 비용은 실행 행렬·stream 규모의 low / base / high를 이 문서의 P10 / P50 / P90에 대응시킨 값이다. P1–P5는 11-17의 135M 경로(§6.4)에 NP arm 재실행과 ET 단 추가분(§6.10)을 더했고, PAPER-5·6은 시간캡슐 기반(TypewriterLM 7.24B로 대표, 확보 안 1)의 retrofit·서빙·ET run을 더했다. 사용한 가정 전체는 [2026-11-18-blueprint-et-design.md](/home/jimmy/repos/full-continual-learning/research/2026-11-18-blueprint-et-design.md)의 부록 TSV(assumptions)에 있다.

| 논문 | phase | ET 단 | 실행(근거) | 자원 tier | 과금 시간 h | 비용 USD | 비고 |
|---|---|---|---|---|---|---|---|
| PAPER-0 | P0(NP) | ET-0 판정, ET-1·ET-3p 탐색 | P0 실행 행렬 R05-R11·R14·R15(필수) + R12·R16(선택), host gate R01-R04 | 1 host(gate), 3 runcrate 48GB급(대량 readout) | 321 / 703 / 1,674 | $395 / $864 / $2,059 | docs/18의 실행 행렬 기준. 선택 R12·R16 포함. host와 노트북 시간은 비용 0이고 §6.7의 합계 표에 따로 있다 |
| PAPER-0b | P0 직후(선택) | ET-0·1 benchmark, ET-3p | P0 공유분 + ET-1 benchmark 확장 1배 + ET-3p 대상 1개 추가 | 3 runcrate 48GB급 | 8.1 / 27.0 / 101 | $10 / $33 / $124 | PAPER-0과 겹치는 run은 다시 세지 않은 추가분이다. 단독 총계는 PAPER-0과 추가분의 합 |
| PAPER-1 | P1 | ET-0(학습 arm 대 NP), ET-3p 회귀 | P1 학습·평가(135M) + NP arm 재실행 + ET 추가분 | 1 host(gate), 2 노트북 우선, 3 48GB급 | 14.4 / 27.9 / 61.5 | $21 / $38 / $78 | 기본 P1 base 135M. 1.7B–4B로 올리면 §6.10의 P1 base 비교표를 본다 |
| PAPER-2 | P2 | ET-0 깊이 곡선, ET-1 | P2 학습·평가(135M) + NP arm + ET 추가분 | 1 host(gate), 3 48GB급 | 36.5 / 86.1 / 234 | $45 / $106 / $288 |  |
| PAPER-3 | P3 | ET-1, ET-2 | P3 학습·평가 + NP arm + ET 추가분 | 1 host(gate), 3 48GB급 | 10.7 / 24.5 / 68.3 | $13 / $30 / $84 |  |
| PAPER-4 | P4 | ET-1 잠복, ET-2, ET-3 pilot 탐색 | P4 Sleep·readout + NP arm + ET 추가분 + ET-3 pilot 탐색(시간캡슐 기반 retrofit은 PAPER-5 행에 둠) | 1 host(gate), 3 48GB급, 4 대형(teacher) | 13.6 / 42.1 / 128 | $18 / $57 / $191 | 시간캡슐 기반 ET-3 pilot 탐색 run은 PAPER-5 행에서 센다(이 행에는 넣지 않음) |
| PAPER-5 | P5 | ET-3(정식) | 시간캡슐 기반(TypewriterLM급 7.24B로 대표) retrofit + readout + soak + ET-3 pilot 대상 1개 + NP arm·ET 추가분 | 1 host(gate), 3 48GB급, 4 대형 가능 | 401 / 1,145 / 3,692 | $787 / $2,593 / $10,583 | 확보 안 1(공개 모델 사용) 가정. 자체 사전학습은 §6.8의 표 |
| PAPER-6 | P6(ET) | ET-4(봉인 주력 대상 1개 기준) | 봉인 사전 명세 recipe로 retrofit 재학습(P5 학습량의 1/3로 가정) + ET-4 봉인 run(대상 1개, 입력 tier 변형과 대조 stream 포함) | 3 48GB급, 4 대형 가능 | 100 / 444 / 1,515 | $230 / $1,010 / $3,661 | 대상 수는 OPEN. 대상이 둘이면 ET-4 부분이 2배 |

읽는 법. (1) PAPER-0의 비용은 P0 실행 행렬 전체(선택 R12·R16 포함)이고 서빙 방식이 가장 큰 레버다(§6.7). (2) PAPER-0b는 PAPER-0과 겹치는 run을 다시 세지 않은 추가분이다. (3) PAPER-1–4는 135M 경로라 작다. 단 P1 base를 올리면 §6.10의 증가분이 더해진다. (4) PAPER-5·6은 retrofit 학습이 지배하고 기반 크기(3.3B–13B, §6.9)와 token 가정에 가장 민감하다. (5) 자체 사전학습을 택하면 §6.8의 비용이 PAPER-5 앞에 더해진다. (6) host·노트북 시간은 비용에 넣지 않았다.

## 7. 운영 절차

**PROPOSAL.** 인스턴스 생성·종료는 마스터(리더)만 한다. 사용자의 비용 승인 없이는 시작하지 않는다.

### 7.1 실행 순서

| 단계 | 하는 일 | 기록·검사 |
|---|---|---|
| ① 사전 검사(host·노트북) | 계약·자동 테스트 통과, 100 step 정도의 smoke run(CPU 또는 노트북)으로 코드 결함을 먼저 잡는다. 클라우드 실패의 대부분은 하드웨어가 아니라 코드·설정이므로 가장 싼 곳에서 먼저 터뜨린다 | 테스트 결과, smoke의 step 시간·메모리 |
| ② 실행 manifest | run ID, 목적(phase·작업), (arm x seed) unit 목록, 코드 git hash, 데이터 hash, 모델 revision, 이미지 digest·uv lock hash, 후보 상품(순서 포함), **예상 GPU-시간·예상 USD, 중단 기준(예상의 1.5배)**, max_runtime·idle 값 | manifest hash를 원장에 먼저 기록 |
| ③ 사용자 비용 승인 gate | 예상 비용과 상한을 사용자에게 보고하고 승인(또는 거절)을 받는다. 승인 범위 밖 지출은 없다 | 승인 기록(날짜·금액 상한) |
| ④ 마스터가 생성 | **max_runtime과 idle_shutdown 지정은 필수**(서버 측 자동 terminate). max_runtime = 예상 과금 시간 x 1.5, idle_shutdown = 30–60분(§7.6). 이름이 아니라 id로 호출한다(ARCHIVE) | 생성 시각, 상품, 시간당 가격 |
| ⑤ 고정 이미지로 부팅 | 이미지 digest와 uv lock으로 환경을 만들고 `nvidia-smi`의 driver·GPU 상품·torch·dtype·flag를 원장에 기록한다. 계획된 smoke 1건으로 정상 여부를 확인한 뒤 본 run을 시작한다 | 환경 지문 |
| ⑥ checkpoint를 N분마다 host로 회수 | 로컬 디스크에 원자적으로 저장(임시 파일 후 rename)하고 백그라운드로 host에 동기화, sha256 대조, 마지막 2개 유지. **terminate가 로컬 디스크를 지우기 때문이다.** N은 §7.2 | 회수 시각·크기·hash |
| ⑦ 결과 회수 | 모든 (arm x seed) 결과·log·ledger·state bundle을 host로 가져와 hash를 확인한다. 회수 확인 전에는 terminate하지 않는다 | |
| ⑧ id로 terminate | 마스터가 id로 종료한다. max_runtime은 안전망일 뿐이며 정상 경로는 수동 종료다 | |
| ⑨ 목록 0개 확인 | 인스턴스 목록을 조회해 0개임을 확인한다. 남으면 시간 과금이 계속된다 | |
| ⑩ 실제 비용을 원장에 기록 | 과금 시작·종료 시각, 시간당 가격, 합계를 run ID에 묶어 쓴다. **실패·취소·재시도 포함**이고 예정 상한을 실행 비용으로 쓰지 않는다([10-evolution-policy.md](/home/jimmy/repos/full-continual-learning/docs/10-evolution-policy.md) §6) | 예상 대 실제 |

**예산이 예상의 1.5배를 넘으면 정지하고 보고한다.** 같은 run의 반복 실패, 평가 결함, 비재현도 중단 조건이다(docs/10 §6, docs/09 §7).

### 7.2 checkpoint 회수 간격 N

잃을 수 있는 작업량과 전송 비용으로 정한다.

- **체크포인트 크기(새 모듈 + Adam 상태).** P1: 135M 약 64MB, 360M 약 180MB. P2: 4–8층이라 수백 MB. P5 1.7B·retrofit 14층: 약 6GB. 기반 가중치는 revision을 고정해 두므로 회수 대상이 아니다.
- **전송 비용.** 이그레스 요금은 공개 문서에 없다(OPEN-7). 소형은 무시할 수 있다고 보고 비동기 복사라 GPU 시간을 쓰지 않는다. 막는 구간(직렬화)만 비용이다.
- **Young–Daly식.** T_opt ≈ √(2·C·M). C = 직렬화로 막히는 시간, M = 인스턴스가 예기치 않게 사라지는 평균 간격. M은 미확인이라 8–72시간으로 두면 C = 5초(수십 MB)에서 약 9–27분, C = 30초(GB급)에서 약 22–66분이다.
- **결정.** N = **15분**(체크포인트 ≤ 100MB인 P1–P4), **30분**(GB급인 P5). 각 (arm x seed) unit이 끝날 때마다 추가로 회수한다. 한 번의 사고에서 잃는 최대 비용은 N/60 x 시간당 가격: main $0.31, H100 VM $1.96 정도다.

### 7.3 seed 묶음과 병렬 인스턴스

- **seed 묶음은 한 인스턴스에서 순차 실행해 준비 비용을 상각한다**(§4.5: 135M run 1건 $0.61 → 5건 $0.27). 인스턴스 1회 세션은 6–12시간 이하로 하고 unit 경계마다 재개할 수 있게 한다.
- **병렬 인스턴스는 벽시계 시간이 중요할 때만 쓴다.** 인스턴스를 하나 더 띄우는 추가 비용은 준비 시간 x 시간당 가격이다(main 약 $0.43, H100 약 $1.1). 연산 지배 대형 run(P5: run당 10시간, 9 run)에서는 병렬화의 추가 비용이 run 비용에 비해 작아 대기 시간을 줄이는 데 쓸 만하지만, 소형 run(P1: run당 약 6분)에서는 상각이 깨져 손해다.
- **한 비교 안의 run은 같은 상품에서.** 병렬화해도 한 비교(H-COMPUTE·quality–compute)의 모든 run은 같은 GPU 상품·driver·torch를 쓴다(§7.4).

### 7.4 비교 환경 고정 (H-COMPUTE·quality–compute)

**PROPOSAL.** [08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md) §6은 batch·sequence length·hardware·warm/cold state를 맞추라고 한다. 이를 확장해 **한 비교 안에서 GPU 상품(listing), driver, torch, dtype, TF32·deterministic 설정, batch 크기를 고정하고 원장에 기록한다.** 시간·계산량 비교는 장치가 다른 run을 섞지 않는다.

**ARCHIVE 근거** (둘 다 private 저장소이므로 인용은 짧게):
- melete@1d95136:docs/implementation/records/2026-10-21-neural-judgment-j1-diagnostics.md — host CPU 실행(Python 3.14.3·Torch 2.9.1+cpu)이 저장된 GPU 실행(Python 3.12.3·Torch 2.9.1+cu128)의 예측을 재현하는 점검에서 G-pair의 확률 차이가 최대 1.37e-6, 448개 중 2개가 절대 1e-6 기준을 넘어 수치 guard가 FAIL이었다(판단 범주 1,792개는 모두 같았다). 장치·런타임·flag를 맞춘 GPU 재현은 최대 4.5e-8~2.4e-7로 통과했다. 원인을 단일 요인으로 확정하지 않았다고 적혀 있다.
- melete@1d95136:docs/implementation/records/2026-10-16-neural-judgment-j1-feedback.md — CPU seed 7과 CUDA seed 11처럼 seed와 장치가 함께 바뀐 두 실험은 그 차이를 순수 seed 효과로 해석하지 않고, 한쪽의 개선이 다른 쪽에서 같은 방향으로 재현되지 않으면 일반 이득을 주장할 수 없다고 적었다.

**적용 (docs/09 §3의 정직한 상한과 일치).** 장치가 다른 run을 한 비교에 섞은 결과에는 등급 상한 문구를 걸고, 같은 장치·같은 상품에서 다시 돌린 것만 H-COMPUTE 근거로 쓴다.

### 7.5 예산 watchdog와 계정 위험

- manifest의 예상 비용을 기준으로 마스터가 정해진 간격으로 과금 누계를 확인한다. 예상의 1.5배에 닿으면 즉시 정지·보고한다. max_runtime은 서버 측 안전망이다.
- 공개 문서에 따르면 잔액이 1달러 아래로 내려가면 자동 충전을 시도하고, 실행 중 인스턴스가 15분 뒤(잔액이 −10달러에 닿으면 더 일찍) 삭제될 수 있다. **같은 계정을 다른 프로젝트와 공유하면 그쪽 지출이 FCL run을 중단시킬 수 있다**(OPEN-13, §9).

### 7.6 자동 종료 설정에서 조심할 것

공개 문서의 idle 종료는 "GPU 사용률 5% 미만이고 접속한 사용자가 없는 상태가 정해진 시간 지속될 때" terminate한다. batch=1 평가와 데이터 준비·rsync 구간은 GPU 사용률이 낮아 **유효한 run을 유휴로 오인해 죽일 수 있다.** 그래서 idle_shutdown은 30–60분으로 길게 잡고, 실행 중에는 ssh 세션을 하나 열어 둔다. 실제 안전망은 max_runtime이다. 부팅은 과금되지 않고(공개 문서) launch→running 중앙값은 4분 14초, 90%는 6분 50초 이내다(449회 관측).


**2026-11-18 갱신: 운영 절차, 승인 gate, 정지 규칙은 그대로 유지한다.** 새로 더해지는 것은 둘이다. (1) P0 UJ0 종료 gate(R01–R04)는 host에서 재현돼야 하고 runcrate는 대량 readout 전용이다. 한 비교 안의 arm은 같은 장치·같은 상품에서 돈다(§7.4). 서빙 방식을 바꾸면(HF eager 대 서버형) 같은 비교에 섞지 않는다. (2) 시간캡슐 기반 사전학습(안 2·3)은 인스턴스 1회 상한(6–24시간)을 훨씬 넘으므로 checkpoint 회수 간격(§7.2)과 자동 종료(§7.6)가 더 중요하고, 사전학습 시작 전에 승인 gate(§9)를 별도로 통과해야 한다. 새 비용은 모두 사용자 결정 gate다.

## 8. 보정 절차: P1-T04 실측으로 추정을 고친다

**PROPOSAL.** 이 추정의 폭이 큰 이유는 MFU·지연·kappa 가정 때문이며 모두 T04에서 잴 수 있다. [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md) P1-T04(spike: base model·자원)의 완료 판정은 바꾸지 않고 측정 항목만 더한다.

**1단계: host와 노트북 실측(무료).** 모델 135M·360M(가능하면 0.6B)에 대해 (a) batch=1 forward 지연(HF eager 대 compile), (b) frozen 기반 + 최소 retrofit stub(T05)의 학습 step 시간과 최대 메모리(step당 8k·16k token), (c) 관측 1건의 test-time write 지연, (d) host CPU의 학습·추론 처리율을 잰다. 결과로 t_call·t_write·kappa·e_gemm·sw·f_trav·tok_step을 교체한다.

**2단계: 사용자 비용 승인 뒤 runcrate 후보 GPU 1–2종의 짧은 microbenchmark.**

| 항목 | 내용 |
|---|---|
| 대상 | main tier 1종(RTX 6000 Ada 또는 L40S VM) + large tier 1종(H100 또는 A100 80GB). 필요하면 48GB 대안 1종 |
| 측정 | 1단계의 (a)–(c)를 같은 코드·같은 pin으로, 병렬 평가 process 수 1 / 4 / 8 / 12에서 처리량·GPU 사용률, step당 16k token 학습 처리율과 메모리, 인스턴스 준비 시간 실측. 선택: CPU 전용 인스턴스(28 vCPU·80GB 약 $0.63/h)의 batch=1 평가 지연 |
| 예상 시간·비용(ESTIMATE) | main 약 2시간 + large 약 1.5시간(준비·재시도 여유 포함). 합계 P50 약 3.7 GPU-시간, **$7.6($5.2–11)**. 상한 **$12**를 설정하고 인스턴스마다 max_runtime(main 120분, large 90분)을 둔다 |
| 승인 | 사용자 비용 승인 전에는 만들지 않는다. 실패·재시작 포함 실제 비용을 원장에 쓴다 |

**3단계: 표 갱신.** 측정값으로 §6의 가정과 표를 다시 계산하고, 갱신 전 표는 "ESTIMATE v0(2026-11-17)"로 남긴다(지우지 않는다). 측정한 t_call·kappa가 가정의 (낙관, 비관) 범위 안이면 범위를 좁히고, 밖이면 넓히며 원인을 기록한다. GPU 순위가 바뀌면 §4를 고친다. 측정 run ID·환경 지문을 원장에 묶는다.

**판정.** 보정 뒤에도 평가 처리량이 요청 수 x 지연 모델보다 크게 낮으면(예: 병렬 process 수가 vCPU 수를 따라가지 못함) 평가 harness의 배치 실행 설계(OPEN-11)를 다시 검토한다.

## 9. 계정·예산 결정 대기 (사용자 결정)

현재 사용할 수 있는 API 키는 **다른 프로젝트 계정에 속해 예산이 공유된다.** FCL 전용 키·예산을 따로 둘지는 사용자가 정한다. 결정 항목을 용도 / 유료 여부 / 예상 비용 / 무료 planB / planB의 품질 저하로 쓴다.

| 항목 | 내용 |
|---|---|
| 용도 | FCL P1-T04 클라우드 microbenchmark, 이어서 P1 sealed readout·P2 이후 학습·readout. P2부터 필요성이 커진다(§10) |
| 유료 여부 | 유료. 선불 잔액에서 시간 단위(초 단위 과금이 대부분, 일부는 분 단위 올림)로 차감한다. 잔액이 모자라면 실행 중 인스턴스가 삭제될 수 있다(공개 문서) |
| 예상 비용(ESTIMATE, NOT RUN) | T04 P50 약 $7.6($5.2–11, 상한 $12). P1 P50 $17($10–35, 135M), P1–P4 P50 $198($86–516, 135M). P5는 두 번째 모델에 따라 P50 $205(360M)–$548(1.7B)(P10–P90 $66–2,537). 이 범위는 T04 실측 전의 추정이며 승인된 상한이 아니다 |
| 무료 planB | host CPU(계약·E2E·소규모 평가) + 노트북 GPU(12GB, 간헐 연결). P1 135M은 약 20 run에 P50 약 7.7시간(P10–P90 1.7–37시간)으로 시작할 수 있다 |
| planB의 품질 저하 | 효율 쪽 손해가 크다: P2 학습은 노트북 환산 P50 약 82시간(연속 약 3.4일), 360M 이상은 step당 token 축소·0.6B 이상은 불가, 연결 단절 시 재시작. 시간에 맞추려고 seed·arm을 줄이면 sealed readout이 INCONCLUSIVE가 되기 쉬워 등급 3 확증이 약해진다. 과학적 내용(실험 설계)은 같다. host 직렬 readout은 호스트 메모리 압박 속에서 한 대를 점유한다 |
| 결정할 것 | (a) T04 microbenchmark 승인 여부와 상한, (b) FCL 전용 키·예산(권장: 클라우드를 쓰기로 하면 전용 키와 상한을 따로 둔다. 공유 잔액에서는 다른 프로젝트 지출이 FCL run을 끊을 수 있고 반대도 가능하다), (c) phase별 클라우드 상한은 T04 실측 뒤 phase 시작 때 따로 승인 |

## 10. D-04·D-01·D-12 개정 추천 요약

모두 **OPEN**이며 결정자는 사용자다. 편집안은 docs/09 §10에 EC로 제안한다.

**D-04 (retrofit 학습의 계산 장소·시간 상한).** 현재 추천은 "T04 실측 뒤 (b)의 시간 상한을 먼저 승인. (c)는 P5 전까지 보류"다. 작업량 추정에 근거해 이렇게 바꿀 것을 제안한다.

- (b) 노트북으로 P1 135M 개발·T09를 시작하되 시간 상한과 재개(checkpoint) 조건을 승인한다.
- (c)는 두 단계로 나눠 묻는다. ① T04의 소액 microbenchmark(2종, P50 약 $7.6, 상한 $12)는 지금 승인 요청. ② 학습·readout용 (c)는 T04로 보정한 **phase별 비용 상한을 phase 시작 때 따로 승인**한다.
- "P5 전까지 보류"는 근거가 약해 철회를 제안한다. P1 비용은 작지만(P50 약 $17, ESTIMATE) 노트북은 P2 학습만 P50 약 82시간(연속 약 3.4일)이고 12GB·간헐 연결이라 P1→P2 경로를 막을 수 있다. 클라우드가 실질적으로 필요해지는 지점은 P5가 아니라 **P2(또는 P1 sealed readout)** 다.

**D-01 (P1 base model).** 추천 (a) SmolLM2-135M은 바꾸지 않는다. 후보 점검 결과(§6.2)를 근거로 남긴다. 새 후보 Granite-4.0-350M-Base·Qwen3.5-0.8B-Base는 P1 후보가 아니라 OPEN 후보다.

**D-12 (두 번째 base model·크기).** 추천(P4 종료 재검토에서 결정)은 바꾸지 않는다. 후보에 Granite-4.0-350M-Base(한국어·dense·Apache-2.0)와 1.7B급을 올리고 비용 영향을 병기한다: P5가 1.7B이면 P50 $548($141–2,537), 360M이면 P50 $205($66–791)(ESTIMATE).


### 10-1. 2026-11-18 갱신: 결정 후보와 요약 표

모두 **OPEN**이며 결정자는 사용자다. 번호는 [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md) §10의 결정 번호다. 이미 있는 결정과 겹치는 후보는 그 번호(D-20·D-29·N-11)를 쓰고 같은 번호의 행이 여럿일 수 있다([id-map.tsv](/home/jimmy/repos/full-continual-learning/research/2026-11-18-blueprint-et-design/id-map.tsv)).

| ID | 결정 | 선택지 | 추천 | 비용 발생 | 결정자 |
|---|---|---|---|---|---|
| D-46 | P0 대량 readout의 서빙 방식과 frozen LLM 크기 | (a) HF eager 8B급(P50 $864). (b) 서버형 continuous batching(P50 $389). (c) 4B급 복제·보조 run(P50 $468). (d) 서버형 + 4B급($210) | (b)를 기본 검토하되 「같은 CLI·session 프로토콜·runtime 경로」 동등성(OPEN-11)과 NP-1 hook 호환을 P0-T04에서 확인한 뒤에 정한다. 주 모델은 8B급 유지 | 있음 | 사용자 |
| N-11 | P0 클라우드 비용 상한과 FCL 전용 키·예산(N-11) | (a) P0-T04 실측으로 처리량을 보정한 뒤 phase 상한을 승인. (b) 지금 상한 승인 | (a). 상한 후보는 보정 뒤 P90 | 있음 | 사용자 |
| D-29 | 시간캡슐 기반 확보 안 | (a) 공개 모델 사용(P50 약 $7). (b) 소형 자체 사전학습(P50 약 $3,165, 한 노드 약 5.3일). (c) 중형 자체 사전학습(P50 약 $43,496, 한 노드로 비현실적) | (a). (b)(c)는 공개 모델의 마감·누수·라이선스로 ET-3·4가 막힐 때만 | 있음(b, c) | 사용자 |
| D-20 | P1 base 크기(D-01과 연결) | (a) 135M 유지. (b) 1.7B급(P50 +약 $22). (c) 4B급(P50 +약 $56, 단 48GB 초과) | (a). 시간캡슐 기반은 P5부터 쓴다 | (b)(c)에서 증가 | 사용자 |
| D-47 | 자체 사전학습용 다중 GPU 노드와 월 약정 | (a) 쓰지 않는다. (b) 안 2에서만 4장 이상 노드 1개 | (a). 안 2·3을 택할 때 다시 묻는다 | (b)에서 있음 | 사용자 |

**D-04·N-11과의 관계.** D-04(retrofit 학습의 계산 장소·시간 상한) 개정 추천(위 §10)은 그대로다. P0는 학습이 없지만 클라우드 비용이 가장 먼저 크게 생기는 phase라서 D-04의 「phase 시작 때 따로 승인」 원칙을 P0에도 적용한다(N-11). N-11(FCL 전용 runcrate 키·예산)은 P0에서 더 급해졌다: 공유 계정에서는 P0의 대량 readout이 다른 프로젝트의 지출과 같은 잔액을 쓴다.

**2026-11-18 갱신 요약 표 (P50, 괄호는 P10–P90).**

| 항목 | 11-17 표 | 11-18 갱신 |
|---|---|---|
| 상품 목록과 가격 | 192개, 주력 $1.23, H100 1장 VM 하한 $3.91 | 177개, 주력 $1.23, H100 1장 VM 하한 $4.72. 어제 표를 오늘 가격으로 재계산해도 변화 −0.0% ~ +0.3% |
| P1–P4 합계(135M 경로) | $198($86–$516) | 변화 없음. 새 NP arm·ET 단 추가분이 phase마다 더해진다(§6.10) |
| P0(NP) | 없음(새 phase) | runcrate $864($395–$2,059), host UJ0 gate 벽시계 약 19.2시간 |
| 시간캡슐 기반 확보 | 없음 | 공개 모델 약 $7, 소형 자체 사전학습 약 $3,165, 중형 약 $43,496 |
| P5(두 번째·더 큰 모델) | $205(360M) – $548(1.7B) | 시간캡슐 7.24B 기준 PAPER-5 $787 / $2,593 / $10,583, retrofit이 지배 |
| P6(ET 최종) | 없음(새 phase) | PAPER-6 $230 / $1,010 / $3,661 |

## 11. OPEN 목록

| ID | 내용 |
|---|---|
| OPEN-1 | 공개 문서(containers)와 상품 정보(vm 164·container 28)가 다르다. VM의 사용자 가시 차이는 미확인. ARCHIVE의 VM 실측(Ubuntu 22.04·driver 570.148.08·Docker `--gpus`)을 재확인하지 않았다 |
| OPEN-2 | `port_mapped`의 의미가 공개 문서에 없다 |
| OPEN-3 | 사용자 정의 Docker 이미지(digest 고정)가 container 상품에서 되는지 미확인 |
| OPEN-4 | 영구 볼륨(10–10,000GB, 0.03 USD/GB-month, `/workspace`, terminate 뒤 유지, 한 번에 한 인스턴스)이 vm 상품에서도 되는지, 입출력 속도. 되면 체크포인트의 2차 사본으로 쓸 수 있다(10GB 볼륨 약 $0.3/월) |
| OPEN-5 | API의 자동 종료 필드명. 공개 CLI는 `--max-runtime`(5분–168시간)·`--idle-stop`(5분–24시간)로 같은 기능을 제공한다. API 레퍼런스 페이지는 이번에 읽지 못했다 |
| OPEN-6 | spot 상품의 존재 범위(공개 문서가 개념만 서술). 이 계획은 spot을 쓰지 않는다 |
| OPEN-7 | 데이터 전송·egress 요금은 어떤 공개 문서에도 없다 |
| OPEN-8 | stopped(일시 정지, 자원 유지) 상태의 과금·로컬 디스크 보존 여부. ARCHIVE는 '중지는 terminate뿐'이라고 기록 |
| OPEN-9 | NVIDIA 수치 중 유도치(H100·H200 dense = sparsity/2, B200 per-GPU, 노트북 GPU)·미조회(A100 40GB 대역폭)·미확인(상품 변종, L40 BF16)이 있다. A10·A40·A4000·A5000·L4·V100·GH200·Gaudi2는 비교에서 제외했다 |
| OPEN-10 | 추정의 핵심 가정(forward 지연, write 지연, kappa, MFU, 병렬 process 유효 수)은 모두 미측정이다. T04로 교체한다 |
| OPEN-11 | 대량 readout을 빠르게 하는 배치·병렬 session 실행이 "같은 CLI·같은 session 프로토콜·같은 runtime 경로"와 동등함을 보이는 방법(P1-T12 설계). 단일 session 직렬이면 §6.5의 지연 모델이 시간을 정한다 |
| OPEN-12 | CPU·GPU 장치별 Contract 허용오차(P1-T10 재시작 동등 등)를 어떻게 선언할지 |
| OPEN-13 | 공유 계정에서 잔액 부족 시 인스턴스가 삭제될 수 있다. FCL 전용 키·예산 결정(§9)과 연결 |
| OPEN-14 | seed 수·world 수(D-05), 세계 token 규모(T06), P2 recurrence 학습 규모, P3 시행착오 규모, P4 teacher 크기, P5 token 규모는 가정이다 |
| OPEN-15 | 새 후보 Granite-4.0-350M-Base·Qwen3.5-0.8B-Base와 Titan-Llama pin의 호환(P1-T05에서만 확인), Qwen3 계열(QK-norm)의 pin 호환 |
| OPEN-16 | 이 문서의 표를 만든 계산 스크립트와 TSV를 저장소(예: `experiments/compute-plan/`)에 두고 실측으로 갱신할지 |
| OPEN-17 | ARCHIVE 운영 사실(이름 경로 401, terminate만, 월 약정 0–8% 등) 중 스냅샷·공개 문서와 다른 것: 월 약정은 스냅샷 1/3/6/12개월 5/8/11/15%·공개 문서 최대 15%이므로 스냅샷 수치를 쓴다 |


**2026-11-18 갱신 OPEN.** 위 OPEN-1~17에 이어진다.

| ID | 내용 |
|---|---|
| OPEN-18 | P0 host 처리량(8B 4-bit GGUF와 1.7B HF의 CPU token/s)과 runcrate 8B HF 서빙 처리량(prefill MFU, decode 대역폭 효율, 동시 sequence 수)은 모두 가정이다. P0-T04와 microbenchmark로 교체한다 |
| OPEN-19 | NP-1 hook(activation 추출·주입)의 forward 배수 1.05–1.40과 hidden-state kNN 저장·검색 비용은 가정이다. llama.cpp의 hidden-state 추출 경로는 확인되지 않았고 HF backend를 전제한다 |
| OPEN-20 | 서버형 continuous batching이 NP 대역의 순차 write·hook과 호환되는지, 「같은 CLI·session 프로토콜」 동등성(OPEN-11)을 어떻게 보일지 |
| OPEN-21 | Talkie 13B의 층·hidden 구조를 확인하지 못해 가정했다. GPT-1900 D34는 value embedding 때문에 파라미터 3.29B 중 FLOP에 드는 본체를 약 2.1B로 환산했다 |
| OPEN-22 | 4장 이상 노드를 여러 개 묶는 다중 노드 사전학습이 runcrate에서 가능한지(공개 문서 미확인). 오늘 H100은 4장 VM만 있고 8장은 없다. A100 80GB 8장 VM이 대안이다 |
| OPEN-23 | 시간캡슐 기반 모델의 라이선스(TypewriterLM 미명시 등)와 Ranke-4B의 공개 여부는 조사 기록이 다룬다. 비용이 아니라 사용 가능 여부가 ET-3·4의 선결이다 |
| OPEN-24 | 이 절의 계산 스크립트(w6_1118.py 등)와 TSV를 저장소에 둘지(OPEN-16과 같은 결정) |

## 12. 변경 기록

| 날짜 | 변경 | 이유 | 영향 |
|---|---|---|---|
| 2026-11-17 | 이 문서 신설(초안, PROPOSAL/ESTIMATE/NOT RUN) | 사용자 요청: runcrate 클라우드 GPU를 과하지도 모자라지도 않게 쓰는 계획. 판단 기준을 시간당 가격이 아니라 유효 실험 1건의 총비용으로 | 새 문서. [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md) §10 자원 표·D-04·D-01·D-12·§11 개정안은 별도 편집으로 제안(전부 OPEN). phase·데모·gate·상한·미루는 것은 바뀌지 않음 |
| 2026-11-18 | 「2026-11-18 갱신」 표기의 문장·표·절을 더함(§4.7, §5.4, §6.7–§6.11, §10-1, OPEN-18~24). 11-17의 수치와 표는 고치지 않았다 | 새 로드맵(P0(NP)–P6(ET), 논문 PAPER-0~6)에 맞춰 계산 자원을 붙임. 사용자 요청: runcrate를 쓰는 실험 계획 포함. 오늘 스냅샷(177개, 가격 거의 그대로) 반영 | P0·시간캡슐 확보·ET·PAPER-k 비용이 새로 생김(ESTIMATE / NOT RUN). 새 결정 후보 D-46~05. 11-17의 D-04 개정 추천과 N-11은 유지 |
