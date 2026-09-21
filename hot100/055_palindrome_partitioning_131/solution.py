"""
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a
palindrome. Return all possible palindrome partitioning of s.

Example 1:
    Input: s = "aab"
    Output: [["a","a","b"],["aa","b"]]

Example 2:
    Input: s = "a"
    Output: [["a"]]

Constraints:
    1 <= s.length <= 16
    s contains only lowercase English letters.
"""

from typing import List


class Solution:
    """
    这是 yao 自己写的一个版本，有bug

    def partition(self, s: str) -> List[List[str]]:
        global_results = []

        def dfs(idx, path):
            # return a list of list of strings
            nonlocal global_results
            if idx == len(s):
                global_results.append(path)

                #这里有一个严重的 bug, 在找到答案的时候，需要copy 固定下来。不然以后会被后续的 pop 影响
                return
            cur = idx
            while cur < len(s) and s[cur] == s[idx]:
                path.append(s[idx:cur+1])
                dfs(cur + 1, path)
                path.pop()
                cur += 1

        dfs(0, [])
        return global_results
    """

    def partition(self, s: str) -> List[List[str]]:
        global_results = []

        def isPalindrome(s):
            if len(s) == 1:
                return True
            left = 0
            right = len(s) - 1 - left
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(idx, path):
            if idx == len(s):
                global_results.append(path.copy())
                return

            cur = idx
            # iterate cur from [idx, len(s)-11], check if s[idx, cur] is Palindrome
            for cur in range(idx, len(s)):
                substr = s[idx:cur+1]
                if isPalindrome(substr):
                    path.append(substr)
                    dfs(cur + 1, path)
                    path.pop()

        dfs(0, [])
        return global_results
