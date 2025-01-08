'''
https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/

1930. Unique Length-3 Palindromic Subsequences
Solved
Medium
Topics
Companies
Hint
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".


Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
Example 2:

Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
Example 3:

Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")


Constraints:

3 <= s.length <= 105
s consists of only lowercase English letters.
'''


from collections import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        ans = 0

        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            between = set()

            for k in range(i + 1, j):
                between.add(s[k])

            ans += len(between)

        return ans


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26

        for i in range(len(s)):
            curr = ord(s[i]) - ord("a")
            if first[curr] == -1:
                first[curr] = i

            last[curr] = i

        ans = 0
        for i in range(26):
            if first[i] == -1:
                continue

            between = set()
            for j in range(first[i] + 1, last[i]):
                between.add(s[j])

            ans += len(between)

        return ans


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        res = set()
        left = set()
        right = Counter(s)

        for middle_char in s:
            right[middle_char] -= 1

            for left_char in left:
                if right[left_char] > 0:
                    res.add(left_char + middle_char + left_char)

            left.add(middle_char)

        return len(res)


sol = Solution()

print(sol.countPalindromicSubsequence("aabca") == 3)
print(sol.countPalindromicSubsequence("adc") == 0)
print(sol.countPalindromicSubsequence("bbcbaba") == 4)


# dp and dfs, do not try

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        left = [[False] * 26 for _ in range(n)]
        right = [[False] * 26 for _ in range(n)]

        # Fill left array
        for i in range(1, n):
            for j in range(26):
                left[i][j] = left[i-1][j]
            left[i][ord(s[i-1]) - ord('a')] = True

        # Fill right array
        for i in range(n-2, -1, -1):
            for j in range(26):
                right[i][j] = right[i+1][j]
            right[i][ord(s[i+1]) - ord('a')] = True

        unique_palindromes = set()

        # Check for palindromic subsequences
        for i in range(1, n-1):
            for j in range(26):
                if left[i][j] and right[i][j]:
                    unique_palindromes.add(
                        chr(j + ord('a')) + s[i] + chr(j + ord('a')))

        return len(unique_palindromes)


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        def dfs(start, path):
            if len(path) == 3:
                if path[0] == path[2]:  # Check if it's a palindrome
                    palindromes.add(path)
                return

            for i in range(start, len(s)):
                dfs(i + 1, path + s[i])

        palindromes = set()
        dfs(0, "")
        return len(palindromes)


sol = Solution()

print(sol.countPalindromicSubsequence("aabca") == 3)
print(sol.countPalindromicSubsequence("adc") == 0)
print(sol.countPalindromicSubsequence("bbcbaba") == 4)
