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

## 3. 빠른 업데이트

기억 정확도·관측 예측·피드백을 구분한 예:

$$\mathcal L_t^{fast}=\lambda_{kv}\mathcal L_{kv}+\lambda_p\mathcal L_{pred}+\lambda_f\mathcal L_{feedback}.$$

$$m_{k,t}=\beta_tm_{k,t-1}-\eta_t\gamma_{t,k}\nabla_{\phi_k}\mathcal L_t^{fast}$$

$$\phi_{k,t+1}=(1-\alpha_t)\phi_{k,t}+m_{k,t}.$$

이 식은 Titans에서 영감을 얻은 후보이지 모든 HOPE/Titans 구현의 동일 식이라는 뜻은 아니다. α는 decay/retention 표기의 선택이다. 입력별 계수의 범위·norm·root budget을 사전 명시한다. 작은 학습률이 안정성 전체를 보장하지 않는다.

## 4. 느린 schema 학습: 적응 후 새 사례 일반화

새 과제 τ의 support Sτ로 m회 적응하고 독립 query Qτ로 평가한다.

$$\min_{\theta,\psi}\;\mathbb E_\tau[\mathcal L_{Q_\tau}(\operatorname{Adapt}_m(\theta,\psi;S_\tau))]+\lambda_{ret}\mathcal L_{retention}+\lambda_{eq}\mathcal L_{equivariance}+\lambda_{cap}C.$$

단순 reconstruction이 아니라 이후의 전이·학습 효율이 objective에 들어간다. 이름·대상 순열 g가 출력에도 반영돼야 하는 과제에서는 f(gx)≈g f(x)의 equivariance를 사용한다. 모든 변환에 invariant하면 오히려 역할 차이를 잃을 수 있다.

새 schema 생성 비용·representation expansion·경쟁/통합 규칙은 후보 가설이다. rank나 모듈 수가 늘었다는 사실만으로 schema 분화를 선언하지 않는다.

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
