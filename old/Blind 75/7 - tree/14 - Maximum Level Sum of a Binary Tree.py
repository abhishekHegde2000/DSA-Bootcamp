'''
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

1161. Maximum Level Sum of a Binary Tree

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105

'''

from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # Initialize the maximum sum to negative infinity, the level counter to 0, and the level of the maximum sum to 0
        max_sum, level_counter, max_sum_level = -float('inf'), 0, 0
        # Initialize a queue and add the root node to it
        queue = deque()
        queue.append(root)
        # While the queue is not empty
        while queue:
            # Increment the level counter
            level_counter += 1
            # Initialize the sum of the current level to 0
            current_level_sum = 0
            # For each node in the current level
            for _ in range(len(queue)):
                # Remove the node from the queue
                node = queue.popleft()
                # Add the node's value to the sum of the current level
                current_level_sum += node.val
                # If the node has a left child, add it to the queue
                if node.left:
                    queue.append(node.left)
                # If the node has a right child, add it to the queue
                if node.right:
                    queue.append(node.right)
            # Print the level and the sum of the current level for debugging purposes
            print(f"Level: {level_counter}, Sum: {current_level_sum}")
            # If the sum of the current level is greater than the maximum sum
            if max_sum < current_level_sum:
                # Update the maximum sum and the level of the maximum sum
                max_sum, max_sum_level = current_level_sum, level_counter
                # Print the new maximum sum and its level for debugging purposes
                print(f"New max sum: {max_sum} at level {max_sum_level}")
        # Return the level of the maximum sum
        return max_sum_level
