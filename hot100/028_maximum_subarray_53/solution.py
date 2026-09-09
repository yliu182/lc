"""
53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return
its sum.

Example 1:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
    Input: nums = [1]
    Output: 1

Example 3:
    Input: nums = [5,4,-1,7,8]
    Output: 23

Constraints:
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
"""

from typing import List

"""
如果之前累积的 sum 对当前数字有帮助，就继续；如果之前的 sum 已经是负担，就从当前数字重新开始。
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        final_result = float('-inf')
        cur_max = float('-inf')

        for n in nums:
            cur_max = max(cur_max + n, n)
            final_result = max(final_result, cur_max)

        return final_result
