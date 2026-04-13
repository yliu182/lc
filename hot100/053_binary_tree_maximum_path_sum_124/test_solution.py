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


class TestMaxPathSum:
    def test_example1(self, sol):
        root = build_tree([1, 2, 3])
        assert sol.maxPathSum(root) == 6

    def test_example2(self, sol):
        root = build_tree([-10, 9, 20, None, None, 15, 7])
        assert sol.maxPathSum(root) == 42

    def test_single_node(self, sol):
        root = build_tree([5])
        assert sol.maxPathSum(root) == 5

    def test_all_negative(self, sol):
        root = build_tree([-3, -2, -1])
        assert sol.maxPathSum(root) == -1

    def test_negative_root(self, sol):
        root = build_tree([-1, 2, 3])
        assert sol.maxPathSum(root) == 4


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
