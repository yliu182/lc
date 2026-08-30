"""
23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in
ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]

Example 2:
    Input: lists = []
    Output: []

Example 3:
    Input: lists = [[]]
    Output: []
"""

from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     dummy = ListNode()

    #     def mergeTwo(l1, l2):
    #         dummy = ListNode()
    #         p = dummy
    #         p1 = l1
    #         p2 = l2
    #         while p1 is not None and p2 is not None:
    #             if p1.val <= p2.val:
    #                 p.next = p1
    #                 p1 = p1.next
    #             else:
    #                 p.next = p2
    #                 p2 = p2.next
    #             p = p.next

    #         p.next = p1 if p1 is not None else p2
    #         return dummy.next

    #     while len(lists) > 1:
    #         new_lists = []
    #         for i in range(0, len(lists), 2):
    #             p1 = lists[i]
    #             p2 = lists[i+1] if i+1 < len(lists) else None
    #             new_lists.append(mergeTwo(p1, p2))
    #         lists = new_lists

    #     if len(lists) == 1:
    #         return lists[0]
    #     else:
    #         return None



# heap = []
# heapq.heappush(heap, x)
# min_value = heapq.heappop(heap)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        p = dummy
        # 每个 list 的 head 放进 heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        while heap:
            val, i, node = heapq.heappop(heap)
            p.next = node
            p = p.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next
