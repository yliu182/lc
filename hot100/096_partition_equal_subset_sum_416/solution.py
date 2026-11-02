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
        target = total // 2
        '''
        因为不同的选择路径可能到达相同状态：
        (index, cur_sum)
        例如：
        nums = [1, 1, 1]
        状态 (index=2, cur_sum=1) 可以通过两种方式到达：
        选择第一个 1，跳过第二个 1
        跳过第一个 1，选择第二个 1
        没有缓存时，该状态后面的所有分支会重复计算。添加缓存后，每个 (index, cur_sum) 只计算一次。
        '''
        @cache
        def dfs(index, cur_sum) -> bool:
            if cur_sum == target:
                return True
            elif cur_sum
            if index == len(nums):
                return False

            return dfs(index + 1, cur_sum + nums[index]) or dfs(index + 1, cur_sum)

        return dfs(0, 0)
