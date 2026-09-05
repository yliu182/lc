"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be if it were
inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2

Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1

Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4
"""

from typing import List

class Solution:
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     l = 0
    #     r = len(nums) - 1
    #     while l <= r:
    #         m = (l + r) // 2
    #         if nums[m] == target:
    #             return m
    #         elif target < nums[m] and m > 0 and target > nums[m-1]:
    #             return m
    #         elif target < nums[m-1]:
    #             r = m - 1
    #         elif target > nums[m] and m < len(nums) - 1 and target < nums[m+1]:
    #             return m+1
    #         else:
    #             l = m + 1

    #     if m == len(nums) - 1:
    #         return len(nums)
    #     return m

    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif target < nums[m]:
                r = m -1
            else:
                l = m + 1

        return l

"""
input  = [1,3,5,6],
target = 7

l = 0
r = 3
m = 1

nums[m] = 3 < target
the results should be in rignt side, throw away left side

l = m + 1 = 2
m = 2
nums[m] = 5
l = m+1 = 3
r = 3


m = 3
l = 4
m = 3




"""
