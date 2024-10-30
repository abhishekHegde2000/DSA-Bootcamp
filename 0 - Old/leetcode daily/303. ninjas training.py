'''
https://www.naukri.com/code360/problems/ninja-s-training_3621003

 Ninja’s Training
Moderate
0/80
Average time to solve is 30m
Contributed by
806 upvotes
Asked in companies
Problem statement
Ninja is planing this ‘N’ days-long training schedule. Each day, he can perform any one of these three activities. (Running, Fighting Practice or Learning New Moves). Each activity has some merit points on each day. As Ninja has to improve all his skills, he can’t do the same activity in two consecutive days. Can you help Ninja find out the maximum merit points Ninja can earn?

You are given a 2D array of size N*3 ‘POINTS’ with the points corresponding to each day and activity. Your task is to calculate the maximum number of merit points that Ninja can earn.

For Example
If the given ‘POINTS’ array is [[1,2,5], [3 ,1 ,1] ,[3,3,3] ],the answer will be 11 as 5 + 3 + 3.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 10
1 <= N <= 100000.
1 <= values of POINTS arrays <= 100 .

Time limit: 1 sec
Sample Input 1:
2
3
1 2 5
3 1 1
3 3 3
3
10 40 70
20 50 80
30 60 90
Sample Output 1:
11
210
Explanation of sample input 1:
For the first test case,
One of the answers can be:
On the first day, Ninja will learn new moves and earn 5 merit points.
On the second day, Ninja will do running and earn 3 merit points.
On the third day, Ninja will do fighting and earn 3 merit points.
The total merit point is 11 which is the maximum.
Hence, the answer is 11.

For the second test case:
One of the answers can be:
On the first day, Ninja will learn new moves and earn 70 merit points.
On the second day, Ninja will do fighting and earn 50 merit points.
On the third day, Ninja will learn new moves and earn 90 merit points.
The total merit point is 210 which is the maximum.
Hence, the answer is 210.
Sample Input 2:
2
3
18 11 19
4 13 7
1 8 13
2
10 50 1
5 100 11
Sample Output 2:
45
110
'''
from typing import *


def ninjaTraining(n: int, points: List[List[int]]) -> int:

    days = n
    dp = [[0] * 3 for _ in range(days)]

    for i in range(3):
        dp[0][i] = points[0][i]

    print(dp)

    for i in range(1, days):
        for j in range(3):
            for k in range(3):
                if j != k:
                    dp[i][j] = max(dp[i][j], points[i][j] + dp[i - 1][k])

    return max(dp[-1])


def ninjaTraining_dfs(n: int, points: List[List[int]]) -> int:
    days = n
    dp = [[0] * 3 for _ in range(days)]

    def dfs(day, activity):
        if day >= days:
            return 0

        if dp[day][activity] != 0:
            return dp[day][activity]

        max_points = 0

        for i in range(3):
            if i != activity:
                max_points = max(max_points, points[day][i] + dfs(day + 1, i))

        dp[day][activity] = max_points

        return dp[day][activity]

    # Initialize for the first day
    max_total_points = 0
    for i in range(3):
        max_total_points = max(max_total_points, dfs(0, i))

    return max_total_points


print(ninjaTraining(3, [[1, 2, 5], [3, 1, 1], [3, 3, 3]]))  # 11
print(ninjaTraining(3, [[10, 40, 70], [20, 50, 80], [30, 60, 90]]))  # 210
print(ninjaTraining(3, [[18, 11, 19], [4, 13, 7], [1, 8, 13]]))  # 45
print(ninjaTraining(2, [[10, 50, 1], [5, 100, 11]]))  # 110

print(ninjaTraining_dfs(3, [[1, 2, 5], [3, 1, 1], [3, 3, 3]]))  # 11
print(ninjaTraining_dfs(3, [[10, 40, 70], [20, 50, 80], [30, 60, 90]]))  # 210
print(ninjaTraining_dfs(3, [[18, 11, 19], [4, 13, 7], [1, 8, 13]]))  # 45
print(ninjaTraining_dfs(2, [[10, 50, 1], [5, 100, 11]]))  # 110
