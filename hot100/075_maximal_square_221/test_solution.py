import pytest
from solution import Solution


class TestMaximalSquare:
    def test_example1(self):
        matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
        assert Solution().maximalSquare(matrix) == 4

    def test_example2(self):
        matrix = [["0", "1"], ["1", "0"]]
        assert Solution().maximalSquare(matrix) == 1

    def test_example3_all_zero(self):
        matrix = [["0"]]
        assert Solution().maximalSquare(matrix) == 0

    def test_single_one(self):
        matrix = [["1"]]
        assert Solution().maximalSquare(matrix) == 1

    def test_all_ones(self):
        matrix = [["1", "1"], ["1", "1"]]
        assert Solution().maximalSquare(matrix) == 4

    def test_no_square(self):
        matrix = [["0", "0"], ["0", "0"]]
        assert Solution().maximalSquare(matrix) == 0

    def test_3x3_square(self):
        matrix = [
            ["1", "1", "1"],
            ["1", "1", "1"],
            ["1", "1", "1"],
        ]
        assert Solution().maximalSquare(matrix) == 9


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
