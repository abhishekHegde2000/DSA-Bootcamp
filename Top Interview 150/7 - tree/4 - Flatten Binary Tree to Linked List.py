'''
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/?envType=study-plan-v2&envId=top-interview-150

114. Flatten Binary Tree to Linked List
Medium
Topics
Companies
Hint
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
 

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
'''

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(node):
            if not node:
                print("Node is None. Returning None.")
                return None

            print(f"Flattening left subtree of node {node.val}")
            leftSubtreeTail = dfs(node.left)
            print(f"Flattening right subtree of node {node.val}")
            rightSubtreeTail = dfs(node.right)

            if node.left:
                print(
                    f"Appending flattened right subtree to tail of flattened left subtree")
                leftSubtreeTail.right = node.right
                print(f"Appending flattened left subtree to node {node.val}")
                node.right = node.left
                node.left = None

            print(
                f"Returning tail of flattened tree rooted at node {node.val}")
            return rightSubtreeTail or leftSubtreeTail or node

        print("Starting to flatten the tree")
        dfs(root)


sol = Solution()
# Example 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(5)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.right = TreeNode(6)

sol = Solution()
sol.flatten(root1)

# The flattened tree should look like: [1, null, 2, null, 3, null, 4, null, 5, null, 6]
