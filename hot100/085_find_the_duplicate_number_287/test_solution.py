import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


def test_example1(sol):
    assert sol.findDuplicate([1, 3, 4, 2, 2]) == 2


def test_example2(sol):
    assert sol.findDuplicate([3, 1, 3, 4, 2]) == 3


def test_example3(sol):
    assert sol.findDuplicate([3, 3, 3, 3, 3]) == 3


def test_two_elements(sol):
    assert sol.findDuplicate([1, 1]) == 1


def test_duplicate_at_end(sol):
    assert sol.findDuplicate([1, 2, 3, 4, 4]) == 4


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
