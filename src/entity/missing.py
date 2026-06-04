from entity.constants import BLANK_CELL, MAGIC_MAX, VALUE_MIN


def find_not_exist_nums(grid: list[list[int]]) -> list[int]:
    """격자에 없는 1~MAGIC_MAX 값을 오름차순으로 반환."""
    present = {cell for row in grid for cell in row if cell != BLANK_CELL}
    return [n for n in range(VALUE_MIN, MAGIC_MAX + 1) if n not in present]
