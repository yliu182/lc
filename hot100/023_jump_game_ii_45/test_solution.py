import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestJumpGameII:
    def test_example1(self, sol):
        assert sol.jump([2, 3, 1, 1, 4]) == 2

    def test_example2(self, sol):
        assert sol.jump([2, 3, 0, 1, 4]) == 2

    def test_example3(self, sol):
        assert sol.jump([1, 2, 3]) == 2

    def test_single_element(self, sol):
        assert sol.jump([0]) == 0

    def test_two_elements(self, sol):
        assert sol.jump([1, 1]) == 1

    def test_large_first_jump(self, sol):
        assert sol.jump([10, 1, 1, 1, 1]) == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
