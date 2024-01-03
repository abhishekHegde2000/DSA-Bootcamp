'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 
 '''

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize an empty hashmap
        num_to_index = {}

        # Iterate over the list of numbers
        for i, num in enumerate(nums):
            print(f"Checking number: {num}")

            # Calculate the complement
            complement = target - num
            print(f"Complement: {complement}")

            # If the complement is in the hashmap
            if complement in num_to_index:
                print(f"Found the two numbers: {num} and {complement}")
                return [num_to_index[complement], i]

            # If the complement is not in the hashmap, add the number and its index to the hashmap
            num_to_index[num] = i
            print(f"Added {num} to the hashmap")

        # If no two numbers add up to the target, return an empty list
        return []


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
print(sol.twoSum([3, 2, 4], 6))
print(sol.twoSum([3, 3], 6))
