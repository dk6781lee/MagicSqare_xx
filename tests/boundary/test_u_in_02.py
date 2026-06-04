from control import error_codes as err
from boundary.input_handler import handle_grid_input


def test_u_in_02_wrong_size_returns_e001(grid_3x4):
    # Given: grid 3×4
    # When: handle_grid_input 호출
    # Then: E001 INVALID_SIZE
    result = handle_grid_input(grid_3x4)
    assert result["ok"] is False
    assert result["error_code"] == err.E001
    assert result["detail"] == err.INVALID_SIZE
