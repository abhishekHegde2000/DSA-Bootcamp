'''
https://leetcode.com/problems/set-matrix-zeroes/description/

73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows_to_zero = set()
        cols_to_zero = set()

        ROWS, COLS = len(matrix), len(matrix[0])

        # Identify positions of zero elements
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)

        # Update rows to zero
        for row in rows_to_zero:
            for col in range(COLS):
                matrix[row][col] = 0

        # Update columns to zero
        for col in cols_to_zero:
            for row in range(ROWS):
                matrix[row][col] = 0


def setMatrixZeroes(matrix):
    rows_to_zero = set()
    cols_to_zero = set()

    num_rows, num_cols = len(matrix), len(matrix[0])

    # Identify positions of zero elements
    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[row][col] == 0:
                print(f"Found zero at position ({row}, {col})")
                rows_to_zero.add(row)
                cols_to_zero.add(col)

    print(f"Rows to zero: {rows_to_zero}")
    print(f"Columns to zero: {cols_to_zero}")

    # Update rows to zero
    for row in rows_to_zero:
        for col in range(num_cols):
            print(f"Setting position ({row}, {col}) to zero")
            matrix[row][col] = 0

    # Update columns to zero
    for col in cols_to_zero:
        for row in range(num_rows):
            print(f"Setting position ({row}, {col}) to zero")
            matrix[row][col] = 0


sol = Solution()

# [[1,0,1],[0,0,0],[1,0,1]]
print(sol.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
# [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
print(sol.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
