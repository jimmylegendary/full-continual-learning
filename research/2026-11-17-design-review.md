# 델타 설계 반영 감사와 계산 계획: 11-12 감사 뒤의 자료는 설계에 들어갔는가 (2026-11-17)

**요청 (USER, 2026-11-17):** 「오늘 날짜 기준으로 다시 검토해봐. 그리고 full continual learning repo도 업데이트해서 반영. 그리고 지금 우리 host에 runcrate 사용환경 있을거야. melete를 앞으로 만들고 학습시 사용한다면 어떻게 쓸 수 있을지, 비용효율을 위해서 너무 과도한 사양이 아닌, 그렇다고 minimum으로 품질이나 효율을 떨어트리지 않으면서 쓴다면 어떻게 쓸 수 있을지 계획해봐」 원문과 항목별 해석은 [2026-11-17-discussion.md](/home/jimmy/repos/full-continual-learning/sources/sync/2026-11-17-discussion.md)와 원장 U17-01–U17-08에 있다.

**답 (요청 3개).**

| 요청 | 결과 | 어디 |
|---|---|---|
| 재검토 | 11-12 감사(커밋 2ecf3e0) 이후 들어온 자료를 항목 단위 원장 434개로 대조했다. 판정은 reflected 106 / partial 181 / not-reflected 76 / conflict 16 / out-of-scope 22 / 결정 대기 33이다. 사용자 원문(USER)으로 확인되는 항목은 20개뿐이고 나머지는 ChatGPT의 제안·재구성·보고 이관이다. 설계 본문에 중복·충돌·누락이 있는 곳은 편집 주석으로 표시했다 | §2–§3, [ledger-delta.json](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/ledger-delta.json) |
| 저장소 반영 | 편집 블록 105개 중 86개를 적용하고 15개를 고쳐 적용했고 4개를 제외했다(3개는 다른 블록에 합쳤고 1개는 중복). 통합 담당(W6)의 편집 16개(README·manifest·출처·참고문헌·계산 계획 등)를 더했다. 설계 문서 12개에 주석·후보를 넣고 새 문서 docs/15를 만들었다. 문서·계획만 바꿨고 학습·GPU·비용·백서 재생성·외부 발송은 0회다 | §4, [edits-applied.tsv](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/edits-applied.tsv) |
| runcrate 계획 | 횡단 문서 [15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md)를 만들었다. 별도 인프라 phase가 아니라 P1–P5에 자원을 붙인다. 판단 기준은 시간당 가격이 아니라 유효 실험 1건의 총비용이다. 모든 수치는 ESTIMATE이고 NOT RUN이며 결정은 사용자 몫이다 | §6, §7 |

## 1. 방법

- **범위.** ChatGPT hourly 「FCL 연구 기록 동기화」 작업의 커밋 5개(aa1413d..280dc9a, 2026-11-14~11-17)가 추가·수정한 15개 파일(docs/13·14, SYNC_POLICY.md, research/2026-11-16·17-*, references 3개, sources/sync/*, README·AGENTS 수정), 사용자 공유 링크 연구 카드, 2026-11-17 사용자 원문이다. 11-12 감사 때의 설계 문서 01–12와 로드맵은 대조 대상이다.
- **입력 커밋.** 280dc9a(= 원격 main, 2026-11-17). 작업은 별도 worktree의 branch `design/2026-11-17-review`에서 했고 push·rebase·병합은 하지 않았다.
- **판정 기준.** 원장의 status는 감사 시점(편집 반영 전)의 판정이다: reflected(반영·일치), partial(일부), not-reflected(반영 위치 없음), conflict(다른 문서·원문·현재 상태와 충돌하거나 낡음), out-of-scope(설계 반영 대상이 아닌 관찰), pending(사용자 결정 대기). 증거 라벨은 USER·USER-HYPOTHESIS·PROPOSAL·LITERATURE·ARCHIVE·OPEN·NOT RUN이고 계산 추정은 ESTIMATE다. USER 원문은 [2026-11-16-discussion.md](/home/jimmy/repos/full-continual-learning/sources/sync/2026-11-16-discussion.md)의 블록 2개와 11-17 블록뿐이다. ChatGPT의 정리는 재구성이다. 편집 블록의 '없다·반영돼 있지 않다'는 기준 커밋 280dc9a의 상태이며 이 검토의 편집이 들어간 뒤에는 달라질 수 있다.
- **워커 구성.** 병렬 워커 6명이다.

| 워커 | 몫 | 산출 |
|---|---|---|
| W1 | docs/13의 정의·수학 §7.1–7.5, schema-decomposition 보충 참고문헌 | 원장 D13·REF13 112, 수학 점검, 편집 33 |
| W2 | docs/14의 CRUD·두 가지 삭제·controller·실험 배치·Ali 공동논문 초안 | 원장 D14·SYN·X13·REF14 127, 대응표·배치표·초안 점검, 편집 27 |
| W3 | 11-16·17 연구 기록과 참고문헌(Sleep-time·SoMem·증거 연계 read·Tian 중복) | 원장 R16·REFST 102, 후보 행 36, 편집 21 |
| W4 | 사용자 공유 링크 카드 98장의 재분류와 논문 확정 | 원장 TI 10, 후보 행 5, 편집 9 |
| W5 | runcrate 계산 계획 | docs/15 본문, 추정 TSV 7개, 편집 15 |
| W6 | 통합: 동기화 정책·사용자 원문·대기 항목 감사, 편집 적용, 원장 병합, 기록 | 원장 SYNC·U17·PEND·C15 83, 이 문서 |

- **검증 도구와 한계.** 저장소 쓰기는 W6만 했다. 편집 블록은 Edit 도구와 같은 규칙(앵커가 현재 본문에 정확히 한 번 있어야 함)을 지키는 적용 스크립트(저장소 밖)로 넣었다. 블록 105개의 본문을 손으로 다시 입력하면 전사 오류 위험이 커서 스크립트를 썼고, 합치거나 고친 블록은 [edits-applied.tsv](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/edits-applied.tsv)에 이유를 적었다. `tools/validate_docs.py`는 `/home/jimmy/repos/full-continual-learning/…` 절대 링크를 다른 위치의 checkout에서 모두 미해결로 판정하므로(§3 남은 정정) 접두를 worktree로 바꿔 해석하는 wrapper로 같은 검사를 했다.

## 2. 수치

| 원장 | 담당 | 항목 | reflected | partial | not-reflected | conflict | out-of-scope | pending |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| D13 | W1 | 94 | 26 | 46 | 17 | 4 | 1 | 0 |
| REF13 | W1 | 18 | 3 | 4 | 9 | 1 | 1 | 0 |
| D14 | W2 | 79 | 19 | 47 | 8 | 2 | 3 | 0 |
| SYN | W2 | 10 | 3 | 6 | 1 | 0 | 0 | 0 |
| X13 | W2 | 21 | 5 | 12 | 4 | 0 | 0 | 0 |
| REF14 | W2 | 17 | 6 | 3 | 8 | 0 | 0 | 0 |
| R16 | W3 | 88 | 16 | 47 | 10 | 3 | 12 | 0 |
| REFST | W3 | 14 | 0 | 0 | 11 | 3 | 0 | 0 |
| TI | W4 | 10 | 0 | 5 | 3 | 0 | 2 | 0 |
| SYNC | W6 | 33 | 20 | 6 | 1 | 3 | 3 | 0 |
| U17 | W6 | 8 | 8 | 0 | 0 | 0 | 0 | 0 |
| PEND | W6 | 33 | 0 | 0 | 0 | 0 | 0 | 33 |
| C15 | W6 | 9 | 0 | 5 | 4 | 0 | 0 | 0 |
| 합계 | | 434 | 106 | 181 | 76 | 16 | 22 | 33 |

- **USER 원문**: SYN 10 + SYNC 2 + U17 8 = 20개. docs/13 내용에 대한 사용자 원문 블록은 저장소에 없다(D13의 USER-verbatim 0).
- **편집**: W1–W5 블록 105개 = 적용 86 + 수정 적용 15 + 제외 4. W6 편집 16개(EW6-01–16)는 모두 적용. 원장 항목 중 편집이 걸린 것은 307개다.
- **새 파일**: docs/15, sources/sync/2026-11-17-discussion.md, references/shared-links-2026-11-17.md, 이 문서와 폴더 research/2026-11-17-design-review/의 안내 [README.md](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/README.md). references/catalog.tsv에 후보 33행(100 → 133행)을 더했다.

## 3. 핵심 발견

반드시 볼 10개 주제의 판정·근거·반영 위치다. 근거 항목 id는 원장에서 찾는다.

1. **두 가지 「삭제」: 분리돼 있지 않다(conflict, D14-006).** docs/07 §7은 한 문장에서 eviction(용량 정책)과 '삭제'(= §8의 source 삭제)를 섞고, docs/09의 '삭제' 39회는 모두 source 삭제인데, docs/14·증거 연계 보충·Sleep-time 교차 검토는 Delete/Retain 아래에 '삭제된 source'를 함께 둔다. 사용자의 Delete는 "무한히 증가하는 지식에 대해서 망각의 비용을 어떻게 치뤄야할지"(USER)로 source 삭제가 아니다. 평가 gate도 다르다(Efficacy 대 Contract·Product). 학습 방법으로서의 가중치 삭제(공유 링크 논문 T2)는 세 번째 뜻이다.
   → [07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md) §7(E14-01 용어 한정, E14-02 구분표·쓰기 규칙), [08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md) §1(E14-03), [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md) P1-T13 주(E14-07), [14-schema-lifecycle-crud-and-joint-paper.md](/home/jimmy/repos/full-continual-learning/docs/14-schema-lifecycle-crud-and-joint-paper.md) §4(E14-20: 세 뜻을 한 주석으로 합침). 결정 대기: N-2.
2. **CRUD와 controller: P1 규칙형 controller v0는 Read·Update만 덮는다(partial).** fast는 Read, learn은 Read+Update, deep은 Read+Update+추가 계산이다. Create는 P3 accommodation부터, Delete/Retain은 측정이 P1부터이고 정책은 P4부터라고 대응시켰다(제안). 사용자의 low-rank expert in-place update·create와 docs/05의 CMS 분기(B_j=0)는 형태(기반 + gate된 low-rank 합)가 같지만 색인 축이 다르다(j는 갱신 시간척도, 사용자의 expert는 문맥으로 선택·할당되는 기능 단위). NMM은 binding이라 expert로 읽지 않는다. 사용자 원문의 "적합한 schema를 못찾으면 create"는 docs/14가 '구조적 새로움이 확인될 때만 create'로 좁혀 충돌한다(conflict, D14-021). docs/05 §4의 v0(학습형 head)와 docs/09 P1의 규칙형 v0는 이름이 같다.
   → [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md) §1.1의 U-T12 행(E14-05)과 §4-1 CRUD 대응(E14-06), [05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §4 이름 정리(E14-10: P1 규칙형을 'v0-rule'로 부름)·§5 low-rank expert 관계(E14-11), [11-research-agenda.md](/home/jimmy/repos/full-continual-learning/docs/11-research-agenda.md) §2(E14-12), [14-schema-lifecycle-crud-and-joint-paper.md](/home/jimmy/repos/full-continual-learning/docs/14-schema-lifecycle-crud-and-joint-paper.md) §3(E14-18). 결정 대기: N-4, D-14.
3. **docs/13의 정의·수학 §7.1–7.5: 틀린 명제는 없지만 전제가 부족하다.** 직접 유도와 소규모 numpy 점검(모델 효용 근거가 아님)의 판정은 7.1 정확(전제 보강) / 7.2 조건 보강 필요 / 7.3 조건 보강 필요 / 7.4 조건 보강 필요 / 7.5 정확(무오류 회상 한정)이고 틀림 0, 검증 불가 0이다. 보강한 조건: 7.2는 ReLU 반례·plain SGD 한 step 한정(Adam은 방향이 다름)·minibatch 기대값의 노이즈 항·다단계 K² 누적, 7.3은 bit 동일성이 결정적 실행을 전제하므로 상태 층(byte 해시)과 출력 층(허용오차 ≥ noise floor ν)을 나눌 것, 7.4는 soft mixture에서 δ가 정의되지 않으므로 볼록 손실의 대체 식이 필요함, 7.5는 근사 회상에 rate–distortion·Fano의 별도 한계가 있음. 정의 쪽에서는 §1의 「사용자 제안」과 가설 1–4가 사용자 원문이 아니라 재구성이고(D13의 USER-verbatim 0), 가설 1(여러 schema가 엉킴)이 원문이 있는 U-T06(하나의 schema → sub-schema 분화)과 표현이 충돌한다(D13-009). 설계 본문과의 연결에서는 docs/06 §3의 빠른 업데이트 식이 감쇠·momentum을 γ로 gate하지 않아 γ=0인 schema도 바뀌므로 docs/13 §9.1의 격리 주장과 충돌한다.
   → [13-schema-decomposition-and-interference.md](/home/jimmy/repos/full-continual-learning/docs/13-schema-decomposition-and-interference.md) 주석 17(E13-01–E13-17), [06-mathematical-framework.md](/home/jimmy/repos/full-continual-learning/docs/06-mathematical-framework.md) 기호 대응표(E13-23)·감쇠 주(E13-24)·신설 §11 명제 A–E(E13-25), [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md) P1-T10 허용오차·noise floor(E13-28)와 P1-T11 검사 후보(E13-29), docs/01·03·04·05·07·11의 대응 주석. 결정 대기: N-7, N-9.
4. **실험 배치: 새 phase 없이 기존 UJ의 판독으로 넣는다.** 실험 A·E는 UJ2, C는 UJ1·UJ2, D는 UJ1·UJ4, CU는 UJ1·UJ3, R은 UJ3의 판독이다. P1에 더하는 것은 계측 열 1개, resume 후 update 동등 Contract 테스트 1개, 새 학습과 보존의 쌍 보고 서식 1개뿐이다. 새 arm(`ftall`, `adapters`, `sel-*`)은 P2, Create arm 4종은 P3, eviction 2–3종은 P4에서 처음 넣는다. docs/08에는 F01–F21이 있으나 docs/09는 F01–F12만 배치한다. 충돌: 실험 B(post-training 분기)는 P5 '미루는 것'과 모델 1종 상한에 걸리고, D의 정책 비교는 11-12 감사 §5 #17이 미결로 남긴 질문이다. 가장 무거운 축은 실험 E의 depth 격자다. 계산 규모는 docs/15 §5.3·§6에서 ESTIMATE로 가늠했다.
   → [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md) §6-1(E14-08), [08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md) §2-2의 제안 family F22·F23·F24(E14-04), docs/13 §10·docs/14 §8의 위치 주석(E14-16·E14-25·EC-13·EC-14). 결정 대기: N-5.
5. **Ali 공동논문 초안의 상한: 초안은 현재 설계 단계(등급 0)보다 강하게 읽힌다.** 16항목 점검에서 상한을 넘는 표현 7건(제안 문장 3개, 흐름의 공통 단위와 공동 연구 질문, 제안문 둘째·셋째 문장), 주의 4건, 적합 5건, 누락된 문구 4건(현재 상태 0회, 단순 대조 약속, 등급 약속, 깊이 축)이다. MIRAS의 retention은 공개 PDF 발췌 범위에서 순환 memory 갱신의 retention gate이며 schema·artifact 단위의 보존 예산이 아니므로 '이미 다뤘다'로 읽히지 않게 한정했다. 초안은 바꾸지 않았고 수정 문안은 삽입 주석으로만 냈다. 초안은 미발송이며 이 검토도 발송하지 않았다. 사용자가 U-T09에서 전한 Ali의 관심 축(loop·MoD·MoR·depth attention)은 초안에 없다.
   → [14-schema-lifecycle-crud-and-joint-paper.md](/home/jimmy/repos/full-continual-learning/docs/14-schema-lifecycle-crud-and-joint-paper.md) §3·§4·§5·§7 주석(E14-19, E14-21–E14-24), docs/10 §8-1(E14-15), [schema-lifecycle-2026-11-16.md](/home/jimmy/repos/full-continual-learning/references/schema-lifecycle-2026-11-16.md)(E14-26). 결정 대기: N-6.
6. **Sleep-time·SoMem·recursive state capacity: 핵심 문서에 반영이 없다(not-reflected).** 읽기에 충분한 상태와 이후 갱신에 충분한 상태를 가르는 구분이 docs/01–12에 없고, 복원 수준의 단서(docs/07 §5의 읽기 전용 복원 대 이어서 학습할 복원, F12, P4 보장)만 있다. arXiv:2611.13760의 recursive는 token 시계 위의 상태 갱신이라 docs/07 §1의 recursion index가 아니므로 이름 혼동을 막는 시계 구분 문장을 모든 편집에 넣었다. 연구 기록의 해석은 대체로 맞고, 논문 본문 대조로 조건을 더 정확히 적었다(사건 질의 오차는 log-확률 오차, Θ(log(1/ε))는 2-state, 생성 하한은 nondegenerate 2-state·가중치 고정·결정적 갱신 전제, §6.4가 2-state 초과를 열린 문제로 둠). 논문은 schema·continual learning을 다루지 않는다. SoMem은 외부 문서 memory의 근거 보존 재조직이며 MIRIX-2.0의 AutoDream·A03의 Dreaming과 이름만 비슷하다.
   → [07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md) §5 읽기 충분 상태(ER-01)·§7 증거 계보와 색인 재구축(ER-08), [08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md) F24 연속 갱신 뒤 읽기 보존(E14-04에 합침)·§6 비용 항 후보(ER-21), [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md) P2·P4의 후보 readout(ER-03·ER-04: 측정만, 종료 gate·등급 판정 제외), [05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §11 용어 구분(ER-05). 결정 대기: N-5.
7. **증거 연계 read(WikiTrace·HiVe-Mem): 연구 보충 기록과 docs/14의 한 줄에만 있다(partial).** docs/14 §5 본문의 Read 흐름에는 원본 근거를 되짚는 단계가 없고, docs/07의 provenance는 입력 쪽(root, generated≠observed)만 반영돼 있다. 외부 agent memory를 neural schema 지속학습과 동일시한 문장은 찾지 못했다. 두 논문은 저자 초록 수준의 확인이며 재현하지 않았다.
   → [03-foundations.md](/home/jimmy/repos/full-continual-learning/docs/03-foundations.md) §6 범주 명시(ER-06), [14-schema-lifecycle-crud-and-joint-paper.md](/home/jimmy/repos/full-continual-learning/docs/14-schema-lifecycle-crud-and-joint-paper.md) §5(ER-07), docs/07 §7(ER-08), docs/08 §4 강한 참고 대조 후보(ER-09).
8. **과장 점검: 설계 본문에는 과장이 없고 연결 공백이 있으며, 연구 기록 안에 정정이 필요한 곳이 있다.** docs/03·11에는 11-16 SBL 보고와 영향 가설이 거의 연결돼 있지 않다. 영향 가설 기록은 조건부·재사용 금지 문장이 충분하다. 정정 필요: 보충 선별 기록 §3이 docs/05·08·14 반영을 현재형으로 서술했으나 280dc9a에서 05·08은 바뀌지 않았다(R16-085), 'Tian 신규 발견'은 저장소 기준 신규가 아니다(R16-003), '8건 모두 개정일 독립 확인'은 Continual-ARC v3(2026-11-15)를 놓쳤다(R16-038). docs/13 §1의 'Melete는 … 제한한다'(L34)와 docs/14의 제안 문장은 설계 목표를 현재형으로 쓴 것이라 등급 0 문구로 읽어야 한다.
   → docs/13(E13-03), docs/14(E14-19·E14-21·E14-22), [2026-11-17-sleep-time-melete-selected-addendum.md](/home/jimmy/repos/full-continual-learning/research/2026-11-17-sleep-time-melete-selected-addendum.md)(ER-19), docs/11 §8 영향 가드(ER-12)와 무제한 무망각 비주장(E14-13).
9. **남은 정정.** (a) Tian: 저장소 기준 신규가 아님을 확정했다(catalog N28, 11-02 baseline 33행, 첫 커밋 11-09). 서지는 Crossref로 대조했다(Nature Communications 17, 2150, 2026-01-29, 저자 8명). 처리: ER-13·ER-14·ER-15·ER-16. (b) Continual-ARC 최신 버전: ER-17. (c) 증거 라벨 어휘가 문서마다 다르다(SYNC-07): SYNC_POLICY 7종, README·AGENTS 5종, docs/13은 DERIVATION을 더 쓴다 → README 새 절에 7종과 ESTIMATE를 적었다. (d) README 정리 기준일(2026-11-12)과 백서 기준(SYNC-16·SYNC-22) → 갱신·표시했다. (e) `tools/validate_docs.py`는 `/home/jimmy/repos/full-continual-learning/…` 절대 링크를 다른 위치의 checkout에서 모두 미해결로 판정한다(기준 커밋에서 192건, SYNC-34). 11-12 감사의 '오류 0건'은 main checkout 위치에서만 성립한다. 도구는 고치지 않았다(개선안은 결정 대기 N-10). (f) manifest의 base_commit은 첫 동기화 기준으로 남아 있다(SYNC-23, 항목만 추가). (g) manifest에 외부 자동화의 task·run 식별자가 공개돼 있다(SYNC-26, 손대지 않음, 결정 대기 N-10). (h) 기호 충돌(φ·θ·b·B·C·D·Q·k·e): 06 기호를 기준으로 한 대응표를 넣었다(E13-23). (i) catalog 누락 33건을 후보 행으로 올렸고 보충 파일의 R 식별자가 catalog의 R01–R11과 충돌함을 표시했다(E13-18).
10. **대기 항목: 해소된 것은 하나도 없다.** 11-12 감사 §5의 사용자 확인 19건은 변화 없음 14 / 영향 있음 5 / 해소 0, docs/09 §10의 D-01–D-14는 변화 없음 10 / 영향 있음 4 / 해소 0다. 근거 원문은 11-16 블록 2개와 11-17 요청뿐이며 판정은 §7이다.

## 4. 반영한 편집 (문서별)

설계 문서 12개에 W1–W5 편집 블록을 넣었다. ChatGPT 동기화 문서(docs/13·14, research/2026-11-16·17-*, 동기화 참고문헌, sources/sync/2026-11-16)는 기존 문장을 지우거나 바꾸지 않고 삽입 주석만 넣었다. docs/07의 한 문장은 '삭제'의 두 뜻을 구분하도록 용어를 한정했고(E14-01), docs/09 §10의 표 칸에는 기존 문구를 남기고 추정·개정 추천을 덧붙였다(EC-03, EC-05–EC-07). EC-02와 EC-04는 기존 문구의 범위를 좁혔다(기본 후보를 P1 135M으로, '추정을 쓰지 않았다'를 표로). 기존 상대 링크는 없애지 않았다. D-04의 기존 추천은 지우지 않고 '2026-11-12 추천(개정 대상)'으로 남긴 뒤 개정 추천을 덧붙였다(EC-05).

| 문서 | 편집 | 편집 id |
|---|---:|---|
| [01-intent-and-charter.md](/home/jimmy/repos/full-continual-learning/docs/01-intent-and-charter.md) | 1 | E13-33 |
| [03-foundations.md](/home/jimmy/repos/full-continual-learning/docs/03-foundations.md) | 4 | E13-19, ER-06, ER-10, ET-06 |
| [04-rhythms-and-orchestration.md](/home/jimmy/repos/full-continual-learning/docs/04-rhythms-and-orchestration.md) | 1 | E13-20 |
| [05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) | 7 | E13-21, E13-22, E14-10, E14-11, ER-05, ET-04, ET-08 |
| [06-mathematical-framework.md](/home/jimmy/repos/full-continual-learning/docs/06-mathematical-framework.md) | 3 | E13-23, E13-24, E13-25 |
| [07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md) | 7 | E13-26, E13-27, E14-01, E14-02, ER-01, ER-08, ET-05 |
| [08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md) | 5 | E14-03, E14-04, ER-09, ER-21, EC-11 |
| [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md) | 21 | E13-28, E13-29, E14-05, E14-06, E14-07, E14-08, E14-09, ER-03, ER-04, EC-01, EC-02, EC-03, EC-04, EC-05, EC-06, EC-07, EC-08, EC-09, EC-10, EW6-09, EW6-10 |
| [10-evolution-policy.md](/home/jimmy/repos/full-continual-learning/docs/10-evolution-policy.md) | 3 | E14-14, E14-15, EC-12 |
| [11-research-agenda.md](/home/jimmy/repos/full-continual-learning/docs/11-research-agenda.md) | 6 | E13-30, E13-31, E14-12, E14-13, ER-11, ER-12 |
| [13-schema-decomposition-and-interference.md](/home/jimmy/repos/full-continual-learning/docs/13-schema-decomposition-and-interference.md) (ChatGPT 동기화 문서: 삽입 주석만) | 20 | E13-01, E13-02, E13-03, E13-04, E13-05, E13-06, E13-07, E13-08, E13-09, E13-10, E13-11, E13-12, E13-13, E13-14, E13-15, E13-16, E13-17, E14-16, ET-01, EC-13 |
| [14-schema-lifecycle-crud-and-joint-paper.md](/home/jimmy/repos/full-continual-learning/docs/14-schema-lifecycle-crud-and-joint-paper.md) (ChatGPT 동기화 문서: 삽입 주석만) | 15 | E14-17, E14-18, E14-19, E14-20, E14-21, E14-22, E14-23, E14-24, E14-25, E14-27, ER-07, ER-20, ET-03, ET-09, EC-14 |
| [EVIDENCE.md](/home/jimmy/repos/full-continual-learning/EVIDENCE.md) | 1 | EW6-15 |
| [README.md](/home/jimmy/repos/full-continual-learning/README.md) | 5 | EW6-01, EW6-02, EW6-03, EW6-04, EW6-05 |
| [15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md) | 1 | EW6-14 |
| [2026-11-16-sleep-time-melete.md](/home/jimmy/repos/full-continual-learning/references/2026-11-16-sleep-time-melete.md) (ChatGPT 동기화 문서: 삽입 주석만) | 1 | ER-17 |
| [README.md](/home/jimmy/repos/full-continual-learning/references/README.md) | 1 | EW6-11 |
| [catalog.tsv](/home/jimmy/repos/full-continual-learning/references/catalog.tsv) | 3 | ER-15, ER-16, EW6-13 |
| [schema-decomposition-2026-11-14.md](/home/jimmy/repos/full-continual-learning/references/schema-decomposition-2026-11-14.md) (ChatGPT 동기화 문서: 삽입 주석만) | 1 | E13-18 |
| [schema-lifecycle-2026-11-16.md](/home/jimmy/repos/full-continual-learning/references/schema-lifecycle-2026-11-16.md) (ChatGPT 동기화 문서: 삽입 주석만) | 1 | E14-26 |
| [shared-links-2026-11-17.md](/home/jimmy/repos/full-continual-learning/references/shared-links-2026-11-17.md) | 1 | EW6-12 |
| [2026-11-16-memory-evidence-read-supplement.md](/home/jimmy/repos/full-continual-learning/research/2026-11-16-memory-evidence-read-supplement.md) (ChatGPT 동기화 문서: 삽입 주석만) | 1 | ER-18 |
| [2026-11-16-sbl-tracking.md](/home/jimmy/repos/full-continual-learning/research/2026-11-16-sbl-tracking.md) (ChatGPT 동기화 문서: 삽입 주석만) | 2 | ER-14, ET-07 |
| [2026-11-17-sleep-time-melete-selected-addendum.md](/home/jimmy/repos/full-continual-learning/research/2026-11-17-sleep-time-melete-selected-addendum.md) (ChatGPT 동기화 문서: 삽입 주석만) | 1 | ER-19 |
| [2026-11-16-discussion.md](/home/jimmy/repos/full-continual-learning/sources/sync/2026-11-16-discussion.md) (ChatGPT 동기화 문서: 삽입 주석만) | 1 | ER-13 |
| [2026-11-17-discussion.md](/home/jimmy/repos/full-continual-learning/sources/sync/2026-11-17-discussion.md) | 1 | EW6-07 |
| [manifest.json](/home/jimmy/repos/full-continual-learning/sources/sync/manifest.json) | 1 | EW6-06 |
| [user-statements.md](/home/jimmy/repos/full-continual-learning/sources/user-statements.md) | 1 | EW6-08 |

- **합친 블록**: E13-32 → E14-13(무제한 무망각 비주장), ER-02 → E14-04(F-CI에 F24 번호를 주고 F22·F23과 한 표에), ET-02 → E14-20('삭제' 용어 주석). 제외: EC-15(README 행은 EW6-02로 이미 넣음).
- **고친 블록 15개**: 기준 시점 한정(E13-06·E13-14·E13-18·E13-31·E14-23·E14-26·ER-19: catalog 후보 행과 이 검토의 주석이 들어간 뒤에도 문장이 참이도록 '280dc9a 기준'을 적음), 단정 약화(E14-15: 공동논문이 B15 논문과 별개라는 단정을 확인 대기로), 번호·구조(E14-04, E14-07 들여쓰기, E14-09), 합침(E14-13, E14-20), 기준선 보존(EC-05), 변경 기록(EC-09).
- **W6 편집 16개**: README(기준일·읽는 순서 행 3개·백서 기준 표시·새 절), manifest 항목 3개, 11-17 대화 출처, user-statements의 U-T12–U-T14 위치 표시, docs/09 §1.1의 U-T14 행·§10의 영향 갱신, 참고문헌 안내·catalog 33행·shared-links 파일, docs/15, EVIDENCE.md 한 절, 이 기록. 전부 [edits-applied.tsv](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/edits-applied.tsv)에 있다.
- **새 설계 문서**: [15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md)(번호 15는 01–14의 다음). 로드맵 P1–P5의 데모 시나리오·넓이/깊이 변화·성립하는 보장과 상한·종료 gate·미루는 것은 바뀌지 않았고 ESTIMATE를 게이트로 올리지 않았다.

## 5. 사용자 공유 링크 카드 재검토 결과

사용자가 공유한 링크 카드 98장을 읽기 전용으로 다시 분류했다(11-13 이후 새로 들어온 카드 73장 포함). FCL 연구 6장, skill·도구 19장, 무관 73장이다. 카드 id·앱 이름·공유 단축 링크는 공개하지 않고 'T1…'로 부른다. 원문 확인은 공식 arXiv 초록 페이지·학회 사이트·저자 게시 페이지의 제목·저자·날짜·버전 확인과 일부 본문 정독이며 전문 정독·코드 실행·수치 재현은 아니다. 상세는 [W4-papers.txt](/home/jimmy/repos/full-continual-learning/research/2026-11-17-design-review/W4-papers.txt)와 [shared-links-2026-11-17.md](/home/jimmy/repos/full-continual-learning/references/shared-links-2026-11-17.md)에 있다.

| 카드 | 확정 대상 | 확인 수준 | 설계 연결 | catalog |
|---|---|---|---|---|
| T1 | arXiv 2604.10589, 범주론 관점의 schema-based learning working paper(v1 2026-04-12) | metadata-checked + 본문 부분 정독. 11-16 기록에 discussion-import로 이미 있었음(부분 중복) | symbolic·formal 비교점. CRUD 어휘의 형식적 선례이나 Del은 기능 손실을 다루지 않는 집합 연산. 저자 스스로 미완 working paper | S43 (ET-06·ET-07·ET-09) |
| T2 | arXiv 2611.10866, 가중치 삭제 튜닝(v1 2026-11-07) | metadata-checked + 본문 부분 정독. NeurIPS 2026 poster 등재는 학회 공식 사이트로 확인하되 제목·방법명이 다르고 main/workshop 구분과 심사 판정은 확인하지 못함 | post-training의 연결 제거 사례. 순차 지속학습은 저자가 미시험. '삭제'의 세 번째 뜻 | A36 (ET-01) |
| T3 | arXiv 2610.15095, Swarm Telepathy(v1 2026-10-10) | metadata-checked + 본문 p.1–8 부분 정독 | H4의 learned interface·migration adapter의 인접 사례. 한 번의 handoff만 평가 | A37 (ET-04·ET-05) |
| T4 | 논문이 아님: 저자 조직의 Hugging Face 블로그(2026-11-10), 새 expert·router row 추가 대 LoRA 평균 병합 | 게시 페이지 metadata-checked + 전문 정독. 동료 심사·코드 없음 | Create·통합 원칙과 CMS 분기 cold-start의 인접 사례. low-rank schema expert의 증거가 아님 | A38 (ET-03·ET-08) |
| T5 | arXiv 2610.39302, JEPA와 표상 정렬 가설(v1 2026-10-29) | metadata-checked(초록만) | 지속학습·schema 효용과 직접 연결되지 않아 참고문헌 후보로만 둠 | S46 |
| T6 | 논문 미확정: 1900년 이전 과학 지식만 학습시키는 영상 | 설명을 읽지 못함 | 연결 근거가 없어 원장·편집에 올리지 않음 | 없음 |

- skill·도구 카드 19장은 사용 후보 3 / 보류 10 / 불필요 6으로 판정했다. 이들은 FCL 설계가 아니라 다른 작업 환경의 문제이므로 이 저장소에는 목록을 싣지 않았다. 무관 73장은 일괄 불필요다. 이전 검토(11-13)의 FCL 카드 3건(T1–T3)에는 새 판본이 없다.

## 6. 계산 계획 요약 ([15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md))

- **성격.** P1–P5에 자원을 붙이는 횡단 문서이며 별도 인프라 phase가 아니다. 어떤 자원을 쓰든 phase 종료 gate의 E2E는 사용자가 재현할 수 있는 환경(host CPU와 노트북)에서 실제 `fcl` CLI·실제 pretrained 가중치로 돈다. 클라우드에서만 도는 gate는 gate로 인정하지 않는다. 가격은 2026-11-17 조회 시점이며 변동 가능하다.
- **판단 기준.** 시간당 가격이 아니라 유효 실험 1건(manifest 해시가 맞고 budget 일치 검사를 통과한 (arm × seed) 결과 하나)의 총비용이다. 사용자의 두 제약은 이렇게 옮겼다: '과도한 사양이 아닌'은 연산이 아니라 메모리·운영 이유가 없는 H100급을 기본으로 쓰지 않는 것, 'minimum으로 품질·효율을 떨어트리지 않으면서'는 OOM 재실행·재현 못 하는 gate·seed·arm 축소로 인한 근거 약화를 최소의 비용으로 세는 것.
- **결론 6줄(ESTIMATE).** (1) 연산 비용은 작다: SmolLM2-135M 기반이면 P1 전체 클라우드 비용은 P50 약 $17(P10–P90 $10–35). (2) GPU 종류별 비용/FLOP은 거의 평평해(소형 모델 추정 유효 TFLOP-hour 단가 약 14.5–28.8 m$) tier는 메모리 헤드룸·vCPU/RAM·VM·벽시계로 고른다. (3) 주력은 48GB급 1장 VM. (4) A100 80GB·H100은 학습 메모리가 48GB를 넘는 일, 세션 상한을 넘는 연산 지배 대형 run, 8B teacher·참고선에만 쓴다. (5) 평가(readout)는 GPU가 아니라 지연시간과 vCPU가 지배한다. (6) D-04는 개정을 제안한다.

| phase | 학습·대량 readout 배정 | 클라우드 과금 시간 h (P50, P10–P90) | 클라우드 비용 (P50, P10–P90) |
|---|---|---|---|
| P1 | 노트북 우선, 부족하면 48GB급 1장. T04 microbenchmark는 승인 시 2종 | 11.5 (6.5–25.4) | $17 ($10–$35) |
| P2 | 48GB급 1장 | 63.2 (21.7–208) | $78 ($27–$255) |
| P3 | 48GB급 1장 | 22.5 (8.7–66.2) | $28 ($11–$81) |
| P4 | 48GB급 1장(전체 student 1.7B·8B teacher는 대형) | 40.0 (11.5–127) | $54 ($15–$188) |
| P5 | 두 번째·큰 모델 학습은 대형, readout·서빙은 48GB급 | 69.7 (25.6–160) | $130 ($44–$395) |
| P1–P4 합계 | | 152 (65.5–394) | $198 ($86–$516) |

P5의 두 번째 모델이 1.7B이면 P5는 P50 $548($141–2,537), 360M이면 P50 $205($66–791)다. host·노트북 시간은 비용에 넣지 않았다. 노트북 사양은 AI TOPS에서 유도한 가정이고 모든 핵심 가정(forward 지연, write 지연, MFU)은 미측정이다. P1-T04에서 측정해 표를 고친다(보정 절차는 docs/15 §8).

## 7. 사용자 결정 대기

비용이 드는 선택은 결정 전에 실행하지 않는다. 아래에서 해소된 결정은 없다. 판정은 11-12 이후 새 USER 원문(11-16 블록 2개, 11-17 요청)이 항목의 전제·선택지·추천을 바꾸는지로 했고, 말하지 않은 것은 결정 대기로 유지했다.

### 7.1 열린 결정 D-01–D-14 (변화 없음 10 / 영향 있음 4 / 해소 0)

| ID | 질문 | 판정 | 이유 |
|---|---|---|---|
| D-01 | P1 base model(추천: SmolLM2-135M, 크기 상향은 비용) | 영향 있음 | 비용효율과 품질 하한을 함께 요구하는 제약이 생겼다. 모델 크기 선택의 근거가 되지만 크기를 정한 말은 아니다. 결정 대기 유지. |
| D-02 | Titan-Llama 코드 사용 방식 | 변화 없음 | 새 USER 원문이 다루지 않았다. |
| D-03 | P1 구조 family | 변화 없음 | 새 USER 원문이 다루지 않았다. |
| D-04 | retrofit 학습의 계산 장소·시간 상한(추천: 노트북 GPU 시간 상한 먼저, 클라우드 GPU는 P5 전까지 보류) | 영향 있음 | 사용자가 host의 runcrate 사용환경을 전제로 학습 시 사용 계획을 요청했다. '클라우드 GPU는 P5 전까지 보류'라는 추천의 전제가 바뀌었다. 그러나 '계획해봐'는 계획 요청이지 사용 승인이 아니다. 개정 추천은 PROPOSAL이고 결정은 OPEN. |
| D-05 | readout 통계 계획 | 변화 없음 | 새 USER 원문이 다루지 않았다. |
| D-06 | P1에 source 삭제 포함 | 변화 없음 | 결정 내용(source 삭제를 P1에 얇게 포함할지)은 그대로다. 사용자의 Delete는 기능 손실 기반 망각의 비용이라는 다른 뜻이라 용어 충돌만 주의한다(N-2(검토 기록 §7)). |
| D-07 | P1에서 sealed readout 실행 | 변화 없음 | 새 USER 원문이 다루지 않았다. |
| D-08 | 참고선 Qwen3-8B+raw history 도입 시점 | 변화 없음 | 새 USER 원문이 다루지 않았다. |
| D-09 | 세계 렌더링 언어 | 변화 없음 | 새 USER 원문이 다루지 않았다. |
| D-10 | self-evolution 자동화 범위·예산 | 변화 없음 | 새 USER 원문에 자동화 범위가 없다. 계산 계획이 붙인 비용 추정은 ESTIMATE이며 결정이 아니다. |
| D-11 | 외부 agent 연결 대상·방식·시점 | 변화 없음 | 새 USER 원문이 다루지 않았다. |
| D-12 | 두 번째 base model·크기(비용: 다운로드·학습, 클라우드 가능성) | 영향 있음 | '클라우드 가능성'이 runcrate 계획 요청으로 구체화됐다. 결정 시점(P4 종료 재검토)과 선택지는 사용자가 정하지 않았다. 결정 대기 유지. |
| D-13 | 위상(phase) 조율(D) 실험의 배치 | 변화 없음 | 새 USER 원문이 다루지 않았다. |
| D-14 | schema 판단 구조(controller)의 최소형을 P1에 넣을지(2026-11-12 마스터 판단으로 (b), 사용자 확인 대기) | 영향 있음 | 사용자가 해법의 일부로 문맥 기반 schema 탐색(Read)과 update/create 분기를 서술했다. P1의 규칙형 controller v0가 이를 얼마나 덮는지 재검토가 필요하다(검토 기록 §3 'CRUD와 controller'). 사용자 확인은 여전히 대기. |

D-04 개정 추천(PROPOSAL, OPEN): ① (b) 노트북으로 P1 135M 개발·T09를 시작하되 시간 상한과 재개 조건을 먼저 승인, ② (c) 클라우드는 둘로 나눠 묻는다. T04의 소액 microbenchmark(2종, ESTIMATE P50 약 $7.6, 상한 $12)를 지금 승인 요청하고, 학습·readout용은 T04로 보정한 phase별 상한을 phase 시작 때 따로 승인. ③ '클라우드는 P5 전까지 보류'는 근거가 약해 철회를 제안(노트북 환산 P2 학습만 P50 약 82시간). 결정은 사용자다.

### 7.2 11-12 감사 §5의 사용자 확인 19건 (변화 없음 14 / 영향 있음 5 / 해소 0)

| ID | 질문 | 판정 | 이유 |
|---|---|---|---|
| #1 | U-T 번호가 대화 순서인가. U-T07 '내가 원래 생각한건'은 새 결정인가 재서술인가 | 변화 없음 | 새 USER 원문 3개 중 U-T 번호나 U-T07의 성격을 다룬 것이 없다. SUPERSEDED 2건의 근거는 그대로다. |
| #2 | docs/02 정정표 1·2행과 T04 서술(assistant 재해석)을 수용하는가 | 변화 없음 | 새 USER 원문이 수용 여부를 말하지 않았다. docs/13의 USER-HYPOTHESIS(LLM의 schema 중첩 등)는 11-14 대화의 재구성이고 원문 블록이 없어 판정 근거로 쓰지 못한다. |
| #3 | 헌장 §3의 4–6층을 사용자 의도로 인정하는가 | 변화 없음 | 새 USER 원문에 헌장 층위를 다루는 말이 없다. |
| #4 | U-T05의 'latent space(continual space)'를 continuous로 읽은 것이 맞는가 | 변화 없음 | 새 USER 원문은 latent space의 뜻을 말하지 않았다. 'low rank expert'는 연속 파라미터 모듈이라는 간접 정황일 뿐 그 읽기를 확인한 것이 아니다. |
| #5 | U-T11의 '모든 내용'은 주제별 재구성으로 충족된 것으로 보는가 | 영향 있음 | U-T11('모든 내용…올려줘') 뒤에 '대화내용과 정보를 항상 update'하라는 상시 요청이 생겼다. 그러나 주제별 재구성이 '모든 내용'을 충족하는지는 말하지 않았다. 결정 대기 유지. |
| #6 | U-T09의 'Ali도 최근 관심있는 개념들'은 배경 정보인가 우선순위 신호인가 | 영향 있음 | Ali는 배경 정보를 넘어 공동논문 제안의 대상이다(USER). 다만 Ali의 관심이 설계 우선순위라는 말은 하지 않았으므로 '우선순위 신호' 해석은 결정 대기 유지. |
| #7 | H4의 text/vec2text 인터페이스를 필수 경로에서 내리는 것이 사용자 의사인가 | 변화 없음 | 새 USER 원문에 text interface를 다룬 말이 없다. |
| #8 | 사용자의 단계 처리를 다중 신호 controller로 일반화하는 것을 수용하는가 | 영향 있음 | 사용자가 해법을 '기존 expert의 in-place update, 적합한 schema를 못 찾으면 create'라는 문맥 의존 선택으로 서술했다. 낯섦 하나의 단조 규칙보다 풍부한 판단이 필요하다는 방향의 간접 근거다. 일반화를 수용한다는 말은 아니므로 결정 대기 유지. |
| #9 | 'model needs sleep의 방법으로'가 A03의 특정 전환 절차인가 일반 Sleep인가 | 변화 없음 | 새 USER 원문에 Sleep이 없다. (11-16 Sleep-time 보고는 ChatGPT 정리이지 USER 원문이 아니다.) |
| #10 | B04의 '흘려듣기'를 학습 대상 제외·보류로 읽어도 되는가 | 변화 없음 | 새 USER 원문이 다루지 않았다. |
| #11 | B08의 '오류(overfitting)를 유도'를 시간축 반례로 줄이는 성급한 일반화 허용으로 읽어도 되는가 | 변화 없음 | 새 USER 원문이 다루지 않았다. |
| #12 | 점진적 해상도 적용 방식(P1 = 실제 CLI + 소형 pretrained, controller v0)이 맞는가 | 변화 없음 | 새 USER 원문이 P1 정의를 확인하거나 바꾸지 않았다. 11-17 계산 계획은 이 틀을 전제로 쓴 횡단 문서이며 사용자가 틀을 승인했다는 근거는 아니다. |
| #13 | 최종 사용 인터페이스는 무엇이며 Codex·Prime agent에 backend로 연결할 권한·인프라가 있는가 | 변화 없음 | 새 USER 원문이 인터페이스·agent 연결을 다루지 않았다. |
| #14 | B15의 논문은 Melete 논문인가 FCL 논문인가. veridraft 개선 요청이 계속되는가 | 영향 있음 | 공동논문 제안이라는 새 논문 건이 생겼다(내용은 CRUD 세 포인트와 해법). B15의 논문과 같은 것인지, veridraft 요청이 계속되는지는 말하지 않았다. 결정 대기 유지. |
| #15 | B16의 superpowers 사용 지시를 FCL 작업에도 적용하는가 | 변화 없음 | 새 USER 원문이 다루지 않았다. |
| #16 | Melete의 학습 방법 대장·atlas를 FCL로 이관해 통합 모델 기준으로 다시 순위를 매기는가 | 변화 없음 | 새 USER 원문이 다루지 않았다. 11-17 원문의 'melete'가 무엇을 가리키는지는 별도 새 확인 항목으로 올렸다(N-1(검토 기록 §7)). |
| #17 | B01에서 '아이디어 없음'으로 남긴 eviction·forgetting·memory revision을 어느 phase에서 다룰 것인가 | 영향 있음 | 사용자가 '망각의 비용을 어떻게 치를지'(Delete)를 지속학습의 세 포인트 중 하나로 직접 지목했다. '다룰 것인가'에는 사실상 답이 났으나, 어느 phase에서 다룰지는 말하지 않았다. phase 배치는 결정 대기. |
| #18 | 이번에 들어간 틀(F13–F21, gate 레지스트리, 진화 권한 사다리 E0–E3, controller 해상도 사다리 v0–v2, 리듬 실험 A–D 배치)을 승인하는가 | 변화 없음 | 새 USER 원문이 어느 틀도 승인하지 않았다. 모두 PROPOSAL이다. |
| #19 | J1의 gate 수치(5pp 등)는 당시 master 제안이다. FCL gate 수치는 pilot 분산 뒤 사전 확정·사용자 승인 | 변화 없음 | 새 USER 원문이 gate 수치를 다루지 않았다. |

### 7.3 이번 검토에서 새로 생긴 결정·확인

| ID | 내용 | 근거 |
|---|---|---|
| N-1 | 11-17 원문의 'melete'가 이 저장소의 통합 모델 System ONE(P1–P5 학습)인지, 별도 Melete 신경 기억 실험까지 포함하는지. docs/13의 'Melete'(L34·L97·L149)가 가리키는 대상도 같은 질문이다 | U17-05, W1 확인 요청 U2 |
| N-2 | '삭제'를 source 삭제 / 기능적 망각·보존(Delete/Retain) / 가중치 삭제 학습으로 나눠 부르는 용어안의 수용 | E14-02·E14-20 |
| N-3 | Delete/Retain 정책을 어느 phase에 둘지(제안: 측정 P1, 정책 P4, 압축·폐기 P5). 11-12 감사 §5 #17의 구체화 | 사용자 확인 #17 |
| N-4 | 사용자 원문 '못찾으면 create'를 docs/14처럼 '구조적 새로움이 확인될 때만'으로 읽어도 되는지, low-rank expert를 schema 보관 단위의 기본 후보로 올릴지 | E14-09, E14-18 |
| N-5 | 신규 arm(`ftall`, `adapters`, `sel-*`)·family F22–F24·실험 B(Base/Instruct)의 채택, P2·P4의 F-CI 측정 전용 후보 readout, controller 'v0' 이름 정리 | E14-04·E14-09·E14-10, ER-03·ER-04 |
| N-6 | Ali 제안문 수정안의 승인, 발송 여부, 초안에 깊이·recursion 축을 넣을지 | E14-24 |
| N-7 | docs/13 가설 1–2와 U-T06 원문의 관계, 2026-11-14 대화 원문을 확보할 수 있는지 | E13-01·E13-02 |
| N-8 | 지속학습의 목적(11-16 원문)을 헌장 U13으로 올릴지 U03·U10·보호 family에 묶을지, '무망각'을 선택적·점진적 망각 정책으로 읽어도 되는지 | E13-33 |
| N-9 | P1 '허용오차'를 noise floor ν로 봉인하는 방식(설계 담당 판단일 수 있음) | E13-28 |
| N-10 | 공개 저장소에 외부 자동화의 task·run 식별자를 둘지, catalog에 링크 전용 7행을 넣을지, `validate_docs.py`가 절대 링크 접두를 ROOT로 해석하도록 고칠지 | SYNC-26, 참고문헌 후보 W3-30–36, SYNC-34 |
| N-11 | **FCL 전용 runcrate 키·예산과 T04 microbenchmark 승인(credential gating 5항목)** | docs/15 §9 |

N-11을 credential gating 5항목으로 적는다. **용도:** FCL P1-T04 클라우드 microbenchmark, 이어서 P1 sealed readout과 P2 이후 학습·readout(필요성은 P2부터 커짐). **유료 여부:** 유료이며 선불 잔액에서 시간 단위로 차감되고 잔액이 모자라면 실행 중 인스턴스가 삭제될 수 있다(공개 문서). 지금 쓸 수 있는 키는 다른 프로젝트 계정에 속해 예산이 공유되므로 전용 키·예산을 따로 둘지가 결정 대상이다. **예상 비용(ESTIMATE, NOT RUN):** T04 P50 약 $7.6($5.2–11, 상한 $12), P1 P50 $17, P1–P4 P50 $198(135M 기준), P5는 두 번째 모델에 따라 P50 $205–$548. 승인된 상한이 아니다. **무료 planB:** host CPU(계약·E2E·소규모 평가)와 노트북 GPU 12GB(간헐 연결). **planB의 품질 저하:** P2 학습이 노트북 환산 P50 약 82시간(연속 약 3.4일), 360M 이상은 step당 token 축소·0.6B 이상은 불가, 시간을 맞추려고 seed·arm을 줄이면 sealed readout이 INCONCLUSIVE가 되기 쉬워 등급 3 확증이 약해진다. 과학적 내용(실험 설계)은 같다.

## 8. 이 검토로 성립하지 않는 것 (NOT RUN)

- 모델 학습·GPU 실행·클라우드 인스턴스 생성·비용 지출·runcrate API 호출·유료 API·모델 가중치 다운로드는 0회다. 키 파일과 조회 스크립트는 열지 않았다. 백서 재생성·배포, 외부 발송(Ali 제안문 포함), push·rebase·병합도 하지 않았다.
- 계산 계획의 모든 수치는 ESTIMATE이며 측정이 아니다. 가격은 2026-11-17 조회 시점이다. 핵심 가정은 P1-T04에서 측정하기 전까지 가정이다.
- 논문은 공식 초록 페이지와 일부 본문을 읽었다. 전문 정독(fulltext-read)은 없고 코드 실행·재현도 없다. 수학 점검은 항등식·부등식의 성립·반례를 소규모 numpy로 확인한 것이며 모델 효용의 근거가 아니다.
- 원장 판정은 문서 대 문서의 대조다. 설계가 맞다는 증명이 아니고, 새로 들어간 문장은 PROPOSAL·OPEN이다. 백서는 2026-11-12 기준 그대로다.
- 사용자 결정은 하나도 대신하지 않았다. 11-17 요청의 '계획해봐'는 비용 승인이 아니다.
- **검증 결과(worktree, 기준 280dc9a 위 branch):** wrapper(저장소의 절대 링크 접두를 worktree로 바꿔 해석하는 검증기, 저장소 밖에 둠): errors 0, 파일 184·markdown 54·로컬 링크 623·참고문헌 133. 원본 `tools/validate_docs.py`: errors 512이고 전부 `/home/jimmy/repos/full-continual-learning/…` 접두 절대 링크다(기준선 192에서 새 문서·주석의 절대 링크만큼 늘었고 다른 종류는 0). 병합 뒤 main checkout에서 돌리면 풀릴 것으로 보이나 이번에는 실행하지 않았다(NOT RUN). JSON 2개(manifest·ledger-delta) 파싱 통과, TSV 12개의 열 수 일치, catalog.tsv 8열·ID 유일(133). 기존 파일의 삭제·이름 변경 0(`git diff --diff-filter=DR 280dc9a`가 비어 있음). 공개 안전성 스캔은 추가 14,707줄에서 금지 패턴(작업 폴더·.claude 경로, 키 이름, 이메일·IP 형태, private 저장소 경로, 앱 이름, 상품 식별자 192개, 잔액, 카드 id 98개)이 0건이다. 원 논문의 긴 인용은 없다(제목과 한 문장 이하의 짧은 발췌뿐).
