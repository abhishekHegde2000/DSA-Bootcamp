'''
https://leetcode.com/problems/single-element-in-a-sorted-array/

540. Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 
'''


from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Initialize pointers to the start and end of the array
        lower_bound = 0
        upper_bound = len(nums) - 1

        while lower_bound < upper_bound:
            # Calculate the middle index
            middle_index = lower_bound + (upper_bound - lower_bound) // 2
            print(f"Checking index {middle_index}")

            # If the middle index is even and the next number is the same, or the middle index is odd and the previous number is the same, the single non-duplicate number is in the right half
            if (middle_index % 2 == 0 and nums[middle_index] == nums[middle_index + 1]) or (middle_index % 2 == 1 and nums[middle_index] == nums[middle_index - 1]):
                print(f"The single non-duplicate number is in the right half")
                lower_bound = middle_index + 1
            else:
                print(f"The single non-duplicate number is in the left half")
                upper_bound = middle_index

        # The single non-duplicate number is at the left pointer
        print(f"The single non-duplicate number is {nums[lower_bound]}")
        return nums[lower_bound]
