import pytest
from solution import Solution


class TestMaxProduct:
    def test_example1(self):
        assert Solution().maxProduct([2, 3, -2, 4]) == 6

    def test_example2(self):
        assert Solution().maxProduct([-2, 0, -1]) == 0

    def test_example3_single_negative(self):
        assert Solution().maxProduct([-2]) == -2

    def test_all_positive(self):
        assert Solution().maxProduct([1, 2, 3, 4]) == 24

    def test_two_negatives(self):
        assert Solution().maxProduct([-2, 3, -4]) == 24

    def test_single_element(self):
        assert Solution().maxProduct([0]) == 0

    def test_zeros_between(self):
        assert Solution().maxProduct([2, 0, 3, -2, 4]) == 4


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
