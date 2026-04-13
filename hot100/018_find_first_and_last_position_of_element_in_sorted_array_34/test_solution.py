import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


# --- LeetCode Examples ---

def test_example1(sol):
    assert sol.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]


def test_example2(sol):
    assert sol.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]


def test_example3(sol):
    assert sol.searchRange([], 0) == [-1, -1]


# --- Edge Cases ---

def test_single_element_found(sol):
    assert sol.searchRange([1], 1) == [0, 0]


def test_single_element_not_found(sol):
    assert sol.searchRange([1], 2) == [-1, -1]


def test_all_same(sol):
    assert sol.searchRange([2, 2, 2, 2], 2) == [0, 3]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
