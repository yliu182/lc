"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.

Example 1:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6

Example 2:
    Input: height = [4,2,0,3,2,5]
    Output: 9

Constraints:
    n == height.length
    1 <= n <= 2 * 10^4
    0 <= height[i] <= 10^5
"""

from typing import List


"""
可以把这道题理解成：每一个柱子上方能存多少水，然后全部加起来。

最关键的公式是：

water[i] = min(text{左边最高柱子},text{右边最高柱子}) - height[i]

因为水最终能有多高，取决于左右两边较矮的那堵墙。

但这中间有一个重要的反例：

height = [3, 0, 5, 0, 4]
index 1: min(3,5) - 0 = 3
index 3: min(5,4) - 0 = 4
total = 3 + 4 = 7

整个地图的水不一定由“一对左右边界”定义。但实际上可能存在多个 basin（水坑）：

但实际上可能存在多个 basin（水坑）：

左边这个坑水位由 3 和 5 决定，右边这个坑水位由 5 和 4 决定。中间的 5 同时是：

左边水坑的右墙
右边水坑的左墙

所以不能找一对 (i, j) 把整个问题包起来。
"""

class Solution:

    # # has bug
    # def trap(self, height: List[int]) -> int:
    #     n = len(height)
    #     if n < 2:
    #         return 0

    #     l = 0
    #     result = 0
    #     for i in range(n-2):
    #         for j in range(i+2, n, 1):
    #             area = 0
    #             min_h = min(height[i], height[j])
    #             for p in range(i+1, j, 1):
    #                 area += max(min_h - height[p], 0)
    #             result = max(result, area)
    #     return result

    ## Correct but O(n^2)
    # def trap(self, height: List[int]) -> int:
    #     n = len(height)
    #     result = 0
    #     for i in range(n):
    #         max_lh = 0
    #         max_rh = 0
    #         for j in range(i-1, -1, -1):
    #             max_lh = max(max_lh, height[j])
    #         for j in range(i+1, len(height), 1):
    #             max_rh = max(max_rh, height[j])
    #         result += max(min(max_lh, max_rh) - height[i], 0)
    #     return result

    def trap(self, height: List[int]) -> int:
        n = len(height)
        result = 0
        max_l = {0: 0}
        max_r = {n-1: 0}
        v = 0
        for i in range(1, n, 1):
            v = max(v, height[i-1])
            max_l[i] = v

        v = 0
        for i in range(n-2, -1, -1):
            v = max(v, height[i+1])
            max_r[i] = v

        for i in range(n):
            result += max(min(max_l[i], max_r[i]) - height[i], 0)

        return result
