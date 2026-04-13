import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


def test_example1(sol):
    result = sol.calcEquation(
        [["a", "b"], ["b", "c"]], [2.0, 3.0],
        [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    )
    expected = [6.0, 0.5, -1.0, 1.0, -1.0]
    for r, e in zip(result, expected):
        assert abs(r - e) < 1e-5


def test_example2(sol):
    result = sol.calcEquation(
        [["a", "b"], ["b", "c"], ["bc", "cd"]], [1.5, 2.5, 5.0],
        [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    )
    expected = [3.75, 0.4, 5.0, 0.2]
    for r, e in zip(result, expected):
        assert abs(r - e) < 1e-5


def test_example3(sol):
    result = sol.calcEquation(
        [["a", "b"]], [0.5],
        [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    )
    expected = [0.5, 2.0, -1.0, -1.0]
    for r, e in zip(result, expected):
        assert abs(r - e) < 1e-5


def test_self_division(sol):
    result = sol.calcEquation(
        [["a", "b"]], [2.0],
        [["a", "a"]]
    )
    assert abs(result[0] - 1.0) < 1e-5


def test_unknown_variable(sol):
    result = sol.calcEquation(
        [["a", "b"]], [2.0],
        [["x", "y"]]
    )
    assert abs(result[0] - (-1.0)) < 1e-5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
