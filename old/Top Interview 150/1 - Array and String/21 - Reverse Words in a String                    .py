'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
'''

from typing import List


class Solution:
    def reverseWords(self, input_string: str) -> str:
        # Strip the input string and split it into a list of words
        word_list = input_string.strip().split(' ')

        # Initialize an empty list to store the non-empty words
        non_empty_words = []

        # Iterate over the list of words and add the non-empty words to the new list
        for word in word_list:
            if word:
                non_empty_words.append(word)

        print("Initial Array: ", non_empty_words)

        # Initialize two pointers at the start and end of the list
        left, right = 0, len(non_empty_words) - 1

        # Swap the words at the positions of the two pointers and move the pointers towards the center of the list
        while left <= right:
            non_empty_words[left], non_empty_words[right] = non_empty_words[right], non_empty_words[left]
            print("Swapped Array: ", non_empty_words)
            left += 1
            right -= 1

        # Join the words in the list into a string with spaces in between and return it
        return ' '.join(non_empty_words)


obj = Solution()

print(obj.reverseWords("Let's take LeetCode contest"))
print(obj.reverseWords("  hello world  "))
print(obj.reverseWords("a good   example"))
