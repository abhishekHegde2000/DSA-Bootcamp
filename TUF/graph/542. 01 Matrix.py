'''
https://leetcode.com/problems/01-matrix/

542. 01 Matrix
Solved
Medium
Topics
Companies
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.



Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
'''

from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        inf = 10 ** 5

        R, C = len(mat), len(mat[0])

        distance = [[inf] * C for _ in range(R)]

        q = deque()

        for i in range(R):
            for j in range(C):
                if mat[i][j] == 0:
                    distance[i][j] = 0
                    q.append((i, j))

        while q:
            r, c = q.popleft()

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < R and 0 <= nc < C and distance[nr][nc] == inf:
                    distance[nr][nc] = distance[r][c] + 1
                    q.append((nr, nc))

        return distance


sol = Solution()

# [[0,0,0],[0,1,0],[0,0,0]]
print(sol.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
# [[0,0,0],[0,1,0],[1,2,1]]
print(sol.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
print(sol.updateMatrix([[0, 1]]))  # [[0,1]]
