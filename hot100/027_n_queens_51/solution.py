"""
51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.
You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
    Input: n = 4
    Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

Example 2:
    Input: n = 1
    Output: [["Q"]]

Constraints:
    1 <= n <= 9
"""

from typing import List

"""
Similar to permutation kind of problem, consider using DFS (backtrack kind of solution)

def dfs(row):
    if row == n:
        # 找到一个完整 solution
        return

    for col in range(n):
        if 冲突:
            continue

        # choose
        放 Queen
        加入 cols / diag

        dfs(row + 1)

        # undo
        移除 Queen
        从 cols / diag 删除

DFS 并不是暴力生成所有棋盘。它每放一个 Queen，就立刻用这三个条件剪枝：
    col in cols
    row - col in diag1
    row + col in diag2

cols , diag1, diag2 就是三个我们需要维护的 list
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # [[3, 1, 2, 0], [0, 2, 3, 1]]
        solutions = []


        used_cols = set()
        used_diag1 = set()
        used_diag2 = set()
        path = []

        def dfs(
            row_idx, # int, current index of row to process
        ):
            if row_idx == n:
                solutions.append(path.copy())
                return

            for col_idx in range(n):
                if col_idx in used_cols:
                    continue

                if row_idx - col_idx in used_diag1:
                    continue

                if row_idx + col_idx in used_diag2:
                    continue

                used_cols.add(col_idx)
                used_diag1.add(row_idx - col_idx)
                used_diag2.add(row_idx + col_idx)
                path.append(col_idx)

                dfs(row_idx+1)

                used_cols.remove(col_idx)
                used_diag1.remove(row_idx - col_idx)
                used_diag2.remove(row_idx + col_idx)
                path.pop()

        dfs(0)

        final_results = []
        for i, col_ids in enumerate(solutions):
            result = []
            for col_id in col_ids:
                s = ['.'] * n
                s[col_id] = 'Q'
                result.append(''.join(s))
            final_results.append(result)

        return final_results
