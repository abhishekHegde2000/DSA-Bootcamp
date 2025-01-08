'''
https://leetcode.com/problems/split-array-largest-sum/

410. Split Array Largest Sum
Hard
Topics
Companies
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.



Example 1:

Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.


Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 106
1 <= k <= min(50, nums.length)

'''

from typing import List


class Solution:
    def split_array(self, nums: List[int], k: int) -> int:
        """
        Splits the array into k subarrays such that the largest sum among the subarrays is minimized.

        Args:
            nums: List of integers representing the array.
            k: Integer representing the number of subarrays.

        Returns:
            The minimized largest sum among the k subarrays.
        """
        n = len(nums)
        memo = {}

        def dfs(index: int, k: int) -> int:
            """
            Helper function to perform depth-first search with memoization.

            Args:
                index: Current index in the array.
                k: Remaining number of subarrays to split.

            Returns:
                The minimized largest sum for the current state.
            """
            # Check if the result is already computed
            if (index, k) in memo:
                return memo[(index, k)]

            # If only one subarray is left, return the sum of the remaining elements
            if k == 1:
                return sum(nums[index:])

            # If we have reached the end of the array
            if index == n:
                return 0

            result, current_sum = float('inf'), 0

            # Try to split the array at different positions
            for i in range(index, n - k + 1):
                current_sum += nums[i]
                max_sum = max(current_sum, dfs(i + 1, k - 1))
                result = min(result, max_sum)
                # Early stopping if the current sum exceeds the result
                if current_sum > result:
                    break

            # Memoize the result
            memo[(index, k)] = result
            return result

        return dfs(0, k)


# Example usage
sol = Solution()
print(sol.split_array([7, 2, 5, 10, 8], 2))  # Output: 18
print(sol.split_array([1, 2, 3, 4, 5], 2))   # Output: 9


class Solution:
    def split_array(self, nums: List[int], k: int) -> int:
        """
        Splits the array into k subarrays such that the largest sum among the subarrays is minimized.

        Args:
            nums: List of integers representing the array.
            k: Integer representing the number of subarrays.

        Returns:
            The minimized largest sum among the k subarrays.
        """
        n = len(nums)
        # Create a prefix sum array
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]

        # Initialize the DP table
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for m in range(i):
                    dp[i][j] = min(dp[i][j], max(
                        dp[m][j - 1], prefix_sums[i] - prefix_sums[m]))

        return dp[n][k]


# Example usage
sol = Solution()
print(sol.split_array([7, 2, 5, 10, 8], 2))  # Output: 18
print(sol.split_array([1, 2, 3, 4, 5], 2))   # Output: 9


class Solution:
    def split_array(self, nums: List[int], k: int) -> int:
        """
        Splits the array into k subarrays such that the largest sum among the subarrays is minimized.

        Args:
            nums: List of integers representing the array.
            k: Integer representing the number of subarrays.

        Returns:
            The minimized largest sum among the k subarrays.
        """
        def can_split(nums: List[int], k: int, max_sum: int) -> bool:
            """
            Helper function to check if the array can be split into k or fewer subarrays
            with each subarray sum less than or equal to max_sum.

            Args:
                nums: List of integers representing the array.
                k: Integer representing the number of subarrays.
                max_sum: The maximum allowed sum for each subarray.

            Returns:
                True if the array can be split into k or fewer subarrays, False otherwise.
            """
            current_sum = 0
            subarrays = 1
            for num in nums:
                if current_sum + num > max_sum:
                    subarrays += 1
                    current_sum = num
                    if subarrays > k:
                        return False
                else:
                    current_sum += num
            return True

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if can_split(nums, k, mid):
                right = mid
            else:
                left = mid + 1

        return left


# Example usage
sol = Solution()
print(sol.split_array([7, 2, 5, 10, 8], 2))  # Output: 18
print(sol.split_array([1, 2, 3, 4, 5], 2))   # Output: 9
