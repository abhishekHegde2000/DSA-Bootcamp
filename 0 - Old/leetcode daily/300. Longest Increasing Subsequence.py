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
        n = len(nums)
        dp = [1] * n  # Initialize DP array with 1s

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


sol = Solution()

print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
print(sol.lengthOfLIS([0, 1, 0, 3, 2, 3]))  # 4
print(sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))  # 1
