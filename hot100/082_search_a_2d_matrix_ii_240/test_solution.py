import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


MATRIX = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]


def test_example1(sol):
    assert sol.searchMatrix(MATRIX, 5) is True


def test_example2(sol):
    assert sol.searchMatrix(MATRIX, 20) is False


def test_example3(sol):
    assert sol.searchMatrix([[1]], 1) is True


def test_single_not_found(sol):
    assert sol.searchMatrix([[1]], 2) is False


def test_top_right_corner(sol):
    assert sol.searchMatrix(MATRIX, 15) is True


def test_bottom_left_corner(sol):
    assert sol.searchMatrix(MATRIX, 18) is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
