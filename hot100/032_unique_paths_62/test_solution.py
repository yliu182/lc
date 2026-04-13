import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestUniquePaths:
    def test_example1(self, sol):
        assert sol.uniquePaths(3, 7) == 28

    def test_example2(self, sol):
        assert sol.uniquePaths(3, 2) == 3

    def test_example3(self, sol):
        assert sol.uniquePaths(7, 3) == 28

    def test_1x1(self, sol):
        assert sol.uniquePaths(1, 1) == 1

    def test_1xn(self, sol):
        assert sol.uniquePaths(1, 5) == 1

    def test_2x2(self, sol):
        assert sol.uniquePaths(2, 2) == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
