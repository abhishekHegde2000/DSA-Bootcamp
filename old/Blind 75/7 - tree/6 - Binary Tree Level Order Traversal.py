'''
102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

'''

from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Initialize an empty list to store the level order traversal
        result = []

        # Initialize a queue with the root node
        queue = deque([root])

        print(f"Queue has been created with root {
              root.val if root else 'None'}")

        # While the queue is not empty
        while queue:
            # Get the number of nodes at the current level
            current_level_size = len(queue)

            # Initialize an empty list to store the nodes at the current level
            current_level = []

            print(f"Processing {
                  current_level_size} nodes at the current level")

            # For each node at the current level
            for _ in range(current_level_size):
                # Remove the node from the queue
                node = queue.popleft()

                print(f"Popped node = {
                      node.val if node else 'No node present in queue as of now'}")

                # If the node is not None
                if node:
                    # Add its value to current_level
                    current_level.append(node.val)

                    # Add its left and right children to the queue
                    queue.append(node.left)
                    queue.append(node.right)

            # If current_level is not empty, add it to result
            if current_level:
                result.append(current_level)

        return result


sol = Solution()
print(sol.levelOrder(root=[3, 9, 20, None, None, 15, 7]))
