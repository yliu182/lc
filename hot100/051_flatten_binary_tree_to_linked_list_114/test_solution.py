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


def flatten_to_list(root):
    """Convert flattened tree to list of values."""
    result = []
    while root:
        assert root.left is None, "Left child should be None after flattening"
        result.append(root.val)
        root = root.right
    return result


@pytest.fixture
def sol():
    return Solution()


class TestFlattenBinaryTree:
    def test_example1(self, sol):
        root = build_tree([1, 2, 5, 3, 4, None, 6])
        sol.flatten(root)
        assert flatten_to_list(root) == [1, 2, 3, 4, 5, 6]

    def test_example2(self, sol):
        root = build_tree([])
        sol.flatten(root)
        assert root is None

    def test_example3(self, sol):
        root = build_tree([0])
        sol.flatten(root)
        assert flatten_to_list(root) == [0]

    def test_left_only(self, sol):
        root = build_tree([1, 2, None, 3])
        sol.flatten(root)
        assert flatten_to_list(root) == [1, 2, 3]

    def test_right_only(self, sol):
        root = build_tree([1, None, 2, None, 3])
        sol.flatten(root)
        assert flatten_to_list(root) == [1, 2, 3]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
