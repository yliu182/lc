"""
152. Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find a subarray that has the largest product, and return
the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
    Input: nums = [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.

Example 2:
    Input: nums = [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
    1 <= nums.length <= 2 * 10^4
    -10 <= nums[i] <= 10
    The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""

from typing import List


class Solution:
    """
    这是 yao 写的第一版，但是有个严重的 bug

    def maxProduct(self, nums: List[int]) -> int:
        # the max product of subarray that ends with current idx
        # or starts from the current idx
        if len(nums) == 1:
            return nums[0]

        cur_min_product = nums[0]
        cur_max_product = nums[0]
        global_max = nums[0]

        for x in nums[1:]:
            cur_min_product = min(
                cur_max_product * x,
                cur_min_product * x,
                x
            )
            cur_max_product = max(
                cur_max_product * x,
                cur_min_product * x,
                x
            )
            global_max = max(global_max, cur_max_product)

        return global_max
    """


    def maxProduct(self, nums: List[int]) -> int:
        # the max product of subarray that ends with current idx
        # or starts from the current idx
        if len(nums) == 1:
            return nums[0]

        cur_min_product = nums[0]
        cur_max_product = nums[0]
        global_max = nums[0]

        for x in nums[1:]:
            prev_max = cur_max_product
            prev_min = cur_min_product
            cur_min_product = min(
                prev_max * x,
                prev_min * x,
                x
            )
            cur_max_product = max(
                prev_max * x,
                prev_min * x,
                x
            )
            global_max = max(global_max, cur_max_product)

        return global_max
