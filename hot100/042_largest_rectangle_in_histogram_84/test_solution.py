import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestLargestRectangleInHistogram:
    def test_example1(self, sol):
        assert sol.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10

    def test_example2(self, sol):
        assert sol.largestRectangleArea([2, 4]) == 4

    def test_single_bar(self, sol):
        assert sol.largestRectangleArea([5]) == 5

    def test_all_same_height(self, sol):
        assert sol.largestRectangleArea([3, 3, 3, 3]) == 12

    def test_descending(self, sol):
        assert sol.largestRectangleArea([5, 4, 3, 2, 1]) == 9

    def test_ascending(self, sol):
        assert sol.largestRectangleArea([1, 2, 3, 4, 5]) == 9


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
