'''
https://leetcode.com/problems/path-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75

437. Path Sum III
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.numberOfPaths = 0

        def helper(node, currentSum):
            if not node:
                return
            print(f"Current node value: {node.val}, Current sum: {currentSum}")
            if currentSum + node.val == targetSum:
                self.numberOfPaths += 1
                print(f"Found a path with sum {targetSum}")
            currentSum += node.val
            helper(node.left, currentSum)
            helper(node.right, currentSum)

        def dfs(node):
            if not node:
                return
            print(f"DFS on node with value: {node.val}")
            helper(node, 0)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        print(f"Total number of paths with sum {
              targetSum}: {self.numberOfPaths}")
        return self.numberOfPaths