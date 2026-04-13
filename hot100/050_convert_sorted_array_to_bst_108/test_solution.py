import pytest
from solution import Solution, TreeNode


def is_bst(node, low=float('-inf'), high=float('inf')):
    if not node:
        return True
    if node.val <= low or node.val >= high:
        return False
    return is_bst(node.left, low, node.val) and is_bst(node.right, node.val, high)


def get_height(node):
    if not node:
        return 0
    return 1 + max(get_height(node.left), get_height(node.right))


def is_balanced(node):
    if not node:
        return True
    left_h = get_height(node.left)
    right_h = get_height(node.right)
    return abs(left_h - right_h) <= 1 and is_balanced(node.left) and is_balanced(node.right)


def inorder(node):
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)


@pytest.fixture
def sol():
    return Solution()


class TestSortedArrayToBST:
    def test_example1(self, sol):
        root = sol.sortedArrayToBST([-10, -3, 0, 5, 9])
        assert is_bst(root)
        assert is_balanced(root)
        assert inorder(root) == [-10, -3, 0, 5, 9]

    def test_example2(self, sol):
        root = sol.sortedArrayToBST([1, 3])
        assert is_bst(root)
        assert is_balanced(root)
        assert inorder(root) == [1, 3]

    def test_single_element(self, sol):
        root = sol.sortedArrayToBST([0])
        assert root.val == 0
        assert root.left is None
        assert root.right is None

    def test_three_elements(self, sol):
        root = sol.sortedArrayToBST([1, 2, 3])
        assert is_bst(root)
        assert is_balanced(root)
        assert inorder(root) == [1, 2, 3]

    def test_seven_elements(self, sol):
        root = sol.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
        assert is_bst(root)
        assert is_balanced(root)
        assert inorder(root) == [1, 2, 3, 4, 5, 6, 7]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
