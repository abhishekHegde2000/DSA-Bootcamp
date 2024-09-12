'''
Move Zeroes

https://leetcode.com/problems/move-zeroes/

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

'''

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        # Get the length of the list
        listLength = len(nums)

        # Initialize the left pointer to 0
        nonZeroIndex = 0

        # Iterate over the list with the right pointer
        for currentIndex in range(listLength):


sol = Solution()
print(sol.moveZeroes([0, 1, 0, 3, 12]))
