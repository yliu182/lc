"""
62. Unique Paths

There is a robot on an m x n grid. The robot is initially located at the
top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right
corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right
at any point in time.

Given the two integers m and n, return the number of possible unique paths that
the robot can take to reach the bottom-right corner.

Example 1:
    Input: m = 3, n = 7
    Output: 28

Example 2:
    Input: m = 3, n = 2
    Output: 3

Constraints:
    1 <= m, n <= 100
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(
            r_remain,
            d_remain,
        ):
            if r_remain == 0 and d_remain == 0:
                return 1

            result = 0
            if r_remain > 0:
                result += dfs(r_remain - 1, d_remain)

            if d_remain > 0:
                result += dfs(r_remain, d_remain - 1)

            return result

        return dfs(m - 1, n - 1)
