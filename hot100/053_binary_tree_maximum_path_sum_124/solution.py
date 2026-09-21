"""
124. Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent
nodes in the sequence has an edge connecting them. A node can only appear in
the sequence at most once. Note that the path does not need to pass through
the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty
path.

Example 1:
    Input: root = [1,2,3]
    Output: 6
    Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of
    2 + 1 + 3 = 6.

Example 2:
    Input: root = [-10,9,20,null,null,15,7]
    Output: 42
    Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of
    15 + 20 + 7 = 42.

Constraints:
    The number of nodes in the tree is in the range [1, 3 * 10^4].
    -1000 <= Node.val <= 1000
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Yao's original solution, has a bug for all negative inputs
    Each dfs returns the
    (1) max sum of all paths that starts and ends in any nodes of tree
    (2) max sum of all paths that ends in the root node

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return 0, 0
            l_max, l_end_max = dfs(root.left)
            r_max, r_end_max = dfs(root.right)
            new_end_max = max(l_end_max, r_end_max) + root.val
            new_max = max(
                max(l_max, r_max),
                max(l_end_max, 0) + root.val + max(r_end_max, 0)
            )
            return new_max, new_end_max

        max_sum, _ = dfs(root)
        return max_sum
    """

    """
    问题一：空树的最大路径不能是 0
        题目要求路径非空。对于“子树内最大路径”，空树不应该贡献 0，否则它会超过所有负数路径。
        应区分：
            空树内部最大路径：负无穷
            空树向父节点提供的贡献：0

    问题二：向父节点返回的路径可以不选孩子
        new_end_max = max(l_end_max, r_end_max) + root.val
        这强制选择一个孩子。如果两个孩子都是负数，应该一个都不选：

    更清晰的标准写法
        只让 DFS 返回“当前节点向下的最大贡献”，另外维护全局答案

    """
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max = float('-inf')

        def dfs(root):
            nonlocal global_max
            if root is None:
                return 0
            l_end_max = dfs(root.left)
            r_end_max = dfs(root.right)
            # 向父节点返回的单边路径：
            ret = root.val + max(l_end_max, r_end_max, 0)

            # 经过当前节点的完整路径：
            global_max = max(
                root.val + max(l_end_max, 0) + max(r_end_max, 0),
                global_max,
            )

            return ret

        dfs(root)
        return global_max
