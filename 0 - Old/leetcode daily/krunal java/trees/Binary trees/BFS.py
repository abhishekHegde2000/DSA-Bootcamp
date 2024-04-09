
# import deque , optional list

from typing import Optional, List
from collections import deque


#  Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def Display(self, root, level=0, prefix="Root: "):
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.val))
            if root.left is not None or root.right is not None:
                self.Display(root.left, level + 1, "L--- ")
                self.Display(root.right, level + 1, "R--- ")

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        q = deque()
        q.append(root)

        while q:
            level_size = len(q)
            current_level = []
            for _ in range(level_size):
                node = q.popleft()
                if node:
                    current_level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    print("Node is None")

            if current_level:
                print(f"Current level: {current_level}")
                res.append(current_level)

        print(f"Result: {res}")
        return res


# Copy the provided code here

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

# Create an instance of the Solution class
solution = Solution()

# Run the level order traversal
result = solution.levelOrder(root)

# Print the result
print(result)
