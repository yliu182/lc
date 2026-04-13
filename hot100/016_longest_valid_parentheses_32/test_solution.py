import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


# --- LeetCode Examples ---

def test_example1(sol):
    assert sol.longestValidParentheses("(()") == 2


def test_example2(sol):
    assert sol.longestValidParentheses(")()())") == 4


def test_example3(sol):
    assert sol.longestValidParentheses("") == 0


# --- Edge Cases ---

def test_all_open(sol):
    assert sol.longestValidParentheses("((((") == 0


def test_all_close(sol):
    assert sol.longestValidParentheses("))))") == 0


def test_nested(sol):
    assert sol.longestValidParentheses("()(())") == 6


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
