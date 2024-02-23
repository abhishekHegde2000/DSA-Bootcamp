'''

https://leetcode.com/problems/arranging-coins/

441. Arranging Coins

You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

 

Example 1:


Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:


Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
'''

from typing import List


class Solution:
    def arrangeCoins(self, total_coins: int) -> int:
        # Initialize pointers to the start and end of the range
        lower_bound = 0
        upper_bound = total_coins

        while lower_bound <= upper_bound:
            # Calculate the middle number
            potential_row_number = lower_bound + \
                (upper_bound - lower_bound) // 2
            print(f"Checking if we can fill {potential_row_number} rows")

            # Determine the appropriate action based on the total number of coins in the potential number of rows
            total_coins_in_rows = (
                potential_row_number * (potential_row_number + 1)) // 2
            if total_coins_in_rows == total_coins:
                print(f"Found that we can fill exactly {
                      potential_row_number} rows")
                return potential_row_number
            elif total_coins_in_rows > total_coins:
                print(f"We can't fill {
                      potential_row_number} rows, searching lower half.")
                upper_bound = potential_row_number - 1
            else:
                print(f"We can fill {
                      potential_row_number} rows, but maybe we can fill more, searching upper half.")
                lower_bound = potential_row_number + 1

        # Return the largest number of rows we can completely fill
        print(f"We can fill {upper_bound} rows")
        return upper_bound
