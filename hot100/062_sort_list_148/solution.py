"""
148. Sort List
https://leetcode.com/problems/sort-list/

Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:
    Input: head = [4,2,1,3]
    Output: [1,2,3,4]

Example 2:
    Input: head = [-1,5,3,4,0]
    Output: [-1,0,3,4,5]

Example 3:
    Input: head = []
    Output: []

Constraints:
    The number of nodes in the list is in the range [0, 5 * 10^4].
    -10^5 <= Node.val <= 10^5

Follow up: Can you sort the linked list in O(n log n) time and O(1) memory?
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
这是 yao 写的第一版，明显比较别扭

class Solution:
    def _swap_two_following_nodes(self, begin: ListNode) -> None:
        # swap the two nodes: begin.next and begin.next.next (assuming both of them are not None)
        a = begin.next
        b = a.next
        tail = b.next
        # swap
        begin.next = b
        b.next = a
        a.next = tail

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # the linked list version of bubble sort
        if head is None or head.next is None:
            return head

        dummy_head = ListNode(0, head)

        num_elements = 0
        p = head
        while p:
            p = p.next
            num_elements += 1

        for i in range(num_elements):
            prev = dummy_head
            while prev and prev.next and prev.next.next:
                p1 = prev.next
                p2 = prev.next.next
                if p1.val > p2.val:
                    self._swap_two_following_nodes(prev)
                prev = prev.next

        return dummy_head.next
"""

############################################################
"""
第二版，比较简化的程序，
但是 time complexity is O(n^2)

class Solution:
    def _swap_next_two(self, begin: ListNode) -> None:
        if begin is None or begin.next is None or begin.next.next is None:
            return
        p1 = begin.next
        p2 = p1.next
        tail = p2.next
        begin.next = p2
        p2.next = p1
        p1.next = tail


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        swapped = True
        while swapped:
            swapped = False
            prev = dummy
            while prev.next and prev.next.next:
                p1 = prev.next
                p2 = p1.next
                if p1.val > p2.val:
                    self._swap_next_two(prev)
                    swapped = True
                prev = prev.next
        return dummy.next
"""
