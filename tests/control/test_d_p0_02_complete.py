from control import grid_status as status
from control.square_validator import can_claim_complete


def test_d_p0_02_g1_solved_can_claim_complete(grid_g1_solved):
    # Given: G1 해답(7,10), 10라인 34, 빈칸 0
    # When: can_claim_complete 호출
    # Then: COMPLETE
    result, failed = can_claim_complete(grid_g1_solved)
    assert result == status.COMPLETE
    assert failed == []
