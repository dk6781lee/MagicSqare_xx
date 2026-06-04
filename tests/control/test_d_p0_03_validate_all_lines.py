from control.square_validator import validate_all_lines


def test_d_p0_03_diagonal_fail_lists_d0(grid_p0_diagonal_fail):
    # Given: D0 실패 격자
    # When: validate_all_lines 호출
    # Then: D0 in failed
    failed = validate_all_lines(grid_p0_diagonal_fail)
    assert "D0" in failed
