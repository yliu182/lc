"""
138. Copy List with Random Pointer

A linked list of length n is given such that each node contains an additional
random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n
brand new nodes, where each new node has its value set to the value of its
corresponding original node. Both the next and random pointer of the new nodes
should point to new nodes in the copied list such that the pointers in the
original list and copied list represent the same list state.

Return the head of the copied linked list.

Example 1:
    Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
    Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
    Input: head = [[1,1],[2,1]]
    Output: [[1,1],[2,1]]

Example 3:
    Input: head = [[3,null],[3,0],[3,null]]
    Output: [[3,null],[3,0],[3,null]]

Constraints:
    0 <= n <= 1000
    -10^4 <= Node.val <= 10^4
    Node.random is null or is pointing to some node in the linked list.
"""

from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None

        o_ptr = head # iterator on old list
        n_head = Node(head.val)
        n_ptr = n_head
        old_to_new = {None: None}
        while o_ptr.next is not None:
            old_to_new[o_ptr] = n_ptr
            to_add = Node(o_ptr.next.val)
            n_ptr.next = to_add
            n_ptr = n_ptr.next
            o_ptr = o_ptr.next

        # 这一句话很容易漏掉，非常容易犯错
        old_to_new[o_ptr] = n_ptr

        old_p = head
        new_p = n_head
        while old_p is not None:
            new_p.random = old_to_new[old_p.random]
            old_p = old_p.next
            new_p = new_p.next

        return n_head
