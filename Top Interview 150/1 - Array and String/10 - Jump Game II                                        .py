'''

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


# example usage
sol = Solution()
nums = [2, 3, 1, 1, 4]
print(sol.jump(nums))
nums = [2, 3, 0, 1, 4]
print(sol.jump(nums))
