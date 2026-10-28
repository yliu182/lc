"""
297. Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a
sequence of bits so that it can be stored in a file or memory buffer, or
transmitted across a network connection link to be reconstructed later in the
same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no
restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and
this string can be deserialized to the original tree structure.

Example 1:
    Input: root = [1,2,3,null,null,4,5]
    Output: [1,2,3,null,null,4,5]

Example 2:
    Input: root = []
    Output: []

Constraints:
    - The number of nodes in the tree is in the range [0, 10^4].
    - -1000 <= Node.val <= 1000
"""

from typing import Optional


'''
推荐使用前序遍历 + 空节点标记。
序列化顺序：
根节点 -> 左子树 -> 右子树
不能只保存节点值，必须保存空节点，否则无法唯一确定树的结构。例如使用 # 表示空节点，用逗号分隔。
对于：
    1
   / \
  2   3
     / \
    4   5
序列化结果可以是：
1,2,#,#,3,4,#,#,5,#,#
序列化
- 当前节点为空：记录 #。
- 当前节点非空：记录节点值。
- 然后递归序列化左子树和右子树。
- 最后用逗号连接所有结果。
反序列化
- 将字符串按逗号拆分成 token。
- 按顺序读取 token。
- 如果 token 是 #，返回空节点。
- 否则创建当前节点。
- 接下来递归构造它的左子树。
- 再递归构造它的右子树。
- 返回当前节点。
因为序列化和反序列化采用相同的前序规则，每个 token 都只会消费一次。
复杂度：
- 序列化时间：O(n)
- 反序列化时间：O(n)
- 存储空间：O(n)
- 递归栈：O(h)，最坏 O(n)
节点最多 10^4，极端退化树可能超过 Python 递归深度。更稳健但稍复杂的方案是使用 BFS 和队列进行序列化、反序列化。
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        # a stack-based pre-order traversal of tree
        st = [root]
        ret = []
        while st:
            cur = st.pop()
            ret.append(str(cur.val) if cur else "#")
            if cur:
                st.append(cur.right)
                st.append(cur.left)

        return ",".join(ret)


    # def deserialize(self, data: str) -> Optional[TreeNode]:
    #     tokens = iter(data.split(","))

    #     def dfs() -> Optional[TreeNode]:
    #         next_token = next(tokens)
    #         if next_token == "#":
    #             return None

    #         node = TreeNode(int(next_token))
    #         node.left = dfs()
    #         node.right = dfs()
    #         return node

    #     return dfs()

    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')
        def dfs(index: int):
            if data[index] == '#':
                return None, index + 1

            node = TreeNode(int(data[index]))
            node.left, next_idx = dfs(index+1)
            node.right, next_idx = dfs(next_idx)
            return node, next_idx

        root_node, _ = dfs(0)
        return root_node
