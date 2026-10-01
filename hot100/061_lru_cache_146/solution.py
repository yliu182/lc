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

import time

class LRUCache:
    def __init__(self, capacity: int):
        self.accessed_keys = {} # key -> timestamp
        self.cache = {}
        self.capacity = capacity
        self.timestamp = 0

    def get(self, key: int) -> int:
        # 这是一个重要的 bug, 如果 key 不存在 的话，那么不应该 update 时间
        # self.accessed_keys[key] = time.time()
        # return self.cache.get(key, -1)
        # if key in self.cache:
        #     self.accessed_keys[key] = time.time()
        # return self.cache.get(key, -1)
        self.timestamp += 1
        if key not in self.cache:
            return -1
        self.accessed_keys[key] = self.timestamp
        return self.cache[key]


    def put(self, key: int, value: int) -> None:
        """
        if key already exist
            update only
        else
            if capacity is full before put:
                first erase the earlier access key first
            write
        """
        if key not in self.cache and len(self.cache) == self.capacity:
            # find the oldest key
            oldest_key = None
            smallest_timestamp = float("Inf")
            for k, t in self.accessed_keys.items():
                if t < smallest_timestamp:
                    oldest_key = k
                    smallest_timestamp = t
            self.accessed_keys.pop(oldest_key)
            self.cache.pop(oldest_key)
        self.timestamp += 1
        self.cache[key] = value
        self.accessed_keys[key] = self.timestamp
