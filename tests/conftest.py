import pytest

from entity.constants import BLANK_CELL, BLANK_COUNT, GRID_SIZE


@pytest.fixture
def grid_g1():
    """G1 — 4×4, 빈칸(BLANK_CELL) 2개, row-major (2,2)·(3,3) 1-index."""
    grid = [
        [16, 3, 2, 13],
        [5, BLANK_CELL, 11, 8],
        [9, 6, BLANK_CELL, 12],
        [4, 15, 14, 1],
    ]
    assert len(grid) == GRID_SIZE
    assert all(len(row) == GRID_SIZE for row in grid)
    assert sum(cell == BLANK_CELL for row in grid for cell in row) == BLANK_COUNT
    return grid
