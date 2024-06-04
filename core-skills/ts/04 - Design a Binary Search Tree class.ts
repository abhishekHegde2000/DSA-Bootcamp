/*
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
*/

class TreeNode {
    key: number;
    value: number;
    rightChild: TreeNode | null;
    leftChild: TreeNode | null;

    constructor(key: number, value: number) {
        this.key = key;
        this.value = value;
        this.rightChild = null;
        this.leftChild = null;
    }
}

class TreeMap {
    rootNode: TreeNode | null;

    constructor() {
        this.rootNode = null;
    }

    insert(key: number, value: number): void {
        let newNode = new TreeNode(key, value);
        if (!this.rootNode) {
            this.rootNode = newNode;
            console.log(
                `Inserted root node with key ${key} and value ${value}`
            );
            return;
        }

        let currentNode = this.rootNode;
        while (true) {
            if (key > currentNode.key) {
                if (!currentNode.rightChild) {
                    currentNode.rightChild = newNode;
                    console.log(
                        `Inserted node with key ${key} and value ${value} to the right of node with key ${currentNode.key}`
                    );
                    return;
                }
                currentNode = currentNode.rightChild;
            } else if (key < currentNode.key) {
                if (!currentNode.leftChild) {
                    currentNode.leftChild = newNode;
                    console.log(
                        `Inserted node with key ${key} and value ${value} to the left of node with key ${currentNode.key}`
                    );
                    return;
                }
                currentNode = currentNode.leftChild;
            } else {
                currentNode.value = value;
                console.log(
                    `Updated node with key ${key} to new value ${value}`
                );
                return;
            }
        }
    }

    get(key: number): number {
        let currentNode = this.rootNode;
        while (currentNode) {
            if (key < currentNode.key) {
                currentNode = currentNode.leftChild;
            } else if (key > currentNode.key) {
                currentNode = currentNode.rightChild;
            } else {
                console.log(
                    `Found node with key ${key} and value ${currentNode.value}`
                );
                return currentNode.value;
            }
        }
        console.log(`Node with key ${key} not found`);
        return -1;
    }

    getMin(): number {
        let currentNode = this.findMin(this.rootNode);
        return currentNode ? currentNode.value : -1;
    }

    findMin(node: TreeNode | null): TreeNode | null {
        while (node && node.leftChild) {
            node = node.leftChild;
        }
        return node;
    }

    getMax(): number {
        let currentNode = this.rootNode;
        while (currentNode && currentNode.rightChild) {
            currentNode = currentNode.rightChild;
        }
        return currentNode ? currentNode.value : -1;
    }

    remove(key: number): void {
        this.rootNode = this.removeHelper(this.rootNode, key);
    }

    removeHelper(currentNode: TreeNode | null, key: number): TreeNode | null {
        if (!currentNode) {
            return null;
        }

        if (key > currentNode.key) {
            currentNode.rightChild = this.removeHelper(
                currentNode.rightChild,
                key
            );
        } else if (key < currentNode.key) {
            currentNode.leftChild = this.removeHelper(
                currentNode.leftChild,
                key
            );
        } else {
            if (!currentNode.leftChild) {
                return currentNode.rightChild;
            } else if (!currentNode.rightChild) {
                return currentNode.leftChild;
            } else {
                let minNode = this.findMin(currentNode.rightChild);
                if (minNode) {
                    currentNode.key = minNode.key;
                    currentNode.value = minNode.value;
                    currentNode.rightChild = this.removeHelper(
                        currentNode.rightChild,
                        minNode.key
                    );
                }
            }
        }
        return currentNode;
    }

    getInorderKeys(): number[] {
        let result: number[] = [];
        this.inorderTraversal(this.rootNode, result);
        return result;
    }

    inorderTraversal(rootNode: TreeNode | null, result: number[]): void {
        if (rootNode) {
            this.inorderTraversal(rootNode.leftChild, result);
            result.push(rootNode.key);
            this.inorderTraversal(rootNode.rightChild, result);
        }
    }
}
