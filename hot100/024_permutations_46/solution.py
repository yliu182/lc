"""
46. Permutations

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Example 1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

Example 3:
    Input: nums = [1]
    Output: [[1]]

Constraints:
    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.
"""

from typing import List


class Solution:

    ## More expensive solution
    # def permute(self, nums: List[int]) -> List[List[int]]:

    #     final_results = []
    #     def dfs(
    #         path, # List[int]
    #     ):
    #         if len(path) == len(nums):
    #             final_results.append(path)
    #             return

    #         used = set(path)
    #         for n in nums:
    #             if n not in used:
    #                 dfs(path + [n])

    #     dfs([])
    #     return final_results

    def permute(self, nums: List[int]) -> List[List[int]]:
        final_results = []
        used = set()
        path = []

        def dfs():
            if len(path) == len(nums):
                final_results.append(path.copy())
                return

            for n in nums:
                if n not in used:
                    path.append(n)
                    used.add(n)
                    dfs()
                    path.pop()
                    used.remove(n)

        dfs()
        return final_results
