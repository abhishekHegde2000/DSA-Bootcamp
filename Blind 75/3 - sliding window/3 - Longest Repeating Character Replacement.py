'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

'''


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize variables: left pointer, maximum length, and character frequency dictionary
        left_pointer = 0
        max_length = 0
        char_frequency = {}

        # Iterate over the string with the right pointer
        for right_pointer in range(len(s)):
            # Update the frequency of the current character in the dictionary
            char_frequency[s[right_pointer]] = 1 + \
                char_frequency.get(s[right_pointer], 0)

            # Check if the current window is not repeatable (exceeds k replacements)
            while (right_pointer - left_pointer + 1) - max(char_frequency.values()) > k:
                # Move the left pointer to the right and update character frequency
                char_frequency[s[left_pointer]] -= 1
                left_pointer += 1

            # Update the maximum length with the current window size
            max_length = max(max_length, right_pointer - left_pointer + 1)

        # Return the final maximum length
        return max_length
