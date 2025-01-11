'''

https://www.geeksforgeeks.org/detect-cycle-undirected-graph/





'''


from typing import List
from collections import deque


class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:

        def dfs(node, parent, visited):
            visited[node] = True

            for nb in adj[node]:
                if not visited[nb]:
                    if dfs(nb, node, visited):
                        return True
                elif nb != parent:
                    return True

            return False

        visited = [False] * V

        for i in range(V):
            if not visited[i]:
                if dfs(i, -1, visited):
                    return True

        return False


class Solution:
    # Function to detect cycle in an undirected graph using BFS.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:

        def bfs(start):
            queue = deque([(start, -1)])
            visited[start] = True

            while queue:
                node, parent = queue.popleft()

                for nb in adj[node]:
                    if not visited[nb]:
                        visited[nb] = True
                        queue.append((nb, node))
                    elif nb != parent:
                        return True

            return False

        visited = [False] * V

        for i in range(V):
            if not visited[i]:
                if bfs(i):
                    return True

        return False


sol = Solution()

print(sol.isCycle(4, [[1, 2], [0, 2], [0, 1, 3], [2]]))  # True
print(sol.isCycle(4, [[1, 3], [0, 2], [1, 3], [0, 2]]))  # False
print(sol.isCycle(4, [[1, 2], [0, 2, 3], [0, 1, 3], [1, 2]]))  # True
print(sol.isCycle(4, [[1, 2], [0, 2, 3], [0, 1, 3], [1, 2]]))  # True
