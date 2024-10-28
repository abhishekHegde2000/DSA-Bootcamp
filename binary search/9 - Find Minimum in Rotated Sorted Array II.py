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

        c_min = nums[0]

        while start <= end:

            if nums[start] <= nums[end]:
                # Array is not rotated
                return nums[start]

            mid = (start + end) // 2

            c_min = min(c_min, nums[mid])

            if nums[mid] > nums[end]:

                start = mid + 1
            elif nums[mid] < nums[end]:
                end = mid
            else:
                end -= 1


sol = Solution()

print(sol.findMin([1, 3, 5]))  # 1
print(sol.findMin([2, 2, 2, 0, 1]))  # 0
print(sol.findMin([1, 1, 1, 1, 1, 1]))  # 1
