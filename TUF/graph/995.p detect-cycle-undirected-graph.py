'''

https://www.geeksforgeeks.org/detect-cycle-undirected-graph/





'''

from typing import List


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

        # for bfs
        def bfs(node, visited):
            queue = [(node, -1)]

            while queue:
                node, parent = queue.pop(0)
                visited[node] = True

                for nb in adj[node]:
                    if not visited[nb]:
                        queue.append((nb, node))
                    elif nb != parent:
                        return True

            return False
        # for i in range(V):
        #     if not visited[i]:
        #         if bfs(i, visited):
        #             return True
        # return False

        return False


sol = Solution()

print(sol.isCycle(4, [[1, 2], [0, 2], [0, 1, 3], [2]]))  # True
print(sol.isCycle(4, [[1, 3], [0, 2], [1, 3], [0, 2]]))  # False
print(sol.isCycle(4, [[1, 2], [0, 2, 3], [0, 1, 3], [1, 2]]))  # True
print(sol.isCycle(4, [[1, 2], [0, 2, 3], [0, 1, 3], [1, 2]]))  # True
