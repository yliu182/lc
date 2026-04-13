import pytest
from collections import deque
from solution import Solution, TreeNode


def build_tree(values):
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


class TestValidateBST:
    def test_example1(self, sol):
        root = build_tree([2, 1, 3])
        assert sol.isValidBST(root) is True

    def test_example2(self, sol):
        root = build_tree([5, 1, 4, None, None, 3, 6])
        assert sol.isValidBST(root) is False

    def test_single_node(self, sol):
        root = build_tree([1])
        assert sol.isValidBST(root) is True

    def test_equal_values(self, sol):
        # BST does not allow equal values
        root = TreeNode(1)
        root.left = TreeNode(1)
        assert sol.isValidBST(root) is False

    def test_left_subtree_violation(self, sol):
        # 5 -> left=1, right=6; 6 -> left=3 (3 < 5 so invalid)
        root = build_tree([5, 1, 6, None, None, 3, 7])
        assert sol.isValidBST(root) is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
