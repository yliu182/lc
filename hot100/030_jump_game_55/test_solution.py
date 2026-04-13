import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestJumpGame:
    def test_example1(self, sol):
        assert sol.canJump([2, 3, 1, 1, 4]) is True

    def test_example2(self, sol):
        assert sol.canJump([3, 2, 1, 0, 4]) is False

    def test_example3(self, sol):
        assert sol.canJump([0]) is True

    def test_single_element(self, sol):
        assert sol.canJump([1]) is True

    def test_all_zeros_except_first(self, sol):
        assert sol.canJump([0, 1]) is False

    def test_large_first_jump(self, sol):
        assert sol.canJump([5, 0, 0, 0, 0, 1]) is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
