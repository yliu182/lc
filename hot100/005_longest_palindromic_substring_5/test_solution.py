import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


# --- LeetCode Examples ---

def test_example1(sol):
    result = sol.longestPalindrome("babad")
    assert result in ("bab", "aba")


def test_example2(sol):
    assert sol.longestPalindrome("cbbd") == "bb"


# --- Edge Cases ---

def test_single_char(sol):
    assert sol.longestPalindrome("a") == "a"


def test_all_same(sol):
    assert sol.longestPalindrome("aaaa") == "aaaa"


def test_no_palindrome_longer_than_1(sol):
    result = sol.longestPalindrome("abcd")
    assert len(result) == 1 and result in "abcd"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
