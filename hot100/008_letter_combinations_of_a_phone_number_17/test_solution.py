import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


# --- LeetCode Examples ---

def test_example1(sol):
    result = sorted(sol.letterCombinations("23"))
    assert result == sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])


def test_example2(sol):
    assert sol.letterCombinations("") == []


def test_example3(sol):
    result = sorted(sol.letterCombinations("2"))
    assert result == ["a", "b", "c"]


# --- Edge Cases ---

def test_digit_7(sol):
    result = sorted(sol.letterCombinations("7"))
    assert result == ["p", "q", "r", "s"]


def test_digit_9(sol):
    result = sorted(sol.letterCombinations("9"))
    assert result == ["w", "x", "y", "z"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
