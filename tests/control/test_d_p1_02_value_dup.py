from control import grid_status as status
from control.square_validator import can_claim_complete


def test_d_p1_02_duplicate_nonzero_invalid(grid_duplicate):
    # Given: 0 아닌 값 중복
    # When: can_claim_complete 호출
    # Then: INVALID
    result, failed = can_claim_complete(grid_duplicate)
    assert result == status.INVALID
    assert failed == []


def test_d_p1_02_value_oob_invalid(grid_value_oob):
    # Given: 1~16 밖 값
    # When: can_claim_complete 호출
    # Then: INVALID
    result, failed = can_claim_complete(grid_value_oob)
    assert result == status.INVALID
    assert failed == []
