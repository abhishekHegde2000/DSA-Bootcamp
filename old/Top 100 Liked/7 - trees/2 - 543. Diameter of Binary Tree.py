'''
https://leetcode.com/problems/diameter-of-binary-tree/

543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
'''


from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        nonlocal_max = 0

        def deapth(node):
            if not node:
                return 0

            left = deapth(node.left)
            right = deapth(node.right)

            nonlocal nonlocal_max
            nonlocal_max = max(nonlocal_max, left + right)

            return max(left, right) + 1

        deapth(root)
        return nonlocal_max


sol = Solution()

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)),
                TreeNode(3))  # [1,2,3,4,5]
print(sol.diameterOfBinaryTree(root))  # 3

root = TreeNode(1, TreeNode(2))  # [1,2]
print(sol.diameterOfBinaryTree(root))  # 1
