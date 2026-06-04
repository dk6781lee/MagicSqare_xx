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


@pytest.fixture
def grid_g0():
    """G0 — 완성 4×4 마방진 (빈칸 없음, 10라인 합=MAGIC_SUM)."""
    return [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]


@pytest.fixture
def grid_g1_solved():
    """G1 빈칸 채움 (7,10) — 10라인 합=MAGIC_SUM."""
    return [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]


@pytest.fixture
def grid_p0_diagonal_fail():
    """10라인 중 D0 실패 (SC2 대각 누락 — CanClaimComplete 불가)."""
    return [
        [3, 16, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]


@pytest.fixture
def grid_3x4():
    return [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


@pytest.fixture
def grid_one_blank():
    return [
        [16, 3, 2, 13],
        [5, BLANK_CELL, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]


@pytest.fixture
def grid_value_oob():
    return [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 17],
    ]


@pytest.fixture
def grid_duplicate():
    return [
        [16, 3, 2, 13],
        [5, 10, 10, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]
