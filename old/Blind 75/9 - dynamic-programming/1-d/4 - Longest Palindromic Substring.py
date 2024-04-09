'''
https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        string_length = len(s)
        max_length = 0
        longest_palindrome = ""

        for i in range(string_length):
            # For odd length palindrome
            left, right = i, i
            while left >= 0 and right < string_length and s[left] == s[right]:
                print(f"Odd length palindrome: {s[left:right+1]}")
                if right - left + 1 > max_length:
                    longest_palindrome = s[left:right+1]
                    max_length = right - left + 1
                right += 1
                left -= 1

            # For even length palindrome
            left, right = i, i + 1
            while left >= 0 and right < string_length and s[left] == s[right]:
                print(f"Even length palindrome: {s[left:right+1]}")
                if right - left + 1 > max_length:
                    longest_palindrome = s[left:right+1]
                    max_length = right - left + 1
                right += 1
                left -= 1

        return longest_palindrome


sol = Solution()

print(sol.longestPalindrome("babad"))  # "bab"
print(sol.longestPalindrome("cbbd"))  # "bb"
print(sol.longestPalindrome("a"))  # "a"
