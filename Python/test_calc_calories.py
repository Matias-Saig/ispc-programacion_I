import pytest
from calc_calories import CalcCalories

@pytest.mark.parametrize("power, time, expected_result", [


# success
(50,60,717),
(10,30,72),

# error
(25,90,538),
(0, 0,50),
(0,0,0)

])

def test_calc_calories(power, time, expected_result):
    my_test_calories = CalcCalories(power, time)
    assert my_test_calories.calculate_calories() == expected_result
