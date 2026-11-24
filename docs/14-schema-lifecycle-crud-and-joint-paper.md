# 14. Schema 생명주기: Update/Create · Delete/Retain · Read/Activate

정리일: 2026-11-16. 출처: 이번 대화에서 사용자가 제시한 CRUD 관점과 이어진 assistant 답변. 사용자 질문은 [출처 기록](../sources/sync/2026-11-16-discussion.md)에 보존한다.

**USER:** 기존 지식인 low-rank expert를 schema에 따라 in-place update하고, 적합한 구조가 없으면 새 expert를 생성한다. Delete와 Read를 포함한 연구 구조를 정리해 Ali에게 공동논문 상세안을 제안하려 한다.

**PROPOSAL:** 아래 retention·retrieval 정책, 목적함수, 제안문과 실험은 그 요청에 대한 설계 제안이다. **NOT RUN:** 이번 문서화에서 모델 구현·실험·외부 발송은 하지 않았다. 관련 [schema 정의·변경 간섭](13-schema-decomposition-and-interference.md)과 [현행 로드맵](09-roadmap.md)을 대체하지 않는다.

## 1. 중심 문제와 주장

> 새 지식을 배우는 비용, 오래된 지식을 보존하는 비용, 필요한 지식에 접근하는 비용을 분리하고 schema 단위로 함께 최적화한다.

| 문제 | 메커니즘 제안 | 검증할 결과 |
|---|---|---|
| Update / Create | Schema-conditioned plasticity; 적합 expert의 in-place adaptation; 부적합 시 새 용량 할당 | 새 학습과 무관한 유효 지식의 손상 제한 |
| Delete / Retain | Offload·압축·통합·버전 정리·선택적 폐기 | 예산 안에서 기능 손실과 재접근 비용 통제 |
| Read / Activate | 문맥·목표에 따른 검색, 버전 확인, 적재, 선택·조합 | 저장된 지식을 현재 판단과 새로운 학습에 활용 |

종료 시점이 정해지지 않은 경험 흐름에서 새로 배우는 능력을 유지하는 것과, 모든 독립 정보를 유한 용량에 영구 보존하는 것은 다르다. 비용은 저장량 증가, 접근 지연, 통합 계산, 선택적 정보 손실 중 어느 형태로든 발생한다. 이를 기존 지식의 비의도적 덮어쓰기로만 지불하지 않도록 하는 것이 연구 목표다.

첫 실험 설정 후보는 활성 GPU 메모리·질의당 계산을 제한하고 외부 저장 증가를 허용하는 조건이다. 전체 저장량까지 고정한 조건은 별도 평가한다. 두 조건을 합쳐 무제한 무망각을 주장하지 않는다.

## 2. CRUD의 공통 단위

Schema expert는 여러 경험에서 재사용할 조건부 관계·예측·판단을 구현하는 low-rank 신경 계산 모듈이라는 운영적 가설을 둔다. 하나의 schema가 여러 layer의 파라미터 묶음에 걸칠 수 있다. Low-rank 자체가 schema의 증거는 아니며 구조 전이·개입·학습 효용을 확인한다.

$$
W_\ell^{\mathrm{eff}}(c)=W_\ell^{\mathrm{base}}+\sum_{i\in\mathcal A(c)}g_i(c)B_{\ell,i}A_{\ell,i}.
$$

위 식은 설명용 후보이고, 모든 expert를 동시에 활성화하거나 모든 경험을 새 expert로 만드는 계약이 아니다. Artifact에는 파라미터·fast state 외에도 검색 표현, 적용 조건, schema ID/version, backbone/encoder 의존성, 학습 재개 상태, 출처와 회귀 기록을 포함한다.

**OPEN (2026-11-17 검토):** 위 식의 i(schema expert)와 [05-integrated-architecture.md](05-integrated-architecture.md) §5의 j(CMS level)는 같은 축이 아니다. 형태(기반 + gate된 low-rank 합)는 같으나 j는 갱신 시간척도, i는 문맥으로 선택·할당되는 기능 단위다. 식도 이 문서는 가중치 공간, docs/05는 활성 공간 분기(σ 포함)다. P1은 fast level이 1개라 expert 집합이 없다. artifact의 '검색 표현'(index) 버전과 회귀 기록은 [07-state-and-storage.md](07-state-and-storage.md) §5의 manifest에 아직 필드가 없다.

## 3. Update / Create: 어디를 바꾸는가

| 경험의 상태 | 처리 후보 |
|---|---|
| 이미 충분히 설명됨 | Read; 큰 update를 필수로 하지 않음 |
| 구조는 맞고 대상·역할·조건이 새로움 | 기존 expert 또는 binding의 국소적 빠른 update |
| 같은 조건의 판단이 틀렸다는 근거 | 해당 기능 수정; 유효한 다른 조건 보호 |
| 다른 기존 schema로 설명됨 | 전환·조합; 불필요한 Create 억제 |
| 기존 구조에 수용하기 어려운 규칙성이 확인됨 | 새 expert 할당 또는 분화 |

검색 실패와 실제 구조적 새로움을 구별한다. 잘못 찾았다는 이유만으로 expert를 늘리지 않는다. 서로 다른 expert를 분리해도 같은 expert 내부의 간섭, shared encoder 변경, router 변화는 남을 수 있다. 따라서 쓰기 경계와 경계 내부의 가소성 모두 평가한다.

**OPEN (2026-11-17 검토):** 사용자 원문은 "문맥에 따라 적합한 schema를 못찾으면 create로 진행해서 새로운 low rank expert를 생성함"이다([2026-11-16-discussion.md](../sources/sync/2026-11-16-discussion.md), **USER**). 위 문단은 이를 '구조적 새로움이 확인될 때만 create'로 좁힌다. 검색이 놓친 경우를 가려내는 보수적 정제이지만 사용자가 확인한 해석이 아니며, 서로 다른 세 트리거(사용자 원문의 '못 찾음', 이 문서의 '구조적 새로움', STRUCTK25의 오류 크기: [05-integrated-architecture.md](05-integrated-architecture.md) §4)가 남는다. 사용자 확인 전에는 셋을 같은 예산에서 비교하는 대조로 두고 어느 하나를 기본으로 확정하지 않는다([09-roadmap.md](09-roadmap.md) §4-1).

In-place update는 같은 schema ID의 파라미터를 계속 학습하는 기본 경로다. Versioning은 의미 있는 checkpoint/delta를 보존하는 별도 기능이며 매 gradient step을 새 expert로 만들지 않는다. 새 조건과 옛 조건이 모두 유효하면 단순 덮어쓰기 대신 분기·조건부 변환을 검토한다. 공유 의존성을 사용하는 확정 버전은 안전한 snapshot/검증 후 승격 대상으로 취급한다.

**LITERATURE (2026-11-17 확인, 사용자 공유 링크 경유; 본문 부분 정독):** CRUD 어휘의 형식적 선례로 범주론 기반 SBL working paper([arXiv 2604.10589](https://arxiv.org/abs/2604.10589), v1 2026-04-12)가 있다. 이 논문은 syntactic 층의 기본 연산자를 {null, Comb(직렬·병렬), Encap, Ref, Ctx, Add, Del}로 두고, Add는 schema 집합에 새 schema를 더하고 Del은 집합에서 제거하는 집합 연산(중립·멱등·교환 법칙)으로 정의한다. 구현 층에는 syntactic schema를 고정한 채 표현 언어와 파라미터만 바꾸는 vertical 연산자 Transform·Update를 따로 둔다. 같은 구조의 파라미터 변경과 schema 집합의 구조 변경을 구분한다는 점이 이 절의 in-place update 대 새 expert 할당 구분과 닮았다. **OPEN:** 논문의 Del은 의존성·기능 손실·재학습 비용을 다루지 않는 집합 연산이고, 연산자 성질의 증명은 저자도 진행 중으로 적었으며 신경망 실험이 없다. 따라서 §4의 기능 손실 기반 retention이나 Update 정책의 근거로 쓰지 않고 어휘의 선행 사례로만 둔다. 읽은 범위는 초록·§1–§2·§3 일부(정의 3.1.1·3.1.2·3.1.10·3.1.11·3.2.4)·§5.2 일부·§7–§8이며 Update·Ref·Encap·Ctx의 세부 정의는 읽지 않았다.

Replay, 유효 기능 보존, update 방향 제약, 신뢰도별 변경 강도, 분화는 비교할 후보다. Low-rank 간섭 제어 자체는 선행연구가 있으므로 독창성으로 과장하지 않는다. 새 질문은 task ID 없이 재사용할 구조와 변경 경계를 학습할 수 있는가다.

제안 문장: **새로운 경험을 전체 파라미터에 쓰는 대신 적합한 schema에 선택적으로 쓴다. 기존 구조가 맞으면 in-place adaptation을 하고, 수용할 구조가 없으면 용량을 할당한다.**

**OPEN (2026-11-17 검토, 결과 등급 상한):** 위 제안 문장은 현재형 선언이라 문장 단독으로 읽으면 구현된 기제처럼 보인다. 현재 구현·학습은 0회(등급 0)이고 선택적 쓰기와 용량 할당은 로드맵 P3의 설계 대상이다([09-roadmap.md](09-roadmap.md) §3·§4). 논문·편지에 옮길 때는 이렇게 쓴다: "새로운 경험을 전체 파라미터에 쓰는 대신 적합한 schema 후보에 선택적으로 쓰는 방식을 설계한다. 기존 구조가 맞으면 in-place adaptation을, 수용할 구조가 없으면 용량 할당을 하는 정책을 같은 예산의 대조와 비교해 검증할 계획이다(NOT RUN)."

## 4. Delete / Retain: 무엇을 어떤 비용으로 남기는가

| 동작 | 줄이는 비용 | 지불하는 대가 |
|---|---|---|
| GPU → CPU/NVMe offload | 활성 메모리 | 전송·재적재 지연 |
| Rank/정밀도 축소 | 저장·때로는 계산 | 기능 손실 가능성 |
| 공통 구조 통합 | 중복 용량 | 통합 학습비용·간섭 위험 |
| 옛 버전 정리 | 이력 저장 | 복구 가능한 시점 감소 |
| Schema 폐기 | 전체 저장 | 기능 손실·재학습 비용 |

Offload는 지식 삭제가 아니다. 먼저 위치를 바꾸고, 이후 압축·통합을 평가하고, 예산이 부족하면 손실을 평가하며 폐기한다. 이 순서는 출발 정책이며 모든 workload의 최적 정책으로 확정하지 않는다.

**OPEN (2026-11-17 검토, 용어):** 이 저장소에서 '삭제'는 세 가지 다른 뜻으로 쓰인다. (1) source 삭제·철회: 원장에서 철회한 뒤 남은 source를 재생해 재구성한다([09-roadmap.md](09-roadmap.md) P1-T13, UJ1 ⑨). (2) 이 절의 Delete/Retain: 예산 아래 기능 손실을 평가하고 압축·통합·폐기를 고르는 기능적 망각/보존이다. 위 '지식 삭제'는 (1)이 아니라 (2)의 폐기를 뜻한다. (3) 학습 방법으로서의 가중치 삭제: 사전학습 가중치 일부를 0으로 두는 이진 mask만 학습해 새 능력을 얻는 방식이다([13-schema-decomposition-and-interference.md](13-schema-decomposition-and-interference.md) §4.2의 2026-11-17 LITERATURE 항목). (3)은 (1)의 삭제 요청 충족이나 (2)의 retention 정책의 근거가 아니며, 용어가 같다는 이유로 어느 쪽에도 쓰지 않는다. Update 경로의 비교 후보로만 남긴다.

구분표와 쓰기 규칙은 [07-state-and-storage.md](07-state-and-storage.md) §7, 평가 위치는 [08-evaluation.md](08-evaluation.md) §1·§2-2(제안 F22)를 본다. 통합·압축·폐기는 replay 재구성의 전제를 줄이므로 이 절의 정책은 source 삭제의 보장 범위를 좁힌다.

통합은 가중치 평균이나 파라미터 유사성만으로 결정하지 않는다. 두 schema의 적용 문맥에서 기능을 확인하고, 공통 관계와 조건별 차이를 더 작은 표현에 학습한 뒤 새 조합 및 원래 조건을 검사한다. 중요한 예외는 별도 residual로 남기는 후보도 비교한다.

**LITERATURE (2026-11-17 확인, 사용자 공유 링크 경유; 논문이 아니라 저자 조직의 블로그 게시물이며 동료 심사와 arXiv 번호가 없다):** TNG의 [Bring Your Own Expert! Extending MoE Models with New Domain Expertise](https://huggingface.co/blog/tngtech/bring-your-own-expert-extending-moe-models-with-ne)(Hugging Face Community Article, 2026-11-10)는 Qwen3.5-35B-A3B-Base를 고정하고 층마다 새 expert와 router row만 학습해(expert당 약 125M 파라미터, 8×B200에서 도메인당 약 반나절이라고 보고) Rust pass@1 0.62→0.73, Haskell 0.32→0.51을 보고했다. 독립 학습한 두 expert를 이어 붙인 checkpoint는 0.70·0.50을 유지했고, 같은 조건의 LoRA 두 개를 평균하면 0.67·0.36으로 base 쪽으로 되돌아갔으며 합산은 더 나빴다고 한다. 가중치 평균만으로 통합하지 않는다는 위 원칙과 §3의 '새 expert 할당' 경로에 대한 인접 사례다. **OPEN:** 코드 도메인 2개·base 1종·continued pretraining 단계에서만 시험됐고, 저자도 full post-training 뒤 유지 여부와 다수 expert 공존 시 간섭, expert parallelism 비용을 미해결로 적었다. MoE의 전체 expert 추가이므로 low-rank schema expert나 schema 학습의 증거가 아니다. 재현은 **NOT RUN**이다.

사용 빈도보다 **없어졌을 때의 기능 손실**을 평가한다. 드물지만 중요한 기능과 다른 expert로 대체 가능한 자주 쓰이는 기능을 구별한다.

$$
\widehat D_t(a)=\mathbb E_{z\sim\widehat Q_t}\left[\left(\ell(f_{a(\mathcal M_t)},z)-\ell(f_{\mathcal M_t},z)\right)_+\right].
$$

이는 기억 관리 동작 a의 손실 추정치다. 미래 분포를 정확히 안다는 보장이 없다. 최근 입력뿐 아니라 과거 대표 사례·재방문 조건·구조 전이를 포함한다. 평균 점수에 가려질 보호 조건은 별도 한도를 둔다. 직전 버전 대비 작은 손실만 보는 대신 장기 anchor와도 비교해 누적 열화를 측정한다.

**LITERATURE / OPEN (2026-11-17 검토, 선행 정의):** 위 $\widehat D_t(a)$의 꼴(손실 증가의 양수 부분의 기댓값)은 He와 Lin의 [Continual Learning from the Perspective of Compression](https://arxiv.org/abs/2006.15078)(ICML 2020 Lifelong Learning Workshop)이 forgetting을 '순차 학습한 모델로 이전 데이터를 압축할 때 description length의 증가'로 정의한 식 $F=\max(L(x|\theta_j)-L(x|\theta_i),0)$와 같은 형태다. 새 정의로 주장하지 않는다. 차이는 평가 대상이 이전 데이터가 아니라 기억 관리 동작 a를 적용한 뒤의 상태이고 분포가 과거 표본이 아니라 추정 분포 $\widehat Q_t$라는 점이다. 그 논문은 forgetting이 음수가 되지 않도록 max를 쓴다고 적었으므로, 손실이 줄어드는 압축·폐기를 0으로 처리하는 성질도 같다. 확인 범위는 공개 PDF 본문 발췌이며 재현은 하지 않았다.

재사용 가능성, 고유한 기능, 의존 관계, 재학습 비용, cold-load 비용을 함께 고려한다. 잘못 검색된 schema가 자주 읽혔다는 이유로 보존되는 자기 강화는 피한다. 모든 버전을 무한히 보존하는 것은 저장 문제의 해결이 아니며 의존성을 보존하는 checkpoint/delta 정리가 필요하다.

제안 문장: **지식 증가 비용을 암묵적 덮어쓰기로만 치르지 않는다. 위치·표현 크기·기능 가치를 관리하고 피할 수 없는 손실은 평가 가능한 선택적 망각으로 다룬다.**

**OPEN (2026-11-17 검토, 결과 등급 상한):** 위 제안 문장은 현재형 선언이다. 관리 정책은 P4(offload·Sleep 통합)–P5(압축·폐기)에서 비로소 평가되고 기능 손실 추정기($\widehat D_t(a)$)는 검증되지 않았다. 옮길 때는 이렇게 쓴다: "지식 증가 비용을 암묵적 덮어쓰기로만 치르지 않도록, 위치·표현 크기·기능 가치를 관리하고 피할 수 없는 손실은 평가 가능한 선택적 망각으로 다루는 정책을 설계한다. 기능 손실 추정기는 아직 검증하지 않았다(NOT RUN)."

## 5. Read / Activate: 무엇을 지금 쓰는가

문맥 표현 → 후보 검색 → 적용 조건·버전 확인 → expert 적재 → 소수 선택·조합 → 결과에 따른 재평가.

검색 key는 schema의 주소이지 schema 자체가 아니다. 주제 유사성뿐 아니라 역할·관계·목표·유효 조건·오적용 조건·표현 공간 호환성을 반영하는 후보를 학습한다. 비슷한 단어지만 관계가 반대인 조건을 구별해야 한다.

큰 집합에서 후보를 좁히는 검색과 실제 계산에 참여시키는 gating을 분리한다. Routing confidence만으로 사실성을 판단하지 않는다. 현재 증거로 구별되지 않는 경우 여러 가능성, 보류, 더 깊은 계산을 허용한다.

$$
\mathcal A_t^{\mathrm{answer}}\ne\mathcal A_t^{\mathrm{learning}},\qquad
\mathcal A_t^{\mathrm{write}}\subseteq\mathcal A_t^{\mathrm{learning}}.
$$

답변에는 최신 유효 schema를 쓰더라도 학습에는 과거 버전과 관련 구조를 함께 참조할 수 있다. 많이 읽는 것과 모두 수정하는 것은 다르다. 과거 조건을 묻는 질문에서는 최신 버전이 아닌 다른 버전이 적합할 수 있다.

In-place update 후에는 검색 표현·적용 범위도 점검한다. 공유 encoder가 바뀌면 index의 의미가 바뀔 수 있으므로 재인덱싱·호환성 검사가 필요하다. Retrieval 실패는 파라미터 기억의 손상과 분리해서 측정한다.

제안 문장: **원문을 매번 길게 넣는 대신 현재 문맥에 적합한 신경 계산 기능을 검색·활성화하고, 판단용 읽기와 학습용 참조를 구분한다.**

**OPEN (2026-11-17 검토, 결과 등급 상한):** 위 제안 문장의 '대신'은 토큰·계산 절감을 함의한다. '계산 절감'은 등급 3 이전에 쓸 수 없고([09-roadmap.md](09-roadmap.md) §3), raw history를 넣는 `ctx` 대조는 P1부터 있으며 사전 명세한 예산에서 `ctx`가 같거나 낫다면 그 경로를 유지한다([09-roadmap.md](09-roadmap.md) §7). 학습된 선택은 P3, 외부 retrieval은 P5다. 옮길 때는 이렇게 쓴다: "원문을 매번 넣는 방식(raw-history 대조)과 같은 토큰·계산 예산에서 비교하는 것을 전제로, 현재 문맥에 적합한 신경 계산 기능을 검색·활성화하고 판단용 읽기와 학습용 참조를 구분하는 방법을 설계한다. 토큰·계산 절감은 아직 주장하지 않는다(NOT RUN)."

**OPEN (2026-11-17 검토):** 위 흐름에는 원본 근거를 되짚는 단계가 없다. 외부 agent memory 연구 WikiTrace(arXiv:2611.14320, 2026-11-10 v1)는 잘못되거나 맥락에 맞지 않는 교훈을 쓰는 것이 원래 풀던 과제를 틀리게 만드는 memory-induced degradation을 다루며, 교훈을 요약과 원본 trajectory에 연결해 두고 읽는 시점에 확인한다고 보고한다. HiVe-Mem(arXiv:2611.12872, 2026-11-09 v1)은 관계 기반 후보 확장과 질의별 evidence 선택을 보고한다. 둘 다 arXiv preprint이고 저자 초록 수준의 확인이며 이 저장소에서 재현하지 않았고 neural schema 지속학습의 증거로 세지 않는다. 후보로 둘 것은 원본 관측 → 파생 해석 → schema version → 색인의 계보를 확인하는 별도 Read 경로이며, 근거 재읽기(프롬프트에 근거를 다시 넣는 일)와 expert 활성화를 다른 연산으로 두고 token·지연 비용을 따로 보고하는 것이다. 현재 문서에서는 §8 말미의 Read 대조군만 이를 다룬다. 계보·색인의 상태 쪽 근거는 [07-state-and-storage.md](07-state-and-storage.md) §2·§6·§7에 있다. 상세: [2026-11-16-memory-evidence-read-supplement.md](../research/2026-11-16-memory-evidence-read-supplement.md).

## 6. 결합된 생명주기와 목적함수

Update는 검색 표현·버전·보존 가치에 영향을 준다. Create는 index와 예산에 연결된다. 압축·통합·폐기는 의존성과 검색 경로를 바꾼다. Read의 실패는 검색 실패·지식 부족·오염을 진단하는 신호다.

$$
\min_{\pi_{CU},\pi_D,\pi_R}\mathbb E\sum_{t=1}^{T}\left[\ell_t+\lambda C_t^{\mathrm{total}}\right]
$$

$$
B_t^{\mathrm{active}}\le B_{\mathrm{active}},\qquad B_t^{\mathrm{total}}\le B_{\mathrm{total}}(t),\qquad\widehat D_t^{\mathrm{protected}}\le\epsilon.
$$

총비용에는 forward, write/backward, router, 검색, 전송, Sleep, 통합, index 유지 비용을 포함한다. 목적함수와 추정 제약을 적었다고 실제 보호 보장이 생기는 것은 아니다. 보존 조건, 추정 오차, 장기 분포 이동을 별도로 검증한다.

## 7. Ali 공동논문 제안의 흐름

1. **문제:** 간섭·보존 비용·접근 비용을 동시에 해결해야 하는 장기 경험 학습.
2. **공통 단위:** task별 단순 adapter가 아니라 여러 과제에 재사용할 low-rank schema expert.
3. **세 정책:** 선택적 쓰기·용량 할당, 기능 손실 기반 retention, 문맥 기반 addressing/activation.
4. **선행연구 접점:** Nested Learning의 다중 학습 수준과 MIRAS의 retention 관점을 schema 내부 학습에 연결한다. MIRAS가 retention을 이미 다룬다는 점을 명시하며 '기존은 Update만 한다'고 주장하지 않는다.
5. **공동 연구 질문:** 기존 expert의 수정 가능 조건, 기능 거리와 분화·압축 기준, 미래 효용을 통한 정책 공동학습.
6. **검증:** task ID 없는 구조 전이·재방문·새 관계 등장, 동일 활성/전체 자원에서 비교.

**OPEN (2026-11-17 검토, 결과 등급 상한 점검):** 현재 통합 모델 구현·학습은 0회(등급 0)이고 합성 Phase-0는 통합 PoC가 아니다. 등급 0에서는 '설계됨'·'NOT RUN'만 쓸 수 있다([09-roadmap.md](09-roadmap.md) §3). 위 6항목 중 아래는 문장 단독으로 읽으면 상한을 넘는다.
- 2 공통 단위: 가설이 확정형으로 적혔다. "공통 단위(가설): 여러 과제에 재사용될 수 있다고 가정하는 low-rank expert(schema 후보). 재사용·기능적 역할·학습 효용이 실험으로 확인되기 전에는 schema라고 부르지 않는다."
- 5 공동 연구 질문: 정책 공동학습은 로드맵 P1–P5에 일정이 없다. "탐색 후보(일정 없음): 기존 expert의 수정 가능 조건, 기능 거리와 분화·압축 기준. 미래 효용을 통한 정책 공동학습은 현재 로드맵 밖의 장기 질문이다."
- 주의: 3은 기능 손실 기반 retention의 추정기가 미검증이므로 '설계 후보'로 쓴다. 4의 MIRAS(arXiv 2504.13173)는 280dc9a 기준 catalog에 없었고 이 검토가 후보 행으로 올렸다. 이번 검토에서 발췌 확인한 범위에서 MIRAS의 retention은 순환 memory 갱신의 retention gate(학습과 기존 상태 유지의 균형을 정하는 정규화)이며 schema·artifact 단위의 보존 예산이나 폐기를 다룬 것이 아니다. '관점을 연결한다'는 가설로 쓰고 MIRAS가 이 문제를 이미 다룬다고 읽히지 않게 한다([schema-lifecycle-2026-11-16.md](../references/schema-lifecycle-2026-11-16.md)). 6은 전체 저장 자원의 일치가 budget meter에 없고 결과가 합성 family·소형 모델 범위이므로 그 범위를 적는다.
- 정책은 단순 대조(같은 계산·쓰기 예산의 고정·무구조·항상-갱신, raw history `ctx`)보다 나은 때에만 필요성을 주장한다([09-roadmap.md](09-roadmap.md) §7).

### 제안문 초안 — 미발송

> Continual learning을 schema의 생명주기로 다루고자 합니다. 경험에서 재사용 가능한 관계 구조를 low-rank expert로 학습하고, 적합한 구조는 선택적으로 갱신하며, 수용하기 어려운 경험에는 새 expert를 할당합니다. 증가하는 지식은 offload·압축·통합·폐기로 관리하되 기능 손실과 저장·접근·학습 비용을 분리해 평가합니다. 현재 문맥과 목표에 맞는 schema를 검색·활성화하는 정책까지 결합하여, Nested Learning 및 MIRAS의 관점과 함께 장기적인 새 학습 능력과 유효 지식의 보존을 개선할 수 있는지 검증하고자 합니다.

**OPEN (2026-11-17 검토, 미발송 초안의 상한 점검):** 위 초안은 발송하지 않았다. 둘째·셋째 문장("학습하고… 갱신하며… 할당합니다", "관리하되… 평가합니다")은 구현된 능력처럼 읽히고, 압축·통합·폐기는 로드맵에 일정이 없으며(P4 상한은 '삭제 보장 없음'), 초안에는 현재 상태(구현·실험 0회)와 단순 대조를 두겠다는 약속이 없다. 사용자가 승인하기 전에는 위 초안을 바꾸지 않는다. 수정 문안 제안:

> Continual learning을 schema의 생명주기(Update·Create, Delete·Retain, Read·Activate)로 다루는 연구를 설계하고 있습니다. 아직 구현과 실험을 하지 않은 설계 단계입니다. 경험에서 재사용 가능한 관계 구조를 low-rank expert(schema 후보)로 학습·갱신하고 수용하기 어려운 경험에는 새 expert를 할당하는 방법을 제안하며, 이 구조가 실제로 재사용되는지는 실험으로 확인할 계획입니다. 증가하는 지식은 offload·압축·통합·폐기로 관리하는 정책을 설계 중이며 기능 손실과 저장·접근·학습 비용을 분리해 평가하려 합니다. 현재 문맥과 목표에 맞는 expert를 검색·활성화하는 정책까지 결합해, Nested Learning 및 MIRAS의 관점과 함께, 같은 계산·쓰기 예산의 단순한 대조(raw history 포함)보다 장기적인 새 학습 능력과 유효 지식의 보존을 개선할 수 있는지 검증하고자 합니다. 단순한 방법이 같거나 낫다면 그 범위에서 복잡한 구조의 필요성은 주장하지 않겠습니다.

Ali가 관심 있다고 전해진 loop transformer·MoD·MoR·depth attention 축([user-statements.md](../sources/user-statements.md) U-T09)은 이 초안에 없다. 넣을지는 사용자 판단이다(**OPEN**).

## 8. 결정적인 실험

- **CU:** 같은 구조/새 개체, 같은 개체/새 구조, 잡음, 독립 정정, ABA. 새 학습과 무관 조건 회귀를 함께 측정한다.
- **D:** 같은 저장 예산에서 무작위·최근성·빈도 정책, offload-only, 압축/통합 정책 비교. 즉시 손실뿐 아니라 재방문과 재학습 비용 측정.
- **R:** 동일 expert 집합에서 oracle 선택, learned gate, random gate, stale index 비교. 원문 검색과 기능 retrieval의 비용·효과도 분리한다.
- **Joint:** 전체 파라미터, optimizer, 버전, index, replay, 학습·통합 계산을 합산한다. 한 task당 전체 모델/adapter 복제와 용량을 맞춘다.
- **System ONE:** controller를 우회한 depth×update 품질 곡선으로 모델 내부 효율 변화를 먼저 확인하고, 이후 learned routing의 실제 p50/p95 latency와 cold/warm-load를 측정한다.

전체 pipeline 점수만으로 세 원인의 실패를 구분하지 않는다. D의 순수 손실은 올바른 경로를 주는 조건으로 진단하고, R의 순수 실패는 expert 내용을 고정해 측정한다. 망각 감소가 학습 정지의 결과인지, 이득이 저장량 증가 때문인지 확인한다.

**추가 Read 대조군 (PROPOSAL / NOT RUN):** [WikiTrace·HiVe-Mem 보충 검토](../research/2026-11-16-memory-evidence-read-supplement.md)를 참고하여 schema-only vs 원본 근거 확인 가능한 Read, 기억 사용으로 인한 회귀, retrieval 토큰·지연을 평가한다. External agent memory의 검증을 neural schema 학습의 증거로 취급하지 않는다.

**OPEN (2026-11-17 검토, 배치):** 이 절의 CU·D·R·Joint·System ONE은 [09-roadmap.md](09-roadmap.md) §6-1에 기존 phase의 판독으로 배치했다(System ONE은 [13-schema-decomposition-and-interference.md](13-schema-decomposition-and-interference.md) §10 E와 같은 실험이고 Joint는 C와 합쳤다). D(보존 정책 비교)와 R(선택 오류)에는 대응하는 family가 없어 [08-evaluation.md](08-evaluation.md) §2-2 뒤에 F22·F23을 제안했다. 이 절의 비교가 성립하려면 공유 파라미터를 갱신하는 arm(`ftall`)과 task별 oracle adapter(`adapters`)가 arm 표에 필요하다. 'D'의 '삭제'는 기능적 망각/보존이며 source 삭제와 다르다([07-state-and-storage.md](07-state-and-storage.md) §7).

**OPEN (2026-11-17 검토):** 위 결정적 실험(CU·D·R·Joint·System ONE)도 별도 phase가 아니라 P2–P4의 작업이며, 자원 배정과 규모 가늠은 [15-compute-plan.md](15-compute-plan.md) §5.3에 있다(NOT RUN).

## 9. 남은 결정과 출처

Expert의 수·rank·검색 key·분화 기준·retention budget·압축 손실·commit 단위·정답 접근권은 아직 확정되지 않았다. 세 정책의 결합이 기존 방법보다 유리하다는 실험도 NOT RUN이다. 초기 정책을 고정한 작은 전체 MVP에서 시작해 독립 evaluator 아래 self-evolution을 적용한다.

[보충 참고문헌 및 확인 수준](../references/schema-lifecycle-2026-11-16.md). 기존 [상태 계약](07-state-and-storage.md), [평가](08-evaluation.md), [진화 정책](10-evolution-policy.md)과 함께 읽는다.

## 10. 별도 Sleep-time 주간 보고와의 교차 검토 — 2026-11-16

Memory utility·원본 증거 보존·learned memory I/O·장기 기술 획득 평가·LoRA effective rank/merging의 8건 선별 분석은 [연구 연결 기록](../research/2026-11-16-sleep-time-melete-integration.md)에 있다. **PROPOSAL / NOT RUN:** 기존 schema CRUD 구현·판정의 확정 변경이 아니라 실험 후보와 선행연구 경계다.

**OPEN (2026-11-17 검토):** 이 절은 8건만 가리킨다. 이후 보충 선별 4건은 여기에 연결돼 있지 않다. WikiTrace·HiVe-Mem(증거 연계 Read, [2026-11-16-memory-evidence-read-supplement.md](../research/2026-11-16-memory-evidence-read-supplement.md))은 §8 말미에만 있고, SoMem(외부 근거 보존 재조직)과 recursive state capacity(읽기 충분 상태 대 갱신 충분 상태)는 [2026-11-17-sleep-time-melete-selected-addendum.md](../research/2026-11-17-sleep-time-melete-selected-addendum.md)와 README에만 있다. 또 위 연구 연결의 실험 후보와 Delete/Retain의 '미래 갱신에 필요한 상태', Read의 '증거 계보 확인·색인 재구축'은 §3–§5 본문에 합쳐지지 않았다. 반영 후보 위치는 [07-state-and-storage.md](07-state-and-storage.md) §5·§7, [08-evaluation.md](08-evaluation.md)의 F-CI·§4, [09-roadmap.md](09-roadmap.md) P2·P4의 후보 readout이다(모두 제안·NOT RUN).

**Read/Activate 보충 (2026-11-24; PROPOSAL / OPEN / NOT RUN):** [공유 기억과 조건부 Read 대조](../research/2026-11-24-shared-schema-read-control.md)는 동일 expert 내용에서 depth별 복제와 공유 고정/조건부 read의 차이를 비교하는 후보를 추가한다. Chorus의 이산 n-gram 주소는 neural schema 선택·갱신을 증명하지 않는다. 읽기·학습·저장 비용, answer/learning read 및 offload/delete의 구분과 기존 결정 상태를 유지한다.
