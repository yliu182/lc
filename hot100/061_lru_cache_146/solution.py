"""
146. LRU Cache
https://leetcode.com/problems/lru-cache/

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. Otherwise,
  add the key-value pair to the cache. If the number of keys exceeds the capacity from
  this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example 1:
    Input: ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
           [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    Output: [null, null, null, 1, null, -1, null, -1, 3, 4]

Constraints:
    1 <= capacity <= 3000
    0 <= key <= 10^4
    0 <= value <= 10^5
    At most 2 * 10^5 calls will be made to get and put.
"""

# from collections import deque
# import time

# class LRUCache:
#     def __init__(self, capacity: int):
#         self.accessed_keys = {} # key -> timestamp
#         self.cache = {}
#         self.capacity = capacity
#         self.timestamp = 0

#     def get(self, key: int) -> int:
#         # 这是一个重要的 bug, 如果 key 不存在 的话，那么不应该 update 时间
#         # self.accessed_keys[key] = time.time()
#         # return self.cache.get(key, -1)
#         # if key in self.cache:
#         #     self.accessed_keys[key] = time.time()
#         # return self.cache.get(key, -1)
#         self.timestamp += 1
#         if key not in self.cache:
#             return -1
#         self.accessed_keys[key] = self.timestamp
#         return self.cache[key]


#     def put(self, key: int, value: int) -> None:
#         """
#         if key already exist
#             update only
#         else
#             if capacity is full before put:
#                 first erase the earlier access key first
#             write
#         """
#         if key not in self.cache and len(self.cache) == self.capacity:
#             # find the oldest key
#             oldest_key = None
#             smallest_timestamp = float("Inf")
#             for k, t in self.accessed_keys.items():
#                 if t < smallest_timestamp:
#                     oldest_key = k
#                     smallest_timestamp = t
#             self.accessed_keys.pop(oldest_key)
#             self.cache.pop(oldest_key)
#         self.timestamp += 1
#         self.cache[key] = value
#         self.accessed_keys[key] = self.timestamp



# from collections import OrderedDict

# """
# get：平均 O(1)
# put：平均 O(1)
# 空间：O(capacity)
# """
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = OrderedDict()

#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         self.cache.move_to_end(key)
#         return self.cache[key]


#     def put(self, key: int, value: int) -> None:
#         self.cache[key] = value
#         self.cache.move_to_end(key)
#         if len(self.cache) > self.capacity:
#             self.cache.popitem(last=False)


"""
标准做法是：
哈希表 + 双向链表
两者分别解决不同问题：
哈希表：O(1) 找到 key 对应的节点
双向链表：O(1) 删除节点、移动节点、淘汰最旧节点
约定链表顺序：
head <-> 最久未使用 <-> ... <-> 最近使用 <-> tail
head 和 tail 是哨兵节点，不保存真实数据。
为什么使用双向链表
找到某个节点后，需要将它从原位置删除：
node.prev.next = node.next
node.next.prev = node.prev
双向链表可以直接获得前后节点，因此删除是 O(1)。
如果使用单向链表，还需要从头查找前一个节点，删除会变成 O(n)。

get() 的流程
    key 不存在 -> 返回 -1
    key 存在：
    1. 从哈希表找到节点
    2. 从原位置删除节点
    3. 将节点添加到链表末尾
    4. 返回 value
put() 的流程
    key 已存在：
        1. 更新 value
        2. 将节点移动到链表末尾
    key 不存在：
        1. 创建新节点
        2. 加入哈希表
        3. 添加到链表末尾
        4. 如果超过容量，删除 head 后面的第一个真实节点
    节点必须同时保存 key 和 value：
        self.key = key
        self.value = value
    淘汰节点时，不仅要从链表删除，还要使用它的 key 从哈希表删除：
"""

class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> Node
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node: Node)-> None:
        old_prev = node.prev
        old_next = node.next
        old_prev.next = old_next
        old_next.prev = old_prev


    def _add_to_end(self, node: Node)-> None:
        old_prev = self.tail.prev
        old_prev.next = node
        node.prev = old_prev
        node.next = self.tail
        self.tail.prev = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        n = self.cache[key]
        # move this 'n' to the end of list
        self._remove_node(n)
        self._add_to_end(n)
        return n.value

    def put(self, key: int, value: int) -> None:
        """
        (1) if key exist:
                move node to the end
                update cache
        (2) if key not exist:
                create new node
                move node to the end
                update cache
                if size > capacity:
                    remove first node from list
                    delete element from cache
        """
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_to_end(node)
            return

        node = Node(key, value)
        self._add_to_end(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            first_node = self.head.next
            first_key = first_node.key
            self._remove_node(first_node)
            del self.cache[first_key]
