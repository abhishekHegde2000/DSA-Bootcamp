'''
https://leetcode.com/problems/longest-palindromic-subsequence/description/

516. Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
 

Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.


'''

# space optimized


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        word1 = s
        word2 = s[::-1]

        dp = [[0 for col in range(len(word2)+1)]
              for row in range(len(word1) + 1)]

        for row in range(len(word1)-1, -1, -1):
            for col in range(len(word2)-1, -1, -1):

                if word1[row] == word2[col]:
                    dp[row][col] = 1 + dp[row+1][col+1]
                else:
                    dp[row][col] = max(dp[row+1][col], dp[row][col+1])

        return dp[0][0]


# Brute force

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        def helper(i: int, j: int) -> int:
            # Debugging print statement
            print(
                f"Calculating longest palindromic subsequence for indices {i}, {j}")

            # If indices are out of bounds, return 0
            if i < 0 or j >= len(s):
                return 0

            # If characters at indices i and j are the same
            if s[i] == s[j]:
                length = 1 if i == j else 2
                return helper(i-1, j+1) + length
            else:
                # If characters are not the same
                left = helper(i-1, j)
                right = helper(i, j+1)
                return max(left, right)

        # Initialize the maximum length of palindromic subsequence
        max_length = 0

        for i in range(len(s)):
            # Calculate the length of longest palindromic subsequence for even and odd length palindromes
            even = helper(i, i)
            odd = helper(i, i+1)

            # Update the maximum length
            max_length = max(max_length, even, odd)

        return max_length


# Memoization

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # Create a memoization table to store the results of subproblems
        memo = [[-1 for _ in range(len(s))] for _ in range(len(s))]

        def helper(i: int, j: int) -> int:
            # Debugging print statement
            print(
                f"Calculating longest palindromic subsequence for indices {i}, {j}")

            # If indices are out of bounds, return 0
            if i < 0 or j >= len(s):
                return 0

            # If we have already calculated the result for these indices, return it
            if memo[i][j] != -1:
                return memo[i][j]

            # If characters at indices i and j are the same
            if s[i] == s[j]:
                length = 1 if i == j else 2
                memo[i][j] = helper(i-1, j+1) + length
                print(f"Characters are the same, longest palindromic subsequence is {
                      memo[i][j]}")
            else:
                # If characters are not the same
                left = helper(i-1, j)
                right = helper(i, j+1)
                memo[i][j] = max(left, right)
                print(f"Characters are not the same, longest palindromic subsequence is {
                      memo[i][j]}")

            return memo[i][j]

        # Initialize the maximum length of palindromic subsequence
        max_length = 0

        for i in range(len(s)):
            # Calculate the length of longest palindromic subsequence for even and odd length palindromes
            even = helper(i, i)
            odd = helper(i, i+1)

            # Update the maximum length
            max_length = max(max_length, even, odd)

        return max_length


sol = Solution()
sol.longestPalindromeSubseq("bbbab")  # 4
sol.longestPalindromeSubseq("cbbd")  # 2
sol.longestPalindromeSubseq("a")  # 1
