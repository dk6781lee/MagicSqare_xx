from control import grid_status as status
from control.square_validator import can_claim_complete


def test_d_p0_01_diagonal_fail_cannot_claim_complete(grid_p0_diagonal_fail):
    # Given: 행·열 34, D0 실패 격자
    # When: can_claim_complete 호출
    # Then: INCOMPLETE, 실패 라인에 D0 포함
    result, failed = can_claim_complete(grid_p0_diagonal_fail)
    assert result == status.INCOMPLETE
    assert "D0" in failed
