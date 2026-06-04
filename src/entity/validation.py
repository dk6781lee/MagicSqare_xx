from entity.constants import (
    BLANK_CELL,
    BLANK_COUNT,
    GRID_SIZE,
    MAGIC_MAX,
    VALUE_MIN,
)
from entity.lines import LINE_IDS, line_is_valid


def is_magic_square(grid: list[list[int]]) -> bool:
    """완성 4×4 마방진(I1~I5): 크기·값·빈칸 0·비중복·10라인 합=MAGIC_SUM."""
    if len(grid) != GRID_SIZE or any(len(row) != GRID_SIZE for row in grid):
        return False
    blank_count = 0
    non_blank: list[int] = []
    for row in grid:
        for cell in row:
            if cell == BLANK_CELL:
                blank_count += 1
            elif VALUE_MIN <= cell <= MAGIC_MAX:
                non_blank.append(cell)
            else:
                return False
    if blank_count != 0:
        return False
    if len(non_blank) != len(set(non_blank)):
        return False
    if len(non_blank) != MAGIC_MAX:
        return False
    return all(line_is_valid(grid, line_id) for line_id in LINE_IDS)
