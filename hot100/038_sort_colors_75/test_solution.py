import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestSortColors:
    def test_example1(self, sol):
        nums = [2, 0, 2, 1, 1, 0]
        sol.sortColors(nums)
        assert nums == [0, 0, 1, 1, 2, 2]

    def test_example2(self, sol):
        nums = [2, 0, 1]
        sol.sortColors(nums)
        assert nums == [0, 1, 2]

    def test_example3(self, sol):
        nums = [0]
        sol.sortColors(nums)
        assert nums == [0]

    def test_already_sorted(self, sol):
        nums = [0, 0, 1, 1, 2, 2]
        sol.sortColors(nums)
        assert nums == [0, 0, 1, 1, 2, 2]

    def test_reverse_sorted(self, sol):
        nums = [2, 2, 1, 1, 0, 0]
        sol.sortColors(nums)
        assert nums == [0, 0, 1, 1, 2, 2]

    def test_all_same(self, sol):
        nums = [1, 1, 1]
        sol.sortColors(nums)
        assert nums == [1, 1, 1]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
