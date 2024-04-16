'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

154. Find Minimum in Rotated Sorted Array II

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.

 

Example 1:

Input: nums = [1,3,5]
Output: 1
Example 2:

Input: nums = [2,2,2,0,1]
Output: 0
 

'''

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize pointers to the start and end of the array
        start = 0
        end = len(nums) - 1

        while start < end:
            print(f"Start: {start}, End: {end}")
            # Calculate the middle index
            middle = (start + end) // 2
            print(f"Middle: {middle}, Middle Element: {nums[middle]}")

            # Determine the appropriate search direction
            if nums[middle] > nums[end]:
                print("Searching right side of array.")
                start = middle + 1
            elif nums[middle] < nums[end]:
                print("Searching left side of array.")
                end = middle
            else:
                print("Uncertain which side to search, reducing search space by 1.")
                end -= 1

        # Return the found minimum value
        print("Found minimum.")
        return nums[start]


sol = Solution()
print(sol.findMin([1, 3, 5]))
print(sol.findMin([2, 2, 2, 0, 1]))
