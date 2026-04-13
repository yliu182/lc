import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


def test_example1(sol):
    assert sol.subarraySum([1, 1, 1], 2) == 2


def test_example2(sol):
    assert sol.subarraySum([1, 2, 3], 3) == 2


def test_example3(sol):
    assert sol.subarraySum([1], 1) == 1


def test_negative_numbers(sol):
    assert sol.subarraySum([-1, -1, 1], 0) == 1


def test_all_zeros(sol):
    assert sol.subarraySum([0, 0, 0], 0) == 6


def test_no_match(sol):
    assert sol.subarraySum([1, 2, 3], 7) == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
