"""
198. House Robber
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. Each house has a
certain amount of money stashed, the only constraint stopping you from robbing each of
them is that adjacent houses have security systems connected and it will automatically
contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the
maximum amount of money you can rob tonight without alerting the police.

Example 1:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3). Total = 4.

Example 2:
    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), house 3 (money = 9) and house 5 (money = 1). Total = 12.

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 400
"""

from functools import cache
from typing import List


class Solution:
    # def rob(self, nums: List[int]) -> int:

    #     @cache
    #     def dfs(idx):
    #         if idx >= len(nums):
    #             return 0
    #         max_result = max(
    #             nums[idx] + dfs(idx + 2),
    #             dfs(idx+1)
    #         )
    #         return max_result

    #     return dfs(0)


    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        size = len(nums)
        if size <= 1:
            return nums[0]
        elif size == 2:
            return max(nums[0], nums[1])

        dp[size - 1] = nums[size-1]
        dp[size - 2] = max(nums[size - 1], nums[size - 2])

        for i in range(size - 3, -1, -1):
            dp[i] = max(
                dp[i+1],
                dp[i+2] + nums[i],
            )

        return dp[0]
