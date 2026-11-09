# 게시·소스·수치 검증 기록

검증일: **2026-11-09**. 초기 연구 이관 commit: `58613da820656953355ec38beb716206a60e189b`, tree: `4f5820a9c5dac0f322acd1efd61cad9829037ba3`.

## 1. 실제 확인한 원격 내용

GitHub connector에서 recursive Git tree를 다시 읽었다. `truncated=false`, 파일33개, 그중 Markdown25개였다. README의16개 읽기 순서 링크가 모두 해당 tree의 실제 파일로 연결되는 것을 대조했다. 이 후속 commit은 수치 요약·원본 manifest·검증 receipt를 추가한다.

이는 **원격 경로와 README navigation 검사**다. 모든 Markdown 본문 링크나 모든 외부 논문 URL을 자동으로 전수 검사했다는 뜻은 아니다. 로컬 git clone은 실행 환경의 DNS 제한으로 실패했다. `tools/validate_docs.py`는 제공했지만 이 작업에서는 저장소 전체를 내려받아 해당 명령을 끝까지 실행하지 못했다.

## 2. 원본 소스의 byte identity

Library에서 실제 확보한 원본 파일의 `SHA1('blob '+length+'\\0'+bytes)`를 계산해 원격 Git tree의 blob SHA와 대조했다.

| 파일 | 원격 blob SHA | 원본과 일치 |
|---|---|---|
| `probe.py` | `543a5c0ce300cba4a4690ad40d4e5013d77bdb07` | 예 |
| `verify.py` | `520a74c1b2da972431ba499e4067a934dbbf168c` | 예 |
| `requirements.txt` | `871c966c09f89af68c058514f0f7ecce9f1578d3` | 예 |
| `verification.original.json` | `c57c4be0d7ca32e9ba186f14bb8ae1de6eee701d` | 예 — 원본 `verification.json`의 파일명만 구분 |

원본 코드2개는 Python AST parsing도 통과했다. 원본 PDF와 ZIP의 SHA-256도 다시 계산해 [EVIDENCE](EVIDENCE.md)의 값과 일치함을 확인했다.

## 3. 작은 Phase-0의 실제 재실행

실제 실행:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python probe.py --output results.rerun.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python verify.py
```

원본 산출물을 덮어쓰지 않는 별도 작업 디렉터리에서 실행했다. `verify.py`에는 원래 저장된 `results.json`을 넣어 첫 seed를 재실행하고 비교했다. 별도의 전체 rerun에서는 원본과 다음 필드들을 비교했다.

| 비교 | 결과 |
|---|---|
| Config 전체 | 정확히 일치 |
| 2환경 ×6seeds =12 runs의 per-task scores·tuning 결과 전체 | 정확히 일치 |
| 집계 summary 전체 | 정확히 일치 |
| Bayesian posterior와 독립 primal 해법 | 최대 절대오차 `3.58046925441613e-14` |
| 동일 mixture component의 single prior 환원 | 최대 절대오차 `1.7763568394002505e-15` |
| 동일 component의 posterior responsibility | prior probabilities와 일치 |

현재 환경: Python3.13.5, NumPy2.3.5, SciPy1.17.0. 역사적 환경의 Python3.12.14와 다르지만 비교한 수치 필드는 같았다. 환경·실행시간을 포함한 JSON 전체 bytes가 같다는 주장은 하지 않는다. 이번 전체 작은 실험의 실행시간은 약3.079초였으며 **LLM latency benchmark가 아니다.**

Machine-readable receipt: [publication-validation.json](experiments/phase0/publication-validation.json).

## 4. 검증하지 않은 것

- 통합 HOPE/Titans/CMS/recursive model의 구현·학습·GPU 실행.
- 자연어의 schema 형성·자율 분화·Sleep의 실제 효용.
- 같은 정확도에서 LLM보다 빠른 System ONE.
- 모든 외부 논문의 본문·수치·코드와 최신 버전의 독립 감사.
- 전체 repository의 모든 로컬 링크·외부 URL 전수 실행 검사.

작은 합성 실험의 재현은 원래 scope 안에서의 확인이다. 위 미실행 영역의 PASS로 확대하지 않는다.
