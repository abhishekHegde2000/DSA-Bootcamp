'''
https://www.geeksforgeeks.org/problems/topological-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=topological-sort


Topological sort
Difficulty: MediumAccuracy: 56.52%Submissions: 245K+Points: 4
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

Seen this question in a real interview before ?
Yes
No
Company Tags
Moonfrog LabsFlipkartMorgan StanleyAccoliteAmazonMicrosoftOYO RoomsSamsungD-E-ShawVisa
Topic Tags
GraphData Structures
Related Interview Experiences
De Shaw Interview Experience Off Campus 3
Expected Complexities
Time Complexity: O(V + E)Auxiliary Space: O(V)

'''


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

    def bfs(self, adj, vis, ans, q):
        while q:
            node = q.pop(0)
            ans.append(node)
            for child in adj[node]:
                vis[child] -= 1
                if vis[child] == 0:
                    q.append(child)

    def topologicalSortBFS(self, adj):

        vis = [0]*len(adj)
        for i in range(len(adj)):
            for child in adj[i]:
                vis[child] += 1
        q = []
        for i in range(len(adj)):
            if vis[i] == 0:
                q.append(i)
        ans = []
        self.bfs(adj, vis, ans, q)
        return ans
