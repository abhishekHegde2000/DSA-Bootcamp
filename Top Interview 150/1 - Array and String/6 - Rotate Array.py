'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

'''


class Solution(object):
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Calculate the effective number of steps
        k = k % len(nums)

        # Split the array into two parts: left and right
        left = nums[-k:]
        right = nums[:-k]

        # Concatenate the left and right parts
        full = left + right

        # Update the original array with the rotated elements
        nums[:] = full


sol = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(sol.rotate(nums))
print(nums)
nums = [-1, -100, 3, 99]
k = 2
print(sol.rotate(nums))
print(nums)
