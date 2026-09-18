"""
84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where
the width of each bar is 1, return the area of the largest rectangle in the
histogram.

Example 1:
    Input: heights = [2,1,5,6,2,3]
    Output: 10
    Explanation: The largest rectangle has an area = 10 units (from index 2 to 3
    with height 5).

Example 2:
    Input: heights = [2,4]
    Output: 4

Constraints:
    1 <= heights.length <= 10^5
    0 <= heights[i] <= 10^4
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        The largest rectangle must be using one height.
        We can iterate the array to exhaust each height option
        For each height (heights[i]) we need to record the left_most and right_most index that uses this height, the left_most index that has value >= cur
        So we traverse input once to construct the l_idx and r_idx array

        对于位置 i: 矩形高度 = heights[i]
        左边界 = 左边第一个比 heights[i] 小的位置之后
        右边界 = 右边第一个比 heights[i] 小的位置之前
        面积为： heights[i] × 可扩张宽度
        但如果每根柱子都分别向左右扫描，最坏时间复杂度是：O(n²)

        单调栈的核心
        维护一个高度递增的栈。 建议栈中保存：(start_index, height)
        含义是：
            高度为 height 的矩形，最早可以从 start_index 开始向右扩张。
            遍历到当前下标 i、高度 current_height 时：
            - 如果当前高度大于等于栈顶，可以继续保持递增，压入栈。
            - 如果当前高度小于栈顶，说明栈顶高度不能再向右扩张。
            - 弹出栈顶，并计算以弹出高度为高的最大面积。

        高柱子先入栈等待；一旦遇到矮柱子，就说明前面的高柱子右边界出现了，于是不断 pop 并结算面积。

        最后还有一个小问题：如果右边一直没有矮柱子呢？
        一个很漂亮的技巧是在最后想象加一个高度为 0 的柱子：

        新柱子必须要继承被弹出柱子的起点.
        当前代码出栈后使用：
            ms.append((i, cur_h))
        这会丢失当前较矮柱子可以向左延伸的信息。

        以递减数组开头为例：
        [5, 4, 3, 2, 1]
        放入 stack 里的内容需要是：
        (0, 5) -> (0, 4) -> (0, 3) -> (0, 2) -> (0, 1)
        """
        if len(heights) == 0:
            return 0
        ms = [(0, heights[0])]

        max_area = float('-inf')
        for i in range(1, len(heights) + 1):
            if i == len(heights):
                cur_h = 0
            else:
                cur_h = heights[i]

            if cur_h >= ms[-1][1]:
                ms.append((i, cur_h))
            else:
                left_boundary = 0
                while len(ms) > 0 and cur_h < ms[-1][1]:
                    top_i, top_h = ms.pop()
                    left_boundary = top_i
                    area = top_h * (i - top_i)
                    max_area = max(max_area, area)

                ms.append((left_boundary, cur_h))
        return max_area

"""
3, 5, 6, 4, 3
         cur

(0, 3), (1, 4)
last_left = index(5) = 1

when compute the area for 4


4 * 3
"""
