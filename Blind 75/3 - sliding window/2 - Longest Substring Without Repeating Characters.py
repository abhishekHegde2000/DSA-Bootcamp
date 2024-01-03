'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
 
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring_length = 0
        current_substring_start = 0
        unique_characters_seen = set()

        for current_char_index in range(len(s)):
            current_char = s[current_char_index]

            if current_char not in unique_characters_seen:
                unique_characters_seen.add(current_char)
                max_substring_length = max(
                    max_substring_length, current_char_index - current_substring_start + 1
                )
            else:
                # Debugging print statement
                print(f"Duplicate found: {current_char}")
                while current_char in unique_characters_seen:
                    character_to_remove = s[current_substring_start]
                    print(
                        # Debugging print statement
                        f"Removing {character_to_remove} from the window."
                    )
                    unique_characters_seen.remove(character_to_remove)
                    current_substring_start += 1
                unique_characters_seen.add(current_char)

        return max_substring_length


sol = Solution()

print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))
print(sol.lengthOfLongestSubstring("bbbbb"))
