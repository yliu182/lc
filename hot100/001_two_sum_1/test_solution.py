import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


# --- LeetCode Examples ---

def test_example1(sol):
    assert sorted(sol.twoSum([2, 7, 11, 15], 9)) == [0, 1]


def test_example2(sol):
    assert sorted(sol.twoSum([3, 2, 4], 6)) == [1, 2]


def test_example3(sol):
    assert sorted(sol.twoSum([3, 3], 6)) == [0, 1]


# --- Edge Cases ---

def test_negative_numbers(sol):
    assert sorted(sol.twoSum([-1, -2, -3, -4, -5], -8)) == [2, 4]


def test_large_list(sol):
    nums = list(range(1, 10001))
    result = sorted(sol.twoSum(nums, 19999))
    assert result == [9998, 9999]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
