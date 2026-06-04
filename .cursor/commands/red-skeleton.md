# RED Skeleton — tests/ 스켈레톤만

MagicSquare_xxx — 앞 **`/red-test-plan`** 설계표 기준. **`tests/`만** 작성 · **`src/` 수정 금지**.

---

## 필수 선언

```
Phase: red | Layer: <entity|control|boundary> | Track: <Logic|UI> | ID: <D-*|U-*>
```

---

## 절차

1. 설계표에서 **Test ID·파일·픽스처·pytest 명령** 확인
2. **`tests/conftest.py`** — G1 등 픽스처 (로직 없음)
3. **`tests/<layer>/test_*.py`** — **함수 1개** RED
4. **AAA 주석** (Given / When / Then)
5. **Then** — `pytest.fail("RED: <ID> — …")` **한 줄만**
6. **pytest 실행** — FAIL 확인 → 보고

---

## 규칙

| 항목 | 규칙 |
|------|------|
| assert 본문 | **금지** (Then은 `pytest.fail`만) |
| skip / xfail / 통과 더미 | **금지** |
| src/ | **수정·생성 금지** |
| 상수 | `entity.constants` import — **픽스처 데이터만** (`GRID_SIZE`, `MAGIC_SUM`, `MAGIC_MAX`, `BLANK_*`) |
| Logic Mock | Domain Mock **금지** |

---

## Logic 템플릿 (D-LOC-01 예)

**파일:** `tests/entity/test_d_loc_01.py`

```python
import pytest


def test_d_loc_01_blank_coords_row_major(grid_g1):
    # Given: G1 격자 (0이 2개)
    # When: find_blank_coords(grid_g1) 호출
    # Then: [(2,2),(3,3)] 반환 (1-index, row-major)
    pytest.fail("RED: D-LOC-01 — 구현 없음, 의도적 실패")
```

**conftest:** `grid_g1` — G1 4×4, `BLANK_CELL`×2, row-major (2,2)·(3,3) 1-index

---

## UI 템플릿 (U-IN-01 예)

```python
def test_u_in_01_null_grid_returns_e003(grid_none):
    # Given: grid=None
    # When: boundary 입력 handler 호출
    # Then: E003 INVALID_NULL
    pytest.fail("RED: U-IN-01 — handler 미구현, 의도적 실패")
```

---

## pytest

```bash
python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v
```

**기대:** `pytest.fail` → `Failed` 또는 `entity.constants` 미구현 → `ModuleNotFoundError` (RED 유효)

---

## 보고

| 항목 | 내용 |
|------|------|
| Test ID | `D-*` / `U-*` |
| FAIL | pytest 마지막 한 줄 |
| 변경 파일 | **`tests/`만** |

---

## 금지

- GREEN / REFACTOR
- `src/` 구현
- 사용자 미요청 `git commit`
