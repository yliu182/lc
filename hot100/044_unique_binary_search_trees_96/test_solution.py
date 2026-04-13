import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestUniqueBinarySearchTrees:
    def test_example1(self, sol):
        assert sol.numTrees(3) == 5

    def test_example2(self, sol):
        assert sol.numTrees(1) == 1

    def test_n_equals_2(self, sol):
        assert sol.numTrees(2) == 2

    def test_n_equals_4(self, sol):
        assert sol.numTrees(4) == 14

    def test_n_equals_5(self, sol):
        assert sol.numTrees(5) == 42


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
