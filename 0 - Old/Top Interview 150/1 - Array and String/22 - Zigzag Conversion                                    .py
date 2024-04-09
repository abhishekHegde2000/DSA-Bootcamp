'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
'''

from typing import List


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If the number of rows is 1, return the string as it is
        if numRows == 1:
            return s

        # Initialize an empty string for each row
        rows = [''] * numRows
        current_row = 0
        direction_down = False

        # Iterate over the characters in the string
        for char in s:
            # Add each character to the appropriate row
            rows[current_row] += char
            print(f"Adding {char} to row {current_row}")
            # Change the direction when the first or last row is reached
            if current_row == 0 or current_row == numRows - 1:
                direction_down = not direction_down
                print(
                    f"Changing direction to {'down' if direction_down else 'up'}")
            current_row += 1 if direction_down else -1

        # After all characters are placed, concatenate the rows to get the final result
        return ''.join(rows)


sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))
print(sol.convert("PAYPALISHIRING", 4))
print(sol.convert("A", 1))
