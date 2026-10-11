"""
200. Number of Islands
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally
or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    Output: 1

Example 2:
    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
"""

from typing import List


class Solution:


    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0
        stack = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ret += 1
                    stack.append((i, j))
                    while len(stack) > 0:
                        x, y = stack.pop()
                        grid[x][y] = "0"
                        for direction in directions:
                            dest_i = x + direction[0]
                            dest_j = y + direction[1]
                            if dest_i >= 0 and dest_i < len(grid) and dest_j >= 0 and dest_j < len(grid[0]) and grid[dest_i][dest_j] == "1":
                                stack.append((dest_i, dest_j))
        return ret

    """
    def numIslands(self, grid: List[List[str]]) -> int:

        # dfs(i, j)

        def dfs_swap(row, col, grid, not_flip=False):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0":
                return
            # flip
            grid[row][col] = "0"

            dfs_swap(row+1, col, grid)
            dfs_swap(row, col + 1, grid)
            dfs_swap(row-1, col, grid)
            dfs_swap(row, col - 1, grid)

        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ret += 1
                    dfs_swap(i, j, grid)

        return ret
    """
