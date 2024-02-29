'''
https://leetcode.com/problems/partition-equal-subset-sum/

416. Partition Equal Subset Sum

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
'''
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        # initialize memoization
        dp = [[-1 for _ in range(target + 1)] for _ in range(len(nums))]

        def subSum(nums, i, target, memo):

            if target == 0:
                return True

            if i == len(nums) or target < 0:
                return False

            if memo[i][target] != -1:
                return memo[i][target]

            take = subSum(nums, i + 1, target - nums[i], memo)
            leave = subSum(nums, i + 1, target, memo)

            memo[i][target] = take or leave

            return memo[i][target]

        return subSum(nums, 0, target, dp)


sol = Solution()
print(sol.canPartition([1, 2, 3]))  # True
print(sol.canPartition([1, 5, 11, 5]))  # True
print(sol.canPartition([1, 2, 3, 5]))  # False
print(sol.canPartition([1, 2, 3, 4, 5, 6, 7]))  # True
print(sol.canPartition([1, 2, 3, 4, 5, 6, 7, 8]))  # False
