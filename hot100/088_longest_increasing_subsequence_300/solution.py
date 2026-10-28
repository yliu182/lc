"""
300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing
subsequence.

Example 1:
    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
    Input: nums = [0,1,0,3,2,3]
    Output: 4

Example 3:
    Input: nums = [7,7,7,7,7,7,7]
    Output: 1

Constraints:
    - 1 <= nums.length <= 2500
    - -10^4 <= nums[i] <= 10^4
"""

from typing import List


class Solution:

    # o(n**2)
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [1] * n
    #     dp[n-1] = 1
    #     max_ret = 1
    #     for i in range(n-2,-1,-1):
    #         for j in range(i+1, n):
    #             if nums[i] < nums[j]:
    #                 dp[i] = max(dp[i], 1 + dp[j])
    #                 max_ret = max(dp[i], max_ret)
    #     return max_ret

    def lengthOfLIS(self, nums: List[int]) -> int:
        def first_larger_element(stack: List[int], target: int) -> int:
            left = 0
            right = len(stack)
            while left < right:
                mid = left + (right - left) // 2
                if stack[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left


        length = len(nums)

        '''
        因为正确算法中的 stack（通常叫 tails）满足这个定义：
        stack[i] = 长度为 i + 1 的递增子序列中，最小的结尾值
        例如：
        stack = [2, 3, 7, 18]
        表示当前已经能够构造出长度分别为 1、2、3、4 的递增子序列，因此最长长度就是 4。
        处理新元素时只有两种情况：
        if idx == len(stack):
            stack.append(num)
        说明 num 大于所有结尾值，可以把现有最长子序列延长一位，所以长度增加。
        else:
            stack[idx] = num
        这里只替换结尾值，不改变长度。使用更小的结尾值，可以让该长度的子序列将来更容易继续延长。
        因此 stack 的长度：
        - 只会增加，不会减少；
        - 每增加一次，就表示找到了更长的递增子序列；
        - 最终长度就是全局 LIS 长度。
        所以不需要额外维护 max_ret：
        return len(stack)
        需要注意，stack 中的元素不一定组成原数组里真实的一条 LIS，它保存的是各个长度下的最优结尾值。你之前因为删除了后面的元素，stack 长度会减少，所以才需要 max_ret；正确算法只替换一个位置，长度不会减少。
        '''
        stack = []
        max_ret = 1

        for n in nums:
            # scan stack[0:l-1], find the first index that is larger than n, namely "idx"
            # swap stack[idx] = n, and pop all element after that
            idx = first_larger_element(stack, n)
            if idx == len(stack):
                stack.append(n)
            else:
                stack[idx] = n

            # num_to_pop = len(stack) - idx
            # for _ in range(num_to_pop):
            #     stack.pop()
            # stack.append(n)
        #max_ret = max(max_ret, len(stack))

        return len(stack)
