'''
1071. Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
'''

from typing import List


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Get the lengths of the two strings
        length_str1, length_str2 = len(str1), len(str2)

        # Define a helper function to check if a length is a divisor of both lengths
        def isDivisor(length):
            print(f"Checking if {length} is a divisor")
            if length_str1 % length or length_str2 % length:
                print(f"{length} is not a divisor")
                return False
            factor1, factor2 = length_str1 // length, length_str2 // length
            result = str1[:length] * \
                factor1 == str1 and str1[:length] * factor2 == str2
            print(f"{length} is a divisor: {result}")
            return result

        # Check each possible length from the minimum length to 1
        for length in range(min(length_str1, length_str2), 0, -1):
            if isDivisor(length):
                print(f"The GCD of the strings is {str1[:length]}")
                return str1[:length]
        print("The strings have no GCD")
        return ""


sol = Solution()

print(sol.gcdOfStrings("ABCABC", "ABC"))
print(sol.gcdOfStrings("ABABAB", "ABAB"))
