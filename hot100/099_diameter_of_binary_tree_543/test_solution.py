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
    root = build_tree([1, 2, 3, 4, 5])
    assert sol.diameterOfBinaryTree(root) == 3


def test_example2(sol):
    root = build_tree([1, 2])
    assert sol.diameterOfBinaryTree(root) == 1


def test_example3(sol):
    root = build_tree([1])
    assert sol.diameterOfBinaryTree(root) == 0


def test_left_skewed(sol):
    root = build_tree([1, 2, None, 3, None, 4])
    assert sol.diameterOfBinaryTree(root) == 3


def test_not_through_root(sol):
    # Diameter might not pass through root
    root = build_tree([1, 2, 3, 4, 5, None, None, 6, None, None, 7])
    assert sol.diameterOfBinaryTree(root) == 4  # 6->4->2->5->7


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
