import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


def sorted_combos(result):
    return sorted([sorted(c) for c in result])


# --- LeetCode Examples ---

def test_example1(sol):
    result = sorted_combos(sol.combinationSum([2, 3, 6, 7], 7))
    assert result == [[2, 2, 3], [7]]


def test_example2(sol):
    result = sorted_combos(sol.combinationSum([2, 3, 5], 8))
    assert result == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]


def test_example3(sol):
    assert sol.combinationSum([2], 1) == []


# --- Edge Cases ---

def test_single_candidate_exact(sol):
    result = sorted_combos(sol.combinationSum([3], 9))
    assert result == [[3, 3, 3]]


def test_single_candidate_no_match(sol):
    assert sol.combinationSum([5], 3) == []


def test_large_target(sol):
    result = sorted_combos(sol.combinationSum([1], 3))
    assert result == [[1, 1, 1]]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
