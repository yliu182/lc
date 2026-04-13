import pytest
from solution import LRUCache


class TestLRUCache:
    def test_example1(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        assert cache.get(1) == 1
        cache.put(3, 3)  # evicts key 2
        assert cache.get(2) == -1
        cache.put(4, 4)  # evicts key 1
        assert cache.get(1) == -1
        assert cache.get(3) == 3
        assert cache.get(4) == 4

    def test_example2_overwrite(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(1, 10)  # update existing key
        assert cache.get(1) == 10
        assert cache.get(2) == 2

    def test_example3_get_refreshes(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(1)  # refresh key 1
        cache.put(3, 3)  # evicts key 2 (least recently used)
        assert cache.get(2) == -1
        assert cache.get(1) == 1

    def test_capacity_one(self):
        cache = LRUCache(1)
        cache.put(1, 1)
        assert cache.get(1) == 1
        cache.put(2, 2)
        assert cache.get(1) == -1
        assert cache.get(2) == 2

    def test_get_nonexistent(self):
        cache = LRUCache(2)
        assert cache.get(1) == -1

    def test_put_updates_recently_used(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(1, 5)  # update key 1, making it most recent
        cache.put(3, 3)  # should evict key 2
        assert cache.get(2) == -1
        assert cache.get(1) == 5
        assert cache.get(3) == 3


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
