"""
142. Linked List Cycle II

Given the head of a linked list, return the node where the cycle begins. If
there is no cycle, return None.

There is a cycle in a linked list if there is some node in the list that can
be reached again by continuously following the next pointer.

Do not modify the linked list.

Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: tail connects to node index 1
    Explanation: There is a cycle in the linked list, where tail connects to
    the second node.

Example 2:
    Input: head = [1,2], pos = 0
    Output: tail connects to node index 0
    Explanation: There is a cycle in the linked list, where tail connects to
    the first node.

Example 3:
    Input: head = [1], pos = -1
    Output: no cycle
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
    这个代码返回的是快慢指针的相遇节点，但相遇节点不一定是环的入口节点：
    if slow is fast:
        return slow  # 错误：这里只能确认有环
    例如：
    3 -> 2 -> 0 -> -4
         ^         |
         |_________|
    快慢指针可能在 -4 相遇，但环的入口是 2。
    相遇后需要：
    1. 将一个指针重新放到 head
    2. 两个指针每次各走一步
    3. 再次相遇的位置就是环入口

    head 到环入口的距离 = a
    环入口到第一次相遇点的距离 = b
    环的长度 = L
    链表结构可以表示为：
    head --------> 环入口 --------> 相遇点
        a              b
                        |
                        | 剩余 L - b 步回到环入口
                        v
    第一次相遇
    慢指针每次走 1 步，快指针每次走 2 步。
    相遇时，假设慢指针走了：
    a + b
    那么快指针走了：
    2(a + b)
    快指针比慢指针多走的距离一定是若干个完整的环：
    2(a + b) - (a + b) = kL
    所以：
    a + b = kL

    is 和 == 的区别：
    - == 比较两个对象的值是否相等，可能会调用对象的 __eq__ 方法。
    - is 比较两个变量是否指向内存中的同一个对象。

    在链表题中，我们需要判断两个指针是否指向同一个节点，而不是节点的值
    是否相同，因此应该使用：
        slow is fast

    两个不同节点可以有相同的 val，此时它们的值可能相等，但并不是同一个节点。
    判断 None 时也应该使用 is 或 is not：
        node is None
        node is not None
    """
    # def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

    #     fast = head
    #     slow = head

    #     if head is None:
    #         return None

    #     while fast and fast.next:
    #         fast = fast.next.next
    #         slow = slow.next
    #         if slow is fast:
    #             return slow

    #     return None

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        # if not head:
        #     return None

        # if head.next == head:
        #     return head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                # there is loop
                ptr = head
                while ptr is not slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr

        # there is no loop
        return None
