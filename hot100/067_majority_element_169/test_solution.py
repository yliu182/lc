import pytest
from solution import Solution


class TestMajorityElement:
    def test_example1(self):
        assert Solution().majorityElement([3, 2, 3]) == 3

    def test_example2(self):
        assert Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2

    def test_example3_single(self):
        assert Solution().majorityElement([1]) == 1

    def test_all_same(self):
        assert Solution().majorityElement([5, 5, 5, 5]) == 5

    def test_two_elements(self):
        assert Solution().majorityElement([3, 3]) == 3

    def test_negative_numbers(self):
        assert Solution().majorityElement([-1, -1, 2]) == -1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
