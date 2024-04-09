'''
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
        # Initialize two pointers
        sPointer, tPointer = 0, 0

        # While the sPointer is less than the length of s and the tPointer is less than the length of t
        while sPointer < len(s) and tPointer < len(t):
            # If the characters at the sPointer and tPointer are equal
            if s[sPointer] == t[tPointer]:
                # Move the sPointer to the right
                sPointer += 1
                print(f"Moved sPointer to the right: {sPointer}")

            # Move the tPointer to the right
            tPointer += 1
            print(f"Moved tPointer to the right: {tPointer}")

        # Return true if the sPointer is equal to the length of s
        return sPointer == len(s)


sol = Solution()
print(sol.isSubsequence("abc", "ahbgdc"))
print(sol.isSubsequence("axc", "ahbgdc"))
