import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


def test_example1(sol):
    assert sol.findAnagrams("cbaebabacd", "abc") == [0, 6]


def test_example2(sol):
    assert sol.findAnagrams("abab", "ab") == [0, 1, 2]


def test_example3(sol):
    assert sol.findAnagrams("baa", "aa") == [1]


def test_no_anagram(sol):
    assert sol.findAnagrams("abcdef", "xyz") == []


def test_p_longer_than_s(sol):
    assert sol.findAnagrams("ab", "abc") == []


def test_entire_string(sol):
    assert sol.findAnagrams("abc", "cba") == [0]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
