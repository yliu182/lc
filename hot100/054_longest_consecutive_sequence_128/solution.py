"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
    Therefore its length is 4.

Example 2:
    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9

Constraints:
    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ret = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                # num could be the start of sequence
                cur = num
                while cur in nums_set:
                    cur += 1
                ret = max(ret, cur - num)
        return ret

    """
    为什么是 O(n)

    虽然代码中有嵌套的 while，但只会从每个连续序列的起点开始向后扫描。
    对于：
    1, 2, 3, 4
    只从 1 开始扫描一次，不会再从 2、3、4 重复扫描。
    因此每个数字最多被处理常数次：
    时间：O(n)
    空间：O(n)
    需要特别注意：如果从集合中的每个数字都向后扫描，连续数组情况下会退化成 O(n²)。关键优化就是：
    if num - 1 not in num_set:
    只从连续序列的起点开始。
    """
