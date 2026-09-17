"""
76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum
window substring of s such that every character in t (including duplicates) is
included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"

Example 2:
    Input: s = "a", t = "a"
    Output: "a"

Example 3:
    Input: s = "a", t = "aa"
    Output: ""

Constraints:
    m == s.length
    n == t.length
    1 <= m, n <= 10^5
    s and t consist of uppercase and lowercase English letters.
"""

from collections import defaultdict

class Solution:
    """
    right：负责扩大窗口
    left：负责缩小窗口
    整体节奏是：
    right 加入一个字符
        ↓
    检查窗口是否有效
        ↓
    如果有效，left 不断向右缩小
        ↓
    窗口变得无效
        ↓
    right 再加入下一个字符

    对应结构：

    for right in range(len(s)):
        # 把 s[right] 加入窗口

        while 窗口有效:
            # 更新最短答案
            # 移除 s[left]
            left += 1
    """
    def minWindow(self, s: str, t: str) -> str:
        target_map = defaultdict(int)
        for c in t:
            target_map[c] += 1

        matched_cnt = 0 # number of distinct character c that have matched_map[c] == target_map[c]
        matched_map = defaultdict(int)
        left = 0

        min_result_length = float('inf')
        min_result_str = ""

        for right in range(len(s)):
            if s[right] in target_map:
                matched_map[s[right]] += 1
                if matched_map[s[right]] == target_map[s[right]]:
                    matched_cnt += 1

            while matched_cnt == len(target_map):
                if min_result_length > right - left + 1:
                    min_result_str = s[left : right + 1]
                    min_result_length = right - left + 1

                # move left ptr, shrink the window until it does not meet the requirement
                c = s[left]
                if c in target_map:
                    matched_map[c] -= 1
                    if matched_map[c] < target_map[c]:
                        # substring [left, right] is a solution candidate, further increasing left will disquality
                        matched_cnt -= 1
                left += 1

        return min_result_str


"""
    Input: s = "abc", t = "abc"
    Output: ""

target_map = {'a': 1, 'b': 1, 'c': 1}

matched_map = {'a': 1}, matched_cnt = 1


"""
