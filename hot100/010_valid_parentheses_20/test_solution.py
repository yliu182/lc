import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


# --- LeetCode Examples ---

def test_example1(sol):
    assert sol.isValid("()") is True


def test_example2(sol):
    assert sol.isValid("()[]{}") is True


def test_example3(sol):
    assert sol.isValid("(]") is False


# --- Edge Cases ---

def test_single_bracket(sol):
    assert sol.isValid("(") is False


def test_nested(sol):
    assert sol.isValid("{[()]}") is True


def test_wrong_order(sol):
    assert sol.isValid("([)]") is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
