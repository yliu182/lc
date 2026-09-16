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
    # def uniquePaths(self, m: int, n: int) -> int:
    #     def dfs(
    #         r_remain,
    #         d_remain,
    #     ):
    #         if r_remain == 0 and d_remain == 0:
    #             return 1

    #         result = 0
    #         if r_remain > 0:
    #             result += dfs(r_remain - 1, d_remain)

    #         if d_remain > 0:
    #             result += dfs(r_remain, d_remain - 1)

    #         return result

    #     return dfs(m - 1, n - 1)


    # def uniquePaths(self, m: int, n: int) -> int:
    #     # 假设计算：
    #     # dfs(2, 2)
    #     # 递归关系是：
    #     # dfs(2, 2) = dfs(1, 2) + dfs(2, 1)
    #     # 继续展开：
    #     # dfs(1, 2)
    #     # ├── dfs(0, 2)
    #     # └── dfs(1, 1)

    #     # dfs(2, 1)
    #     # ├── dfs(1, 1)
    #     # └── dfs(2, 0)
    #     # 可以看到：
    #     # dfs(1, 1)
    #     # 被计算了两次。网格越大，这种重复越严重。
    #     @cache
    #     def dfs(
    #         r_remain,
    #         d_remain,
    #     ):
    #         if r_remain == 0 or d_remain == 0:
    #             return 1

    #         return dfs(r_remain - 1, d_remain) + dfs(r_remain, d_remain - 1)

    #     return dfs(m - 1, n - 1)

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
