'''
Shortest Path in Directed Acyclic Graph Topological Sort: G-27


72

1
Given a DAG, find the shortest path from the source to all other nodes in this DAG. In this problem statement, we have assumed the source vertex to be ‘0’. You will be given the weighted edges of the graph.

Note: What is a DAG ( Directed Acyclic Graph)?

A Directed Graph (containing one-sided edges) having no cycles is said to be a Directed Acyclic Graph.

Examples:

Example 1:





Input: n = 6, m= 7
edges =[[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]]


Output: 0 2 3 6 1 5


Explanation:  The above output list shows the shortest path
to all the nodes from the source vertex (0),


Dist[0] = 0


Dist[1] = 2


Dist[2] = 3


Dist[3] = 6


Dist[4] = 1


Dist[5] = 5


Example 2:




Input: n = 7, m= 8
Edges =[[0,4,2],[0,5,3],[5,4,1],[4,6,3],[4,2,1],[6,1,2],[2,3,3],[1,3,1]]


Output: 0 7 3 6 2 3 5


Explanation:


The above output list shows the shortest path to all the nodes
from the source vertex (0),


Dist[0] = 0


Dist[1] = 7


Dist[2] = 3


Dist[3] = 6


Dist[4] = 2


Dist[5] = 3


Dist[6] = 5


Solution

Disclaimer: Don’t jump directly to the solution, try it out yourself first.

Intuition:
Finding the shortest path to a vertex is easy if you already know the shortest paths to all the vertices that can precede it. Processing the vertices in topological order ensures that by the time you get to a vertex, you've already processed all the vertices that can precede it which reduces the computation time significantly. In this approach, we traverse the nodes sequentially according to their reachability from the source.

Dijkstra's algorithm is necessary for graphs that can contain cycles because they can't be topologically sorted. In other cases, the topological sort would work fine as we start from the first node, and then move on to the others in a directed manner.

Approach:
We will calculate the shortest path in a directed acyclic graph by using topological sort. Topological sort can be implemented in two ways- BFS and DFS. Here, we will be implementing using the DFS technique. Depth First Search, DFS is a traversal technique where we visit a node and then continue visiting its adjacent nodes until we reach the end point, i.e., it keeps on moving in the depth of a particular node and then backtracks when no further adjacent nodes are available.

Initial configuration:
Adjacency List: Create an adjacency list of the formed vector of pairs of size ‘N’, where each index denotes a node ‘u’ and contains a vector that consists of pairs denoting the adjacent nodes ‘v’ and the distance to that adjacent node from initial node ‘u’.
Visited Array: Create a visited array and mark all the indices as unvisited (0) initially.
Stack: Define a stack data structure to store the topological sort.
Distance Array: Initialise this array by Max integer value and then update the value for each node successively while calculating the shortest distance between the source and the current node.
The shortest path in a directed acyclic graph can be calculated by the following steps:

Perform topological sort on the graph using BFS/DFS and store it in a stack. In order to get a hang of how the Topological Sort works, you can refer to this article for the same.
Now, iterate on the topo sort. We can keep the generated topo sort in the stack only, and do an iteration on it, it reduces the extra space which would have been required to store it. Make sure for the source node, we will assign dist[src] = 0.
For every node that comes out of the stack which contains our topo sort, we can traverse for all its adjacent nodes, and relax them.
In order to relax them, we simply do a simple comparison of dist[node] + wt and dist[adjNode]. Here dist[node] means the distance taken to reach the current node, and it is the edge weight between the node and the adjNode.
If (dist[node] + wt < dist[adjNode]), then we will go ahead and update the distance of the dist[adjNode] to the new found better path.
Once all the nodes have been iterated, the dist[] array will store the shortest paths and we can then return it.
'''
from collections import deque


class Solution:
    def shortestPath(self, n, m, edges):
        # Code here
        adj = [[] for i in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
        vis = [0]*n
        stack = []

        def dfs(v):
            vis[v] = 1
            for u, w in adj[v]:
                if not vis[u]:
                    dfs(u)
            stack.append(v)
        for i in range(n):
            if not vis[i]:
                dfs(i)
        dist = [float('inf')]*n
        dist[0] = 0
        while stack:
            v = stack.pop()
            for u, w in adj[v]:
                if dist[v] + w < dist[u]:
                    dist[u] = dist[v] + w
        return dist

    def shortestPathBfs(self, n, m, edges):
        # Code here
        adj = [[] for i in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
        indegree = [0]*n
        for u, v, w in edges:
            indegree[v] += 1
        q = deque([0])
        dist = [float('inf')]*n
        dist[0] = 0
        while q:
            v = q.popleft()
            for u, w in adj[v]:
                if dist[v] + w < dist[u]:
                    dist[u] = dist[v] + w
                indegree[u] -= 1
                if indegree[u] == 0:
                    q.append(u)
        return dist


sol = Solution()


print(sol.shortestPath(6, 7, [[0, 1, 2], [0, 4, 1], [4, 5, 4], [
      4, 2, 2], [1, 2, 3], [2, 3, 6], [5, 3, 1]]))  # [0, 2, 3, 6, 1, 5]
print(sol.shortestPath(7, 8, [[0, 4, 2], [0, 5, 3], [5, 4, 1], [4, 6, 3], [
      4, 2, 1], [6, 1, 2], [2, 3, 3], [1, 3, 1]]))  # [0, 7, 3, 6, 2, 3, 5]
print(sol.shortestPath(6, 7, [[0, 1, 2], [0, 4, 1], [4, 5, 4], [
      4, 2, 2], [1, 2, 3], [2, 3, 6], [5, 3, 1]]))  # [0, 2, 3, 6, 1, 5]
