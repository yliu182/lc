import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


def test_example1(sol):
    assert sol.countBits(2) == [0, 1, 1]


def test_example2(sol):
    assert sol.countBits(5) == [0, 1, 1, 2, 1, 2]


def test_example3(sol):
    assert sol.countBits(0) == [0]


def test_one(sol):
    assert sol.countBits(1) == [0, 1]


def test_power_of_two(sol):
    assert sol.countBits(8) == [0, 1, 1, 2, 1, 2, 2, 3, 1]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
