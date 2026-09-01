"""
31. Next Permutation

A permutation of an array of integers is an arrangement of its members into a
sequence or linear order.

The next permutation of an array of integers is the next lexicographically
greater permutation of its integer.

If such arrangement is not possible, the array must be rearranged as the lowest
possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

Example 1:
    Input: nums = [1,2,3]
    Output: [1,3,2]

Example 2:
    Input: nums = [3,2,1]
    Output: [1,2,3]

Example 3:
    Input: nums = [1,1,5]
    Output: [1,5,1]
"""

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            p = len(nums) - 1 - i
            q = p+1
            # find the mininum element that is bigger than nums[p]
            # in the range of [q, q+1, ..., len(nums)-1]
            min_val = float('inf')
            min_idx = None
            while q < len(nums):
                if nums[q] > nums[p] and nums[q] < min_val:
                    min_val = min(min_val, nums[q])
                    min_idx = q
                q += 1

            if min_idx is not None:
                # swap nums[p] and nums[min_idx] in place
                nums[min_idx] = nums[p]
                nums[p] = min_val
                return

        return nums.sort()
