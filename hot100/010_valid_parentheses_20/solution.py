"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input: s = "()"
    Output: True

Example 2:
    Input: s = "()[]{}"
    Output: True

Example 3:
    Input: s = "(]"
    Output: False
"""


class Solution:
    """
这类题不能只看“每种括号数量是否相等”，而要看：

最近打开的括号，必须最先关闭。

这正好是 stack / 栈 的性质：Last In, First Out。
    """

    def isValid(self, s: str) -> bool:
        mapping = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = []
        for c in s:
            if c in mapping:
                rc = mapping[c]
                if not stack:
                    return False

                if stack[-1] != rc:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0
