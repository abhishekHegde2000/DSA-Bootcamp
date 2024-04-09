'''
104. Maximum Depth of Binary Tree
Solved
Easy
Topics
Companies
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

'''
from collections import deque
from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        print(f"Finding the maximum depth of the tree with root value {
              root.val if root else 'None'}")

        # If the root is None, return 0
        if not root:
            print("The tree is empty")
            return 0

        # Find the maximum depth of the left subtree
        print(f"Finding the maximum depth of the left subtree of the node with value {
              root.val}")
        left_depth = self.maxDepth(root.left)

        # Find the maximum depth of the right subtree
        print(f"Finding the maximum depth of the right subtree of the node with value {
              root.val}")
        right_depth = self.maxDepth(root.right)

        # Return 1 plus the maximum of the depths of the left and right subtrees
        max_depth = 1 + max(left_depth, right_depth)
        print(f"The maximum depth of the tree with root value {
              root.val} is {max_depth}")
        return max_depth


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        print(f"Finding the maximum depth of the tree with root value {
              root.val if root else 'None'}")

        # If the root is None, return 0
        if not root:
            print("The tree is empty")
            return 0

        # Initialize a queue with the root node
        node_queue = deque([root])
        # Initialize level to 0
        level = 0

        while node_queue:
            print(f"Processing level {level} of the tree")

            # For each node in the current level
            for _ in range(len(node_queue)):
                # Remove the node from the queue
                current_node = node_queue.popleft()

                # Add the node's children to the queue
                if current_node.left:
                    node_queue.append(current_node.left)
                if current_node.right:
                    node_queue.append(current_node.right)

            # Increment level
            level += 1

        print(f"The maximum depth of the tree with root value {
              root.val} is {level}")
        return level

        def display_tree(self, root, level=0):

            if not root:
                return

            indent = "    " * level

            arrow = " --> " if level > 0 else ""

            print(f"{indent}{arrow}Level {level}: {root.val}")

            # print(f"Displaying the left subtree of the node with value {root.val}")

            self.display_tree(root.left, level + 1)
            # print(f"Displaying the right subtree of the node with value {root.val}")
            self.display_tree(root.right, level + 1)


sol = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.left = TreeNode(7)
print(sol.maxDepth(root))  # 3

root = TreeNode(1)
root.right = TreeNode(2)
print(sol.maxDepth(root))  # 2

root = None
print(sol.maxDepth(root))  # 0
