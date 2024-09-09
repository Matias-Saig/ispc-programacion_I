import pytest
from calc_distance import CalcDistance

@pytest.mark.parametrize("rpm, time, expected_result", [

    # success
    (30,90,500),
    (50,30,833),
    (75,55,1253),

    # error
    (24,65,1.5),
    (54,34,76.2),
    (0,0,0)

])

def test_calc_distance(rpm, time, expected_result):
    my_test_speed = CalcDistance(rpm, time)
    assert my_test_speed.calculate_distance() == expected_result
