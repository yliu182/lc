import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestFirstMissingPositive:
    def test_example1(self, sol):
        assert sol.firstMissingPositive([1, 2, 0]) == 3

    def test_example2(self, sol):
        assert sol.firstMissingPositive([3, 4, -1, 1]) == 2

    def test_example3(self, sol):
        assert sol.firstMissingPositive([7, 8, 9, 11, 12]) == 1

    def test_single_element_one(self, sol):
        assert sol.firstMissingPositive([1]) == 2

    def test_single_element_two(self, sol):
        assert sol.firstMissingPositive([2]) == 1

    def test_consecutive_from_one(self, sol):
        assert sol.firstMissingPositive([1, 2, 3, 4, 5]) == 6

    def test_all_negative(self, sol):
        assert sol.firstMissingPositive([-1, -2, -3]) == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
