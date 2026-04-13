import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


# --- LeetCode Examples ---

def test_example1(sol):
    result = sorted(sol.generateParenthesis(3))
    assert result == sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])


def test_example2(sol):
    assert sorted(sol.generateParenthesis(1)) == ["()"]


# --- Edge Cases ---

def test_n2(sol):
    result = sorted(sol.generateParenthesis(2))
    assert result == sorted(["(())", "()()"])


def test_n4_count(sol):
    result = sol.generateParenthesis(4)
    assert len(result) == 14


def test_all_valid(sol):
    for s in sol.generateParenthesis(3):
        count = 0
        for c in s:
            count += 1 if c == '(' else -1
            assert count >= 0
        assert count == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
