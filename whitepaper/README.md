# FCL System ONE 설계 백서 (웹)

**웹 주소:** https://fcl-system-one-whitepaper.vercel.app

저장소의 통합 설계(System ONE)를 근거·검증 계획·열린 결정과 함께 한곳에 모은 읽기용 백서다. 기준은 main `2ecf3e0`(2026-11-12)이다. 통합 모델은 구현·학습·효용 검증이 하나도 없으며, 백서는 설계 문서를 다시 쓴 것이지 새 결과가 아니다. 주장마다 저장소와 같은 증거 라벨(USER / PROPOSAL / LITERATURE / ARCHIVE / OPEN)을 단다.

## 구성

| 파일 | 내용 |
|---|---|
| [index.html](/home/jimmy/repos/full-continual-learning/whitepaper/site/index.html) | 본문. 17절 6부로 나뉜다: 들어가며(2분 요약·읽는 법), 1부 왜·어디서 왔나(목적·계보·피드백 반영 추적·문헌), 2부 어떻게 동작하나(통합 구조·수학 명세·상태 계약), 3부 어떻게 검증하고 나아가나(평가·로드맵·진화 정책·열린 질문), 4부 다른 눈으로 보기(전문가 델타·지식 그래프), 부록 |
| [brief.html](/home/jimmy/repos/full-continual-learning/whitepaper/site/pages/brief.html) | 결정권자용 한 장(eli50) |
| [intuition.html](/home/jimmy/repos/full-continual-learning/whitepaper/site/pages/intuition.html) | 처음 보는 사람용 직관 설명(eli15) |
| [expert.html](/home/jimmy/repos/full-continual-learning/whitepaper/site/pages/expert.html) | 분야 전문가용 델타와 약점 공개(eli-guru) |
| [graph.html](/home/jimmy/repos/full-continual-learning/whitepaper/site/pages/graph.html) | 문서 코퍼스 35개의 지식 그래프. 노드 494개·연결 1,841개이며 graphify 0.9.106으로 만들었다 |
| [ledger.html](/home/jimmy/repos/full-continual-learning/whitepaper/site/pages/ledger.html) | 피드백 원장 325항목 탐색기. 데이터는 [2026-11-12-design-audit](/home/jimmy/repos/full-continual-learning/research/2026-11-12-design-audit/README.md)의 원장 JSON이다 |

## 다시 만들기와 배포

- **조립:** `python3 -I whitepaper/assemble.py`가 `sections/*.html` 조각, `assets/` 그림, `pages/` 동반 페이지, `style.css`, `template.html`을 묶는다. `site/`는 지우고 새로 만든다.
  - 조립하면서 번호·목차·그림/표 번호를 붙인다.
  - 다음을 검사하고, 하나라도 걸리면 실패한다: id 중복, 깨진 앵커, 누락 asset, 외부 리소스 로드, 호스트 경로, 이메일.
- **오프라인 동작:** CDN·웹폰트·외부 스크립트를 쓰지 않는다. 수식은 MathML이다.
- **배포:** `site/`의 복사본에서 `vercel deploy --prod`로 올린다. Vercel 프로젝트 이름은 `fcl-system-one-whitepaper`다.
- **이 저장소에 없는 빌드 도구:** 원장 탐색기(React 번들)와 지식 그래프는 별도 도구로 만든 결과물만 들어 있다.
  - 원장 탐색기: web-artifacts-builder로 번들했다. `node_modules`는 넣지 않았다.
  - 지식 그래프: graphify 산출물이다.

## 만든 방법과 검사

- **분담:** 작업자 6명이 공통 계약을 지키며 섹션·그림·동반 페이지를 나눠 만들었다. 마스터가 조립·검사·배포했다.
- **작업자별 skill:**
  - 디자인: ui-ux-pro-max·frontend-design
  - 원장 탐색기: web-artifacts-builder
  - 그림 21개: diagram-design
  - 차트 색 검증: dataviz
  - 수준별 글: eli50·eli15·eli-guru
  - 지식 그래프: graphify
- **검사 결과 (2026-11-12):**
  - 게이트 1–7 전부 PASS.
  - 조각·페이지·그림 45개가 0 FAIL·0 WARN.
  - 그림 self_check 21개 OK.
  - 데스크톱 1440px와 모바일 390px에서 가로 넘침 0. 모바일의 표 속 `.sr-only`가 문서 폭을 528px로 넓히던 문제는 고쳤다.
  - 배포본에서 그림 23개를 모두 불러왔고 MathML 429개를 렌더링했다.
- **검사가 보증하지 않는 것:** 문장이 저장소 문서와 같은 뜻인지는 원문과 대조해야 한다. 설계가 맞다는 증명도 아니다.

## 제3자 구성요소

[vis-network.min.js](/home/jimmy/repos/full-continual-learning/whitepaper/pages/vendor/vis-network.min.js)는 vis-network이며 Apache-2.0과 MIT의 이중 라이선스다. 라이선스 전문은 같은 폴더의 [LICENSE-vis-network-APACHE-2.0.txt](/home/jimmy/repos/full-continual-learning/whitepaper/pages/vendor/LICENSE-vis-network-APACHE-2.0.txt)와 [LICENSE-vis-network-MIT.txt](/home/jimmy/repos/full-continual-learning/whitepaper/pages/vendor/LICENSE-vis-network-MIT.txt)에 있다.
