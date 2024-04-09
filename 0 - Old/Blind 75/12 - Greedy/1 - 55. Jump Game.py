'''
https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-100-liked

55. Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105


'''

from typing import List

# Brute Force


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def canJumpFromPosition(pos: int, nums: List[int]) -> bool:
            print(f"Current position: {pos}")

            # If we are at the last index, we can reach the end
            if pos == len(nums) - 1:
                return True

            # Determine the maximum jump length at the current position
            maxJumpLength = min(pos + nums[pos], len(nums) - 1)
            print(f"Max jump length from position {pos}: {maxJumpLength}")

            # Check each jump pattern from the current position
            for i in range(pos + 1, maxJumpLength + 1):
                print(f"Jumping to position {i}")
                if canJumpFromPosition(i, nums):
                    return True

            return False

        return canJumpFromPosition(0, nums)


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [None] * len(nums)

        def canJumpFromPosition(pos: int, nums: List[int]) -> bool:
            print(f"Current position: {pos}")

            # If we have a memoized result for this position, return it
            if memo[pos] is not None:
                return memo[pos]

            # If we are at the last index, we can reach the end
            if pos == len(nums) - 1:
                return True

            # Determine the maximum jump length at the current position
            maxJumpLength = min(pos + nums[pos], len(nums) - 1)
            print(f"Max jump length from position {pos}: {maxJumpLength}")

            # Check each jump pattern from the current position
            for i in range(pos + 1, maxJumpLength + 1):
                print(f"Jumping to position {i}")
                if canJumpFromPosition(i, nums):
                    memo[pos] = True
                    return True

            memo[pos] = False
            return False

        return canJumpFromPosition(0, nums)


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastPos = len(nums) - 1
        print(f"Initial lastPos: {lastPos}")

        for i in range(len(nums) - 1, -1, -1):
            print(f"Checking position {i}")
            if i + nums[i] >= lastPos:
                print(f"Position {i} can reach lastPos")
                lastPos = i
                print(f"Updated lastPos: {lastPos}")

        return lastPos == 0


sol = Solution()

print(sol.canJump([2, 3, 1, 1, 4]))  # True
print(sol.canJump([3, 2, 1, 0, 4]))  # False
