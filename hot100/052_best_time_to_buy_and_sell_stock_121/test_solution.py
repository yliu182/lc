import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestMaxProfit:
    def test_example1(self, sol):
        assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5

    def test_example2(self, sol):
        assert sol.maxProfit([7, 6, 4, 3, 1]) == 0

    def test_single_price(self, sol):
        assert sol.maxProfit([5]) == 0

    def test_two_prices_profit(self, sol):
        assert sol.maxProfit([1, 5]) == 4

    def test_all_same(self, sol):
        assert sol.maxProfit([3, 3, 3, 3]) == 0

    def test_increasing(self, sol):
        assert sol.maxProfit([1, 2, 3, 4, 5]) == 4


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
