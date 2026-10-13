"""
215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:
    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5

Example 2:
    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4

Constraints:
    1 <= k <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
"""
import random
from typing import List


class Solution:

    """
    This is basically quickSort
    [l, i) stores processed numbers that is smaller than pivot
    [i, j) stores processed numbers that is bigger than pivot
    [j, r) stored unprocessed numbers
    nums[r] is the pivot

    Best video to explain this:
        https://www.youtube.com/watch?v=duln2xAZhBA
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums) - 1
        target_idx = len(nums) - k

        while l <= r:
            pivot_idx = random.randint(l, r)
            pivot = nums[pivot_idx]
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
            i = l
            for j in range(l, r):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[r], nums[i] = nums[i], nums[r]

            if i == target_idx:
                return nums[i]
            elif target_idx > i:
                l = i + 1
            else:
                r = i - 1
