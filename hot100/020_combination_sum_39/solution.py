"""
39. Combination Sum

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers
sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen
numbers is different.

Example 1:
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]

Example 2:
    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
    Input: candidates = [2], target = 1
    Output: []
"""

from typing import List


"""
BFS type solution

bt(
    path, # [2, 2, 2]
    target, #2
    solution, # [[]]
)

how to dedup ?
(1) first construct solution, and then dedup
(2) dedup while construct "solution"

"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final_solution = [] # list of tuple
        def bt(candidates, path, target, solution):
            if target < 0:
                return
            if target == 0:
                path.sort()
                t = tuple(path)
                if t not in solution:
                    solution.append(t)
                return

            for c in candidates:
                if c <= target:
                    bt(candidates, path + [c], target - c, solution)

        bt(candidates, [], target, final_solution)

        return [list(t) for t in final_solution]
