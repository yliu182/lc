"""
105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder
traversal of a binary tree and inorder is the inorder traversal of the same
tree, construct and return the binary tree.

Example 1:
    Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    Output: [3,9,20,null,null,15,7]

Example 2:
    Input: preorder = [-1], inorder = [-1]
    Output: [-1]

Constraints:
    1 <= preorder.length <= 3000
    inorder.length == preorder.length
    -3000 <= preorder[i], inorder[i] <= 3000
    preorder and inorder consist of unique values.
    Each value of inorder also appears in preorder.
    preorder is guaranteed to be the preorder traversal of the tree.
    inorder is guaranteed to be the inorder traversal of the tree.
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
[3,9,20,15,7] pre
[9,3,15,20,7] in
3 is the root
left [9], right is [15, 20, 7]

so revisit the pre-order list, get the
    left-subtree
        preorder [9]
        inorder [9]
    right-subtree
        preorder [20, 15, 7]
        inorder [15, 20, 7]

    recursive function to process the sub-tree
"""

class Solution:

    """
    是的，你当前解法的最坏时间复杂度是 O(n²)，更准确地说是 Θ(n²)。
    主要成本来自两处：
    r_idx = in_list.index(r)  # O(k)
    以及数组切片：
    left_in = in_list[:r_idx]
    right_in = in_list[r_idx + 1:]
    left_pre = pre_list[1:1 + len(left_in)]
    right_pre = pre_list[1 + len(left_in):]
    Python 切片会复制列表，也是 O(k)。
    """
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    #     def recursive(pre_list, in_list):
    #         if len(pre_list) == 0 or len(in_list) == 0:
    #             return None

    #         r = pre_list[0]
    #         r_idx = in_list.index(r)
    #         left_in = in_list[0:r_idx]
    #         right_in = in_list[r_idx+1:]
    #         left_pre = pre_list[1:1+len(left_in)]
    #         right_pre = pre_list[1+len(left_in):]

    #         root_node = TreeNode(r)
    #         root_node.left = recursive(left_pre, left_in)
    #         root_node.right = recursive(right_pre, right_in)
    #         return root_node

    #     return recursive(preorder, inorder)


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {
            val: i
            for i, val in enumerate(inorder)
        }
        preorder_index = 0

        def recursive(left, right):
            """
            left and right pos in the inorder list
            """
            nonlocal preorder_index

            if left > right:
                return None

            root_value = preorder[preorder_index]
            root_node = TreeNode(root_value)
            mid = inorder_index[root_value]
            preorder_index += 1
            root_node.left = recursive(left, mid-1)
            root_node.right = recursive(mid+1, right)
            return root_node

        return recursive(0, len(inorder) - 1)
