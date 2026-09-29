"""
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a
cycle in it.

There is a cycle in a linked list if there is some node in the list that can
be reached again by continuously following the next pointer.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects
    to the 1st node (0-indexed).

Example 2:
    Input: head = [1,2], pos = 0
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects
    to the 0th node.

Example 3:
    Input: head = [1], pos = -1
    Output: false
    Explanation: There is no cycle in the linked list.

Constraints:
    The number of the nodes in the list is in the range [0, 10^4].
    -10^5 <= Node.val <= 10^5
    pos is -1 or a valid index in the linked-list.
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    """
    My first solution has big mistake.

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        p = head.next

        while p and p != head:
            p = p.next

        if p is None:
            return False
        else:
            return True
    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        visited = set()
        p = head
        while p:
            if p in visited:
                return True
            else:
                visited.add(p)
                p = p.next

        return False
