"""
96. Unique Binary Search Trees

Given an integer n, return the number of structurally unique BST's (binary
search trees) which has exactly n nodes of unique values from 1 to n.

Example 1:
    Input: n = 3
    Output: 5

Example 2:
    Input: n = 1
    Output: 1

Constraints:
    1 <= n <= 19
"""
from collections import defaultdict

class Solution:
    def numTrees(self, n: int) -> int:
        dp = defaultdict(int) # dp[i]: the number of options with i nodes in total
        dp[0] = 1
        dp[1] = 1

        # 1,...i-1      i       i+1, ... n

        # dp[2]
        # dp[2] = dp[1] + dp[0] = 2
        # dp[3] = dp[0] * dp[2] + dp[1] * dp[1]  + dp[2] * dp[0] = 1 * 2 + 1 * 1 + 1 * 2 = 5
        #          1 be root       2 be root.       3 being root

        for i in range(2, n+1):
            for r in range(1, i+1):
                # [1, 2, ... r-1] in left subtree,  r is root,  [r+1, ...., i] being right sub-tree
                dp[i] += dp[r-1] * dp[i - r]

        return dp[n]
