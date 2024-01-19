'''
https://leetcode.com/problems/leaf-similar-trees/description/?envType=study-plan-v2&envId=leetcode-75

872. Leaf-Similar Trees

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
 

Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].
'''

from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def getLeaves(currentNode, leafList):
            if not currentNode:
                print("Reached a leaf node, returning.")
                return

            if not currentNode.left and not currentNode.right:
                print(f"Node {currentNode.val} is a leaf node.")
                leafList.append(currentNode.val)

            getLeaves(currentNode.left, leafList)
            getLeaves(currentNode.right, leafList)

        leafList1 = []
        leafList2 = []

        print("Starting to collect the leaf nodes from the first tree")
        getLeaves(root1, leafList1)
        print("Starting to collect the leaf nodes from the second tree")
        getLeaves(root2, leafList2)

        print(f"Leaf nodes from the first tree: {leafList1}")
        print(f"Leaf nodes from the second tree: {leafList2}")

        areLeafSimilar = leafList1 == leafList2
        print(f"Are the two trees leaf-similar? {areLeafSimilar}")

        return areLeafSimilar
