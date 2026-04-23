"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single
digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if l1 is None:
            return l2
        if l2 is None:
            return l1


        # fake head
        res_head = ListNode(0)
        cur_node = res_head

        p1 = l1
        p2 = l2
        carry = 0

        while p1 is not None and p2 is not None: 
            cur_sum = p1.val + p2.val + carry
            v = cur_sum % 10
            carry = (int)(cur_sum / 10)
            cur_node.next = ListNode(v)
            cur_node = cur_node.next
            p1 = p1.next
            p2 = p2.next

        while p1 is not None:
            cur_sum = p1.val + carry
            v = cur_sum % 10
            carry = (int)(cur_sum) / 10
            cur_node.next = ListNode(v)
            cur_node = cur_node.next
            p1 = p1.next

        while p2 is not None:
            cur_sum = p2.val + carry
            v = cur_sum % 10
            carry = (int)(cur_sum) / 10
            cur_node.next = ListNode(v)
            cur_node = cur_node.next
            p2 = p2.next

        if carry != 0:
            cur_node.next = ListNode(carry)

        return res_head.next




