"""
78. Subsets

Given an integer array nums of unique elements, return all possible subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in
any order.

Example 1:
    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
    Input: nums = [0]
    Output: [[],[0]]

Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.
"""

from typing import List


class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     solution = []

    #     """
    #     当前时间复杂度
    #     一共有 2^n个子集。
    #     每个叶子处，你需要遍历长度为 n 的 path： for i, p in enumerate(path):
    #     因此时间复杂度是： O(n × 2^n)
    #     """
    #     def dfs(path):
    #         if len(path) == len(nums):
    #             candidate = []
    #             for i, p in enumerate(path):
    #                 if p == 1:
    #                     candidate.append(nums[i])
    #             solution.append(candidate)
    #             return

    #         dfs(path + [0]) # exclude the next elements in nums
    #         dfs(path + [1]) # include

    #     dfs([])
    #     return solution

    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution = []
        """
        就是经典回溯：
        做出选择
        递归
        撤销选择

        这种方式的优点是：
        - 不需要维护 0/1 标记
        - 不需要在叶子重新遍历标记构造子集
        - 不需要每次递归都执行 path + [...]
        - 递归含义更直接

        不过叶子处的：path.copy()
        """

        path = []
        solution = []
        def dfs(i):
            # i is the next index to process
            if i == len(nums):
                solution.append(path.copy())
                return

            # option 1, does not include nums[i] into the path
            dfs(i+1)

            # option 2, include nums[i] into the path
            path.append(nums[i])
            dfs(i+1)
            path.pop()

        dfs(0)
        return solution
