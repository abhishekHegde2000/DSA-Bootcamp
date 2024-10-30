'''
https://www.naukri.com/code360/problems/frog-jump_3621012?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

https://takeuforward.org/data-structure/dynamic-programming-frog-jump-dp-3/
'''


from typing import List


class Solution:
    def frog_jump(self, heights: List[int]) -> int:

        n = len(heights)
        dp = [0] * n

        for i in range(1, n):

            jump_two = float('inf')
            jump_one = dp[i - 1] + abs(heights[i] - heights[i - 1])

            if i > 1:
                jump_two = dp[i - 2] + abs(heights[i] - heights[i - 2])

            dp[i] = min(jump_one, jump_two)

        return dp[-1]

    def frog_jump_dfs(self, heights: List[int]) -> int:
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
                jump_two = dfs(curr + 2) + \
                    abs(heights[curr] - heights[curr + 2])

            dp[curr] = min(jump_one, jump_two)

            return dp[curr]

        return dfs(0)


# Example usage:
heights = [10, 30, 20, 50, 40]
solution = Solution()
# Output: 30 (minimum cost to jump from first to last stone)
print(solution.frog_jump_dfs(heights))

print(solution.frog_jump(heights))
