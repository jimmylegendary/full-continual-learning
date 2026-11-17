# docs/15 계산 계획 갱신의 부록: 색인·새 참고문헌·조사 출처 (2026-11-18)

**상태 라벨:** 설계 작업 기록의 부록(PROPOSAL / OPEN / NOT RUN)이다. [15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md)를 개정한 역할의 변경 요약 끝에 있던 세 부록을 이곳에 둔다. 초안 원문이므로 가칭(DC-·NEW-로 시작하는 번호)을 그대로 두었고, 최종 번호는 [id-map.tsv](/home/jimmy/repos/full-continual-learning/research/2026-11-18-blueprint-et-design/id-map.tsv)와 [2026-11-18-blueprint-et-design.md](/home/jimmy/repos/full-continual-learning/research/2026-11-18-blueprint-et-design.md)의 대응표에 있다. 작성일 2026-11-18.

## 부록 A. 색인

### 소유 정의 위치

| 소유 정의(지시문 §3-2) | 위치 |
|---|---|
| token·GPU-시간·비용 수치 | docs/15 §4.7(스냅샷·가격), §6.7(P0), §6.8(시간캡슐 확보), §6.9(시간캡슐 retrofit·ET run), §6.10(P1 base 비교와 phase별 추가분), §6.11(PAPER-k 묶음표) |

### 이 초안이 정의한 ID

| ID | 뜻 |
|---|---|
| DC-W6-01 ~ 05 | 사용자 결정 후보(가칭): 서빙 방식·frozen LLM 크기 / P0 클라우드 상한과 N-11 / 시간캡슐 확보 안 / P1 base 크기 / 자체 사전학습 노드·월 약정 |
| OPEN-18 ~ 24 | 갱신 OPEN: host·서빙 처리량 가정, hook 배수, 서버형 서빙 동등성, 모델 구조 가정, 다중 노드, 라이선스, 스크립트 보관 |
| PAPER-k 묶음표 | docs/15 §6.11의 표 이름(docs/19가 이 이름으로 가리킨다) |

### 남의 정의를 가리킨 곳

| 가리킨 것 | 소유 |
|---|---|
| P0 실행 행렬(R01–R16: 세계 수·arm·checkpoint·probe·호출·token), host gate 처리량 가정, ET-3p 설계, 실행 위치 규칙 | docs/18 |
| ET 단 정의·phase 대응, stream 규모(항목·token·checkpoint·probe·run 수) | docs/17, docs/09 |
| 논문별 실험 설계 | docs/19 |
| 시간캡슐 모델의 크기·corpus·학습 token·라이선스·공개 여부 | 조사 기록(시간캡슐 모델 현황 표) |
| 결정 D-04, D-01, N-11, docs/09 §10의 비용 수치 | docs/09, 11-17 감사 |

### 가칭 목록

DC-W6-01 ~ 05(5개). 새 평가 family 없음. 새 참고문헌 NEW-W6-01(1개).

## 부록 B. 새 참고문헌

| id | title | category | date_note | url | code_url | status | note |
|---|---|---|---|---|---|---|---|
| A71 (가칭 NEW-W6-01) | Qwen3-4B 모델 카드와 config.json | code | 2025; 구조 확인 2026-11-18 | https://huggingface.co/Qwen/Qwen3-4B | | metadata-checked | config.json과 카드 일부만 확인(36층, hidden 2560, ffn 9728, GQA 32/8, vocab 151936, tied embedding, Apache-2.0). P1 base 비교(§6.10)의 구조 입력이다. 가중치는 내려받지 않음 |

## 부록 C. 조사 출처

접근일은 모두 2026-11-18이다. 확인 수준은 `직접`(해당 파일을 직접 읽음)과 `요약`(조사 기록의 요약을 인용)이다.

| URL 또는 출처 | 읽은 범위 | 확인 수준 |
|---|---|---|
| https://huggingface.co/Qwen/Qwen3-4B | config.json 전체와 카드의 라이선스·파라미터 수 줄 | 직접 |
| 조사 기록의 시간캡슐 모델 현황 표(S146, 03, 04, 05, 06의 출처) | 크기·층 구조·corpus·학습 token·비용 앵커(TimeCapsuleLLM v2 H100 117시간 약 341달러, Ranke-4B 사전 공개 노트의 GH200 시간) | 요약 |
| docs/17, docs/18의 입력표(stream 규모, P0 실행 행렬) | 표 전체 | 직접 |
| runcrate 상품 스냅샷 2026-11-18과 2026-11-17(로컬, 비공개) | types_all(상품 목록)과 instances 건수만. 잔액은 읽지 않음 | 직접 |
| 2026-11-17 공개 입력표(research/2026-11-17-design-review/ W5-*.tsv 7개) | 재현 대조 | 직접 |
