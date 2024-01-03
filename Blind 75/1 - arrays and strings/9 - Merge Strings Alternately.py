'''
1768. Merge Strings Alternately


You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

'''
from typing import List


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Get the lengths of the two words
        length_word1 = len(word1)
        length_word2 = len(word2)

        # Initialize an empty string to store the result
        merged_word = ''

        # Initialize two pointers to iterate over the two words
        pointer_word1, pointer_word2 = 0, 0

        # While both pointers are within the lengths of their respective words
        while pointer_word1 < length_word1 and pointer_word2 < length_word2:
            # Add the current characters from both words to the result
            merged_word += word1[pointer_word1]
            pointer_word1 += 1
            merged_word += word2[pointer_word2]
            pointer_word2 += 1

        print(
            f"Pointer positions: word1 - {pointer_word1}, word2 - {pointer_word2}")

        # If all characters from word1 have been added to the result
        if pointer_word1 >= length_word1:
            # Add the remaining characters from word2 to the result
            merged_word += word2[pointer_word2:]
            return merged_word

        # Add the remaining characters from word1 to the result
        merged_word += word1[pointer_word1:]
        return merged_word


sol = Solution()
print(sol.mergeAlternately("abc", "pqr"))
print(sol.mergeAlternately("ab", "pqrs"))
print(sol.mergeAlternately("abcd", "pq"))
