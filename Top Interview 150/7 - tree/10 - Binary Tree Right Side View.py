'''
https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=leetcode-75

199. Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

'''

from collections import deque
from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize a queue with the root node
        nodeQueue = deque([root])
        # Initialize a result list
        rightView = []

        while nodeQueue:
            # Get the length of the queue
            levelLength = len(nodeQueue)
            # Initialize a variable to keep track of the rightmost node
            rightmostNode = None

            for i in range(levelLength):
                # Dequeue a node from the queue
                currentNode = nodeQueue.popleft()
                if currentNode:
                    # If the node is not null, update the rightmost node
                    rightmostNode = currentNode
                    print(f"Rightmost node at current level: {
                          rightmostNode.val}")
                    # Enqueue the left and right children of the node
                    nodeQueue.append(currentNode.left)
                    nodeQueue.append(currentNode.right)

            if rightmostNode:
                # If there is a rightmost node, add its value to the result list
                rightView.append(rightmostNode.val)

        print(f"Right view of the binary tree: {rightView}")
        return rightView


sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
sol.rightSideView(root)
