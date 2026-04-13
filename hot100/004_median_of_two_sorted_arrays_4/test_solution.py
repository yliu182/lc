import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


# --- LeetCode Examples ---

def test_example1(sol):
    assert sol.findMedianSortedArrays([1, 3], [2]) == pytest.approx(2.0)


def test_example2(sol):
    assert sol.findMedianSortedArrays([1, 2], [3, 4]) == pytest.approx(2.5)


# --- Edge Cases ---

def test_one_empty(sol):
    assert sol.findMedianSortedArrays([], [1]) == pytest.approx(1.0)


def test_single_elements(sol):
    assert sol.findMedianSortedArrays([1], [2]) == pytest.approx(1.5)


def test_same_elements(sol):
    assert sol.findMedianSortedArrays([1, 1], [1, 1]) == pytest.approx(1.0)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
