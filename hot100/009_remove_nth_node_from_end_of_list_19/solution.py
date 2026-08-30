"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list
and return its head.

Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Example 2:
    Input: head = [1], n = 1
    Output: []

Example 3:
    Input: head = [1,2], n = 1
    Output: [1]
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        dummy = ListNode(0, head)

        p1 = dummy
        p2 = dummy
        # p2 先走 n + 1 步
        for _ in range(n+1):
            if p2 is not None:
                p2 = p2.next
            else:
                return head
        # 然后一起走，直到 p2 走到 None
        while p2 is not None:
            p1 = p1.next
            p2 = p2.next

        # p1 此时正好在待删除节点的前一个位置
        p1.next = p1.next.next

        return dummy.next
"""
    [1, 2, 3, 4, 5]  n =2
     p1    p2
        p1    p2
            1.   2


有一个edge case 是说 p2 先走了n 步之后，p1 刚好需要被删掉，需要删 head.

"""
