'''

https://leetcode.com/problems/sqrtx/

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

'''

from typing import List


class Solution:
    def mySqrt(self, x: int) -> int:
        # Initialize pointers to the start and end of the range
        lower_bound = 1
        upper_bound = x

        while lower_bound <= upper_bound:
            # Calculate the middle number
            potential_square_root = lower_bound + \
                (upper_bound - lower_bound) // 2
            print(f"Checking if {
                  potential_square_root} is the square root of {x}")

            # Determine the appropriate action based on the square of the middle number
            if potential_square_root * potential_square_root == x:
                print(f"Found that {
                      potential_square_root} is the square root of {x}")
                return potential_square_root
            elif potential_square_root * potential_square_root > x:
                print(f"Square of {potential_square_root} is greater than {
                      x}, searching lower half.")
                upper_bound = potential_square_root - 1
            else:
                print(f"Square of {potential_square_root} is less than {
                      x}, searching upper half.")
                lower_bound = potential_square_root + 1

        # Return False if no square root is found
        print("No perfect square found.")
        return upper_bound
