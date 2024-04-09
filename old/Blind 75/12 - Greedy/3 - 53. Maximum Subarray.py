'''
https://leetcode.com/problems/maximum-subarray/description/

53. Maximum Subarray

Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

'''
from typing import List


class Solution:
    def maxSubArray(self, input_numbers: List[int]) -> int:
        # Initialize maximum_sum as the first element of input_numbers
        maximum_sum = input_numbers[0]
        print(f"Initial maximum_sum: {maximum_sum}")

        # Initialize current_sum as 0
        current_sum = 0
        print(f"Initial current_sum: {current_sum}")

        for number in input_numbers:
            # Reset current_sum to 0 if it becomes negative
            if current_sum < 0:
                current_sum = 0
                print(f"Reset current_sum to 0 as it became negative")

            # Add number to current_sum
            current_sum += number
            print(f"Added {number} to current_sum. New current_sum: {
                  current_sum}")

            # Update maximum_sum
            maximum_sum = max(current_sum, maximum_sum)
            print(f"Updated maximum_sum: {maximum_sum}")

        # Return the maximum subarray sum
        return maximum_sum


class Solution:
    def maxSubArray(self, input_numbers: List[int]) -> int:
        # Initialize maximum_sum to negative infinity
        maximum_sum = float('-inf')
        print(f"Initial maximum_sum: {maximum_sum}")

        for start_index in range(len(input_numbers)):
            # Initialize current_sum as 0
            current_sum = 0
            print(f"Start_index: {
                  start_index}, Initial current_sum: {current_sum}")

            for end_index in range(start_index, len(input_numbers)):
                # Add number at end_index to current_sum
                current_sum += input_numbers[end_index]
                print(f"Added {input_numbers[end_index]} to current_sum. New current_sum: {
                      current_sum}")

                # Update maximum_sum
                maximum_sum = max(current_sum, maximum_sum)
                print(f"Updated maximum_sum: {maximum_sum}")

        # Return the maximum subarray sum
        return maximum_sum


sol = Solution()

print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(sol.maxSubArray([1]))  # 1
print(sol.maxSubArray([5, 4, -1, 7, 8]))  # 23
print(sol.maxSubArray([-1]))  # -1
print(sol.maxSubArray([-2, 1]))  # 1
