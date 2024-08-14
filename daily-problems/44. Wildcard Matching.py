'''
https://leetcode.com/problems/wildcard-matching/description/

44. Wildcard Matching

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
 

Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        n, m = len(s), len(p)

        dp = [[-1] * (m+1) for i in range(n+1)]

        def isAllStars(word, curr):
            # if the remaining part of the word is all stars
            for i in range(curr, len(word)):
                if word[i] != '*':
                    return False
            return True

        def match(i, j):

            # both s and p reach the end
            if i == n and j == m:
                return True
            # if s reaches the end, then p should be all stars to match empty string
            if i == n:
                return isAllStars(p, j)
            # if p reaches the end, and s is not empty, then it can't match
            if j == m:
                return False

            if dp[i][j] != -1:
                return dp[i][j]
            # if both strings match or p has a '?', then move to the next character
            if s[i] == p[j] or p[j] == '?':
                dp[i][j] = match(i+1, j+1)

            # if p has a '*', then it can match with any sequence of characters
            elif p[j] == '*':
                delete = match(i+1, j)
                Add = match(i, j+1)
                dp[i][j] = delete or Add

            else:
                # if none of the above conditions are met, then the strings don't match
                dp[i][j] = False

            return dp[i][j]

        return match(0, 0)


sol = Solution()

print(sol.isMatch("aa", "a"))  # False
print(sol.isMatch("aa", "*"))  # True
print(sol.isMatch("cb", "?a"))  # False
