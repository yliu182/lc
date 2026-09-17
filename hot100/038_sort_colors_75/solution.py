"""
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them
in-place so that objects of the same color are adjacent, with the colors in the
order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and
blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
    Input: nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]

Example 2:
    Input: nums = [2,0,1]
    Output: [0,1,2]

Constraints:
    n == nums.length
    1 <= n <= 300
    nums[i] is either 0, 1, or 2.
"""

from typing import List
from collections import defaultdict

class Solution:

    # easy solution
    # 时间：O(n)
    # 额外空间：O(1)
    # def sortColors(self, nums: List[int]) -> None:
    #     cnt_map = defaultdict(int)
    #     for n in nums:
    #         cnt_map[n] += 1

    #     cur_pos = 0
    #     for _ in range(cnt_map[0]):
    #         nums[cur_pos] = 0
    #         cur_pos += 1

    #     for _ in range(cnt_map[1]):
    #         nums[cur_pos] = 1
    #         cur_pos += 1

    #     for _ in range(cnt_map[2]):
    #         nums[cur_pos] = 2
    #         cur_pos += 1

    def sortColors(self, nums: List[int]) -> None:
        """
        left      i       right
         ↓        ↓       ↓
[ 0 0 0 | 1 1 1 | ? ? ? ? ? | 2 2 2 ]
  已搞定   已搞定    待检查       已搞定


  [0 区域] [1 区域] [未知区域] [2 区域]
           ↑        ↑
          left      i
                            ↑
                            right (the expected position of next 2)
        """

        left = 0
        i = 0
        right = len(nums) - 1

        while i <= right:
            if nums[i] == 0:
                # swap nums[left] with nums[i]
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                # swap nums[i] with nums[right] (right is the expected position of the next 2)
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
