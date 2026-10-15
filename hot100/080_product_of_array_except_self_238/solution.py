"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to the
product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]

Constraints:
    2 <= nums.length <= 10^5
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array
does not count as extra space for space complexity analysis.)
"""

from typing import List


class Solution:
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1] * len(nums)
        for i in range(1, len(nums), 1):
            left_product[i] = nums[i-1] * left_product[i-1]

        ret = [0] * len(nums)
        right_product = 1
        for j in range(len(nums) - 1 , 0, -1):
            ret[j] = left_product[j] * right_product
            right_product *= nums[j]

        ret[0] = right_product
        return ret
    '''

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1] * len(nums)
        # first pass, calculate the left-side and temporarily store in result array
        for i in range(1, len(nums), 1):
            ret[i] = nums[i-1] * ret[i-1]
        right_product = 1
        for j in range(len(nums) - 1 , 0, -1):
            ret[j] = ret[j] * right_product
            right_product *= nums[j]
        ret[0] = right_product
        return ret
