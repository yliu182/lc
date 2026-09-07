"""
41. First Missing Positive

Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
    Input: nums = [1,2,0]
    Output: 3

Example 2:
    Input: nums = [3,4,-1,1]
    Output: 2

Example 3:
    Input: nums = [7,8,9,11,12]
    Output: 1

Constraints:
    1 <= nums.length <= 10^5
    -2^31 <= nums[i] <= 2^31 - 1
"""

from typing import List


class Solution:
    """
    uses O(1) auxiliary space.
       - likely to use in-place SWAP to put data into list

    assume n = len(nums)
    the answer must be an integer in the range of [1, n+1]

    sort the nums in an efficient way

    sort:    O(n log n) complexity

    Sorting gives me a simple O(n log n) solution, but since the problem requires O(n), I'll need to use the array itself to encode whether each value from 1 to n exists




    while the current element is not placed into its desired position:
        swap

    最容易漏掉的是这个条件：nums[nums[i] - 1] != nums[i], 它是为了处理重复数字。
    如果没有这个条件, 你会一直：swap 1 和 1

    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i, val in enumerate(nums):
            cur = val
            while cur > 0 and cur <= n:
                target_pos = cur - 1
                cur, nums[target_pos] = nums[target_pos], cur
                if nums[target_pos] == cur:
                    break

        for i, n in enumerate(nums):
            if n != i+1:
                return i+1

        return n+1
