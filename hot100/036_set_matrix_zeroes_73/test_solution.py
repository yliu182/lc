import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestSetMatrixZeroes:
    def test_example1(self, sol):
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        sol.setZeroes(matrix)
        assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    def test_example2(self, sol):
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        sol.setZeroes(matrix)
        assert matrix == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

    def test_example3(self, sol):
        matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
        sol.setZeroes(matrix)
        assert matrix == [[1, 0, 3], [0, 0, 0], [7, 0, 9]]

    def test_no_zeroes(self, sol):
        matrix = [[1, 2], [3, 4]]
        sol.setZeroes(matrix)
        assert matrix == [[1, 2], [3, 4]]

    def test_all_zeroes(self, sol):
        matrix = [[0, 0], [0, 0]]
        sol.setZeroes(matrix)
        assert matrix == [[0, 0], [0, 0]]

    def test_single_element_zero(self, sol):
        matrix = [[0]]
        sol.setZeroes(matrix)
        assert matrix == [[0]]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
