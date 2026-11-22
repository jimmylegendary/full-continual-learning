# 2026-11-23 Sleep-time 주간 조사 → Melete 직접 관련 선별 기록

**ARCHIVE / discussion-import + selected LITERATURE(official abstract verified); PROPOSAL / OPEN / NOT RUN.** 독립 자동화 `Sleep-time Compute 주간 동향`의 2026-11-23 완료 결과(run `ba80ff6c-c93c-8332-b32f-968bbee0c1c6`, 조사 11/16–22)를 직접 확인했다. 이번 파일은 **증거 보존·기억 압축/재인출·학습 비용·self-evolution 판정**과 연결된 항목만 선별한 cross-project note다. 전체 13편 등의 자동화 본문을 무조건 재배포하지 않는다. 별도 HAT/HBF 하드웨어 주제(예: LaFlash)는 이 neural schema 문서에 옮기지 않는다. [확인 범위와 원문 목록](../references/2026-11-23-sbl-sleep-sources.md).

## 1. 11/17–19 최초 공개 (공식 arXiv 초록 독립 확인)

| 논문 / 날짜 | 원문에서 확인한 기여와 저자 보고 | FCL 적용 질문 (PROPOSAL) |
|---|---|---|
| [MemFolder](https://arxiv.org/abs/2611.26427) · **11/19** · Liu et al. | 외부 agent 기억의 record 수와 회수되는 text 길이를 나눠 줄이는 RecordFolder/ContextFolder. 원자료에서 핵심 사실이 복구되지 않으면 다시 압축을 수정. 저자 초록: Mem0에서 records 50% 감소 시 3개 text benchmark 평균 성능의 **99.0% 유지** | source evidence를 지우지 않은 파생 기억의 압축 후보 검증, 복구 테스트·미래 질의 비용 |
| [GrepMem](https://arxiv.org/abs/2611.25123) · **11/18** · Yang et al. | append-only 원문 로그 + regex 검색. 저자 초록: ContextBench **95–97%** vs 비교 lossy 방법 최대 **21%**; Qwen3.5-9B RL 사용. Lossless external episodic history이지 neural schema 지속학습 아님 | 압축/CRUD의 **강한 원본 보존 baseline**. 검증 가능한 원본과 파생 schema를 구분 |
| [The Resolution Hypothesis](https://arxiv.org/abs/2611.23068) · **11/17** · Zeng et al. | 7 evolutionary methods×6 models, **10M+ LLM calls** 저자 실험. 노이즈 큰 평가가 유용 후보와 악성 후보를 구별하지 못하면 자동 진화가 잘못된 선택을 누적 | [self-evolution 승격 기준](../docs/10-evolution-policy.md)의 paired 평가, 반복 seed, 보호 과제 회귀, independent confirmation / rollback |
| [Replay, Don't Resample](https://arxiv.org/abs/2611.24059) · **11/18** · Yue et al. | 세 RL 전문 정책의 기존 학습 rollout·확률·보상 순서를 재활용해 통합, 재샘플링 없이 student 학습. 저자 초록: consolidation compute는 전문가 원학습의 약 **1/7**. 별도 RL policy training 연구 | 새 외부 관측 수와 재처리/gradient/teacher 비용 구분, trajectory order vs volume 및 총 C* |
| [How Much Should an Agent Remember?](https://arxiv.org/abs/2611.26361) · **11/19** · Jayaram et al. | agent trajectory→lessons→guidelines로 통합. 모델별 적절한 기억량이 다르고 provenance 누락·빈도 높은 guideline 실패 사례를 보고. 저자 초록: DeepSeek-V3.2 191개 guideline 전부로 task +9.5pp; gpt-oss-120b는 약 29개 선별이 199개 전체보다 좋음. **IAAI 2027 oral 채택 표기(원문 Comments)** | activation/read budget을 모델·질의 조건에 맞추되 support-count를 correctness나 novelty와 동일시 금지 |
| [SkillPlumber](https://arxiv.org/abs/2611.25429) · **11/19** · Tan et al. | 자연어 procedural skill instruction을 followed/not-followed/not-covered로 구분해 수정. 저자 초록: 강한 기준보다 8.7–14.0pp 성공률 상승 | 실패가 잘못된 schema인지 read/activation 실패인지 국소 분리; neural schema 성능으로 오해 금지 |

**경계:** MemFolder/GrepMem/IBM/SkillPlumber는 **외부 언어 기억/agent workflow**, Resolution은 진화 평가, MRPD는 **RL distillation**이다. 어느 논문도 Melete의 continuous latent neural schema 형성·변경·세션 간 망각 없는 학습을 직접 입증하지 않는다. 수치는 원저자의 특정 비교·벤치마크 결과이지 본 저장소의 측정이 아니다.

## 2. FCL에 연결할 검증 가설 (PROPOSAL / OPEN)

1. **Evidence-preserving memory promotion**: append-only 근거 ledger를 authority로 보존하고, 파생 text summary·neural expert·retrieval index는 versioned 후보로 관리. 이를 삭제(Delete)와 offload(Recall 가능한 보관)로 혼동하지 않는다.
2. **검증된 Sleep commit**: 원본 재구성/held-out 기능 보호/정책 전이/동등한 N·C·S에서의 미래 정확도와 총비용을 확인한 후보만 승격. 평가 잡음이 커 순위를 결정할 수 없으면 **INCONCLUSIVE**, 이전 상태 유지 및 rollback 가능 상태 보존.
3. **Read/Activate 분리**: 답변 시 retrieval과 학습/재결정화에 사용하는 source read의 목적과 비용을 별도 장부로 추적. 너무 많은 guideline을 주는 것과 부족한 정보로 대답하는 것 모두 실패일 수 있다.
4. **Reprocessing isn't new information**: MRPD·Sleep·replay는 새 외부 고유 관측을 증가시키지 않지만, 훈련 step/teacher/forward·backward/스토리지 비용을 총계산 장부에 포함한다. Ali A/B/C의 같은 입력·같은 목표 품질 비교에 연결한다.

이것은 기존 [evaluation](../docs/08-evaluation.md), [lifecycle](../docs/14-schema-lifecycle-crud-and-joint-paper.md), [evolution policy](../docs/10-evolution-policy.md)의 가설을 보완하는 제안일 뿐 이미 구현됐거나 GPU 검증을 통과한 결과가 아니다.

## 3. 읽은 범위와 한계

11/23 별도 주간 자동화의 완료 보고 전체(표시 가능한 텍스트)를 참고했고, 위 6편은 arXiv의 **초록·메타데이터**를 별도로 대조했다. PDF/부록 full-text audit, 코드 실행, model/agent/GPU 실행, 최적화 성능의 독립 재현, HBF HW 시뮬레이션은 **NOT RUN**. 다른 연구 저장소의 파일을 복제하거나 변경하지 않았다.
