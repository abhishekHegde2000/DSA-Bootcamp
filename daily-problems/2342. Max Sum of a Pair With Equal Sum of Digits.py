'''
https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/


2342. Max Sum of a Pair With Equal Sum of Digits

2342. Max Sum of a Pair With Equal Sum of Digits
Attempted
Medium
Topics
Companies
Hint
You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.



Example 1:

Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.
Example 2:

Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.

'''


class Solution:
    # Helper function to compute the sum of digits of a number
    def calculate_digit_sum(self, num):
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum

    def maximumSum(self, nums):
        digit_sum_pairs = []

        # Store numbers with their digit sums as pairs
        for number in nums:
            digit_sum = self.calculate_digit_sum(number)
            digit_sum_pairs.append((digit_sum, number))

        # Sort based on digit sums, and if equal, by number value
        digit_sum_pairs.sort()

        max_pair_sum = -1

        # Iterate through the sorted array to find the maximum sum of pairs
        for index in range(1, len(digit_sum_pairs)):
            current_digit_sum = digit_sum_pairs[index][0]
            previous_digit_sum = digit_sum_pairs[index - 1][0]

            # If two consecutive numbers have the same digit sum
            if current_digit_sum == previous_digit_sum:
                current_sum = (
                    digit_sum_pairs[index][1] + digit_sum_pairs[index - 1][1]
                )
                max_pair_sum = max(max_pair_sum, current_sum)

        return max_pair_sum


sol = Solution()

print(sol.maximumSum([18,43,36,13,7])) # 54
print(sol.maximumSum([10,12,19,14])) # -1
print(sol.maximumSum([10,12,19,14, 91])) # 110
