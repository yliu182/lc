"""
79. Word Search

Given an m x n grid of characters board and a string word, return true if word
exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring. The same letter cell
may not be used more than once.

Example 1:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: true

Example 2:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    Output: true

Example 3:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    Output: false

Constraints:
    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.
"""

from typing import List

class Solution:
    """
    dfs(row, col, index)
    表示：
    当前位于 board[row][col]，尝试匹配 word[index] 以及后面的字符。
    """

    #### First version, contains bugs
    # def exist(self, board: List[List[str]], word: str) -> bool:

    #     visited = [[0] * len(board[0]) for _ in range(len(board))] # List[List[int]] 0 or 1
    #     solution = False

    #     def dfs(row, col, index):
    #         if index == len(word):
    #             solution = True
    #             return

    #         if row < 0 or row >= len(board):
    #             return

    #         if col < 0 or col >= len(board[0]):
    #             return

    #         if visited[row][col] == 1:
    #             return

    #         if board[row][col] == word[index]:
    #             visited[row][col] = 1
    #             # try to move to (row+1, col)
    #             dfs(row+1, col, index + 1)
    #             dfs(row-1, col, index + 1)
    #             dfs(row, col + 1, index + 1)
    #             dfs(row, col - 1, index + 1)
    #             visited[row][col] = 0

    #     for i in range(len(board)):
    #         for j in range(len(board[0])):
    #             dfs(i, j, 0)

    #     return solution


    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = [[0] * len(board[0]) for _ in range(len(board))] # List[List[int]] 0 or 1
        solution = False

        def dfs(row, col, index):
            if index == len(word):
                return True

            if row < 0 or row >= len(board):
                return False

            if col < 0 or col >= len(board[0]):
                return False

            if visited[row][col] == 1:
                return False

            if board[row][col] == word[index]:
                visited[row][col] = 1
                # try to move to (row+1, col)
                if dfs(row+1, col, index + 1):
                    return True
                if dfs(row-1, col, index + 1):
                    return True
                if dfs(row, col + 1, index + 1):
                    return True
                if dfs(row, col - 1, index + 1):
                    return True
                visited[row][col] = 0
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
