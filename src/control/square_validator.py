from entity.constants import BLANK_CELL, BLANK_COUNT, GRID_SIZE, MAGIC_MAX, VALUE_MIN
from entity.lines import LINE_IDS, line_is_valid

from control import grid_status as status


def validate_line(grid: list[list[int]], line_id: str) -> bool:
    return line_is_valid(grid, line_id)


def validate_all_lines(grid: list[list[int]]) -> list[str]:
    """실패한 라인 ID 목록 (H0–H3, V0–V3, D0, D1)."""
    return [line_id for line_id in LINE_IDS if not line_is_valid(grid, line_id)]


def _domain_structure_ok(grid: list[list[int]]) -> bool:
    if len(grid) != GRID_SIZE or any(len(row) != GRID_SIZE for row in grid):
        return False
    blank_count = 0
    seen: set[int] = set()
    for row in grid:
        for cell in row:
            if cell == BLANK_CELL:
                blank_count += 1
                continue
            if cell < VALUE_MIN or cell > MAGIC_MAX:
                return False
            if cell in seen:
                return False
            seen.add(cell)
    if blank_count not in (0, BLANK_COUNT):
        return False
    return True


def can_claim_complete(grid: list[list[int]]) -> tuple[str, list[str]]:
    """R1~R6 종합. (COMPLETE|INCOMPLETE|INVALID, 실패 라인 목록)."""
    if not _domain_structure_ok(grid):
        return status.INVALID, []
    failed = validate_all_lines(grid)
    if failed:
        return status.INCOMPLETE, failed
    return status.COMPLETE, []
