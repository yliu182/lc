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


def find_node(root, val):
    """Find a node with the given value in the tree."""
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


class TestLowestCommonAncestor:
    def test_example1(self):
        root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p = find_node(root, 5)
        q = find_node(root, 1)
        result = Solution().lowestCommonAncestor(root, p, q)
        assert result.val == 3

    def test_example2_ancestor_is_p(self):
        root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p = find_node(root, 5)
        q = find_node(root, 4)
        result = Solution().lowestCommonAncestor(root, p, q)
        assert result.val == 5

    def test_example3_parent_child(self):
        root = build_tree([1, 2])
        p = find_node(root, 1)
        q = find_node(root, 2)
        result = Solution().lowestCommonAncestor(root, p, q)
        assert result.val == 1

    def test_siblings(self):
        root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p = find_node(root, 6)
        q = find_node(root, 2)
        result = Solution().lowestCommonAncestor(root, p, q)
        assert result.val == 5

    def test_deep_nodes(self):
        root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p = find_node(root, 7)
        q = find_node(root, 4)
        result = Solution().lowestCommonAncestor(root, p, q)
        assert result.val == 2

    def test_left_and_right_subtrees(self):
        root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p = find_node(root, 6)
        q = find_node(root, 0)
        result = Solution().lowestCommonAncestor(root, p, q)
        assert result.val == 3


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
