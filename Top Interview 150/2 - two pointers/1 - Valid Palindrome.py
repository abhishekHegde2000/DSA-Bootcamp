'''
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
        # Convert the string to lowercase
        s = s.lower()
        print(f"Lowercase string: {s}")

        # Initialize two pointers
        leftPointer, rightPointer = 0, len(s) - 1

        # While the left pointer is less than the right pointer
        while leftPointer < rightPointer:
            # If the character at the left pointer is not alphanumeric
            while leftPointer < rightPointer and not s[leftPointer].isalnum():
                leftPointer += 1
                print(f"Moved left pointer to the right: {leftPointer}")

            # If the character at the right pointer is not alphanumeric
            while leftPointer < rightPointer and not s[rightPointer].isalnum():
                rightPointer -= 1
                print(f"Moved right pointer to the left: {rightPointer}")

            # If the characters at the left pointer and the right pointer are not equal
            if s[leftPointer] != s[rightPointer]:
                print(
                    f"Characters at left pointer ({s[leftPointer]}) and right pointer ({s[rightPointer]}) are not equal")
                return False

            # Move the left pointer to the right and the right pointer to the left
            leftPointer += 1
            rightPointer -= 1
            print(
                f"Moved left pointer to the right: {leftPointer}, Moved right pointer to the left: {rightPointer}")

        # The string is a palindrome
        print("The string is a palindrome")
        return True
