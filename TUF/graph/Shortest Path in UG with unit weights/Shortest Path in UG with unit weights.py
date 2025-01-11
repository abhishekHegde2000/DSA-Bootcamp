'''
Shortest Path in Undirected Graph with unit distance: G-28


82

3
Given an Undirected Graph having unit weight, find the shortest path from the source to all other nodes in this graph. In this problem statement, we have assumed the source vertex to be ‘0’. If a vertex is unreachable from the source node, then return -1 for that vertex.

Example 1:



Input:
n = 9, m = 10
edges = [[0,1],[0,3],[3,4],[4 ,5],[5, 6],[1,2],[2,6],[6,7],[7,8],[6,8]]
src=0

Output: 0 1 2 1 2 3 3 4 4

Explanation:
The above output array shows the shortest path to all
the nodes from the source vertex (0), Dist[0] = 0,
Dist[1] = 1 , Dist[2] = 2 , …. Dist[8] = 4
Where Dist[node] is the shortest path between src and
the node. For a node, if the value of Dist[node]= -1,
then we conclude that the node is unreachable from
the src node.
Example 2:



Input:
n = 8, m = 10
Edges =[[1,0],[2,1],[0,3],[3,7],[3,4],[7,4],[7,6],[4,5],[4,6],[6,5]]
src=0

Output: 0 1 2 1 2 3 3 2

Explanation:
The above output list shows the shortest path to all the
nodes from the source vertex (0),  Dist[0] = 0,
Dist[1] = 1, Dist[2] = 2,.....Dist[7] = 2
'''

from collections import deque


class Solution:

    def shortestPath(self, n, m, edges, src):
        # Code here
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dist = [-1]*n
        dist[src] = 0
        q = deque([src])
        while q:
            node = q.popleft()
            for child in adj[node]:
                if dist[child] == -1:
                    dist[child] = dist[node] + 1
                    q.append(child)
        return dist

    def shortestPathDfs(self, n, m, edges, src):
        # Code here
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dist = [-1]*n
        dist[src] = 0
        self.dfs(src, adj, dist)
        return dist

    def dfs(self, v, adj, dist):
        for child in adj[v]:
            if dist[child] == -1:
                dist[child] = dist[v] + 1
                self.dfs(child, adj, dist)
