import pytest
from solution import Trie


class TestTrie:
    def test_example1(self):
        trie = Trie()
        trie.insert("apple")
        assert trie.search("apple") is True
        assert trie.search("app") is False
        assert trie.startsWith("app") is True
        trie.insert("app")
        assert trie.search("app") is True

    def test_example2_multiple_words(self):
        trie = Trie()
        trie.insert("hello")
        trie.insert("help")
        assert trie.search("hello") is True
        assert trie.search("help") is True
        assert trie.search("hel") is False
        assert trie.startsWith("hel") is True

    def test_example3_no_match(self):
        trie = Trie()
        trie.insert("abc")
        assert trie.search("abd") is False
        assert trie.startsWith("abd") is False
        assert trie.startsWith("ab") is True

    def test_empty_trie_search(self):
        trie = Trie()
        assert trie.search("a") is False
        assert trie.startsWith("a") is False

    def test_single_char(self):
        trie = Trie()
        trie.insert("a")
        assert trie.search("a") is True
        assert trie.startsWith("a") is True
        assert trie.search("ab") is False

    def test_overlapping_words(self):
        trie = Trie()
        trie.insert("app")
        trie.insert("apple")
        trie.insert("application")
        assert trie.search("app") is True
        assert trie.search("apple") is True
        assert trie.search("application") is True
        assert trie.search("appli") is False
        assert trie.startsWith("appli") is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
