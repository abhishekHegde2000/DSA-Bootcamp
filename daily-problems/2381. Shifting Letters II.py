'''

https://leetcode.com/problems/shifting-letters-ii/description/https://leetcode.com/problems/shifting-letters-ii/description/


2381. Shifting Letters II
Medium
Topics
Companies
Hint
You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.

Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

Return the final string after all such shifts to s are applied.



Example 1:

Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
Output: "ace"
Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".
Example 2:

Input: s = "dztz", shifts = [[0,0,0],[1,1,1]]
Output: "catz"
Explanation: Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".


Constraints:

1 <= s.length, shifts.length <= 5 * 104
shifts[i].length == 3
0 <= starti <= endi < s.length
0 <= directioni <= 1
s consists of lowercase English letters.

'''
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Step 1: Initialize the difference array
        n = len(s)
        diff = [0] * (n + 1)

        # Step 2: Populate the difference array based on shifts
        for start, end, direction in shifts:
            shift_value = 1 if direction == 1 else -1
            diff[start] += shift_value
            if end + 1 < n:
                diff[end + 1] -= shift_value

        # Step 3: Compute the prefix sum to get net shifts
        net_shifts = [0] * n
        current_shift = 0
        for i in range(n):
            current_shift += diff[i]
            net_shifts[i] = current_shift

        # Step 4: Apply the shifts to the string
        result = []
        for i in range(n):
            # Calculate the new character after applying the shift
            new_char = chr(
                (ord(s[i]) - ord('a') + net_shifts[i]) % 26 + ord('a'))
            result.append(new_char)

        # Step 5: Return the final string
        return ''.join(result)


Sol = Solution()

print(Sol.shiftingLetters(s="abc", shifts=[
      [0, 1, 0], [1, 2, 1], [0, 2, 1]]))  # "ace"

print(Sol.shiftingLetters(s="dztz", shifts=[[0, 0, 0], [1, 1, 1]]))  # "catz"
