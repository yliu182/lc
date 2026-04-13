import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestSearchA2DMatrix:
    def test_example1(self, sol):
        assert sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) is True

    def test_example2(self, sol):
        assert sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) is False

    def test_example3(self, sol):
        assert sol.searchMatrix([[1]], 1) is True

    def test_single_not_found(self, sol):
        assert sol.searchMatrix([[1]], 2) is False

    def test_first_element(self, sol):
        assert sol.searchMatrix([[1, 3], [5, 7]], 1) is True

    def test_last_element(self, sol):
        assert sol.searchMatrix([[1, 3], [5, 7]], 7) is True

    def test_target_too_small(self, sol):
        assert sol.searchMatrix([[2, 4], [6, 8]], 1) is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
