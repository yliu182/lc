import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestMaximumSubarray:
    def test_example1(self, sol):
        assert sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    def test_example2(self, sol):
        assert sol.maxSubArray([1]) == 1

    def test_example3(self, sol):
        assert sol.maxSubArray([5, 4, -1, 7, 8]) == 23

    def test_all_negative(self, sol):
        assert sol.maxSubArray([-3, -2, -1, -4]) == -1

    def test_all_positive(self, sol):
        assert sol.maxSubArray([1, 2, 3]) == 6

    def test_single_negative(self, sol):
        assert sol.maxSubArray([-1]) == -1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
