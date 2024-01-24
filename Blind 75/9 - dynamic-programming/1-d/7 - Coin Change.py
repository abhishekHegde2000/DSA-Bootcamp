'''
https://leetcode.com/problems/coin-change/description/

322. Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104


'''
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount + 1] * ((amount) + 1)

        dp[0] = 0

        for a in range(1, amount + 1):

            for c in coins:

                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        return dp[amount] if dp[amount] != amount + 1 else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()

        def dp(n):
            # return memo if n is in memo
            if n in memo:
                return memo[n]
            # return 0 if n is 0
            if n == 0:
                return 0
            # return -1 if no combination can sum to n
            if n < 0:
                return -1
            res = float('inf')
            for coin in coins:
                subproblem = dp(n - coin)
                if subproblem == -1:
                    continue
                res = min(res, 1 + subproblem)
            # take the result from the loop, store it to memo, and return memo[n]
            memo[n] = res if res != float('inf') else -1
            return memo[n]

        return dp(amount)


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(current_amount, num_coins):
            # If current amount is 0, return num_coins
            if current_amount == 0:
                return num_coins
            # If current amount is less than 0, return -1
            if current_amount < 0:
                return -1
            min_coins = float('inf')
            # For each coin, recursively call dfs with current amount minus coin value and num_coins plus 1
            for coin in coins:
                res = dfs(current_amount - coin, num_coins + 1)
                # If res is not -1, update min_coins
                if res != -1:
                    min_coins = min(min_coins, res)
            return min_coins if min_coins != float('inf') else -1

        return dfs(amount, 0)


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins_dict = dict()

        def dfs(current_amount, num_coins):
            # Check if current amount is in memoization dictionary
            if current_amount in min_coins_dict:
                return min_coins_dict[current_amount]
            # If current amount is 0, return num_coins
            if current_amount == 0:
                return num_coins
            # If current amount is less than 0, return -1
            if current_amount < 0:
                return -1
            min_coins = float('inf')
            # For each coin, recursively call dfs with current amount minus coin value and num_coins plus 1
            for coin in coins:
                res = dfs(current_amount - coin, num_coins + 1)
                # If res is not -1, update min_coins
                if res != -1:
                    min_coins = min(min_coins, res)
            # Store the minimum number of coins needed for current amount in memoization dictionary
            min_coins_dict[current_amount] = min_coins if min_coins != float(
                'inf') else -1
            return min_coins_dict[current_amount]

        return dfs(amount, 0)


sol = Solution()

print(sol.coinChange([1, 2, 5], 11))  # 3
print(sol.coinChange([2], 3))  # -1
print(sol.coinChange([1], 0))  # 0
