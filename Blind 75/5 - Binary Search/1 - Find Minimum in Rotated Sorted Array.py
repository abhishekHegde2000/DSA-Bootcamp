'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

153. Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 
 '''
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize pointers to the start and end of the array
        start = 0
        end = len(nums) - 1
        # Assume the first element is the minimum
        current_minimum = nums[0]

        while start <= end:
            print(f"Start: {start}, End: {
                  end}, Current Minimum: {current_minimum}")
            # If the start element is less than the end element, the array is not rotated
            if nums[start] < nums[end]:
                print("Array is not rotated.")
                return nums[start]

            # Calculate the middle index
            middle = (start + end) // 2
            print(f"Middle: {middle}, Middle Element: {nums[middle]}")

            # Update the current minimum if necessary
            current_minimum = min(current_minimum, nums[middle])
            print(f"Updated Current Minimum: {current_minimum}")

            # Determine the appropriate search direction
            if nums[middle] >= nums[start]:
                print("Moving start pointer to the right.")
                start = middle + 1
            else:
                print("Moving end pointer to the left.")
                end = middle

        # Return the found minimum value
        print("Found minimum.")
        return current_minimum


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize the start and end pointers
        start_pointer, end_pointer = 0, len(nums) - 1

        while start_pointer < end_pointer:
            # Calculate the middle index
            middle_index = start_pointer + (end_pointer - start_pointer) // 2
            print(f"start_pointer = {start_pointer}, end_pointer = {
                  end_pointer}, middle_index = {middle_index}")

            # If the middle element is less than the end element, move the end pointer to the middle index
            if nums[middle_index] < nums[end_pointer]:
                print(f"nums[middle_index] < nums[end_pointer] : {
                      nums[middle_index]} < {nums[end_pointer]}")
                end_pointer = middle_index
                print(f"end_pointer changed to middle_index >> {end_pointer}")
            # Otherwise, move the start pointer to the middle index + 1
            else:
                start_pointer = middle_index + 1
                print(
                    f"start_pointer changed to middle_index + 1 >> {start_pointer}")

        # The minimum element is at the start pointer
        return nums[start_pointer]


sol = Solution()

nums = [3, 4, 5, 1, 2]
print(sol.findMin(nums))

nums = [4, 5, 6, 7, 0, 1, 2]
print(sol.findMin(nums))

nums = [11, 13, 15, 17]
print(sol.findMin(nums))
