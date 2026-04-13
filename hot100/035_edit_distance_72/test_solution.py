import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestEditDistance:
    def test_example1(self, sol):
        assert sol.minDistance("horse", "ros") == 3

    def test_example2(self, sol):
        assert sol.minDistance("intention", "execution") == 5

    def test_example3(self, sol):
        assert sol.minDistance("", "a") == 1

    def test_both_empty(self, sol):
        assert sol.minDistance("", "") == 0

    def test_same_string(self, sol):
        assert sol.minDistance("abc", "abc") == 0

    def test_one_empty(self, sol):
        assert sol.minDistance("abc", "") == 3


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
