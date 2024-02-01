'''
https://leetcode.com/problems/counting-bits/description/

338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
 

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?

'''

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize an array dp to store the count of 1's for each number from 0 to n.
        dp = [0] * (n + 1)

        # The offset variable helps in creating a pattern while traversing the array.
        # Initially set offset to 1.
        offset = 1

        # Iterate over the numbers from 1 to n.
        for i in range(1, n + 1):
            # When i is a power of 2, update the offset.
            if i == offset * 2:
                offset = i

            # The count of 1's for i is 1 plus the count for the number obtained by subtracting the offset.
            dp[i] = 1 + dp[i - offset]

        # Return the array containing the count of 1's for each number from 0 to n.
        return dp


sol = Solution()

print(sol.countBits(2))  # [0,1,1]
print(sol.countBits(5))  # [0,1,1,2,1,2]
