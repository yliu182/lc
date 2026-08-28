"""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:
    Input: s = "babad"
    Output: "bab" (or "aba")

Example 2:
    Input: s = "cbbd"
    Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left+1, right-1

        if len(s) < 2:
            return s

        final_left = 0
        final_right = 0

        for center in range(len(s)):
            left, right = expand(center, center)
            if right - left > final_right - final_left:
                final_right = right
                final_left = left

        for start in range(len(s)-1):
            if s[start] == s[start+1]:
                left, right = expand(start, start+1)
                if right - left > final_right - final_left:
                    final_right = right
                    final_left = left

        return s[final_left : final_right + 1]
