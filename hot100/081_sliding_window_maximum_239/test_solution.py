import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


def test_example1(sol):
    assert sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]


def test_example2(sol):
    assert sol.maxSlidingWindow([1], 1) == [1]


def test_example3(sol):
    assert sol.maxSlidingWindow([1, -1], 1) == [1, -1]


def test_all_same(sol):
    assert sol.maxSlidingWindow([5, 5, 5, 5], 2) == [5, 5, 5]


def test_decreasing(sol):
    assert sol.maxSlidingWindow([4, 3, 2, 1], 2) == [4, 3, 2]


def test_k_equals_length(sol):
    assert sol.maxSlidingWindow([1, 3, 2], 3) == [3]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
