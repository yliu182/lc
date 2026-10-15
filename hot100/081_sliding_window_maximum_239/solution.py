"""
239. Sliding Window Maximum

You are given an array of integers nums, and there is a sliding window of size k
which is moving from the very left of the array to the very right. You can only
see the k numbers in the window. Each time the sliding window moves right by one
position. Return the max sliding window.

Example 1:
    Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [3,3,5,5,6,7]

[1,3,-1,-3,5,3,6,7]
   i

[1,2,3]
[3,-1,-3]


Example 2:
    Input: nums = [1], k = 1
    Output: [1]

Constraints:
    - 1 <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4
    - 1 <= k <= nums.length
"""

from typing import List
from collections import deque


class Solution:
    '''
    可以把 deque 理解成一个“最大值候选名单”。它不保存窗口内所有元素，只保存那些未来可能成为最大值的元素下标。
    队列对应的数值始终保持从大到小：
    队首：当前最大值
    队尾：较小的候选值

    两个核心操作
    假设当前处理 nums[i]。
    1. 删除已经离开窗口的下标
    窗口范围是：
    [i - k + 1, i]
    如果队首下标小于 i - k + 1，说明它已经离开窗口，需要从队首删除。
    2. 删除队尾不大于当前值的元素
    如果新元素比队尾元素大：
    旧元素更小，并且出现得更早
    新元素更大，并且存活时间更长
    旧元素以后不可能成为窗口最大值，因此可以永久删除。
    '''
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ret = []
        for i, n in enumerate(nums):
            if q and q[0] < i - k + 1:
                q.popleft()

            while q and nums[q[-1]] <= n:
                    q.pop()
            q.append(i)

            if i >= k - 1:
                ret.append(nums[q[0]])
        return ret
