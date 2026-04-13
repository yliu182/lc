import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestMergeIntervals:
    def test_example1(self, sol):
        assert sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]

    def test_example2(self, sol):
        assert sol.merge([[1, 4], [4, 5]]) == [[1, 5]]

    def test_example3(self, sol):
        assert sol.merge([[1, 4], [0, 4]]) == [[0, 4]]

    def test_no_overlap(self, sol):
        assert sol.merge([[1, 2], [4, 5], [7, 8]]) == [[1, 2], [4, 5], [7, 8]]

    def test_single_interval(self, sol):
        assert sol.merge([[1, 5]]) == [[1, 5]]

    def test_all_overlap(self, sol):
        assert sol.merge([[1, 4], [2, 5], [3, 6]]) == [[1, 6]]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
