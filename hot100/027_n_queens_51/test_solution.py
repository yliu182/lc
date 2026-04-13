import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestNQueens:
    def test_example1(self, sol):
        result = sol.solveNQueens(4)
        expected = [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
        assert sorted(result) == sorted(expected)

    def test_example2(self, sol):
        assert sol.solveNQueens(1) == [["Q"]]

    def test_n2_no_solution(self, sol):
        assert sol.solveNQueens(2) == []

    def test_n3_no_solution(self, sol):
        assert sol.solveNQueens(3) == []

    def test_n5_count(self, sol):
        result = sol.solveNQueens(5)
        assert len(result) == 10

    def test_n8_count(self, sol):
        result = sol.solveNQueens(8)
        assert len(result) == 92


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
