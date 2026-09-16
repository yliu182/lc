"""
72. Edit Distance

Given two strings word1 and word2, return the minimum number of operations
required to convert word1 to word2.

You have the following three operations permitted on a word:
    - Insert a character
    - Delete a character
    - Replace a character

Example 1:
    Input: word1 = "horse", word2 = "ros"
    Output: 3

Example 2:
    Input: word1 = "intention", word2 = "execution"
    Output: 5

Constraints:
    0 <= word1.length, word2.length <= 500
    word1 and word2 consist of lowercase English letters.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        dp[i][j] be the "min number of edits to change 'word1[of length i]' to 'word2[of length j]'"

        if word1[i] == word2[j]
            return dp[i-1][j-1]
        else:
            case 1: insertion, insert word2[j] in the end of word1
            case 2: deletion, remove word1[i] from the end of word1
            case 3: replace, change word1[i] to be word2[j]
        """
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # initialization
        dp[0][0] = 0

        for i in range(1, m+1):
            dp[i][0] = i

        for i in range(1, n+1):
            dp[0][i] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # case 1: dp[i-1][j]
                    # case 2: dp[i][j-1]
                    # case 3: dp[i-1][j-1]
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

        return dp[m][n]
