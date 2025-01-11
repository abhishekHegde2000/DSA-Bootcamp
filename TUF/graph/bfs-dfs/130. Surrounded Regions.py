'''

https://leetcode.com/problems/surrounded-regions/


130. Surrounded Regions
Solved
Medium
Topics
Companies
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.



Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]



Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.

'''

from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        R, C = len(board), len(board[0])

        # Directions for BFS: up, down, left, right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Function to perform BFS starting from (r, c)
        def bfs(r, c):
            queue = deque([(r, c)])
            while queue:
                row, col = queue.popleft()
                if 0 <= row < R and 0 <= col < C and board[row][col] == 'O':
                    board[row][col] = 'T'  # Mark as temporary 'T'
                    for dr, dc in directions:
                        queue.append((row + dr, col + dc))

        # Step 1: Process borders and their connected regions
        for i in range(R):
            for j in range(C):
                if (i == 0 or i == R - 1 or j == 0 or j == C - 1) and board[i][j] == 'O':
                    bfs(i, j)

        # Step 2: Convert remaining 'O's to 'X' and revert 'T's back to 'O'
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        R, C = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or board[r][c] != 'O':
                return

            board[r][c] = 'T'  # Mark as temporary 'T'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Process borders and their connected regions
        for i in range(R):
            for j in range(C):
                if (i == 0 or i == R - 1 or j == 0 or j == C - 1) and board[i][j] == 'O':
                    dfs(i, j)

        # Step 2: Convert remaining 'O's to 'X' and revert 'T's back to 'O'
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'


sol = Solution()

# [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
print(sol.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"],
      ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
print(sol.solve([["X"]]))  # [["X"]]
# [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
print(sol.solve([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]))
