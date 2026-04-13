import pytest
from solution import Solution


class TestFindKthLargest:
    def test_example1(self):
        assert Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5

    def test_example2(self):
        assert Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

    def test_example3_k_equals_1(self):
        assert Solution().findKthLargest([1], 1) == 1

    def test_all_same(self):
        assert Solution().findKthLargest([7, 7, 7, 7], 2) == 7

    def test_k_equals_length(self):
        assert Solution().findKthLargest([3, 1, 2], 3) == 1

    def test_negative_numbers(self):
        assert Solution().findKthLargest([-1, -2, -3, -4], 2) == -2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
