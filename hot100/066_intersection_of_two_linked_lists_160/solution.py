"""
160. Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/

Given the heads of two singly linked-lists headA and headB, return the node at which
the two lists intersect. If the two linked lists have no intersection at all, return null.

The linked lists must retain their original structure after the function returns.

Example 1:
    Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
    Output: Reference of the node with value = 8

Example 2:
    Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
    Output: Reference of the node with value = 2

Example 3:
    Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
    Output: null (no intersection)

Constraints:
    The number of nodes of listA is in the m.
    The number of nodes of listB is in the n.
    1 <= m, n <= 3 * 10^4
    1 <= Node.val <= 10^5
    0 <= skipA < m
    0 <= skipB < n

Follow up: Could you write a solution that runs in O(m + n) time and uses only O(1) memory?
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    假设：
    A 独有部分长度 = a
    B 独有部分长度 = b
    公共部分长度 = c
    两个指针走过的路径分别是：
    pointer_a：a + c + b
    pointer_b：b + c + a
    总长度相同：
    a + c + b = b + c + a
    所以两个指针会消除链表长度差，并同时到达相交节点。
    如果没有交点，它们各自走完两个链表后，会同时变成 None：
    pointer_a is pointer_b  # True
    """
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    #     p1 = headA
    #     p2 = headB
    #     p1_concated = False
    #     p2_concated = False
    #     while True:
    #         if p1 is None:
    #             if not p1_concated:
    #                 p1 = headB
    #                 p1_concated = True
    #         if p2 is None:
    #             if not p2_concated:
    #                 p2 = headA
    #                 p2_concated = True

    #         if p1 is None or p2 is None:
    #             return None
    #         if p1 is p2:
    #             return p1
    #         p1 = p1.next
    #         p2 = p2.next

    #     return None


    # 大幅简化之后的写法
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        while p1 is not p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA

        return p1
