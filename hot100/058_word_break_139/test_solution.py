import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestWordBreak:
    def test_example1(self, sol):
        assert sol.wordBreak("leetcode", ["leet", "code"]) is True

    def test_example2(self, sol):
        assert sol.wordBreak("applepenapple", ["apple", "pen"]) is True

    def test_example3(self, sol):
        assert sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False

    def test_single_word(self, sol):
        assert sol.wordBreak("a", ["a"]) is True

    def test_no_match(self, sol):
        assert sol.wordBreak("abc", ["d", "e"]) is False

    def test_reuse_word(self, sol):
        assert sol.wordBreak("aaaa", ["a", "aa"]) is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
