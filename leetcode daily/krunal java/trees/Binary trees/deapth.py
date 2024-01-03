from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def Display(self, root, level=0, prefix="Root: "):

        if root:
            print(" " * (level * 4) + prefix + str(root.val))
            if root.left or root.right:
                self.Display(root.left, level + 1, "L--- ")
                self.Display(root.right, level + 1, "R--- ")

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: if the root is None, the depth is 0
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)

# Create a binary tree

# Example:
#    3
#   / \
#  9  20
#     / \
#    15  7


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
print(sol.maxDepth(root))
