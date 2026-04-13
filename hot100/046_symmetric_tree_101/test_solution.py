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


class TestSymmetricTree:
    def test_example1(self, sol):
        root = build_tree([1, 2, 2, 3, 4, 4, 3])
        assert sol.isSymmetric(root) is True

    def test_example2(self, sol):
        root = build_tree([1, 2, 2, None, 3, None, 3])
        assert sol.isSymmetric(root) is False

    def test_single_node(self, sol):
        root = build_tree([1])
        assert sol.isSymmetric(root) is True

    def test_two_levels_asymmetric(self, sol):
        root = build_tree([1, 2, 3])
        assert sol.isSymmetric(root) is False

    def test_symmetric_with_nulls(self, sol):
        root = build_tree([1, 2, 2, None, 3, 3, None])
        assert sol.isSymmetric(root) is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
