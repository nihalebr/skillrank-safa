import pytest
from missing import find_missing_number

# Normal test cases
@pytest.mark.parametrize("nums, n, expected", [
    ([1, 2, 4, 5], 5, 3),
    ([2, 3, 1, 5], 5, 4),
    ([1], 2, 2),
    ([1, 3], 3, 2),
])
def test_find_missing_number(nums, n, expected):
    assert find_missing_number(nums, n) == expected

# Edge case: wrong size
def test_missing_number_invalid_size():
    with pytest.raises(ValueError):
        find_missing_number([1, 2, 3], 5)
