"""
98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree
(BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's
  key.
- The right subtree of a node contains only nodes with keys greater than the
  node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
    Input: root = [2,1,3]
    Output: true

Example 2:
    Input: root = [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
    The number of nodes in the tree is in the range [1, 10^4].
    -2^31 <= Node.val <= 2^31 - 1
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Yao's original recursive solution
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:

    #     def dfs(node):
    #         if node is None:
    #             return None, None, True

    #         ret_max = node.val
    #         ret_min = node.val

    #         left_max, left_min, left_is_bst = dfs(node.left)
    #         right_max, right_min, right_is_bst = dfs(node.right)
    #         ret = left_is_bst and right_is_bst
    #         if node.left is not None:
    #             ret = ret and (node.val > left_max)
    #             ret_min = left_min
    #         if right_min is not None:
    #             ret = ret and (node.val < right_min)
    #             ret_max = right_max
    #         return ret_max, ret_min, ret

    #     _, _, is_bst = dfs(root)
    #     return is_bst

    # recursive solution 2, where we do an inorder traversal
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # do an inorder traversal using recursive
        solution = []
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            solution.append(root.val)
            dfs(root.right)
            return

        dfs(root)
        for i in range(len(solution) - 1):
            if solution[i] >= solution[i+1]:
                return False
        return True
