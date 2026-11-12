# 설계 반영 감사: 사용자 피드백·논문이 FCL 설계에 들어갔는가 (2026-11-12)

**질문 (USER, 2026-11-12):** 지금까지 준 피드백(논문 포함)이 설계에 반영됐는가. 설계에 집중하고, 반영된 설계를 시각화 백서로 총망라한다.

**답:** 감사 전에는 부분적으로만 반영돼 있었다. 사용자 진술 202개 원자 항목 중 111개(55%)만 설계 문서에 자리가 있었다. 2026-11-11 논문 원문 검토는 `research/`에만 있고 설계 본문에 들어가지 않았다. 로드맵은 사용자 전역 규칙 "점진적 해상도"와 어긋났다. 이번 감사에서 다음을 반영했다.

- 설계 문서 10개에 편집 70개를 넣었다.
- [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md)를 다시 썼다.

그 결과 사용자 진술 202개 중 195개가 설계 위치를 갖는다. 다만 새로 들어간 내용 대부분은 **PROPOSAL·OPEN 수준의 설계 서술**이다. 구현·실행·효용 검증이 아니다. 아래 §5의 사용자 확인 항목과 §6의 열린 결정이 남아 있다.

## 1. 방법

- **원장:** 사용자 진술을 원자 항목(인용·출처 줄·날짜·종류·라벨)으로 쪼갰다. 원천은 둘이다.
  - FCL 시기: U-T01–U-T11, docs/01·02, README.
  - Melete 시기: B01–B20 세션 요약, H1–H5, J0/J1 교훈.
- **판정:** 항목마다 docs/03–12에서의 반영 위치(파일:줄과 절)와 한 줄 이유를 붙였다. 판정값은 다음 넷이다.
  - REFLECTED: 반영됨.
  - PARTIAL: 일부만 반영됨.
  - MISSING: 반영 위치 없음. 검색 0건을 근거로 붙였다.
  - SUPERSEDED: 이후 사용자 진술이 대체함. 그런 진술이 있을 때만 썼다.
- **보완:** 빠진 항목마다 앵커 문장(원문 그대로)과 새 문장, 증거 라벨로 된 편집 블록을 만들었다. 2026-11-11 원문 검토와 11-09 주간 조사도 같은 형식으로 설계 문서에 옮겼다.
- **검증:** 검사기(원장 형식, 앵커가 원문에 정확히 한 번 등장, 로드맵 필수 요소)와 리더 검증(인용 325개·설계 위치 1,028개 대조, 무작위 판정 12건 재검토)을 거쳤다. 그 뒤 마스터가 검수해 반영했다. 반영 후 `tools/validate_docs.py` 오류는 0건이다.
- **작업 분담:** worker 4개(W1 FCL 원장, W2 Melete 원장, W3 문헌 통합, W4 로드맵)가 초안을 쓰고 리더가 검증했다. 마스터가 충돌을 정리해 반영했다. 원장과 초안은 [2026-11-12-design-audit](/home/jimmy/repos/full-continual-learning/research/2026-11-12-design-audit/README.md)에 있다.

## 2. 수치

| 원장 | 항목 | 사용자 진술(USER) | 감사 전 REFLECTED | PARTIAL | MISSING | SUPERSEDED |
|---|---:|---:|---:|---:|---:|---:|
| FCL 시기 ([ledger-fcl.json](/home/jimmy/repos/full-continual-learning/research/2026-11-12-design-audit/ledger-fcl.json)) | 177 | 112 | 133 (75%) | 40 | 3 | 1 |
| Melete 시기 ([ledger-melete.json](/home/jimmy/repos/full-continual-learning/research/2026-11-12-design-audit/ledger-melete.json)) | 148 | 90 | 60 (41%) | 78 | 9 | 1 |
| 합계 | 325 | 202 | 193 (59%) | 118 | 12 | 2 |

PARTIAL·MISSING 130개는 이번 반영 후 이렇게 바뀌었다.

| 원장 | 설계 문서 편집으로 위치가 생김 | 새 로드맵에 들어감 | 문헌 정독이 남음 |
|---|---:|---:|---:|
| FCL 시기 | 28 | 11 | 4 |
| Melete 시기 | 66 | 16 | 5 |

"문헌 정독이 남음" 9개 중 4개(11-09 주간 조사 2, 11-11 원문 검토 2)는 W3의 문헌 통합 편집으로 다뤘다. 실제로 남은 것은 5개다(§6.2).

사용자 진술만 보면 다음과 같다.

| 시기 | 감사 전 REFLECTED | 이번에 설계 위치가 생김 | 문헌 정독이 남음 | SUPERSEDED |
|---|---:|---:|---:|---:|
| FCL 시기 (112) | 79 | 29 | 3 | 1 |
| Melete 시기 (90) | 32 | 55 | 2 | 1 |

## 3. 핵심 발견

1. **로드맵이 규칙과 어긋났다.** 옛 docs/09 P0–P6에는 다음 문제가 있었다.
   - 계약·조사 전용 phase(P0)가 있었다.
   - phase가 계층별(재귀·controller·Sleep·확대·외부화)로 나뉘었다.
   - capability × phase 표와 phase별 데모·상한·미루는 것이 없었다.
   - depth read, 리듬 실험 A–D, post-training 분화 가설이 어느 phase에도 없었다.

   → 새 로드맵은 P1–P5다. 매 phase 종료 때 `fcl` CLI에서 실제 retrofit 모델이 경험 입력부터 재시작 복원까지 전체 여정을 돈다.
2. **논문 검토가 설계 본문에 없었다.** 2026-11-11 원문 검토(학습된 구조 대 고정·무구조 대조의 부재, 새로움 gating의 무엇·어디·얼마나·언제 분해, accommodation 공백, 망각·표면/구조·계산량 미측정, 식에서 재구현)는 `research/`에만 있었다.

   → docs/03·05·06·08·10·11에 35개 편집으로 옮겼다. 기존 결론을 약화·정정하는 편집이 3건이다.
   - docs/03 §2의 SBL 행: HWU20에서 새 schema 학습이 빨라지지 않았다.
   - docs/03 §7의 "신경망 구현 11편": 11편에는 Yoshida가 없고 리뷰·관점 2편이 들어 있다.
   - docs/11 §3의 [S25] 근거 지위: ELDER26은 순차 학습·망각을 시험하지 않았다.
3. **"빠르고 편향된 추론"의 '편향'이 정의·지표 없이 쓰였다.**

   → 결과 이전 조건부 prior q^-의 이득과 해악(일치 사례의 첫 시도 정확도, 불일치 사례의 conformity·correction latency)을 [08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md) §6에 넣었다.
4. **헌장 6층(같은 초기 모델이라도 이력에 따라 구조·계산·학습 정책이 달라짐)에 설계·평가가 없었다.**

   → F17(이력 분기) family와 [11-research-agenda.md](/home/jimmy/repos/full-continual-learning/docs/11-research-agenda.md) §6의 가설 문단을 넣었다.
5. **"SBL 이론 대부분을 적용·검증"(U-T06)은 선언만 있었다.**

   → 13개 이론을 조작 가능한 질문·family·필수 대조로 대응한 표를 넣었다. 추가 후보 family F13–F21과 수치 gate 레지스트리 틀도 [08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md) §2-1·§2-2·§6에 넣었다.
6. **Melete 시기 피드백은 메커니즘보다 이력으로 남은 것이 많았다.** 해당 항목은 다음과 같다.
   - H2·H3a·H5의 hit 경로 강화.
   - 최초 query 재읽기와 재개 지점.
   - 낯선 입력의 세 경로(쓰기 뒤 재읽기 / 가장 가까운 기존 schema / 보류).
   - B04의 흘려듣기(학습 가능성 신호).
   - B03·B08의 학습 철학(optimizer가 아니라 다섯 결정 축).
   - B11의 검증 수준 표기.

   → docs/04·05·06·07·08에 계약·평가로 넣었다.
7. **SUPERSEDED는 2건뿐이며 둘 다 U-T07이 근거다.**
   - "System 1을 담당하는 별도 부분"(F-UT06-11).
   - H3의 "LLM=slow, Melete=fast" 역할 분할(M-H3-01).

   H4의 text interface가 필수가 아니라는 서술은 사용자 진술이 아니라 정리자의 추론이었다. 그래서 OPEN으로 낮췄다([12-melete-lineage.md](/home/jimmy/repos/full-continual-learning/docs/12-melete-lineage.md) §1, [05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §10).
8. **반영이 탄탄했던 영역도 있다.**
   - 뇌 리듬 재고찰(04), 상태·저장 계약(07), 진화 정책(10).
   - 헌장의 비목표 7개.
   - 정답 없는 학습, 학습량과 충격도의 분리, evaluator 전용 oracle, frozen·no-memory 대조, observed/generated 출처 구분.

## 4. 반영 중 마스터가 고친 것

- **family 번호 충돌.** W1과 W2가 서로 다른 새 family 다섯 개에 같은 번호 F13–F17을 붙였다. W1의 F13–F17을 유지하고 W2의 후보를 F18–F21로 옮겼다. W2의 "이력 의존 편향"은 조작이 같은 F17(이력 분기)의 측정 항목으로 합쳤다. 이 번호를 가리키는 편집 3개(G2-03·G2-04·G2-17)도 같이 고쳤다.
- **수치 귀속 오류.** 학습된 graph의 추가 이득 0.48%는 Melete N0–N5 기록([12-melete-lineage.md](/home/jimmy/repos/full-continual-learning/docs/12-melete-lineage.md) §2)이다. J1이 아니므로 출처 표기를 바로잡았다.
- **controller 위치(D-14).** W4 초안은 schema 판단 구조(controller)를 P3부터 두고, P1에 최소형을 넣을지를 열린 결정으로 남겼다. 이를 P1의 규칙형 controller v0로 고쳤다.
  - **v0의 동작:** 익숙함 신호의 두 임계값으로 fast(쓰기 없이 답) / learn(쓰기 뒤 답) / deep(쓰기 뒤 retrofit 블록을 한 번 더 적용) 경로를 고르고, 결정 trace를 남긴다.
  - **근거 1:** U-T07 원문이 핵심 거동을 "익숙하면 매우 빠르게, 덜 익숙하면 rapid learning, 더 낯설면 더 깊은 loop"로 정의하고 "이 과정에서 입력 문맥에 대한 schema판단 mlp나 구조를 넣어서"라고 했다.
  - **근거 2:** 점진적 해상도 규칙은 P1이 핵심 여정 전체를 얇게 관통하라고 요구한다.
  - **원인 혼동 대응:** W4가 걱정한 원인 혼동은 `noctl` 대조 arm(controller 없이 learn 경로 고정)으로 분리한다.
  - **한계:** v0는 단조 규칙이라 "익숙해도 긴 합성은 깊게" 같은 다중 신호 결정을 다루지 못한다. 이는 P3의 학습된 controller로 올린다.
  - 이 판단은 사용자 확인 대기다.
- **H4 서술.** 새 로드맵 §9 대응표의 "정정으로 필수가 아니다"를 "정리자 추론, 사용자 확인 대기(OPEN)"로 낮췄다.
- **그 밖에.**
  - B 번호의 기간을 2026-09-27부터로 바로잡았다.
  - 산출물 정책 블록에 소제목과 시점(2026-11-12)을 달았다.
  - 같은 앵커에 붙는 블록은 논리 순서로 정렬했다.

## 5. 사용자 확인이 필요한 것

판정이나 설계가 아래 해석에 기대고 있다. 확인 전까지는 PROPOSAL 또는 OPEN이다.

**A. 판정의 전제**
1. U-T 번호가 대화 순서인가. U-T07의 "내가 원래 생각한건"은 새 결정인가, 원래 의도의 재서술인가. SUPERSEDED 2건이 이에 기댄다.
2. docs/02 정정표 1·2행과 T04 서술은 assistant의 재해석이다. 이를 수용하는가.
   - 1행: LLM에도 구조적 표상이 있을 수 있다.
   - 2행: schema·경험·직관을 사건·재사용 구조·빠른 적용으로 구분한다.
3. 헌장 §3의 4–6층(유용한 편향, 학습·사고 정책도 학습, 이력에 따른 자기 조직화)은 대화에서 도출한 해석이다. 이를 사용자 의도로 인정하는가.
4. U-T05의 "latent space(continual space)"를 continuous로 읽었다. 맞는가.
5. U-T11의 "모든 내용"은 주제별 재구성으로 충족된 것으로 보는가.
6. U-T09의 "Ali도 최근 관심있는 개념들"은 배경 정보인가, 우선순위 신호인가.

**B. 설계 해석**
7. H4의 text/vec2text 인터페이스를 필수 경로에서 내리는 것이 사용자 의사인가.
8. 사용자의 단계 처리(익숙함 정도 → 빠르게 / rapid learning / 더 깊은 loop)를 다중 신호 controller로 일반화하는 것을 수용하는가. docs/05 §4는 "낯섦 하나의 단조 함수로 제어하지 않는다"고 쓴다. P1 v0는 단조 규칙이고 P3에서 다중 신호로 간다.
9. U-T07의 "model needs sleep의 방법으로"가 A03의 특정 전환 절차를 뜻하는가, 일반적인 Sleep 통합을 뜻하는가.
10. B04의 "흘려듣기"를 학습 불가능이 아니라 학습 대상 제외·보류로 읽어도 되는가.
11. B08의 "오류(overfitting)를 유도"를 "성급한 일반화를 허용하고 시간축 반례로 줄인다(오류를 높이는 목적함수는 아님)"로 읽어도 되는가.
12. 점진적 해상도를 연구 저장소에 적용한 방식이 맞는가. P1을 "실제 CLI + 실제 소형 pretrained 모델" 제품으로 읽고, controller v0를 P1에 넣었다.

**C. 범위와 산출물**
13. 최종 사용 인터페이스는 무엇이며, Codex·Prime agent에 backend로 연결할 권한·인프라가 있는가(B12, 로드맵 D-11).
14. B15의 논문은 Melete 논문인가 FCL 논문인가. veridraft 개선 요청이 계속되는가.
15. B16의 superpowers 사용 지시를 FCL 작업에도 적용하는가.
16. Melete의 학습 방법 대장·atlas(50개 항목·13개 조합)를 FCL로 이관해 통합 모델 기준으로 다시 순위를 매기는가.
17. B01에서 "아이디어 없음"으로 남긴 eviction·forgetting·memory revision을 어느 phase에서 다룰 것인가.

**D. 승인이 필요한 틀과 수치**
18. 이번에 들어간 틀은 모두 PROPOSAL이다. 승인해야 확정된다.
    - family F13–F21
    - gate 레지스트리
    - 진화 권한 사다리 E0–E3
    - controller 해상도 사다리 v0–v2
    - 리듬 실험 A–D 배치
19. J1의 gate 수치(5pp 등)는 당시 master의 제안이었다. FCL의 gate 수치는 pilot 분산을 본 뒤 사전에 확정하고 사용자 승인을 받는다.

## 6. 남은 일

### 6.1 열린 결정

[09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md) §10의 D-01–D-14이며, 각 결정의 선택지·추천·비용은 그 표에 있다. 비용이 드는 결정은 결정 전에 실행하지 않는다.

| 결정 | 내용 |
|---|---|
| D-01 | base model. 추천은 SmolLM2-135M이고, 크기를 올리면 비용이 든다. |
| D-04 | 학습 계산 장소·시간 상한. 비용이 든다. |
| D-10 | self-evolution 자동화 범위. 비용이 든다. |
| D-12 | 두 번째 base model. 비용이 든다. |
| D-14 | controller 위치. 마스터 판단으로 P1 v0를 반영했고 사용자 확인 대기다. |

### 6.2 문헌 정독이 남은 항목

1. **재료 논문 원문 정독.** 사용자는 "논문 포함 읽고 이해하고"를 요청했다(U-T09). 아직 fulltext-read가 0편이다.
   - 대상: Titans, Nested Learning/HOPE, Language Models Need Sleep, Titan-Llama, Looped·Recurrent Depth, MoD·MoR, Depth-Attention 계열, Retrofitted Recurrence 등 A01–A04·A06–A15.
   - 현재 확인 깊이는 metadata-checked 이하다.
   - [05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §5의 F_CMS 식과 §7–§9는 이 깊이에서 쓴 프로젝트 제안이다.
   - 정독 우선순위와 대조할 질문은 [W1-gaps.txt](/home/jimmy/repos/full-continual-learning/research/2026-11-12-design-audit/W1-gaps.txt)의 G1-14에 있다.
2. **Melete neural-memory 연구층(B06).** 대상은 Sleep-time compute, agent memory, admission·commit·validity, canonical/materialized state 분리, Sleep을 transactional compiler로 보는 관점이다. 이를 [05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §11(Sleep)과 [07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md)에 어떻게 연결할지 검토해야 한다(G2-28).
3. **학습 규칙 후보 지도.** 대상은 fast-state(TTT·Titans·DeltaNet), eligibility/three-factor, 국소 신용(predictive coding·Forward-Forward 등) 계열이다. 각 계열의 원문 근거, library 존재, 수학적 정의 완결 여부를 표로 만든다([11-research-agenda.md](/home/jimmy/repos/full-continual-learning/docs/11-research-agenda.md) §7, G2-18·G2-29).
4. **뇌과학 근거 확인.** 확인할 질문은 둘이다.
   - 낯선 입력의 세 경로.
   - 이해 수준에 따라 받아들이는 다음 내용이 달라지는가(흘려듣기).

   후보 문헌은 N12–N19와 Schapiro et al. 2017이며, 아직 내용을 확인하지 않았다(G2-30).

### 6.3 이 감사로 성립하지 않는 것

- 원장 판정은 문서 대 문서의 대조다. 설계가 맞다는 증명이 아니다.
- 새로 들어간 문장 대부분은 PROPOSAL·OPEN이다. 구현·학습·효용 검증은 하나도 없다. [VALIDATION.md](/home/jimmy/repos/full-continual-learning/VALIDATION.md)의 "검증하지 않은 것"은 그대로다.
- B 번호(Melete 시기 피드백)는 세션 요약을 원천으로 썼다. 원 대화 전문 대조는 아니다.

## 7. 시각화 백서

이 감사와 반영된 설계를 웹 백서로 정리했다: https://fcl-system-one-whitepaper.vercel.app (소스와 조립기는 [README.md](/home/jimmy/repos/full-continual-learning/whitepaper/README.md)). 백서는 이 문서와 설계 문서를 다시 쓴 것이며 새 결과가 아니다.
