'''
https://leetcode.com/problems/path-sum/description/?envType=study-plan-v2&envId=top-interview-150
112. Path Sum

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
'''

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, remainingSum):
            if not node:
                print("Node is None. Returning False.")
                return False

            if not node.left and not node.right:
                print(
                    f"Node {node.val} is a leaf. Checking if its value equals the remaining sum.")
                return node.val == remainingSum

            print(f"Checking if the updated remaining sum can be obtained in the left subtree or the right subtree of node {
                  node.val}")
            return dfs(node.left, remainingSum - node.val) or dfs(node.right, remainingSum - node.val)

        print("Starting to check if the tree has a path with the target sum")
        return dfs(root, targetSum)


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currentSum):
            if not node:
                print("Node is None. Returning False.")
                return False

            currentSum += node.val
            print(f"Added node {
                  node.val} value to current sum. Current sum is {currentSum}")

            if not node.left and not node.right:
                print(
                    f"Node {node.val} is a leaf. Checking if current sum equals the target sum.")
                return currentSum == targetSum

            print(f"Checking if the target sum can be obtained in the left subtree or the right subtree of node {
                  node.val}")
            return dfs(node.left, currentSum) or dfs(node.right, currentSum)

        print("Starting to check if the tree has a path with the target sum")
        return dfs(root, 0)
