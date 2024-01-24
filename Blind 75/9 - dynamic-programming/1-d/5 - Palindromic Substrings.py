'''
https://leetcode.com/problems/palindromic-substrings/description/

647. Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.


'''


class Solution:
    def countSubstrings(self, s: str) -> int:
        # Initialize the count of palindromic substrings
        palindrome_count = 0
        # Get the length of the string
        string_length = len(s)

        # Iterate over each character in the string
        for center in range(string_length):
            # Initialize the left and right pointers at the center
            left, right = center, center

            # Expand the left and right pointers while the substring is a palindrome
            while left >= 0 and right < string_length and s[left] == s[right]:
                print(f"Odd length palindrome: {s[left:right+1]}")
                palindrome_count += 1
                right += 1
                left -= 1

            # Reset the left and right pointers for even length palindrome
            left, right = center, center + 1

            # Expand the left and right pointers while the substring is a palindrome
            while left >= 0 and right < string_length and s[left] == s[right]:
                print(f"Even length palindrome: {s[left:right+1]}")
                palindrome_count += 1
                right += 1
                left -= 1

        # Return the count of palindromic substrings
        return palindrome_count


class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        def backtrack(start: int, path: str, result: list) -> None:
            if path:  # Only append non-empty strings
                result.append(path)
            for i in range(start, len(s)):
                backtrack(i + 1, path + s[i], result)

        substrings = []
        backtrack(0, "", substrings)
        palindrome_count = 0

        for substring in substrings:
            if is_palindrome(substring):
                palindrome_count += 1

        return palindrome_count


sol = Solution()

print(sol.countSubstrings("abc"))  # 3
print(sol.countSubstrings("aaa"))  # 6


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True
            count += 1

        # Check for substring of length 2.
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1

        # Check for substrings of length 3 to n
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    count += 1

        return count


class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = {}  # Create a memo dictionary

        def is_palindrome(start: int, end: int) -> bool:
            # If the result is in the memo, return it
            if (start, end) in memo:
                return memo[(start, end)]

            # If the substring has less than 2 characters, it's a palindrome
            if start >= end:
                memo[(start, end)] = True
            # If the first and last characters are the same, check the substring in between
            elif s[start] == s[end]:
                memo[(start, end)] = is_palindrome(start + 1, end - 1)
            # If the first and last characters are different, it's not a palindrome
            else:
                memo[(start, end)] = False

            return memo[(start, end)]

        count = 0
        for start in range(len(s)):
            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    count += 1

        return count
