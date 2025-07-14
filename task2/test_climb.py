import pytest
from climb import climb_stairs


def test_climb_stairs_basic():
    """Test climbing basic stairs:
    - 0 stairs should return 0
    - 1 stair should return 1"""
    assert climb_stairs(0) == 0
    assert climb_stairs(1) == 1


def test_climb_stairs_four():
    """Test climbing 4 stairs should return 5"""
    assert climb_stairs(4) == 5


def test_climb_stairs_seven():
    """Test climbing 7 stairs should return 21"""
    assert climb_stairs(7) == 21


def test_climb_stairs_negative():
    """Test climbing negative stairs should return 0"""
    assert climb_stairs(-1) == 0
    assert climb_stairs(-5) == 0


def test_climb_stairs_large_number():
    """Test climbing a larger number of stairs"""
    assert climb_stairs(20) == 10946


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (6, 13),
        (7, 21),
        (8, 34),
        (9, 55),
        (10, 89),
    ],
)
def test_climb_stairs_parametrized(n, expected):
    """Test climbing stairs with parametrized values"""
    assert climb_stairs(n) == expected
