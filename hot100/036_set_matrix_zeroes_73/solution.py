"""
73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row
and column to 0's.

You must do it in place.

Example 1:
    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -2^31 <= matrix[i][j] <= 2^31 - 1
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        rows = set()
        cols = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in rows:
            for j in range(n):
                matrix[i][j] = 0


        for j in cols:
            for i in range(m):
                matrix[i][j] = 0

        return


# 这已经是很好的解法，也满足原地修改矩阵的要求，但还能优化为：
# 额外空间：O(1)
# 最优空间思路
# 直接使用矩阵的第一行和第一列作为标记空间。
# 如果发现：
# matrix[i][j] == 0
# 就标记：
# matrix[i][0] = 0
# matrix[0][j] = 0
# 后面根据第一列和第一行的标记，将对应元素清零。
# 不过 matrix[0][0] 同时属于第一行和第一列，无法同时表示两个状态，因此需要两个额外布尔变量：
# first_row_zero
# first_col_zero
# 整体步骤是：
# 1. 记录原始第一行是否有零。
# 2. 记录原始第一列是否有零。
# 3. 遍历除第一行、第一列之外的元素，并在第一行、第一列做标记。
# 4. 根据标记清零内部元素。
# 5. 最后处理第一行和第一列。
# 必须最后处理第一行和第一列，否则提前清零会破坏标记。
# 最优复杂度为：
# 时间：O(m × n)
# 空间：O(1)
# 所以结论是：你的解法时间最优、清晰且正确；如果题目追求严格意义上的最优额外空间，还可以用第一行和第一列作为标记，将 O(m+n) 优化为 O(1)。我没有修改文件。
