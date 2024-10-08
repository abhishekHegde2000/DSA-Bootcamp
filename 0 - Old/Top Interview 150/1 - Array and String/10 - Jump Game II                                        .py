'''
https://leetcode.com/problems/jump-game-ii/

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2

'''

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # Initialize the number of jumps to 0
        num_jumps = 0
        # Initialize the left and right pointers to 0
        left, right = 0, 0

        # Get the length of the list
        n = len(nums)

        # While the right pointer is less than the last index
        while right < n - 1:
            print(f"Current right pointer: {right}")

            # Initialize the farthest reachable index to 0
            farthest = 0
            # For each index from the left pointer to the right pointer
            for i in range(left, right + 1):
                # Update the farthest reachable index
                farthest = max(farthest, i + nums[i])
                print(f"Farthest reachable index: {farthest}")

            # Move the left pointer to the right of the current right pointer
            left = right + 1
            print(f"Updated left pointer: {left}")

            # Move the right pointer to the farthest reachable index
            right = farthest
            print(f"Updated right pointer: {right}")

            # Increment the number of jumps
            num_jumps += 1
            print(f"Number of jumps: {num_jumps}")

        # Return the number of jumps
        return num_jumps


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        # Create a memoization table to store minimum jumps for each index
        memo = [-1] * n

        # Define a helper function to calculate the minimum jumps from an index
        def min_jumps_helper(index):
            # Base case: Reached the last element, no jumps needed
            if index == n - 1:
                return 0

            # Check if the minimum jumps for this index are already calculated
            if memo[index] != -1:
                return memo[index]

            # Initialize the minimum jumps to a large value
            min_jumps = float('inf')

            # Iterate through elements reachable from the current index
            for i in range(1, nums[index] + 1):
                # Check if the next index is within the array bounds
                if index + i < n:
                    # Calculate minimum jumps for the next index and add 1 for the current jump
                    next_jumps = min_jumps_helper(index + i) + 1
                    # Update the minimum jumps if the total is less
                    min_jumps = min(min_jumps, next_jumps)

            # Store the minimum jumps for the current index in the memo table
            memo[index] = min_jumps

            # Return the minimum jumps for the current index
            return min_jumps

        # Start calculation from the beginning
        jumps = min_jumps_helper(0)

        # Return the calculated minimum jumps
        return jumps


# example usage
sol = Solution()
nums = [2, 3, 1, 1, 4]
print(sol.jump(nums))
nums = [2, 3, 0, 1, 4]
print(sol.jump(nums))
