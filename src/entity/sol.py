"""FR-SOL — blank cell solver (entity)."""

from entity.constants import BLANK_CELL, MAGIC_MAX, VALUE_MIN
from entity.lines import LINE_IDS, line_is_valid
from entity.loc import find_blank_coords


def _missing_values(grid: list[list[int]]) -> list[int]:
    used = {cell for row in grid for cell in row if cell != BLANK_CELL}
    return [value for value in range(VALUE_MIN, MAGIC_MAX + 1) if value not in used]


def solution(grid: list[list[int]]) -> list[int] | None:
    (r1, c1), (r2, c2) = find_blank_coords(grid)
    missing = _missing_values(grid)
    for i, n1 in enumerate(missing):
        for n2 in missing[i + 1 :]:
            for v1, v2 in ((n1, n2), (n2, n1)):
                trial = [row[:] for row in grid]
                trial[r1 - 1][c1 - 1] = v1
                trial[r2 - 1][c2 - 1] = v2
                if all(line_is_valid(trial, line_id) for line_id in LINE_IDS):
                    return [r1, c1, v1, r2, c2, v2]
    return None
