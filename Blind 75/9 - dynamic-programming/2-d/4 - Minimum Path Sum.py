'''
https://leetcode.com/problems/minimum-path-sum/description/?envType=study-plan-v2&envId=top-100-liked

64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200


'''


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        colLen = len(grid[0])
        rowLen = len(grid)

        dp = [[-1 for col in range(colLen)] for row in range(rowLen)]
        print(f"dp = {dp}")

        def helper(i, j):

            if i == 0 and j == 0:
                return dp[0][0]

            if i < 0 or j < 0:
                return float("inf")

            if dp[i][j] != -1:
                return dp[i][j]

            up = helper(i-1, j)
            left = helper(i, j-1)

            dp[i][j] = dp[i][j] + min(up, left)

        return grid[0][0]

# space optimization
    
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        