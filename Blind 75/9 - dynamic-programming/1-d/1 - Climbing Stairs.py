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
    def climbStairs(self, total_steps: int) -> int:
        # Initialize memoization list
        memo = [0] * (total_steps + 1)

        def calculate_ways(current_step):
            print(f"Current step: {current_step}")

            # If the current step is beyond total steps, return 0
            if current_step > total_steps:
                print(
                    f"Step {current_step} is beyond total steps. Returning 0.")
                return 0

            # If the current step is the final step, return 1
            if current_step == total_steps:
                print(f"Step {current_step} is the final step. Returning 1.")
                return 1

            # If the number of ways to reach the current step is already calculated, return it
            if memo[current_step] > 0:
                print(f"Number of ways to reach step {
                      current_step} is already calculated. Returning {memo[current_step]}.")
                return memo[current_step]

            # Calculate the number of ways to reach the current step
            memo[current_step] = calculate_ways(
                current_step + 1) + calculate_ways(
                    current_step + 2)
            print(f"Total ways to reach step {
                  current_step}: {memo[current_step]}")
            return memo[current_step]

        # Call calculate_ways with the initial step
        return calculate_ways(0)


sol = Solution()

print(sol.climbStairs(2))  # 2
print(sol.climbStairs(3))  # 3
print(sol.climbStairs(4))  # 5
