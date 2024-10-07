'''
https://leetcode.com/problems/minimum-string-length-after-removing-substrings/


2696. Minimum String Length After Removing Substrings
Easy
Topics
Companies
Hint
You are given a string s consisting only of uppercase English letters.

You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s.

Return the minimum possible length of the resulting string that you can obtain.

Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.

 

Example 1:

Input: s = "ABFCACDB"
Output: 2
Explanation: We can do the following operations:
- Remove the substring "ABFCACDB", so s = "FCACDB".
- Remove the substring "FCACDB", so s = "FCAB".
- Remove the substring "FCAB", so s = "FC".
So the resulting length of the string is 2.
It can be shown that it is the minimum length that we can obtain.
Example 2:

Input: s = "ACBBD"
Output: 5
Explanation: We cannot do any operations on the string so the length remains the same.
 

Constraints:

1 <= s.length <= 100
s consists only of uppercase English letters.
'''

# Brute force solution


class Solution:
    def minLength(self, s: str) -> int:
        # Continue looping until no more substrings "AB" or "CD" can be found
        while True:
            # Check if "AB" is in the string and remove it
            if "AB" in s:
                s = s.replace("AB", "")
                print(f"Removed 'AB', new string: {s}")
                continue

            # Check if "CD" is in the string and remove it
            if "CD" in s:
                s = s.replace("CD", "")
                print(f"Removed 'CD', new string: {s}")
                continue

            # If neither "AB" nor "CD" is found, break the loop
            break

        # Return the length of the resulting string
        return len(s)


class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for char in s:
            # Check if the current character and the top of the stack form "AB" or "CD"
            if stack and ((stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D')):
                # Pop the stack if a match is found
                removed_char = stack.pop()
                print(f"Removed '{removed_char}{char}', new stack: {stack}")
            else:
                # Push the current character onto the stack
                stack.append(char)
                print(f"Added '{char}', new stack: {stack}")

        # The length of the stack is the length of the resulting string
        return len(stack)


sol = Solution()

print(sol.minLength("ABFCACDB"))  # 2
print(sol.minLength("ACBBD"))  # 5
print(sol.minLength("ABCD"))  # 0
