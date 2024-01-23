'''
https://leetcode.com/problems/house-robber-ii/description/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000

'''

from typing import List


class Solution:
    def rob(self, houses: List[int]) -> int:

        def calculate_max_robbery(houses):
            previous_robbery, current_robbery = 0, 0

            # Iterate over each house in the list
            for current_house_money in houses:
                print(f"Current house money: {current_house_money}")

                # Calculate the maximum amount of money that can be robbed if this house is robbed
                new_robbery = max(previous_robbery +
                                  current_house_money, current_robbery)
                print(f"New robbery: {new_robbery}")

                # Update previous_robbery and current_robbery
                previous_robbery = current_robbery
                print(f"Previous robbery: {previous_robbery}")
                current_robbery = new_robbery
                print(f"Current robbery: {current_robbery}")

            # Return the maximum amount of money that can be robbed from all houses
            return current_robbery

        # Call calculate_max_robbery twice and return the maximum of these two values and the money in the first house
        return max(houses[0], calculate_max_robbery(houses[1:]), calculate_max_robbery(houses[:-1]))


class Solution:
    def rob(self, houses: List[int]) -> int:
        def dfs(current_index, total_robbed):
            # If the current index is out of bounds, return the total amount of money robbed so far
            if current_index >= len(houses):
                return total_robbed

            # Calculate the maximum amount of money that can be robbed by either skipping the current house or robbing the current house
            skip_current_house = dfs(current_index + 1, total_robbed)
            rob_current_house = dfs(
                current_index + 2, total_robbed + houses[current_index])

            return max(skip_current_house, rob_current_house)

        # Call dfs with the initial index and the initial total amount of money robbed
        return dfs(0, 0)


class Solution:
    def rob(self, houses: List[int]) -> int:
        memo = [-1] * len(houses)

        def dfs(current_index):
            # If the current index is out of bounds, return 0
            if current_index >= len(houses):
                return 0

            # If the maximum amount of money that can be robbed up to the current house is already calculated, return it
            if memo[current_index] != -1:
                return memo[current_index]

            # Calculate the maximum amount of money that can be robbed up to the current house
            skip_current_house = dfs(current_index + 1)
            rob_current_house = houses[current_index] + dfs(current_index + 2)

            memo[current_index] = max(skip_current_house, rob_current_house)
            return memo[current_index]

        # Call dfs with the initial index
        return dfs(0)


sol = Solution()

print(sol.rob([2, 3, 2]))  # 3
print(sol.rob([1, 2, 3, 1]))  # 4
print(sol.rob([1, 2, 3]))  # 3
print(sol.rob([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 27
