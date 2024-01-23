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


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        previous_robbery, current_robbery = 0, 0

        # Iterate over each house in the list
        for current_house_money in nums:
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


class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(index, total_robbed):
            print(f"Current index: {index}, Total robbed: {total_robbed}")

            # If the current index is out of bounds, return the total amount of money robbed so far
            if index >= len(nums):
                print(f"Index {index} is out of bounds. Returning {
                      total_robbed}.")
                return total_robbed

            # Calculate the maximum amount of money that can be robbed by either skipping the current house or robbing the current house
            skip_current_house = dfs(index + 1, total_robbed)
            print(f"Skip current house: {skip_current_house}")
            rob_current_house = dfs(index + 2, total_robbed + nums[index])
            print(f"Rob current house: {rob_current_house}")

            return max(skip_current_house, rob_current_house)

        # Call dfs with the initial index and the initial total amount of money robbed
        return dfs(0, 0)


sol = Solution()

print(sol.rob([1, 2, 3, 1]))  # 4
print(sol.rob([2, 7, 9, 3, 1]))  # 12
print(sol.rob([2, 1, 1, 2]))  # 4
