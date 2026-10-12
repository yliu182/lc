"""
208. Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently
store and retrieve keys in a dataset of strings. There are various applications of this
data structure, such as autocomplete and spellchecker.

Implement the Trie class:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was
  inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string
  word that has the prefix prefix, and false otherwise.

Example 1:
    Input: ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
           [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    Output: [null, null, true, false, true, null, true]

Constraints:
    1 <= word.length, prefix.length <= 2000
    word and prefix consist only of lowercase English letters.
    At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.
"""


class Node:
    def __init__(self):
        self.children = {}
        self.eow = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            # if c in cur.children:
            #     cur = cur.children[c]
            # else:
            #     new_node = Node()
            #     cur.children[c] = new_node
            #     cur = new_node
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.eow = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.eow


    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
