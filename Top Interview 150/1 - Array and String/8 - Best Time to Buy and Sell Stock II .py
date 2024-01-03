'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

'''

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables
        i = 0
        buy, sell, profit = 0, 0, 0
        N = len(prices) - 1

        # Iterate through the prices array
        while i < N:
            # Find the local minimum (buy point)
            while i < N and prices[i + 1] <= prices[i]:
                i += 1
            buy = prices[i]
            print("Buy:", buy)  # Debug print statement

            # Find the local maximum (sell point)
            while i < N and prices[i + 1] > prices[i]:
                i += 1
            sell = prices[i]
            print("Sell:", sell)  # Debug print statement

            # Calculate and accumulate profit
            profit += sell - buy
            print("Profit:", profit)  # Debug print statement

        # Return the total profit
        return profit


# example usage
sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(sol.maxProfit(prices))
prices = [1, 2, 3, 4, 5]
print(sol.maxProfit(prices))
prices = [7, 6, 4, 3, 1]
print(sol.maxProfit(prices))
