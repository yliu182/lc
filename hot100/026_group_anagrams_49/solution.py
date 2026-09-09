"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the
answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
    Input: strs = [""]
    Output: [[""]]

Example 3:
    Input: strs = ["a"]
    Output: [["a"]]

Constraints:
    1 <= strs.length <= 10^4
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
"""

from typing import List

"""
dict("sorted letters concat into a str" -> [])

这个方法的复杂度是：假设一共有 n 个字符串，每个字符串平均长度为 k，
Time:  O(n * k log k)
Space: O(n * k)
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for s in strs:
            key = "".join(sorted(s))
            """
            Python 的 string 本身就可以直接遍历：
            sorted("eat") -> ['a', 'e', 't']

            sort() 和 sorted() 不一样
            x = ['e', 'a', 't']
            x.sort() will change x inplace
            sorted(x) will create a new list
            """
            if key not in mapping:
                mapping[key] = [s]
            else:
                mapping[key].append(s)

        final_return = []
        for v in mapping.values():
            final_return.append(v)
        return final_return
