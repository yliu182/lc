import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


def test_example1(sol):
    assert sorted(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]


def test_example2(sol):
    assert sorted(sol.topKFrequent([1], 1)) == [1]


def test_example3(sol):
    assert sorted(sol.topKFrequent([1, 2], 2)) == [1, 2]


def test_all_same(sol):
    assert sorted(sol.topKFrequent([5, 5, 5], 1)) == [5]


def test_negative_numbers(sol):
    assert sorted(sol.topKFrequent([-1, -1, 2, 2, 2, 3], 2)) == [-1, 2]


def test_k_equals_unique(sol):
    assert sorted(sol.topKFrequent([1, 2, 3], 3)) == [1, 2, 3]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
