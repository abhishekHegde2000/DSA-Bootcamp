'''
https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph


2192. All Ancestors of a Node in a Directed Acyclic Graph

You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).

You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.

Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.

A node u is an ancestor of another node v if u can reach v via a set of edges.

 

Example 1:


Input: n = 8, edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
Output: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
Explanation:
The above diagram represents the input graph.
- Nodes 0, 1, and 2 do not have any ancestors.
- Node 3 has two ancestors 0 and 1.
- Node 4 has two ancestors 0 and 2.
- Node 5 has three ancestors 0, 1, and 3.
- Node 6 has five ancestors 0, 1, 2, 3, and 4.
- Node 7 has four ancestors 0, 1, 2, and 3.
Example 2:


Input: n = 5, edgeList = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Output: [[],[0],[0,1],[0,1,2],[0,1,2,3]]
Explanation:
The above diagram represents the input graph.
- Node 0 does not have any ancestor.
- Node 1 has one ancestor 0.
- Node 2 has two ancestors 0 and 1.
- Node 3 has three ancestors 0, 1, and 2.
- Node 4 has four ancestors 0, 1, 2, and 3.
 

Constraints:

1 <= n <= 1000
0 <= edges.length <= min(2000, n * (n - 1) / 2)
edges[i].length == 2
0 <= fromi, toi <= n - 1
fromi != toi
There are no duplicate edges.
The graph is directed and acyclic.

'''


from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # 1. Initialize adjacency list (reversed edges)
        graph = [[] for _ in range(n)]
        print("Initialized graph:", graph)  # Print the initial empty graph

        # 2. Populate adjacency list with reversed edges
        for edge in edges:
            from_node, to_node = edge
            graph[to_node].append(from_node)
        print("Populated graph:", graph)  # Print the populated graph

        ancestors_list = []

        # 3. For each node, find ancestors (children in reversed graph)
        for i in range(n):
            current_ancestors = []
            visited = set()
            # Print the node being processed
            print("Finding ancestors for node:", i)

            # 4. DFS to find children (ancestors in reversed graph)
            self.find_children(i, graph, visited)

            # 5. Add visited nodes (ancestors) to current node's list
            for node in range(n):
                if node == i:
                    continue
                if node in visited:
                    current_ancestors.append(node)
            print("Ancestors found for node", i, ":",
                  current_ancestors)  # Print ancestors
            ancestors_list.append(current_ancestors)

        return ancestors_list

    def find_children(self, current_node, graph, visited_nodes):
        # 1. Mark current node as visited
        visited_nodes.add(current_node)

        # 2. Recursively traverse neighbors (children in reversed graph)
        for neighbour in graph[current_node]:
            if neighbour not in visited_nodes:
                # Print neighbor being visited
                print("Visiting neighbor:", neighbour)
                self.find_children(neighbour, graph, visited_nodes)


sol = Solution()

print(sol.getAncestors(8, [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [
      # [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
      3, 6], [3, 7], [4, 6]]))
print(sol.getAncestors(5, [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [
      1, 4], [2, 3], [2, 4], [3, 4]]))  # [[],[0],[0,1],[0,1,2],[0,1,2,3]]
