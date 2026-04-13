import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestSingleNumber:
    def test_example1(self, sol):
        assert sol.singleNumber([2, 2, 1]) == 1

    def test_example2(self, sol):
        assert sol.singleNumber([4, 1, 2, 1, 2]) == 4

    def test_example3(self, sol):
        assert sol.singleNumber([1]) == 1

    def test_negative_numbers(self, sol):
        assert sol.singleNumber([-1, -1, -2]) == -2

    def test_zero_is_single(self, sol):
        assert sol.singleNumber([0, 1, 1]) == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
