import pytest
from collections import deque
from solution import Solution, TreeNode


def build_tree(values):
    """Build a binary tree from level-order list (None for missing nodes)."""
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


class TestKthSmallest:
    def test_example1(self):
        root = build_tree([3, 1, 4, None, 2])
        assert Solution().kthSmallest(root, 1) == 1

    def test_example2(self):
        root = build_tree([5, 3, 6, 2, 4, None, None, 1])
        assert Solution().kthSmallest(root, 3) == 3

    def test_example3_single_node(self):
        root = TreeNode(1)
        assert Solution().kthSmallest(root, 1) == 1

    def test_k_equals_n(self):
        root = build_tree([2, 1, 3])
        assert Solution().kthSmallest(root, 3) == 3

    def test_left_skewed(self):
        root = build_tree([3, 2, None, 1])
        assert Solution().kthSmallest(root, 2) == 2

    def test_right_skewed(self):
        root = build_tree([1, None, 2, None, 3])
        assert Solution().kthSmallest(root, 3) == 3


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
