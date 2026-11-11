# 06. 수학적 연구 명세와 제한된 이론

**PROPOSAL:** 아래 식은 대화에서 제안된 모델링 언어다. 원논문의 공식을 모두 재현한 통합 정리나 실제 뇌의 확정식이 아니다. 이미 실행된 수치 실험은 별도 [Phase-0](../experiments/phase0/README.md)이다.

## 1. 상태와 시간

외부 경험 e_t=(x_t,y_t,c_t,source_t), 내부 recursion r, optimizer/update step u, level별 consolidation clock s_l를 분리한다. y_t는 관측 결과/피드백으로, 예측 당시에는 아직 알 수 없을 수 있다.

느린 schema 파라미터 θ_k, fast binding/adaptation state φ_{k,t}, controller ψ, 작업 hidden h_{t,r}, depth bank D_{t,r}, committed memory M_t와 tentative memory M~_{t,r}를 둔다. 이산 k는 선택의 예시이며 schema 본체가 기호라는 뜻은 아니다. 분산 mixture나 continuous routing으로 일반화할 수 있다.

## 2. 결과 이전 선택과 이후 책임 추정

$$q^-_{t,k}=q_\psi(k\mid x_t,c_t,D_{<t})$$

$$p(y_t\mid x_t,D_{<t})=\sum_kq^-_{t,k}\,p_{\theta_k,\phi_{k,t}}(y_t\mid x_t)$$

관측 후:

$$\gamma_{t,k}\propto q^-_{t,k}\,p_{\theta_k,\phi_{k,t}}(y_t\mid x_t).$$

q^-는 판단에, γ는 관측 후 attribution/update에 사용한다. 평가용 future label·latent cause를 learner/controller에 제공하지 않는다. 같은 likelihood가 성립하는 구조들은 현재 관측만으로 구별 불가능할 수 있다.

**USER (U-T09):** 주어진 schema에 따른 빠른, 편향된 추론을 원한다. **PROPOSAL:** 편향은 오류를 고집하는 성향이 아니라 결과 이전의 조건부 prior q^-_{t,k}가 경험으로 한쪽에 집중된 정도다. 집중도는 H(q^-_t) = -sum_k q^-_{t,k} log q^-_{t,k}로 둔다(작을수록 편향이 강하다). 유용한 편향은 schema 일치 사례에서 H(q^-)가 작고 정답률이 유지되며 필요한 계산이 줄어드는 경우다. 해로운 편향은 불일치 사례에서도 H(q^-)가 작아 γ_{t,k}가 관측 쪽으로 옮겨가지 못하는 경우다. 따라서 편향은 H(q^-) 자체를 최소화하는 목표가 아니라 [08-evaluation.md](/home/jimmy/repos/full-continual-learning/docs/08-evaluation.md) §6의 편향 이득·해악 지표로 보고한다. **OPEN:** continuous routing이나 분산 mixture에서는 엔트로피 대신 유효 schema 수 같은 대체 척도를 정한다.

## 3. 빠른 업데이트

기억 정확도·관측 예측·피드백을 구분한 예:

$$\mathcal L_t^{fast}=\lambda_{kv}\mathcal L_{kv}+\lambda_p\mathcal L_{pred}+\lambda_f\mathcal L_{feedback}.$$

$$m_{k,t}=\beta_tm_{k,t-1}-\eta_t\gamma_{t,k}\nabla_{\phi_k}\mathcal L_t^{fast}$$

$$\phi_{k,t+1}=(1-\alpha_t)\phi_{k,t}+m_{k,t}.$$

이 식은 Titans에서 영감을 얻은 후보이지 모든 HOPE/Titans 구현의 동일 식이라는 뜻은 아니다. α는 decay/retention 표기의 선택이다. 입력별 계수의 범위·norm·root budget을 사전 명시한다. 작은 학습률이 안정성 전체를 보장하지 않는다.

**USER (B08, 2026-10-09):** 학습은 적은 data로 빠른 일반화의 오류(overfitting)를 유도하고 시간축 continual learning으로 그 오류가 상황에 맞게 사라지게 하는 것이다. GD→SGD→Adam→Muon 같은 일반 optimizer가 맞는지 묻고, backward·SGD 수준의 근간 학습 방법을 조사·고찰하라고 했다.

**PROPOSAL:** 학습 방법 선택을 optimizer 하나로 묻지 않고 다섯 결정 축으로 분리해 기록한다. (1) 학습 신호·목적: 실제로 새로 관측한 것이 무엇이며 다음 판단의 어떤 차이가 중요한가. (2) 귀속: 어떤 관계·경로가 결과에 기여했는가. (3) 바뀌는 상태: fast φ, slow θ, controller ψ, memory M 중 무엇인가. (4) 갱신 규칙: 국소 규칙인가 gradient optimizer인가. (5) 가소성·시간척도: 학습량·망각·보존·통합을 언제 조절하는가. 위 빠른 업데이트 식은 (4)의 후보 하나다. 표준 optimizer(예: AdamW)는 느린 층의 기준선으로 같은 신호·예산의 대조군에 둔다. optimizer를 바꾼다고 적은 경험에서 유용한 문맥이 자동으로 발견된다고 가정하지 않는다.

**ARCHIVE:** Melete는 모델 구조·기억의 상태/시간척도·학습 목표·credit assignment/update rule·optimizer를 서로 다른 축으로 두고 SGD/Adam 교체만으로 암묵지 학습을 만들었다고 부르지 않는다고 했다 ([neural-basis.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/design/neural-basis.md)). 같은 분리를 정리하며 SGD/Adam/Muon은 신용 정보를 이용해 갱신을 만드는 방법이고, 큰 data에서의 성공이 알고리즘의 대량 data 요구를 뜻하지는 않는다고 기록했다 ([2026-10-09-learning-foundations.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/research/2026-10-09-learning-foundations.md)). 같은 문서는 'overfitting'(특정 표본에 맞춰 전이가 약해짐)과 '성급한 일반화'(근거가 적은 규칙의 넓은 적용)를 구분해 측정하고, 오류 자체를 높이는 목적함수는 적응 목적을 표현하지 못한다고 했다.

**OPEN:** B08의 '오류를 유도한다'를 '빠른 가설 생성의 부작용을 허용하고 시간축 반례로 줄인다'로 읽는 것은 Melete 문서의 해석이며 사용자 확인이 필요하다. 근간 학습 규칙(국소 신용·forward 계열·뇌 모사)의 조사는 [11-research-agenda.md](/home/jimmy/repos/full-continual-learning/docs/11-research-agenda.md)의 후보 지도에 둔다.

**LITERATURE (SWAMI23, W6-swami23-metadata-gap.md:47):** 선택적 갱신의 출발점은 보호/쓰기 규칙이다. leave-one-out 조건부확률과 p_surprise로 확신 있게 맞은 위치(anchor)는 보호하고 틀린 위치만 다시 묶으며, 임계값은 저자가 정한 값(LIALT 0.1, dax 1/16)이다.

**LITERATURE (MICONI25, W3-elder26-miconi25.md:258-262,281):** 네트워크가 스스로 만든 스칼라 neuromodulator m(t)가 연결별 가소성 계수 A와 Hebbian trace로 쓰기를 gate하며, 연결별 계수가 필수다(단일 스칼라로 바꾸면 active 해가 30 run 중 0개).

**ARCHIVE (S21 GNM, 2026-11-09-sbl-tracking.md:29,39; 확인 깊이 official-search-checked):** 무엇을 쓸지를 자연어 지시로 학습하는 neural memory write이며 write-gradient 차단 ablation에서 선택적 기억의 개선이 크게 감소했다고 보고됐다. 추상 schema discovery의 직접 증거는 아니다.

**PROPOSAL ([2026-11-11-sbl-fulltext-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext-review.md#5-fcl-설계의-시작점-proposal) §4.2·§5 출발점 2):** MICONI25식 학습된 neuromodulator를 SWAMI23식 규칙보다 강한 후보로 둔다. §5의 u(write 대상·허용)는 "어디에", η(강도)는 "얼마나", §1의 level clock s_l은 "언제"에 대응시키고 "무엇을"은 쓸 증거의 선택으로 두어 하나의 gate로 합치지 않고 따로 시험하며, 대조군은 항상 쓰기, surprise만, 고정 무작위 gate를 같은 쓰기 예산에서 비교한다. 구현이나 채택 결정이 아니다.

## 4. 느린 schema 학습: 적응 후 새 사례 일반화

새 과제 τ의 support Sτ로 m회 적응하고 독립 query Qτ로 평가한다.

$$\min_{\theta,\psi}\;\mathbb E_\tau[\mathcal L_{Q_\tau}(\operatorname{Adapt}_m(\theta,\psi;S_\tau))]+\lambda_{ret}\mathcal L_{retention}+\lambda_{eq}\mathcal L_{equivariance}+\lambda_{cap}C.$$

단순 reconstruction이 아니라 이후의 전이·학습 효율이 objective에 들어간다. 이름·대상 순열 g가 출력에도 반영돼야 하는 과제에서는 f(gx)≈g f(x)의 equivariance를 사용한다. 모든 변환에 invariant하면 오히려 역할 차이를 잃을 수 있다.

새 schema 생성 비용·representation expansion·경쟁/통합 규칙은 후보 가설이다. rank나 모듈 수가 늘었다는 사실만으로 schema 분화를 선언하지 않는다.

**LITERATURE (MICONI25·TEM20, W3-elder26-miconi25.md:258-262, W4-tem20-kumar26.md:104-113):** 느린 구조를 얻는 방식은 논문마다 다르다. MICONI25는 바깥 루프(A2C+BPTT)와 gradient 없는 안쪽 Hebbian trace를, TEM20은 바깥 BPTT(25 step, 4-lap은 100)와 환경마다 0으로 리셋하는 안쪽 Hebbian M을 쓴다.

**LITERATURE (GOUDAR23·CHU25, W2-chu25-goudar23.md:99-104,299-304,371):** 두 논문에는 명시적 meta-objective가 없고 GOUDAR23의 문제 경계·Adam 리셋·안정화 정규화와 CHU25의 단계 경계는 실험 틀이 공급한다. GOUDAR23에서 재사용을 막으면 가중치 변화가 약 8–12배 커진다.

**PROPOSAL (W2-chu25-goudar23.md:374, 원문 검토 §5 출발점 7):** Adam은 step 크기가 정규화돼 있어 변화량과 trial 수의 상관이 일부 기계적일 수 있고, 위 목적함수의 retention 항 크기를 정할 문헌 측정도 거의 없다.

**OPEN:** 명시적 바깥 루프로 갈지 순차 문제 안에서의 창발에 맡길지는 정해지지 않았다.

## 5. 현재 생각과 지속 기억의 읽기

$$m_{t,r}=\operatorname{SchemaRead}(h_{t,r},M_{t,r}),\qquad d_{t,r}=\operatorname{DepthRead}(h_{t,r},D_{t,r})$$

$$ (a_{t,r},u_{t,r},\eta_{t,r},b_{t,r})=\pi_\psi(h_{t,r},m_{t,r},d_{t,r},c_{t,r}).$$

a는 token/block 계산 mask, u는 write 대상·허용, η는 강도, b는 통신/종료 등 정책을 나타내는 제안 표기다.

$$h_{t,r+1}=h_{t,r}+a_{t,r}\odot F_\theta(h_{t,r},x_t,m_{t,r},d_{t,r})$$

$$M_{t,r+1}=M_{t,r}+u_{t,r}\odot\mathcal U_{\eta_{t,r}}(M_{t,r},\mathcal E_{t,r}).$$

여기서 \mathcal E는 출처와 대상 경험에 결속된 증거다. 내부 update를 임시 상태에서 수행한 뒤 commit할지, 온라인 committed state를 버전별로 갱신할지는 [상태 계약](07-state-and-storage.md)에서 선택한다.

## 6. 비용 민감한 제어

한 요청이 아니라 연속 경험 구간의 비용과 향후 이득을 고려한다.

$$J=\mathbb E\big[\sum_t(\mathcal L_{task,t}+\lambda_c C_t+\lambda_f\mathcal L_{forget,t}+\lambda_r\mathcal L_{risk,t})\big].$$

C에는 encoder, core 반복, routing, depth read, write/backward, retrieval/offload, decoder가 포함된다. Sleep는 online latency와 별도 표시하되 amortized total compute에는 포함한다. 지금 학습해서 다음 요청에서 비용을 줄이는 선택을 평가하려면 horizon이 필요하다.

추가 loop의 예상 효용과 비용을 비교하는 halting이 후보다. Familiarity만으로 halt하지 않는다. 동일 질의에 여러 (loop,update) 조합을 평가해 요구 품질을 만족하는 저비용 행동을 학습 신호로 쓸 수 있지만, 이 teacher 비용도 기록한다.

**LITERATURE (HWU20·SPECTRUM26·SWAMI23, 원문 검토 §4.4 계산량, W1-spens24-hwu20.md:332, W5-spectrum26-structk25.md:94-95, W6-swami23-metadata-gap.md:56-57):** 같은 품질의 추론 계산량을 잰 논문은 읽은 11편에서 찾지 못했다. HWU20의 절감도 학습 epoch이다. 개념 수준의 근거는 SPECTRUM26(accommodation이 더 많은 시간과 계산을 요구한다는 정성적 서술)과 SWAMI23(posterior 엔트로피 감소, 1회 EM으로 충분)뿐이다.

**PROPOSAL (원문 검토 §5 출발점 6, W6-swami23-metadata-gap.md:73, W2-chu25-goudar23.md:204, W4-tem20-kumar26.md:315):** H-COMPUTE는 문헌 지지가 가장 약한 사실상 우리 고유 가설이다. halting의 후보 신호는 CSCG posterior 엔트로피(SWAMI23), 기억 recall 신뢰도(KUMAR26의 0.6 임계값), attractor 수렴 탐침(CHU25 S-C.3의 응용)이며 이 신호들의 계산 절감 효과는 시험되지 않았다. 고정 깊이의 품질–계산 곡선을 먼저 얻고, §9의 C*_ε 첫 추정은 문헌 대조 없는 우리 실측으로 적는다.

**USER (B03, 2026-10-05):** SGD·cross entropy·오차 기반 학습은 대량 data에 유리하다. 우리는 적은 data가 시간축으로 계속 들어오고 빠르고 성급한 일반화를 누적하는 pattern·surprise 기반 학습이 필요하다. RL도 시도 횟수가 많아야 하지 않나?

**PROPOSAL:** 시행착오로 신호를 얻는 학습(RL, bandit, 여러 행동 조합의 teacher 탐색)은 시도 횟수가 곧 비용이다. 경험 직후의 빠른 경로는 이런 신호를 요구하지 않는다. 한 관측에서 얻는 신호(예측 잔차, 정정, 피드백)로 먼저 갱신한다. 시행착오형 신호는 controller 학습과 Sleep 단계에서만 쓰며 시도 횟수와 teacher 비용을 총 계산에 포함한다. 시행착오형 방법은 같은 관측·계산 예산의 국소 갱신 대조군과 비교한다.

**ARCHIVE:** Melete v0.2는 경험 직후의 첫 방법을 case lookup·no-write·normalized delta·작은 SGD write로 두고, 여러 경험 뒤의 층에서만 필요한 경우 meta-learning/RL을 쓰도록 층을 나눴다 ([experience-system.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/design/experience-system.md) §8).

**OPEN:** 시행착오형 학습을 후속 단계의 어느 지점에서 허용할지는 정하지 않았다.

## 7. 제한된 선형 표본 효율 설명

$$y=x^\top U_ka+\epsilon,\quad U_k^\top U_k=I_r,\quad x\sim\mathcal N(0,I_d),\quad\epsilon\sim\mathcal N(0,\sigma^2),\quad r\ll d.$$

올바른 U_k가 알려져 있고 새 task의 n개 독립 관측으로 계수 a를 OLS 추정하며 n>r+1이면, 새 noiseless signal에 대한 기대 excess prediction MSE는

$$\mathbb E[\mathrm{MSE}_{signal}]=\frac{\sigma^2r}{n-r-1}.$$

U_k를 쓰지 않는 d차원 OLS에는 n>d+1일 때 r 대신 d가 들어간다. schema는 새 task에서 추정할 자유도를 줄일 수 있다는 제한된 설명이다. U_k 발견·선택 비용, misspecification, nonlinear language, noise modeling, intercept 등은 이 식에 포함되지 않는다.

## 8. Loop 감소의 제한된 수렴 설명

고정 memory에서 F가 올바른 해 h* 근방의 contraction이라고 가정하면

$$\|h_{r+1}-h^*\|\le\kappa\|h_r-h^*\|,\quad0<\kappa<1$$

따라서 \|h_r-h*\|≤κ^r\|h_0-h*\|. 좋은 schema는 초기오차나 반복 변환을 개선할 수 있다. 실제 Transformer가 contraction이라는 주장도, 고정점이 정답이라는 주장도 아니다. 반복 중 weights가 바뀌면 이 단순 정리를 그대로 적용할 수 없다.

## 9. 프로젝트의 핵심 측정량

$$C_\epsilon^*(M)=\min\{C:\operatorname{Error}(M;\mathcal T_{new},C)\le\epsilon\}.$$

새로운 entity/value/binding이지만 관계 구조를 공유하는 \mathcal T_new에서

$$C_\epsilon^*(M_{after})<C_\epsilon^*(M_{before})$$

인지 확인한다. 최소값은 실제 측정한 budget grid 내에서만 계산하고 측정하지 않은 threshold crossing을 보간해 단정하지 않는다. query-level noise와 history/world-level variation을 나눠 통계 처리한다.

## 10. 아직 정리가 아닌 주장

- 모든 schema가 저랭크라는 명제.
- semantic abstraction level과 CMS frequency가 일치한다는 명제.
- post-training이 반드시 schema를 분화한다는 명제.
- oscillator가 event scheduler보다 항상 효율적이라는 명제.
- loop 증가가 단조적으로 정답률을 올린다는 명제.

이들은 반례와 비교 방법을 가진 OPEN 가설로 관리한다.

**OPEN (원문 검토 §4.1·§4.3, 문헌 검토 뒤 추가):** 같은 방식으로 관리할 명제가 더 있다. 학습된 schema 구조가 같은 예산의 고정·무구조 대조보다 낫다는 명제(읽은 11편에 직접 비교가 없다). 오류가 크면 새 구조를 만들고 작으면 미세 조정하는 규칙이 옳다는 명제(STRUCTK25·SPECTRUM26의 정성 규칙이며 데이터가 없다). 예외만 따로 저장하면 schema가 보존된다는 명제(SPENS24 확장 모델의 설계이며 schema 개정과 다중 seed가 없다).

**LITERATURE (SPENS24, W1-spens24-hwu20.md:99,127):** 확장 모델은 consolidation 전에도 prototype 쪽 왜곡을, DRM 모형은 lure 회상을 정성적으로 재현한다. **PROPOSAL (원문 검토 §5 출발점 3, W4-tem20-kumar26.md:182):** 위 명제들의 반례·실패 모드 후보는 잘못된 구조가 조용히 내용을 묶는 것(TEM20형 분리에서의 위험)과 schema 과적용(prototype 왜곡·DRM lure)이다.
