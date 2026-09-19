"""
102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes'
values. (i.e., from left to right, level by level).

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

Example 2:
    Input: root = [1]
    Output: [[1]]

Example 3:
    Input: root = []
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000
"""

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque()
        ret = []
        if root is None:
            return []

        queue.append(root)

        while len(queue) > 0:
            res_list = []
            next_queue = deque()
            for _ in range(len(queue)):
                c = queue.popleft()
                res_list.append(c.val)
                if c.left:
                    next_queue.append(c.left)
                if c.right:
                    next_queue.append(c.right)

            queue = next_queue
            ret.append(res_list)

        return ret
