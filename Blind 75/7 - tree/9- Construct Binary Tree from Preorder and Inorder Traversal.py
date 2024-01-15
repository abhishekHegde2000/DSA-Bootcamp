'''
105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.

'''
from typing import List, Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # If the preorder or inorder traversal is empty, return None
        if not preorder or not inorder:
            print("The preorder or inorder traversal is empty")
            return None

        # Create a new node with the first element of the preorder traversal as the root
        root_value = preorder[0]
        root = TreeNode(root_value)
        print(f"Created a new node with value {root_value} as the root")

        # Find the index of the root in the inorder traversal
        root_index_inorder = inorder.index(root_value)
        print(f"The index of the root in the inorder traversal is {
              root_index_inorder}")

        # Recursively build the left subtree with the elements before the root in the inorder traversal and the corresponding elements in the preorder traversal
        print("Building the left subtree")
        root.left = self.buildTree(
            preorder[1:root_index_inorder+1], inorder[:root_index_inorder])

        # Recursively build the right subtree with the elements after the root in the inorder traversal and the corresponding elements in the preorder traversal
        print("Building the right subtree")
        root.right = self.buildTree(
            preorder[root_index_inorder+1:], inorder[root_index_inorder+1:])

        # Return the root node
        return root


sol = Solution()
print(sol.buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]))
print(sol.buildTree(preorder=[-1], inorder=[-1]))
print(sol.buildTree(preorder=[1, 2], inorder=[1, 2]))
