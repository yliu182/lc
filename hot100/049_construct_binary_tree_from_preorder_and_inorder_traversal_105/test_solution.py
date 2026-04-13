import pytest
from collections import deque
from solution import Solution, TreeNode


def tree_to_list(root):
    """Convert a binary tree to level-order list representation."""
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


@pytest.fixture
def sol():
    return Solution()


class TestBuildTree:
    def test_example1(self, sol):
        root = sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
        assert tree_to_list(root) == [3, 9, 20, None, None, 15, 7]

    def test_example2(self, sol):
        root = sol.buildTree([-1], [-1])
        assert tree_to_list(root) == [-1]

    def test_left_skewed(self, sol):
        root = sol.buildTree([3, 2, 1], [1, 2, 3])
        assert tree_to_list(root) == [3, 2, None, 1]

    def test_right_skewed(self, sol):
        root = sol.buildTree([1, 2, 3], [1, 2, 3])
        assert tree_to_list(root) == [1, None, 2, None, 3]

    def test_two_nodes(self, sol):
        root = sol.buildTree([1, 2], [2, 1])
        assert tree_to_list(root) == [1, 2]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
