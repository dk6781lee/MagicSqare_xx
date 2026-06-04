from control import grid_status as status
from control.square_validator import can_claim_complete


def test_d_p1_03_wrong_size_invalid(grid_3x4):
    # Given: 3×4 격자
    # When: can_claim_complete 호출
    # Then: INVALID
    result, failed = can_claim_complete(grid_3x4)
    assert result == status.INVALID
    assert failed == []
