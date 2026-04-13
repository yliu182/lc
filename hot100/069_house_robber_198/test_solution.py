import pytest
from solution import Solution


class TestHouseRobber:
    def test_example1(self):
        assert Solution().rob([1, 2, 3, 1]) == 4

    def test_example2(self):
        assert Solution().rob([2, 7, 9, 3, 1]) == 12

    def test_example3_single(self):
        assert Solution().rob([5]) == 5

    def test_two_houses(self):
        assert Solution().rob([1, 2]) == 2

    def test_all_same(self):
        assert Solution().rob([3, 3, 3, 3]) == 6

    def test_decreasing(self):
        assert Solution().rob([10, 1, 1, 10]) == 20


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
