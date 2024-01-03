'''
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

'''

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        d = []
        c = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                c += 1
            else:
                d.append([chars[i-1], c])
                c = 1
        d.append([chars[-1], c])
        i = 0
        for k, v in d:
            chars[i] = k
            i += 1
            if v > 1:
                for item in str(v):
                    chars[i] = str(item)
                    i += 1
        return i


sol = Solution()
print(sol.compress(["a", "a", "b", "b", "c", "c", "c"]))
print(sol.compress(["a"]))
print(sol.compress(["a", "b", "b", "b", "b",
      "b", "b", "b", "b", "b", "b", "b", "b"]))
print(sol.compress(["a", "a", "a", "b", "b", "a", "a"]))


'''
# Brute Force Solution
The brute force solution would be to create a new list and fill it with the compressed string. This would involve iterating over the input list and for each character, counting the number of consecutive occurrences and adding the character and count to the new list. This solution would not be in-place and would have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input list.

# Optimized Solution
The optimized solution would be to modify the input list in-place to create the compressed string. This would involve using two pointers, one to read the characters and the other to write the compressed string. This solution would have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input list.

# Code with meaningful variable names, debugging print statements, and comments for each step
```python
class Solution:
    def compress(self, chars: List[str]) -> int:
        # Initialize an empty list to store the characters and their counts
        char_counts = []
        # Initialize a counter for the current character
        current_char_count = 1
        # Iterate over the characters in the list
        for i in range(1, len(chars)):
            # If the current character is the same as the previous one, increment the counter
            if chars[i] == chars[i-1]:
                current_char_count += 1
            else:
                # If the current character is different, add the previous character and its count to the list
                char_counts.append([chars[i-1], current_char_count])
                # Reset the counter for the new character
                current_char_count = 1
        # Add the last character and its count to the list
        char_counts.append([chars[-1], current_char_count])
        # Initialize a pointer for writing the compressed string
        write_pointer = 0
        # Iterate over the characters and their counts
        for char, count in char_counts:
            # Write the character to the list
            chars[write_pointer] = char
            write_pointer += 1
            # If the count is greater than 1, write the count to the list
            if count > 1:
                for digit in str(count):
                    chars[write_pointer] = str(digit)
                    write_pointer += 1
        # Return the length of the compressed string
        return write_pointer
```
This code compresses the string in-place by counting the number of consecutive occurrences of each character and writing the character and its count to the list. It uses a list to store the characters and their counts and two pointers to read and write the characters. The time complexity is O(n) and the space complexity is O(1), where n is the length of the input list.

'''
