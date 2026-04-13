import pytest
from solution import Solution


class TestRotateArray:
    def test_example1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        Solution().rotate(nums, 3)
        assert nums == [5, 6, 7, 1, 2, 3, 4]

    def test_example2(self):
        nums = [-1, -100, 3, 99]
        Solution().rotate(nums, 2)
        assert nums == [3, 99, -1, -100]

    def test_example3_k_equals_length(self):
        nums = [1, 2, 3]
        Solution().rotate(nums, 3)
        assert nums == [1, 2, 3]

    def test_k_zero(self):
        nums = [1, 2, 3]
        Solution().rotate(nums, 0)
        assert nums == [1, 2, 3]

    def test_k_greater_than_length(self):
        nums = [1, 2]
        Solution().rotate(nums, 5)
        assert nums == [2, 1]

    def test_single_element(self):
        nums = [1]
        Solution().rotate(nums, 1)
        assert nums == [1]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
