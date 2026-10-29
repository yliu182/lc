"""
337. House Robber III

The thief has found himself a new place for his thievery again. There is only one
entrance to this area, called root. Besides the root, each house has one and only
one parent house. After a tour, the smart thief realized that all houses in this
place form a binary tree. It will automatically contact the police if two
directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief
can rob without alerting the police.

Example 1:
    Input: root = [3,2,3,null,3,null,1]
    Output: 7
    Explanation: 3 + 3 + 1 = 7

Example 2:
    Input: root = [3,4,5,1,3,null,1]
    Output: 9
    Explanation: 4 + 5 = 9

Constraints:
    - The number of nodes in the tree is in the range [1, 10^4].
    - 0 <= Node.val <= 10^4
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''
    Version 1 is not efficient, because each node was processed by dfs functions multiple times

    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs_with_root(root: TreeNode) -> int:
            if root is None:
                return 0
            return dfs_no_root(root.left) + root.val + dfs_no_root(root.right)

        def dfs_no_root(root: TreeNode) -> int:
            if root is None:
                return 0
            return max(dfs_no_root(root.left), dfs_with_root(root.left)) + max(dfs_no_root(root.right), dfs_with_root(root.right))

        return max(dfs_with_root(root), dfs_no_root(root))
    '''


    """
    If I want to be more efficient, we can add cache for each dfs function if we intentionally call it
    more than once.

    @cache
    def dfs()
    """
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root: TreeNode) -> int:
            if root is None:
                return 0, 0

            left_with_root, left_no_root = dfs(root.left)
            right_with_root, right_no_root = dfs(root.right)

            max_with_root = left_no_root + right_no_root + root.val
            max_no_root = max(left_with_root, left_no_root) + max(right_with_root, right_no_root)
            return max_with_root, max_no_root

        max_with_root, max_no_root = dfs(root)
        return max(max_with_root, max_no_root)
