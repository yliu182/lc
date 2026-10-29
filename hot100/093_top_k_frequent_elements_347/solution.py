"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

Example 2:
    Input: nums = [1], k = 1
    Output: [1]

Constraints:
    - 1 <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4
    - k is in the range [1, the number of unique elements in the array].
    - It is guaranteed that the answer is unique.
"""

from typing import List
import heapq

from collections import Counter

class Solution:
    '''
    A minHeap of size k.
    Complexity:
        * To construct heap, o(nums * logK)

    返回顺序不一定按频率排列，但题目允许任意顺序。
    - 统计频率：O(n)
    - 维护堆：O(m log k)
    - 堆空间：O(k)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        frequencies = Counter(nums)
        for item, frequency in frequencies.items():
            heapq.heappush(heap, (frequency, item))
            if len(heap) > k:
                heapq.heappop(heap)

        return [h[1] for h in heap]
    '''

    '''
    从高频桶向低频桶遍历，即可优先取得出现次数最多的元素。
    - 时间复杂度：O(n)
    - 空间复杂度：O(n)

    常见应用
        - 对分布均匀的浮点数排序。
        - 年龄、成绩、日期等范围明确的数据。
        - 按频率分组。
        - Top K Frequent Elements。
        - 根据优先级、距离或区间进行分组。

    在 Top K Frequent Elements 中：
        桶下标 = 出现频率
        桶内容 = 具有该频率的数字
        频率范围一定是 [1, n]，所以最多只需要 n + 1 个桶：
        buckets[frequency].append(num)
        然后从高频桶向低频桶遍历即可，不需要对所有元素进行比较排序。

    不适合的情况
        - 数值范围非常大但数据很少，例如只有 100 个数字，范围却是 [0, 10^12]。
        - 数据严重集中在一个桶中，桶内仍然需要大量排序。
        - 无法设计合理的桶映射规则。
        - 内存有限，但桶的数量非常多。
    '''s
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for item, frequency in frequencies.items():
            bucket[frequency].append(item)

        ans = []
        # for frequency, items in enumerate(bucket):

        for i in range(len(bucket)-1, -1, -1):
            ans.extend(bucket[i])
            if len(ans) >= k:
                return ans[:k]
        return ans
