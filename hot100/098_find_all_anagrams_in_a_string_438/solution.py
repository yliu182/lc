"""
438. Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's
anagrams in s. You may return the answer in any order.

An anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

Example 1:
    Input: s = "cbaebabacd", p = "abc"
    Output: [0,6]

Example 2:
    Input: s = "abab", p = "ab"
    Output: [0,1,2]

Constraints:
    - 1 <= s.length, p.length <= 3 * 10^4
    - s and p consist of lowercase English letters.
"""

from typing import List
from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # keep a sliding window of size 'len(p)'
        window = defaultdict(int) # char -> count
        target_counts = defaultdict(int)
        for c in p:
            target_counts[c] += 1

        ans = []
        for i in range(len(s) - len(p) + 1):
            if i > 0:
                window[s[i-1]] -= 1
                if window[s[i-1]] == 0:
                    del window[s[i-1]]
                window[s[i + len(p) - 1]] += 1
            else:
                for c in s[0:len(p)]:
                    window[c] += 1

            if target_counts == window:
                ans.append(i)
        return ans
