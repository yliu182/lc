import pytest
from collections import deque
from solution import Solution, TreeNode


def build_tree(values):
    """Build a binary tree from level-order list."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


@pytest.fixture
def sol():
    return Solution()


def test_example1(sol):
    root = build_tree([3, 2, 3, None, 3, None, 1])
    assert sol.rob(root) == 7


def test_example2(sol):
    root = build_tree([3, 4, 5, 1, 3, None, 1])
    assert sol.rob(root) == 9


def test_example3(sol):
    root = build_tree([1])
    assert sol.rob(root) == 1


def test_single_path(sol):
    root = build_tree([2, 1, None, 4])
    assert sol.rob(root) == 6  # 2 + 4


def test_all_same(sol):
    root = build_tree([1, 1, 1, 1, 1, 1, 1])
    assert sol.rob(root) == 4  # pick all leaves + root level


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
