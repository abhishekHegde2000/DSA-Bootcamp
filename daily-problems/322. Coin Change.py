'''
https://leetcode.com/problems/coin-change/

322. Coin Change
Solved
Medium
Topics
Companies
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


from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n + 1)]

        def dfs(ind, target):
            if target == 0:
                return 0

            if target < 0:
                return float('inf')

            if ind == n:
                return float('inf')

            if dp[ind][target] != -1:
                return dp[ind][target]

            if coins[ind] <= target:
                take = 1 + dfs(ind, target - coins[ind])
                leave = dfs(ind + 1, target)
                dp[ind][target] = min(take, leave)
            else:
                dp[ind][target] = dfs(ind + 1, target)

            return dp[ind][target]

        res = dfs(0, amount)
        return res if res != float('inf') else -1


sol = Solution()

print(sol.coinChange([7, 5, 3], 10))  # 3

print(sol.coinChange([1, 2, 5], 11))  # 3
print(sol.coinChange([2], 3))  # -1
print(sol.coinChange([1], 0))  # 0
