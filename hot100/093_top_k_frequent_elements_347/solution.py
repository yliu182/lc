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
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        frequencies = Counter(nums)
        for item, frequency in frequencies.items():
            heapq.heappush(heap, (frequency, item))
            if len(heap) > k:
                heapq.heappop(heap)

        return [h[1] for h in heap]
