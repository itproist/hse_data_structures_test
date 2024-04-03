import pytest
from main.simplemath import f_me

@pytest.mark.parametrize("x, expected", [
    (0, 10),
    (5, 135),
    (-5, -115),
    (10, 260),
    (-10, -240),
    (20, 510),
    (-20, -490),
    (5.74, 153.5),
    (-5.74, -133.5),
    (float("inf"), None),
    (float("-inf"), None),
    ("abc", None),
    (None, None)
])

def test_f_me(x, expected):
    assert f_me(x) == expected
