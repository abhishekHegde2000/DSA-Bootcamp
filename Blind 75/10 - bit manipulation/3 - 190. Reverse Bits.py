'''

https://leetcode.com/problems/reverse-bits/description/

190. Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 

Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
 

Constraints:

The input must be a binary string of length 32
 

Follow up: If this function is called many times, how would you optimize it?

'''


class Solution:
    def reverseBits(self, n: int) -> int:
        # Initialize a variable to hold the reversed bits of the input number.
        reversed_bits = 0
        print(f"Initial reversed_bits: {reversed_bits}")

        # Iterate over the range from 0 to 31.
        for i in range(32):
            print(f"\nCurrent iteration: {i}")

            # Extract the ith bit from the input number.
            bit = (n >> i) & 1
            print(f"Extracted bit: {bit}")

            # Left shift bit by (31 - i) places and perform a bitwise OR operation with reversed_bits.
            reversed_bits = (bit << (31 - i)) | reversed_bits
            print(f"Updated reversed_bits: {reversed_bits}")

        # Return reversed_bits which now holds the reversed bits of the input number.
        return reversed_bits


sol = Solution()

# 964176192 (00111001011110000010100101000000)
print(sol.reverseBits(0b00000010100101000001111010011100))
# 3221225471 (10111111111111111111111111111111)
print(sol.reverseBits(0b11111111111111111111111111111101))
