import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


# --- LeetCode Examples ---

def test_example1(sol):
    assert sol.searchInsert([1, 3, 5, 6], 5) == 2


def test_example2(sol):
    assert sol.searchInsert([1, 3, 5, 6], 2) == 1


def test_example3(sol):
    assert sol.searchInsert([1, 3, 5, 6], 7) == 4


# --- Edge Cases ---

def test_insert_at_beginning(sol):
    assert sol.searchInsert([1, 3, 5, 6], 0) == 0


def test_single_element_found(sol):
    assert sol.searchInsert([1], 1) == 0


def test_single_element_insert_after(sol):
    assert sol.searchInsert([1], 2) == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
