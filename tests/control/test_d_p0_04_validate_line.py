from control.square_validator import validate_line


def test_d_p0_04_validate_line_d0_fails_h0_passes(grid_p0_diagonal_fail):
    # Given: D0 실패 격자
    # When: validate_line(grid, lineId)
    # Then: D0 False, H0 True (슬라이드 예시 맥락 — H0는 통과)
    assert validate_line(grid_p0_diagonal_fail, "D0") is False
    assert validate_line(grid_p0_diagonal_fail, "H0") is True
    assert validate_line(grid_p0_diagonal_fail, "V0") is False
