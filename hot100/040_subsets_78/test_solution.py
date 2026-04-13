import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestSubsets:
    def test_example1(self, sol):
        result = sol.subsets([1, 2, 3])
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        assert sorted([sorted(s) for s in result]) == sorted([sorted(s) for s in expected])

    def test_example2(self, sol):
        result = sol.subsets([0])
        expected = [[], [0]]
        assert sorted([sorted(s) for s in result]) == sorted([sorted(s) for s in expected])

    def test_example3(self, sol):
        result = sol.subsets([1, 2])
        expected = [[], [1], [2], [1, 2]]
        assert sorted([sorted(s) for s in result]) == sorted([sorted(s) for s in expected])

    def test_count_four_elements(self, sol):
        result = sol.subsets([1, 2, 3, 4])
        assert len(result) == 16

    def test_negative_numbers(self, sol):
        result = sol.subsets([-1, 0])
        expected = [[], [-1], [0], [-1, 0]]
        assert sorted([sorted(s) for s in result]) == sorted([sorted(s) for s in expected])


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
