"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

Example 2:
    Input: nums = [0]
    Output: [0]

Constraints:
    - 1 <= nums.length <= 10^4
    - -2^31 <= nums[i] <= 2^31 - 1
"""

from typing import List


class Solution:
    '''
    推荐使用快慢指针，核心是把所有非零元素稳定地移动到数组前面。
    - fast 负责从左到右扫描每个元素。
    - slow 指向下一个非零元素应该放置的位置。
    - 当 fast 遇到非零元素时，把它放到 slow 的位置，然后让 slow 向右移动。
    - 遇到零时，slow 不动，fast 继续寻找下一个非零元素。
    - 因为非零元素按照原来的扫描顺序依次放置，所以相对顺序不会改变。
    '''
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0 # next candidate place to put non-"0" element
        fast = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1

        for i in range(slow, len(nums)):
            nums[i] = 0

        return nums
