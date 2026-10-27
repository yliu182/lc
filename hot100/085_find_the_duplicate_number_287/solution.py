"""
287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is
in the range [1, n] inclusive. There is only one repeated number in nums, return
this repeated number.

You must solve the problem without modifying the array nums and using only
constant extra space.

Example 1:
    Input: nums = [1,3,4,2,2]
    Output: 2

Example 2:
    Input: nums = [3,1,3,4,2]
    Output: 3

Example 3:
    Input: nums = [3,3,3,3,3]
    Output: 3

Constraints:
    - 1 <= n <= 10^5
    - nums.length == n + 1
    - 1 <= nums[i] <= n
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        推荐使用 Floyd 快慢指针判环，把数组看成一条隐式链表。
        数组中的关系可以理解为：
        下标 i -> 下一个下标 nums[i]
        因为所有值都在 [1, n]，所以每个值都能作为合法下标继续跳转。数组有 n + 1 个位置，但目标下标只有 1 到 n，必然有多个位置指向同一个节点，因此会形成环。
        例如：
        nums = [1, 3, 4, 2, 2]

        0 -> 1 -> 3 -> 2 -> 4
                        ↑    |
                        |____|
        环的入口是 2，也就是重复数字。
        寻找过程分两阶段：
        1. 一个慢指针每次跳一步，一个快指针每次跳两步，它们最终会在环内相遇。
        2. 相遇后，把其中一个指针放回起点；然后两个指针都每次走一步。
        3. 两者再次相遇的位置就是环入口，也就是重复数字。
        关键点：
        - 指针的移动不是 index + 1，而是根据当前位置的数组值跳转。
        - 第一阶段只负责证明并找到环内相遇点。
        - 第二阶段才负责定位环的入口。
        - 不修改原数组。
        - 时间复杂度 O(n)。
        - 额外空间 O(1)。
        '''

        fast = 0
        slow = 0
        is_begin = True
        while fast != slow or is_begin:
            is_begin = False
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]

        return fast
