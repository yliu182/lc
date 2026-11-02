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

    # def canPartition(self, nums: List[int]) -> bool:
    #     total = sum(nums)
    #     if total % 2 != 0:
    #         return False
    #     target = total // 2
    #     '''
    #     因为不同的选择路径可能到达相同状态：
    #     (index, cur_sum)
    #     例如：
    #     nums = [1, 1, 1]
    #     状态 (index=2, cur_sum=1) 可以通过两种方式到达：
    #     选择第一个 1，跳过第二个 1
    #     跳过第一个 1，选择第二个 1
    #     没有缓存时，该状态后面的所有分支会重复计算。添加缓存后，每个 (index, cur_sum) 只计算一次。
    #     '''
    #     @cache
    #     def dfs(index, cur_sum) -> bool:
    #         if cur_sum == target:
    #             return True
    #         elif cur_sum
    #         if index == len(nums):
    #             return False
    #         return dfs(index + 1, cur_sum + nums[index]) or dfs(index + 1, cur_sum)
    #     return dfs(0, 0)

    # 2D dp knapsack problem
    def canPartition(self, nums: List[int]) -> bool:
        '''

        standard 0-1 problem:
        dp[i][w] if only use the first i elements,  under the capacity constraint of w, what is the maximum value

        dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i-1]] + value[i-1]
        this can be simplified to
            dp[w] = max(dp[w], dp[w-weight] + value)


        But for this problem, we need a differenty definition:
        dp[i][target] whether we can achieve target using first i elements
        '''
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]

        for i in range(1, len(nums) + 1, 1):
            dp[i][0] = True

        for i in range(1, len(nums) + 1, 1):
            for j in range(1, target + 1, 1):
                if j >= nums[i-1]:
                    dp[i][j] = (
                        dp[i-1][j] or dp[i-1][j - nums[i-1]]
                    )
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(nums)][target]




    # def canPartition(self, nums: List[int]) -> bool:
    #     dp[]
