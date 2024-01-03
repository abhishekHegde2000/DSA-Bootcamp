'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 
'''


# Intuition
# The idea is to use the sliding window technique to find the minimum window
# in str1 that contains all characters from str2.

# Approach
# We use two hashmaps to keep track of the characters in str2 (countT)
# and the characters in the current window (window).
# We iterate through str1 using two pointers (l and r) to create a window.
# The "have" variable keeps track of the characters in the current window
# that match the characters in str2. The "need" variable is the total
# number of distinct characters in str2.

# Pseudo Code
"""
Initialize countT and window hashmaps
Initialize result pointers and result length
Initialize variables have and need to track matching characters
Use two pointers (l and r) to iterate through str1
    Update window hashmap for the current character
    Check if the character is in str2 and the count matches
        Increment have if a match is found
    Check if have is equal to need
        Update the result if the current window is smaller
        Decrease the window size from the left side
            Update the result if the new window is smaller
            Update have and l pointer
Return the minimum window substring
"""

# Complexity
# Time complexity: O(n), where n is the length of str1
# Space complexity: O(m), where m is the number of distinct characters in str2


class Solution:

    def minWindow(self, str1: str, str2: str) -> str:

        if len(str1) < len(str2):
            return ""

        # Initialize hashmaps
        countT, window = {}, {}

        # Count characters in str2
        for c in str2:
            countT[c] = 1 + countT.get(c, 0)

        # Initialize result pointers and length
        result = [-1, -1]
        resLen = float("infinity")

        # Initialize variables to track matching characters
        have, need = 0, len(countT)

        # Initialize pointers
        l = 0

        # Iterate through str1
        for r in range(len(str1)):
            chr = str1[r]

            # Update window hashmap
            window[chr] = 1 + window.get(chr, 0)

            # Check for a match in str2
            if chr in countT and window[chr] == countT[chr]:
                have += 1

            # Check if all characters in str2 are found
            while have == need:
                # Update result if the current window is smaller
                if (r - l + 1) < resLen:
                    result = [l, r]
                    resLen = (r - l + 1)

                # Decrease window size from the left
                window[str1[l]] -= 1

                # Check if the character is in str2
                if str1[l] in countT and window[str1[l]] < countT[str1[l]]:
                    have -= 1

                # Move left pointer
                l += 1

        l, r = result
        return str1[l:r+1] if resLen != float("infinity") else ""
