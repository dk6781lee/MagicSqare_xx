from control import error_codes as err
from boundary.input_handler import handle_grid_input


def test_u_in_01_null_grid_returns_e003():
    # Given: grid=None
    # When: handle_grid_input 호출
    # Then: E003 INVALID_NULL
    result = handle_grid_input(None)
    assert result["ok"] is False
    assert result["error_code"] == err.E003
    assert result["detail"] == err.INVALID_NULL
