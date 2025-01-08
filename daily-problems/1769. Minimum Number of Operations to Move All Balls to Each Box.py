'''

https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

1769. Minimum Number of Operations to Move All Balls to Each Box
Solved
Medium
Topics
Companies
Hint
You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

Each answer[i] is calculated considering the initial state of the boxes.



Example 1:

Input: boxes = "110"
Output: [1,1,3]
Explanation: The answer for each box is as follows:
1) First box: you will have to move one ball from the second box to the first box in one operation.
2) Second box: you will have to move one ball from the first box to the second box in one operation.
3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
Example 2:

Input: boxes = "001011"
Output: [11,8,5,4,3,4]


Constraints:

n == boxes.length
1 <= n <= 2000
boxes[i] is either '0' or '1'.
'''
from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n

        # Left to right pass
        left_count = 0  # Number of balls to the left
        left_operations = 0  # Cumulative operations from the left
        for i in range(n):
            answer[i] += left_operations
            if boxes[i] == '1':
                left_count += 1
            left_operations += left_count  # Add the cost of moving left balls to box i

        # Right to left pass
        right_count = 0  # Number of balls to the right
        right_operations = 0  # Cumulative operations from the right
        for i in range(n - 1, -1, -1):
            answer[i] += right_operations
            if boxes[i] == '1':
                right_count += 1
            right_operations += right_count  # Add the cost of moving right balls to box i

        return answer


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n

        balls_to_left = 0
        moves_to_left = 0
        balls_to_right = 0
        moves_to_right = 0

        # Single pass: calculate moves from both left and right
        for i in range(n):
            # Left pass
            answer[i] += moves_to_left
            balls_to_left += int(boxes[i])
            moves_to_left += balls_to_left

            # Right pass
            j = n - 1 - i
            answer[j] += moves_to_right
            balls_to_right += int(boxes[j])
            moves_to_right += balls_to_right

        return answer


sol = Solution()

print(sol.minOperations("110"))  # [1,1,3]
print(sol.minOperations("001011"))  # [11,8,5,4,3,4]
