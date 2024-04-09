'''
https://leetcode.com/problems/sum-root-to-leaf-numbers/description/?envType=study-plan-v2&envId=top-interview-150

129. Sum Root to Leaf Numbers
Solved
Medium
Topics
Companies
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

 

Example 1:


Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:


Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 9
The depth of the tree will not exceed 10.

'''
from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, num):
            if not node:
                print("Node is None. Returning 0.")
                return 0

            num = num * 10 + node.val
            print(f"Formed number {num} by appending node {
                  node.val} value to number formed so far")

            if not node.left and not node.right:
                print(f"Node {node.val} is a leaf. Returning number {
                      num} formed so far")
                return num

            print(f"Calculating sum of numbers formed in the left subtree and the right subtree of node {
                  node.val}")
            return dfs(node.left, num) + dfs(node.right, num)

        print("Starting to calculate the total sum of all root-to-leaf numbers")
        return dfs(root, 0)


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, num_str):
            if not node:
                return

            num_str += str(node.val)

            if not node.left and not node.right:
                result.append(int(num_str))
                return

            dfs(node.left, num_str)
            dfs(node.right, num_str)

        result = []
        dfs(root, "")
        return sum(result)


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [""]

            left_nums = dfs(node.left)
            right_nums = dfs(node.right)

            return [str(node.val) + num for num in left_nums + right_nums if num or node.left or node.right]

        return sum(int(num) for num in dfs(root))
