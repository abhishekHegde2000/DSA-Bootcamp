'''
https://leetcode.com/problems/sum-of-two-integers/description/

371. Sum of Two Integers

Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
 

Constraints:

-1000 <= a, b <= 1000

'''
import math
from typing import List


class Solution:
    def getSum(self, a: int, b: int) -> int:
        return int(math.log(2**a*2**b, 2))


class Solution:
    def getSum(self, a: int, b: int) -> int:
        l = [a, b]
        return sum(l)
#  usinf bit manipulation


class Solution:
    def getSum(self, a: int, b: int) -> int:

        # 32 bit mask in hexadecimal
        mask = 0xffffffff

        # works both as while loop and single value check
        while (b & mask) > 0:

            carry = (a & b) << 1
            a = (a ^ b)
            b = carry

        # handles overflow
        return (a & mask) if b > 0 else a


sol = Solution()
print(sol.getSum(1, 2))  # 3
print(sol.getSum(2, 3))  # 5
print(sol.getSum(-2, 3))  # 1
