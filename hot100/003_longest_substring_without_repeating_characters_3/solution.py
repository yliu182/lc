"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating
characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        left = 0
        right = 1
        dedup_set = {s[0]}
        max_result = 1
        while right < len(s):
            if s[right] not in dedup_set:
                dedup_set.add(s[right])
                right += 1
                max_result = max(max_result, len(dedup_set))
            else:
                first_ocur_idx = s[left:right].find(s[right])
                for i in range(first_ocur_idx + 1 - left):
                    dedup_set.remove(s[i + left])
                left = first_ocur_idx + 1
                dedup_set.add(s[right])
                right += 1

        return max_result



# "bbbb"
#  l
#   r

# left  1
# right 2
# first_ocur_idx 0
# max_result
# dedup_set {b}
