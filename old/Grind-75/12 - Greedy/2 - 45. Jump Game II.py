'''
https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-100-liked

45. Jump Game II

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
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].

'''
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        def minJumpsFromPosition(pos: int, nums: List[int]) -> int:
            print(f"Current position: {pos}")

            # If we are at the last index, no jumps are needed
            if pos == len(nums) - 1:
                return 0

            # Determine the maximum jump length at the current position
            maxJumpLength = min(pos + nums[pos], len(nums) - 1)
            print(f"Max jump length from position {pos}: {maxJumpLength}")

            # Initialize minJumps to infinity
            minJumps = float('inf')

            # Check each jump pattern from the current position
            for i in range(pos + 1, maxJumpLength + 1):
                print(f"Jumping to position {i}")
                minJumps = min(minJumps, 1 + minJumpsFromPosition(i, nums))

            return minJumps

        return minJumpsFromPosition(0, nums)


class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = [None] * len(nums)

        def minJumpsFromPosition(pos: int, nums: List[int]) -> int:
            print(f"Current position: {pos}")

            # If we have a memoized result for this position, return it
            if memo[pos] is not None:
                return memo[pos]

            # If we are at the last index, no jumps are needed
            if pos == len(nums) - 1:
                return 0

            # Determine the maximum jump length at the current position
            maxJumpLength = min(pos + nums[pos], len(nums) - 1)
            print(f"Max jump length from position {pos}: {maxJumpLength}")

            # Initialize minJumps to infinity
            minJumps = float('inf')

            # Check each jump pattern from the current position
            for i in range(pos + 1, maxJumpLength + 1):
                print(f"Jumping to position {i}")
                minJumps = min(minJumps, 1 + minJumpsFromPosition(i, nums))

            # Store the result in the memo table
            memo[pos] = minJumps

            return minJumps

        return minJumpsFromPosition(0, nums)


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        currentJumpEnd = 0
        furthestJump = 0

        for i in range(len(nums) - 1):
            print(f"Current position: {i}")
            furthestJump = max(furthestJump, i + nums[i])
            print(f"Furthest jump: {furthestJump}")

            if i == currentJumpEnd:
                jumps += 1
                currentJumpEnd = furthestJump
                print(f"Updated jumps: {
                      jumps}, currentJumpEnd: {currentJumpEnd}")

        return jumps


sol = Solution()

print(sol.jump([2, 3, 1, 1, 4]))  # 2
print(sol.jump([2, 3, 0, 1, 4]))  # 2
print(sol.jump([1, 1, 1, 1]))  # 3
print(sol.jump([1, 2, 1, 1, 1]))  # 3
