"""
25. Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time,
and return the modified list.

k is a positive integer and is less than or equal to the length of the linked
list. If the number of nodes is not a multiple of k then left-out nodes, in
the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be
changed.

Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]

Example 2:
    Input: head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    """
    反转前：

g_prev -> 1 -> 2 -> 3 -> g_next
          ↑         ↑
       g_start     kth


反转后：

g_prev -> 3 -> 2 -> 1 -> g_next
                    ↑
                  g_prev（下一轮）

    """
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        g_prev = dummy

        def getK(cur, k):
            while k > 0 and cur is not None:
                cur = cur.next
                k -= 1
            return cur

        while True:
            kth = getK(g_prev, k)
            if kth is None:
                break

            g_next = kth.next
            g_start = g_prev.next

            prev = g_next
            cur = g_start
            while cur != g_next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            g_prev.next = kth
            g_prev = g_start
        return dummy.next




        # def reverse(ListNode head):
        #     prev = None
        #     cur = head
        #     while cur is not None:
        #         nxt = cur.next
        #         cur.next = prev
        #         cur = nxt
        #         prev = cur
        #     return prev
