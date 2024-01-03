'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

'''

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_index = 0  # Index to buy at
        sell_index = 1  # Index to sell at
        max_profit = 0  # Maximum profit initialized to 0

        while sell_index < len(prices):
            # Calculate the current profit
            current_profit = prices[sell_index] - prices[buy_index]
            print(f"Current profit: {current_profit}")

            # If the selling price is higher than the buying price
            if prices[buy_index] < prices[sell_index]:
                # Update the maximum profit if the current profit is higher
                max_profit = max(current_profit, max_profit)
                print(f"New max profit: {max_profit}")
            else:
                # Move the buying index to the current index
                buy_index = sell_index
                print(f"New buy index: {buy_index}")

            # Move to the next selling index
            sell_index += 1

        print(f"Final max profit: {max_profit}")
        return max_profit


# example usage
sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(sol.maxProfit(prices))
prices = [7, 6, 4, 3, 1]
print(sol.maxProfit(prices))
