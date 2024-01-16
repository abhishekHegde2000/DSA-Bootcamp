'''
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/?envType=study-plan-v2&envId=top-interview-150


106. Construct Binary Tree from Inorder and Postorder Traversal

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
 

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Base case: if inorder is empty, return None
        if not inorder:
            print("Inorder list is empty. Returning None.")
            return None

        # The last element in postorder is the root of the current binary tree
        rootValue = postorder.pop()
        print(f"Creating new TreeNode with value {rootValue}")
        rootNode = TreeNode(rootValue)

        # Find the index of the root value in inorder
        rootIndex = inorder.index(rootValue)
        print(f"Index of root value in inorder: {rootIndex}")

        # Build right subtree with elements in inorder after the root value
        print("Building right subtree")
        rootNode.right = self.buildTree(inorder[rootIndex+1:], postorder)

        # Build left subtree with elements in inorder before the root value
        print("Building left subtree")
        rootNode.left = self.buildTree(inorder[:rootIndex], postorder)

        # Return the root node
        return rootNode
