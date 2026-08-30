"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

Mapping (like on telephone buttons):
    2: abc, 3: def, 4: ghi, 5: jkl, 6: mno, 7: pqrs, 8: tuv, 9: wxyz

Example 1:
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
    Input: digits = ""
    Output: []

Example 3:
    Input: digits = "2"
    Output: ["a","b","c"]
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        m = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if len(digits) == 0:
            return []

        final_results = []

        # backtrace version 1, using list as "path", we are mutating the same
        # list in place, not create new list, so we have to pop.
        def bt_v1(
            index, # int
            path, # List[str]
        ):
            if index == len(digits):
                final_results.append("".join(path))
                return

            letter = digits[index]
            for s in m[letter]:
                path.append(s)
                bt_v1(index + 1, path)
                path.pop()

        # backtrace version 2, using str as "path", we are creating new string
        # for each iteration.
        def bt_v2(
            index, # int
            path, # str
        ):
            if index == len(digits):
                final_results.append(path)
                return

            letter = digits[index]
            for s in m[letter]:
                bt_v2(index + 1, path + s)

        # bt_v1(0, [])
        bt_v2(0, "")
        return final_results
