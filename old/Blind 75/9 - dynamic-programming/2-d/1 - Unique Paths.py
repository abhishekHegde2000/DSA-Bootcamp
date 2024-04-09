'''
https://leetcode.com/problems/unique-paths/description/

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100

https://takeuforward.org/data-structure/grid-unique-paths-dp-on-grids-dp8/

'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[-1 for col in range(n)] for row in range(m)]

        def helper(r, c):

            if r < 0 or c < 0:
                return 0

            if r == 0 and c == 0:
                return 1

            if dp[r][c] != -1:
                return dp[r][c]

            up = helper(r-1, c)
            left = helper(r, c-1)

            dp[r][c] = up + left

            return dp[r][c]

        return helper(m-1, n-1)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize the dp table
        dp = [[1 if i == 0 or j ==
               0 else 0 for j in range(n)] for i in range(m)]
        print(f"Initial dp: {dp}")

        # Iterate over the dp table starting from the second row and second column
        for i in range(1, m):
            for j in range(1, n):
                print(f"\nProcessing cell ({i}, {j})")

                # Update the number of unique paths to the current cell
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                print(f"Updated dp: {dp}")

        # Return the number of unique paths to the bottom-right cell
        return dp[-1][-1]


sol = Solution()


print(sol.uniquePaths(3, 3))  # 6
print(sol.uniquePaths(3, 7))  # 28
print(sol.uniquePaths(3, 2))  # 3
