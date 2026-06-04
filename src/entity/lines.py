from entity.constants import GRID_SIZE, MAGIC_SUM

LINE_IDS: tuple[str, ...] = (
    "H0",
    "H1",
    "H2",
    "H3",
    "V0",
    "V1",
    "V2",
    "V3",
    "D0",
    "D1",
)


def line_cells(grid: list[list[int]], line_id: str) -> list[int]:
    if line_id.startswith("H"):
        row = int(line_id[1:])
        return list(grid[row])
    if line_id.startswith("V"):
        col = int(line_id[1:])
        return [grid[row][col] for row in range(GRID_SIZE)]
    if line_id == "D0":
        return [grid[i][i] for i in range(GRID_SIZE)]
    if line_id == "D1":
        return [grid[i][GRID_SIZE - 1 - i] for i in range(GRID_SIZE)]
    raise ValueError(f"unknown line_id: {line_id}")


def line_sum(grid: list[list[int]], line_id: str) -> int:
    return sum(line_cells(grid, line_id))


def line_is_valid(grid: list[list[int]], line_id: str) -> bool:
    return line_sum(grid, line_id) == MAGIC_SUM
