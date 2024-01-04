'''


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


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Finds the minimum value in a potentially rotated sorted array.

        Args:
            nums: The input array.

        Returns:
            The minimum value in the array.
        """

        # Initialize variables with meaningful names
        current_minimum = nums[0]
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:
            # Check for the case where the array is not rotated
            if nums[left_pointer] < nums[right_pointer]:
                return nums[left_pointer]

            # Calculate the middle index
            middle_index = (left_pointer + right_pointer) // 2

            # Update the current minimum if necessary
            current_minimum = min(current_minimum, nums[middle_index])

            # Determine the appropriate search direction
            if nums[middle_index] >= nums[left_pointer]:
                left_pointer = middle_index + 1
            else:
                right_pointer = middle_index

        # Return the found minimum value
        return current_minimum
