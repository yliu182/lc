import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


# --- LeetCode Examples ---

def test_example1(sol):
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3


def test_example2(sol):
    assert sol.lengthOfLongestSubstring("bbbbb") == 1


def test_example3(sol):
    assert sol.lengthOfLongestSubstring("pwwkew") == 3


# --- Edge Cases ---

def test_empty_string(sol):
    assert sol.lengthOfLongestSubstring("") == 0


def test_single_char(sol):
    assert sol.lengthOfLongestSubstring("a") == 1


def test_all_unique(sol):
    assert sol.lengthOfLongestSubstring("abcdef") == 6


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
