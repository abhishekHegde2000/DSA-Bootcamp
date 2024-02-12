'''
https://leetcode.com/problems/number-of-islands/

200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''


from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Get the number of rows and columns in the grid
        rowLen, colLen = len(grid), len(grid[0])
        # Set to keep track of visited cells
        visited = set()
        # Counter for the number of islands
        landCount = 0

        # Define BFS function to explore the island from a given cell
        def bfs(row, col):
            # Initialize the deque with the starting cell
            q = deque([(row, col)])
            # Mark the starting cell as visited
            visited.add((row, col))

            # Continue BFS until the deque is empty
            while q:
                r, c = q.popleft()
                # Define directions to explore (up, down, left, right)
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                # Explore neighbors in all four directions
                for dr, dc in directions:
                    R, C = r + dr, c + dc

                    # Check if the neighbor is within bounds, is part of an island, and is not visited
                    if 0 <= R < rowLen and 0 <= C < colLen and grid[R][C] == "1" and (R, C) not in visited:
                        # Add the neighbor to the deque and mark it as visited
                        q.append((R, C))
                        visited.add((R, C))

        # Iterate through each cell in the grid
        for i in range(rowLen):
            for j in range(colLen):
                # If the cell is part of an island and not visited yet
                if (i, j) not in visited and grid[i][j] == "1":
                    # Explore the island using BFS
                    bfs(i, j)
                    # Increment the island count
                    landCount += 1

        # Return the total number of islands
        return landCount


sol = Solution
