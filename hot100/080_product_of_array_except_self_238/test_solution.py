import pytest
from solution import Solution


class TestProductExceptSelf:
    def test_example1(self):
        assert Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]

    def test_example2_with_zero(self):
        assert Solution().productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

    def test_example3_two_elements(self):
        assert Solution().productExceptSelf([1, 2]) == [2, 1]

    def test_all_ones(self):
        assert Solution().productExceptSelf([1, 1, 1, 1]) == [1, 1, 1, 1]

    def test_contains_negatives(self):
        assert Solution().productExceptSelf([-1, -2, -3]) == [6, 3, 2]

    def test_two_zeros(self):
        assert Solution().productExceptSelf([0, 0, 1, 2]) == [0, 0, 0, 0]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
