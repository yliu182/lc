"""
394. Decode String

Given an encoded string, return its decoded string. The encoding rule is:
k[encoded_string], where the encoded_string inside the square brackets is being
repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white
spaces, square brackets are well-formed, etc. Furthermore, you may assume that
the original data does not contain any digits and that digits are only for those
repeat numbers, k.

Example 1:
    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"

Example 2:
    Input: s = "3[a2[c]]"
    Output: "accaccacc"

Example 3:
    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"

Constraints:
    - 1 <= s.length <= 30
    - s consists of lowercase English letters, digits, and square brackets '[]'.
"""


class Solution:
    '''
    关键点：
    - 栈保存的是进入括号前的外层状态。
    - 每个 [ 相当于进入一层递归。
    - 每个 ] 相当于完成当前层并返回上一层。
    - 必须正确处理多位数字。
    时间复杂度与最终解码字符串长度相关，可记为 O(output length)；栈空间与最大嵌套深度相关。
    '''
    def decodeString(self, s: str) -> str:
        prev_str = ""
        cur_num = 0
        cur_str = ""
        stack = [] #  (prev_str, prev_num) of the last layer
        for c in s:
            if c == '[':
                stack.append((cur_num, cur_str))
                cur_str = ""
                cur_num = 0
            elif c == ']':
                repeat, prev_str = stack.pop()
                cur_str = prev_str + cur_str * repeat
            elif c.isdigit():
                cur_num = 10 * cur_num + int(c)
            else:
                cur_str = cur_str + c

        return cur_str
