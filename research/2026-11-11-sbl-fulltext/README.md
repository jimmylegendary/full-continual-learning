# 2026-11-11 SBL 원문 검토 상세 기록

종합과 결론은 [2026-11-11-sbl-fulltext-review.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext-review.md)에 있다. 이 폴더에는 논문별 정독 기록과 원문 확보 증거만 둔다.

| 기록 | 대상 | 내용 |
|---|---|---|
| [W1-spens24-hwu20.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/W1-spens24-hwu20.md) | SPENS24, HWU20 | 생성 모델 공고화, schema 의존 부호화. 공식 코드 감사 |
| [W2-chu25-goudar23.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/W2-chu25-goudar23.md) | CHU25, GOUDAR23 | sequence attractor, population subspace. 코드 감사 |
| [W3-elder26-miconi25.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/W3-elder26-miconi25.md) | ELDER26, MICONI25 | 불변 회로, meta-learned neuromodulated plasticity. 코드 감사 |
| [W4-tem20-kumar26.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/W4-tem20-kumar26.md) | TEM20, KUMAR26 | 구조/내용 분리, one-shot binding. 코드 감사 |
| [W5-spectrum26-structk25.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/W5-spectrum26-structk25.md) | SPECTRUM26 (+STRUCTK25 대체 안내) | schema 스펙트럼 관점, 두 리뷰의 상호 인용 |
| [W6-swami23-metadata-gap.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/W6-swami23-metadata-gap.md) | SWAMI23, 11편 서지, 갭 탐색 | CSCG rebinding, 공식 서지 대조, 반례 탐색 범위 |
| [W7-remediation.md](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/W7-remediation.md) | STRUCTK25와 보완 | 원문 정독, 위치 보완, 표기 점검, TEM20 재집계, CHU25 쪽수 |
| [evidence.json](/home/jimmy/repos/full-continual-learning/research/2026-11-11-sbl-fulltext/evidence.json) | 11편 | 접근 경로, 판본, 단어 수, 파일별 SHA-256 |

## 기록의 성격

- 각 기록은 worker의 정독 결과를 마스터가 검수해 옮긴 것이다. 각 문서 머리말에 정정한 내용과 표기 규칙을 적었다.
- 진행 순서:
  1. worker 6명이 원문을 정독했다.
  2. 리더 검증은 **FAIL**이었다. 리뷰 1편(STRUCTK25)의 원문 파일을 확보하지 못했고, 사실과 추론의 표기가 섞여 있었다.
  3. 보완 worker(W7)가 STRUCTK25 원문을 확보하고 위치 보완·정정을 마쳤다.
  4. 마스터가 핵심 주장 일부를 원문에서 다시 찾아 대조했다.
- 원문 파일은 저작권 때문에 저장소에 넣지 않았다. 호스트 작업 폴더 `fcl-sbl-fulltext-20261111/`에 있다. 같은 파일을 가진 사람은 evidence.json의 해시로 동일성을 확인할 수 있다.
- 코드는 읽기만 했고 실행하지 않았다. 재현 가능성 평가는 모두 정적 읽기에 근거한다.
- 라이선스가 없는 공식 코드 저장소가 많다. 인용과 식의 재구현은 가능하지만 코드를 그대로 가져오지 않는다.
