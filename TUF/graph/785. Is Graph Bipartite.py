'''
https://leetcode.com/problems/is-graph-bipartite/


785. Is Graph Bipartite?
Solved
Medium
Topics
Companies
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.



Example 1:


Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
Example 2:


Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.


Constraints:

graph.length == n
1 <= n <= 100
0 <= graph[u].length < n
0 <= graph[u][i] <= n - 1
graph[u] does not contain u.
All the values of graph[u] are unique.
If graph[u] contains v, then graph[v] contains u.

'''

from typing import List
from collections import defaultdict, deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        partition = [0] * n

        def bfs(node):
            if partition[node]:
                # checking if this perticulra node already been visited ? then return ture as i dont have to visit again
                return True

            q = deque([node])
            partition[node] = -1

            while q:

                curr_node = q.popleft()

                for nei in graph[curr_node]:

                    if partition[nei] and partition[curr_node] == partition[nei]:
                        return False
                    elif not partition[nei]:
                        q.append(nei)
                        partition[nei] = -1 * partition[curr_node]
            return True

        for i in range(n):
            if not bfs(i):
                return False

        return True


sol = Solution()

print(sol.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))  # False
print(sol.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))  # True
print(sol.isBipartite([[1, 2, 3], [0], [0], [0]]))  # True
