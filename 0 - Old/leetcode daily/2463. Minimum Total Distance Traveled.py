'''

https://leetcode.com/problems/minimum-total-distance-traveled/https://leetcode.com/problems/minimum-total-distance-traveled/


2463. Minimum Total Distance Traveled
Hard
Topics
Companies
Hint
There are some robots and factories on the X-axis. You are given an integer array robot where robot[i] is the position of the ith robot. You are also given a 2D integer array factory where factory[j] = [positionj, limitj] indicates that positionj is the position of the jth factory and that the jth factory can repair at most limitj robots.

The positions of each robot are unique. The positions of each factory are also unique. Note that a robot can be in the same position as a factory initially.

All the robots are initially broken; they keep moving in one direction. The direction could be the negative or the positive direction of the X-axis. When a robot reaches a factory that did not reach its limit, the factory repairs the robot, and it stops moving.

At any moment, you can set the initial direction of moving for some robot. Your target is to minimize the total distance traveled by all the robots.

Return the minimum total distance traveled by all the robots. The test cases are generated such that all the robots can be repaired.

Note that

All robots move at the same speed.
If two robots move in the same direction, they will never collide.
If two robots move in opposite directions and they meet at some point, they do not collide. They cross each other.
If a robot passes by a factory that reached its limits, it crosses it as if it does not exist.
If the robot moved from a position x to a position y, the distance it moved is |y - x|.


Example 1:


Input: robot = [0,4,6], factory = [[2,2],[6,2]]
Output: 4
Explanation: As shown in the figure:
- The first robot at position 0 moves in the positive direction. It will be repaired at the first factory.
- The second robot at position 4 moves in the negative direction. It will be repaired at the first factory.
- The third robot at position 6 will be repaired at the second factory. It does not need to move.
The limit of the first factory is 2, and it fixed 2 robots.
The limit of the second factory is 2, and it fixed 1 robot.
The total distance is |2 - 0| + |2 - 4| + |6 - 6| = 4. It can be shown that we cannot achieve a better total distance than 4.
Example 2:


Input: robot = [1,-1], factory = [[-2,1],[2,1]]
Output: 2
Explanation: As shown in the figure:
- The first robot at position 1 moves in the positive direction. It will be repaired at the second factory.
- The second robot at position -1 moves in the negative direction. It will be repaired at the first factory.
The limit of the first factory is 1, and it fixed 1 robot.
The limit of the second factory is 1, and it fixed 1 robot.
The total distance is |2 - 1| + |(-2) - (-1)| = 2. It can be shown that we cannot achieve a better total distance than 2.


Constraints:

1 <= robot.length, factory.length <= 100
factory[j].length == 2
-109 <= robot[i], positionj <= 109
0 <= limitj <= robot.length
The input will be generated such that it is always possible to repair every robot.
🎉 Thank you for your feedback!
Accepted
12.5K
Submissions
27.3K
Acceptance Rate
46.0%
Topics
Array
Dynamic Programming
Sorting
Companies
Hint 1
Sort robots and factories by their positions.
Hint 2
After sorting, notice that each factory should repair some subsegment of robots.
Hint 3
Find the minimum total distance to repair first i robots with first j factories.




'''

from typing import List
from collections import deque


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Sort positions to enable optimal matching
        robot.sort()
        factory.sort()

        m, n = len(robot), len(factory)
        # DP table initialization
        dp = [[0]*(n+1) for _ in range(m+1)]

        # Base case: if no factories left, distance is infinite
        for i in range(m):
            dp[i][-1] = float('inf')

        # Process each factory from right to left
        for j in range(n-1, -1, -1):
            prefix = 0
            qq = deque([(m, 0)])

            # Process each robot from right to left
            for i in range(m-1, -1, -1):
                # Add distance to current factory
                prefix += abs(robot[i] - factory[j][0])

                # Remove elements outside factory limit window
                if qq[0][0] > i+factory[j][1]:
                    qq.popleft()

                # Maintain monotonic queue property
                while qq and qq[-1][1] >= dp[i][j+1] - prefix:
                    qq.pop()

                qq.append((i, dp[i][j+1] - prefix))
                dp[i][j] = qq[0][1] + prefix

        return dp[0][0]


sol = Solution()

print(sol.minimumTotalDistance(robot=[0, 4, 6], factory=[[2, 2], [6, 2]]))  # 4
print(sol.minimumTotalDistance(robot=[1, -1], factory=[[-2, 1], [2, 1]]))  # 2
