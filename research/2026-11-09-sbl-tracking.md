# SBL 주간 조사 — 2026-11-09 대화 보고 보존

조사 구간으로 보고된 기간: 2026-11-02~09. **ARCHIVE:** 아래 수치는 직전 대화의 보고를 그대로 연구 기록으로 이관한 것이다. 이번 게시에서 모든 본문 표/통계/코드를 독립 재검증한 결과가 아니다. 공식 식별자는 새로 확인 가능한 경우 보완했으며 [catalog](../references/catalog.tsv)의 확인 수준을 따른다.

당시 결론: 해당 기간에 continuous neural schema의 형성·선택·수정·지속학습을 모두 통합 검증한 새 논문은 확인하지 못했다. 이를 분야 전체의 부존재 증명으로 확대하지 않는다.

## 1. Curriculum unlearning — S19

Jirko Rubruck, Alice Zhang, Andrew Saxe, Christopher Summerfield. 2026-11-03 preprint. [논문](https://arxiv.org/abs/2611.04565), [코드](https://github.com/licezhang/curriculum_unlearning).

세 이진 feature의 8개 사례 중 6개는 단순 규칙, 2개는 예외. 단순한 규칙에 맞춰 압축된 representation이 예외를 표현할 차원을 약화시킬 수 있다는 연구로 보고됐다. 직접적인 CMS/LLM architecture 연구가 아닌 adjacent evidence다.

보고된 인간 n=207 조건에서 규칙+예외 전략에 도달한 비율: simple→complex 65.3%, 순서 구분 없음 44.4%, complex→simple 19.4%. Neural exception accuracy delta +0.071 [0.037,0.104], rule accuracy delta −0.024 [−0.035,−0.012]. 노출량 통제와 representation/사전학습 ablation을 보고했다.

해석: mismatch의 일부는 기존 파라미터 값뿐 아니라 필요한 구분을 담지 못하는 표현 문제일 수 있다. Learning rate/step만 늘리는 것과 capacity expansion/splitting을 구분한다. 인간 행동실험에서 neural dimensionality를 직접 측정한 것은 아니다.

## 2. Invariance before structure — S20

Hardik Rajpal, Dan Goodman. 2026-11-05 preprint; 당시 NeurIPS2026 UniReps workshop extended abstract로 소개됐다. [논문](https://arxiv.org/abs/2611.07952).

Parameter-space compression과 task temporal state-space structure를 구분한다. 500개 fixed recurrent units와 10D trained bottleneck에서 전자의 half-change 약8 epoch, 후자 약40 epoch, 약32 epoch 간격으로 보고됐다. Parameter-level 지표 약0.78→0.96. Temporal shuffle에서 초기 invariance는 남고 후기 task 구조가 나타나지 않았다고 보고했다.

Melete 가설: 안정된 cluster/저차원화 자체를 schema 형성 PASS로 삼지 말고 새 task 예측과 전이를 평가한다. 실제 지속학습·rapid binding 연구는 아니고 code 공개는 당시 미확인이었다.

## 3. Tell Me What To Learn / GNM — S21

Max S. Bennett, Thomas P. Zollo, Richard Zemel. 최초2026-02-26, 대화에서 최신개정2026-11-05 v3로 보고. [논문](https://arxiv.org/abs/2602.23201), [공식 구현](https://github.com/maxbennett/Generalized-Neural-Memory).

Llama 기반 MemoryLLM 계열의 neural memory bank에 무엇을 쓸지 자연어 지시로 학습한다. 선택적 사실·선호·기억 거부/수정을 다루며 abstract schema discovery의 직접 증거는 아니다. 학습된 write operation과 추론시 모든 weights의 매번 fine-tuning을 구분한다.

| 당시 보고 지표 | GNM | 비교 |
|---|---:|---|
| CounterFACT 종합 score | 84.1 | ICL-FT67.3 / RAG-FT70.5 / MemoryLLM38.7 |
| PersonaMem 종합 score | 93.8 | ICL-FT90.5 |
| PersonaMem leak | 6.1% | ICL-FT10.5% |

서로 다른 score 정의는 직접 비교하지 않는다. 최대400대화 장기 평가, 저장 문서 수 대비 per-query FLOPs의 특징을 보고했지만 무제한 retention이나 전체 latency 보장으로 확대하지 않는다.

Write-gradient 차단 ablation에서 선택적 기억의 개선이 크게 감소했다고 보고됐다. v3 부록의 별도 단기 조건: 명시적 지시94.8%, 암묵 지시87.9%, frozen LLM이 만든 지시92.7%. 이 수치를 본문의 다른 benchmark 점수와 혼합하지 않는다. 일반적인 학습 지시가 무엇이든 저장하는 정책을 만들 수 있어 prompt 영향을 따로 본다.

## 4. Continual episodic memory CLS — S22

Xu Pan, Ely Hahami, Roy Siegelmann, Haim Sompolinsky. 원고2026-08-24, eLife reviewed preprint2026-11-04. [심사 공개본](https://elifesciences.org/reviewed-preprints/112891v1), [코드](https://github.com/xup5/Continual-Episodic-Memory-in-Large-Language-Models).

경험별 rank2 masked LoRA, embedding 기반 선택, Llama3.1-8B-Instruct/Qwen3-8B, 고랭크 replay 통합. 최대1000 episodes의 저장·인출·통합을 다룬다. 개별 episodic adapter를 추상 schema로 부르지 않는다.

보고된 N=1000 결과:

- 필터링된 direct QA 약1% 수준이라는 서술이 있었다.
- 원문 복원 후 다시 context로 제공하는 iRAG의 filtered QA: Wiki99.3%, Character85.4%.
- Unfiltered iRAG: Wiki98.4%, Character81.1%.
- 원문 재구성만으로 consolidation한 직접 QA: Wiki31%, Character33%.
- 재구성+knowledge instruction: Wiki73%, Character50%.
- 재구성+masked reconstruction: Wiki69%, Character59%.

Filtered set은 원문을 제공하면 답할 수 있는 질문을 남긴 것이므로 일반 end-to-end 정확도와 구별한다. 기억 복원과 유용한 판단은 별도 학습 문제다. 추가 목적함수와 기존 능력 보존의 trade-off도 함께 기록한다. eLife reviewed preprint를 확정 최종 논문으로 쓰지 않는다. 생물학적 대응의 범위와 기술 구현의 성과를 분리한다.

## 5. 신규 발견한 이전 연구: From sequences to schemas — S23

Vezha Boboeva, Alberto Pezzotta, George Dimitriadis, Athena Akrami. 2026-04-10 bioRxiv. [원문](https://www.biorxiv.org/content/10.64898/2026.04.10.717706v1.full).

`aab/ccd/eef`처럼 토큰과 관계를 분리하는 sequence task. 당시 160 recurrent units, 7 abstract classes, 약rank3 common component로 보고됐다. Singular component 개입으로 temporal 관계 통합의 선택적 손상을 분석하고 recurrent scaffold를 다음 예측 task로 이전하는 실험이 소개됐다.

Autoencoder 사전학습의 암기 향상과 relational transfer를 구분한다. 고정 scaffold+새 readout만으로 같은 이득이 없었다는 보고는 후속 가소성의 역할을 묻는다. 범용 schema discovery, 실제 동물 회로의 입증이 아니다. 이전 조사에서는 검색에 노출된 본문 외 직접 전체 접근과 code verification이 제한됐다고 밝혔다. 이번에는 정확한 full title/DOI의 official search identity를 확인했지만 모든 수치는 여전히 원보고 범위로 귀속한다.

## 6. Task Schema and Binding — S24

Chaeha Kim. 2025-12-19 preprint. [논문](https://arxiv.org/abs/2512.17325).

9개 모델의 activation patching에서 abstract task type과 concrete association을 구분했다고 소개됐다. 일부 실험의 late-MLP task schema transfer100%, residual binding62%가 보고됐다. 개별 실험 수치를 모든 모델의 보편적 결과로 쓰지 않는다. 강한 prior와 새 binding의 충돌도 연구점이다.

연속 activation의 기능적 분해이며 세션 간 weight update 연구는 아니다. ‘FFN=모든 schema, sequence=모든 binding’의 일반 법칙을 주장하지 않는다. CMS/Titan 역할 분담의 후보 가설로 사용한다.

## 7. Invariant schema within plastic networks — S25

James R. Elder, Jie Zheng, Lydia B. Shimelis, Ueli Rutishauser, Milo M. Lin. online2026-06-30 / print2026-09. [원문](https://doi.org/10.1007/s10827-026-00940-x), [코드](https://github.com/jre411/bdENN).

시각 경계 과제에서 상위 schema circuit은 안정적으로 유지하고 upstream representation이 새 데이터를 반영하는 계층 학습. 당시 accuracy62.3±3.8% 대 end-to-end56.1±4.7%로 보고됐다. ±의 정확한 통계 정의와 denominator는 출판 사용 전 원문 확인이 필요하다. 인간 단일 뉴런 처리 순서와의 일치를 실제 뇌 학습 규칙의 입증으로 확대하지 않는다.

## 8. Symbolic/discrete 비교

Graph schemas [S18]: Guntupalli et al., 2023-02-14, [arXiv2302.07350](https://arxiv.org/abs/2302.07350). Latent graph/slots/transition으로 구조를 transfer한다. continuous neural이 아니다.

Agentic Program Induction Schema [S27]: Zeng et al., 2026-09-30, [arXiv2609.39140](https://arxiv.org/abs/2609.39140). Persistent executable programs로 unknown environment를 모델링. 당시 ARC-AGI-3 RHAE58.7→99.2%를 보고했으나 특정 harness/평가 범위이며 neural schema의 증거가 아니다.

## 9. Melete로 옮길 세 가설

A: 안정화/압축과 재사용 가능한 구조 형성을 구별한다.

B: rapid learning에서 보호·국소 수정·표현 확장·분리의 선택을 연구한다.

C: schema 선택과 선택적 쓰기가 다음 추론의 비용에 영향을 주는지 본다.

이 논문들은 recursive System ONE 전체에서 동일 정확도의 loop/latency 감소를 통합 입증하지 않았다. 그것은 프로젝트의 별도 검증 대상이다.

## 10. 추적 항목

P0: Boboeva full code/수치, GNM write-path/자율 지시, Yoshida 원문/코드.
P1: S-HAI schema 생성/경쟁, curriculum 표현 지표, Task Schema causal 재현, CLS 직접 QA 통합.
P2: graph/program schema와 neural 모델의 공통 전이 benchmark.

당시 기존 목록의 S-HAI v3(10/26), Kumar v5(10/20)는 새 논문으로 재소개하지 않았다. 다음 보고에서는 최신 버전을 다시 조회해야 한다.
