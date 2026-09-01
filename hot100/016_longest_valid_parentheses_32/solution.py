"""
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', return the length of
the longest valid (well-formed) parentheses substring.

Example 1:
    Input: s = "(()"
    Output: 2
    Explanation: The longest valid parentheses substring is "()".

Example 2:
    Input: s = ")()())"
    Output: 4
    Explanation: The longest valid parentheses substring is "()()".

Example 3:
    Input: s = ""
    Output: 0
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        final_result = 0
        for i in range(len(s)):
            if s[i] == ')':
                continue
            left = 1
            right = 0
            j = i + 1
            for j in range(i+1, len(s), 1):
                if s[j] == '(':
                    left += 1
                else:
                    right += 1
                if left < right:
                    break
                if left == right:
                    final_result = max(final_result, j - i + 1)

        return final_result
