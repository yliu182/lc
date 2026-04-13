import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


def test_example1(sol):
    assert sol.decodeString("3[a]2[bc]") == "aaabcbc"


def test_example2(sol):
    assert sol.decodeString("3[a2[c]]") == "accaccacc"


def test_example3(sol):
    assert sol.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"


def test_no_encoding(sol):
    assert sol.decodeString("abc") == "abc"


def test_nested_deep(sol):
    assert sol.decodeString("2[a2[b]]") == "abbabb"


def test_double_digit(sol):
    assert sol.decodeString("10[a]") == "aaaaaaaaaa"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
