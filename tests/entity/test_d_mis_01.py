from entity.missing import find_not_exist_nums


def test_d_mis_01_g1_missing_nums(grid_g1):
    # Given: G1 격자
    # When: find_not_exist_nums(grid_g1) 호출
    # Then: [7, 10] 반환
    assert find_not_exist_nums(grid_g1) == [7, 10]
