import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestPalindromePartitioning:
    def test_example1(self, sol):
        result = sol.partition("aab")
        expected = [["a", "a", "b"], ["aa", "b"]]
        assert sorted(result) == sorted(expected)

    def test_example2(self, sol):
        assert sol.partition("a") == [["a"]]

    def test_single_char(self, sol):
        assert sol.partition("b") == [["b"]]

    def test_all_same(self, sol):
        result = sol.partition("aaa")
        expected = [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]
        assert sorted(result) == sorted(expected)

    def test_no_palindrome_partition(self, sol):
        result = sol.partition("abc")
        assert result == [["a", "b", "c"]]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
