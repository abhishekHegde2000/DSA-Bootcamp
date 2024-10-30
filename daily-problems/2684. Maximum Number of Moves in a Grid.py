'''
https://leetcode.com/problems/maximum-number-of-moves-in-a-grid


2684. Maximum Number of Moves in a Grid
Solved
Medium
Topics
Companies
Hint
You are given a 0-indexed m x n matrix grid consisting of positive integers.

You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move to, should be strictly bigger than the value of the current cell.
Return the maximum number of moves that you can perform.



Example 1:


Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
Output: 3
Explanation: We can start at the cell (0, 0) and make the following moves:
- (0, 0) -> (0, 1).
- (0, 1) -> (1, 2).
- (1, 2) -> (2, 3).
It can be shown that it is the maximum number of moves that can be made.
Example 2:


Input: grid = [[3,2,4],[2,1,9],[1,1,7]]
Output: 0
Explanation: Starting from any cell in the first column we cannot perform any moves.


Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
1 <= grid[i][j] <= 106

'''


from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = {}

        def dfs(r, c):
            if r < 0 or r >= m or c >= n:
                return 0

            if (r, c) in dp:
                return dp[(r, c)]

            max_moves = 0
            current_value = grid[r][c]

            top_right = 0
            right = 0
            bottom_right = 0

            if r - 1 >= 0 and c + 1 < n and grid[r - 1][c + 1] > current_value:
                top_right = dfs(r - 1, c + 1)

            if c + 1 < n and grid[r][c + 1] > current_value:
                right = dfs(r, c + 1)

            if r + 1 < m and c + 1 < n and grid[r + 1][c + 1] > current_value:
                bottom_right = dfs(r + 1, c + 1)

            dp[(r, c)] = max_moves
            return max_moves

        max_moves = 0
        # Try starting from each cell in the first column
        for r in range(m):
            max_moves = max(max_moves, dfs(r, 0))

        return max_moves


sol = Solution()

print(sol.maxMoves([[2, 4, 3, 5], [5, 4, 9, 3],
      [3, 4, 2, 11], [10, 9, 13, 15]]))  # 3
print(sol.maxMoves([[3, 2, 4], [2, 1, 9], [1, 1, 7]]))  # 0
print(sol.maxMoves([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # 2
