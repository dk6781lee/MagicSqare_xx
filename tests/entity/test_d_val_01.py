from entity.validation import is_magic_square


def test_d_val_01_g0_is_magic(grid_g0):
    # Given: G0 완성 마방진
    # When: is_magic_square(grid_g0) 호출
    # Then: True
    assert is_magic_square(grid_g0) is True
