from typing import Optional, List


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def displayTree(self, root: Optional[TreeNode], level=0, prefix="Root: ") -> None:

        if root is not None:
            print(" " * (level * 4) + prefix + str(root.value))
            if root.left is not None or root.right is not None:
                self.displayTree(root.left, level + 1, "L--- ")
                self.displayTree(root.right, level + 1, "R--- ")

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize an empty list to store the result
        ans = []

        # Helper function to perform postorder traversal
        def postorder(node):
            # Base case: if the node is None, return
            if node is None:
                return

            # Traverse the left subtree
            postorder(node.left)

            # Traverse the right subtree
            postorder(node.right)

            # Visit the root node
            ans.append(node.value)

        # Start the postorder traversal from the root
        postorder(root)

        # Return the final result
        return ans


# Example usage:
# Construct a simple binary tree
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
# Assuming None for missing nodes in this example
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Create an instance of the Solution class
solution = Solution()

# Display the binary tree structure
solution.displayTree(root)

# Perform postorder traversal using the class method
result = solution.postorderTraversal(root)

# Print the result
print("Postorder traversal:", result)
