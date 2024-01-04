'''
74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        number_of_rows = len(matrix)
        number_of_columns = len(matrix[0])  # Get dimensions of the matrix

        lowest_possible_index = 0
        highest_possible_index = number_of_rows * \
            number_of_columns - 1  # Set boundaries

        while lowest_possible_index <= highest_possible_index:
            middle_index = (lowest_possible_index +
                            highest_possible_index) // 2

            row_index = middle_index // number_of_columns  # Map to matrix coordinates
            column_index = middle_index % number_of_columns

            print(f"Searching at row {row_index}, column {
                  column_index} (index {middle_index})")  # Debugging print

            if matrix[row_index][column_index] == target:
                return True  # Target found
            elif matrix[row_index][column_index] < target:
                lowest_possible_index = middle_index + 1  # Focus on the right half
            else:
                highest_possible_index = middle_index - 1  # Focus on the left half

        return False  # Target not found


# Test case
matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17],
]
target = 5

sol = Solution()
result = sol.searchMatrix(matrix, target)

if result:
    print(f"Target {target} found in the matrix.")
else:
    print(f"Target {target} not found in the matrix.")
