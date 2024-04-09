'''
https://leetcode.com/problems/search-in-a-binary-search-tree/description/?envType=study-plan-v2&envId=leetcode-75

700. Search in a Binary Search Tree

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 

Example 1:


Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
Example 2:


Input: root = [4,2,7,1,3], val = 5
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107

'''

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.ans = None

        def dfs(node):
            if not node:
                return

            if node.val == val:
                self.ans = node
                return

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.ans


class Solution:
    def searchBST(self, root: Optional[TreeNode], target_value: int) -> Optional[TreeNode]:
        # Define a helper function to perform the search
        def find_node(current_node, target_value):
            # If the current node is None, return None
            if not current_node:
                return None
            # Print the current node value for debugging purposes
            print(f"Current node value: {current_node.val}")
            # If the current node's value is equal to the target value
            if current_node.val == target_value:
                # Return the current node
                return current_node
            # If the current node's value is less than the target value
            elif current_node.val < target_value:
                # Recursively search the right subtree
                return find_node(current_node.right, target_value)
            # If the current node's value is greater than the target value
            else:
                # Recursively search the left subtree
                return find_node(current_node.left, target_value)

        # Call the helper function on the root
        return find_node(root, target_value)
