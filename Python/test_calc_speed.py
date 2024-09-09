import pytest
from calc_speed import CalcSpeed

@pytest.mark.parametrize("rpm, time, expected_result", [

    # success
    (30,90,20),
    (50,30,100),
    (75,55,82),

    # error
    (24,65,1.5),
    (54,34,76.2),
    (0,0,0)

])

def test_calc_speed(rpm, time, expected_result):
    my_test_speed = CalcSpeed(rpm, time)
    assert my_test_speed.calculate_speed() == expected_result
