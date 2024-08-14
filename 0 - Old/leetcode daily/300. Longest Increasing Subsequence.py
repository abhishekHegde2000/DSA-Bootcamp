'''
https://leetcode.com/problems/longest-increasing-subsequence/

300. Longest Increasing Subsequence

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
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
'''


from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        self.memo = {}
        return self.solve(0, float('-inf'), length, nums)

    def solve(self, idx, prev, length, nums):
        if idx >= length:
            return 0

        if (idx, prev) in self.memo:
            return self.memo[(idx, prev)]

        taken = 0
        if nums[idx] > prev:
            taken = 1 + (self.solve(idx+1, nums[idx], length, nums))

        not_taken = self.solve(idx+1, prev, length, nums)

        self.memo[(idx, prev)] = max(taken, not_taken)
        return self.memo[(idx, prev)]


sol = Solution()

print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
print(sol.lengthOfLIS([0, 1, 0, 3, 2, 3]))  # 4
print(sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))  # 1
