''' 

Code

125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

'''

from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left_pointer = 0
        right_pointer = len(s) - 1
        while left_pointer < right_pointer:
            if not s[left_pointer].isalnum():
                left_pointer += 1
            elif not s[right_pointer].isalnum():
                right_pointer -= 1
            elif s[left_pointer] != s[right_pointer]:
                return False
            else:
                left_pointer += 1
                right_pointer -= 1
        return True


sol = Solution()

print(sol.isPalindrome("A man, a plan, a canal: Panama"))


'''
# Intuition
The problem is asking to determine if a given string is a palindrome, considering only alphanumeric characters and ignoring cases. 

# Approach
The approach is to use two pointers, one starting from the beginning of the string and the other from the end. We move the pointers towards each other, skipping non-alphanumeric characters, and compare the characters they point to. If at any point the characters are not equal, we return `False`. If we finish the loop without finding unequal characters, we return `True`.

# Pseudo Code
```
convert s to lowercase
initialize left_pointer to 0 and right_pointer to len(s) - 1
while left_pointer is less than right_pointer
    if character at left_pointer is not alphanumeric
        increment left_pointer
    else if character at right_pointer is not alphanumeric
        decrement right_pointer
    else if characters at left_pointer and right_pointer are not equal
        return False
    else
        increment left_pointer and decrement right_pointer
return True
```

# Complexity
- Time complexity: O(n), where n is the length of `s`. This is because we are checking each character in the string once.
- Space complexity: O(1), excluding the input and output. This is because we are not using any additional data structures that scale with the size of the input.

# Code
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left_pointer = 0
        right_pointer = len(s) - 1
        while left_pointer < right_pointer:
            if not s[left_pointer].isalnum():
                left_pointer += 1
            elif not s[right_pointer].isalnum():
                right_pointer -= 1
            elif s[left_pointer] != s[right_pointer]:
                return False
            else:
                left_pointer += 1
                right_pointer -= 1
        return True
```

'''
