# ET 대상·시간캡슐 기반 모델·사료 조사: 2026-11-18 조사 기록의 부록 (W2c)

**상태 라벨:** 조사 기록(LITERATURE 확인 수준 표기, 선택과 추천은 PROPOSAL). 2026-11-18 기준. 읽기 전용 조사이고 구현·학습·GPU 실행·비용 지출은 0회(NOT RUN)다. 이 글은 [17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md)의 대상 묶음 절과 [2026-11-18-blueprint-et-design.md](/home/jimmy/repos/full-continual-learning/research/2026-11-18-blueprint-et-design.md)의 재료다. ET의 운영 정의·rubric·단별 상한은 docs/17, P0 실행 설계는 [18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md), 비용은 [15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md)가 소유한다. 여기서는 대상과 자료와 모델의 사실만 낸다.

## 한눈에 보기

| 질문 | 조사 결과 |
|---|---|
| 지금 쓸 수 있는 시간캡슐 모델은? | 마감 1899(GPT-1900, 1.68B·3.29B, MIT), 1904(GPT-1905, 3.29B), 1913(TypewriterLM, 7.24B, 라이선스 미명시), 1930-12-31(Talkie-1930, 13B, Apache-2.0), 1875(TimeCapsuleLLM, 런던 영어), 1938(TypewriterLM-1938, 세부 미확인). Ranke-4B(1913–1946)는 가중치 공개를 확인하지 못했다. 1914–1929 구간과 1939년 이후에는 공개된 처음부터 학습한 모델이 없다 |
| ET 대상 추천은? | 주력 Einstein 1905(GPT-1900), pilot Planck 1900(GPT-1900)과 Chadwick 중성자 1932(Talkie-1930), 대안 일반상대성 1915(TypewriterLM-1913)와 Turing 1936(Talkie-1930). 후보 16개 중 두 관문(마감이 맞는 가용 모델, 수식·수치 채점)을 통과한 5개다 |
| MD-H 잠정안과 달라진 점은? | Planck 1900을 pilot으로 추가, 일반상대성 1915는 주력 후보에서 대안으로, 1930년 이후 발견은 Ranke-4B 미공개 때문에 1932와 1936만 가능, 정보 이론 1948은 기반이 없어 제외, 기준표에 기반 능력(C9)과 관문 추가 |
| 가장 큰 병목은? | 기반 모델 능력(타 논문 벤치 HellaSwag: GPT-1900 32.3, Talkie-1930 49.8), 독일어 사료와 현대 LLM 번역의 누수, Einstein 편집판의 접근·권리, 후대 서술에 의한 사후 편향 |
| Einstein test의 출처는? | TIME 2025-04-15(기자 서술, 연도 없음), Hassabis의 2026-02 발언(1911 → 일반상대성 1915, 2차 인용), 2026-05 Google I/O·Axios 인터뷰 보도와 2026-10 WSJ 인물 기사 요약(1901 → 1905, 모두 기자 서술이고 원문 미열람). 별개로 학술 의견 논문 CACM 2026-05가 절차 골격을 제시했다 |
| 사용자 원문의 「1901 → 1904」는? | 지식 마감 1901은 판본 b에 가깝고 「1904」는 역사의 1905와 다르다. 조용히 맞추지 않고 기록했다(§5-1) |
| 참고 영상은? | 영상의 존재와 제목만 확인했다. 내용은 확인하지 못해 needs-resolution이다(§5-4) |
| 지시문 §1-6에서 고친 것 | 10건(§7). TypewriterLM의 제목과 모델 카드 없음, Ranke-4B 공개 미확인, GPT-1900 결과 서술, 「공개된 절차가 없다」는 평 등 |
| 사용자 결정 후보 | DC-W2c-01 ~ 07(§8) |

모든 수치와 공개 상태는 2026-11-18 조회 결과다. 벤치 수치는 타 논문이 잰 값이며 재현하지 않았다. 확인하지 못한 칸은 「미확인」이다.

## 1. 시간캡슐(vintage·historical) 언어모델 현황

기준일 2026-11-18. 모델 카드, 논문, 공식 저장소, Hugging Face 공개 메타데이터를 직접 열어 확인했다. 가중치와 corpus는 내려받지 않았다. 표 칸의 확인 수준은 세 가지다. `primary-read`는 1차 문서(블로그·논문·모델 카드·저장소)를 직접 읽은 것, `primary-partial`은 카드나 API 메타데이터만 본 것, `secondary`는 목록·보도로만 본 것이다. 칸이 비었거나 「미확인」이면 확인하지 못한 것이다. 표는 열이 많아 1a–1c로 나눴다.

**표 1a. 정체와 공개물**

| 모델 | 만든 곳 | 지식 마감 | 크기 | 학습 token | 구조 | 공개물과 라이선스 |
|---|---|---|---|---|---|---|
| GPT-1900 (D34) | Michael Hla (독립 연구자) | 1900-01-01 이전 출판물(블로그의 서술). 단 같은 저자의 physics-CLM 카드에 표준 d34-22btok에는 일부 1900년 이후 자료가 있다는 서술이 있음 | 3.29B (34층, hidden 2176) | 약 22B token(깨끗한 1900년 이전 영어 text). D34는 10,507 step, token 대 파라미터 비 약 11배 | nanochat 계열 맞춤 GPT(RoPE, QK-norm, ReLU2, value embedding, 층별 residual scalar), context 2048, vocab 32768 | Hugging Face에 가중치·corpus 공개, 모델 카드 라이선스 MIT. corpus 원천(Institutional Books 등)의 재배포 조건 상속 여부는 미확인 |
| GPT-1900 (D26) | Michael Hla (독립 연구자) | 1900-01-01 이전(위와 같음) | 1.68B (26층, hidden 1664) | 22B token을 2 epoch | 위와 같은 계열, context 2048 | HF 가중치(약 4.9GB), 카드 라이선스 MIT |
| GPT-1905 (D34) | Michael Hla (독립 연구자) | 1905-01-01 이전 출판물(카드: pre-1905, 특수상대성 직전) | 3.29B (34층) | 약 40B token(카드). Institutional Books와 American Stories 신문 | GPT-1900 D34와 같은 구조, context 2048 | HF 가중치, 카드 라이선스 MIT |
| GPT-1964 (D34) | Michael Hla (독립 연구자) | 1964 이전(1900-1964 text) | 3.29B | 미확인(step 19,103) | GPT-1900 D34와 같은 구조 | HF 가중치, 카드 라이선스 MIT |
| TypewriterLM-1913 (7.24B) | Luo, Shinnick, Griesshaber, Wang, Yu, Shi, Torr, Lu (Waterloo·Vector·Oxford·UCL 등) | 1913. 논문 초록은 pre-1913, 본문 corpus는 1700-1913이고 데이터 카드의 재현 필터는 1700 이상 1913 이하(1913 포함 여부 미확정) | 7.24B | corpus 54B token(1700-1913), 학습 약 140B token(2.59 epoch) | Llama 3 구조(GQA, RMSNorm, RoPE), context 8192, 자체 BPE vocab 32000 | HF typewriter-ai 조직에 가중치 공개. 모델 카드가 없어 라이선스 미명시. 데이터 카드는 license other, Institutional Books 부분은 약관상 재배포 불가라고 명시 |
| TypewriterLM-1938 계열 | typewriter-ai 조직(논문 저자와 같은 프로젝트로 보이나 미확인) | 프로젝트 페이지는 마감 1938로 표기. 논문에는 없음 | 7.24B instruct 1종, 3.0B EN-DE base 1종(영어와 독일어) | 미확인(프로젝트 페이지의 54B token 표기는 1913판 수치와 같아 확인 필요) | Llama 구조, 7B는 context 8192 추정(config 확인은 1913판만), 3B는 context 4096 | HF 가중치 공개, 모델 카드 없음(라이선스 미명시) |
| Talkie-1930 (13B) | Nick Levine, David Duvenaud, Alec Radford | 1930-12-31(미국 저작권 소멸 경계, 보고서의 서술) | 13B | 260B token(영어 pre-1931: 책, 신문, 정기간행물, 과학 학술지, 특허, 판례) | 구조 세부는 미확인(자체 참조 코드 사용). 자매 모델 talkie-web-13b-base는 같은 구조·같은 FLOPs로 FineWeb 학습 | HF 가중치(base와 it)와 GitHub 코드 모두 Apache-2.0. 접근 제한 없음 |
| Ranke-4B 계열 | Daniel Goettlich, Dominik Loibner, Guohui Jiang, Hans-Joachim Voth (Zurich, Cologne) | 1913, 1929, 1933, 1939, 1946 다섯 판 | 4B | 판마다 80B token(전체 정제 corpus 약 600B token) | Qwen3 구조를 처음부터 학습. 1900년까지 한 checkpoint를 학습한 뒤 1900-마감 구간 20B token을 이어 학습 | 2025-12 사전 공개 노트와 information hub만 확인. 2026-11-18 조회에서 두 HF 조직의 공개 모델은 0개이고 DPO 샘플 dataset 2개만 있음. 가중치·라이선스 미확인 |
| TimeCapsuleLLM v2 (1.22B) | Hayk Grigorian (Muhlenberg College와 Georgia State University 협력) | 1875 (런던 1800-1875 text) | 1.22B (v0 16M부터 v3mini 500M까지 여러 크기) | 112GB text(HF 카드, awesome 목록은 90GB로 표기), 182,000 step, 약 0.5 epoch | Llama 구조 22층 hidden 2048, GQA, context 2048, 자체 BPE vocab 32000 | HF 가중치 MIT(v3mini 500M은 Apache-2.0), 코드 GitHub |
| Mr. Chatterbox | Trip Venturella | 1899 (빅토리아 시대 영국 1837-1899 text) | 0.34B(MIT 판)와 2.7B 계열(CC BY-NC-SA 4.0) | 약 2.93B token(awesome 목록 서술) | nanochat 기반 | HF 공개, 0.34B 판 MIT, 신판은 CC BY-NC-SA 4.0 |
| MonadGPT | Pierre-Carl Langlais | 1700 (초기 근대 text 약 11,000개, 1400-1700) | 7B | 미확인(fine-tune) | Mistral-Hermes 2를 fine-tune한 것으로 처음부터 학습한 모델이 아님 | HF 공개(라이선스 미확인) |

**표 1b. 쓰임새와 한계**

| 모델 | instruction 판 | 실행 형식 | 알려진 누수·한계 | 발견 시험 결과 | 확인 수준 |
|---|---|---|---|---|---|
| GPT-1900 (D34) | 있음: instruct-v3-sft(현대 LLM이 만든 합성 대화 53,458개로 SFT), physics CLM(1900년 이전 물리서 약 290M token), reasoning SFT, discovery RL(현대 LLM judge) | PyTorch .pt와 nanochat 코드(맞춤 구조). GGUF 변환본은 검색에서 못 찾음(미확인) | SFT·RL 단계에 현대 LLM이 들어가 저자 스스로 무오염 주장이 약해진다고 서술. 번역자 서문 등 후대 문구 누수 사례를 저자가 보고. context 2048이라 긴 stream 불가. 벤치(타 논문 측정) HellaSwag 32.3, ARC-E 36.7 | 저자 보고: 단서가 붙은 모순 문제에서 단편적 직관(예: 빛은 불연속 에너지 양)이 가끔 나옴. 저자 평가는 대부분의 물리 과제 실패, 평가는 인상 기반(vibes)이며 발견 주장 아님 | primary-read(블로그 전문, HF 카드 4종, HF API) |
| GPT-1900 (D26) | D34와 별개 instruct 판 없음(미확인) | PyTorch .pt와 nanochat 코드 | D34와 같은 corpus 한계. final val BPB 0.751(저자 보고) | 발견 시험 보고 없음(미확인) | primary-read(HF 카드, HF API) |
| GPT-1905 (D34) | 카드에 instruct 판 언급 없음(미확인) | PyTorch .pt와 nanochat 코드 | 카드는 Planck 초기 연구와 Lorentz 전자론은 알고 특수상대성·광자는 모른다고 서술(저자 진술, 누수 감사 방법은 미확인) | 발견 시험 보고 없음(미확인) | primary-read(HF 카드) |
| GPT-1964 (D34) | 없음 | PyTorch .pt와 nanochat 코드 | 저자가 카드 첫머리에 신문체 출력만 나오는 거의 쓸모없는 모델이라고 경고 | 해당 없음 | primary-read(HF 카드) |
| TypewriterLM-1913 (7.24B) | 있음: LIMA판(1,000개 단일 턴과 30개 다중 턴), SelfInstruct판(287,860쌍), LoRA. 응답은 1913년 이전 원문에서만 어휘를 가져오는 제약. 지시문 일부는 현대 LLM(Claude Opus)이 생성해 사람이 검토 | HF safetensors BF16(LlamaForCausalLM)이라 PyTorch hook 가능. 제3자 GGUF 변환본 존재(품질 미검증). 공식 GGUF 허가 문의가 HF 토론에 열려 있음 | 1913년 이후 사건 회상 누수가 strict 0.0 퍼센트 relaxed 0.6 퍼센트라는 수치는 alphaXiv의 AI 요약 보고서 기준이며 v2 Table 3은 열람하지 못함. v2 부록은 ILO 1919와 Civil Rights Act 1964 누수 사례를 제시. 벤치 HellaSwag 36.1, ARC-E 43.3(v2 Table 2). 논문 Figure 1의 선별 예에서 Einstein 이름은 알지만 물리학자로서 말할 만큼은 모른다고 답함 | 발견 시험 없음(논문은 시간 일관성·언어 벤치만) | primary-read(논문 v2 일부 쪽, HF API, 데이터 카드) |
| TypewriterLM-1938 계열 | 7B는 instruct 판 | HF safetensors BF16(Llama) | 누수 감사 방법과 결과는 미확인(논문 밖) | 없음(미확인) | primary-partial(HF API와 config, 프로젝트 페이지) |
| Talkie-1930 (13B) | 있음(it): 1931년 이전 참고서에서 만든 지시-응답 SFT, 그다음 Claude Sonnet 4.6을 judge로 쓴 online DPO, Claude Opus 4.6과의 합성 대화로 SFT | 참조 코드는 PyTorch로 bf16에 28GB 이상 VRAM 요구. 제3자 HF transformers, GGUF, MLX, GPTQ, ONNX 변환본이 다수 있음(변환 충실도 미검증) | 저자 보고: 7B 초기판은 Roosevelt 대통령 임기와 New Deal을 알았고 13B도 제2차 세계대전과 전후 질서 일부를 안다(필터 불완전). RL에 AI 피드백을 써서 시대에 맞지 않는 말투가 생길 수 있음. 벤치 HellaSwag 49.8, ARC-E 55.8(타 논문 측정) | 발견 시험 결과 보고 없음. 보고서는 Hassabis의 1911 질문을 인용하고 Turing 1936 논문을 마감 이후 사례로 그림에 넣었으나 시험 결과는 싣지 않음 | primary-read(보고서 전문, HF 카드와 API, GitHub README) |
| Ranke-4B 계열 | 사전 공개 노트에 SFT와 GRPO 후처리 서술. 공개 여부 미확인 | 공개 weights 미확인 | 사전 공개 노트: 정규화 필터가 의미 내용이 아니라 가독성 기준이며 중복 제거를 하지 않음. 누수 평가 방식은 미확인 | 발견 시험 없음 | primary-partial(README와 사전 공개 노트 앞부분, GitHub와 HF API) |
| TimeCapsuleLLM v2 (1.22B) | instruct 판 없음(미확인) | HF safetensors(Llama), 제3자 GGUF와 MLX 변환본 존재 | OCR 잔재(Digitized by Google)가 출력에 남는다고 저자와 다른 논문이 보고. 학습 비용 사례: H100 SXM 117시간 약 341달러(저자 카드) | 발견 시험 없음 | primary-read(README, HF 카드) |
| Mr. Chatterbox | chat 판 있음 | HF 가중치, 신판 GGUF 존재 | 작은 모델이라 능력이 낮음(저자 서술). 마감 이전 text의 편향 보존 | 발견 시험 없음 | secondary(목록과 HF API 메타데이터만) |
| MonadGPT | chat 판 | HF 가중치와 제3자 GGUF | 기반 모델이 현대 text를 이미 알아 시간 일관성이 없음. ET 기반으로 부적합 | 발견 시험 없음 | secondary(awesome 목록) |

**표 1c. 대표 URL (TSV의 url 열)**

| 모델 | 대표 URL |
|---|---|
| GPT-1900 (D34) | https://michaelhla.com/blog/machina-mirabilis.html |
| GPT-1900 (D26) | https://huggingface.co/mhla/pre1900_d26_22btok_2epoch |
| GPT-1905 (D34) | https://huggingface.co/mhla/gpt1905-d34 |
| GPT-1964 (D34) | https://huggingface.co/mhla/gpt1964-d34 |
| TypewriterLM-1913 (7.24B) | https://arxiv.org/abs/2606.02991 |
| TypewriterLM-1938 계열 | https://huggingface.co/typewriter-ai/typewriter-1938-3B-EN-DE-base |
| Talkie-1930 (13B) | https://talkie-lm.com/ |
| Ranke-4B 계열 | https://github.com/DGoettlich/history-llms |
| TimeCapsuleLLM v2 (1.22B) | https://github.com/haykgrigo3/TimeCapsuleLLM |
| Mr. Chatterbox | https://huggingface.co/tventurella/mr_chatterbox_model |
| MonadGPT | https://huggingface.co/Pclanglais/MonadGPT |


### 1-1. 표를 읽는 법

| 항목 | 내용 | 확인 수준 |
|---|---|---|
| 「지식 마감」의 뜻이 모델마다 다르다 | GPT-1900은 1900-01-01 이전 출판물, Talkie-1930은 1930-12-31(미국에서 저작권이 소멸하는 경계라는 보고서의 설명), TypewriterLM-1913은 초록이 pre-1913이고 corpus는 1700-1913, 데이터 카드의 재현 필터는 1700 이상 1913 이하여서 1913 포함 여부가 미확정이다. ET의 T0는 모델 이름이 아니라 corpus의 year 열로 감사해서 확정한다 | 1차 문서 직접 확인 |
| 지금 쓸 수 있는 마감 | 1899(GPT-1900), 1904(GPT-1905), 1913(TypewriterLM-1913), 1930(Talkie-1930), 1875(TimeCapsuleLLM, 런던 영어), 1938(TypewriterLM-1938 계열, 세부 미확인). 1914–1929 구간과 1939년 이후에는 공개된 처음부터 학습한(clean-room) 모델이 없다. Ranke-4B의 1929·1933·1939·1946판은 가중치 공개를 확인하지 못했다 | HF 조직 조회로 확인(공개 0개), 공개 시점은 미확인 |
| 능력 | 같은 논문이 잰 벤치(HellaSwag / ARC-Easy)는 GPT-1900 32.3 / 36.7, TypewriterLM 36.1 / 43.3, Talkie-1930 49.8 / 55.8, 현대 GPT-2 XL 48.8 / 50.8, Qwen3-4B 65.9 / 77.4다. GPT-1900 저자는 대부분의 물리 과제에서 실패한다고 썼다. 발견 과제에 필요한 수식 조작이 기반 모델 능력에 막힐 수 있다. 우리 과제 수행 능력은 측정하지 않았다(NOT RUN) | 타 논문의 측정값과 저자 서술 |
| instruct 판의 현대 LLM 영향 | GPT-1900은 SFT 대화 생성과 RL judge에, Talkie는 DPO judge와 합성 대화에, TypewriterLM은 LIMA 지시문 일부에 현대 LLM이 들어갔다(저자 서술). MD-I에 따라 ET-3p·3·4에서 시스템 안의 생성·판정은 시간캡슐 모델만 쓰므로 이는 누수 경로 점검 항목이다 | 저자 서술 |
| 실행 형식 | GPT-1900과 Talkie는 자체 PyTorch 코드(맞춤 구조), TypewriterLM·TimeCapsuleLLM은 HF transformers의 Llama 구조라 activation hook(NP-1)을 걸기 쉽다. Talkie·TypewriterLM·TimeCapsuleLLM에는 제3자 GGUF가 있으나 변환 충실도는 검증하지 않았다. GPT-1900은 GGUF를 못 찾았다 | HF API와 카드 |
| host에서의 크기 | docs/15의 자원 tier 1(host CPU, RAM 약 27GB)에서 GPT-1900 D26은 가중치 파일이 약 4.9GB(카드)이고 D34는 파일 크기를 확인하지 못했으나 파라미터 비례로 약 9–10GB(ESTIMATE)라 둘 다 들어간다. PyTorch CPU 추론 속도는 측정하지 않았다. Talkie 13B는 bf16 약 26GB(참조 코드는 28GB 이상 VRAM 요구)라 host RAM에 맞지 않아 4-bit급 변환본이나 runcrate가 필요하다. 비용과 시간 판단은 docs/15가 소유한다 | 파라미터 수와 카드 서술에서 계산한 크기(ESTIMATE) |
| 라이선스 | GPT-1900·GPT-1905·TimeCapsuleLLM(v2)·Mr. Chatterbox 0.34B는 MIT, Talkie는 Apache-2.0, TypewriterLM은 모델 카드가 없어 미명시다. GPT-1900 corpus의 MIT 표기가 원천 데이터(Institutional Books)의 약관을 상속하는지는 확인하지 못했다. TypewriterLM 데이터 카드는 Institutional Books를 약관상 재배포할 수 없다고 적었다 | 카드 직접 확인 |

### 1-2. 누수 통제에 관한 모델별 메모 (MD-I의 「시간캡슐 모델 자체의 누수」 점검 항목)

| 모델 | 점검할 것 | 근거 |
|---|---|---|
| GPT-1900 | 어느 checkpoint가 1900년 이전만으로 학습됐는지. 같은 저자의 카드는 표준 d34-22btok에 일부 1900년 이후 자료가 있고 별도의 pre-1900-only 기반이 있다고 서술한다. 번역자 서문 같은 후대 문구는 문서 단위 키워드 제거로 걸렀다는 저자의 서술이 있다 | 블로그와 카드 직접 확인 |
| GPT-1905 | 누수 감사 방법이 카드에 없다. 1900–1904 구간이 corpus에 들어 있으므로 T0..t 지식이 이미 가중치에 있다 | 카드 직접 확인 |
| TypewriterLM | 후대 판본·도서관 메타데이터·웹 잔재를 규칙으로 걸렀다고 논문이 서술하고, 그래도 일부 누수가 남는다고 보고한다. 1913년 이후 사건에 대한 recall 누수 수치는 모델 간에 비교됐다(수치의 출처 판본은 표 1b 참조) | 논문 v2 일부 열람 |
| Talkie-1930 | 저자가 FDR 대통령 임기와 New Deal, 13B는 제2차 세계대전과 전후 질서 일부를 안다고 직접 보고했다. 1931년 이후 대상(Chadwick 1932, Turing 1936)에는 누수 probe가 필수다 | 보고서 직접 확인 |
| 모두 | OCR 메타데이터(Digitized by Google 등), 후대 주석·서문, 현대 LLM이 만든 SFT·RL 데이터 | 저자·타 논문 서술 |

## 2. 대상 후보 매트릭스와 MD-H 기준표 점수

후보는 16개다. 발견 시점과 기반 모델 마감의 관계, 두 관문(G1·G2), 기준표 점수를 나란히 둔다. 발견 시점은 역사 일반지식 수준이며, 1차 확인은 §4의 추천 대상에 대해서만 했다. 점수는 조사자의 판단(PROPOSAL)이고 측정이 아니다.

### 2-1. 점수 규칙 (MD-H의 8개 기준 + 추가 1개)

| 기준 | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| C1 직관 의존도(시험 가치) | 계산·자료 축적으로 도달 | 증거 해석의 선택 | 새 개념 도입이 핵심 | 원리 수준의 개념 전환 |
| C2 날짜 있는 과정 기록의 양과 신뢰도 | 거의 없음 | 회고·전기 위주 | 1차 사료(편지·논문)와 회고 혼재 | 연구기를 날짜순으로 복원할 1차 사료가 다수 |
| C3 지식 마감이 맞는 공개 시간캡슐 모델 | 없음 또는 마감이 발견 이후 | 모델은 있으나 간극이 5년 초과이거나 누수 우려가 큼 | 가용하나 라이선스·마감·간극 중 하나가 불명확 | 마감이 T0와 맞고 가용 |
| C4 T0 이전 corpus 확보 | 없음 | 일부 | 공개 corpus가 있으나 재배포·상속 조건이 불명확 | 공개이고 조건이 명확 |
| C5 채점 객관성 | 불가 | 정성 위주 | 정량과 정성 혼합 | 수식·수치로 동치 판정 |
| C6 누수 통제 가능성 | 불가 | 어려움(후대 서술이 방대하거나 모델 누수가 보고됨) | 가능하나 감사 부담이 큼 | 쉬움 |
| C7 언어 | 외국어이고 번역 없음 | 주로 외국어(번역 필요) | 영어와 외국어 혼합 | 영어 중심 |
| C8 저작권 | 대부분 보호 | 상당 부분 보호 | 원문은 소멸했으나 번역·편집판·아카이브에 권리 주장 | 대부분 소멸 또는 명확한 허용 |
| C9(추가) 기반 능력 적합 | 대상 수준의 수식 조작을 기대하기 어려움 | 낮음 | 중간 | 높음 |

- 관문 G1: C3가 2 이상(마감이 맞는 가용 공개 모델이 있다). MD-H가 「주요 기준」이라고 한 항목이다.
- 관문 G2: C5가 2 이상(수식·수치로 채점할 수 있다).
- C9는 MD-H 본문의 「확인할 것: 공개 모델의 수학·물리 능력」을 점수 칸으로 만든 것이다. 모델 카드와 타 논문의 벤치에서 조사자가 판단했고 우리 과제 수행 능력은 측정하지 않았다(NOT RUN).
- 합계는 참고용이다. 점수 차이가 2 이하면 구별하지 않는다. 선택은 관문 통과가 먼저고 그다음이 위험 검토다.

### 2-2. 후보 매트릭스 (표 2a)

| ID | 대상(발견) | 발견 시점 | 기반 모델 후보(T0) | 마감과 발견의 간극 | 주 언어 | G1 | G2 | 판정 |
|---|---|---|---|---|---|---|---|---|
| TG-01 | Einstein 1905: 광양자, 브라운 운동, 특수상대성, 질량-에너지(사용자가 든 예) | 1905-03 ~ 1905-09 | GPT-1900(T0 1900-01-01, 주), GPT-1905(T0 1905-01-01, 비교) | 5년 / 0 | 독일어(논문·편지), 영어는 편집·번역판 | 통과 | 통과 | 주력 후보 |
| TG-02 | Planck 1900: 복사 법칙과 에너지 요소 | 1900-10 ~ 1900-12 | GPT-1900(T0 1900-01-01) | 1년 미만 | 독일어 | 통과 | 통과 | pilot 후보 |
| TG-03 | Einstein 일반상대성 1915(Hassabis 판본 a) | 1915-11 | TypewriterLM-1913(T0 1912말 또는 1913말 미확정). Ranke-4B-1913은 미공개 | 2–3년(Hassabis의 1911과는 1–2년 차이) | 독일어 | 통과(조건부) | 통과 | 대안(확장) |
| TG-04 | Bohr 원자 모형 1913 | 1913-07 ~ 1913-11 | 없음. TypewriterLM은 1913을 포함할 수 있어 누수, GPT-1905는 간극 8년 | 해당 없음 | 영어, 덴마크어 | 불통과 | 통과 | 제외 |
| TG-05 | Rutherford 핵 원자 1911 | 1911-05 | GPT-1905(간극 6년). TypewriterLM은 1911을 포함 | 6년 | 영어 | 불통과 | 통과 | 후순위(ET-1 재료) |
| TG-06 | Chadwick 중성자 1932 | 1932-02 ~ 1932-05 | Talkie-1930(T0 1930-12-31) | 약 1년 | 영어, 일부 프랑스어·독일어 | 통과 | 통과 | pilot 후보 |
| TG-07 | Turing 계산 가능성 1936 | 1936 중반 ~ 1936 말 | Talkie-1930 | 약 5년 | 영어 | 통과 | 통과 | 대안 |
| TG-08 | 핵분열 1938–39(Hahn·Strassmann, Meitner·Frisch) | 1938-12 ~ 1939-02 | TypewriterLM-1938 계열(세부 미확인) | 불명 | 독일어 | 불명 | 통과 | 보류 |
| TG-09 | Shannon 정보 이론 1948 | 1948 | 없음(Ranke-4B-1946 미공개) | 해당 없음 | 영어 | 불통과 | 통과 | 제외(MD-H 후보였음) |
| TG-10 | Darwin 자연선택 1838 | 1838-09 ~ 1838-10 | 없음. TimeCapsuleLLM(마감 1875)은 『종의 기원』 이후라 누수, 자체 사전학습 필요 | 해당 없음 | 영어 | 불통과 | 불통과 | 후순위(ET-1 재료) |
| TG-11 | Mendeleev 주기율 1869 | 1869-03 | 없음. TimeCapsuleLLM(마감 1875)이 발견 이후 | 해당 없음 | 러시아어, 독일어 | 불통과 | 통과 | 후순위(ET-1 재료) |
| TG-12 | Maxwell 전자기장 이론 1861–65 | 1861 ~ 1865 | 없음. TimeCapsuleLLM(마감 1875)이 발견 이후 | 해당 없음 | 영어 | 불통과 | 통과 | 후순위 |
| TG-13 | Semmelweis 손 씻기 1847 | 1847 | 없음 | 해당 없음 | 독일어, 헝가리어 | 불통과 | 통과 | 후순위(ET-1 재료) |
| TG-14 | Watson·Crick 이중나선 1953 | 1953 | 없음(Ranke-4B-1946 미공개, Talkie와 23년 간극) | 해당 없음 | 영어 | 불통과 | 통과 | 제외 |
| TG-15 | Gödel 불완전성 1930–31 | 1930-09 ~ 1930-11 | 없음. Talkie의 마감(1930-12-31)이 발견 이후, Ranke-4B-1929 미공개 | 해당 없음 | 독일어 | 불통과 | 통과 | 제외 |
| TG-16 | 양자역학 1925–26(Heisenberg, Schrödinger, de Broglie 1923–24) | 1923 ~ 1926 | 없음(1914–1929 공백) | 해당 없음 | 독일어 | 불통과 | 통과 | 제외 |

### 2-3. MD-H 기준표 점수 (표 2b)

| ID | C1 직관 | C2 기록 | C3 모델 | C4 corpus | C5 채점 | C6 누수 | C7 언어 | C8 저작권 | 합(C1–C8) | C9 능력 | 합(C1–C9) | G1·G2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TG-01 | 3 | 2 | 3 | 2 | 3 | 1 | 1 | 2 | 17 | 1 | 18 | 통과 |
| TG-02 | 3 | 1 | 3 | 2 | 3 | 2 | 1 | 3 | 18 | 1 | 19 | 통과 |
| TG-03 | 3 | 3 | 2 | 2 | 3 | 1 | 1 | 2 | 17 | 0 | 17 | 통과 |
| TG-04 | 3 | 3 | 1 | 2 | 3 | 1 | 2 | 2 | 17 | 1 | 18 | G1 불통과 |
| TG-05 | 2 | 2 | 1 | 2 | 3 | 2 | 3 | 3 | 18 | 1 | 19 | G1 불통과 |
| TG-06 | 2 | 1 | 2 | 1 | 3 | 1 | 2 | 1 | 13 | 2 | 15 | 통과 |
| TG-07 | 3 | 1 | 2 | 1 | 3 | 1 | 2 | 1 | 14 | 1 | 15 | 통과 |
| TG-08 | 3 | 2 | 1 | 1 | 3 | 1 | 1 | 1 | 13 | 1 | 14 | G1 불통과(정보 부족) |
| TG-09 | 3 | 1 | 0 | 0 | 3 | 1 | 3 | 0 | 11 | 1 | 12 | G1 불통과 |
| TG-10 | 3 | 3 | 0 | 2 | 1 | 1 | 3 | 3 | 16 | 2 | 18 | G1·G2 불통과 |
| TG-11 | 2 | 1 | 0 | 1 | 3 | 1 | 1 | 3 | 12 | 2 | 14 | G1 불통과 |
| TG-12 | 3 | 2 | 0 | 2 | 3 | 1 | 3 | 3 | 17 | 0 | 17 | G1 불통과 |
| TG-13 | 2 | 2 | 0 | 0 | 2 | 1 | 1 | 3 | 11 | 2 | 13 | G1 불통과 |
| TG-14 | 3 | 2 | 0 | 0 | 2 | 1 | 3 | 0 | 11 | 1 | 12 | G1 불통과 |
| TG-15 | 3 | 1 | 0 | 1 | 3 | 1 | 1 | 1 | 11 | 1 | 12 | G1 불통과 |
| TG-16 | 3 | 2 | 0 | 0 | 3 | 1 | 1 | 1 | 11 | 0 | 11 | G1 불통과 |

### 2-4. 점수 근거 (관문을 통과한 5개와 판단이 갈릴 만한 칸)

| ID | 근거 | 확인 수준 |
|---|---|---|
| TG-01 | C3=3: GPT-1900의 마감이 T0와 정확히 맞고 MIT. C2=2: 1901–1904 논문과 편지, 1905-05경 Habicht 편지(CPAE 5권 문서 27, 날짜는 5-18 또는 5-25로 편집되나 2026년 arXiv 논문이 6-01을 주장)가 있으나 연구 과정의 회고가 많다. C6=1: 전기·교과서 같은 후대 서술이 가장 방대하고 GPT-1900 표준 판에는 일부 1900년 이후 자료가 있다는 카드 서술이 있다. C7=1: 논문·편지는 독일어이고 영어는 편집 번역판. C8=2: 원문은 소멸 가능성이 있으나 편집판과 아카이브는 Hebrew University와 Princeton UP가 권리를 주장한다. C9=1: GPT-1900은 저자가 대부분의 물리 과제 실패라고 평가 | 1차 문서와 2차 설명 혼합 |
| TG-02 | C3=3: 마감이 T0와 정확히 일치. C2=1: 보간식에서 에너지 요소까지 날짜 있는 연구 과정 기록이 얇다. C8=3: 저자(1947 사망)와 논문 모두 소멸 | 2차 설명(Planck의 법칙 연표는 Wikipedia 열람, 일(日)은 미확인) |
| TG-03 | C2=3: 가장 풍부하다(Zurich 노트, Besso·Grossmann·Hilbert 편지 등. 구체 문서는 미확인). C3=2: TypewriterLM은 가용하나 모델 카드가 없어 라이선스가 불명이고 1913 포함 여부가 미확정이며 Hassabis의 T0(1911)와 1–2년 차이. C9=0: 텐서 미적분은 7B 1913 모델의 능력 밖일 가능성이 크다 | 2차 설명과 모델 메타데이터 |
| TG-06 | C3=2: Talkie는 Apache-2.0이고 간극이 약 1년이나 마감 이후 누수(FDR, 제2차 세계대전 일부)가 보고돼 있다. C2=1: 논문 날짜는 명확하나 실험 노트 접근은 확인하지 못했다. C6=1: 누수 probe가 필수. C8=1: 1931–32 문헌은 보호 기간 안이다 | 1차(보고서)와 2차(Wikipedia) 혼합 |
| TG-07 | C3=2: 간극 약 5년이라 1931–1936의 세계 지식을 stream으로 넣어야 한다. C2=1: 전기와 회고 위주로 날짜 있는 과정 기록이 얇다. Talkie 보고서가 Turing 1936 논문을 마감 이후 사례의 하나로 그림에 넣었다 | 1차(보고서)와 2차 혼합 |
| TG-04 | G1 불통과의 이유: TypewriterLM 데이터 카드의 재현 필터가 1913 이하라 Bohr의 1913년 논문이 학습 corpus에 있을 수 있다. 가장 직접적인 마감 불일치 사례다 | 데이터 카드 직접 확인 |
| TG-10 | G1 불통과: 영어이고 사료가 가장 풍부한 사례이나 공개 모델이 없다. 자체 사전학습(P4–P6의 안 2·3)이 필요하다. docs/15가 비용을 소유한다 | 모델 목록 조회 |

## 3. 추천 묶음과 근거

### 3-1. 묶음 (표 3a) — PROPOSAL, 최종 선택은 사용자 결정(DC-W2c-01)

| 역할 | ID | 대상 | 기반 모델 | T0 | T1 | 이유 | 주요 위험 |
|---|---|---|---|---|---|---|---|
| 주력(ET-4 봉인 후보) | TG-01 | Einstein 1905 | GPT-1900(주), GPT-1905(비교) | 1900-01-01 / 1905-01-01 | 구성요소별(표 4a) | 사용자가 든 예이고, 마감이 T0와 정확히 맞는 공개 모델이 있으며, 논문 4건을 따로 채점할 수 있고, 같은 문제를 다룬 비발견자의 사료가 풍부하다 | 기반 능력, 독일어 사료와 번역 누수, 후대 서술에 의한 사후 편향, 사료 접근과 권리 |
| pilot A(ET-3p와 ET-3의 개발) | TG-02 | Planck 1900 | GPT-1900 | 1900-01-01 | 1900-10 ~ 1900-12 | 주력과 기반·T0가 같고 대상만 달라 개발과 봉인을 대상 단위로 나눌 수 있다. 창이 작고 수식으로 채점한다. 1.7B–3.3B 기반이라 host 재현이 가능한 크기다 | Planck 1900의 결과가 주력의 T0 이후 세계 지식(1900–1904)에 들어간다. pilot run의 저장 상태를 주력 run에 재사용하면 오염이다 |
| pilot B(ET-3의 개발, 두 번째 기반) | TG-06 | Chadwick 중성자 1932 | Talkie-1930 | 1930-12-31 | 1932-02 ~ 1932-05 | 영어이고 창이 짧으며 사료 안에 같은 데이터를 다르게 해석한 비발견자(Joliot-Curie 부부, Bothe·Becker)가 있다. Apache-2.0 | 마감 이후 누수(probe 필수), 1931–32 문헌의 저작권, 13B는 host RAM에 맞지 않는다 |
| 대안 1(주력 확장 후보) | TG-03 | 일반상대성 1915 | TypewriterLM-1913 | 1912말 또는 1913말(미확정) | 1915-11 | Hassabis의 판본 a. 날짜 있는 과정 기록이 후보 중 가장 풍부하다 | 모델 카드가 없어 라이선스 미명시, 7B 1913 모델의 수학 능력, 독일어 사료, 마감 1913과 Hassabis의 1911의 차이 |
| 대안 2 | TG-07 | Turing 1936 | Talkie-1930 | 1930-12-31 | 1936 중반 ~ 말 | 영어이고 정의·증명으로 채점할 수 있다. Talkie 보고서가 같은 논문을 마감 이후 사례로 들었다 | 간극 약 5년(1931–1936 세계 지식을 stream으로 넣어야 한다), 날짜 있는 과정 기록이 얇음, 누수 |

기반 단위의 쌍: GPT-1900은 Planck(개발)과 Einstein(봉인), Talkie-1930은 Chadwick(개발)과 Turing(봉인 후보)이다. 쌍으로 두는 이유는 개발 중에 얻은 프롬프트·probe·절차 수정이 봉인 대상의 정답과 무관하게 같은 기반의 특성에만 맞춰지도록 하려는 것이다. 이 분리 규칙의 공식 정의는 docs/17이 소유한다.

### 3-2. 다른 후보를 고르지 않은 이유 (한 줄)

| 후보 | 이유 |
|---|---|
| TG-04 Bohr 1913, TG-05 Rutherford 1911 | 마감이 맞는 모델이 없다(TypewriterLM의 재현 필터가 1913을 포함하고, GPT-1905와는 6–8년 간극). 영어 사료와 소멸된 저작권 덕분에 ET-1 재분장 원형의 재료로는 좋다 |
| TG-08 핵분열 1938–39 | TypewriterLM-1938 계열은 모델 카드와 누수 감사 정보가 없다. 세부를 확인하면 재평가한다 |
| TG-09 Shannon 1948, TG-14 DNA 1953 | MD-H 잠정안에서 마감 1946 모델을 상정했으나 Ranke-4B의 공개를 확인하지 못했다 |
| TG-10~13 Darwin, Mendeleev, Maxwell, Semmelweis | 공개 모델이 없다. 자체 사전학습(P4–P6의 확보 안 2·3)이 필요하다. ET-1 재분장 원형의 재료로 쓴다 |
| TG-15 Gödel, TG-16 양자역학 | 발견이 마감 이전이거나 1914–1929 공백에 있다 |

### 3-3. MD-H 잠정안과 달라진 점 (표 3b)

| MD-H 잠정안 | 조사 결과 | 바뀐 것 | 이유 |
|---|---|---|---|
| 주력 Einstein 1905, T0 1900말, 기반 pre-1900 공개 모델. 확인할 것: 사료의 언어·접근·저작권, 공개 모델의 수학·물리 능력 | GPT-1900(마감 1900-01-01)과 GPT-1905(마감 1905-01-01)가 공개돼 있다. 사료는 독일어이고 영어는 편집 번역판이다. CPAE의 새 플랫폼(Einstein Portal)은 일부 무료와 구독이고, 편집판은 Hebrew University·Princeton UP가 권리를 주장한다. GPT-1900 저자는 대부분의 물리 과제 실패라고 평가했다 | 주력은 유지한다. 비교 기반으로 GPT-1905를 더한다. 네 가지 확인 사항은 위험으로 기록한다 | 사용자가 든 예이고 마감이 맞는 유일한 물리 사례이기 때문이다. 능력 한계는 도달 수준 상한을 낮게 보고하는 쪽으로 반영한다(docs/17 소유) |
| 후보 일반상대성 1915, T0 1911–1913, 기반 마감 1913 공개 모델 | TypewriterLM-1913이 공개돼 있다(라이선스 미명시, 1913 포함 여부 미확정). Ranke-4B-1913은 가중치를 확인하지 못했다 | 주력 후보에서 대안(확장)으로 내린다 | 라이선스와 능력(C9=0)이 불확실하고 Hassabis의 T0(1911)와 기반의 마감이 다르다 |
| 후보 1930년 이후(중성자 1932, 계산 가능성 1936, 핵분열 1938, 정보 이론 1948), 기반 마감 1929–1946 공개 모델 | Ranke-4B의 1929–1946판은 공개를 확인하지 못했다. Talkie-1930만 가용하다 | 1932와 1936만 남기고 Talkie-1930을 기반으로 한다. 1938은 보류, 1948은 제외한다 | G1(마감이 맞는 가용 모델) |
| 후순위 Darwin 1838, Mendeleev 1869, Semmelweis 1847 | 공개 모델 없음 | 유지하고 Maxwell을 더한다. ET-1 재료로 쓴다 | TimeCapsuleLLM(마감 1875)은 발견 이후다 |
| 개발용(pilot)과 봉인 주력을 나눈다 | 기반 하나가 대상 둘을 맡을 수 있다 | pilot A(Planck 1900)를 새로 더한다. 기반별 pilot·봉인 쌍을 제안한다 | 기반·T0가 같아 개발 때 절차를 다듬어도 봉인 대상의 내용은 건드리지 않는다 |
| 기준표 8개 | MD-H가 「확인할 것」으로 남긴 기반 모델 능력을 칸으로 만들 수 있다 | C9(기반 능력 적합)와 관문 G1·G2를 더한다 | 점수 합이 아니라 관문으로 거르는 편이 주관적 점수의 오차에 덜 민감하다 |

### 3-4. ET-3p 후보 조합 (사실만. 설계는 docs/18, 계산은 docs/15 소유)

| 조합 | 사실 | 한계 |
|---|---|---|
| GPT-1900 D26(1.68B) 또는 D34(3.29B) + Planck 1900 | D26 가중치 파일이 약 4.9GB(카드)이고 D34는 약 9–10GB(파라미터 비례 추정, ESTIMATE)라 host CPU RAM에 올라간다. 자체 PyTorch 코드라 activation hook을 걸 수 있다. context가 2048 token이다 | 긴 stream·긴 이력 투입이 안 된다. 능력이 낮다. instruct 판의 현대 LLM 영향 |
| Talkie-1930 13B + Chadwick 1932 | Apache-2.0. 제3자 4-bit급 변환본이 있다(충실도 미검증) | bf16은 약 26GB라 host RAM에 맞지 않는다. hook이 필요한 NP-1은 PyTorch 원본이 필요하다 |
| TypewriterLM-1913 7.24B + 일반상대성 | HF transformers Llama 구조라 hook이 쉽다. context 8192. bf16 약 14.5GB(7.24B × 2바이트, ESTIMATE)로 host RAM에 빠듯하게 들어간다 | 라이선스 미명시. 1913 포함 여부 미확정 |

## 4. 추천 묶음의 데이터 계획

ET의 운영 정의, stream 항목 schema, 입력 tier, rubric은 docs/17이 소유한다. 여기서는 대상과 자료의 사실만 낸다. 사료와 논문의 원문은 저장소에 재배포하지 않는다(구성한 stream은 항목마다 출처 인용과 해시만 둔다). 확인하지 못한 칸은 「미확인」이다.

### 4-1. TG-01 Einstein 1905 (주력)

| 항목 | 내용 | 확인 수준 |
|---|---|---|
| W(≤T0)를 맡을 모델 | GPT-1900(T0 1900-01-01). 후보 checkpoint는 둘이다. 표준 `d34-22btok`은 같은 저자의 카드가 일부 1900년 이후 자료를 포함한다고 쓴 판이고, `physics-clm-pre1900`은 pre-1900-only 기반에서 이어 학습한 중간 판이다. 어느 것을 쓸지는 누수 감사 뒤에 정한다(DC-W2c-02). 비교용으로 GPT-1905(T0 1905-01-01)를 둔다. context 2048 token. corpus는 공개이고 year 열이 있어 문서 단위 감사가 가능하다. 단 corpus 필터가 radiation·quantum·nuclear 같은 모호한 용어가 3개 이상 겹치는 문서를 제거하므로 1900년 이전 복사 이론 문헌이 과하게 빠졌을 수 있다(추정, 검증 필요) | 카드와 dataset 카드 직접 확인 |
| T0 이후 세계 지식 W(T0..t) | 1900-01 ~ 1905-06 구간을 System ONE의 지속학습 입력으로 넣는다(MD-G 기본). 출처 후보: (1) 영어 동시대 정기간행물(Nature, Philosophical Magazine, Proc. Royal Society, Physical Review, Science 등)은 1931년 이전 출판이라 공개 도메인이고 Internet Archive·HathiTrust에 스캔이 있다(항목별 확인 필요), (2) 외국어 논문의 동시대 영어 요약인 Science Abstracts(IEE와 Physical Society of London이 1898년부터 발행, 1898년 1,423건, 1903년부터 물리 분책. HathiTrust 쪽수 이미지가 있다고 Online Books Page가 적는다), (3) 독일어 원문(Annalen der Physik 등)은 영어 전용 기반이 읽지 못하고 현대 LLM 번역은 MD-I의 누수 경로라 쓸 수 없다. 따라서 (1)(2)를 우선하고, 사람이 한 당대 번역이나 번역 없는 원문 투입의 가부는 결정 항목이다(DC-W2c-04). 규모는 선별 목록을 만든 뒤에 센다(미확인). 핵심 항목: Planck 1900–01 복사 법칙, Lenard 1902 광전 실험, Kaufmann 1901–03 전자 질량 실험, Lorentz 1904, Poincaré 1904, Rutherford·Soddy 1902–03, J.J. Thomson 1904 | 출처 유형은 확인, 개별 문서 목록과 규모는 미확인 |
| 인물 stream의 1차 사료 | CPAE(Collected Papers of Albert Einstein) 1권(초기 1879–1902), 2권(스위스 시기 논문 1900–1909), 5권(스위스 시기 서신 1902–1914). 원문은 독일어이고 영어 번역 보충판이 붙는다. 접근: Princeton UP와 Paradigm의 Einstein Portal이 1879–1930 17권을 원문과 영어 번역으로 싣고, 일부는 무료이며 개인·기관 구독이 있다(공지 직접 확인). 이전의 무료 Digital Einstein 사이트가 2025-08-15에 종료됐다는 서술은 2차 출처만 있다. 편지: Marić 서신(1897–1903), Besso, Habicht(1905-05경의 네 논문 편지는 5권 문서 27, 편집 날짜 5-18 또는 5-25, 2026년 arXiv 논문이 6-01을 주장), Solovine. 독서: Olympia Academy(1902 결성, 처음 읽은 책은 Pearson의 Grammar of Science, 이어 Mach, Poincaré, Mill, Hume, Spinoza 등)는 회고에 기대며 Wikipedia 문서 자체가 출처가 약하다고 표시돼 있어 입력 tier B 이하로 다룬다. 저작권: Hebrew University가 Einstein의 저작에 대한 권리를 가지며 Princeton UP가 편집판의 출판권을 가진다(두 기관의 페이지를 인용한 검색 요약으로 확인했고 원문 페이지는 직접 열람하지 못함). 원문 재배포는 하지 않는다 | Princeton UP 공지·Wikipedia·arXiv 검색으로 확인, 개별 문서 열람은 미확인 |
| T0와 T1 | T0는 1900-01-01(GPT-1900) 또는 1905-01-01(GPT-1905). T1은 구성요소별이다(표 4a). 사용자 원문의 「1901–1904」는 입력 구간 P_post의 핵심이고 「1904년 발견」은 역사의 1905와 다르다. 조용히 맞추지 않고 기록한다: 입력은 1904까지, 논문은 모두 1905년이다 | 날짜는 Wikipedia 열람(1차 확인 못함) |
| 발견의 구성요소(rubric 재료) | (a) 광양자: 고주파(Wien 영역) 복사를 독립 에너지 양자 hν의 기체처럼 다루고 광전 효과·Stokes 법칙을 설명. (b) 브라운 운동: 삼투압과 Stokes 점성을 결합해 확산 계수와 평균 제곱 변위를 유도하고 N_A 측정을 예측. (c) 특수상대성: 상대성 원리와 광속 불변에서 동시성을 재정의하고 Lorentz 변환, 길이 수축, 시간 지연, 속도 합성을 유도. (d) 질량-에너지: 복사를 내보낸 물체는 L/c²만큼 질량을 잃는다. 수식 동치와 수치 예측으로 채점하는 재료다. rubric 자체는 docs/17이 소유한다 | 역사 일반지식 수준(원문 미확인) |
| 비발견자 대조 stream 후보 | 특수상대성: Lorentz(1895, 1899, 1904)와 Poincaré(1898–1905)는 같은 전기동역학 문제에서 에테르를 유지한 다른 결론에 갔다. Abraham(1902–03 강체 전자). 광양자: Planck(양자는 공진자에만 두고 광양자는 받지 않음), Lenard(1902 광전 실험과 다른 설명). 브라운 운동: Smoluchowski(1906), Sutherland(1905). 질량-에너지: Hasenöhrl(1904 공동 복사). 사료는 대부분 1931년 이전 출판이다. 무관한 인물 stream은 같은 시기의 다른 분야 연구자 한 명을 후속 작업이 고른다(미선정) | 역사 일반지식 수준(원문 미확인). 후속 확인 필요 |

**표 4a. Einstein 1905 구성요소의 T1 후보 (Wikipedia 열람, 1차 확인 못함)**

| 구성요소 | 수신 | 발행 | 서지 |
|---|---|---|---|
| 광양자(광전 효과) | 1905-03-18 | 1905-06-09 | Annalen der Physik 17(6), 132–148 |
| 브라운 운동 | 1905-05-11 | 1905-07-18 | Annalen der Physik 17(8), 549–560 |
| 특수상대성 | 1905-06-30 | 1905-09-26 | Annalen der Physik 17(10), 891–921 |
| 질량-에너지 | 1905-09-27 | 1905-11-21 | Annalen der Physik 18(13), 639–641 |

### 4-2. TG-02 Planck 1900 (pilot A)

| 항목 | 내용 | 확인 수준 |
|---|---|---|
| W(≤T0)를 맡을 모델 | GPT-1900(T0 1900-01-01). Hla의 평가 문제 중 UV 파탄(Planck 법칙) 항목이 같은 대상을 단서와 함께 다룬다(단서가 있어 ET와 다르다) | 블로그 직접 확인 |
| W(T0..t) | 1900-01 ~ 1900-10. Rayleigh 1900-06(저주파 equipartition 식, Philosophical Magazine, 영어), 1900-09 실험가들의 Wien-Planck 식 이탈 보고, Rubens·Kurlbaum의 장파장 측정(1900-10), Planck 자신의 1899–1900 복사 논문(독일어). 영어 자료를 우선한다. 규모는 미확인 | Planck의 법칙 연표(Wikipedia)로 확인 |
| 인물 stream의 1차 사료 | Planck의 1897–1900 불가역 복사 논문(Annalen, 독일어, 소멸), Boltzmann의 조합 해석, Wien의 변위·분포 법칙(1896), 독일물리학회(DPG) 회의록. 날짜 있는 연구 과정 기록은 얇다. Planck가 1931년 편지에서 에너지 요소를 「절망의 행위」라고 회고했다는 서술은 회고이므로 입력 tier B 이하다(출처 미확인) | 회고 서술은 미확인 |
| T0와 T1 | T0 1900-01-01. T1: 1900-10(보간식 제시. Wikipedia는 10-19 DPG 회의에 연결해 적고 보간식을 만든 정확한 날은 적지 않음), 1900-12(에너지 요소 발표. 일(日)은 이번 조사에서 미확인) | 부분 확인 |
| 발견의 구성요소 | (a) 보간 법칙 u(ν,T) 자체, (b) 에너지 요소 ε = hν와 공진자 통계, (c) 상수 h와 k의 수치. 수식·수치 채점 재료 | 역사 일반지식 수준 |
| 비발견자 대조 stream | Wien(1896 법칙), Rayleigh(1900-06), Jeans(1905), Thiesen(1900, 선행 식), 실험가 Rubens·Kurlbaum·Lummer·Pringsheim. 같은 자료에서 다른 식에 간 사례다 | Wien·Rayleigh는 연표 확인, 나머지는 미확인 |

### 4-3. TG-06 Chadwick 중성자 1932 (pilot B)

| 항목 | 내용 | 확인 수준 |
|---|---|---|
| W(≤T0)를 맡을 모델 | Talkie-1930 base(T0 1930-12-31, 13B, Apache-2.0). 마감 이후 누수가 보고된 모델이라 중성자 관련 지식의 유무를 probe로 먼저 잰다 | 보고서 직접 확인 |
| W(T0..t) | 1931-01 ~ 1932-02. Joliot-Curie의 Comptes Rendus 194:273(1932, 프랑스어: 수소 함유 물질에서 약 5 MeV 양성자가 나오고, 감마선 해석이면 약 50 MeV가 필요하다는 논리 문제가 있었음), 그 밖의 1931–32 보고. 1931년 이후 문헌은 저작권 기간 안이라 구성한 stream은 출처 인용과 해시만 둔다. T0 이전이라 기반에 이미 있어야 할 것: Bothe·Becker 1930(Z. Phys. 66:289, 감마선으로 해석), Rutherford 1920 Bakerian 강연(Proc. R. Soc. A 97:374, 질량 1의 중성 입자 가설) | Wikipedia 열람(서지와 해석 확인), 개별 원문 미확인 |
| 인물 stream의 1차 사료 | Chadwick의 Nature 129:312(1932-02, 「Possible Existence of a Neutron」)와 Proc. R. Soc. A 136:692–708(1932, 5월 송고, 「The Existence of a Neutron」). Cavendish 연구소의 실험 노트와 Rutherford와의 서신은 접근을 확인하지 못했다. Chadwick 자신의 회고는 후대 서술이라 tier B 이하다 | 서지 확인, 노트·서신은 미확인 |
| T0와 T1 | T0 1930-12-31. T1 1932-02(Nature 투고)와 1932-05(상세 논문). 창이 약 1–2개월로 짧다 | Wikipedia 열람 |
| 발견의 구성요소 | (a) 5 MeV 양성자와 50 MeV 감마선의 에너지 불일치를 인식, (b) 전하가 없고 양성자 질량 정도인 입자 가설, (c) 충돌 운동학으로 질량 추정, (d) 에너지·운동량 보존 논증. 수치(질량 추정)로 채점 가능 | Wikipedia 서술 기반 |
| 비발견자 대조 stream | Irène·Frédéric Joliot-Curie(1932-01, 감마선 해석 유지), Bothe·Becker(1930, 감마선). 출판 안 된 Majorana의 결론은 stream이 없다 | Wikipedia 열람 |

### 4-4. TG-03 일반상대성 1915 (대안 1)

| 항목 | 내용 | 확인 수준 |
|---|---|---|
| W(≤T0)를 맡을 모델 | TypewriterLM-1913(7.24B, context 8192, HF transformers). T0는 1912말과 1913말 사이에서 corpus year 열 감사로 확정한다(1912–13의 Einstein·Grossmann 논문이 corpus에 있는지가 핵심). 모델 카드 없음 | 논문·HF 메타데이터 확인 |
| W(T0..t) | 1914 ~ 1915-11. Nordström의 스칼라 중력 이론(1912–14), Einstein·Fokker 1914, Hilbert 1915-11, 수성 근일점 관측(Le Verrier, Newcomb의 43″는 이미 알려진 사실이라 T0 이전 지식). 독일어 비중이 크다. 규모 미확인 | 역사 일반지식 수준 |
| 인물 stream의 1차 사료 | CPAE 4권(논문 1912–14, Zurich 노트 포함), 5권·8권(서신), 6권(베를린 시기 논문 1914–17). 원문 독일어, 접근·권리는 4-1과 같다. 날짜 있는 과정 기록은 후보 중 가장 풍부하다 | 권 구성은 편집판 일반 정보(개별 확인 못함) |
| T0와 T1 | T1은 1915-11(장 방정식 확정, 같은 달 수성 근일점 계산). Hassabis의 판본 a는 마감 1911 | 역사 일반지식 수준 |
| 발견의 구성요소 | (a) 등가 원리(1907) → 빛 휨 예측(1911), (b) 계량 텐서를 중력 퍼텐셜로 보는 것(1912–13), (c) 일반 공변성과 장 방정식(1915), (d) 수성 근일점 43″와 빛 휨 1.74″ 수치. 텐서 미적분이 필요하다 | 역사 일반지식 수준 |
| 비발견자 대조 stream | Nordström(스칼라 중력), Abraham(변광속), Mie. 같은 중력 문제를 Lorentz 공변 틀 안에서 푼 사례다 | 역사 일반지식 수준 |

### 4-5. TG-07 Turing 1936 (대안 2)

| 항목 | 내용 | 확인 수준 |
|---|---|---|
| W(≤T0)를 맡을 모델 | Talkie-1930 base(T0 1930-12-31) | 보고서 직접 확인 |
| W(T0..t) | 1931 ~ 1936. Gödel 1931(독일어), Church의 1932–36 논문, Kleene 1935, Herbrand, Hilbert·Bernays 1934. 대부분 1931년 이후라 저작권 기간 안이고 독일어가 섞인다. 간극이 5년이라 투입량이 크다 | 역사 일반지식 수준 |
| 인물 stream의 1차 사료 | Turing의 1936–37 논문(Proc. London Math. Soc. ser. 2, 42:230–265, 정정 43:544–546). 학생기 독서와 Newman의 1935 강의는 전기 서술에 의존한다. 날짜 있는 과정 기록은 얇다 | 서지는 Wikipedia로 확인, 수신·낭독 날짜(통설 1936-05-28, 1936-11-12)는 미확인 |
| T0와 T1 | T0 1930-12-31, T1 1936 중반~말 | 미확인 |
| 발견의 구성요소 | (a) 사람 계산자의 분석에서 기계 모델 도출, (b) 계산 가능한 수의 정의, (c) 범용 기계, (d) 결정 문제의 해결 불가능성. 정의·증명으로 채점 | 역사 일반지식 수준 |
| 비발견자 대조 stream | Church(1936, 람다 계산, 같은 부정적 결론에 독립 도달), Post(1936), Kleene, Hilbert 학파의 기대(결정 가능). 「다른 결론」보다 「같은 결론에 다른 경로」 사례가 많아 대조 설계가 달라진다 | 역사 일반지식 수준 |

## 5. 「Einstein test」 제안의 출처, 판본, 비판, 참고 영상

### 5-1. 판본 표 (표 5a)

직접 인용은 직접 열어 확인한 문장만, 짧게 쓴다. 나머지는 요지와 확인 수준으로 적는다.

| 판본 | 지식 마감 → 대상 | 누가·언제·어디서 | 문구의 성격 | 확인 수준 |
|---|---|---|---|---|
| 선행 서술 | 연도 없음. Einstein이 접근할 수 있던 정보만으로 일반상대성 | TIME의 Billy Perrigo, 2025-04-15 게재, Hassabis 인터뷰 기사. 기사는 AGI의 존재 시험으로 「come up with general relativity with only the information Einstein had access to」라고 쓴다. 기자의 서술이고 Hassabis의 직접 인용이 아니다 | 기자 요약 | WebFetch 요약으로 확인(원문 전체 열람 못함, TIME 서버가 직접 요청을 막음) |
| 판본 a | 1911 → 일반상대성(1915) | Hassabis의 2026-02 India AI Impact Summit 기간 발언. 한 2차 글은 IISc Bangalore에서 Varun Mayya와 한 2026-02-17 인터뷰라고 적고 주 무대 발언은 02-18이라고 구분한다. OfficeChai(2026-02-20)는 「knowledge cutoff of, say, 1911」, 「come up with general relativity」를 인용한다. 같은 말을 적은 전사본(Singju Post)이 있다고 검색 요약이 적었으나 접속하지 못했다 | 보도의 인용 | 2차(전사본 원문 미열람) |
| 판본 a의 재인용 | 같음 | Talkie 보고서(2026-04): 「As Demis Hassabis has asked, could a model trained up to 1911 independently discover General Relativity, as Einstein did in 1915?」 | 1차 보고서가 Hassabis의 질문을 요약 인용 | 보고서 직접 확인 |
| 판본 b | 1901 → 1905년 annus mirabilis 논문들 | (1) digit.in(2026-05-28 갱신, Siddharth Chauhan)이 Google I/O 2026 기간 Hassabis의 Axios 인터뷰 절에서 1901년 knowledge cutoff로 Einstein의 1905년 통찰에 도달하는지를 기자의 서술로 적는다. 같은 글의 Hassabis 직접 인용은 「I think today systems clearly can't」이다. 2026-05-26자 Axios 기사가 검색되나 열람하지 못했다(403). (2) WSJ Magazine의 Ben Cohen 인물 기사(2026-10-21)를 인용한 aiweekly.co(같은 날)가 「a system trained only on human knowledge up to 1901」이 1905년의 일을 내놓는지로 서술한다. 두 곳 모두 Hassabis가 그 연도를 직접 말했는지는 구분되지 않는다. Startup Fortune과 Trending Topics 글에는 이 서술이 없다 | 기자 서술 | WSJ(유료)와 Axios 원문은 열람 못함. 가장 약한 근거 |
| 공식 제안 | 연도 미지정. 「all available knowledge up to the development of that breakthrough」 | CACM Opinion 「The Einstein Test: A Test of AI's Ability to Generate Transformative Science」(Benrimoh, Harel, Mikus, Stone, Rosenfeld, 2026-05, 69권 5호 49–50쪽, DOI 10.1145/3771100). 「we propose the Einstein Test, which assesses whether a given AI system can independently ‘rediscover’ known scientific breakthroughs」. 저자들은 Perrigo와 Wolf의 글을 보고 「어떤 수렴」이 있었다고 쓴다 | 학술 의견 논문 | 2쪽 전문 직접 확인 |

사용자 원문의 「1901 이전 data → 1904년 발견」은 지식 마감 연도로는 판본 b(1901)에 가깝고, 발견 연도로는 어느 판본과도 다르다. 판본 b의 대상은 1905년의 논문들이고, 판본 a의 대상은 1915년이다. 「1904」는 역사의 1905와 어긋난다. 조용히 맞추지 않고 기록한다. 입력 구간은 1901–1904이고 논문은 모두 1905년이므로 ET의 입력 stream은 1904-12-31까지 또는 구성요소별 T1 직전까지로 나눌 수 있다(표 4a).

### 5-2. 공식 제안(CACM)의 절차 골격과 우리 ET의 차이

| CACM 판본 | 우리 ET(MD-G) | 비고 |
|---|---|---|
| 전문가 위원회가 미공개 역사적 돌파구를 고른다 | 개발용 pilot과 봉인 주력을 나누고 사전 등록한다 | 비슷 |
| 돌파구 이전의 모든 지식을 담은 curated dataset을 주고 학습에도 쓸 수 있다 | W(≤T0)는 시간캡슐 기반이 맡고 T0 이후 지식은 지속학습 입력으로 넣는다 | 우리는 기반을 다시 학습하지 않는다 |
| 시험팀이 처음에 이끄는 안내를 주되 「guiding hand」가 되지 않게 한다고 경고한다 | 중립 probe와 누설도 채점으로 통제한다 | 같은 위험을 다룬다 |
| 시험팀이 「research assistant」가 되어 시스템이 요청한 실험 데이터를 당대에 가능했던 범위에서 준다 | 기본은 open-loop(인물 입력이 시스템 출력과 무관하게 고정), closed-loop는 OPEN | 대응 관계가 분명하다 |
| 시스템이 완료를 선언하거나 오답을 주장하거나 포기하면 끝나고 정답과 형식적으로 비교한다 | 시간순 입력과 checkpoint 중간 채점으로 발견 곡선을 그린다 | 우리는 한 번의 성패보다 어느 입력에서 나오는지를 본다 |
| 「We deliberately do not lay out any exact technical specifications for the test」 | docs/17이 운영 정의를 쓴다 | 공개된 절차가 아예 없는 것이 아니라 골격만 있고 기술 사양을 일부러 비운 상태다 |

### 5-3. 비판과 한계 (표 5b)

| 비판 | 출처 | 요지 | 확인 수준 |
|---|---|---|---|
| 조회표로도 통과한다 | Nova, Substack 「The Einstein Test」(2026-02-24) | 1911 이전 물리를 일반상대성으로 사상하는 조회표도 통과하므로 시험은 결과물만 보고 과정을 알 수 없다. 「It tests for the ability to produce intelligence's artifacts.」 | WebFetch 요약으로 확인(의견 글) |
| AGI가 아니라 초지능의 정의다 | Elon Musk의 반응으로 보도됨 | 한 매체(36Kr)만 전한다 | 단일 2차 출처, 1차 미확인 |
| 공개된 실행 절차가 없다 | 여러 보도 | 정확히는 위 CACM 의견이 골격을 제시하되 기술 사양은 비웠다. 「통과한 시스템의 공개 결과가 없다」는 서술은 Startup Fortune(2026-10-22) 등에 있다 | 보도 확인, CACM은 직접 확인 |
| LLM은 귀추적 도약(Jump)을 못 한다 | Google DeepMind의 Tom Zahavy 논문 「LLMs can't jump」로 소개됨 | 귀납과 연역은 되지만 등가 원리 같은 도약이 안 된다는 주장. 후속 논문(arXiv 2608.14397)의 초록이 이렇게 요약한다 | 후속 논문의 요약만 확인, Zahavy 원문 미확인 |
| 평가가 쉽게 설계되어 있다 | Hla 자신(2026-03) | 문제를 제시하고 단서를 주는 것이 발견 과정의 핵심인데 자기 평가는 그보다 훨씬 쉽다. 「Curating the information and posing the right questions is a critical part of the discovery process」 | 블로그 직접 확인 |
| 시간캡슐 모델의 무오염 주장이 약해진다 | Hla, 36Kr의 2차 보도 | SFT와 RL에 현대 LLM(Claude Sonnet 4 등)을 썼다. 저자도 무오염 주장이 약해진다고 쓴다 | 블로그 직접 확인, 36Kr는 2차 |
| 귀추적 원리 발명이 핵심이며 인공 세계와 역사 재구성 둘 다 필요하다 | Shalyt, Regev, Soljačić, Kaminer(arXiv 2607.27794, 2026-07) | 일반상대성은 귀납도 연역도 아니라 대칭 원리에서 후보 이론을 귀추로 세운 것이다. 숨은 법칙이 있는 인공 세계와 Hassabis의 1911 시험 같은 역사 재구성 과제를 함께 쓰자고 제안한다 | 논문 일부 직접 확인. 우리 ET-0(인공 세계)와 ET-3·4(역사)의 병행 설계를 지지하는 문헌 |
| 새 발견은 질문을 스스로 만드는 일까지 포함한다 | Thomas Wolf, 「The Einstein AI model」(2025) | 순종적인 학생이 아니라 혁명가가 필요하다. 후기에서 아직 모르는 최근 발견으로 시험하자고 제안한다 | WebFetch 요약으로 확인. 우리 ET-2(마감 이후 실제 사례)와 닮았다 |

### 5-4. 참고 영상이 다루는 프로젝트의 정체 (상태: needs-resolution)

- 확인한 것: 참고 영상(제목 「AI에게 1900년 이전의 과학 지식만 학습시켜본 결과」)은 공개 YouTube 영상으로 존재한다(공개 oEmbed 메타데이터로 제목 확인).
- 확인하지 못한 것: 영상의 설명, 자막, 본문. YouTube 페이지에서 설명을 추출하지 못했고, 제목으로 한 웹 검색에서도 영상 자체의 설명은 나오지 않았다.
- 제목과 부합하는 공개 사례: GPT-1900(Michael Hla, 2026-03, 1900년 이전 영어 약 22B token으로 처음부터 학습, 물리 모순 문제로 평가). 그러나 영상이 이를 다룬다는 근거는 확인하지 못했다. 다른 1900년 이전 모델이나 다른 실험일 가능성을 배제하지 못한다.
- 처리: needs-resolution으로 두고 추정으로 채우지 않는다. 이 조사 기록은 영상 내용을 근거로 어떤 주장도 하지 않는다. 확정하려면 영상의 설명란이나 자막을 사람이 확인해야 한다(DC-W2c-05).

## 6. 대상별 위험 (누수, 사료 공백, 저작권, 기반)

| ID | 누수 | 사료 공백 | 저작권·접근 | 기반과 실행 |
|---|---|---|---|---|
| TG-01 Einstein 1905 | (1) 기반: 표준 GPT-1900 d34에 일부 1900년 이후 자료가 있다는 카드 서술, 번역자 서문 누수 사례. 반대 방향으로 corpus 필터가 radiation·quantum 같은 모호한 용어의 동시 출현 문서를 제거해 1900년 이전 복사 이론 문헌이 빠졌을 수 있다(추정). (2) stream 구성: 전기·교과서·자서전 같은 후대 서술이 방대해 사후 편향이 가장 크다. (3) 번역: 현대 LLM 번역은 누수 경로. (4) instruct 판의 현대 LLM 영향 | 1905-03 ~ 06 연구기의 날짜 있는 과정 기록은 Habicht 편지 1통(날짜 논쟁)과 논문 자체뿐이고 나머지는 회고다. 독서 목록은 회고이고 출처가 약하다 | 편집판은 Hebrew University와 Princeton UP가 권리를 주장하고 Einstein Portal은 일부 무료와 구독이다. 원문 재배포 금지. 독일어를 영어 전용 기반이 읽지 못한다 | GPT-1900은 context 2048이고 저자가 대부분의 물리 과제 실패라고 평가. 도달 수준 상한을 낮게 보고해야 한다 |
| TG-02 Planck 1900 | 같은 기반의 누수. 같은 모델이 UV 파탄 문제를 단서와 함께 받은 평가가 있어 단서 없는 중립 probe가 필요하다 | Planck의 사고 과정 기록이 얇고 에너지 요소 회고는 후대 서술이다 | 저자와 논문 모두 소멸. 독일어 | 같음. pilot이므로 실행 크기는 host에 맞다 |
| TG-06 Chadwick 1932 | Talkie-1930이 마감 이후(1936 대통령, 제2차 세계대전 일부)를 안다고 저자가 보고했다. 중성자와 Joliot-Curie 결과의 유무를 probe로 먼저 잰다 | 실험 노트·서신 접근 미확인. Majorana의 미발표 결론은 stream이 없다 | 1931–32 문헌은 보호 기간 안이다. 구성한 stream은 출처 인용과 해시만 둔다. Joliot-Curie는 프랑스어 | 13B는 bf16 약 26GB라 host RAM에 맞지 않는다. 변환본의 충실도 미검증 |
| TG-03 일반상대성 1915 | 1913 포함 여부 미확정이라 1912–13 Einstein·Grossmann 논문이 corpus에 들어 있을 수 있다. 모델이 Einstein 이름은 알지만 물리 업적은 모른다고 답한 선별 예가 논문에 있으나 일반화할 수 없다. 우선권 논쟁(Hilbert)의 후대 서술이 방대하다 | 후보 중 가장 풍부하나 개별 문서는 확인하지 못했다 | 모델 카드 없음(라이선스 미명시). 편집판 권리는 TG-01과 같다. 독일어 | 7.24B 1913 모델의 텐서 미적분 능력이 낮을 가능성(C9=0, 추정) |
| TG-07 Turing 1936 | 간극 5년이고 Talkie의 1930년대 누수 보고가 있다. Gödel 1931 이후의 세계 지식을 stream으로 넣어야 한다 | 날짜 있는 과정 기록이 얇다. 학생기 독서와 강의는 전기 서술에 의존한다 | 1931–36 문헌은 보호 기간 안이다. Turing의 원 논문은 영국에서는 사망 후 70년이 지났을 수 있으나 확인하지 못했고 국가별로 다르다 | Talkie와 같다 |

묶음 공통 위험:

- 기반 모델의 능력이 발견 과제의 병목일 수 있다. 우리 과제 수행 능력은 측정하지 않았다(NOT RUN). 결과 등급 상한과 쓸 수 있는 문구는 docs/17이 정한다.
- 시간캡슐 모델의 가용성이 바뀐다. Ranke-4B 가중치의 공개 여부, TypewriterLM의 라이선스 명시, Talkie의 후속 GPT-3급 모델(보고서가 2026년 여름 공개를 희망한다고 썼으나 2026-11-18의 HF 목록에는 없다) 모두 미확정이다. 각 phase 시작 때 다시 조회한다(DC-W2c-07).
- 「마감」의 정의가 모델마다 다르므로 T0는 corpus의 year 열 감사로 확정한다.
- 표 안의 벤치 수치는 모두 타 논문이 잰 값이다. 우리가 재현하지 않았다.
- 조사 기준일은 2026-11-18이고 모든 수치와 공개 상태는 그날의 조회 결과다.

## 7. 정정 목록 (지시문 §1-6에서 고친 것)

| # | 지시문 §1-6의 서술 | 조사 결과 | 확인 수준 |
|---|---|---|---|
| 1 | TypewriterLM 「arXiv 2606.02991 『Pretraining Language Models on Historical Text』, 1913년 이전 영어 text, 약 7B」 | 같은 arXiv 번호의 v2(2026-10-02, v1은 2026-06-02, arXiv Comments에 EMNLP 2026 채택 표시) 제목은 「A Language Model from 1913: Pretraining on Historical Text」이고 파라미터는 7.24B다. 마감은 초록이 pre-1913, corpus가 1700-1913, 데이터 카드의 필터가 1913 이하라 포함 여부가 미확정이다. HF 저장소에는 모델 카드가 없어 라이선스가 미명시다. 논문에 없는 1938 변형(7B instruct, 3B 영어·독일어 base)이 HF에 있다 | 논문 v2 직접 확인 |
| 2 | Ranke-4B 「지식 마감 1913 / 1929 / 1933 / 1939 / 1946」 | 마감과 Qwen3 구조는 맞다. 그러나 2026-11-18 조회에서 두 HF 조직의 공개 모델은 0개이고 사전 공개 노트(2025-12)와 DPO 샘플 dataset 2개만 확인했다. 가중치 공개는 미확인이다 | README·노트·HF API 직접 확인 |
| 3 | GPT-1900 「광양자·특수상대성 재발견은 대부분 실패로 보고됐다」 | 저자는 단서가 붙은 모순 문제에서 단편적 직관이 나온다고 보고하고 전체로는 물리 과제의 대부분에서 실패한다고 평가했다. 평가는 저자가 스스로 인상 기반이라고 밝힌 것이라 재발견 실패나 성공을 정량으로 판정한 결과가 아니다. 크기는 1.68B(D26)와 3.29B(D34), context는 2048이다. 1905 변형 외에 1964 변형도 있다. SFT뿐 아니라 RL judge에도 현대 LLM이 쓰였다 | 블로그·카드 직접 확인 |
| 4 | Talkie-1930 「1931년 이전 text 약 2,600억 token, 13B, base판과 instruction-tuned판, Apache-2.0으로 보도됨」 | 모두 확인했다. 마감은 1930-12-31이고 Apache-2.0은 HF 카드와 GitHub에서 확인했다. 저자가 마감 이후 누수(Roosevelt 임기, New Deal, 제2차 세계대전 일부)를 직접 보고했다 | 보고서·카드 직접 확인 |
| 5 | TimeCapsuleLLM 「1800–1875 London text, 소형」 | v0 16M부터 v2 1.22B까지 여러 크기이고 v3mini 500M(영어 1800–1875)도 있다. v2는 H100 117시간 약 341달러에 학습됐다고 저자가 적었다 | README·카드 직접 확인 |
| 6 | Einstein test 「Hassabis의 제안으로 보도됨」, 판본 b 「WSJ 기사를 인용한 보도」 | 판본 a(1911 → 1915)는 2차 보도 인용으로 확인했다. 더 이른 선행 서술이 있다(TIME 2025-04-15, 연도 없음). 판본 b(1901 → 1905)는 기자 서술로만 확인했다. digit.in(2026-05, Google I/O 기간 Axios 인터뷰 절)과 aiweekly.co(2026-10, WSJ 기사 요약) 두 곳이다. WSJ와 Axios 원문, Hassabis가 그 연도를 직접 말했는지는 확인하지 못했다. 판본 b는 WSJ 인용 보도보다 이른 2026-05 보도에도 있다. 공식 학술 제안(CACM 2026-05)이 따로 있다 | 표 5a 참조 |
| 7 | 비판 「공개된 실행 절차가 없다는 평」 | CACM 의견 글이 절차 골격을 내놓았다. 다만 기술 사양은 일부러 비워 두었다. 「통과한 시스템의 공개 결과가 없다」는 서술은 맞는 것으로 보인다 | CACM 직접 확인 |
| 8 | 비판 「AGI가 아니라 초지능의 정의라는 지적」 | Musk의 반응으로 한 매체(36Kr)만 전한다. 1차 확인 못함 | 단일 2차 출처 |
| 9 | 참고 영상 | 영상의 존재와 제목은 확인했다. 내용은 확인하지 못했다. needs-resolution 유지 | §5-4 |
| 10 | 함의 「공개 모델로 역사 ET를 일찍 시작할 수 있다」 | 부분 확인. 마감이 맞는 가용 모델이 있는 대상은 5개(TG-01, 02, 06, 07, 조건부로 03)이고 기반 모델 능력이 병목이다 | §2–§3 |

## 8. 사용자 결정 후보 (가칭. 최종 번호는 통합 담당이 붙인다)

| 가칭 | 결정 | 선택지 | 추천 | 비용 발생 | 결정자 |
|---|---|---|---|---|---|
| DC-W2c-01 | ET 대상 묶음 | (a) 주력 Einstein 1905, pilot Planck 1900와 Chadwick 1932, 대안 일반상대성 1915와 Turing 1936. (b) 주력을 일반상대성 1915로 교체. (c) 주력 2개(Einstein 1905와 Turing 1936) | (a). 마감이 맞는 가용 모델이 있는 5개이고 기반별 pilot·봉인 쌍이 된다 | 없음(후속 실행 비용은 docs/15) | 사용자 |
| DC-W2c-02 | Einstein 주력의 기반 checkpoint와 T0 | (a) pre-1900-only 체인의 checkpoint, T0 1900-01-01. (b) 표준 d34. (c) GPT-1905, T0 1905-01-01을 비교 기반으로 병행 | (a)를 기본, (c)를 비교로 병행. (b)는 누수 감사 뒤에 대조로만 | 없음 | 사용자 |
| DC-W2c-03 | TypewriterLM의 라이선스 확인과 사용 | (a) 확인 전에는 일반상대성 대안을 보류. (b) 저자에게 문의(외부 연락이라 이번 범위 밖) | (a) | 없음 | 사용자 |
| DC-W2c-04 | 영어 전용 기반에서 독일어 사료의 처리 | (a) 영어 동시대 자료와 당대 영어 요약만 쓴다. (b) 사람이 한 소멸 저작권의 번역만 허용. (c) 현대 LLM 번역을 시스템 밖 구성 보조로 쓰고 입력 tier C와 누설도 채점을 붙인다 | (a)와 (b) | 없음 | 사용자 |
| DC-W2c-05 | 참고 영상의 정체 | (a) 사람이 설명란·자막을 확인해 알려준다. (b) needs-resolution 유지 | (b) | 없음 | 사용자 |
| DC-W2c-06 | 사료 접근 비용 | (a) 무료 범위로 TG-02·TG-01의 1900–1904 논문과 서신을 먼저 확인하고 구독은 P5 시작 때 결정. (b) 지금 구독 | (a) | 있음(Einstein Portal 구독과 1931년 이후 문헌 접근, 규모 미확인) | 사용자 |
| DC-W2c-07 | 시간캡슐 모델 공개 상태의 재점검 주기 | (a) phase 시작 때마다 1회. (b) 하지 않는다 | (a) | 없음 | 마스터 |

새 평가 family 후보(F-NEW-W2c-x)와 대응하는 W2c 항목은 없다.

## 부록 A. 색인

### 소유 정의 위치

| 소유 정의(지시문 §3-2) | 위치 |
|---|---|
| Einstein test 출처 | §5 「Einstein test」 제안의 출처, 판본, 비판, 참고 영상 (표 5a, 5b와 §5-2, §5-4) |
| 시간캡슐 모델 현황 표 | §1 시간캡슐(vintage·historical) 언어모델 현황 (표 1a–1c, §1-1, §1-2) |
| 대상 후보 매트릭스와 추천 묶음 | §2 대상 후보 매트릭스와 MD-H 기준표 점수 (표 2a, 2b), §3 추천 묶음과 근거 (표 3a, 3b) |
| 대상별 사료·데이터 계획 | §4 추천 묶음의 데이터 계획 (§4-1 ~ §4-5, 표 4a) |

### 이 초안이 정의한 ID

| ID | 뜻 |
|---|---|
| TG-01 ~ TG-16 | ET 대상 후보 ID(가칭 성격. 최종 형식은 통합 담당이 정한다) |
| C1 ~ C9, G1, G2 | MD-H 기준표의 점수 칸 8개와 추가 1개, 관문 2개(§2-1) |
| 표 1a–1c, 2a–2b, 3a–3b, 4a, 5a–5b | 이 초안의 표 번호 |

### 남의 정의를 가리킨 곳

| 가리킨 것 | 소유 |
|---|---|
| MD-G(ET 운영 정의의 원칙), MD-H(대상 추천), MD-I(누수 통제) | 지시문 §2 |
| ET 운영 정의, stream 항목 schema, 입력 tier, rubric, 단별 상한과 쓸 수 있는 문구, 분리 규칙 | docs/17 |
| frozen LLM 후보 표와 실행 위치 규칙, ET-3p의 설계 | docs/18 |
| 비용, GPU-시간, 시간캡슐 기반 확보 3안 | docs/15 |

### 가칭 목록

| 가칭 | 요약 |
|---|---|
| DC-W2c-01 | ET 대상 묶음(추천 (a)) |
| DC-W2c-02 | Einstein 주력의 기반 checkpoint와 T0 |
| DC-W2c-03 | TypewriterLM 라이선스 확인과 사용 |
| DC-W2c-04 | 영어 전용 기반에서 독일어 사료의 처리 |
| DC-W2c-05 | 참고 영상의 정체 확인 방식 |
| DC-W2c-06 | 사료 접근 비용(구독) 승인 시점 |
| DC-W2c-07 | 시간캡슐 모델 공개 상태의 재점검 주기 |
| NEW-W2c-01 ~ 16 | 부록 B의 새 참고문헌 16행 |
| F-NEW-W2c-* | 없음 |

## 부록 B. 새 참고문헌

| id | title | category | date_note | url | code_url | status | note |
|---|---|---|---|---|---|---|---|
| S146 (가칭 NEW-W2c-01) | Machina Mirabilis (GPT-1900: 1900년 이전 text만으로 학습한 LLM으로 양자역학·상대성 재발견을 시험) | evaluation | 2026-03; Michael Hla 블로그 | https://michaelhla.com/blog/machina-mirabilis.html | https://github.com/michaelhla/gpt1900 | metadata-checked | 블로그 본문과 부록 전체와 HF 카드를 직접 읽음. 결과 평가는 저자가 인상 기반이라고 밝힘. 현대 LLM을 SFT·RL에 사용. 주장과 수치를 원문과 쪽 단위로 대조한 수준은 아님 |
| A69 (가칭 NEW-W2c-02) | GPT-1900 / GPT-1905 / GPT-1964 모델·corpus 카드(Hugging Face mhla) | code | 2026-02~04; MIT 표기 | https://huggingface.co/mhla | https://huggingface.co/datasets/mhla/pre1900-corpus | metadata-checked | 카드 7종과 corpus 카드, 공개 API 메타데이터를 읽음. 가중치는 내려받지 않음 |
| S147 (가칭 NEW-W2c-03) | A Language Model from 1913: Pretraining on Historical Text (TypewriterLM) | evaluation | arXiv 2606.02991, v1 2026-06-02, v2 2026-10-02, EMNLP 2026 채택 표시(arXiv Comments). 초기 판 제목은 alphaXiv 표제 기준 Pretraining Language Models on Historical Text | https://arxiv.org/abs/2606.02991 | https://huggingface.co/typewriter-ai | metadata-checked | v2의 1–6, 11–12, 15쪽과 HF 메타데이터를 읽음. 모델 카드가 없어 라이선스 미명시. 전체 본문을 대조한 수준은 아님 |
| S148 (가칭 NEW-W2c-04) | Introducing talkie: a 13B vintage language model from 1930 | evaluation | 2026-04; Levine, Duvenaud, Radford | https://talkie-lm.com/ | https://github.com/talkie-lm/talkie | metadata-checked | 보고서 전문과 HF 카드와 GitHub README를 읽음. Apache-2.0. 마감 이후 누수를 저자가 보고 |
| S149 (가칭 NEW-W2c-05) | History LLMs / Ranke-4B (시간 고정 역사 모델 정보 허브) | evaluation | 2025-12 사전 공개 노트; Göttlich, Loibner, Jiang, Voth | https://github.com/DGoettlich/history-llms | | metadata-checked | README와 사전 공개 노트 앞부분을 읽음. 2026-11-18 조회에서 HF 공개 모델 0개, 가중치 공개 미확인 |
| A70 (가칭 NEW-W2c-06) | TimeCapsuleLLM (런던 1800–1875 text로 처음부터 학습) | code | 2025–2026; Grigorian, Yaghoobian | https://github.com/haykgrigo3/TimeCapsuleLLM | https://huggingface.co/collections/haykgrigorian/timecapsulellm-1800-1875-london | metadata-checked | README 앞부분과 v2 카드를 읽음. MIT(v3mini는 Apache-2.0) |
| S150 (가칭 NEW-W2c-07) | The Einstein Test: A Test of AI's Ability to Generate Transformative Science | evaluation | CACM 69권 5호 49–50쪽, 2026-05; Benrimoh, Harel, Mikus, Stone, Rosenfeld | https://doi.org/10.1145/3771100 | | metadata-checked | 저자 사본의 2쪽 전문을 읽음. DOI는 사본에 인쇄된 값. 절차 골격을 제시하고 기술 사양은 의도적으로 비움 |
| S151 (가칭 NEW-W2c-08) | Demis Hassabis Is Preparing for AI's Endgame (TIME 인터뷰 기사) | evaluation | 2025-04-15; Billy Perrigo | https://time.com/7277608/demis-hassabis-interview-time100-2025/ | | official-search-checked | WebFetch 요약으로 해당 문장만 확인. 원문 전체 열람 못함. 기자의 서술이고 Hassabis의 직접 인용이 아님 |
| S152 (가칭 NEW-W2c-09) | Can AI Follow In Einstein's Footsteps? | evaluation | arXiv 2607.27794 v1, 2026-07-30; Shalyt, Regev, Soljačić, Kaminer | https://arxiv.org/abs/2607.27794 | | metadata-checked | 1, 3, 6, 11–12쪽과 참고문헌을 읽음. Hassabis의 1911 시험과 Machina Mirabilis를 언급 |
| S153 (가칭 NEW-W2c-10) | The Einstein Test (Substack 비판 글) | evaluation | 2026-02-24; Nova | https://novawritesforall.substack.com/p/the-einstein-test | | official-search-checked | WebFetch 요약으로 확인. 의견 글. 조회표 비판 |
| S154 (가칭 NEW-W2c-11) | A Test Of AGI Could Be If A System Trained Till 1911 Data Could Discover General Relativity (OfficeChai) | evaluation | 2026-02-20 | https://officechai.com/ai/a-test-of-agi-could-be-if-a-system-trained-till-1911-data-could-discover-general-relativity-google-deepmind-ceo-demis-hassabis/ | | official-search-checked | WebFetch 요약으로 확인. 판본 a의 2차 인용 |
| S155 (가칭 NEW-W2c-12) | The Einstein AI model (Thomas Wolf) | evaluation | 2025; 게시일 미확인 | https://thomwolf.io/blog/scientific-ai.html | | official-search-checked | WebFetch 요약으로 확인. 후기에 아직 모르는 최근 발견으로 시험하자는 제안 |
| S156 (가칭 NEW-W2c-13) | LLMs can't jump (Tom Zahavy) | evaluation | 2026; 2차 출처만 | | | needs-resolution | 원문을 찾지 못함. arXiv 2608.14397 초록의 요약과 보도로만 확인. 제목·식별자를 만들어 채우지 않음 |
| S157 (가칭 NEW-W2c-14) | WSJ Magazine 인물 기사(Hassabis, Ben Cohen) | evaluation | 2026-10-21 | | | needs-resolution | 원문 접근 불가. aiweekly.co 요약으로만 확인. 판본 b(1901 → 1905)를 인용한 보도의 출처 |
| S158 (가칭 NEW-W2c-15) | Google DeepMind CEO Demis Hassabis says we're close to AGI (Axios 기사) | evaluation | 2026-05-26 | https://www.axios.com/2026/05/26/deepmind-ceo-demis-hassabis | | official-search-checked | 검색 결과로 존재만 확인. 열람 실패(403)라 Einstein test 서술이 있는지 미확인 |
| S159 (가칭 NEW-W2c-16) | Google DeepMind CEO says AGI may arrive by 2030, calls current AI agents a practice run (digit.in) | evaluation | 2026-05-28 갱신; Siddharth Chauhan | https://www.digit.in/news/general/google-deepmind-ceo-says-agi-may-arrive-by-2030-calls-current-ai-agents-a-practice-run.html | | official-search-checked | WebFetch 요약으로 확인. 판본 b(1901 → 1905)를 기자 서술로 적고 Hassabis 직접 인용은 「I think today systems clearly can't」 |

## 부록 C. 조사 출처

접근일은 모두 2026-11-18이다. 확인 수준은 `직접`(1차 문서를 직접 읽음), `부분`(일부만 읽음), `요약`(WebFetch 요약이나 검색 요약만), `실패`(열지 못함)다.

| URL | 읽은 범위 | 확인 수준 |
|---|---|---|
| https://michaelhla.com/blog/machina-mirabilis.html | 블로그 본문과 부록 전체 | 직접 |
| https://huggingface.co/mhla (모델 카드 7종, dataset 카드, 공개 API 목록) | 카드 본문, 모델 49개와 dataset 10개의 메타데이터 | 직접 |
| https://arxiv.org/abs/2606.02991 | v2의 1–6, 11–12, 15쪽(alphaXiv), 초기 판의 AI 요약 보고서 | 부분 |
| https://huggingface.co/typewriter-ai , https://typewriter.chat/ | 모델 목록, config 2종, 데이터 카드, 프로젝트 페이지, HF 토론 목록 | 직접(모델 카드는 없음) |
| https://talkie-lm.com/ , https://huggingface.co/talkie-lm , https://github.com/talkie-lm/talkie | 보고서 전문, base 카드, 모델 목록, README 앞부분, 제3자 변환본 검색 | 직접 |
| https://github.com/DGoettlich/history-llms | README, 사전 공개 노트 앞부분, 커밋 목록, 두 HF 조직의 API | 부분 |
| https://github.com/haykgrigo3/TimeCapsuleLLM , https://huggingface.co/haykgrigorian | README 앞부분, v2 카드, 모델 목록 | 부분 |
| https://github.com/entanglr/awesome-vintage-llms | README 앞 9천 자 | 부분(2차 목록) |
| https://doi.org/10.1145/3771100 (저자 사본 PDF) | 2쪽 전문 | 직접 |
| https://time.com/7277608/demis-hassabis-interview-time100-2025/ | 한 문장과 서지 | 요약(서버가 직접 요청을 막음) |
| https://officechai.com/ai/a-test-of-agi-could-be-if-a-system-trained-till-1911-data-could-discover-general-relativity-google-deepmind-ceo-demis-hassabis/ , https://zaruko.com/insights/the-einstein-test | 판본 a의 인용과 날짜 | 요약 |
| https://aiweekly.co/alerts/hassabis-trims-agi-window-to-two-to-three-years-in-wsj-profile , https://startupfortune.com/demis-hassabis-now-says-agi-could-arrive-in-just-two-to-three-years/ , https://www.trendingtopics.eu/hassabis-agi-two-three-years/ , https://www.digit.in/news/general/google-deepmind-ceo-says-agi-may-arrive-by-2030-calls-current-ai-agents-a-practice-run.html | 판본 b와 WSJ 기사 서지 확인 | 요약 |
| https://www.axios.com/2026/05/26/deepmind-ceo-demis-hassabis | 접속하지 못함(403) | 실패 |
| https://novawritesforall.substack.com/p/the-einstein-test , https://eu.36kr.com/en/p/3990930500221697 , https://thomwolf.io/blog/scientific-ai.html | 비판과 관련 제안 | 요약 |
| https://arxiv.org/abs/2607.27794 | 1, 3, 6, 11–12쪽과 참고문헌 | 부분 |
| https://arxiv.org/abs/2608.14397 | 검색 결과의 초록 요약만 | 요약 |
| https://singjupost.com/demis-hassabis-on-agi-advice-for-indian-engineers-ai-in-gaming-more-transcript/ | 접속하지 못함 | 실패 |
| https://press.princeton.edu/node/71269 , https://einsteinpapers.press.princeton.edu/ | Einstein Portal 공지와 사이트 소개(권리 서술은 두 기관 페이지를 인용한 검색 요약으로만 확인) | 요약 |
| https://huggingface.co/datasets/institutional/institutional-books-1.0 | 로그인이 필요해 열지 못함 | 실패 |
| https://en.wikipedia.org/wiki/Annus_mirabilis_papers , https://en.wikipedia.org/wiki/Olympia_Academy , https://en.wikipedia.org/wiki/James_Chadwick , https://en.wikipedia.org/wiki/Planck%27s_law , https://en.wikipedia.org/wiki/Computable_number , https://en.wikipedia.org/wiki/Discovery_of_the_neutron | 날짜·서지·독서 목록(2차, WebFetch 요약. Planck 문서는 앞 10만 자) | 요약(2차) |
| https://arxiv.org/abs/2605.04192 | 검색 요약(Habicht 편지 날짜 논쟁) | 요약 |
| https://www.theiet.org/membership/library-and-archives/the-iet-archives/iet-history/history-of-science-abstracts-and-inspec/inspec-history-1898-1914 | 검색 요약(Science Abstracts 연혁) | 요약 |
| https://www.youtube.com/watch?v=rOlniH_UJ5A (참고 영상) | 공개 oEmbed 메타데이터의 제목만. 설명·자막은 열지 못함 | 부분(내용 미확인) |

