import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestRotateImage:
    def test_example1(self, sol):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        sol.rotate(matrix)
        assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    def test_example2(self, sol):
        matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        sol.rotate(matrix)
        assert matrix == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

    def test_example3(self, sol):
        matrix = [[1]]
        sol.rotate(matrix)
        assert matrix == [[1]]

    def test_2x2(self, sol):
        matrix = [[1, 2], [3, 4]]
        sol.rotate(matrix)
        assert matrix == [[3, 1], [4, 2]]

    def test_all_same(self, sol):
        matrix = [[1, 1], [1, 1]]
        sol.rotate(matrix)
        assert matrix == [[1, 1], [1, 1]]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
