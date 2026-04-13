import pytest
from collections import deque
from solution import Codec, TreeNode


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


def tree_to_list(root):
    """Convert tree to level-order list for comparison."""
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
def codec():
    return Codec()


def test_example1(codec):
    root = build_tree([1, 2, 3, None, None, 4, 5])
    data = codec.serialize(root)
    result = codec.deserialize(data)
    assert tree_to_list(result) == [1, 2, 3, None, None, 4, 5]


def test_example2(codec):
    root = build_tree([])
    data = codec.serialize(root)
    result = codec.deserialize(data)
    assert tree_to_list(result) == []


def test_example3(codec):
    root = build_tree([1])
    data = codec.serialize(root)
    result = codec.deserialize(data)
    assert tree_to_list(result) == [1]


def test_left_skewed(codec):
    root = build_tree([1, 2, None, 3])
    data = codec.serialize(root)
    result = codec.deserialize(data)
    assert tree_to_list(result) == [1, 2, None, 3]


def test_negative_values(codec):
    root = build_tree([-1, -2, -3])
    data = codec.serialize(root)
    result = codec.deserialize(data)
    assert tree_to_list(result) == [-1, -2, -3]


def test_roundtrip_string(codec):
    root = build_tree([1, 2, 3])
    data = codec.serialize(root)
    assert isinstance(data, str)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
