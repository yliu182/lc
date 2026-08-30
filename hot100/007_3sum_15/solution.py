"""
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

Example 2:
    Input: nums = [0,1,1]
    Output: []

Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                cur_sum = nums[l] + nums[r] + nums[i]
                if cur_sum < 0:
                    l += 1
                elif cur_sum > 0:
                    r -= 1
                else:
                    results.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

        return results

"""
Example 1:
    Input: nums = [-1,0,1,2,-1,-4]

                  [-4, -1, -1, 0, 1, 2]

                           i
                   0                 5

    cur_sum = 0

    [-1, -1, 2]

    Output: [[-1,-1,2],[-1,0,1]]

Example 2:
    Input: nums = [0,1,1]
    Output: []

Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]

cur_sum = 0
l = 2
r = 1
"""
