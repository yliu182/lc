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
    root = build_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    assert sol.pathSum(root, 8) == 3


def test_example2(sol):
    root = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    assert sol.pathSum(root, 22) == 3


def test_example3(sol):
    root = build_tree([1])
    assert sol.pathSum(root, 1) == 1


def test_empty_tree(sol):
    assert sol.pathSum(None, 0) == 0


def test_no_path(sol):
    root = build_tree([1, 2, 3])
    assert sol.pathSum(root, 10) == 0


def test_single_node_matches(sol):
    root = build_tree([0])
    assert sol.pathSum(root, 0) == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
