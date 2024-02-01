'''
https://leetcode.com/problems/number-of-1-bits/description/

191. Number of 1 Bits

Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
 

Example 1:

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
 

Constraints:

The input must be a binary string of length 32.
 

Follow up: If this function is called many times, how would you optimize it?

'''


class Solution:
    def hammingWeight(self, n: int) -> int:
        bitCount = 0
        print(f"Initial number: {number}")

        while number:
            # Count the least significant bit of the number
            bitCount += number % 2
            print(f"Current bit count: {bitCount}")
            # Right shift the number by 1 bit
            number = number >> 1
            print(f"Number after right shift: {number}")

        return bitCount


class Solution:
    def hammingWeight(self, number: int) -> int:

        # Initialize the count of 1 bits
        oneBitCount = 0
        print(f"Initial number: {number}")

        while number:
            # Perform a bitwise AND operation between number and number - 1
            number = number & (number - 1)
            print(f"Number after bitwise AND operation: {number}")
            # Increment the count of 1 bits
            oneBitCount += 1
            print(f"Current count of 1 bits: {oneBitCount}")

        return oneBitCount


sol = Solution()
# print(sol.hammingWeight(00000000000000000000000000001011)) # 3
# print(sol.hammingWeight(00000000000000000000000010000000)) # 1
print(sol.hammingWeight(11111111111111111111111111111101))  # 31
