import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestTrappingRainWater:
    def test_example1(self, sol):
        assert sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6

    def test_example2(self, sol):
        assert sol.trap([4, 2, 0, 3, 2, 5]) == 9

    def test_example3(self, sol):
        assert sol.trap([1, 0, 1]) == 1

    def test_no_trap_ascending(self, sol):
        assert sol.trap([1, 2, 3, 4]) == 0

    def test_no_trap_descending(self, sol):
        assert sol.trap([4, 3, 2, 1]) == 0

    def test_single_element(self, sol):
        assert sol.trap([5]) == 0

    def test_flat(self, sol):
        assert sol.trap([3, 3, 3]) == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
