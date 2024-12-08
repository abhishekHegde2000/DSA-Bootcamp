'''
https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

Cycle in a Directed Graph
Difficulty: MediumAccuracy: 27.88%Submissions: 427K+Points: 4
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.
The graph is represented as an adjacency list, where adj[i] contains a list of vertices that are directly reachable from vertex i. Specifically, adj[i][j] represents an edge from vertex i to vertex j.

Example 1:

Input:



Output: 1
Explanation: 3 -> 3 is a cycle
Example 2:
Input:


Output: 0
Explanation: no cycle in the graph
'''
# User function Template for python3
from typing import List
from collections import deque


# class Solution:

#     # Function to detect cycle in a directed graph.
#     def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
#         # code here
#         in_degree = [0]*V

#         for i in range(V):
#             for neighbour in adj[i]:
#                 in_degree[neighbour] += 1

#         queue = deque([i for i in range(V) if in_degree[i] == 0])
#         cnt = 0

#         while queue:
#             node = queue.popleft()
#             cnt += 1
#             for neighbour in adj[node]:
#                 in_degree[neighbour] -= 1
#                 if in_degree[neighbour] == 0:
#                     queue.append(neighbour)
#         return cnt != V

# User function Template for python3
from typing import List


class Solution:

    # Function to detect cycle in a directed graph.
    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
        # code here
        vis = [0]*V
        pathvis = [0]*V

        def dfs(node, parent):
            vis[node] = 1
            pathvis[node] = 1
            for i in adj[node]:
                if vis[i] == 0:
                    if dfs(i, node) == True:
                        return True
                elif pathvis[i] == 1:
                    return True
            pathvis[node] = 0
        for i in range(V):
            if vis[i] == 0:
                if dfs(i, -1) == True:
                    return True
        return False


sol = Solution()

print(sol.isCyclic(4, [[1], [2], [3], [3]]))  # true
print(sol.isCyclic(3, [[1], [2], [0]]))  # true
print(sol.isCyclic(4, [[1], [2], [3], []]))  # false
