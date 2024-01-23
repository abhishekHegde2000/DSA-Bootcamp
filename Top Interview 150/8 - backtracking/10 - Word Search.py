'''
https://leetcode.com/problems/word-search/description/

79. Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?

'''

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get the number of rows and columns in the board
        rows, cols = len(board), len(board[0])
        # Initialize path to store the cells that are already visited
        path = set()

        def backtrack(current_row, current_col, current_index):
            # Print current state
            print(f"Current Row: {current_row}, Current Col: {
                  current_col}, Current Index: {current_index}, Path: {path}")

            # If current_index is equal to the length of the word, return True
            if current_index == len(word):
                return True

            # If the current cell is out of the board's boundaries or the character at the current cell is not equal to the character at current_index in the word or the current cell is already visited, return False
            if (current_row < 0 or current_col < 0) or (current_row >= rows or current_col >= cols) or (word[current_index] != board[current_row][current_col]) or ((current_row, current_col) in path):
                return False

            # Add the current cell to path
            path.add((current_row, current_col))

            # Recursively call backtrack for the right, left, down, and up cells
            res = (backtrack(current_row + 1, current_col, current_index + 1) or
                   backtrack(current_row - 1, current_col, current_index + 1) or
                   backtrack(current_row, current_col + 1, current_index + 1) or
                   backtrack(current_row, current_col - 1, current_index + 1))

            # Remove the current cell from path
            path.remove((current_row, current_col))

            # Return the result of the recursive calls
            return res

        # Iterate over the cells in the board
        for r in range(rows):
            for c in range(cols):
                # If backtrack returns True, return True
                if backtrack(r, c, 0):
                    return True
        # If no valid path is found, return False
        return False


sol = Solution()

print(sol.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], [
      "A", "D", "E", "E"]], word="ABCCED"))  # True
print(sol.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], [
      "A", "D", "E", "E"]], word="SEE"))  # True
print(sol.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], [
      "A", "D", "E", "E"]], word="ABCB"))  # False
