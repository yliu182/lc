"""
437. Path Sum III

Given the root of a binary tree and an integer targetSum, return the number of
paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go
downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:
    Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
    Output: 3
    Explanation: The paths that sum to 8 are: 5->3, 5->2->1, -3->11

Example 2:
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    Output: 3

Constraints:
    - The number of nodes in the tree is in the range [0, 1000].
    - -10^9 <= Node.val <= 10^9
    - -1000 <= targetSum <= 1000
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    '''
    双重 DFS 把问题拆成两层：
    1. 外层 DFS：枚举每个节点作为路径起点。
    2. 内层 DFS：统计从该节点出发、向下延伸的合法路径数量。
    '''
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def start_from(node, target):
            if node is None:
                return 0
            ans = 1 if node.val == target else 0
            ans += start_from(node.left, target-node.val)
            ans += start_from(node.right, target-node.val)
            return ans

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            ans = dfs(node.left) + dfs(node.right) + start_from(node, targetSum)
            return ans

        return dfs(root)
