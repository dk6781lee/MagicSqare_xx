# MagicSquare_1004 (MagicSqare_xx)

4×4 **부분 마방진** 학습·설계 프로젝트. Mom Test로 문제를 정의하고, **10개 라인(행4·열4·대각2) 합=34** 검증을 Rule·Command·Test Loop로 구현하는 것이 1차 목표입니다.

> **현재 상태:** 문서·요구사항 정리 완료 (STEP 1). **소스 코드는 아직 없음.**

---

## 진짜 문제 (Mom Test)

빈 칸 2개를 채운 뒤 **행·열·대각선이 모두 34인지** 스스로 확신하지 못해, 검증에서 **한 줄(예: 대각선)을 빼먹으면** 맞춘 줄 알고 **시간을 낭비(예: 20분)** 한 뒤 다시 맞춰야 한다.

**증거 (인용 3줄)**

1. “지난주 OO 과제에서 빈칸 2개 넣고”
2. “행·열·대각선 합 맞췄는데 대각선 하나를 빼먹어서”
3. “20분 날렸다.”

---

## 도메인

| 항목 | 값 |
|------|-----|
| 격자 | 4×4 |
| 빈칸 | `0` × **2** |
| 숫자 | 1~16 (중복 없음) |
| 마법 합 | **34** |
| 검증 | **10라인** — H0–H3, V0–V3, D0·D1 |

**예시 (슬라이드 4.1, 빈칸 2개)**

```
16  3  2 13
 5 10 11  ?
 9  6  ? 12
 4 15 14  1
```

→ 빈칸 값: 8, 7 (행·열 기준; 전 라인 검증은 구현·테스트 대상)

---

## 이 프로젝트가 하지 않는 것 (표면 문제)

- 마방진 **완성 앱** / **Solver 자동 채우기**에만 집중
- 행·열만 보고 34에서 빼기
- `틀리면 false` 한 줄 응답만
- (초기 범위) GridUI·전체 ECB 한 번에 완성

---

## 디렉터리

```
MagicSqare_xx/
├── README.md                 ← 이 파일
├── docs/
│   └── PRD.md                ← 제품 요구 (Rule, Command, 테스트)
├── report/
│   ├── 01.MagicSquare_ProblemDefinition_Report.md  ← 문제 정의 통합
│   └── 01.MagicSquare_1004-STEP1-MomTest-Report.md ← Mom Test STEP 1
└── Prompring/
    └── 01.MagicSquare_1004-STEP1-Transcript-Export.md  ← 세션 대화 기록
```

---

## 문서 가이드

| 읽을 때 | 파일 |
|---------|------|
| 요구·API·테스트 시나리오 | [`docs/PRD.md`](docs/PRD.md) |
| Mom Test + 도메인 + 채점 | [`report/01.MagicSquare_ProblemDefinition_Report.md`](report/01.MagicSquare_ProblemDefinition_Report.md) |
| 인터뷰·종료 산출만 | [`report/01.MagicSquare_1004-STEP1-MomTest-Report.md`](report/01.MagicSquare_1004-STEP1-MomTest-Report.md) |
| 프롬프트·대화 이력 | [`Prompring/01.MagicSquare_1004-STEP1-Transcript-Export.md`](Prompring/01.MagicSquare_1004-STEP1-Transcript-Export.md) |

---

## 아키텍처 (ECB, 과제 4.1 — 참고)

| 구분 | 클래스 | 1차 범위 |
|------|--------|----------|
| Entity | `MagicSquare`, `Cell`, `SolveResult` | 후속 |
| Control | `SquareValidator`, `MissingFinder`, `Solver` | **Validator 우선** |
| Boundary | `GridUI`, `InputHandler`, `ResultDisplay` | 후속 |

**세션 3 (PRD) 범위:** Rule · Command · (Skill) · **Test Loop**

| Command | 설명 |
|---------|------|
| `ValidateAllLines(grid)` | 10라인 검증 + 실패 라인 목록 |
| `ValidateLine(grid, lineId)` | 단일 라인 |
| `CanClaimComplete(grid)` | 완료 주장 가능 여부 |

---

## 마일스톤

| 단계 | 상태 |
|------|------|
| STEP 1 — Mom Test · 문제 정의 | ✅ |
| `PRD.md` · report · Prompring | ✅ |
| Q2 인터뷰 (인지 순간) | ⬜ 미답 |
| Rule / Command / 테스트 코드 | ⬜ |
| Solver · Boundary · Entity | ⬜ |

---

## 다음 작업

1. Q2 답변 반영 (대각선 누락을 **언제·무엇을 보고** 알았는지)
2. PRD §7 P0 테스트부터 Red → Green (`ValidateAllLines`, `CanClaimComplete`)
3. 대각선만 34인데 “완료” 불가 케이스 고정 (Mom Test SC2)

---

## 참고

- 프로젝트 코드명: **MagicSquare_1004**
- 폴더명: `MagicSqare_xx` (워크스페이스 경로)
- Mom Test 자가 채점: **7 / 10** (Q2 미답)
