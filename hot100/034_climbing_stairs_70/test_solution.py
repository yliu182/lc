import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestClimbingStairs:
    def test_example1(self, sol):
        assert sol.climbStairs(2) == 2

    def test_example2(self, sol):
        assert sol.climbStairs(3) == 3

    def test_example3(self, sol):
        assert sol.climbStairs(4) == 5

    def test_n1(self, sol):
        assert sol.climbStairs(1) == 1

    def test_n5(self, sol):
        assert sol.climbStairs(5) == 8

    def test_n10(self, sol):
        assert sol.climbStairs(10) == 89


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
