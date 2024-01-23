'''
https://leetcode.com/problems/n-queens/description/?envType=study-plan-v2&envId=top-100-liked

51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9


'''
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Initialize result list
        solutions = []
        # Initialize board
        board = [["."] * n for row in range(n)]
        # Initialize sets to store the columns and diagonals that are already occupied by queens
        columns = set()
        positive_diagonals = set()
        negative_diagonals = set()

        def backtrack(current_row):
            # Print current state
            print(f"Current Row: {current_row}, Board: {board}")

            # If current row is equal to n, a valid configuration is found
            if current_row == n:
                solution = ["".join(row) for row in board]
                solutions.append(solution)
                return

            # Iterate over the columns from 0 to n - 1
            for current_column in range(n):
                # If current column is in columns or current row + current column is in positive diagonals or current row - current column is in negative diagonals, skip this column
                if current_column in columns or current_row + current_column in positive_diagonals or current_row - current_column in negative_diagonals:
                    continue

                # Add a queen at the position (current row, current column) on board
                board[current_row][current_column] = "Q"
                # Add current column, current row + current column, and current row - current column to columns, positive diagonals, and negative diagonals respectively
                columns.add(current_column)
                positive_diagonals.add(current_row + current_column)
                negative_diagonals.add(current_row - current_column)

                # Recursively call backtrack with current row + 1
                backtrack(current_row + 1)

                # Remove the queen from the position (current row, current column) on board
                board[current_row][current_column] = "."
                # Remove current column, current row + current column, and current row - current column from columns, positive diagonals, and negative diagonals respectively
                columns.remove(current_column)
                positive_diagonals.remove(current_row + current_column)
                negative_diagonals.remove(current_row - current_column)

        # Call backtrack with initial parameters
        backtrack(0)
        # Return solutions
        return solutions


sol = Solution()

# [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
print(sol.solveNQueens(4))
print(sol.solveNQueens(1))  # [["Q"]]
