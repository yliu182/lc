import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


def test_example1(sol):
    assert sol.canPartition([1, 5, 11, 5]) is True


def test_example2(sol):
    assert sol.canPartition([1, 2, 3, 5]) is False


def test_example3(sol):
    assert sol.canPartition([1, 2, 3, 4]) is True  # [1,4] and [2,3]


def test_single_element(sol):
    assert sol.canPartition([1]) is False


def test_two_equal(sol):
    assert sol.canPartition([5, 5]) is True


def test_odd_sum(sol):
    assert sol.canPartition([1, 2, 4]) is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
