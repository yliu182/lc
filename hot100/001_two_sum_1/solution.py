"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

You can return the answer in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]
"""

from typing import List

"""

nums =         [3, 2, 4]
                   i

sorted_nums =  [2, 3, 4]
                i

"""
class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     if len(nums) == 0:
    #         return []

    #     # sort the list, while keep the index
    #     num_tups = [(nums[i], i) for i in range(len(nums))]
    #     num_tups.sort(key = lambda x: x[0])
    #     l = 0
    #     r = len(num_tups) - 1
    #     while l < r:
    #         s = num_tups[l][0] + num_tups[r][0]
    #         if s == target:
    #             return [num_tups[l][1], num_tups[r][1]]
    #         elif s < target:
    #             l += 1
    #         else:
    #             r -= 1

    #     return []


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1:
            return nums

        sorted_nums = []
        for i, v in enumerate(nums):
            sorted_nums.append((v, i))
        sorted_nums.sort(key=lambda x : x[0])
        l = 0
        r = len(sorted_nums) - 1
        while l < r:
            s = sorted_nums[l][0] + sorted_nums[r][0]
            if s == target:
                return [sorted_nums[l][1], sorted_nums[r][1]]
            elif s < target:
                l = l + 1
            else:
                r = r - 1

        return []
