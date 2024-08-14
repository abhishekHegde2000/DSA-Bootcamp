'''
https://leetcode.com/problems/climbing-stairs/description/

70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

'''


class Solution:
    def climbStairs(self, total_stairs: int) -> int:
        # Initialize previous_step and two_steps_back to 1
        previous_step, two_steps_back = 1, 1
        print(
            f"Initial values - Previous step: {previous_step}, Two steps back: {two_steps_back}")

        # For each number of stairs from 2 to total_stairs
        for _ in range(total_stairs - 1):
            # Calculate the number of ways to climb the current number of stairs
            print(f"Calculating the number of ways to climb the current number of stairs")
            temp = previous_step
            previous_step = previous_step + two_steps_back
            two_steps_back = temp
            print(
                f"Updated values - Previous step: {previous_step}, Two steps back: {two_steps_back}")

        # Return the number of ways to climb total_stairs
        print(f"Returning the number of ways to climb {
              total_stairs} stairs: {previous_step}")
        return previous_step


class Solution:
    def climbStairs(self, total_stairs: int) -> int:
        # If total_stairs is less than 3, return total_stairs
        print(f"Total stairs is {
              total_stairs}, which is less than 3, returning {total_stairs}")
        if total_stairs < 3:
            return total_stairs

        # Initialize a list to store the number of ways to climb each number of stairs
        print(f"Initializing a list to store the number of ways to climb each number of stairs")
        ways_to_climb = [None for _ in range(total_stairs+1)]
        ways_to_climb[0] = 0
        ways_to_climb[1] = 1
        ways_to_climb[2] = 2
        # For each number of stairs from 3 to total_stairs, calculate the number of ways to climb that number of stairs
        for stairs in range(3, total_stairs+1):
            print(f"Calculating the number of ways to climb {stairs} stairs")
            ways_to_climb[stairs] = ways_to_climb[stairs-1] + \
                ways_to_climb[stairs-2]
            print(f"The number of ways to climb {
                  stairs} stairs is {ways_to_climb[stairs]}")

        # Return the number of ways to climb total_stairs
        print(f"Returning the number of ways to climb {
              total_stairs} stairs: {ways_to_climb[total_stairs]}")
        return ways_to_climb[total_stairs]


class Solution:
    def climbStairs(self, total_stairs: int) -> int:
        # Initialize a dynamic programming list with -1 for each stair
        print(f"Initializing a dynamic programming list with -1 for each stair")
        dp = [-1 for stair in range(total_stairs+1)]

        # Set the number of ways to climb 0 stairs and 1 stair to 1
        print(f"Setting the number of ways to climb 0 stairs and 1 stair to 1")
        dp[0] = 1
        dp[1] = 1

        # For each number of stairs from 2 to total_stairs, calculate the number of ways to climb that number of stairs
        for stair in range(2, total_stairs+1):
            print(f"Calculating the number of ways to climb {stair} stairs")
            dp[stair] = dp[stair-1] + dp[stair-2]
            print(f"The number of ways to climb {stair} stairs is {dp[stair]}")

        # Return the number of ways to climb total_stairs
        print(f"Returning the number of ways to climb {
              total_stairs} stairs: {dp[total_stairs]}")
        return dp[total_stairs]


sol = Solution()

print(sol.climbStairs(2))  # 2
print(sol.climbStairs(3))  # 3
print(sol.climbStairs(4))  # 5
