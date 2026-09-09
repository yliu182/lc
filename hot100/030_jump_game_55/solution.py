"""
55. Jump Game

You are given an integer array nums. You are initially positioned at the array's
first index, and each element in the array represents your maximum jump length
at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
    Input: nums = [2,3,1,1,4]
    Output: true

Example 2:
    Input: nums = [3,2,1,0,4]
    Output: false

Constraints:
    1 <= nums.length <= 10^4
    0 <= nums[i] <= 10^5
"""

from typing import List


"""
可以把这个 greedy 思路理解成：

我不关心具体怎么跳，我只关心“目前所有可能路径里，最远能覆盖到哪里”。

这就是为什么它比 BFS 更简单。BFS 会显式探索很多路径，而 greedy 把所有这些路径压缩成了一个信息
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            # 我之前所有能到达的位置，最远也只能到 max_reach，连当前位置 i 都碰不到。
            if max_reach < i:
                return False
            max_reach = max(max_reach, i + nums[i])

        return True
