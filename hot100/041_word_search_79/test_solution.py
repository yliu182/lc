import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestWordSearch:
    def test_example1(self, sol):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        assert sol.exist(board, "ABCCED") is True

    def test_example2(self, sol):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        assert sol.exist(board, "SEE") is True

    def test_example3(self, sol):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        assert sol.exist(board, "ABCB") is False

    def test_single_cell_match(self, sol):
        board = [["A"]]
        assert sol.exist(board, "A") is True

    def test_single_cell_no_match(self, sol):
        board = [["A"]]
        assert sol.exist(board, "B") is False

    def test_word_not_in_board(self, sol):
        board = [["A","B"],["C","D"]]
        assert sol.exist(board, "ABD") is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
