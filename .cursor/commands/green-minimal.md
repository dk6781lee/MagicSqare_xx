# GREEN Minimal — RED 1묶음 최소 통과

MagicSquare_xx — 앞 **`/red-test-plan`**·**`/red-skeleton`** 설계표 기준. **RED 1묶음**만 최소 구현으로 Green. **REFACTOR 금지**.

참고: `.cursorrules`, `.cursor/skills/magic-square-tdd/SKILL.md`, `docs/PRD.md` §7.

---

## 필수 선언 (응답 첫 줄)

```
Phase: green | Layer: <entity|control|boundary> | Track: <Logic|UI> | ID: <D-*|U-*>
```

예: `Phase: green | Layer: entity | Track: Logic | ID: D-LOC-01`

---

## 절차

1. **RED 재확인** — `pytest` 실행. `pytest.fail` 의도적 실패 또는 `ImportError`/`ModuleNotFoundError`(구현·constants 미존재)인지 확인.
2. **`src/` 최소 구현** — 해당 Layer·함수만. **하드코딩·매직넘버 금지** → `entity/constants.py` MagicConstant SSOT (`GRID_SIZE`, `MAGIC_SUM`, `MAGIC_MAX`, `BLANK_*` 등).
3. **ECB (entity일 때)** — E001~E005 **raise/return 금지**. **boundary/control import 금지** (stdlib·typing만).
4. **`tests/`** — `pytest.fail` 제거 → **실제 assert**. **Then은 설계표 SSOT** (Command placeholder 좌표·값 무시).
5. **pytest PASS** — 단일 테스트 노드 + 해당 파일 전체.
6. **(선택) REPL 스모크** — Given fixture(예: G1) vs 설계표 Then.

---

## 규칙

| 항목 | 규칙 |
|------|------|
| 범위 | 이번 RED **Test ID 1묶음**만 |
| 상수 | `34`/`16`/`4`/빈칸 `2` — **constants import만** |
| Logic Mock | Domain Mock **금지** |
| UI Track | boundary에서 control/entity·I/O Mock **허용** |
| Harness | `tests/entity|control|boundary/__init__.py` **생성 금지** (`src/` 패키지 import shadow) |

---

## Logic 템플릿 (D-LOC-01 예)

**구현:** `src/entity/constants.py`, `src/entity/loc.py` — `find_blank_coords(grid)`

**테스트:** `tests/entity/test_d_loc_01.py`

```python
from entity.loc import find_blank_coords


def test_d_loc_01_blank_coords_row_major(grid_g1):
    # Given: G1 격자 (0이 2개)
    # When: find_blank_coords(grid_g1) 호출
    # Then: [(2,2),(3,3)] 반환 (1-index, row-major)  ← 설계표 SSOT
    assert find_blank_coords(grid_g1) == [(2, 2), (3, 3)]
```

---

## pytest 예시 (bash)

프로젝트 루트 (`pip install -e ".[dev]"` 또는 venv 활성화 후):

```bash
python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v
python -m pytest tests/entity/test_d_loc_01.py -v
```

Logic 안전망 (선택):

```bash
python -m pytest tests/entity tests/control -q
```

REPL 스모크 (선택):

```bash
python -c "from entity.constants import BLANK_CELL; from entity.loc import find_blank_coords; g=[[16,3,2,13],[5,BLANK_CELL,11,8],[9,6,BLANK_CELL,12],[4,15,14,1]]; print(find_blank_coords(g))"
```

---

## 보고

| 항목 | 내용 |
|------|------|
| PASS Test ID | `D-*` / `U-*` |
| 변경 파일 | `src/` + `tests/` (layer별 목록) |
| pytest | 명령 + **pass** 로그 (단일·파일) |
| Then | **설계표 SSOT** — Command 예시 좌표와 다르면 설계표 우선 |
| ECB·SSOT | E001~E005 entity 미처리 · 리터럴 34/16 산재 없음 |

---

## 금지

- 이번 RED 묶음 **외 Test ID** 동시 해결
- **REFACTOR** (이름·추출·구조 정리 — 별도 Phase)
- assert 완화 · `@pytest.mark.skip` · `xfail`
- `golden/` 임의 갱신 (`UPDATE_GOLDEN` 승인 없이)
- 사용자 미요청 **git commit**

---

## 사용자가 채팅에 추가할 것

- **RED Test ID** (예: `D-LOC-01`)
- **테스트 파일 경로** (예: `tests/entity/test_d_loc_01.py`)
- **구현 대상 함수** (예: `find_blank_coords`)
- (선택) Layer · Track · 설계표 Then·Given 요약
