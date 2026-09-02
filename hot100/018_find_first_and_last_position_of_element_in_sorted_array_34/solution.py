"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the
starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

Example 2:
    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]

Example 3:
    Input: nums = [], target = 0
    Output: [-1,-1]
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # if len(nums) == 1:
        #     return [0, 0] if nums[0] == target else [-1, -1]

        # first , find the left-most idx that equals target
        def findLeft(nums, target):
            final_result = -1
            l = 0
            r = len(nums) -1

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    final_result = mid
                    r = mid - 1

            return final_result


        def findRight(nums, target):
            final_result = -1
            l = 0
            r = len(nums) -1

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    final_result = mid
                    l = mid + 1

            return final_result

        left_most_idx = findLeft(nums, target)
        right_most_idx = findRight(nums, target)
        return [left_most_idx, right_most_idx]

"""
Test case 1:
[2]

Test case 2:
Input: nums = [5,7,7,8,8,10], target = 6

findLeft:
    l = 0
    r = 5
    mid = 2
    nums[mid] = 7 (> target)

    l = 0
    r = 1    [5, 7]
    mid = 0
    nums[mid] = 5 (< target)

    l = 1
    r = 1
    mid = 1
    nums[mid] = 7  (> target)

    r = mid - 1 = 0

    return final_result = -1




Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

l = 0
r = 5
mid = 2
nums[mid] = 7, < target

l = 3
r = 5
mid = 4
nums[mid] = 8 == target
result = mid = 4

r = mid - 1 = 3
l = 3
mid = 3
nums[mid] = 8
result = mid = 3

r = 2
l = 3
break



"""
