import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestMinimumWindowSubstring:
    def test_example1(self, sol):
        assert sol.minWindow("ADOBECODEBANC", "ABC") == "BANC"

    def test_example2(self, sol):
        assert sol.minWindow("a", "a") == "a"

    def test_example3(self, sol):
        assert sol.minWindow("a", "aa") == ""

    def test_no_match(self, sol):
        assert sol.minWindow("abc", "z") == ""

    def test_entire_string(self, sol):
        assert sol.minWindow("abc", "abc") == "abc"

    def test_duplicate_chars_in_t(self, sol):
        assert sol.minWindow("aab", "aab") == "aab"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
