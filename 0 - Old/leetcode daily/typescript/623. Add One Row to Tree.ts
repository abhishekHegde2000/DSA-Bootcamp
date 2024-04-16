/*
https://leetcode.com/problems/add-one-row-to-tree/?envType=daily-question&envId=2024-04-16https://leetcode.com/problems/add-one-row-to-tree/?envType=daily-question&envId=2024-04-16

623. Add One Row to Tree
Solved
Medium
Topics
Companies
Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
cur's original left subtree should be the left subtree of the new left subtree root.
cur's original right subtree should be the right subtree of the new right subtree root.
If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.
 

Example 1:


Input: root = [4,2,6,3,1,5], val = 1, depth = 2
Output: [4,1,1,2,null,null,6,3,1,5]
Example 2:


Input: root = [4,2,null,3,1], val = 1, depth = 3
Output: [4,2,null,1,1,3,null,null,1]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
The depth of the tree is in the range [1, 104].
-100 <= Node.val <= 100
-105 <= val <= 105
1 <= depth <= the depth of tree + 1

*/

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function addOneRow(
    root: TreeNode | null,
    val: number,
    depth: number
): TreeNode | null {
    function add(node: TreeNode | null, currDepth: number): TreeNode | null {
        if (node === null) {
            return null;
        }

        if (currDepth === depth - 1) {
            const newNodeLeft = new TreeNode(val);
            newNodeLeft.left = node.left;
            node.left = newNodeLeft;

            const newNodeRight = new TreeNode(val);
            newNodeRight.right = node.right;
            node.right = newNodeRight;

            return node;
        }

        node.left = add(node.left, currDepth + 1);
        node.right = add(node.right, currDepth + 1);

        return node;
    }

    if (depth === 1) {
        const newRoot = new TreeNode(val);
        newRoot.left = root;
        return newRoot;
    }

    return add(root, 1);
}

// BFS ----------------

function addOneRow(
    root: TreeNode | null,
    val: number,
    depth: number
): TreeNode | null {
    if (depth === 1) {
        // Create a new root with the given value and current root as its left child
        const newRoot = new TreeNode(val);
        newRoot.left = root;
        return newRoot;
    }

    let level = 1;
    const queue: TreeNode[] = [root];

    while (queue.length > 0) {
        if (level === depth - 1) break;

        const levelSize = queue.length;
        for (let i = 0; i < levelSize; i++) {
            const current = queue.shift()!;
            if (current.left) queue.push(current.left);
            if (current.right) queue.push(current.right);
        }
        level++;
    }

    for (const node of queue) {
        const leftChild = node.left;
        const rightChild = node.right;

        node.left = new TreeNode(val);
        node.left.left = leftChild;

        node.right = new TreeNode(val);
        node.right.right = rightChild;
    }

    return root;
}
