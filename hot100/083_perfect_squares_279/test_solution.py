import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


def test_example1(sol):
    assert sol.numSquares(12) == 3


def test_example2(sol):
    assert sol.numSquares(13) == 2


def test_example3(sol):
    assert sol.numSquares(1) == 1


def test_perfect_square(sol):
    assert sol.numSquares(16) == 1


def test_two_squares(sol):
    assert sol.numSquares(5) == 2  # 1 + 4


def test_larger(sol):
    assert sol.numSquares(7) == 4  # 4 + 1 + 1 + 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
