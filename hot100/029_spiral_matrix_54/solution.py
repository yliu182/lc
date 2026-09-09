"""
54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]

Example 2:
    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100
"""

from typing import List


"""
维护 四个边界
→ top row
↓ right col
← bottom row
↑ left col
走完一条边，就把对应边界往里面缩一格。


"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        output = []
        while top <= bottom and left <= right:
            # → top row
            for i in range(left, right+1, 1):
                output.append(matrix[top][i])
            top += 1

            # ↓ right col
            for i in range(top, bottom+1, 1):
                output.append(matrix[i][right])
            right -= 1

            if bottom >= top:
                # ← bottom row
                for i in range(right, left-1, -1):
                    output.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                # ↑ left col
                for i in range(bottom, top-1, -1):
                    output.append(matrix[i][left])
                left += 1

        return output
