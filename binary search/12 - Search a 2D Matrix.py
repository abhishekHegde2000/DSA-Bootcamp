''' 
74. Search a 2D Matrix
Solved
Medium
Topics
Companies
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

'''

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS - 1

        while top <= bottom:
            row = (top + bottom) // 2
            print(f"Checking row: {row}")
            if matrix[row][0] <= target <= matrix[row][-1]:
                print("Target could be in this row, searching...")
                left, right = 0, COLS - 1
                while left <= right:
                    middle = (left + right) // 2
                    if matrix[row][middle] == target:
                        print("Found target.")
                        return True
                    elif matrix[row][middle] > target:
                        right = middle - 1
                    else:
                        left = middle + 1
                print("Target not found in this row.")
                return False
            elif matrix[row][0] > target:
                print(
                    "Target is less than the first element of this row, searching previous rows.")
                bottom = row - 1
            else:
                print(
                    "Target is greater than the last element of this row, searching next rows.")
                top = row + 1

        print("Target not found.")
        return False


sol = Solution()
print(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
