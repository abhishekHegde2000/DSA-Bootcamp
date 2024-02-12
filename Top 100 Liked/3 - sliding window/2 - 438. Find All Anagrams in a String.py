'''

https://leetcode.com/problems/find-all-anagrams-in-a-string/description/?envType=study-plan-v2&envId=top-100-liked

438. Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.

'''
# Brute force to get window of each and check the count
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []  # Empty list if p is longer than s

        p_counts = {}
        for c in p:
            p_counts[c] = 1 + p_counts.get(c, 0)

        result = []
        for start in range(len(s) - len(p) + 1):
            s_counts = {}
            for i in range(start, start + len(p)):
                s_counts[s[i]] = 1 + s_counts.get(s[i], 0)

            if s_counts == p_counts:
                result.append(start)

        return result


# sliding window


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        pCount, sCount = {}, {}

        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

        res = [0] if sCount == pCount else []
        l = 0

        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1

            if sCount[s[l]] == 0:
                sCount.pop(s[l])

            l += 1

            if sCount == pCount:
                res.append(l)

        return res


class Solution:
    def findAnagrams(self, input_string: str, pattern_string: str) -> List[int]:
        # If the length of the pattern string is greater than the length of the input string, return an empty list
        if len(pattern_string) > len(input_string):
            return []

        # Initialize two dictionaries for the frequency counts of characters in the pattern string and the first window of the input string
        pattern_counts = {}
        window_counts = {}

        # Iterate over the pattern string and the first window of the input string and update the frequency counts in the dictionaries
        for i in range(len(pattern_string)):
            pattern_counts[pattern_string[i]] = 1 + \
                pattern_counts.get(pattern_string[i], 0)
            window_counts[input_string[i]] = 1 + \
                window_counts.get(input_string[i], 0)
        print(f"Pattern counts: {pattern_counts}")
        print(f"Window counts: {window_counts}")

        # If the two dictionaries are equal, initialize the result list with 0. Otherwise, initialize an empty result list
        result = [0] if window_counts == pattern_counts else []
        print(f"Result: {result}")

        # Initialize a left pointer at 0
        left_pointer = 0

        # Iterate over the input string from the length of the pattern string to the end
        for right_pointer in range(len(pattern_string), len(input_string)):
            # Update the frequency count of the current character in the input string dictionary
            window_counts[input_string[right_pointer]] = 1 + \
                window_counts.get(input_string[right_pointer], 0)
            print(f"Window counts after adding right pointer: {window_counts}")

            # Decrease the frequency count of the character at the left pointer in the input string dictionary
            window_counts[input_string[left_pointer]] -= 1
            print(f"Window counts after subtracting left pointer: {
                  window_counts}")

            # If the frequency count of the character at the left pointer in the input string dictionary is 0, remove it from the dictionary
            if window_counts[input_string[left_pointer]] == 0:
                window_counts.pop(input_string[left_pointer])
                print(f"Window counts after popping: {window_counts}")

            # Move the left pointer to the right
            left_pointer += 1
            print(f"Moving left pointer to: {left_pointer}")

            # If the input string dictionary is equal to the pattern string dictionary, append the left pointer to the result list
            if window_counts == pattern_counts:
                result.append(left_pointer)
                print(f"Result: {result}")

        # Return the result list
        return result


sol = Solution()

# Test case 1: Basic test case with anagrams
print(sol.findAnagrams("cbaebabacd", "abc"))  # Expected output: [0, 6]

# Test case 2: Basic test case with no anagrams
print(sol.findAnagrams("abcd", "efg"))  # Expected output: []

# Test case 3: Test case with empty string and non-empty pattern
print(sol.findAnagrams("", "abc"))  # Expected output: []

# Test case 4: Test case with non-empty string and empty pattern
print(sol.findAnagrams("abc", ""))  # Expected output: []

# Test case 5: Test case with both strings being empty
print(sol.findAnagrams("", ""))  # Expected output: []

# Test case 6: Test case with repeated characters in the pattern
print(sol.findAnagrams("ababababab", "aba"))  # Expected output: [0, 2, 4, 6]
