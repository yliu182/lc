import pytest
from solution import Solution


class TestFindMin:
    def test_example1(self):
        assert Solution().findMin([3, 4, 5, 1, 2]) == 1

    def test_example2(self):
        assert Solution().findMin([4, 5, 6, 7, 0, 1, 2]) == 0

    def test_example3_not_rotated(self):
        assert Solution().findMin([11, 13, 15, 17]) == 11

    def test_single_element(self):
        assert Solution().findMin([1]) == 1

    def test_two_elements(self):
        assert Solution().findMin([2, 1]) == 1

    def test_rotated_at_end(self):
        assert Solution().findMin([2, 3, 4, 5, 1]) == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
