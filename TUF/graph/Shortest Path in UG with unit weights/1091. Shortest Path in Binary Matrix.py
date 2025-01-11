'''
https://leetcode.com/problems/shortest-path-in-binary-matrix/


1091. Shortest Path in Binary Matrix
Solved
Medium
Topics
Companies
Hint
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.



Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1


Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
'''

from collections import deque
from typing import List


from typing import List

from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        # Check if the source or destination is blocked
        if grid[source[0]][source[1]] != 1 or grid[destination[0]][destination[1]] != 1:
            return -1

        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Initialize BFS
        queue = deque([(source[0], source[1], 0)])  # (row, col, distance)
        visited = set((source[0], source[1]))

        while queue:
            r, c, distance = queue.popleft()

            # Check if we reached the destination
            if [r, c] == destination:
                return distance

            # Explore neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
                    queue.append((nr, nc, distance + 1))
                    visited.add((nr, nc))

        return -1


sol = Solution()

print(sol.shortestPathBinaryMatrix([[0, 1], [1, 0]]))  # 2
print(sol.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))  # 4
print(sol.shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]))  # -1


# time complexity: O(n * m)
# reason: We are visiting each cell at most once. and we are visiting all the cells in the worst case.

# space complexity: O(n * m)
