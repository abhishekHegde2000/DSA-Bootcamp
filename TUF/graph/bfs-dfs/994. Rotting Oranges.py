'''

https://leetcode.com/problems/rotting-oranges/

994. Rotting Oranges
Solved
Medium
Topics
Companies
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
'''

from typing import List


from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Initialize a queue to keep track of rotten oranges
        rotten_queue = deque()
        # Initialize a counter for fresh oranges and time
        fresh_oranges, time_counter = 0, 0

        # Iterate over the grid to count fresh oranges and add rotten oranges to the queue
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    rotten_queue.append((i, j))
        print(f"Initial fresh oranges: {
              fresh_oranges}, rotten queue: {rotten_queue}")

        # Define the directions for adjacent cells
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # While there are rotten oranges in the queue and fresh oranges in the grid
        while rotten_queue and fresh_oranges:
            # For each rotten orange in the queue
            for _ in range(len(rotten_queue)):
                rotten_i, rotten_j = rotten_queue.popleft()
                # For each direction
                for di, dj in directions:
                    # Calculate the row and column of the adjacent cell
                    adj_i, adj_j = rotten_i + di, rotten_j + dj
                    # If the adjacent cell is out of bounds or not a fresh orange, continue to the next direction
                    if (
                        adj_i < 0
                        or adj_i >= len(grid)
                        or adj_j < 0
                        or adj_j >= len(grid[0])
                        or grid[adj_i][adj_j] != 1
                    ):
                        continue
                    # Change the fresh orange to a rotten orange
                    grid[adj_i][adj_j] = 2
                    # Decrease the counter of fresh oranges
                    fresh_oranges -= 1
                    # Add the new rotten orange to the queue
                    rotten_queue.append((adj_i, adj_j))
                print(f"Fresh oranges after rotting: {
                      fresh_oranges}, rotten queue: {rotten_queue}")
            # Increase the time counter
            time_counter += 1
            print(f"Time counter: {time_counter}")

        # If there are no fresh oranges left, return the time counter. Otherwise, return -1
        return time_counter if fresh_oranges == 0 else -1


sol = Solution()


print(sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))  # 4
print(sol.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))  # -1
print(sol.orangesRotting([[0, 2]]))  # 0
