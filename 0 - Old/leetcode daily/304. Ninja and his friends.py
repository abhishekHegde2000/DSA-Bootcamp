'''
https://takeuforward.org/data-structure/3-d-dp-ninja-and-his-friends-dp-13/

https://www.naukri.com/code360/problems/chocolate-pickup_3125885?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf


Problem statement
Ninja has a 'GRID' of size 'R' X 'C'. Each cell of the grid contains some chocolates. Ninja has two friends Alice and Bob, and he wants to collect as many chocolates as possible with the help of his friends.

Initially, Alice is in the top-left position i.e. (0, 0), and Bob is in the top-right place i.e. (0, ‘C’ - 1) in the grid. Each of them can move from their current cell to the cells just below them. When anyone passes from any cell, he will pick all chocolates in it, and then the number of chocolates in that cell will become zero. If both stay in the same cell, only one of them will pick the chocolates in it.

If Alice or Bob is at (i, j) then they can move to (i + 1, j), (i + 1, j - 1) or (i + 1, j + 1). They will always stay inside the ‘GRID’.

Your task is to find the maximum number of chocolates Ninja can collect with the help of his friends by following the above rules.

Example:
Input: ‘R’ = 3, ‘C’ = 4
       ‘GRID’ = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]
Output: 21

Initially Alice is at the position (0,0) he can follow the path (0,0) -> (1,1) -> (2,1) and will collect 2 + 4 + 6 = 12 chocolates.

Initially Bob is at the position (0, 3) and he can follow the path (0, 3) -> (1,3) -> (2, 3) and will colllect 2 + 2 + 5 = 9 chocolates.

Hence the total number of chocolates collected will be 12 + 9 = 21. there is no other possible way to collect a greater number of chocolates than 21.
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= ‘T’ <= 10
2 <= 'R', 'C' <= 50
0 <= 'GRID[i][j]'<= 10^2
Time Limit: 1sec
Sample Input 1 :
2
3 4
2 3 1 2
3 4 2 2
5 6 3 5
2 2
1 1
1 2
Sample Output 1 :
21
5
Explanation Of Sample Input 1 :
For the first test case, Initially Alice is at the position (0, 0) he can follow the path (0, 0) -> (1, 1) -> (2, 1) and will collect 2 + 4 + 6 = 12 chocolates.

Initially Bob is at the position (0, 3) and he can follow the path (0, 3) -> (1, 3) -> (2, 3) and will collect 2 + 2 + 5 = 9 chocolates.

Hence the total number of chocolates collected will be 12 + 9 = 21.

For the second test case, Alice will follow the path (0, 0) -> (1, 0) and Bob will follow the path (0, 1) -> (1, 1). total number of chocolates collected will be 1 + 1 + 1 + 2 = 5
Sample Input 2 :
2
2 2
3 7
7 6
3 2
4 5
3 7
4 2
Sample Output 2 :
23
25
'''


from os import *
from sys import *
from collections import *
from math import *

from typing import List


'''
    Time complexity: O(3^(R*C))
    Space complexity: O(R*C)

    Where 'R' is the number of rows and 'C' is the number of columns in the grid.
'''


def maximumChocolatesHelper(currRow: int, c1: int, c2: int, grid: List[List[int]]) -> int:

    # Return 0 if current coordinates are not valid.
    if (currRow == len(grid) or c1 < 0 or c1 >= len(grid[0]) or c2 < 0 or c2 >= len(grid[0]) or c1 > c2):
        return 0

    # Initializing the variable 'maximumChocolates'.
    maximumChocolates = 0

    for i in range(-1, 2):
        for j in range(-1, 2):

            # Updating the variable 'maximumChocolates'.
            maximumChocolates = max(maximumChocolates, maximumChocolatesHelper(
                currRow + 1, c1 + i, c2 + j, grid))

    # Condition when both of them are on same coordinate.
    if (c1 != c2):
        maximumChocolates += grid[currRow][c2]

    return (maximumChocolates + grid[currRow][c1])


def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:

    return maximumChocolatesHelper(0, 0, c - 1, grid)

# ---------------------------------------------------------------------------------


'''
    Time complexity: O(R*(C^2))
    Space complexity: O(R*(C^2))

    Where 'R' is the number of rows and 'C' is the number of columns in the grid.
'''


def maximumChocolatesHelper(currRow: int, c1: int, c2: int, grid: List[List[int]], dp: List[List[List[int]]]) -> int:

    # Return 0 if current coordinates are not valid.
    if (currRow == len(grid) or c1 < 0 or c1 >= len(grid[0]) or c2 < 0 or c2 >= len(grid[0]) or c1 > c2):
        return 0

    # If current state is already visited.
    if (dp[currRow][c1][c2] != -1):
        return dp[currRow][c1][c2]

    # Initializing the variable 'maximumChocolates'.
    maximumChocolates = 0

    for i in range(-1, 2):
        for j in range(-1, 2):

            # Updating the variable 'maximumChocolates'.
            maximumChocolates = max(maximumChocolates, maximumChocolatesHelper(
                currRow + 1, c1 + i, c2 + j, grid, dp))

    # Condition when both of them are on same coordinate.
    if (c1 != c2):
        maximumChocolates += grid[currRow][c2]

    dp[currRow][c1][c2] = (maximumChocolates + grid[currRow][c1])
    return dp[currRow][c1][c2]


def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:

    dp = [[[-1 for i in range(c)] for j in range(c)] for k in range(r)]
    return maximumChocolatesHelper(0, 0, c - 1, grid, dp)

# ---------------------------------------------------------------------------------


'''
    Time complexity: O(R*(C^2))
    Space complexity: O(C^2)

    Where 'R' is the number of rows and 'C' is the number of columns in the grid.
'''


def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    # Initializing the 'prev_dp' vector.
    prev_dp = [[0 for i in range(c)] for j in range(c)]

    # Running a loop from 0 to 'r'.
    for row in range(r):
        # Initializing a 'current_dp' vector.
        current_dp = [[0 for i in range(c)] for j in range(c)]

        # Running a loop from 0 to 'min(c, row + 1)'.
        for c1 in range(min(c, row + 1)):
            # Running a loop from 'max(0, c - 1 - row)' to 'c'.
            for c2 in range(max(0, c-1-row), c):

                # Initializing a variable 'prev_max'.
                prev_max = 0

                for offset1 in range(max(0, c1 - 1), min(c-1, c1 + 1) + 1):
                    for offset2 in range(max(0, c2-1), min(c-1, c2 + 1)+1):
                        #  Updating the variable 'prev_max'.
                        prev_max = max(prev_max, prev_dp[offset1][offset2])

                # Case when both are in same row.
                if (c1 == c2):
                    current_dp[c1][c2] = prev_max + grid[row][c1]
                else:
                    current_dp[c1][c2] = prev_max + \
                        grid[row][c1] + grid[row][c2]

        prev_dp = current_dp

    res = 0
    for i in range(c):
        for j in range(c):
            # Updating the variable 'res' with max possible answer.
            res = max(res, prev_dp[i][j])

    return res


print(maximumChocolates(
    3, 4, [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]))  # 21
print(maximumChocolates(2, 2, [[1, 1], [1, 2]]))  # 5
print(maximumChocolates(2, 2, [[3, 7], [7, 6]]))  # 23
