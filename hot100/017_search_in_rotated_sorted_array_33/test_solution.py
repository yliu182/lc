import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


# --- LeetCode Examples ---

def test_example1(sol):
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 0) == 4


def test_example2(sol):
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 3) == -1


def test_example3(sol):
    assert sol.search([1], 0) == -1


# --- Edge Cases ---

def test_single_found(sol):
    assert sol.search([1], 1) == 0


def test_not_rotated(sol):
    assert sol.search([1, 2, 3, 4, 5], 3) == 2


def test_target_at_pivot(sol):
    assert sol.search([3, 1, 2], 3) == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
