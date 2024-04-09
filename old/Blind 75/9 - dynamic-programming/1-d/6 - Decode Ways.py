'''
https://leetcode.com/problems/decode-ways/description/

91. Decode Ways

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).

'''


class Solution:
    def numDecodings(self, s: str) -> int:
        # Initialize the memoization dictionary
        memo = {len(s): 1}

        def decode_ways(i: int) -> int:
            # If the result is in the memo, return it
            if i in memo:
                print(f"Returning memoized result for substring {s[i:]}")
                return memo[i]

            # If the character at index i is "0", there's no way to decode it
            if s[i] == "0":
                print(f"Character at index {
                      i} is '0', so there's no way to decode substring {s[i:]}")
                return 0

            # Calculate the number of ways to decode the string if we take the character at index i as a single digit
            ways = decode_ways(i + 1)
            print(f"Number of ways to decode substring {
                  s[i:]} if we take character at index {i} as a single digit: {ways}")

            # If the next two characters form a valid two-digit number, calculate the number of ways to decode the string if we take them as a two-digit number
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                ways += decode_ways(i + 2)
                print(f"Number of ways to decode substring {s[i:]} if we take characters at index {
                      i} and {i + 1} as a two-digit number: {ways}")

            # Store the result in the memo
            memo[i] = ways
            return ways

        # Calculate the number of ways to decode the entire string
        return decode_ways(0)


sol = Solution()

print(sol.numDecodings("12"))  # 2
print(sol.numDecodings("226"))  # 3
print(sol.numDecodings("06"))  # 0
