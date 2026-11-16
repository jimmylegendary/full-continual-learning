# 2026-11-16 이관 참고문헌과 확인 범위

아래 링크는 CRUD 및 주간 보고 대화에서 연결된 1차 자료의 주소를 보존한다. **이번 작업의 상태는 discussion-import / ARCHIVE**이며 원문 최신성·표·수치·코드 실행을 재검증하지 않았다. 기존 catalog의 확인 등급을 일괄 승격하지 않는다.

## Schema 생명주기 제안의 선행 연결

| 자료 | 링크 | 대화에서 사용한 연결 |
|---|---|---|
| Nested Learning / HOPE | https://arxiv.org/abs/2512.24695 | 다중 학습 수준과 CMS |
| MIRAS | https://arxiv.org/abs/2504.13173 | 기억 설계와 retention; 기존 연구가 Delete를 전혀 다루지 않았다고 말하지 않음 |
| S-LoRA | https://arxiv.org/abs/2311.03285 | 많은 adapter의 저장 계층·선택적 serving; schema 정책의 검증은 아님 |
| WISE | https://arxiv.org/abs/2405.14768 | 원래 지식과 수정 기억의 분리·routing 비교 |
| Learning to Prompt for Continual Learning | https://research.google/pubs/learning-to-prompt-for-continual-learning/ | 입력에 따른 parameter/prompt pool 선택 |
| InfLoRA | https://store.computer.org/csdl/proceedings-article/cvpr/2024/530000x638/20hOEKsYy5y | low-rank 업데이트의 간섭 제어 |
| 압축·기술길이 관점의 continual learning | https://arxiv.org/abs/2006.15078 | 보존/압축 문제의 인접 선행연구; 제목·서지 재대조 필요 |

## 11/16 보고의 추가 확인 대상

| 보고된 자료 | 공식 원문·코드 | 이번 상태 |
|---|---|---|
| Tian et al., Domain-specific schema reuse | https://doi.org/10.1038/s41467-026-68692-x ; https://github.com/kathytian-kx/DomainSpecific_SchemaReuse | 보고 이관. 대화의 이전 언급과 중복; 새 발견으로 재계산하지 않음 |
| Singh et al., mental schema interrelations | https://doi.org/10.1007/s00221-026-07252-7 | 초록 중심이었다는 보고를 보존. continuous 분류 미확정 |
| 위 논문의 correction | https://doi.org/10.1007/s00221-026-07373-z | 정정 내용 미확보라는 제한을 유지 |
| Category-theoretic SBL working paper | https://arxiv.org/abs/2604.10589 | 형식 이론으로 보고; neural 학습 효용 근거로 전용하지 않음 |
| S-HAI code | https://github.com/toonvdm/grounding-schemas | discrete latent/structured probabilistic; 이 주에 새 공개라는 주장 없음 |
| Yoshida sleep/manifold | https://doi.org/10.64898/2026.05.27.728344 | 이전 보고는 초록 중심; 최신 상태 재확인 필요 |
| Kumar schema4one | https://arxiv.org/abs/2106.03580 ; https://github.com/mgkumar138/schema4one | 원 보고는 v5(2026-10-20); 동기화 시점 확인으로 오인하지 않음 |
| Schema for ICL | https://arxiv.org/abs/2510.13905 | explicit scaffolding과 지속적인 neural learning 구분 |
| IP2-RSNN | https://arxiv.org/abs/2501.14539 | neural dynamics 인접 연구; latent schema 자체의 검증과 구분 |

정확한 발행일·개정일·저자·venue·읽은 범위는 후속 실제 접근에서 확인한다. URL의 존재를 전문 정독이나 재현 완료로 바꾸지 않는다.
