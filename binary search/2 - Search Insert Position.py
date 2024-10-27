'''
https://leetcode.com/problems/search-insert-position/

35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
'''

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_pointer = 0  # Initialize left pointer to the start of the array
        # Initialize right pointer to the end of the array
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:
            # Calculate the middle index
            middle_index = (left_pointer + right_pointer) // 2

            # Debugging print statement:
            print(f"Current range: {
                  nums[left_pointer:right_pointer + 1]} | middle_index: {middle_index}")

            if nums[middle_index] == target:
                return middle_index  # Target found, return its index
            elif nums[middle_index] > target:
                right_pointer = middle_index - 1  # Search in the left subarray
            else:
                left_pointer = middle_index + 1  # Search in the right subarray

            # if nums[middle_index] < target:
            #     left_pointer = middle_index + 1
            # else:
            #     right_pointer = middle_index - 1

        # Target not found, return the insertion point (left_pointer)
        return left_pointer


sol = Solution()

print(sol.searchInsert([1, 3, 5, 6], 5))  # 2
print(sol.searchInsert([1, 3, 5, 6], 2))  # 1
print(sol.searchInsert([1, 3, 5, 6], 7))  # 4
print(sol.searchInsert([1, 3, 5, 6], 0))  # 0
