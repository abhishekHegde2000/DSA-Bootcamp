'''
https://leetcode.com/problems/minimize-xor

2429. Minimize XOR
Medium
Topics
Companies
Hint
Given two positive integers num1 and num2, find the positive integer x such that:

x has the same number of set bits as num2, and
The value x XOR num1 is minimal.
Note that XOR is the bitwise XOR operation.

Return the integer x. The test cases are generated such that x is uniquely determined.

The number of set bits of an integer is the number of 1's in its binary representation.



Example 1:

Input: num1 = 3, num2 = 5
Output: 3
Explanation:
The binary representations of num1 and num2 are 0011 and 0101, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.
Example 2:

Input: num1 = 1, num2 = 12
Output: 3
Explanation:
The binary representations of num1 and num2 are 0001 and 1100, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.


Constraints:

1 <= num1, num2 <= 109


'''


'''
editorial


Minimize XOR

LeetCode
8994
Jan 11, 2025
Editorial
Solution
Overview
We are given two integers, num1 and num2. Our task is to find an integer result, such that:

result has the same number of set bits (1s in its binary representation) as num2.
The value of result XOR num1 is as close to 0 as possible, meaning the two numbers result and num1 should differ in as few bit positions as possible.
Note: The XOR operation compares the bits of two numbers. A bit in the result is 1 if the bits at that position in the two numbers are different, and 0 if they are the same.

Let’s go over some essential bitmasking operations that will be useful in solving the problem:

To check if the i-th bit of num is set:

Shift 1 left by i (1 << i) positions to isolate the i-th bit.
Perform a bitwise AND: num & (1 << i).
If the result is not 0, the i-th bit of num is set.

Current

To set the i-th bit of num:

Shift 1 left by i (1 << i) positions to isolate the i-th bit.
Perfom a bitwise OR: num | (1 << i).
Current

To unset the i-th bit of num:

Shift 1 left by i (1 << i) positions to create a mask.
Invert the mask using ~(1 << i) to make the i-th bit 1 and all the other bits 0.
Perform a bitwise AND: num & ~(1 << i).
Current

For a more comprehensive understanding of bit manipulation, check out the Bit Manipulation Explore Card 🔗. This resource provides an in-depth look at bit-level operations, explaining their key concepts and applications with a variety of problems to solidify understanding of the pattern.

Approach 1: From Optimal to Valid
Intuition
A simple observation is that if there were no constraints, the best choice for result would be num1 itself because: num1 XOR num1 = 0 (all bits match, resulting in no differences).
However, result must also have the same number of set bits as num2, so we cannot always use num1 as is. To make result valid, we need to adjust it to match the number of set bits in num2 while trying to keep it as close to num1 as possible. A good way to adjust result is as follows:

Start with result = num1.
Compare the number of set bits in result and num2:
If result has more set bits than num2, we remove extra 1s from result by unsetting bits, starting from the least significant bits (because they are less important for matching num1 closely).
If result has fewer set bits than num2, we add more 1s to result by setting bits, starting from the least significant unset bits.
Algorithm
Initialize result to num1.
Initialize targetSetBitsCount to the number of set bits in num2 and setBitsCount to the number of set bits in result, using the provided built-in function.
Initialize currentBit to 0 (the least significant).
While result has fewer set bits than num2 (i.e., setBitsCount < targetSetBitsCount):
If the currentBit of result is unset:
Set it.
Increment setBitsCount by 1.
Move to the next bit; increment currentBit by 1.
While result has more set bits than num2 (i.e., setBitsCount > targetSetBitsCount):
If the currentBit of result is set:
Unset it.
Decrement setBitsCount by 1.
Move to the next bit; increment currentBit by 1.
Return result.
Implementation

Complexity Analysis
Let n be the maximum possible value of num1 or num2.

Time Complexity: O(logn).

The time complexity of the given solution is O(logn). This is because the algorithm primarily involves two operations: counting the number of set bits in the integers and adjusting the set bits of result to match the target count. The counting of set bits requires iterating over the binary representation of the integer, which takes O(logn) time since the number of bits in an integer is proportional to logn.

Additionally, the while loops iterate over the bits of result, setting or unsetting bits as needed, which also takes logn time in the worst case, as we may need to process up to all 32 bits. The helper functions (isSet, setBit, and unsetBit) involve constant-time bitwise operations and do not impact the overall complexity.

As a result, the time complexity is dominated by the bit manipulation and bit counting operations, both of which are O(logn).

Space Complexity: O(1).

We only use a fixed number of variables and therefore the algorithm requires constant extra space.

Approach 2: Building the Answer
Intuition
In this approach, we build the result from scratch instead of adjusting an existing answer. The idea is to start setting bits of result that match the set bits of num1, starting from the most significant bits, and continue until result has the same number of set bits as num2.

By setting bits from the most significant positions first, we ensure that result remains as close as possible to num1. Higher bits contribute more to the numerical value of a number, so matching them helps reduce the differences between result and num1.

If there aren’t enough set bits in the higher positions, we use the lower bits to "fill in" the remaining set bits required to meet the condition of num2. This ensures that result has the correct number of set bits while maintaining as much similarity to num1 as possible.

Algorithm
Initialize result to 0.
Initialize targetSetBitsCount to the number of set bits in num2 and setBitsCount to 0.
Initialize currentBit to 31 (the most significant).
While result has fewer set bits than num2 (i.e. setBitsCount < targetSetBitsCount):
If the currentBit of num1 is set or we must set all remaining bits in result (i.e. targetSetBitsCount - setBitsCount > currentBit):
Set the currentBit of result.
Increment setBitsCount by 1.
Move to the next bit; decrement currentBit by 1.
Return result.
Implementation

Complexity Analysis
Let n be the maximum possible value of num1 or num2.

Time Complexity: O(logn).

Like in the previous approach, the algorithm involves iterating over the bits of the numbers, which is proportional to logn.

Space Complexity: O(1).

The algorithm uses only a fixed number of variables which does not depend on the input.

'''


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Initialize result to num1. We will modify result.
        result = num1

        target_set_bits_count = bin(num2).count("1")
        set_bits_count = bin(result).count("1")

        # Start with the least significant bit (bit 0).
        current_bit = 0

        # Add bits to result if it has fewer set bits than the target.
        while set_bits_count < target_set_bits_count:
            # If the current bit in result is not set (0), set it to 1.
            if not self._is_set(result, current_bit):
                result = self._set_bit(result, current_bit)
                set_bits_count += 1
            # Move to the next bit.
            current_bit += 1

        # Remove bits from result if it has more set bits than the target.
        while set_bits_count > target_set_bits_count:
            # If the current bit in result is set (1), unset it (make it 0).
            if self._is_set(result, current_bit):
                result = self._unset_bit(result, current_bit)
                set_bits_count -= 1
            # Move to the next bit.
            current_bit += 1

        return result

    # Helper function to check if the given bit position in result is set (1).
    def _is_set(self, x: int, bit: int) -> bool:
        return (x & (1 << bit)) != 0

    # Helper function to set the given bit position in result to 1.
    def _set_bit(self, x: int, bit: int):
        return x | (1 << bit)

    # Helper function to unset the given bit position in x (set it to 0).
    def _unset_bit(self, x: int, bit: int):
        return x & ~(1 << bit)


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        result = 0

        target_set_bits_count = bin(num2).count("1")
        set_bits_count = 0
        current_bit = 31  # Start from the most significant bit.

        # While result has fewer set bits than num2
        while set_bits_count < target_set_bits_count:
            # If the current bit of num1 is set or we must set all remaining bits in result
            if self._is_set(num1, current_bit) or (
                target_set_bits_count - set_bits_count > current_bit
            ):
                result = self._set_bit(result, current_bit)
                set_bits_count += 1
            current_bit -= 1  # Move to the next bit.

        return result

    # Helper function to check if the given bit position in x is set (1).
    def _is_set(self, x: int, bit: int) -> bool:
        return (x & (1 << bit)) != 0

    # Helper function to set the given bit position in x to 1.
    def _set_bit(self, x: int, bit: int):
        return x | (1 << bit)


sol = Solution()

print(sol.minimizeXor(3, 5))  # 3
print(sol.minimizeXor(1, 12))  # 3
print(sol.minimizeXor(1, 1))  # 1
# 65 84

print(sol.minimizeXor(65, 84))
