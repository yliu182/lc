import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


# --- LeetCode Examples ---

def test_example1(sol):
    assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_example2(sol):
    assert sol.maxArea([1, 1]) == 1


# --- Edge Cases ---

def test_ascending(sol):
    assert sol.maxArea([1, 2, 3, 4, 5]) == 6


def test_descending(sol):
    assert sol.maxArea([5, 4, 3, 2, 1]) == 6


def test_all_same(sol):
    assert sol.maxArea([3, 3, 3, 3]) == 9


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
