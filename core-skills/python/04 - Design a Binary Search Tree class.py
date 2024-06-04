"""
https://github.com/kuroxx/dsa/blob/43ee631f61b4100c88d198f30919444373b33cb6/python3/0-data_structure/implementations/binary_search_tree.py#L4

Design a Binary Search Tree class.

The TreeMap class represents a Binary Search Tree (BST) and should provide the following functionalities:

1. Insert a key-value pair into the tree.
   - If the key already exists, update its value.
   - Ensure that the tree remains ordered by keys.
   - Duplicate keys are not allowed.

2. Retrieve the value associated with a given key.
   - If the key is not found, return -1.

3. Get the minimum value stored in the tree.
   - Return -1 if the tree is empty.

4. Get the maximum value stored in the tree.
   - Return -1 if the tree is empty.

5. Remove a key from the tree.
   - Ensure the tree remains a valid BST after removal.
   - Handle cases where the key is not present gracefully.

6. Get an inorder traversal of the tree's keys.
   - Return the keys in ascending order.

The TreeNode class represents a node in the tree and should have attributes for the key, value, left child, and right child.

Implement the TreeMap class and write unit tests to verify its functionality using the provided example inputs and expected outputs.

Example 1:
Input: 
["insert", 1, 2, "get", 1, "insert", 4, 0, "getMin", "getMax"]
Output: 
[null, 2, null, 2, 0]

Example 2:
Input: 
["insert", 1, 2, "insert", 4, 2, "insert", 3, 7, "insert", 2, 1, "getInorderKeys", "remove", 1, "getInorderKeys"]
Output: 
[null, null, null, null, [1, 2, 3, 4], null, [2, 3, 4]]
"""

from typing import List


class TreeNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.right_child = None
        self.left_child = None


class TreeMap:
    def __init__(self):
        self.root_node = None

    def insert(self, key: int, value: int) -> None:
        new_node = TreeNode(key, value)
        if not self.root_node:
            self.root_node = new_node
            print(f"Inserted root node with key {key} and value {value}")
            return

        current_node = self.root_node
        while True:
            if key > current_node.key:
                if not current_node.right_child:
                    current_node.right_child = new_node
                    print(f"Inserted node with key {key} and value {
                          value} to the right of node with key {current_node.key}")
                    return
                current_node = current_node.right_child
            elif key < current_node.key:
                if not current_node.left_child:
                    current_node.left_child = new_node
                    print(f"Inserted node with key {key} and value {
                          value} to the left of node with key {current_node.key}")
                    return
                current_node = current_node.left_child
            else:
                current_node.value = value
                print(f"Updated node with key {key} to new value {value}")
                return

    def get(self, key: int) -> int:
        current_node = self.root_node
        while current_node:
            if key < current_node.key:
                current_node = current_node.left_child
            elif key > current_node.key:
                current_node = current_node.right_child
            else:
                print(f"Found node with key {
                      key} and value {current_node.value}")
                return current_node.value
        print(f"Node with key {key} not found")
        return -1

    def getMin(self) -> int:
        current_node = self.findMin(self.root_node)
        return current_node.value if current_node else -1

    def findMin(self, node) -> TreeNode:
        while node and node.left_child:
            node = node.left_child
        return node

    def getMax(self) -> int:
        current_node = self.root_node
        while current_node and current_node.right_child:
            current_node = current_node.right_child
        return current_node.value if current_node else -1

    def remove(self, key: int) -> None:
        self.root_node = self.removeHelper(self.root_node, key)

    def removeHelper(self, current_node, key) -> TreeNode:
        if current_node == None:
            return None

        if key > current_node.key:
            current_node.right_child = self.removeHelper(
                current_node.right_child, key)
        elif key < current_node.key:
            current_node.left_child = self.removeHelper(
                current_node.left_child, key)
        else:
            if current_node.left_child == None:
                return current_node.right_child
            elif current_node.right_child == None:
                return current_node.left_child
            else:
                min_node = self.findMin(current_node.right_child)
                current_node.key = min_node.key
                current_node.value = min_node.value
                current_node.right_child = self.removeHelper(
                    current_node.right_child, min_node.key)
        return current_node

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root_node, result)
        return result

    def inorderTraversal(self, root_node: TreeNode, result: List[int]) -> None:
        if root_node != None:
            self.inorderTraversal(root_node.left_child, result)
            result.append(root_node.key)
            self.inorderTraversal(root_node.right_child, result)


sol = TreeMap()

# Example 1
sol.insert(1, 2)
sol.get(1)
sol.insert(4, 0)
sol.getMin()
sol.getMax()
