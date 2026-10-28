"""
295. Find Median from Data Stream

The median is the middle value in an ordered integer list. If the size of the list
is even, there is no middle value, and the median is the mean of the two middle values.

Implement the MedianFinder class:
    - MedianFinder() initializes the MedianFinder object.
    - void addNum(int num) adds the integer num from the data stream to the data structure.
    - double findMedian() returns the median of all elements so far.

Example 1:
    Input: ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
           [[], [1], [2], [], [3], []]
    Output: [null, null, null, 1.5, null, 2.0]

Constraints:
    - -10^5 <= num <= 10^5
    - There will be at least one element in the data structure before calling findMedian.
"""

import heapq

class MedianFinder:
    '''
    推荐使用两个堆，将数据分成较小的一半和较大的一半。
    - small：保存较小的一半，使用最大堆。
    - large：保存较大的一半，使用最小堆。
    - Python 只有最小堆，因此 small 中保存负数来模拟最大堆。
    始终维持两个条件：
        small 中所有元素 <= large 中所有元素
        两个堆的大小差不能超过 1
    可以规定：
        small 的数量等于 large 或者 small 比 large 多一个元素

    添加数字时：
    1. 如果 small 为空，或者新数字不大于 small 的最大值，放入 small。
    2. 否则放入 large。
    3. 添加后重新平衡：
    - 如果 small 比 large 多两个，将 small 最大值移到 large。
    - 如果 large 比 small 多，将 large 最小值移到 small。

    查找中位数时：
    - 总数为奇数：small 多一个元素，中位数就是 small 的最大值。
    - 总数为偶数：中位数是 small 最大值与 large 最小值的平均值。
    '''
    def __init__(self):
        self.h_small = [] # 保存较小的一半，使用最大堆。必须有意识的用负号
        self.h_large = [] # 保存较大的一半，使用最小堆。

    def addNum(self, num: int) -> None:
        if len(self.h_small) == 0 or (-self.h_small[0]) >= num:
            heapq.heappush(self.h_small, -num)
        else:
            heapq.heappush(self.h_large, num)

        if len(self.h_small) > len(self.h_large) + 1:
            # move h_small[0] to h_large
            heapq.heappush(
                self.h_large,
                -heapq.heappop(self.h_small)
            )
        elif len(self.h_large) > len(self.h_small):
            # move h_large[0] to h_small
            heapq.heappush(
                self.h_small,
                -heapq.heappop(self.h_large)
            )


    def findMedian(self) -> float:
        if len(self.h_small) == len(self.h_large):
            return (-self.h_small[0] + self.h_large[0]) / 2
        else:
            return -self.h_small[0]
