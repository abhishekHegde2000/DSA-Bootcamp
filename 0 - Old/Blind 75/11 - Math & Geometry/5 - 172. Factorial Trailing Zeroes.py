'''
https://leetcode.com/problems/factorial-trailing-zeroes/?envType=study-plan-v2&envId=top-interview-150

172. Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0
 

Constraints:

0 <= n <= 104
 

Follow up: Could you write a solution that works in logarithmic time complexity?


'''
from typing import List


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count_of_fives = 0

        while n > 0:
            print(f"Current value of n: {n}")
            n //= 5
            print(f"Value of n after division by 5: {n}")
            count_of_fives += n
            print(f"Current count of fives: {count_of_fives}")

        return count_of_fives


sol = Solution()

print(sol.trailingZeroes(100000000000000000000000))  # 0
print(sol.trailingZeroes(5))  # 1
print(sol.trailingZeroes(0))  # 0
