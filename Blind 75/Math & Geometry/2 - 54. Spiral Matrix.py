'''
https://leetcode.com/problems/spiral-matrix/description/

54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

'''
from typing import List


from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        numRows, numCols = len(matrix), len(matrix[0])
        topBoundary, bottomBoundary = 0, numRows - 1
        leftBoundary, rightBoundary = 0, numCols - 1
        result = []
        while topBoundary <= bottomBoundary and leftBoundary <= rightBoundary:
            print(f"Current boundaries: top={topBoundary}, bottom={
                  bottomBoundary}, left={leftBoundary}, right={rightBoundary}")

            # Add all elements from left to right in the top row to result
            for i in range(leftBoundary, rightBoundary + 1):
                result.append(matrix[topBoundary][i])
            topBoundary += 1
            print(f"Result after traversing top row: {result}")

            # Add all elements from top to bottom in the right column to result
            for i in range(topBoundary, bottomBoundary + 1):
                result.append(matrix[i][rightBoundary])
            rightBoundary -= 1
            print(f"Result after traversing right column: {result}")

            # If there are still rows remaining, add all elements from right to left in the bottom row to result
            if topBoundary <= bottomBoundary:
                for i in range(rightBoundary, leftBoundary - 1, -1):
                    result.append(matrix[bottomBoundary][i])
                bottomBoundary -= 1
                print(f"Result after traversing bottom row: {result}")

            # If there are still columns remaining, add all elements from bottom to top in the left column to result
            if leftBoundary <= rightBoundary:
                for i in range(bottomBoundary, topBoundary - 1, -1):
                    result.append(matrix[i][leftBoundary])
                leftBoundary += 1
                print(f"Result after traversing left column: {result}")

        return result


sol = Solution()

# [1,2,3,6,9,8,7,4,5]
print(sol.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# [1,2,3,4,8,12,11,10,9,5,6,7]
print(sol.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
# [1,2,3,4,5,6,7,8,9,10]
print(sol.spiralOrder([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]))
# [1,2,3,4,5,6,7,8,9,10]
print(sol.spiralOrder([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]))
