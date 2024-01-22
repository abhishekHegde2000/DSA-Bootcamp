'''
https://leetcode.com/problems/delete-node-in-a-bst/description/?envType=study-plan-v2&envId=leetcode-75

450. Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105
 

Follow up: Could you solve it with time complexity O(height of tree)?
'''
from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Function to delete a node from a BST
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # If the root is None, return None
        if not root:
            return None

        # If the key is greater than the root's value, delete the node from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # If the key is less than the root's value, delete the node from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # If the root has no children, delete the root
            if not root.left and not root.right:
                root = None
            # If the root has a right child, replace the root's value with its successor's value and delete the successor
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # If the root has only a left child, replace the root's value with its predecessor's value and delete the predecessor
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        # Return the root
        return root

    # Function to find the successor of a node
    def successor(self, root: TreeNode) -> TreeNode:
        # The successor is the smallest node in the right subtree
        root = root.right
        while root.left:
            root = root.left
        return root.val

    # Function to find the predecessor of a node
    def predecessor(self, root: TreeNode) -> TreeNode:
        # The predecessor is the largest node in the left subtree
        root = root.left
        while root.right:
            root = root.right
        return root.val


sol = Solution()

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)
sol.deleteNode(root, 3)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)
sol.deleteNode(root, 0)
