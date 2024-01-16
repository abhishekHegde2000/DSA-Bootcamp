'''
https://leetcode.com/problems/symmetric-tree/description/?envType=study-plan-v2&envId=top-interview-150

101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?
'''

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Helper function to check if two nodes are symmetric
        def isMirror(node1, node2):
            # If both nodes are null, they are symmetric
            if not node1 and not node2:
                return True
            # If only one of the nodes is null, they are not symmetric
            if not node1 or not node2:
                return False

            # Two nodes are symmetric if their values are equal and their respective left and right children are also symmetric
            return (node1.val == node2.val) and isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)

        # If the root is null, the tree is symmetric
        if not root:
            return True

        # Check if the left and right children of the root are symmetric
        return isMirror(root.left, root.right)


sol = Solution()
print(sol.isSymmetric(root=[1, 2, 2, 3, 4, 4, 3]))
print(sol.isSymmetric(root=[1, 2, 2, None, 3, None, 3]))
print(sol.isSymmetric(root=[1, 2, 2, 3, 4, 4, 3]))
print(sol.isSymmetric(root=[1, 2, 2, None, 3, None, 3]))
