'''
https://leetcode.com/problems/path-with-maximum-gold/

1219. Path with Maximum Gold

In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
'''

from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        max_gold = 0
        path = []
        pathSum = 0

        def dfs(r, c, path, pathSum):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0 or (r, c) in visited:
                return

            visited.add((r, c))
            path.append(grid[r][c])
            pathSum += grid[r][c]

            nonlocal max_gold
            max_gold = max(max_gold, pathSum)

            dfs(r + 1, c, path, pathSum)
            dfs(r - 1, c, path, pathSum)
            dfs(r, c + 1, path, pathSum)
            dfs(r, c - 1, path, pathSum)

            path.pop()
            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0:
                    dfs(r, c, path, pathSum)

        return max_gold
