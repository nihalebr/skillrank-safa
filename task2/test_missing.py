import pytest
from missing import find_missing_number


def test_find_missing_number_basic():
    """Test basic missing number scenario"""
    assert find_missing_number([1, 2, 4, 5], 5) == 3


def test_find_missing_number_different_order():
    """Test missing number with different array order"""
    assert find_missing_number([2, 3, 1, 5], 5) == 4


def test_find_missing_number_first_missing():
    """Test when the first number (1) is missing"""
    assert find_missing_number([2, 3, 4, 5], 5) == 1


def test_find_missing_number_last_missing():
    """Test when the last number is missing"""
    assert find_missing_number([1, 2, 3, 4], 5) == 5


def test_find_missing_number_middle_missing():
    """Test when a middle number is missing"""
    assert find_missing_number([1, 2, 4, 5, 6], 6) == 3


def test_find_missing_number_single_element():
    """Test with single element array"""
    assert find_missing_number([1], 2) == 2
    assert find_missing_number([2], 2) == 1


def test_find_missing_number_empty_array():
    """Test with empty array - should return 1"""
    assert find_missing_number([], 1) == 1


def test_find_missing_number_large_range():
    """Test with larger range of numbers"""
    assert find_missing_number([1, 2, 3, 4, 6, 7, 8, 9, 10], 10) == 5


def test_find_missing_number_duplicate_numbers():
    """Test with duplicate numbers (edge case)"""
    # Note: This tests behavior with duplicates, which might not be handled properly
    # depending on the implementation
    assert find_missing_number([1, 1, 2, 4, 5], 5) == 2


def test_find_missing_number_negative_numbers():
    """Test with negative numbers (edge case)"""
    # This tests how the function handles negative numbers
    assert find_missing_number([-2, -1, 0, 1, 3], 3) == 5


def test_find_missing_number_zero_included():
    """Test with zero included in the range"""
    assert find_missing_number([0, 1, 2, 4], 4) == 3


@pytest.mark.parametrize(
    "nums, n, expected",
    [
        ([1, 2, 4, 5], 5, 3),
        ([2, 3, 1, 5], 5, 4),
        ([1, 2, 3, 4], 5, 5),
        ([2, 3, 4, 5], 5, 1),
        ([1, 2, 4, 5, 6], 6, 3),
        ([1], 2, 2),
        ([2], 2, 1),
        ([], 1, 1),
        ([1, 2, 3, 4, 6, 7, 8, 9, 10], 10, 5),
    ],
)
def test_find_missing_number_parametrized(nums, n, expected):
    """Test find_missing_number with various parametrized inputs"""
    assert find_missing_number(nums, n) == expected


def test_find_missing_number_edge_cases():
    """Test various edge cases for the missing number function"""
    # Test with n=1
    assert find_missing_number([], 1) == 1
    assert find_missing_number([1], 1) == 0  # This might be an edge case

    # Test with n=0 (edge case)
    assert find_missing_number([], 0) == 0

    # Test with very small arrays
    assert find_missing_number([1, 3], 3) == 2
