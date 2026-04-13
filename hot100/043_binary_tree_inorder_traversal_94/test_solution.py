import pytest
from collections import deque
from solution import Solution, TreeNode


def build_tree(values):
    """Build a binary tree from a level-order list. None represents missing nodes."""
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


class TestInorderTraversal:
    def test_example1(self, sol):
        root = build_tree([1, None, 2, 3])
        assert sol.inorderTraversal(root) == [1, 3, 2]

    def test_example2(self, sol):
        root = build_tree([])
        assert sol.inorderTraversal(root) == []

    def test_example3(self, sol):
        root = build_tree([1])
        assert sol.inorderTraversal(root) == [1]

    def test_left_skewed(self, sol):
        root = build_tree([3, 2, None, 1])
        assert sol.inorderTraversal(root) == [1, 2, 3]

    def test_complete_tree(self, sol):
        root = build_tree([2, 1, 3])
        assert sol.inorderTraversal(root) == [1, 2, 3]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
