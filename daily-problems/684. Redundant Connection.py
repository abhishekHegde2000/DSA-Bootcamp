'''

https://leetcode.com/problems/redundant-connection/description/

684. Redundant Connection

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.

'''


from typing import List


class Solution:
    def findRedundantConnection(self, edges):
        # Initialize parent and rank arrays
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        print(f"Initial parent: {parent} and rank: {rank}")

        # Function to find the root parent of a node
        def find(node):
            root = parent[node]
            while root != parent[root]:
                root = parent[root]
            print(f"Find root of {node}: {root}")
            return root

        # Function to merge two subsets; returns False if they are already merged
        def union(node1, node2):
            root1, root2 = find(node1), find(node2)

            if root1 == root2:
                print(f"Nodes {node1} and {node2} have the same root {
                      root1}. Edge [{node1}, {node2}] is redundant.")
                return False
            if rank[root1] > rank[root2]:
                parent[root2] = root1
                rank[root1] += rank[root2]
            else:
                parent[root1] = root2
                rank[root2] += rank[root1]
            print(f"After union of {node1} and {
                  node2}: parent: {parent}, rank: {rank}")
            return True

        # Iterate through edges to find the redundant connection
        for start, end in edges:
            if not union(start, end):
                return [start, end]

        return []


sol = Solution()

print(sol.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))  # [2, 3]
print(sol.findRedundantConnection(
    [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))  # [1, 4]
