import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


def test_example1(sol):
    nums = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]


def test_example2(sol):
    nums = [0]
    sol.moveZeroes(nums)
    assert nums == [0]


def test_example3(sol):
    nums = [1]
    sol.moveZeroes(nums)
    assert nums == [1]


def test_no_zeroes(sol):
    nums = [1, 2, 3]
    sol.moveZeroes(nums)
    assert nums == [1, 2, 3]


def test_all_zeroes(sol):
    nums = [0, 0, 0]
    sol.moveZeroes(nums)
    assert nums == [0, 0, 0]


def test_zeroes_at_end(sol):
    nums = [1, 2, 0, 0]
    sol.moveZeroes(nums)
    assert nums == [1, 2, 0, 0]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
