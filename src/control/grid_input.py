from entity.constants import BLANK_CELL, BLANK_COUNT, GRID_SIZE, MAGIC_MAX, VALUE_MIN

from control import error_codes as err


def validate_grid_input(grid: list[list[int]] | None) -> tuple[bool, str | None, str | None]:
    """입력 격자 선검증. (ok, error_code, detail)."""
    if grid is None:
        return False, err.E003, err.INVALID_NULL
    if len(grid) != GRID_SIZE or any(len(row) != GRID_SIZE for row in grid):
        return False, err.E001, err.INVALID_SIZE
    blank_count = 0
    seen_non_blank: set[int] = set()
    for row in grid:
        for cell in row:
            if cell == BLANK_CELL:
                blank_count += 1
                continue
            if cell < VALUE_MIN or cell > MAGIC_MAX:
                return False, err.E003, err.INVALID_VALUE
            if cell in seen_non_blank:
                return False, err.E004, err.INVALID_DUPLICATE
            seen_non_blank.add(cell)
    if blank_count != BLANK_COUNT:
        return False, err.E002, err.INVALID_BLANK_COUNT
    return True, None, None
