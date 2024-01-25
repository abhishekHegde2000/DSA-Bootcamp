'''
https://leetcode.com/problems/house-robber/description/

198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400

'''

from typing import List

# Memoization Solution


class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [-1 for house in range(len(nums))]

        def dfs(index):

            if dp[index] != -1:
                return dp[index]

            if index < 0:
                return 0

            if index == 0:
                return nums[0]

            pick = nums[index] + dfs(index - 2)
            skip = dfs(index - 1)

            dp[index] = max(pick, skip)

            return dp[index]

        return dfs(len(nums) - 1)

# Tabulation Solution


class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [-1 for house in range(len(nums))]

        dp[0] = nums[0]

        for index in range(1, len(nums)):

            pick = nums[index] if index < 2 else nums[index] + dp[index - 2]

            skip = 0 + dp[index - 1]

            dp[index] = max(pick, skip)

        return dp[len(nums) - 1]

# SPACE OPTIMIZED TABULATION SOLUTION


class Solution:
    def rob(self, nums: List[int]) -> int:

        prev = nums[0]
        prev2 = 0

        for i in range(1, len(nums)):

            pick = nums[i] if i < 2 else nums[i] + prev2

            skip = 0 + prev

            curr = max(pick, skip)

            prev2 = prev
            prev = curr

        return prev


sol = Solution()

print(sol.rob([1, 2, 3, 1]))  # 4
print(sol.rob([2, 7, 9, 3, 1]))  # 12
print(sol.rob([2, 1, 1, 2]))  # 4
