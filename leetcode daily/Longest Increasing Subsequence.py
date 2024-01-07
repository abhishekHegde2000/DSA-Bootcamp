'''

300. Longest Increasing Subsequence
Medium
Topics
Companies
Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

'''


from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(prev_index, current_index):
            print(f"current_index: {current_index}, prev_index: {prev_index}")

            if current_index == len(nums):
                return 0

            include_current = 0
            if prev_index < 0 or nums[current_index] > nums[prev_index]:
                print("Including current element")
                include_current = 1 + dfs(current_index, current_index + 1)

            exclude_current = dfs(prev_index, current_index + 1)

            print(f"current_index: {current_index}, prev_index: {prev_index}, include_current: {
                  include_current}, exclude_current: {exclude_current}")
            return max(include_current, exclude_current)

        return dfs(-1, 0)


# Example usage:
solution = Solution()
nums0 = [1, 2, 4, 3]
nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
nums2 = [0, 1, 0, 3, 2, 3]
nums3 = [7, 7, 7, 7, 7, 7, 7]

print(solution.lengthOfLIS(nums0))  # Output: 4
print(solution.lengthOfLIS(nums1))  # Output: 4
print(solution.lengthOfLIS(nums2))  # Output: 4
print(solution.lengthOfLIS(nums3))  # Output: 1
