'''
https://leetcode.com/problems/graph-valid-tree/
https://neetcode.io/problems/valid-tree

Valid Tree
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

Output:
true
Example 2:

Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

Output:
false
Note:

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2
'''

from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not n:
            return True
        visit = set()
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node, prev):
            if node in visit:
                return False

            visit.add(node)
            for i in adj[node]:
                if i == prev:
                    continue

                if not dfs(i, node):
                    return False

            return True

        return dfs(0, -1) and n == len(visit)


class Solution:
    def validTree(self, num_nodes: int, edges: List[List[int]]) -> bool:
        # If the number of nodes is 0, return True
        if not num_nodes:
            return True

        # Initialize a set to keep track of visited nodes
        visited_nodes = set()
        print(f"Initial visited nodes: {visited_nodes}")

        # Initialize a dictionary to keep track of the adjacency list of each node
        adjacency_list = {i: [] for i in range(num_nodes)}
        print(f"Initial adjacency list: {adjacency_list}")

        # For each edge, add the nodes to each other's adjacency list
        for node1, node2 in edges:
            adjacency_list[node1].append(node2)
            adjacency_list[node2].append(node1)
        print(f"Adjacency list after adding edges: {adjacency_list}")

        # Define a depth-first search (DFS) function that takes a node and its previous node as input
        def dfs(node, prev):
            # If the node has been visited, return False
            if node in visited_nodes:
                return False
            print(f"Node {node} not in visited nodes")

            # Add the node to the visited set
            visited_nodes.add(node)
            print(f"Visited nodes after adding node {node}: {visited_nodes}")

            # For each neighbor of the node, if the neighbor is not the previous node, call the DFS function on the neighbor. If the function returns False, return False
            for neighbor in adjacency_list[node]:
                if neighbor == prev:
                    continue
                print(f"Visiting neighbor {neighbor} of node {node}")
                if not dfs(neighbor, node):
                    return False
            print(f"All neighbors of node {node} visited")

            # Return True
            return True

        # If the DFS function on the first node returns False or the number of visited nodes is not equal to the number of nodes, return False
        if not dfs(0, -1) or num_nodes != len(visited_nodes):
            return False
        print(f"All nodes visited")

        # Return True
        return True


'''
# Pseudo Code

1. Check if the number of nodes is zero. If it is, return True as there are no nodes to form a cycle.
    ```python
    if not n:
        return True
    ```
2. Initialize a set to keep track of visited nodes.
    ```python
    visit = set()
    ```
3. Initialize a dictionary to keep track of the adjacency list of each node.
    ```python
    adj = {i: [] for i in range(n)}
    ```
4. For each edge, add the nodes to each other's adjacency list.
    ```python
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)
    ```
5. Define a depth-first search (DFS) function that takes a node and its previous node as input.
    ```python
    def dfs(node, prev):
    ```
6. If the node has been visited, return False.
    ```python
    if node in visit:
        return False
    ```
7. Add the node to the visited set.
    ```python
    visit.add(node)
    ```
8. For each neighbor of the node, if the neighbor is not the previous node, call the DFS function on the neighbor. If the function returns False, return False.
    ```python
    for i in adj[node]:
        if i == prev:
            continue
        if not dfs(i, node):
            return False
    ```
9. Return True.
    ```python
    return True
    ```
10. If the DFS function on the first node returns False or the number of visited nodes is not equal to the number of nodes, return False.
    ```python
    return dfs(0, -1) and n == len(visit)
    ```
11. Return True.
'''
