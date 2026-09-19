"""
94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes'
values.

Example 1:
    Input: root = [1,null,2,3]
    Output: [1,3,2]

Example 2:
    Input: root = []
    Output: []

Example 3:
    Input: root = [1]
    Output: [1]

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        solution = []
        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            solution.append(node.val)
            dfs(node.right)

        dfs(root)
        return solution

“”“
DFS traversal: Time O(n), Space O(h), where h is the height of the tree. For a balanced tree it's O(log n), and worst case it's O(n).

        1
       / \
      2   3
     / \
    4   5

所以内存中的 call stack 是：
┌──────────┐
│ dfs(4)   │  ← 当前执行
├──────────┤
│ dfs(2)   │  ← 等待
├──────────┤
│ dfs(1)   │  ← 等待
└──────────┘
”“”
