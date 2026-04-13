import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


def sorted_triplets(result):
    return sorted([sorted(t) for t in result])


# --- LeetCode Examples ---

def test_example1(sol):
    result = sorted_triplets(sol.threeSum([-1, 0, 1, 2, -1, -4]))
    assert result == [[-1, -1, 2], [-1, 0, 1]]


def test_example2(sol):
    assert sol.threeSum([0, 1, 1]) == []


def test_example3(sol):
    result = sorted_triplets(sol.threeSum([0, 0, 0]))
    assert result == [[0, 0, 0]]


# --- Edge Cases ---

def test_empty(sol):
    assert sol.threeSum([]) == []


def test_two_elements(sol):
    assert sol.threeSum([0, 0]) == []


def test_all_zeros(sol):
    result = sorted_triplets(sol.threeSum([0, 0, 0, 0]))
    assert result == [[0, 0, 0]]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
