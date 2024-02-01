'''
https://leetcode.com/problems/longest-common-subsequence/description/

1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.



'''


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[0 for col in range(len(text2)+1)]
              for row in range(len(text1)+1)]
        print(f"dp: {dp}")

        for r in range(len(text1) - 1, -1, -1):
            for c in range(len(text2) - 1, -1, -1):

                if text1[r] == text2[c]:
                    dp[r][c] = 1 + dp[r+1][c+1]
                else:
                    dp[r][c] = max(dp[r+1][c], dp[r][c+1])

        print(f"dp: {dp}")
        return dp[0][0]

# Memoization


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[-1 for j in range(len(text2))] for i in range(len(text1))]

        def helper(r, c):

            if r < 0 or c < 0:
                return 0

            if dp[r][c] != -1:
                return dp[r][c]

            if text1[r] == text2[c]:
                dp[r][c] = 1 + helper(r-1, c-1)
                return dp[r][c]
            else:
                dp[r][c] = max(helper(r-1, c), helper(r, c-1))
                return dp[r][c]

        return helper(len(text1)-1, len(text2)-1)


sol = Solution()

print(sol.longestCommonSubsequence(text1="abcde", text2="ace"))  # 3
print(sol.longestCommonSubsequence(text1="abc", text2="abc"))  # 3
print(sol.longestCommonSubsequence(text1="abc", text2="def"))  # 0
