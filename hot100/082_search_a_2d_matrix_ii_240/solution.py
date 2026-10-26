"""
240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value target in an m x n integer
matrix. This matrix has the following properties:
    - Integers in each row are sorted in ascending from left to right.
    - Integers in each column are sorted in ascending from top to bottom.

Example 1:
    Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
    Output: true

Example 2:
    Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
    Output: false

Constraints:
    - m == matrix.length
    - n == matrix[i].length
    - 1 <= n, m <= 300
    - -10^9 <= matrix[i][j] <= 10^9
"""

from typing import List


'''
[
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]
]
'''
class Solution:
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     left = 0
    #     right = len(matrix) - 1
    #     while left < right:
    #         mid = (left + right) // 2
    #         if matrix[mid][0] == target:
    #             return True
    #         elif matrix[mid][0] < target:
    #             left = mid
    #         else:
    #             right = mid - 1

    #     # mid if the target row (if target ever exists)
    #     row = mid

    #     left = 0
    #     right = len(matrix[0]) - 1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if matrix[row][mid] == target:
    #             return True
    #         elif matrix[row][mid] < target:
    #             left = mid + 1
    #         else:
    #             right = mid - 1

    #     return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0
        c = len(matrix[0]) - 1
        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r += 1
            else:
                c -= 1
        return False
