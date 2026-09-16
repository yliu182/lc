"""
74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:
    - Each row is sorted in non-decreasing order.
    - The first integer of each row is greater than the last integer of the
      previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: true

Example 2:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    Output: false

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -10^4 <= matrix[i][j], target <= 10^4
"""

from typing import List


class Solution:
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

    #     # first find the row using binary search

    #     m = len(matrix)
    #     n = len(matrix[0])

    #     row_left = 0
    #     row_right = m - 1
    #     row_target = -1
    #     while row_left <= row_right:
    #         mid = (row_left + row_right) // 2

    #         # 对于第 mid 行，检查这一行的范围：
    #         # matrix[mid][0]   # 这一行最小值
    #         # matrix[mid][-1]  # 这一行最大值
    #         if target < matrix[mid][0]:
    #             row_right = mid - 1
    #         elif target > matrix[mid][-1]:
    #             row_left = mid + 1
    #         else:
    #             row_target = mid
    #             break

    #     if row_target == -1:
    #         return False

    #     col_left = 0
    #     col_right = n - 1
    #     while col_left <= col_right:
    #         mid = (col_left + col_right) // 2
    #         if target == matrix[row_target][mid]:
    #             return True
    #         elif target < matrix[row_target][mid]:
    #             col_right = mid -1
    #         else:
    #             col_left = mid + 1

    #     return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # assume this matrix is a 1D m x n array
        height = len(matrix)
        width = len(matrix[0])

        left = 0
        right = height * width - 1

        while left <= right:
            mid = (left + right) // 2
            candidate = matrix[mid // width][mid % width]
            if candidate == target:
                return True
            elif target < candidate:
                right = mid - 1
            else:
                left = mid + 1

        return False
