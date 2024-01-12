'''
226. Invert Binary Tree
Solved
Easy
Topics
Companies
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

'''
# Definition for a binary tree node.

from typing import Optional, List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        print(f"Inverting the tree with root value {
              root.val if root else 'None'}")

        # If the root is None, return None
        if not root:
            print("The tree is empty")
            return None

        # Swap the left and right children of the root
        temp_node = root.left
        root.left = root.right
        root.right = temp_node
        print(f"Swapped the children of the node with value {root.val}")

        # Recursively invert the left and right subtrees
        print(f"Inverting the left subtree of the node with value {root.val}")
        self.invertTree(root.left)
        print(f"Inverting the right subtree of the node with value {root.val}")
        self.invertTree(root.right)

        # Return the root
        print(
            f"Returning the root of the inverted tree with root value {root.val}")
        return root

    def display_tree(self, root: Optional[TreeNode], level=0):
        # If the node is None, return
        if not root:
            return

        # Create an indentation string based on the level
        indent = "    " * level

        # Add an arrow for all levels except the root
        arrow = " --> " if level > 0 else ""

        # Print the current node
        print(f"{indent}{arrow}Level {level}: {root.val}")

        # Recursively display the left and right subtrees
        print(f"Displaying the left subtree of the node with value {root.val}")
        self.display_tree(root.left, level + 1)
        print(
            f"Displaying the right subtree of the node with value {root.val}")
        self.display_tree(root.right, level + 1)


sol = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print("Original Tree:")
sol.display_tree(root)

sol.invertTree(root)

print("Inverted Tree:")
sol.display_tree(root)
