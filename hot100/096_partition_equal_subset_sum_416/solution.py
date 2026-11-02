"""
416. Partition Equal Subset Sum

Given an integer array nums, return true if you can partition the array into two
subsets such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:
    Input: nums = [1,5,11,5]
    Output: true
    Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
    Input: nums = [1,2,3,5]
    Output: false

Constraints:
    - 1 <= nums.length <= 200
    - 1 <= nums[i] <= 100
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total / 2

        def dfs(index, cur_sum) -> bool:
            if cur_sum == target:
                return True
            if index == len(nums):
                return False

            return dfs(index + 1, cur_sum + nums[index]) or dfs(index + 1, cur_sum)

        return dfs(0, 0)
