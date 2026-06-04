from entity.constants import BLANK_CELL


def find_blank_coords(grid: list[list[int]]) -> list[tuple[int, int]]:
    """빈칸(BLANK_CELL) 좌표를 row-major, 1-index로 반환."""
    coords: list[tuple[int, int]] = []
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell == BLANK_CELL:
                coords.append((row_index + 1, col_index + 1))
    return coords
