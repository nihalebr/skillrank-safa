import pytest
from climb import climb_stairs

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 5),
    (5, 8),
    (10, 89),
    (20, 10946),
    (-1, 0),       
    (-10, 0),
])
def test_climb_stairs(n, expected):
    assert climb_stairs(n) == expected
