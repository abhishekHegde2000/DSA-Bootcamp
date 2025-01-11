'''
Given an adjacency list for a Directed Acyclic Graph (DAG) where adj[u] contains a list of all vertices v such that there exists a directed edge u -> v. Return topological sort for the given graph.

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u -> v, vertex u comes before v in the ordering.
Note: As there are multiple Topological orders possible, you may return any of them. If your returned Topological sort is correct then the output will be 1 else 0.

Examples:

Input: adj = [[], [0], [0], [0]]

Output: 1
Explanation: The output 1 denotes that the order is valid. Few valid Topological orders for the given graph are:
[3, 2, 1, 0]
[1, 2, 3, 0]
[2, 3, 1, 0]
Input: adj = [[], [3], [3], [], [0,1], [0,2]]

Output: 1
Explanation: The output 1 denotes that the order is valid. Few valid Topological orders for the graph are:
[4, 5, 0, 1, 2, 3]
[5, 2, 4, 0, 1, 3]
Constraints:
2  ≤  V  ≤  103
1  ≤  E  ≤  (V * (V - 1)) / 2


'''


from collections import deque


class Solution:

    # Function to return list containing vertices in Topological order.
    def dfs(self, v, adj, vis, ans):
        vis[v] = 1
        for child in adj[v]:
            if not vis[child]:
                self.dfs(child, adj, vis, ans)
        ans.append(v)

    def topologicalSort(self, adj):
        # Code here
        vis = [0]*len(adj)
        ans = []
        for i in range(len(adj)):
            if not vis[i]:
                self.dfs(i, adj, vis, ans)
        return list(reversed(ans))


class Solution:
    # Function to return list containing vertices in Topological order using BFS.
    def topologicalSort(self, adj):
        # Calculate the indegree of each vertex
        V = len(adj)
        indegree = [0] * V
        for i in range(V):
            for child in adj[i]:
                indegree[child] += 1

        # Initialize a queue with vertices having indegree 0
        q = deque([i for i in range(V) if indegree[i] == 0])
        ans = []

        # Perform BFS
        while q:
            node = q.popleft()
            ans.append(node)
            for child in adj[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)

        # If the length of the result is not equal to the number of vertices, it means there is a cycle and topological sort is not possible.
        if len(ans) != V:
            return []

        return ans


# Example usage:
adj = [
    [1, 2],  # Adjacency list for node 0
    [3],     # Adjacency list for node 1
    [3],     # Adjacency list for node 2
    [4, 5],  # Adjacency list for node 3
    [],      # Adjacency list for node 4
    [],      # Adjacency list for node 5
    []]      # Adjacency list for node 6

solution = Solution()
print(solution.topologicalSort(adj))  # Output: [0, 6, 1, 2, 3, 4, 5]
