"""
189. Rotate Array
https://leetcode.com/problems/rotate-array/

Given an integer array nums, rotate the array to the right by k steps, where k is
non-negative.

Example 1:
    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]

Example 2:
    Input: nums = [-1,-100,3,99], k = 2
    Output: [3,99,-1,-100]

Constraints:
    1 <= nums.length <= 10^5
    -2^31 <= nums[i] <= 2^31 - 1
    0 <= k <= 10^5

Follow up:
    Try to come up with as many solutions as you can. There are at least three different
    ways to solve this problem.
    Could you do it in-place with O(1) extra space?
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        例如：
            nums = [1,2,3,4,5,6,7]
            k = 3
            目标是把数组分成两部分：
            A = [1,2,3,4]
            B = [5,6,7]

            目标：B + A
            执行三次反转：
            1. 反转整个数组
            [7,6,5,4,3,2,1]

            2. 反转前 k 个元素
            [5,6,7,4,3,2,1]

            3. 反转剩余元素
            [5,6,7,1,2,3,4]
        """
        shift = k % len(nums)
        size = len(nums)
        # swap [0, len(shfit)) , [shift, len(n)), [0, len(n))
        self._swap(nums, 0, size)
        self._swap(nums, 0, shift)
        self._swap(nums, shift, size)

    def _swap(self, nums, start, end):
        i = start
        j = end - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


    """
    复杂度：
        时间：O(n)
        空间：O(n)
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        rotated = [0] * n
        for i, value in enumerate(nums):
            rotated[(i + k) % n] = value

        nums[:] = rotated
    """

    """
    O(n) and O(1)

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        start = 0
        rotated = 0
        while rotated < n:
            cur = start
            prev_val = nums[cur]
            while True:
                next_idx = (cur + k) % n
                nums[next_idx], prev_val = prev_val, nums[next_idx]
                rotated += 1
                cur = next_idx
                if cur == start:
                    break
            start += 1
    """
