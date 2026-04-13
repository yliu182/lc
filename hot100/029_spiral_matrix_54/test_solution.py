import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestSpiralMatrix:
    def test_example1(self, sol):
        assert sol.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    def test_example2(self, sol):
        assert sol.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    def test_example3(self, sol):
        assert sol.spiralOrder([[1, 2, 3, 4]]) == [1, 2, 3, 4]

    def test_single_element(self, sol):
        assert sol.spiralOrder([[1]]) == [1]

    def test_single_column(self, sol):
        assert sol.spiralOrder([[1], [2], [3]]) == [1, 2, 3]

    def test_2x2(self, sol):
        assert sol.spiralOrder([[1, 2], [3, 4]]) == [1, 2, 4, 3]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
