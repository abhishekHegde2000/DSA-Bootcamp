'''
https://leetcode.com/problems/clone-graph/description/

133. Clone Graph

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
 

Constraints:

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.

'''


# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        oldToNew = {}

        def dfs(node):

            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy

            for nb in node.neighbors:
                copy.neighbors.append(dfs(nb))
            return copy

        return dfs(node) if node else None


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Initialize a dictionary to map old nodes to new nodes
        old_to_new = {}

        # Define a depth-first search (DFS) function that takes a node as input
        def dfs(old_node):
            # If the node is already in the dictionary, return its corresponding new node
            if old_node in old_to_new:
                return old_to_new[old_node]
            print(f"Old node {old_node.val} not in old_to_new")

            # Create a new node with the same value as the input node and add it to the dictionary
            new_node = Node(old_node.val)
            old_to_new[old_node] = new_node
            print(f"Created new node {
                  new_node.val} for old node {old_node.val}")

            # Iterate over the neighbors of the input node
            for neighbor in old_node.neighbors:
                # For each neighbor, call the DFS function on it and append the returned new node to the neighbors of the new node
                new_node.neighbors.append(dfs(neighbor))
                print(f"Added new node {
                      dfs(neighbor).val} to neighbors of new node {new_node.val}")

            # Return the new node
            return new_node

        # Call the DFS function on the input node and return the returned new node. If the input node is None, return None
        return dfs(node) if node else None


sol = Solution()

# [[2,4],[1,3],[2,4],[1,3]]
print(sol.cloneGraph([[2, 4], [1, 3], [2, 4], [1, 3]]))
print(sol.cloneGraph([[]]))  # [[]]
print(sol.cloneGraph([]))  # []
