# 2026-11-18 요청 동기화 출처와 범위

이 문서는 2026-11-18에 사용자가 입력한 요청의 원문과 이번 작업의 범위를 보존하는 기록이다. 형식은 [2026-11-17-discussion.md](/home/jimmy/repos/full-continual-learning/sources/sync/2026-11-17-discussion.md)와 [SYNC_POLICY.md](/home/jimmy/repos/full-continual-learning/SYNC_POLICY.md)를 따른다. 아래 블록은 문구를 그대로 옮겼다(오탈자로 보이는 「증면」도 고치지 않았다). 다른 세션의 모든 메시지를 export한 것이 아니다.

## 사용자 원문: 이상 청사진·비모수 POC·단계별 구현과 논문·runcrate 실험 계획·아인슈타인 테스트

```text
이상적인 모습 기준 청사진을 작성해보고 어떤 feature가 포함되고 어떤 flow로 동작할지 설계해
그리고 이걸 달성하기 위한 POC로 검증은 어떤것들 진행할지(모델 학습없이 non parameter 기반의 무언가로 POC검증을 먼저 해보자), 그뒤 단계별 구현(근데 모든 단계는 각 단계가 완전하게 종료되어 독립적으로도 의미를 가지고 돌릴 수 있는 상태여야함)계획과 각 단계별(최초 poc포함)논문을 쓴다면 어떤 주장을 할것이고 논문 제목, 초록을 어떻게 할지 그것도 써서 준비해둬
당연히 runcrate사용한 실험계획(필요한 단계에서)도 포함되어야함
당연히 논문이니까 실험환경이나 객관적 증면, 비교대조, test data어떻게 할지, 학습 data어떻게 할지 계획이 포함되어야 함
최종적으로는 아인슈타인 테스트 통과를 목표로 함. 
- 근데 진짜 1901년 data만 주고 아무 입력 없이 1904년 발견을 도출하는게 아니라 우리 solution 기준이라면 1901~1904사이에 아인슈타인이라면 했을법한 입력 set들을 기반으로 진행하고, 1901 이전 data에 대해서도 아인슈타인이 했을법한 입력 data를 만들어서 준비해야함. 그리고 어떤 data까지 넣었을 때 유의미한 발견들이 나오는지 관찰하는 것임
- 그리고 아인슈타인 테스트라고 해서 아인슈타인만 대상으로 할 필요는 없음(data구하기 어려우니). 근본 목적은 창발적이고 직관에 매우 크게 의존하는 인류 역사상 큰 발견/발명을 AI가 할수 있는지를 보는 테스트라서 2026 이전 어느시점을 기준으로 잡아도 괜찮음. 단지 그 시점에 어떤 사람의 발견/발명을 대상으로 할지, 어디서 과학적 발견, 동료의 연구등을포함한 모든 연구 결과 data를 어느시점까지만 주고 그 이후 특정 인물의 연구, 사고방식 data를 줄지 이런것들을 잘 결정해서 보면 되는 것임

이렇게 고려해서 해봐
```

출처: Claude Code 세션에서 사용자가 입력하고 마스터 agent가 작업 지시에 전달한 원문이다. 전체 대화 export가 아니다. ChatGPT의 hourly 「FCL 연구 기록 동기화」 작업이 읽을 수 있는 대화가 아니므로, 이 내용은 이번 branch 커밋으로만 저장소에 들어온다. 발화 시각은 확인하지 못했고 날짜(2026-11-18)는 작업 지시에 적힌 값이다.

원문은 요청 7개로 나뉜다. 사용자 진술 목록의 번호는 U-T15([user-statements.md](/home/jimmy/repos/full-continual-learning/sources/user-statements.md))다.

| 요청 | 사용자가 말한 것 | 처리 |
|---|---|---|
| 청사진 | 이상적인 모습 기준 청사진을 쓰고 어떤 feature가 들어가고 어떤 flow로 동작할지 설계 | 이상 청사진 [16-ideal-blueprint.md](/home/jimmy/repos/full-continual-learning/docs/16-ideal-blueprint.md): feature 그룹, flow FL-1~FL-6, feature × phase 해상도 표 |
| POC 검증 | 달성을 위한 POC 검증을 먼저 하되 모델 학습 없이 non parameter 기반의 무언가로 | 비모수 POC 설계·검증 계획 [18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md)와 로드맵의 P0(NP) |
| 단계별 구현 | 모든 단계가 완전히 종료되어 독립적으로도 의미를 갖고 돌아가는 상태여야 함 | 로드맵 [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md)의 P0(NP)–P6(ET) 개정. 점진적 해상도 규칙과 같은 방향의 요구다 |
| 단계별 논문 | 최초 POC를 포함해 각 단계 논문의 주장·제목·초록 | 논문 계획 [19-paper-plan.md](/home/jimmy/repos/full-continual-learning/docs/19-paper-plan.md) |
| runcrate 실험 계획 | 필요한 단계에서 runcrate를 쓰는 실험 계획 | 계산 계획 [15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md)의 2026-11-18 갱신(ESTIMATE / NOT RUN) |
| 실험 설계 | 실험환경, 객관적 증명, 비교대조, test data, 학습 data 계획 | 논문별 실험 설계 표([19-paper-plan.md](/home/jimmy/repos/full-continual-learning/docs/19-paper-plan.md))와 P0 검증·실행 행렬([18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md)) |
| 아인슈타인 테스트 | 최종 목표. 입력 set은 그 인물이 했을 법한 것으로 만들고, 어떤 data까지 넣을 때 발견이 나오는지 관찰. 대상은 아인슈타인에 한정하지 않고 시점도 2026 이전에서 고른다 | 시험 설계 [17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md)와 조사 기록의 대상 후보 조사 |

## 해석과 한계

- **날짜와 역사 사실:** 원문은 「1901년 data만 주고 아무 입력 없이 1904년 발견을 도출하는게 아니라」 「1901~1904사이에 아인슈타인이라면 했을법한 입력 set들을 기반으로 진행」한다고 적었다. 이 「1901 → 1904」는 사용자가 든 예이고, 역사 속 아인슈타인의 논문 해(1905)나 보도된 시험 제안의 연도와 같다고 확인된 것이 아니다. 문서는 이 차이를 조용히 맞추지 않고 그대로 기록한다. 시험 제안의 출처와 판본 차이는 [17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md)와 [2026-11-18-blueprint-et-design.md](/home/jimmy/repos/full-continual-learning/research/2026-11-18-blueprint-et-design.md)에 있다.
- **「증면」:** 문맥상 「증명」으로 읽히지만 사용자가 그렇게 말했다는 기록이 없으므로 원문을 고치지 않았다. 문서는 「객관적 증명」으로 읽어 쓴다(해석, PROPOSAL).
- **「입력」의 뜻(OPEN):** 「아인슈타인이라면 했을 법한 입력」이 그 인물이 겪은 경험의 stream을 학습자가 받는 것인지, 그 인물과 대화하는 동반 AI인지는 사용자가 정하지 않았다. 문서는 기본 선택과 대안을 적고 사용자 확인 대기로 둔다.
- **「non parameter」의 범위(OPEN):** 사용자는 모델 학습 없이 non parameter 기반의 무언가로 POC를 먼저 하자고 했다. 문서는 gradient 학습이 없는 구성을 P0(NP)로 두었고, 닫힌 꼴 선형 expert(파라미터는 있으나 backprop은 없음)를 비모수에 넣을지는 사용자 결정 후보다.
- **「P1은 MVP」와의 관계(OPEN):** 사용자의 기존 영구 규칙은 P1을 MVP로 둔다. 이번 요청의 「POC 먼저, 그 뒤 단계별 구현」에 맞춰 P0(NP)가 뼈대와 전체 여정을 먼저 세우고 P1이 첫 학습 해상도가 되도록 읽었다. 이 해석은 사용자 확인 항목이다.
- **대상 선택:** 사용자는 아인슈타인만 대상일 필요가 없고 2026 이전 어느 시점이든 괜찮다고 했다. 그 안에서 어떤 인물·발견·T0를 쓸지는 사용자가 정하지 않았다. 문서의 추천은 PROPOSAL이며 결정은 사용자 몫이다.
- **계획과 실행의 구분:** 「설계해」, 「써서 준비해둬」, 「계획」은 문서 요청이다. 구현, 모델 학습, 클라우드 인스턴스 생성, 비용 발생, 모델·corpus 다운로드는 사용자가 승인한 것이 아니다. 문서의 수치는 ESTIMATE이고 실행은 NOT RUN이다.
- **결정은 사용자 몫:** 문서가 낸 추천은 PROPOSAL이다. [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md) §10의 D-01·D-04·D-05·D-12 등 기존 결정 대기는 이번 요청으로 결정되지 않았다.

## 대응 문서

- [16-ideal-blueprint.md](/home/jimmy/repos/full-continual-learning/docs/16-ideal-blueprint.md): 이상 청사진.
- [17-einstein-test.md](/home/jimmy/repos/full-continual-learning/docs/17-einstein-test.md): 경험 조건부 발견 시험(아인슈타인 테스트)의 운영 정의와 절차.
- [18-poc-nonparametric.md](/home/jimmy/repos/full-continual-learning/docs/18-poc-nonparametric.md): 비모수 POC(P0) 설계와 검증 계획.
- [19-paper-plan.md](/home/jimmy/repos/full-continual-learning/docs/19-paper-plan.md): 단계별 논문 계획.
- [09-roadmap.md](/home/jimmy/repos/full-continual-learning/docs/09-roadmap.md): P0(NP)–P6(ET) 로드맵 개정과 결정 표.
- [15-compute-plan.md](/home/jimmy/repos/full-continual-learning/docs/15-compute-plan.md): 계산 계획의 2026-11-18 갱신.
- [2026-11-18-blueprint-et-design.md](/home/jimmy/repos/full-continual-learning/research/2026-11-18-blueprint-et-design.md): 조사 기록. 방법, 조사 출처와 확인 수준, 마스터 결정, 가칭 대응표, 사용자 결정 대기, NOT RUN 선언.

## 이번 작업의 경계

문서와 계획만 바꿨다. 구현, 모델 학습, GPU 실행, 클라우드 인스턴스 생성, 비용 지출, 외부 발송은 0회다. 변경은 branch 커밋이며 push와 병합은 마스터가 한다. 기존 파일의 이동·이름 변경·삭제는 없다. 원 논문·사료의 전문·그림과 개인 정보, 인증정보는 게시하지 않았다. 저장소 전체 validator는 worktree 검사 도구로 돌렸고(문서의 절대 링크를 worktree로 바꿔 해석), 원본 검사는 병합 뒤 main checkout에서 마스터가 돌린다.
