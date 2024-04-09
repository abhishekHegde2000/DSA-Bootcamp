'''

https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75


1448. Count Good Nodes in Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 

Example 1:



Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:



Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
 

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].
'''

from typing import Optional, List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(currentNode, maxValSoFar):
            if not currentNode:
                print("Reached a leaf node, returning 0.")
                return 0

            goodNodeCount = 1 if currentNode.val >= maxValSoFar else 0
            if goodNodeCount:
                print(f"Node {currentNode.val} is a good node.")
            maxValSoFar = max(maxValSoFar, currentNode.val)

            goodNodeCount += dfs(currentNode.left, maxValSoFar)
            goodNodeCount += dfs(currentNode.right, maxValSoFar)
            return goodNodeCount

        print("Starting to count the number of good nodes in the tree")
        totalGoodNodes = dfs(root, root.val)
        print(f"Total number of good nodes in the tree is {totalGoodNodes}")
        return totalGoodNodes


sol = Solution()
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)
sol.goodNodes(root)
