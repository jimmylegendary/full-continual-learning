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

## 3. Update / Create: 어디를 바꾸는가

| 경험의 상태 | 처리 후보 |
|---|---|
| 이미 충분히 설명됨 | Read; 큰 update를 필수로 하지 않음 |
| 구조는 맞고 대상·역할·조건이 새로움 | 기존 expert 또는 binding의 국소적 빠른 update |
| 같은 조건의 판단이 틀렸다는 근거 | 해당 기능 수정; 유효한 다른 조건 보호 |
| 다른 기존 schema로 설명됨 | 전환·조합; 불필요한 Create 억제 |
| 기존 구조에 수용하기 어려운 규칙성이 확인됨 | 새 expert 할당 또는 분화 |

검색 실패와 실제 구조적 새로움을 구별한다. 잘못 찾았다는 이유만으로 expert를 늘리지 않는다. 서로 다른 expert를 분리해도 같은 expert 내부의 간섭, shared encoder 변경, router 변화는 남을 수 있다. 따라서 쓰기 경계와 경계 내부의 가소성 모두 평가한다.

In-place update는 같은 schema ID의 파라미터를 계속 학습하는 기본 경로다. Versioning은 의미 있는 checkpoint/delta를 보존하는 별도 기능이며 매 gradient step을 새 expert로 만들지 않는다. 새 조건과 옛 조건이 모두 유효하면 단순 덮어쓰기 대신 분기·조건부 변환을 검토한다. 공유 의존성을 사용하는 확정 버전은 안전한 snapshot/검증 후 승격 대상으로 취급한다.

Replay, 유효 기능 보존, update 방향 제약, 신뢰도별 변경 강도, 분화는 비교할 후보다. Low-rank 간섭 제어 자체는 선행연구가 있으므로 독창성으로 과장하지 않는다. 새 질문은 task ID 없이 재사용할 구조와 변경 경계를 학습할 수 있는가다.

제안 문장: **새로운 경험을 전체 파라미터에 쓰는 대신 적합한 schema에 선택적으로 쓴다. 기존 구조가 맞으면 in-place adaptation을 하고, 수용할 구조가 없으면 용량을 할당한다.**

## 4. Delete / Retain: 무엇을 어떤 비용으로 남기는가

| 동작 | 줄이는 비용 | 지불하는 대가 |
|---|---|---|
| GPU → CPU/NVMe offload | 활성 메모리 | 전송·재적재 지연 |
| Rank/정밀도 축소 | 저장·때로는 계산 | 기능 손실 가능성 |
| 공통 구조 통합 | 중복 용량 | 통합 학습비용·간섭 위험 |
| 옛 버전 정리 | 이력 저장 | 복구 가능한 시점 감소 |
| Schema 폐기 | 전체 저장 | 기능 손실·재학습 비용 |

Offload는 지식 삭제가 아니다. 먼저 위치를 바꾸고, 이후 압축·통합을 평가하고, 예산이 부족하면 손실을 평가하며 폐기한다. 이 순서는 출발 정책이며 모든 workload의 최적 정책으로 확정하지 않는다.

통합은 가중치 평균이나 파라미터 유사성만으로 결정하지 않는다. 두 schema의 적용 문맥에서 기능을 확인하고, 공통 관계와 조건별 차이를 더 작은 표현에 학습한 뒤 새 조합 및 원래 조건을 검사한다. 중요한 예외는 별도 residual로 남기는 후보도 비교한다.

사용 빈도보다 **없어졌을 때의 기능 손실**을 평가한다. 드물지만 중요한 기능과 다른 expert로 대체 가능한 자주 쓰이는 기능을 구별한다.

$$
\widehat D_t(a)=\mathbb E_{z\sim\widehat Q_t}\left[\left(\ell(f_{a(\mathcal M_t)},z)-\ell(f_{\mathcal M_t},z)\right)_+\right].
$$

이는 기억 관리 동작 a의 손실 추정치다. 미래 분포를 정확히 안다는 보장이 없다. 최근 입력뿐 아니라 과거 대표 사례·재방문 조건·구조 전이를 포함한다. 평균 점수에 가려질 보호 조건은 별도 한도를 둔다. 직전 버전 대비 작은 손실만 보는 대신 장기 anchor와도 비교해 누적 열화를 측정한다.

재사용 가능성, 고유한 기능, 의존 관계, 재학습 비용, cold-load 비용을 함께 고려한다. 잘못 검색된 schema가 자주 읽혔다는 이유로 보존되는 자기 강화는 피한다. 모든 버전을 무한히 보존하는 것은 저장 문제의 해결이 아니며 의존성을 보존하는 checkpoint/delta 정리가 필요하다.

제안 문장: **지식 증가 비용을 암묵적 덮어쓰기로만 치르지 않는다. 위치·표현 크기·기능 가치를 관리하고 피할 수 없는 손실은 평가 가능한 선택적 망각으로 다룬다.**

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

### 제안문 초안 — 미발송

> Continual learning을 schema의 생명주기로 다루고자 합니다. 경험에서 재사용 가능한 관계 구조를 low-rank expert로 학습하고, 적합한 구조는 선택적으로 갱신하며, 수용하기 어려운 경험에는 새 expert를 할당합니다. 증가하는 지식은 offload·압축·통합·폐기로 관리하되 기능 손실과 저장·접근·학습 비용을 분리해 평가합니다. 현재 문맥과 목표에 맞는 schema를 검색·활성화하는 정책까지 결합하여, Nested Learning 및 MIRAS의 관점과 함께 장기적인 새 학습 능력과 유효 지식의 보존을 개선할 수 있는지 검증하고자 합니다.

## 8. 결정적인 실험

- **CU:** 같은 구조/새 개체, 같은 개체/새 구조, 잡음, 독립 정정, ABA. 새 학습과 무관 조건 회귀를 함께 측정한다.
- **D:** 같은 저장 예산에서 무작위·최근성·빈도 정책, offload-only, 압축/통합 정책 비교. 즉시 손실뿐 아니라 재방문과 재학습 비용 측정.
- **R:** 동일 expert 집합에서 oracle 선택, learned gate, random gate, stale index 비교. 원문 검색과 기능 retrieval의 비용·효과도 분리한다.
- **Joint:** 전체 파라미터, optimizer, 버전, index, replay, 학습·통합 계산을 합산한다. 한 task당 전체 모델/adapter 복제와 용량을 맞춘다.
- **System ONE:** controller를 우회한 depth×update 품질 곡선으로 모델 내부 효율 변화를 먼저 확인하고, 이후 learned routing의 실제 p50/p95 latency와 cold/warm-load를 측정한다.

전체 pipeline 점수만으로 세 원인의 실패를 구분하지 않는다. D의 순수 손실은 올바른 경로를 주는 조건으로 진단하고, R의 순수 실패는 expert 내용을 고정해 측정한다. 망각 감소가 학습 정지의 결과인지, 이득이 저장량 증가 때문인지 확인한다.

## 9. 남은 결정과 출처

Expert의 수·rank·검색 key·분화 기준·retention budget·압축 손실·commit 단위·정답 접근권은 아직 확정되지 않았다. 세 정책의 결합이 기존 방법보다 유리하다는 실험도 NOT RUN이다. 초기 정책을 고정한 작은 전체 MVP에서 시작해 독립 evaluator 아래 self-evolution을 적용한다.

[보충 참고문헌 및 확인 수준](../references/schema-lifecycle-2026-11-16.md). 기존 [상태 계약](07-state-and-storage.md), [평가](08-evaluation.md), [진화 정책](10-evolution-policy.md)과 함께 읽는다.

## 10. 별도 Sleep-time 주간 보고와의 교차 검토 — 2026-11-16

Memory utility·원본 증거 보존·learned memory I/O·장기 기술 획득 평가·LoRA effective rank/merging의 8건 선별 분석은 [연구 연결 기록](../research/2026-11-16-sleep-time-melete-integration.md)에 있다. **PROPOSAL / NOT RUN:** 기존 schema CRUD 구현·판정의 확정 변경이 아니라 실험 후보와 선행연구 경계다.
