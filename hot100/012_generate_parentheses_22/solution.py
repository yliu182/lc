"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
    Input: n = 1
    Output: ["()"]
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final_results = []
        def back(path, left, right):
            if left == n and right == n:
                final_results.append(path)
                return

            if left < n:
                back(path+'(', left+1, right)

            if left > right:
                back(path+')', left, right+1)

        back("", 0, 0)
        return final_results
