import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


def test_example1(sol):
    assert sol.maxProfit([1, 2, 3, 0, 2]) == 3


def test_example2(sol):
    assert sol.maxProfit([1]) == 0


def test_example3(sol):
    assert sol.maxProfit([1, 2]) == 1


def test_decreasing(sol):
    assert sol.maxProfit([5, 4, 3, 2, 1]) == 0


def test_two_transactions(sol):
    assert sol.maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0]) == 13


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
