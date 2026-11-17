# 13. Schema 정의·분해·변경 간섭: LLM과 System ONE의 통합 설명

게시일: **2026-11-14**. 기준 저장소 revision: `6db0ccfe2ea407805129594b9b2ecaae7e50b3ec`.

## 문서의 지위

사용자가 게시를 요청한 schema 정의·분해·catastrophic forgetting 질의와 검토 답변을 연구 문서로 보존한다. 핵심 주장·수식·조건·대조군·한계와 참고문헌을 포함한 재구성이며, 채팅 로그의 문자 단위 덤프는 아니다.

- **USER:** 경험/지식을 schema로 학습하고, versioning·offload·retrieval·context gating으로 활용한다. 기존 LLM과 Melete를 schema 관점에서 함께 설명하려 한다.
- **USER-HYPOTHESIS:** LLM의 schema 중첩, post-training의 선택·분리 효과, 중첩에 의한 망각, 분해를 통한 지속학습은 사용자의 검증 대상 가설이다. 확립된 사실로 표시하지 않는다.
- **PROPOSAL:** 아래의 정의·artifact 계약·수식 적용·실험은 검토 제안이다. 게시 승인이 모든 구현 결정을 확정하거나 기존 로드맵을 대체하지는 않는다.
- **LITERATURE:** 문헌 연결의 대부분은 직전 답변을 보존한 것이다. 일부 식별자는 이번 게시에서 공식 검색으로 확인했으며, 수준은 [참고문헌](../references/schema-decomposition-2026-11-14.md)에 표시한다. 전편 재정독·수치 재검증을 수행한 것은 아니다.
- **DERIVATION:** 단순한 연합기억·Taylor 전개·계산 의존성·유한 정보량에 관한 조건부 설명이다. 정리의 독창성이나 LLM 전체의 무망각을 주장하지 않는다.
- **NOT RUN:** 이번 게시에서 모델 구현·학습·GPU 실행·PoC·실험적 효용 검증은 수행하지 않았다.

**OPEN (2026-11-17 검토):** 위 USER·USER-HYPOTHESIS 표시는 2026-11-14 ChatGPT 재구성 문서 안의 표기이며, 이 저장소에는 그 대화의 사용자 원문 블록이 없다([user-statements.md](/home/jimmy/repos/full-continual-learning/sources/user-statements.md), [2026-11-16-discussion.md](/home/jimmy/repos/full-continual-learning/sources/sync/2026-11-16-discussion.md) 확인). 따라서 §1의 「사용자 제안」과 가설 1–4는 사용자 원문이 아니라 **재구성**이다. 원문으로 확인되는 사용자 진술은 U-T06·U-T07(schema 학습, offload·versioning·retrieval, 입력 문맥 schema 판단 구조, LLM이 하나의 schema를 학습하고 post-training이 이를 sub schema로 분화시켰다는 가설)과 2026-11-16 블록(지속학습의 목적, in-place update·create)뿐이며 이 문서의 내용과는 겹치는 부분만 일치한다. 또한 `DERIVATION`은 [SYNC_POLICY.md](/home/jimmy/repos/full-continual-learning/SYNC_POLICY.md)의 증거 표기 목록에 없으므로 §7의 유도는 **PROPOSAL(직접 유도)**로 읽고 아래 2026-11-17 검토 주석과 함께 본다.

관련 문서: [기반 이론](03-foundations.md), [통합 모델](05-integrated-architecture.md), [수학적 명세](06-mathematical-framework.md), [상태와 저장](07-state-and-storage.md), [평가](08-evaluation.md), [현행 로드맵](09-roadmap.md), [열린 연구 의제](11-research-agenda.md).

## 1. 사용자 제안과 검토 결론

사용자의 출발 개념은 다음과 같다.

> 경험/지식은 schema의 형태로 학습되고, schema를 versioning·외부 offload·retrieval하며, context gating에 따라 알맞은 schema를 가져다 쓴다.

이어 제안한 설명은 다음과 같다.

1. LLM은 여러 schema가 분리되지 않고 엉켜 있는 상태로 학습되었다.
2. Post-training/reasoning/RL/CoT는 특정 schema가 더 잘 활성화되도록 가지치기하고 어느 정도 분리한 것일 수 있다.
3. Schema의 중첩·간섭 때문에 새로운 학습에서 catastrophic forgetting이 발생한다.
4. Schema를 분해해서 지속학습하면 망각을 없애거나 뒤로 늦출 수 있다.
5. Nested Learning이 여러 sequence layer를 최적화 관점으로 통합하듯, schema로 LLM과 Melete를 함께 설명하고 싶다.

**OPEN (2026-11-17 검토):** 가설 1–2와 사용자 원문의 표현 차이. U-T06 원문은 「LLM은 매우 많은 data를 기반으로 하나의 schema를 학습한것이고」, 「post training/RL을 통한 alignment는 해당 schema를 여러 sub schema로의 분화 기능을 만든 것」이라고 하는데, 가설 1은 「여러 schema가 분리되지 않고 엉켜 있는 상태로 학습되었다」고 쓴다. 같은 가설의 다른 표현인지 수정된 가설인지는 알 수 없다. 원문이 있는 쪽은 U-T06뿐이므로 [11-research-agenda.md](/home/jimmy/repos/full-continual-learning/docs/11-research-agenda.md) §1의 서술을 유지하고 가설 1–2는 사용자 확인 전까지 재구성으로 둔다. 가설 3–4의 동기인 지속학습 목적(「재앙적 망각 없이 학습」)은 2026-11-16 원문에 있으나, 중첩이 망각을 일으키고 분해가 이를 없앨 수 있다는 인과 가설은 원문이 없다. 또 이 저장소는 망각을 없앤다고 약속하지 않는다. 유한 총상태에서 독립 사실의 무한 무망각은 §7.5의 한계로 불가능하므로 정직한 상한은 망각을 늦출 수 있다는 것까지다.

검토의 핵심 수정은 **중첩 제거보다 유해한 변경 간섭의 제어**다.

> 기존 LLM과 Melete 모두 경험에서 재사용 가능한 조건부 계산 구조를 학습한다. 차이는 schema의 존재 여부가 아니라 선택·조합·변경을 얼마나 분리해 제어하는가에 있다. Melete는 유익한 공유를 유지하면서 새로운 학습이 무관한 기존 기능을 훼손하지 않도록 변경의 영향 범위를 제한한다.

**OPEN (2026-11-17 검토):** 위 인용문의 「Melete는 … 제한한다」는 설계 목표를 현재형으로 쓴 것이다. 구현·학습·효용 검증은 없고(NOT RUN, [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md#3-결과-등급과-상한)의 등급 0과 같다) P1의 정정은 국소 갱신과 부작용 측정까지이고 수정 메커니즘은 없다(09 §4). 이 저장소의 통합 모델 명칭은 System ONE이고 Melete는 계보상의 출발점([12-melete-lineage.md](/home/jimmy/repos/full-continual-learning/docs/12-melete-lineage.md))이므로 문장의 주어가 어느 쪽인지도 통합 시 정한다. 안전한 표현은 「설계 목표: …」다.

이 방향은 연구 프레임워크로 발전시킬 가치가 있다. 다만 post-training 전체를 schema 분리 하나로 설명하는 것은 확정 결론이 아니라 경쟁 가설이다.

## 2. Schema의 운영적 정의

> **Schema는 여러 경험에서 학습되어 새로운 대상과 상황에 재사용되는, 조건부 관계·예측·판단의 신경 계산 구조다.**

손에 잡히게 말하면 **어떤 조건에서, 대상들 사이의 어떤 관계를 이용해, 무엇을 예상하고 어떻게 판단할 것인가를 수행하는 학습된 계산 단위**다.

단위는 뉴런·벡터·layer 하나라는 뜻이 아니다. 여러 층의 가중치와 활동·동역학에 분산될 수 있다. Goudar 등의 연구는 재사용되는 부분공간과 동역학을 분석하며, 가중치의 변화와 기능의 유지를 구분하는 관련 근거다. 이 과제별 결과를 범용 LLM의 schema 지도라고 확대하지 않는다. [R01]

### 2.1 승인 절차의 예

여러 조직의 업무 경험에서 선행 조건, 권한 범위, 상태 전이에 따라 다음 행동을 판단하는 구조를 배웠다고 하자.

| 구분 | 예 |
|---|---|
| Schema | 선행 조건·권한·상태 전이를 사용해 승인 가능성과 다음 행동을 판단 |
| Binding | 현재 조직의 어떤 사람이 승인자 역할인지 연결 |
| 개별 경험 | 특정 요청의 승인·거절 사건 |
| Schema 수정 | 새로운 예외 조건이나 권한 관계의 학습 |

새 조직에서 기존 구조에 역할과 조건을 연결하면 된다. 설명을 문장으로 했다는 이유로 내부가 symbolic 규칙 문자열이어야 하는 것은 아니다. Continuous neural representation을 우선한다.

### 2.2 판정 기준

- **재사용성:** 개체·표현·수치가 달라도 같은 관계를 활용한다.
- **기능적 역할:** 표현이나 계산에 개입하면 관련 판단·전이가 선택적으로 달라진다.
- **학습 효용:** 관련된 새 경험의 학습이나 이후 계산 비용에 실제 도움이 되는지 평가한다.

좋은 군집이나 파일의 존재만으로 판정하지 않는다. 학습 효용의 크기는 실험 결과여야 한다. 정의에 무망각을 넣어 망각하는 후보를 schema가 아니라고 제외하지 않는다. **Schema인지와 잘 분리된 schema인지는 별개다.**

## 3. Schema와 versioned artifact

> **Schema는 기능적 계산 구조이며, schema artifact는 특정 모델에서 그 구조를 재현·사용·갱신하기 위한 버전이 있는 실행 상태 묶음이다.**

$$
\mathcal A_s^{(v)}=(\phi_s^{(v)},B_s^{(v)},C_s^{(v)},D_s^{(v)},Q_s^{(v)}).
$$

| 구성 | 의미 |
|---|---|
| $\phi_s^{(v)}$ | 가중치·delta·fast memory 등 실제 신경 상태 |
| $B_s^{(v)}$ | 현재 개체·역할과 구조를 연결하는 binding 인터페이스 |
| $C_s^{(v)}$ | 적용 맥락·유효 조건·검색용 표현 |
| $D_s^{(v)}$ | backbone·encoder·다른 schema의 의존 버전 |
| $Q_s^{(v)}$ | 학습 재개용 optimizer·eligibility·출처 상태 등 |

이는 계약 후보다. 항목마다 별도의 독립 파일을 강제하지 않고 공유 항목을 허용한다. 파일이 분리되어도 공통 encoder가 바뀌면 의미가 함께 변할 수 있다. **저장 분리와 기능 분리는 다르다.**

**OPEN (2026-11-17 검토):** (1) 위 다섯 성분과 [07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md) §5 manifest의 대응은 다음과 같다. φ ↔ `slow_weights_or_deltas`·`fast_weights`·`parameter_shapes`, C ↔ `applicability`·`confidence_calibration`·`validation_scope`, D ↔ `base_model_revision`·`encoder_revision`·`tokenizer_revision`, Q ↔ `optimizer_moments`·`update_counters`·`consolidation_state`·`source_root_ids`. B(binding 인터페이스)에 해당하는 필드는 없다(`layer_bindings`는 layer 부착 정보로 다른 뜻). manifest에는 있고 튜플에는 없는 것은 `retention_policy`·`deletion_dependencies`·`migration_status`·`content_hashes` 등이며, 「다른 schema의 의존 버전」을 담는 필드는 manifest에 없다. 설명용 대응이며 manifest 서식을 바꾸지 않는다. (2) C는 「적용 맥락·유효 조건」과 「검색용 표현」을 한 성분에 묶었으나 07 §7은 둘을 분리한다(retrieval visibility와 applicability). 계약으로 옮길 때 C 안에서 필드를 나눈다. (3) 기호 충돌: φ·θ·b·B·C·D·Q·𝒜가 [06-mathematical-framework.md](/home/jimmy/repos/full-continual-learning/docs/06-mathematical-framework.md)·05 §5·14 §2와 다른 뜻으로 쓰이고, 이 문서 안에서도 D(§3 의존 버전, §7.2 분포, §7.3 전체 의존성)와 v(§3 version, §7.1 값)가 겹친다. 대응표는 06 §1 주석에 있다.

모든 경험을 새로운 schema 하나로 만들 필요는 없다. 경험은 schema를 형성·선택·수정하거나 새로운 내용을 결합할 수 있다. 개별 사건과 재사용할 구조를 구별한다.

## 4. 네 가지 가설을 다듬기

### 4.1 LLM의 중첩

Feature superposition은 제한된 차원에 여러 특징을 중첩하는 효율을 설명하지만, 그 feature를 고수준 schema와 동일시하지 않는다. [R02]

Function Vectors는 일부 내부 표현에 개입해 과제 행동을 유도한다. 해당 벡터가 과제 전체를 독립적으로 구현한 프로그램이라는 뜻은 아니다. 따라서 기존 LLM의 기능이 전혀 구분되지 않는다는 주장도 과도하다. [R03]

채택할 표현은 다음과 같다.

> LLM에는 재사용 가능한 기능들이 있으나 표현·실행 경로·변경 경계가 모두 명시적으로 분리되어 관리되지는 않는다. Melete는 특히 선택과 변경의 경계를 더 명확하게 만든다.

### 4.2 Post-training·RL·CoT

다음은 서로 다른 변화다.

1. 기존 기능을 더 잘 선택하도록 행동 분포를 바꾸기.
2. 표현을 구별하기 쉽게 재조직하기.
3. 연결을 제거하거나 독립 변경 경계를 만들기.

LIMA는 적은 instruction-tuning으로 기존 능력을 적절한 출력에 활용하는 관점과 관련되지만, schema의 물리적 분리 증거는 아니다. [R04]

직전 답변에서 대비한 Yue 등의 RLVR 연구와 ProRL은 각각 제한된 훈련·평가 조건에서 sampling 효율과 더 긴 RL 학습의 능력 확장을 다룬다. 모든 RL을 하나의 원리로 확정하지 않는다. [R05, R06]

**LITERATURE (2026-11-17 확인, 사용자 공유 링크 경유; metadata-checked + 본문 부분 정독):** Lu 외, [The Surprising Effectiveness of Deleting Weights in LLM Post-Training](https://arxiv.org/abs/2611.10866)(arXiv v1 2026-11-07, 'NeurIPS 2026' 표기. 학회 공식 사이트에는 'Reasoning and Adaptation' 제목과 Bit-Mask Tuning 명칭의 poster 등재가 있으며 main/workshop 구분과 OpenReview 판정은 확인하지 못했다)는 위 3번 '연결을 제거하는 변화'의 경험 사례다. 저자들은 MLP gate projection 가중치마다 logit을 하나 두어 keep/zero mask만 학습한다(새 값을 쓰지 않음). 전체 가중치의 0.05% 미만을 0으로 만들어 GRPO·SFT·on-policy distillation에서 가장 큰 backbone 기준 full fine-tuning과 같은 정확도를 보고했다. 보존은 Llama 1B/3B/8B의 단일 GRPO(GSM8K) 실행에서 6개 prior-task 평균 정확도가 base의 1점 이내였고 FFT·LoRA·무작위 sparse 학습(MTH)은 최대 5.4점 낮아졌다는 것이다. 저자도 Limitations에서 여러 과제를 순차로 배우는 지속학습을 '다음 시험'으로 남겼다. **OPEN:** 이 결과는 파라미터 선택 방식의 post-training 사례이지 schema 분리·구조 전이의 증거가 아니고, 작은 모델에서는 FFT의 90–99% 수준이며, §8 표의 Supermasks 계열과 같은 mask 방식이다. §1의 설명 2(post-training이 가지치기·분리를 한다)의 지지 근거로 올리려면 §10-B의 같은 base·같은 계산량 대조가 필요하다. 재현·구현은 **NOT RUN**이다.

CoT prompting은 가중치 변경 없이도 동작을 바꿀 수 있으므로, 일시적 활성화와 영속적 분리를 구분한다. 경쟁 질문은 **접근·선택, 조합, 재조직, 새로운 기능 형성 중 무엇이 달라지는가**다.

**OPEN (2026-11-17 검토):** 위 세 변화와 네 갈래 질문은 [11-research-agenda.md](/home/jimmy/repos/full-continual-learning/docs/11-research-agenda.md) §1의 경쟁 가설 표(Access/routing, Specialization, New structure, **Output policy**)와 겹치지만 일대일이 아니다. 선택 = Access/routing, 재조직·연결 제거 = Specialization(11에서는 한 행), 새 기능 형성 = New structure이다. 말투·선호·응답 정책만 바뀌는 **Output policy** 가설은 이 절에 없고(§10 B의 「정책 개선」이 근사), 「조합」은 11의 표에 없다. 통합 시 한 표로 합친다.

### 4.3 중첩과 망각

$$\text{표현 중첩}\ne\text{유해한 업데이트 간섭}.$$

공유된 변경이 여러 기능을 개선할 수 있다. 반대로 분리한 schema 파라미터를 보호해도 공유 encoder·router·출력부가 변하면 기능이 손상된다. GEM과 GPM은 변경 방향이나 중요한 부분공간을 고려하는 관련 대조군이다. [R07, R08]

### 4.4 분해와 지속학습

보호할 대상은 모든 표현의 독립성보다 **유효한 기능을 바꾸는 쓰기 경로**다.

> 읽기와 계산은 공유할 수 있지만, 변경은 영향 범위를 통제한다.

공통 구조를 활용하는 rapid learning의 장점을 유지하면서 무관한 기능으로 변경이 퍼지는 것을 제한한다.

## 5. 표현·활성화·변경의 분리

| 분리 | 질문 | 보존 보장 |
|---|---|---|
| 표현 분리 | 서로 다른 관계가 latent space에서 구분되는가? | 이것만으로는 없음 |
| 활성화 분리 | 문맥에 따라 다른 기능을 쓰는가? | 이것만으로는 없음 |
| 변경 분리 | 새 학습의 무관한 기능에 대한 영향을 제한하는가? | 전체 의존성 조건을 명시하면 가능 |

$$f_A(x)=\phi_A\theta x,\qquad f_B(x)=\phi_B\theta x.$$

위에서 $\phi_A,\phi_B$가 별도여도 공통 $\theta$를 변경하면 둘 다 바뀐다. $\theta$를 고정하고 $\phi_B$만 수정하면 A는 보존된다. 별도의 완전한 모델 두 개를 요구하지 않는다.

목표는 완전한 격리보다 **유익한 공유를 유지하고 무관한 변경 전파를 제한하는 기능적 분해**다.

**OPEN (2026-11-17 검토):** 위 세 분리는 [04-rhythms-and-orchestration.md](/home/jimmy/repos/full-continual-learning/docs/04-rhythms-and-orchestration.md) §3의 동작 구분과 이렇게 겹친다. 활성화 분리 ≈ Activate/read·Switch, 변경 분리 ≈ Write·Protect/expand(+Eligibility), 표현 분리는 동작이 아니라 표현의 성질이다. [05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §2의 네 상태와는 지속 기억(schema를 담는 weights·fast state·CMS level)이 변경 분리의 대상이고 제어 상태(schema 적합성·선택적 write·통합 준비도)가 gate에 해당한다. 이 절에는 Eligibility(어느 경험이 어떤 경로를 썼는지의 후보 흔적), Consolidate, 정보 교환(통신 gate)이 없고 Bind는 §6의 $b_s$로만 나타난다. 한편 핵심 설계 문서(01–12)에는 280dc9a 기준으로 중첩과 간섭의 구분, 그리고 표현 분리·활성화 분리만으로는 보존 보장이 없다는 진술이 없었다(용어 grep 확인. 이 검토의 주석이 들어간 뒤에는 그 주석들이 이를 연결한다). 변경 분리가 「전체 의존성 조건」을 요구하므로(§7.3) 쓰기 허용 $u$만 정해서는 부족하고, 쓰기가 닿는 optimizer 상태·공유 통계·감쇠도 같은 경계 안에 있어야 한다(§9.1).

## 6. 공통 계산 프레임워크

다음은 단순화한 설계식이다.

$$
h_{r+1}=F_{\theta_0}(h_r,x)+\sum_s g_s(h_r,c)T_{\phi_s^{(v)}}(h_r,b_s).
$$

$F$는 공통 계산, $T$는 schema의 관계적 변환, $b_s$는 binding, $g_s$는 문맥별 활성화·조합이다. 실제 구현은 여러 층의 합성·fast-weight modulation일 수 있다. 기존 LLM의 기능을 이 관점으로 분석하고 Melete에서는 관리 가능한 경계를 학습한다.

**OPEN (2026-11-17 검토):** [06-mathematical-framework.md](/home/jimmy/repos/full-continual-learning/docs/06-mathematical-framework.md)와의 관계. 06 §2는 schema를 **선택**하는 혼합($q^-$의 합이 1)이고 06 §5는 읽은 기억 $m$을 입력으로 받는 단일 $F$에 잔차 $h+a\odot F$를 쓰며, 이 식은 공통 core에 gate된 schema 분기를 **더하는** 형태($g_s$가 정규화될 필요 없음)다. 05 §5의 $F_{CMS}(h)=F_0(h)+\sum_j g_j(h)B_j\sigma(A_jh)$와 14 §2의 $W^{\mathrm{eff}}$ 식이 이 가산 분기와 같은 계열이다. 이 식에는 token·block 계산 mask $a$, depth read $d$, 쓰기 허용 $u$가 없고, 06에 없는 binding $b_s$가 있으며 잔차항 $h_r$도 없다. $\phi_s^{(v)}$는 version 첨자라서 token 시계로 변하는 fast state([07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md) §1)를 표현하지 못한다. 선택 혼합·입력 read·가산 분기가 한 모델 안에서 어떻게 공존하는지는 정해지지 않았다(OPEN). 「경계를 학습한다」는 06 §4의 meta-objective(retention·capacity 항)와 §5의 $u$로 표현할 수 있으나 두 문서 사이의 연결은 아직 적혀 있지 않다.

하지만 모델 전체를 schema 하나라고 하면 어떤 모델도 들어가므로 그 자체로 이론이 되지 않는다. 동일 함수가 여러 좌표계와 분해로 표현될 수 있으며, 관측만으로 의미적인 분해가 유일하게 식별된다고 가정할 수도 없다. Locatello 등의 disentanglement 식별 한계는 관련 근거다. [R12]

이론은 어떤 경험이 구조를 공유하는지, 어떤 변경이 다른 기능에 전달되는지, 어떤 분해가 전이를 유지하며 간섭을 줄이는지를 예측해야 한다.

Nested Learning이 여러 context flow와 최적화 수준을 기술한다면, 이 관점은 **재사용되는 기능 단위와 변경의 결합**이라는 축을 제공할 수 있다. 서로 배타적인 설명은 아니다. [R13]

## 7. 수학적으로 확인할 명제

다음은 기본 선형대수·미분·계산 의존성·유한 정보량의 조건부 결과다. 독창적 정리 또는 범용 LLM의 무망각 증명이라고 보고하지 않는다.

### 7.1 선형 연합기억의 정확한 간섭

Key encoder를 고정하고 $\hat v=Mk$, $k_B\ne0$라고 하자. 새 B 경험의 update를

$$M'=M+\eta e_B\frac{k_B^\top}{\|k_B\|^2},\quad e_B=v_B-Mk_B$$

로 두면 대입으로

$$M'k_A-Mk_A=\eta e_B\frac{k_B^\top k_A}{\|k_B\|^2}$$

를 얻는다. 직교 key면 A의 출력은 유지되고, $e_B=0$이면 변경 자체가 없다. A가 원래 정확했고 손실이 $L_A=\frac12\|v_A-Mk_A\|^2$라면

$$\Delta L_A=\frac{\eta^2}{2}\|e_B\|^2\frac{(k_B^\top k_A)^2}{\|k_B\|^4}.$$

이 조건에서는 중첩된 표현으로의 변경이 이전 연합을 훼손하는 양을 정확히 계산한다. A가 원래 틀렸다면 동일 변경이 도움을 줄 수도 있다. Key는 schema 전체가 아니라 접근 표현이고, encoder도 바뀌거나 비선형 모델 전체를 갱신하면 이 식의 보장을 확대할 수 없다.

**OPEN (2026-11-17 검토; 직접 유도와 소규모 numpy 점검, 판정: 정확 — 아래 전제 안에서):** 위 식은 선형 읽기, 고정 key·encoder, 제곱 손실, **단일 step**, 감쇠·momentum·다른 write 없음의 전제에서 대입으로 성립한다. 보강할 조건은 다음과 같다. (a) update는 $\|k_B\|^2$로 정규화된 LMS(Widrow–Hoff) step이고 B 자신의 오차는 $e_B'=(1-\eta)e_B$이므로 $0<\eta<2$에서 수축하고 $0<\eta\le1$에서 overshoot이 없다($\eta=1$이면 $M'k_B=v_B$). 일반 SGD(step $\eta_{\mathrm{sgd}}$)라면 $\eta=\eta_{\mathrm{sgd}}\|k_B\|^2$로 읽는다. $\Delta L_A$ 식 자체는 모든 $\eta$에서 항등식이다. (b) key를 정규화하지 않으면 $\Delta L_A=\tfrac12\eta^2\|e_B\|^2\|k_A\|^2\cos^2\angle(k_A,k_B)/\|k_B\|^2$로 key 크기의 비에도 비례한다. (c) A가 정확하지 않으면 잔차 $r_A=v_A-Mk_A$, $c=k_B^\top k_A/\|k_B\|^2$에 대해 $\Delta L_A=-\eta c\,r_A^\top e_B+\tfrac12\eta^2c^2\|e_B\|^2$로 1차항이 생겨 도움이 될 수도 있다. (d) B 쓰기가 여러 번이면 A 출력의 변화는 벡터로 더해지며 per-step 손실의 합이 아니다. 감쇠 $(1-\alpha)M$이 있으면 직교 key에서도 A의 출력이 $-\alpha Mk_A$만큼 바뀐다. (e) 서로 직교하는 key는 최대 $d_k$개이며, 단위 key가 무작위일 때 N개 A에 대한 기대 간섭 합은 대략 $N/d_k$다(§7.5와 연결). 정리 문안은 [06-mathematical-framework.md](/home/jimmy/repos/full-continual-learning/docs/06-mathematical-framework.md) §11에 있다.

### 7.2 비선형 모델의 국소 간섭

$\theta'=\theta-\eta g_B$인 SGD step에서, 기존 손실 $L_A$가 구간에서 충분히 미분 가능하면

$$L_A(\theta')-L_A(\theta)=-\eta g_A^\top g_B+\frac{\eta^2}{2}g_B^\top H_A(\xi)g_B.$$

$\xi$는 구간의 점이다. Gradient 직교는 곡률 항과 장기 변경까지 제거하지 않는다. $g_A\approx0$인 기존 최적점에서도 손실이 증가할 수 있다. GEM과의 연결은 이러한 국소 근사 범위에서 읽는다. [R07]

**OPEN (2026-11-17 검토; 판정: 조건 보강 필요 — 식은 아래 전제에서 정확):** 위 식은 $\phi(s)=L_A(\theta+s\Delta)$, $\Delta=-\eta g_B$에 Lagrange 나머지를 쓴 것이다. (a) 선분 위의 한 점 $\xi=\theta+s^*\Delta$ ($s^*\in(0,1)$)는 $L_A$가 선분 위에서 $C^1$이고 열린 선분에서 2회 미분 가능할 때만 보장된다. ReLU처럼 구간별 선형인 망의 유한 표본 손실은 파라미터에서 $C^1$도 아닐 수 있어 단일 $\xi$ 꼴이 깨진다(수치 반례: $L_A(a)=\tfrac12(\max(a,0)-0.2)^2$, $a=-0.3$에서 $+1$ step이면 $\phi(1)-\phi(0)-\phi'(0)=0.105$인데 $\tfrac12\phi''\in\{0,0.5\}$). 이때는 평균 Hessian의 적분형 $\int_0^1(1-s)\,\Delta^\top H_A(\theta+s\Delta)\Delta\,ds$에 kink의 도함수 점프항을 더한다. GELU·SiLU·softmax는 매끄럽다. (b) $\theta'=\theta-\eta g_B$는 momentum·weight decay·clipping·전처리가 없는 **plain SGD 한 step**이다. Adam 계열은 $\Delta=-\eta Pg_B$($P$: 상태 의존 전처리)이므로 1차항이 $-\eta g_A^\top Pg_B$이고 부호가 SGD와 다를 수 있다(첫 step은 대략 $-\eta\,\mathrm{sign}(g_B)$. 수치 예: SGD 1차항 $+8\eta$, sign 1차항 $-\eta$). (c) $g_B$가 minibatch(크기 $b$)이면 식은 실현된 update에는 정확하지만 기대값은 $-\eta g_A^\top\bar g_B+\tfrac{\eta^2}{2}(\bar g_B^\top H_A\bar g_B+\operatorname{tr}(H_A\Sigma_B)/b)$가 되어 $\bar g_B=0$이어도 노이즈 항이 남는다(이차 $L_A$에서 수치 확인. 일반 $L_A$에서는 근사). (d) 한 step 식을 여러 step으로 확대할 수 없다. $g_A(\theta_k)$가 바뀌므로 시작점에서 $g_A=0$·직교여도 이후 $g_A^\top g_B\ne0$이 되고, 같은 방향으로 K step이면 곡률 손실이 $\tfrac12\eta^2K^2g_B^\top H_Ag_B$로 $K^2$에 비례한다(수치 확인). 경로 전체에서 $g_A\perp g_B$이면 $L_A$가 불변인 것은 $\eta\to0$의 gradient flow에서만이다.

기능별 변경 민감도 후보는

$$\Gamma_{ij}=\mathbb E_{(x,c)\sim D_i}\left[\|J_i(x,c)U_j\|_F^2\right].$$

$J_i$는 기능 i의 출력 Jacobian, $U_j$는 기능 j에 허용된 변경 방향이다. 이는 국소 민감도이지 손실 증가 자체가 아니다. 업데이트 크기 또는 새 과제 개선량을 맞추고 비교한다. 제한된 probe·작은 실제 update로 근사할 수 있다.

모든 off-diagonal을 0으로 만드는 대신, 유익한 공유를 허용하면서 **무관한 기능 사이**의 민감도를 줄인다.

**OPEN (2026-11-17 검토):** $\Gamma_{ij}$의 해석. $U_j$가 정규직교 기저일 때 $\|J_iU_j\|_F^2=\sum_m\|J_iu_m\|^2$는 단위 방향 섭동에 대한 출력 변화의 제곱합이므로, 계수 $\|z\|=1$인 임의 update $U_jz$에 대해 입력 평균 $\mathbb E\|J_iU_jz\|^2\le\Gamma_{ij}$이고 등방 $z$에서는 평균이 $\Gamma_{ij}/\operatorname{rank}U_j$다(수치 확인). 이것이 **손실 상계가 되려면** 정확 적합(잔차 0)·제곱 손실·1차 선형화·update가 $\operatorname{span}U_j$ 안이라는 조건이 모두 필요하며 그때 $\Delta L_i\lesssim\tfrac12\Gamma_{ij}\|z\|^2$이다. 잔차 $r_i\ne0$이면 1차항 $r_i^\top\delta f_i$가 생겨 $|\Delta L_i|\le\|r_i\|\sqrt{\Gamma_{ij}}\|z\|+\tfrac12\Gamma_{ij}\|z\|^2$이고 부호는 $\Gamma_{ij}$로 정해지지 않는다. 교차엔트로피에서는 출력 곡률을 곱한 Gauss–Newton 꼴 $\mathbb E\operatorname{tr}(U_j^\top J_i^\top H_{\ell,i}J_iU_j)$가 필요하다(후보이며 구현 결정이 아니다). 출력 척도가 다른 기능끼리는 정규화해야 하고 $\Gamma_{ij}\ne\Gamma_{ji}$이며, 「무관한 기능」의 정의(어떤 $(i,j)$ 쌍을 줄일 것인가)를 먼저 정해야 한다(OPEN).

### 7.3 정확한 보존의 충분조건

기존 기능 i의 전체 의존성 $D_i$에는 encoder·출력부·공유 기억·gate의 실제 결과·참조 버전·상태가 모두 들어간다.

> 기존 입력에서 실행되는 경로와 그 경로가 읽는 모든 값·연산을 유지하고, 그 밖의 상태만 변경한다.

이 조건의 결정적 계산에서는

$$\forall(x,c)\in\mathcal C_i,\quad f_{\mathrm{after}}(x,c)=f_{\mathrm{before}}(x,c).$$

계산 그래프 순서의 귀납으로 증명한다. 같은 입력·의존 값·연산이면 중간값과 최종값이 같다. 확률적 실행에서는 동일 난수 경로 또는 출력 분포의 동일성이라는 범위를 명시한다. 이 조건을 모델이 스스로 발견한다는 보장은 아니다. Progressive Neural Networks는 관련 선행 방향이다. [R09]

**Router 파라미터 고정만으로는 부족하다.** Softmax에 새 schema를 추가하면 분모와 이전 선택 확률이 바뀔 수 있다. 보호할 것은 router 파일이 아니라 실제 선택·조합 동작이다.

**OPEN (2026-11-17 검토; 판정: 조건 보강 필요 — 논리는 정확하고 수치 조건이 필요):** (a) 위 귀납은 순수 함수에 대한 것이다. 「경로가 읽는 모든 값」에는 **제어 흐름을 정하는 값**(router·halting·token skip의 결정)과 실행 중 갱신되는 상태(KV·fast weight)가 들어가야 하며, 이 조건은 충분조건이지 필요조건이 아니다. (b) **bit 단위 동일성은 결정적 실행을 전제한다.** GPU에서는 부동소수점 덧셈의 비결합성, reduction 순서·kernel 선택, batch 구성에 따른 수치 차이(batch invariance 부재)로 같은 입력의 출력이 batch마다 달라질 수 있다([Defeating Nondeterminism in LLM Inference](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/), Thinking Machines Lab 2025-09-10. 이 검토는 요지만 확인했다). 이 검토의 호스트 CPU 점검에서도 float32 합의 순서만 바꿔 $2.9\times10^{-4}$, 같은 행을 batch 1과 256으로 계산해 $2.6\times10^{-5}$의 차이가 났다. 따라서 보존 주장은 두 층으로 쓴다. **상태 층**(쓰기 집합 밖 tensor가 byte 동일: 해시로 정확히 검사 가능)과 **출력 층**(허용오차 $\tau$ 안에서 같다. $\tau$의 하한은 변경 전 checkpoint를 batch 구성·순서·장치만 바꿔 재실행한 noise floor $\nu$로 잰다)이며 $\nu$보다 강한 동일성은 약속하지 않는다. 이는 [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md) P1 보장 (3)·(5)의 「허용오차 안에서 같다」와 같은 층위다. (c) Softmax 주장은 더 강하게 성립한다. logit이 유한한 새 schema를 추가하면 기존 모든 gate가 $(1-g^{*\prime})$배가 되어 항상 변하고 기존 gate끼리의 비율만 유지된다(수치 확인). 보존되는 경우의 예는 (i) 새 분기의 기여가 정확히 0일 때(05 §5의 $B_j=0$ 초기화), (ii) gate가 정규화되지 않고 보호 입력에서 0일 때, (iii) 새 logit이 보호 입력에서 마스크($-\infty$)될 때, (iv) top-1 선택에서 새 logit이 최대가 아니고 gate 값을 곱하지 않을 때다.

### 7.4 보존과 retrieval 오류

손실이 $[0,1]$이고 잘못된 경로 확률이 $\delta$이며, 동일 입력 분포에서 항상 올바른 경로를 쓰는 위험이 $R_{\mathrm{correct}}$이면

$$R_{\mathrm{system}}\le R_{\mathrm{correct}}+\delta.$$

올바르게 고른 사건에서는 동작이 같고, 틀린 사건의 추가 손실은 최대 1이기 때문이다. 실제 모델은 올바른 경로를 추론해야 한다.

성능 저하를 기억 내용 손상·선택 오류·공유 표현 drift·저장/재적재 문제로 나눠 평가한다. Versioning만으로 모두 해결되지 않는다.

**OPEN (2026-11-17 검토; 판정: 조건 보강 필요 — 부등식은 정확):** 증명은 $W=\{\text{경로}\ne\text{올바른 경로}\}$, $P(W)=\delta$로 나누어 $R_{\mathrm{system}}=\mathbb E[\ell_c\mathbf 1_{W^c}]+\mathbb E[\ell\,\mathbf 1_W]\le R_{\mathrm{correct}}+\delta$이다(손실 $\ge0$, $\le1$ 필요). 보강할 조건은 다음과 같다. (a) 「올바른 경로」 $c(x,y)$와 $R_{\mathrm{correct}}$가 **어느 모델의 위험인가**를 정해야 한다. 같은 모델을 oracle routing으로 돌린 위험이면 선택 오류 비용의 상계일 뿐이고, 갱신 전 모델의 위험이면 「올바르게 고른 사건에서는 동작이 같고」가 §7.3의 충분조건에 의존한다(7.4는 7.3 위에 얹힌 분해이며 독립 정리가 아니다). (b) $\delta$는 같은 분포·같은 손실에서의 주변확률이며, 올바른 경로가 여럿이면 reference 선택에 따라 달라진다. (c) 손실이 $[0,L_{\max}]$이면 $\delta L_{\max}$로 바뀐다. (d) **soft mixture**에서는 $\delta$가 정의되지 않는다. 볼록이고 $[0,1]$인 손실이면 $R_{\mathrm{soft}}\le R_{\mathrm{correct}}+\mathbb E[1-q_c(x)]$(Jensen), log 손실이면 $R_{\mathrm{soft}}\le R_{\mathrm{correct}}+\mathbb E[-\log q_c(x)]$이다(각각 무작위 20,000회 점검에서 위반 0). 그러나 0-1 손실과 argmax 판독에서는 성립하지 않는다(반례: 정답 성분 (0.34, 0.33, 0.33), 오답 성분 (0, 1, 0)이면 $q_c=0.99$에서도 오답).

### 7.5 유한 용량의 한계

학습 후 접근 가능한 총상태가 B비트이고, N>B개의 독립 이진 사실을 모든 조합에서 정확히 구별해야 한다면 경험 조합 $2^N$개를 상태 $2^B$개로 모두 구분할 수 없다. 다른 이력이 같은 상태로 합쳐진다.

이는 유한 정밀도·유한 총상태·임의 독립 사실의 조건이다. 외부 저장 증가로 제한을 확장할 수 있지만 정보량 비용이 사라지지는 않는다. Schema는 공통 구조를 공유해 필요한 정보를 줄인다. 무작위 예외까지 무료로 압축하지 않는다.

**OPEN (2026-11-17 검토; 판정: 정확 — 정확 구별·유한 상태 한정, 근사 회상은 별도 한계 필요):** 비둘기집 논증이 요구하는 것은 (i) 모든 $2^N$ 조합이 가능한 독립 사실, (ii) 상태 집합 크기 $\le2^B$, (iii) **무오류** 회상이다. 결정적 상태 사상은 필수가 아니다. 상태가 확률적이어도 무오류 회상은 조합마다 상태의 지지집합이 서로 겹치지 않아야 하므로 같은 $B\ge N$이 필요하다. 반면 근사·확률적 회상에는 이 한계가 적용되지 않고 별도 한계가 필요하다. $N$개 균등 독립 비트를 비트당 오류율 $D$로 회상하려면 rate–distortion 한계 $B\ge N(1-h_2(D))$, 전체 벡터를 확률 $1-\epsilon$로 맞히려면 Fano 부등식에서 $B\ge(1-\epsilon)N-1$이다(표준 정보이론 결과이며 수치 확인: $B/N=0.5$이면 $D\ge0.110$, $0.25$이면 $D\ge0.2145$). 따라서 「다른 이력이 같은 상태로 합쳐진다」는 근사 회상에서는 전면 실패가 아니라 오류율의 하한이다. 사실에 구조가 있으면 필요한 비트는 $\log_2$(가능한 이력 수)로 줄어든다(마지막 문단과 일치). $B$는 접근 가능한 raw 비트의 상한이며 실제로 읽어낼 수 있는 유효 용량이 아니다. 유한 상태로 끝없는 스트림을 다루면 어떤 정책이든 선택적 망각이 필요하다는 뜻이므로 「무망각」 목표의 상한 문구에 반영한다([11-research-agenda.md](/home/jimmy/repos/full-continual-learning/docs/11-research-agenda.md) §8 주석). 확률적 유한 상태의 충분 상태 크기는 오차 기준에 따라 달라지는 별개의 결과다([2026-11-17-sleep-time-melete-selected-addendum.md](/home/jimmy/repos/full-continual-learning/research/2026-11-17-sleep-time-melete-selected-addendum.md) §2).

## 8. 선행연구와 독창성 경계

**분리하면 덜 잊는다는 원리 자체는 선행연구가 있다.**

| 연구 | 선행 메커니즘 | Melete의 추가 질문 |
|---|---|---|
| Progressive Neural Networks [R09] | 과거 column 보호·새 column·lateral transfer | Task별 전체 분기보다 작은 구조를 발견하는가? |
| Supermasks in Superposition [R10] | 고정 기반의 task별 mask·선택 | 관계의 재사용·조합·수정까지 학습하는가? |
| GPM [R08] | 과거 기능의 중요한 공간 보호 | 변경 경계를 schema 기능과 연결하는가? |
| WISE [R11] | 원래/수정 지식 분리·routing·sharding | 사실 편집을 넘어 새로운 관계 재조직으로 확장되는가? |

후보 기여는 **task ID를 사람이 미리 나누지 않고 재사용할 관계를 학습·조합하며, 간섭을 제한하고, 새 학습과 추론 비용까지 줄이는 것**이다. Task당 adapter와 task를 넘어 재사용하는 schema를 구별한다. 독창성의 최종 판단은 추가 문헌 비교와 결과 이후다.

**OPEN (2026-11-17 검토):** (a) 후보 기여의 「task ID를 사람이 미리 나누지 않고」는 선행연구와의 경계로 충분하지 않을 수 있다. SupSup(R10)의 arXiv 초록은 task identity가 주어지지 않으면 gradient 기반 최적화로 task를 추론하며 task identity 없이도 학습할 수 있다고 쓴다(초록 수준만 확인하고 본문은 읽지 않았다). 구별선을 task 단위 mask 선택과 재사용되는 관계 구조의 학습·조합·수정으로 다시 그을 수 있는지가 OPEN이다. (b) GPM(R08)류의 층별 입력 부분공간 투영은 §7.1·§7.3의 key와 직교한 쓰기의 정확 보존 논리를 근사 부분공간으로 구현한 것으로 읽을 수 있다(R08 원문은 읽지 않았다). WISE(R11)의 side memory·router 구조는 [05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §5의 $F_{CMS}$ 분기+gate와 구조가 가까워 보인다(식별자 확인 수준). (c) 이 표는 격리·projection·확장 계열 4건뿐이다. 정규화 계열(EWC류), 파라미터 격리(PackNet·HAT류), low-rank 간섭 제어(O-LoRA·InfLoRA류), 입력 기반 task 추론(Expert Gate류) 등은 280dc9a 기준 [catalog.tsv](/home/jimmy/repos/full-continual-learning/references/catalog.tsv)와 이 문서에 없었다(이 검토가 InfLoRA 등 일부를 catalog 끝에 후보 행으로 올렸다). 이들은 비교 후보 이름일 뿐이며 서지와 결과는 확인하지 않았다(OPEN). [11-research-agenda.md](/home/jimmy/repos/full-continual-learning/docs/11-research-agenda.md) §7의 「새 메커니즘 대 기존 조합」 두 조건 중 (1) 직접 구현 부재는 이 계열에 대해 아직 확인되지 않았다.

## 9. 구현에 반영할 제안

### 9.1 공유 core와 선택적 쓰기

하나의 System ONE을 유지한다. 공통 계산을 읽되 국소 schema 상태를 선택적으로 변경한다.

$$g_s^{\mathrm{read}}\ne g_s^{\mathrm{write}}.$$

여러 schema를 읽어도 모두 수정하지 않는다. 파라미터 외에 optimizer momentum·weight decay·공유 통계 등의 변경 의존성도 검사한다. 이것은 구현 계약 제안이지 현재 구현 완료가 아니다.

**OPEN (2026-11-17 검토):** 위의 「optimizer momentum·weight decay」는 [06-mathematical-framework.md](/home/jimmy/repos/full-continual-learning/docs/06-mathematical-framework.md) §3의 빠른 업데이트 식에서 구체적으로 새어 나간다. $\gamma_{t,k}=0$인 schema $k$도 $\phi_{k,t+1}=(1-\alpha_t)\phi_{k,t}+\beta_tm_{k,t-1}$로 바뀐다(감쇠와 momentum이 $\gamma$로 gate되지 않는다). 쓰기 격리를 약속하려면 감쇠·momentum·optimizer 상태·공유 통계(norm 통계, EMA 등)를 같은 쓰기 gate $u$에 묶거나 격리 주장의 범위에서 명시적으로 제외한다. [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md) P1-T11의 「바뀌면 안 된다」 state 집합에 이 항목들을 넣는 것이 가장 싼 검사다(검토 제안).

### 9.2 Copy-on-write와 버전

확정된 구조를 직접 덮어쓰기보다 새 버전을 만들고 평가하는 경로를 고려한다. 기존 소비자가 새 버전으로 이동해도 되는지 검사한다.

- 수정: 같은 조건의 오류 교정.
- 분기: 다른 조건의 구조를 공존시킴.
- 조합: 여러 구조를 함께 사용.

최신 버전 하나로 무조건 교체하지 않는다. 과거 조건에서 유효한 지식과 실제 오류를 구별한다.

**OPEN (2026-11-17 검토):** 위 copy-on-write는 [14-schema-lifecycle-crud-and-joint-paper.md](/home/jimmy/repos/full-continual-learning/docs/14-schema-lifecycle-crud-and-joint-paper.md) §3의 「In-place update는 같은 schema ID의 파라미터를 계속 학습하는 기본 경로다」, 「공유 의존성을 사용하는 확정 버전은 안전한 snapshot/검증 후 승격 대상으로 취급한다」와 같은 방향으로 읽을 수 있다(작업 중 상태는 제자리 갱신, 확정·공유 버전은 새 버전). [07-state-and-storage.md](/home/jimmy/repos/full-continual-learning/docs/07-state-and-storage.md) §2의 committed snapshot → working state → commit과 §6 lineage, [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md)의 P1 원자적 commit(commit 단위 버전)·P4 version lineage(schema 단위)에 대응한다. 또한 §9.3의 「공유 변경을 더 엄격한 검증 경로에」는 로드맵 P4의 Sleep·보호 지표 자동 중단과 겹치지만 별도 사본에서 학습 → 보호 family 회귀 → 승격이라는 작업 단위는 적혀 있지 않다. schema 단위 copy-on-write의 비용(복사량·소비자 이동 검사)은 측정하지 않았다.

### 9.3 Sleep과 공유 기반 변경

온라인에서는 국소 변경을 우선하고 Sleep에서는 관련 경험을 함께 학습해 공통 구조를 개선할 수 있다. 여전히 유효한 기능은 회귀 검사한다. 공유를 금지하는 것이 아니라 공유 변경을 더 엄격한 검증 경로에 둔다.

### 9.4 완전한 LLM 사전 분해는 선행조건이 아님

기존 LLM을 공유 기반으로 유지하며 새 경험을 분리 가능한 경로에 학습할 수 있다. 이후 필요한 기능을 증류·재구성해 artifact로 이전한다. 모든 pretrained schema를 먼저 추출해야 시작할 수 있는 계획으로 바꾸지 않는다.

**OPEN (2026-11-17 검토):** 「기존 LLM을 공유 기반으로 유지」는 [05-integrated-architecture.md](/home/jimmy/repos/full-continual-learning/docs/05-integrated-architecture.md) §5(원 FFN $F_0$ 보존, $B_j=0$)와 [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md) P1·§4(원 FFN을 느린 기반으로, 제거는 증류로만)에 이미 반영돼 있고 사전 분해가 MVP의 선행조건이 아니라는 서술은 [11-research-agenda.md](/home/jimmy/repos/full-continual-learning/docs/11-research-agenda.md) §1에 있다. 「필요한 기능을 증류·재구성해 artifact로 이전」은 원 FFN 제거용 증류와 deep-to-shallow(P4) 외에는 로드맵에 작업 단위가 없다(OPEN).

## 10. 실험 계획 A–E

모든 실험은 **NOT RUN / PROPOSAL**이다. 현행 phase·전체 사용자 여정과 독립 평가 정책 안에서 배치한다.

**OPEN (2026-11-17 검토):** A–E의 phase 배치 제안은 [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md) §6-1에 있다. A·E는 UJ2, C는 UJ1·UJ2, D는 UJ1·UJ4의 판독으로 얇게 시작하고, B는 P5 '미루는 것'과 충돌해 사용자 결정이 필요하다. A·C의 핵심 비교(공유 파라미터를 갱신하는 arm, task별 adapter)는 현재 arm 표에 없다. 이 배치는 구현·실행을 뜻하지 않는다.

### A. 중첩과 간섭의 인과적 분리

작은 관계 환경에서 표현 중첩·관계 충돌·공유 파라미터 변경을 독립 조작하고 초기 품질을 맞춘다.

| 비교군 | 질문 |
|---|---|
| 공유 표현·공유 update | 기본 간섭 |
| 공유 표현·선택적 update | 공유를 유지해도 보호되는가? |
| 분리 표현·공유 encoder update | 표현 분리만으로 충분한가? |
| 분리 상태·oracle gate | 보존의 진단 상한 |
| 분리 상태·학습 gate | 실제 선택 오류 |
| 무작위 분할 | 의미 있는 분해의 추가 가치 |

공유 표현·선택적 변경이 효과적이면 중첩 제거보다 변경 경계 가설을 지지한다. 무작위 분할과 같으면 단순 격리 효과일 수 있다.

### B. Base와 post-training

동일 base에서 형식 SFT·추론 SFT·RL을 분기하고 가중치 고정 CoT prompting을 비교한다. 데이터·teacher·계산량을 통제하거나 차이를 보고한다.

측정: 내부 표현 개입, 새 관계 수정 후 무관 과제 손실, 같은 새 과제 개선에 필요한 변경량, 문맥 선택, 새 관계 조합 전이.

- 성능·선택 개선, 간섭 동일: 접근·정책 개선을 지지.
- 간섭 감소와 전이 유지: 기능적 변경 분리를 지지.
- 새로운 기능 형성: 기존 schema 선택만으로는 설명 부족.

### C. 용량과 지속학습

고정 총용량에서는 파라미터·저장·replay를 함께 제한한다. 성장 허용에서는 모델 복제·task adapter·random partition·schema 재사용을 같은 저장 예산에서 비교한다.

Task/schema ID를 주는 oracle와 문맥에서 추론하는 실제 조건을 구분한다. 새 학습 성과·기존 유효 기능·관련 경험 재사용·비용을 함께 본다. Update를 멈춰 망각만 줄인 모델을 성공으로 보지 않는다.

### D. Artifact 재사용과 기능 보존

새 개체·표현, 새로운 schema 조합, offload/reload, 이전 버전 복원, encoder 변경 후 호환성, 국소 정정 뒤 무관 기능 보존을 검사한다. 과거 task 재생과 새 과제에 도움이 되는 재사용을 구별한다. 추론 복원과 후속 학습 궤적의 복원도 별도다.

### E. System ONE의 계산 효율

Controller를 우회하고 경험 전후의 loop·update 예산별 품질을 비교한다. 새로운 구조 공유 사례에서 같은 정확도에 필요한 총 계산이 줄어드는지 확인한다. 이후 controller가 실제 저비용 경로를 선택하는지 본다.

Router·검색·offload·온라인 update·Sleep 비용을 포함한다. 망각 감소가 자동으로 추론 가속을 의미하지 않는다.

**OPEN (2026-11-17 검토):** 실험 A–E는 새 phase가 아니라 기존 phase의 작업이다(A는 P2, B는 P5 이후, C는 P2–P4, D는 P4, E는 P2·P4). 자원 배정과 규모 가늠은 [15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md) §5.3이다. 실험 B(post-training 분기·RL)의 계산량은 시도 횟수가 비용이라 아직 견적하지 않았다. NOT RUN.

## 11. 최종 연구 명제

> LLM의 재사용 가능한 기능들은 공유된 표현과 파라미터에 구현되며, 새로운 학습이 이 기능들에 결합된 변경을 일으킬 수 있다. 우리는 경험에서 재사용 가능한 조건부 계산 구조를 학습하고, 선택·조합·업데이트 경계를 명시화해 유해한 간섭을 제한한다. 유익한 공유를 유지하면서 지속학습과 경험 기반 계산 효율을 개선하는 것이 목표다.

세 수준을 분리한다.

- **수학:** 어떤 변경 경계와 의존성 조건에서 기존 함수가 보존되는가.
- **실험:** 실제 모델이 구조를 학습·선택하고 제한된 비용으로 새 지식을 배우는가.
- **해석:** LLM과 post-training을 schema 형성·선택·재조직으로 어디까지 설명할 수 있는가.

최종 지향은 **공유해도 되는 것은 공유하고, 함께 바뀌어서는 안 되는 것은 변경 경계를 분리하며, 그 경계 자체를 경험에서 학습하는 것**이다.
