"""
56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

Example 1:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]

Example 2:
    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]

Constraints:
    1 <= intervals.length <= 10^4
    intervals[i].length == 2
    0 <= starti <= endi <= 10^4
"""

from typing import List


"""
先排序，再贪心合并。

先按照每个 interval 的 start 从小到大排序。这样之后，你只需要看“当前区间”和“结果里最后一个区间”是否重叠。
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []

        intervals.sort(key=lambda x:x[0])

        results = [intervals[0]]
        last_start, last_end= intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals), 1):
            interval = intervals[i]
            if interval[0] > last_end:
                results.append(interval)
                last_start, last_end = interval[0], interval[1]
            else:
                # merge
                new_interal = [
                    last_start,
                    max(last_end, interval[1])
                ]
                results.pop()
                results.append(new_interal)
                last_start, last_end = new_interal[0], new_interal[1]

        return results
