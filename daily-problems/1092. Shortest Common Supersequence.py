'''
https://leetcode.com/problems/shortest-common-supersequence/

1092. Shortest Common Supersequence 
Solved
Hard
Topics
Companies
Hint
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
'''


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        n1, n2 = len(str1), len(str2)

        dp = [[-1] * n2 for i in range(n1)]

        def lcs(i1, i2):

            if i1 >= n1 or i2 >= n2:
                return 0

            if dp[i1][i2] != -1:
                return dp[i1][i2]

            if str1[i1] == str2[i2]:
                dp[i1][i2] = 1 + lcs(i1+1, i2+1)
                return dp[i1][i2]

            else:
                right = lcs(i1, i2+1)
                down = lcs(i1+1, i2)

                dp[i1][i2] = max(right, down)
                return dp[i1][i2]

        k = lcs(0, 0)
        print("dp", dp)

        i, j = 0, 0
        res = ""
        while i < n1 and j < n2:

            if str1[i] == str2[j]:
                res += str1[i]
                i += 1
                j += 1

            else:
                if dp[i][j+1] > dp[i+1][j]:
                    res += str2[j]
                    j += 1
                else:
                    res += str1[i]
                    i += 1

        while i < n1:
            res += str1[i]
            i += 1

        while j < n2:

            res += str2[j]
            j += 1

        return res
