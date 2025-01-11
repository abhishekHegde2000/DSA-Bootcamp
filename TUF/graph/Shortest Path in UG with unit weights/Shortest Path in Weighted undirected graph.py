'''

https://www.geeksforgeeks.org/problems/shortest-path-in-weighted-undirected-graph/1


Shortest Path in Weighted undirected graph
Difficulty: MediumAccuracy: 50.0%Submissions: 66K+Points: 4
You are given a weighted undirected graph having n vertices numbered from 1 to n and m edges along with their weights. Find the shortest weight path between the vertex 1 and the vertex n,  if there exists a path, and return a list of integers whose first element is the weight of the path, and the rest consist of the nodes on that path. If no path exists, then return a list containing a single element -1.

The input list of edges is as follows - {a, b, w}, denoting there is an edge between a and b, and w is the weight of that edge.

Note: The driver code here will first check if the weight of the path returned is equal to the sum of the weights along the nodes on that path, if equal it will output the weight of the path, else -2. In case the list contains only a single element (-1) it will simply output -1.

Examples :

Input: n = 5, m= 6, edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
Output: 5
Explanation: Shortest path from 1 to n is by the path 1 4 3 5 whose weight is 5.
Input: n = 2, m= 1, edges = [[1, 2, 2]]
Output: 2
Explanation: Shortest path from 1 to 2 is by the path 1 2 whose weight is 2.
Input: n = 2, m= 0, edges = [ ]
Output: -1
Explanation: Since there are no edges, so no answer is possible.
Expected Time Complexity: O(m* log(n))
Expected Space Complexity: O(n+m)

Constraint:
2 <= n <= 106
0 <= m <= 106
1 <= a, b <= n
1 <= w <= 105

'''


from typing import List
import heapq


from typing import List
import heapq


class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        # Step 1: Create the graph as an adjacency list
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # graph1 = {}

        # for edge in edges:
        #     u, v, w = edge
        #     if u not in graph1:
        #         graph1[u] = {}
        #     if v not in graph1:
        #         graph1[v] = {}

        #     graph1[u][v] = w
        #     graph1[v][u] = w

        # Step 2: Initialize Dijkstra's algorithm
        min_heap = [(0, 1)]  # (distance, node)
        distance = [float('inf')] * (n + 1)
        distance[1] = 0
        parent = [-1] * (n + 1)  # To reconstruct the path

        # Step 3: Perform Dijkstra's algorithm
        while min_heap:
            curr_dist, node = heapq.heappop(min_heap)

            # If a shorter path was already processed, skip
            if curr_dist > distance[node]:
                continue

            for neighbor, weight in graph[node]:
                new_dist = curr_dist + weight
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    heapq.heappush(min_heap, (new_dist, neighbor))
                    parent[neighbor] = node

        # Step 4: If the destination is unreachable, return -1
        if distance[n] == float('inf'):
            return [-1]

        # Step 5: Reconstruct the shortest path
        path = []
        curr = n
        while curr != -1:
            path.append(curr)
            curr = parent[curr]
        path.reverse()

        # Step 6: Return the result
        return [distance[n]] + path


# Example usage
sol = Solution()
print(sol.shortestPath(5, 6, [[1, 2, 2], [2, 5, 5], [2, 3, 4], [
      1, 4, 1], [4, 3, 3], [3, 5, 1]]))  # Output: [5, 1, 4, 3, 5]
print(sol.shortestPath(2, 1, [[1, 2, 2]]))  # Output: [2, 1, 2]
print(sol.shortestPath(2, 0, []))  # Output: [-1]
