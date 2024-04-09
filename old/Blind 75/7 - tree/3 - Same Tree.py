'''
100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
'''

from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
        print(f"Checking if the trees with root values {
              tree1.val if tree1 else 'None'} and {tree2.val if tree2 else 'None'} are the same")

        # If both trees are None, return True
        if not tree1 and not tree2:
            print("Both trees are empty")
            return True

        # If one of the trees is None or the values of the current nodes are not equal, return False
        if not tree1 or not tree2 or tree1.val != tree2.val:
            print("The trees are not the same")
            return False

        # Recursively check if the left and right subtrees of the two trees are the same
        print(f"Checking if the left subtrees of the nodes with values {
              tree1.val} and {tree2.val} are the same")
        is_left_same = self.isSameTree(tree1.left, tree2.left)
        print(f"Checking if the right subtrees of the nodes with values {
              tree1.val} and {tree2.val} are the same")
        is_right_same = self.isSameTree(tree1.right, tree2.right)

        # Return True if both the left and right subtrees are the same, False otherwise
        is_same = is_left_same and is_right_same
        print(f"The trees with root values {tree1.val} and {
              tree2.val} are {'the same' if is_same else 'not the same'}")
        return is_same

    def display(self, root, level=0):

        if not root:
            return

        print(" " * 4 * level + "->" * level, "level", level, ":", root.val)

        self.display(root.left, level + 1)
        self.display(root.right, level + 1)


sol = Solution()

p = [1, 2, 3]
q = [1, 2, 3]
print(sol.isSameTree(p, q))

p = [1, 2]
q = [1, null, 2]
print(sol.isSameTree(p, q))

p = [1, 2, 1]
q = [1, 1, 2]
print(sol.isSameTree(p, q))

p = []
q = []
print(sol.isSameTree(p, q))
