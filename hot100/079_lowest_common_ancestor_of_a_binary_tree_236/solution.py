"""
236. Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined
between two nodes p and q as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself)."

Example 1:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3

Example 2:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5

Example 3:
    Input: root = [1,2], p = 1, q = 2
    Output: 1

Constraints:
    The number of nodes in the tree is in the range [2, 10^5].
    -10^9 <= Node.val <= 10^9
    All Node.val are unique.
    p != q
    p and q will exist in the tree.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    '''
    后序 DFS，让递归函数表示：在当前子树中找到 p、q 或它们的最近公共祖先，并返回对应节点。
    判断逻辑：
    1. 当前节点为空，返回空。
    2. 当前节点就是 p 或 q，直接返回当前节点。
    3. 分别递归搜索左、右子树。
    4. 如果左右都返回非空，说明 p 和 q 分布在两侧，当前节点就是最近公共祖先。
    5. 如果只有一侧非空，将这一侧的结果继续向上传递。
    6. 如果两侧都为空，返回空。
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(r):
            if r is None:
                return r

            if r is p or r is q:
                return r

            ret_left = dfs(r.left)
            ret_right = dfs(r.right)

            if ret_left and ret_right:
                return r
            elif ret_left:
                return ret_left
            elif ret_right:
                return ret_right
            else:
                return None

        return dfs(root)
