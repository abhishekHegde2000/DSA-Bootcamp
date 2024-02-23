'''
https://leetcode.com/problems/binary-search/

704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1'''


# Approach: Binary search to find target index

# Pseudocode:
# 1. Initialize left and right pointers
# 2. While left <= right:
#   2.1 Calculate mid index as average of left and right pointers
#   2.2 If nums[mid] equals target, return mid index
#   2.3 Else if target > nums[mid], update left pointer to mid+1 (search right)
#   2.4 Else update right pointer to mid-1 (search left)
# 3. Return -1 if target not found

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            print(f"Searching nums[{left}:{right+1}]")

            if nums[mid] == target:
                return mid

            elif target > nums[mid]:
                left = mid + 1

            else:
                right = mid - 1

        return -1
