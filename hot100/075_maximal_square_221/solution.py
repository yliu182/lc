"""
221. Maximal Square
https://leetcode.com/problems/maximal-square/

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing
only 1's and return its area.

Example 1:
    Input: matrix = [["1","0","1","0","0"],
                     ["1","0","1","1","1"],
                     ["1","1","1","1","1"],
                     ["1","0","0","1","0"]]
    Output: 4

Example 2:
    Input: matrix = [["0","1"],["1","0"]]
    Output: 1

Example 3:
    Input: matrix = [["0"]]
    Output: 0

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 300
    matrix[i][j] is '0' or '1'.
"""

from typing import List


class Solution:
    """
    推荐使用二维动态规划。
    - 定义状态：dp[i][j] 表示以位置 (i, j) 为右下角、且全部由 1 组成的最大正方形边长。
    - 如果当前格子是 0，则 dp[i][j] = 0。
    - 如果当前格子是 1，它能扩展多大取决于三个位置：正上方、正左方、左上方。取三者最小边长再加 1。
    - 为什么取最小值：扩大正方形时，这三个方向必须同时满足条件，最短的一边决定能扩展的大小。
    - 第一行和第一列只能形成边长为 0 或 1 的正方形。
    - 遍历过程中记录最大边长，最终返回最大边长 × 最大边长。
    时间复杂度为 O(mn)，空间复杂度为 O(mn)，后续还可以优化为 O(n)。
    """
    """
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n_row = len(matrix)
        n_col = len(matrix[0])

        dp = [[0] * n_col for _ in range(n_row)]
        # initialization
        ret = 0
        for i in range(n_row):
            dp[i][0] = 1 if matrix[i][0] == "1" else 0
            if dp[i][0] == 1:
                ret = 1

        for j in range(n_col):
            dp[0][j] = 1 if matrix[0][j] == "1" else 0
            if dp[0][j] == 1:
                ret = 1

        for i in range(1, n_row, 1):
            for j in range(1, n_col, 1):
                """
                dp[i-1][j-1] dp[i-1][j]
                dp[i][j-1]   dp[i][j]
                """
                if matrix[i][j] == "0":
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                ret = max(ret, dp[i][j])
        return ret * ret
    """

    """
    1. DP 数组
    - 之前：二维 dp[i][j]，保存所有格子的结果。
    - 优化后：一维 dp[j]，只保存上一行和当前行需要的数据。
    2. 三个相邻状态
    - top = dp[j]：更新前表示上方。
    - dp[j - 1]：更新后表示左方。
    - top_left：保存更新前的左上方。
    3. 边界处理
    - 之前需要单独初始化第一行和第一列。
    - 优化后使用长度为 n_col + 1 的数组，额外的 0 作为哨兵，不需要单独初始化。
    4. 复杂度
    - 两者时间都是 O(mn)。
    - 空间从 O(mn) 降为 O(n)。
    """
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n_col = len(matrix[0])
        dp = [0] * (n_col + 1)
        max_side = 0

        for row in matrix:
            top_left = 0

            for j in range(1, n_col + 1):
                top = dp[j]

                if row[j - 1] == "1":
                    dp[j] = min(top_left, top, dp[j - 1]) + 1
                    max_side = max(max_side, dp[j])
                else:
                    dp[j] = 0

                top_left = top

        return max_side * max_side
