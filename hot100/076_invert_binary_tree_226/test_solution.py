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


def tree_to_list(root):
    """Convert tree to level-order list."""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()
    return result


class TestInvertBinaryTree:
    def test_example1(self):
        root = build_tree([4, 2, 7, 1, 3, 6, 9])
        result = Solution().invertTree(root)
        assert tree_to_list(result) == [4, 7, 2, 9, 6, 3, 1]

    def test_example2(self):
        root = build_tree([2, 1, 3])
        result = Solution().invertTree(root)
        assert tree_to_list(result) == [2, 3, 1]

    def test_example3_empty(self):
        result = Solution().invertTree(None)
        assert result is None

    def test_single_node(self):
        root = TreeNode(1)
        result = Solution().invertTree(root)
        assert tree_to_list(result) == [1]

    def test_left_only(self):
        root = build_tree([1, 2])
        result = Solution().invertTree(root)
        assert tree_to_list(result) == [1, None, 2]

    def test_right_only(self):
        root = build_tree([1, None, 2])
        result = Solution().invertTree(root)
        assert tree_to_list(result) == [1, 2]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
