'''
https://leetcode.com/problems/path-sum-ii/description/

113. Path Sum II

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
'''

from typing import List, Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
#         resultPaths = []
#         self.dfs(root, targetSum, [], resultPaths)
#         return resultPaths

#     def dfs(self, node, remainingSum, path, resultPaths):
#         if node:
#             print(f"Visiting node with value {
#                   node.val}. Remaining sum is {remainingSum}.")
#             if not node.left and not node.right and remainingSum == node.val:
#                 print(f"Found a path with sum {remainingSum}.")
#                 resultPaths.append(path + [node.val])

#             print(f"Going left from node with value {node.val}.")
#             self.dfs(node.left, remainingSum - node.val,
#                      path + [node.val], resultPaths)
#             print(f"Going right from node with value {node.val}.")
#             self.dfs(node.right, remainingSum - node.val,
#                      path + [node.val], resultPaths)

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def backtrack(node, path, remainingSum):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and remainingSum == node.val:
                resultPaths.append(path.copy())
            backtrack(node.left, path, remainingSum - node.val)
            backtrack(node.right, path, remainingSum - node.val)
            path.pop()

        resultPaths = []
        if root is None:
            return []
        backtrack(root, [], targetSum)
        return resultPaths


sol = Solution()
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)
print(sol.pathSum(root, 22))
