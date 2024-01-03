'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

'''

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)

        # Initialize variables to track potential first and second elements
        first = float('inf')  # Initialize first to infinity
        second = float('inf')  # Initialize second to infinity

        for num in nums:
            # If we find a smaller element than first, update first
            if num <= first:
                first = num  # Keep track of the smallest value seen so far
            # If we find an element larger than first but smaller than second, update second
            elif num <= second:
                second = num  # Keep track of the second smallest, but larger than the first
            # If we find an element larger than both first and second, we have a triplet
            else:
                return True  # We've found an increasing triplet

        return False  # No increasing triplet found


sol = Solution()
print(sol.increasingTriplet([1, 2, 3, 4, 5]))
print(sol.increasingTriplet([5, 4, 3, 2, 1]))
print(sol.increasingTriplet([2, 1, 5, 0, 4, 6]))
