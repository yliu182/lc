import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


def test_example1(sol):
    assert sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4


def test_example2(sol):
    assert sol.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4


def test_example3(sol):
    assert sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1


def test_single(sol):
    assert sol.lengthOfLIS([1]) == 1


def test_increasing(sol):
    assert sol.lengthOfLIS([1, 2, 3, 4, 5]) == 5


def test_decreasing(sol):
    assert sol.lengthOfLIS([5, 4, 3, 2, 1]) == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
