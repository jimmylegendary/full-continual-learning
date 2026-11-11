# 12. 기존 Melete와 연구 자산의 이관 경계

이 문서는 현재 대화에서 읽었던 과거 repository 기록과 실험을 보존한다. **이번 작업에서 기존 `jimmylegendary/melete` 저장소를 변경하거나 최신 HEAD를 감사하지 않았다.** 과거 분석 기준은 `1d95136c3a64580ec25bc588c96c191eecb85b41` 등이며 서로 다른 코드·데이터·문서 checkpoint를 합치지 않는다.

## 1. 이전 H1–H5

H1: 개인 경험·암묵지·판단 경로를 online으로 누적하는 별도 neural layer의 보완 가치.

H2: familiarity 기반 빠른 처리와 새 경험 학습, LLM의 깊은 추론. 학습 속도와 추론 역할은 별도 축.

H3: query의 순서 있는 node/edge trajectory를 task working graph로 compile하고 hit association을 강화. fact validity와 hit frequency는 별도.

H4: 매 turn 전체 hidden-state trajectory를 text reader로 바꾸어 frozen LLM prefix에 전달. terminal/pointer는 비교군.

H5: LLM output을 다시 넣어 compatibility/surprise를 평가하고 input/output/frame을 학습해 최초 query로 recompile·resume. Generated는 학습 신호일 수 있지만 외부 사실의 독립 근거가 아니다.

당시에는 이 가설을 편의상 버리거나 pointer/RAG 성공으로 완료 처리하지 않는 규칙이 있었다. **USER (U-T07):** 이후 사용자가 통합 모델로 목표를 구체화했고, 이 진술이 H3의 'LLM=slow, Melete=fast' 역할 분할을 대체했다(시간 순서: B14는 2026-10-12이고, U-T07은 U-T 번호순으로 볼 때 작성일이 2026-10-31로 표기된 U-T03의 PDF 이후 발화다. 번호가 대화 순서라는 것은 가정이다). **PROPOSAL (정리자 추론):** 이로부터 H4의 text interface가 현재의 필수 조건은 아니라고 추론했다. 사용자는 U-T02에서 vec2text에 대한 기대감이 부족하다고 했을 뿐이며, 보존된 사용자 발화에는 text interface를 폐기한다는 문장이 없다. **OPEN:** 사용자 확인 전까지 H4의 전체 hidden-state 전달과 terminal·pointer 대조는 basis로 유지한다. **역사적 가설 변경을 은폐하거나 이전 실패를 성공으로 바꾸지 않는다.**

## 2. N0–N5 기록에서 남길 결과

- 8개 수치 cue·3개 결과 채널의 합성 neural prototype이었다. 자유 문장 암묵지 학습과 구분.
- root budget이 있는 trained graph 대 같은 budget의 frozen graph 추가 개선: 0.48%, 대략 95% 구간 −3.07~4.04%. neural 표현의 독립 기여 미입증.
- all-state reader calibration 문장 exact 29/256, terminal 38/256. known 3-channel projection inverse 256/256은 임의 latent vec2text가 아니다.
- 실제 frozen Qwen consumer의 3-turn smoke에서 높은 provisional gain으로 좁은 회복을 보였으나 잘못된 해석의 고착 위험과 일반 효용은 미검증.
- 코드/type/test/site gate는 software 검증이며 학습 효과를 대체하지 않는다.

**ARCHIVE:** 학습 방법 roadmap(2026-10-11)의 좁은 결과. 합성 조건부 패턴 8개·query instance 16개·순서 seed 3개에서 1-shot 정확도는 episodic/RLS/slow가 100%, Delta 89.58%, MLP+SGD 39.58%, MLP+Adam 62.5%였다. 10-shot에서는 MLP+Adam도 100%이나 이점이 없었다. 단순 episodic 기준과 source-semantic control이 강해 neural MLP의 추가 효용은 입증되지 않았고 neural default 승격은 FAIL이었다 ([2026-10-11-learning-roadmap-feedback.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/implementation/records/2026-10-11-learning-roadmap-feedback.md)). 12개 독립 잡음 stream의 비교에서는 균일·중간 반감기의 slow 통합이 잡음과 과거 조건 보존에 이득이었으나 변화 초반에 뒤처졌고, 짧은 반감기는 안정 구간의 잡음을 키웠다(같은 문서).

**ARCHIVE:** J0(2026-10-15)는 학습 후보 없이 측정 계약만 검증했고 두 v2 실행이 contract_pass=true, efficacy는 not_evaluated였다. 최초 j0-v1 PASS는 whole-branch review에서 return fixture의 의미 불일치로 철회돼 v2로 대체됐다 ([2026-10-15-conditional-judgment-j0-feedback.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/implementation/records/2026-10-15-conditional-judgment-j0-feedback.md)). 위는 모두 과거 문서의 보고 이력이며 이 repository에서 새로 실행한 값이 아니다.

**OPEN:** 이 결과들이 통합 모델의 학습 규칙 선택에 어떤 제약을 주는지는 [11-research-agenda.md](/home/jimmy/repos/full-continual-learning/docs/11-research-agenda.md)의 학습 규칙 후보 지도가 정해지면 다시 본다.

## 3. J1 개발·진단 기록

동일 sampler/2,048 steps의 seed7 pilot:

| arm | Return | Composition | Macro |
|---|---:|---:|---:|
| G-pair | 100.00% | 73.44% | 86.72% |
| Fixed-pair | 100.00% | 69.53% | 84.77% |
| NoG-pair | 98.44% | 69.53% | 83.98% |
| G-BCE-paired | 100.00% | 78.13% | 89.06% |

Pair objective의 local metric 개선이 primary 개선으로 이어지지 않았다. Composition에서 6 fixes / 12 regressions. master가 제안한 5pp gate(사용자 합의가 아님) 미달로 같은 recipe 확대 중단. Return의 ceiling과 copying baseline, training r변화와 R3 p개입의 차이를 구분했다.

CPU/GPU probability parity와 진단 구현의 실패도 학습 실패와 다르다. 원 GPU에서 parity subcheck를 통과한 후 NoG mask의 CPU/CUDA 혼합으로 진단이 중단되어 module-gradient는 미측정이었다. Dummy tensor 수정으로 원본 연구의 성공을 선언하지 않았다.

이 숫자는 **과거 문서의 보고 이력**이며 이 repository에서 새로 실행한 값이 아니다.

## 4. 가져올 자산

Evidence log, source/revision, snapshot, recompile/resume, budget, root 중복 제어, observed/generated 구분, matched baselines, 실패와 raw 결과 보존, 실제 E2E와 연구 gate의 구분은 현재 방향에도 가치가 있다.

옛 graph가 최종 schema의 유일한 표현이어야 하지는 않는다. 기존 code/packages의 완전 이관은 이번 문서 게시에 포함되지 않으며 다음 구현 작업에서 파일별로 판단한다.

**ARCHIVE:** 이번에 이관하지 않은 Melete 연구 자산은 다음과 같다. (1) 기초 학습 방법 대장(12계열 50개 비교 항목)과 제품 적합 순위·13개 조합 atlas ([2026-10-09-learning-method-catalog.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/research/2026-10-09-learning-method-catalog.md), [2026-10-09-learning-atlas-mechanisms.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/implementation/records/2026-10-09-learning-atlas-mechanisms.md)). (2) latent/graph 상태를 LLM에 전달하는 방법의 전수 조사 ([2026-09-27-readout-survey.md](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/research/2026-09-27-readout-survey.md)). (3) 조건부 판단 측정 계약 J0의 설계·결과 기록. atlas는 문헌·API·수식 검토이며 학습 실행·채택이 아니다.

**OPEN:** 이 자산이 FCL 문서에 없다는 것은 학습 방법의 ELI 그림·제품 적합 순위·조합 정리 요구(B09)가 FCL에서 충족되지 않았다는 뜻이다. 이관 여부와 통합 모델 기준의 재검토는 다음 작업에서 파일별로 판단하며, [11-research-agenda.md](/home/jimmy/repos/full-continual-learning/docs/11-research-agenda.md)의 학습 규칙 후보 지도로 통합한다.

## 5. 과거 private repository 링크

- [Neural basis](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/design/neural-basis.md)
- [Neural workflow feedback](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/implementation/records/2026-10-12-neural-workflow-feedback.md)
- [J1 diagnostics](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/implementation/records/2026-10-21-neural-judgment-j1-diagnostics.md)
- [Historical roadmap](https://github.com/jimmylegendary/melete/blob/1d95136c3a64580ec25bc588c96c191eecb85b41/docs/superpowers/plans/2026-10-15-neural-judgment-roadmap.md)

접근권한이 없는 독자는 이 링크를 읽지 못할 수 있다. 현재 논의에 이미 공개된 연구 요지를 보존했으며 private repository 전체를 복제하지 않았다.
