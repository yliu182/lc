import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


# --- LeetCode Examples ---

def test_example1(sol):
    nums = [1, 2, 3]
    sol.nextPermutation(nums)
    assert nums == [1, 3, 2]


def test_example2(sol):
    nums = [3, 2, 1]
    sol.nextPermutation(nums)
    assert nums == [1, 2, 3]


def test_example3(sol):
    nums = [1, 1, 5]
    sol.nextPermutation(nums)
    assert nums == [1, 5, 1]


# --- Edge Cases ---

def test_single_element(sol):
    nums = [1]
    sol.nextPermutation(nums)
    assert nums == [1]


def test_two_elements(sol):
    nums = [1, 5]
    sol.nextPermutation(nums)
    assert nums == [5, 1]


def test_duplicates(sol):
    nums = [2, 3, 1, 3, 3]
    sol.nextPermutation(nums)
    assert nums == [2, 3, 3, 1, 3]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
