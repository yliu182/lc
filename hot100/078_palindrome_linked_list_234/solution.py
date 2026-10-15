"""
234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list, return true if it is a palindrome or false
otherwise.

Example 1:
    Input: head = [1,2,2,1]
    Output: true

Example 2:
    Input: head = [1,2]
    Output: false

Constraints:
    The number of nodes in the list is in the range [1, 10^5].
    0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
1 2 3 4 5
f
s

    f
  s
        f
    s

1 2 3 4 5 6
      s
            f
'''


class Solution:
    def _reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

    def _is_identical(self, head1: ListNode, head2: ListNode, length: int) -> bool:
        p1 = head1
        p2 = head2
        for _ in range(length):
            if p1 is None or p2 is None or p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True

    '''
    [5 5 5 5]
    fast
    slow
    step 2
    '''
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # first find the middle position
        fast = head
        slow = head
        step = 0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            step += 1

        if fast:
            head2 = slow.next
            reversed_head2 = self._reverse(head2)
            return self._is_identical(head, reversed_head2, step)
        else:
            head2 = slow
            reversed_head2 = self._reverse(head2)
            return self._is_identical(head, reversed_head2, step)
