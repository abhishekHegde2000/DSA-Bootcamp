'''
https://leetcode.com/problems/valid-perfect-square/

367. Valid Perfect Square

Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
 

Constraints:

1 <= num <= 231 - 1
'''

from typing import List


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Initialize pointers to the start and end of the range
        lower_bound = 1
        upper_bound = num

        while lower_bound <= upper_bound:
            # Calculate the middle number
            potential_square_root = lower_bound + \
                (upper_bound - lower_bound) // 2
            print(f"Checking if {
                  potential_square_root} is the square root of {num}")

            # Determine the appropriate action based on the square of the middle number
            if potential_square_root * potential_square_root == num:
                print(f"Found that {
                      potential_square_root} is the square root of {num}")
                return True
            elif potential_square_root * potential_square_root > num:
                print(f"Square of {potential_square_root} is greater than {
                      num}, searching lower half.")
                upper_bound = potential_square_root - 1
            else:
                print(f"Square of {potential_square_root} is less than {
                      num}, searching upper half.")
                lower_bound = potential_square_root + 1

        # Return False if no square root is found
        print("No perfect square found.")
        return False


sol = Solution()
print(sol.isPerfectSquare(16))
print(sol.isPerfectSquare(14))
