'''

392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 
'''

from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        n, m = len(s), len(t)

        if s == None or t == None:
            return None

        if n == 0:
            return True

        while i < n and j < m:

            if s[i] == t[j]:
                i += 1
            j += 1
        return (i == n)


sol = Solution()
print(sol.isSubsequence("abc", "ahbgdc"))
print(sol.isSubsequence("axc", "ahbgdc"))
