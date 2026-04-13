import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestLongestConsecutiveSequence:
    def test_example1(self, sol):
        assert sol.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4

    def test_example2(self, sol):
        assert sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9

    def test_empty(self, sol):
        assert sol.longestConsecutive([]) == 0

    def test_single_element(self, sol):
        assert sol.longestConsecutive([1]) == 1

    def test_duplicates(self, sol):
        assert sol.longestConsecutive([1, 2, 2, 3]) == 3

    def test_no_consecutive(self, sol):
        assert sol.longestConsecutive([10, 20, 30]) == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
