import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


def test_example1(sol):
    assert sol.coinChange([1, 2, 5], 11) == 3


def test_example2(sol):
    assert sol.coinChange([2], 3) == -1


def test_example3(sol):
    assert sol.coinChange([1], 0) == 0


def test_single_coin(sol):
    assert sol.coinChange([1], 5) == 5


def test_exact_coin(sol):
    assert sol.coinChange([5], 5) == 1


def test_large_coins(sol):
    assert sol.coinChange([186, 419, 83, 408], 6249) == 20


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
