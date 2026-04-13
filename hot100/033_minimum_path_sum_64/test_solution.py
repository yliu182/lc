import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestMinimumPathSum:
    def test_example1(self, sol):
        assert sol.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7

    def test_example2(self, sol):
        assert sol.minPathSum([[1, 2, 3], [4, 5, 6]]) == 12

    def test_example3(self, sol):
        assert sol.minPathSum([[1, 2], [1, 1]]) == 3

    def test_single_cell(self, sol):
        assert sol.minPathSum([[5]]) == 5

    def test_single_row(self, sol):
        assert sol.minPathSum([[1, 2, 3]]) == 6

    def test_single_column(self, sol):
        assert sol.minPathSum([[1], [2], [3]]) == 6


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
