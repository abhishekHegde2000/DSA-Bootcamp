from typing import Optional, List


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize an empty list to store the result
        ans = []

        # Helper function to perform preorder traversal
        def preorder(node):
            # Base case: if the node is None, return
            if node is None:
                return

            # Visit the root node
            ans.append(node.value)

            # Traverse the left subtree
            preorder(node.left)

            # Traverse the right subtree
            preorder(node.right)

        # Start the preorder traversal from the root
        preorder(root)

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

# Perform preorder traversal using the class method
result = solution.preorderTraversal(root)

# Print the result
print("Preorder traversal:", result)
