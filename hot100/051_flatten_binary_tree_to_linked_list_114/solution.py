"""
114. Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":
- The "linked list" should use the same TreeNode class where the right child
  pointer points to the next node in the list and the left child pointer is
  always null.
- The "linked list" should be in the same order as a pre-order traversal of
  the binary tree.

Example 1:
    Input: root = [1,2,5,3,4,null,6]
    Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
    Input: root = []
    Output: []

Example 3:
    Input: root = [0]
    Output: [0]

Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def flatten(self, root: Optional[TreeNode]) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     def dfs(root):
    #         # return the tail of the tree node (preorder)
    #         if root is None:
    #             return None

    #         left_end = dfs(root.left)
    #         right_end = dfs(root.right)
    #         if left_end:
    #             old_right = root.right
    #             root.right = root.left
    #             root.left = None
    #             left_end.right = old_right
    #         return right_end or left_end or root

    #     dfs(root)

    def flatten(self, root: Optional[TreeNode]) -> None:
        prev = None
        # prev 永远表示：当前 node 后面应该接的那个节点
        def dfs(root):
            nonlocal prev

            if root is None:
                return None

            dfs(root.right)
            dfs(root.left)

            root.right = prev
            root.left = None
            prev = root

        dfs(root)
