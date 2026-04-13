import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestPermutations:
    def test_example1(self, sol):
        result = sol.permute([1, 2, 3])
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        assert sorted(result) == sorted(expected)

    def test_example2(self, sol):
        result = sol.permute([0, 1])
        expected = [[0, 1], [1, 0]]
        assert sorted(result) == sorted(expected)

    def test_example3(self, sol):
        assert sol.permute([1]) == [[1]]

    def test_two_negative(self, sol):
        result = sol.permute([-1, -2])
        expected = [[-1, -2], [-2, -1]]
        assert sorted(result) == sorted(expected)

    def test_count_four_elements(self, sol):
        result = sol.permute([1, 2, 3, 4])
        assert len(result) == 24


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
