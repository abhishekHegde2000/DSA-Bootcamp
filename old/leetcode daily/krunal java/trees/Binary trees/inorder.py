from typing import Optional, List


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def inorder(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize an empty list to store the result
        ans = []

        # Helper function to perform inorder traversal
        def inorder_traversal(node):
            # Base case: if the node is None, return
            if node is None:
                return

            # Traverse the left subtree
            inorder_traversal(node.left)

            # Visit the root node
            ans.append(node.value)

            # Traverse the right subtree
            inorder_traversal(node.right)

        # Start the inorder traversal from the root
        inorder_traversal(root)

        # Return the final result
        return ans


# Example usage:
# Construct a simple binary tree
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Create an instance of the Solution class
solution = Solution()

# Perform inorder traversal using the class method
result = solution.inorder(root)

# Print the result
print("Inorder traversal:", result)
