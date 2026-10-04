"""
153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:
    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.
    [7,0,1,2,4,5,6]
    [6,7,0,1,2,4,5]
    [5,6,7,0,1,2,4]


Given the sorted rotated array nums of unique elements, return the minimum element of
this array.

You must write an algorithm that runs in O(log n) time.

Example 1:
    Input: nums = [3,4,5,1,2]
    Output: 1

Example 2:
    Input: nums = [4,5,6,7,0,1,2]
    Output: 0

Example 3:
    Input: nums = [11,13,15,17]
    Output: 11

Constraints:
    n == nums.length
    1 <= n <= 5000
    -5000 <= nums[i] <= 5000
    All the integers of nums are unique.
    nums is sorted and rotated between 1 and n times.
"""

from typing import List


# Binary search loop conditions:
#
# 1. Search for an exact target with a closed interval [left, right]:
#       while left <= right
#    When left == right, one element still needs to be checked. Exclude mid
#    after checking it with left = mid + 1 or right = mid - 1. The search
#    ends when left > right and the interval is empty.
#
# 2. Find a boundary/minimum while keeping the answer in [left, right]:
#       while left < right
#    Stop when left == right and only one candidate remains. Preserve mid
#    when it may be the answer with right = mid; otherwise use left = mid + 1.
#
# If an update uses left = mid with left < right, use the upper midpoint
# left + (right - left + 1) // 2 to avoid an infinite loop.
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # a variation of binary search
        left = 0
        right = len(nums) - 1

        while left < right:
            # mid = (left + right) // 2 可能会溢出
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
