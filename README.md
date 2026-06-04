# MagicSquare_1004 (MagicSqare_xx)

4×4 **부분 마방진** 학습·설계 프로젝트. Mom Test로 문제를 정의하고, **10개 라인(행4·열4·대각2) 합=34** 검증을 Rule·Command·Test Loop로 구현하는 것이 1차 목표입니다.

> **현재 상태:** STEP 1~6 · **GREEN + Golden Master** (D-SOL-01). **REFACTOR 1건** (`sol`→`find_not_exist_nums`). **14 tests passed** · 후보 B/C·D-P2-01 후속.

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
| 마법 합 | **34** (MagicConstant SSOT) |
| 검증 | **10라인** — H0–H3, V0–V3, D0·D1 |
| 정상 출력 | `int[6]` → `[r1,c1,n1,r2,c2,n2]` (**좌표 1-index**) |
| 오류 | E001~E007 (**boundary**); entity는 E001~E005 처리 금지 |

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
- GridUI·전체 ECB **한 번에** 완성

---

## 디렉터리

```
MagicSqare_xx/
├── README.md
├── .cursorrules              ← AI·TDD·ECB 규칙
├── pyproject.toml            ← pytest Harness
├── .cursor/
│   ├── commands/             ← /tdd-red, /review-ecb
│   └── skills/magic-square-tdd/
├── src/
│   ├── entity/               ← constants, loc, missing, validation, lines
│   ├── control/              ← square_validator, grid_input, error_codes
│   └── boundary/             ← input_handler
├── tests/
│   ├── entity/               ← Logic D-*  test_d_*
│   ├── control/
│   └── boundary/             ← UI U-*  test_u_*
├── docs/
│   └── PRD.md
├── report/
│   ├── 01.*                  ← STEP 1 Mom Test
│   └── 02.*                  ← STEP 2 Harness
└── Prompring/
    ├── 01.* · 02.*
```

---

## 빠른 시작 (Harness)

```powershell
cd MagicSqare_xx
pip install -e ".[dev]"
pytest
python -c "import entity, control, boundary; print('ok')"
```

| 명령 | 기대 |
|------|------|
| `pytest` | **13 passed** |
| import 확인 | `ok` |

**Harness:** `tests/entity|control|boundary/`에 `__init__.py` 두지 않음 (`src/` 패키지 import shadow 방지).

---

## Dual-Track TDD

| Track | Layer | 테스트 ID | 파일 | Mock |
|-------|-------|-----------|------|------|
| **Logic** | entity, control | `D-*` | `test_d_*.py` | Domain Mock **금지** |
| **UI** | boundary | `U-*` | `test_u_*.py` | **허용** |

**루프:** RED → GREEN → REFACTOR · assert 완화·skip·xfail 금지

**Cursor**

| 용도 | 경로 |
|------|------|
| 규칙 SSOT | [`.cursorrules`](.cursorrules) |
| TDD 절차 Skill | [`.cursor/skills/magic-square-tdd/SKILL.md`](.cursor/skills/magic-square-tdd/SKILL.md) |
| RED Command | [`.cursor/commands/tdd-red.md`](.cursor/commands/tdd-red.md) |
| RED 스켈레톤 | [`.cursor/commands/red-skeleton.md`](.cursor/commands/red-skeleton.md) |
| GREEN 최소 | [`.cursor/commands/green-minimal.md`](.cursor/commands/green-minimal.md) |
| ECB 리뷰 | [`.cursor/commands/review-ecb.md`](.cursor/commands/review-ecb.md) |

---

## 문서 가이드

| 읽을 때 | 파일 |
|---------|------|
| 요구·Rule·Command·테스트 | [`docs/PRD.md`](docs/PRD.md) |
| Mom Test + 도메인 + 채점 | [`report/01.MagicSquare_ProblemDefinition_Report.md`](report/01.MagicSquare_ProblemDefinition_Report.md) |
| STEP 1 인터뷰 | [`report/01.MagicSquare_1004-STEP1-MomTest-Report.md`](report/01.MagicSquare_1004-STEP1-MomTest-Report.md) |
| STEP 2 Harness | [`report/02.MagicSquare_1004-STEP2-Harness-Report.md`](report/02.MagicSquare_1004-STEP2-Harness-Report.md) |
| STEP 3 TDD Plan | [`report/03.MagicSquare_1004-STEP3-TDD-Plan-Report.md`](report/03.MagicSquare_1004-STEP3-TDD-Plan-Report.md) |
| STEP 4 RED Skeleton | [`report/04.MagicSquare_1004-STEP4-RED-Skeleton-Report.md`](report/04.MagicSquare_1004-STEP4-RED-Skeleton-Report.md) |
| STEP 5 GREEN | [`report/05.MagicSquare_1004-STEP5-GREEN-Report.md`](report/05.MagicSquare_1004-STEP5-GREEN-Report.md) |
| STEP 6 Golden Master | [`report/06.MagicSquare_1004-STEP6-GoldenMaster-Report.md`](report/06.MagicSquare_1004-STEP6-GoldenMaster-Report.md) |
| STEP 7 REFACTOR | [`report/07.MagicSquare_1004-STEP7-REFACTOR-Report.md`](report/07.MagicSquare_1004-STEP7-REFACTOR-Report.md) |
| 세션 대화 | [`Prompring/01.*`](Prompring/) … [`Prompring/07.*`](Prompring/07.MagicSquare_1004-STEP7-REFACTOR-Transcript-Export.md) |

---

## 아키텍처 (ECB)

의존: **boundary → control → entity** · entity → * import 금지

| 구분 | 클래스 / 함수 | 범위 |
|------|----------------|------|
| Entity | `find_blank_coords`, `MagicSquare`, … | Logic **D-*** (예: D-LOC-01) |
| Control | `SquareValidator`, `MissingFinder`, `Solver` | C1–C3, **Validator 우선** |
| Boundary | `GridUI`, `InputHandler`, … | UI **U-*** (예: U-IN-01) |

| Command | 설명 |
|---------|------|
| `ValidateAllLines(grid)` | 10라인 검증 + 실패 라인 목록 |
| `ValidateLine(grid, lineId)` | 단일 라인 |
| `CanClaimComplete(grid)` | 완료 주장 가능 여부 |

---

## Git 브랜치

| 브랜치 | 용도 |
|--------|------|
| `main` | 통합 |
| `staging` | 이슈·작업 기준 |
| `spec` | 스펙·설계 |
| `red` | RED 단계 TDD |

원격: https://github.com/dk6781lee/MagicSqare_xx

---

## 마일스톤

| 단계 | 상태 |
|------|------|
| STEP 1 — Mom Test · 문제 정의 | ✅ |
| STEP 2 — Harness · `.cursorrules` · Cursor Skill/Command | ✅ |
| Q2 인터뷰 (인지 순간) | ⬜ |
| Logic GREEN (D-LOC/MIS/VAL) | ✅ |
| Control GREEN (C1–C3, D-P0/P1) | ✅ |
| Boundary UI (U-IN-01/02) | ✅ |
| STEP 6 — Golden Master (D-SOL-01) | ✅ |
| STEP 7 — REFACTOR (1건 + 스멜 문서) | ✅ (부분) |
| REFACTOR 후보 B/C · D-P2-01 (TBD) | ⬜ |

---

## 다음 작업

1. Q2 답변 반영
2. **REFACTOR 후보 B** — 10선 `failed_line_ids` SSOT (`/refactor-safe`)
3. **REFACTOR 후보 C** — `scan_grid` + BlankPolicy
4. D-P2-01 (TBD) · U-OUT-01 golden

---

## 참고

- 프로젝트 코드명: **MagicSquare_1004**
- 폴더명: `MagicSqare_xx`
- Mom Test 자가 채점: **7 / 10** (Q2 미답)
