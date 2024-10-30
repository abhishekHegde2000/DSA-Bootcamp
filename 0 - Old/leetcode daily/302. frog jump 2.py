'''
https://www.naukri.com/code360/problems/minimal-cost_8180930?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf


'''

from typing import *


def minimizeCost_dfs_memo(n: int, k: int, heights: List[int]) -> int:

    n = len(heights)

    dp = {}

    def dfs(curr):

        if curr >= n - 1:
            return 0

        if curr in dp:
            return dp[curr]

        jump_one = dfs(curr + 1) + abs(heights[curr] - heights[curr + 1])

        jump_two = float('inf')

        if curr + 2 < n:
            jump_two = dfs(curr + 2) + abs(heights[curr] - heights[curr + 2])

        dp[curr] = min(jump_one, jump_two)

        return dp[curr]

    return dfs(0)


def minimizeCost_dp(n: int, k: int, heights: List[int]) -> int:

    n = len(heights)

    dp = [float('inf')] * n

    dp[0] = 0

    for i in range(1, n):

        for j in range(1, k + 1):

            if i - j >= 0:
                dp[i] = min(dp[i], dp[i - j] +
                            abs(heights[i] - heights[i - j]))

    return dp[-1]


# Example usage:
print(minimizeCost_dfs_memo(5, 3, [10, 30, 20, 50, 40]))  # 30
print(minimizeCost_dp(5, 2, [10, 30, 20, 50, 40]))  # 20
