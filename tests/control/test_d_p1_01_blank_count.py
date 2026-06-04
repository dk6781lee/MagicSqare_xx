from control import grid_status as status
from control.square_validator import can_claim_complete


def test_d_p1_01_blank_count_not_two_invalid(grid_one_blank):
    # Given: 빈칸 1개
    # When: can_claim_complete 호출
    # Then: INVALID
    result, failed = can_claim_complete(grid_one_blank)
    assert result == status.INVALID
    assert failed == []
