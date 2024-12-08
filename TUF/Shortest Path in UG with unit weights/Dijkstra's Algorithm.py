'''
https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/0

https://neetcode.io/problems/dijkstra

Dijkstra Algorithm
Difficulty: MediumAccuracy: 50.83%Submissions: 192K+Points: 4
Given a weighted, undirected and connected graph where you have given adjacency list adj. You have to find the shortest distance of all the vertices from the source vertex src, and return a list of integers denoting the shortest distance between each node and source vertex src.

Note: The Graph doesn't contain any negative weight edge.

Examples:

Input: adj = [[[1, 9]], [[0, 9]]], src = 0
Output: [0, 9]
Explanation:

The source vertex is 0. Hence, the shortest distance of node 0 is 0 and the shortest distance from node 0 to 1 is 9.
Input: adj = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]], src = 2
Output: [4, 3, 0]
Explanation:

For nodes 2 to 0, we can follow the path 2-1-0. This has a distance of 1+3 = 4, whereas the path 2-0 has a distance of 6. So, the Shortest path from 2 to 0 is 4.
The shortest distance from 0 to 1 is 1 .
Constraints:
1 ≤ no. of vertices ≤ 1000
0 ≤ adj[i][j] ≤ 1000
0 ≤ src < no. of vertices

'''
from typing import List, Dict
import heapq
from typing import List, Tuple


class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex src.

    # dijkstra function to find the shortest distance of all the vertices from the source vertex src.
    def dijkstra(self, adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
        # Your code here
        n = len(adj)

        min_heap = [(0, src)]

        # Initialize the distance of all the vertices from the source vertex to infinity.

        distance = [float('inf')] * n

        # Initialize the distance of the source vertex from itself to 0.

        distance[src] = 0

        # Loop until the heap is not empty.

        while min_heap:
            # Pop the element from the heap.

            dist, vertex = heapq.heappop(min_heap)

            # Traverse the adjacency list of the current vertex.

            for neighbor, weight in adj[vertex]:
                # If the distance of the neighbor from the source vertex is greater than the distance of the current vertex from the source vertex plus the weight of the edge between the current vertex and the neighbor.

                if distance[neighbor] > distance[vertex] + weight:
                    # Update the distance of the neighbor from the source vertex.

                    distance[neighbor] = distance[vertex] + weight

                    # Push the neighbor and its distance from the source vertex to the heap.

                    heapq.heappush(min_heap, (distance[neighbor], neighbor))

        # Return the distance of all the vertices from the source vertex.

        return distance


# class Solution:
#     # Implementation for Dijkstra's shortest path algorithm
#     def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
#         adj = {}
#         for i in range(n):
#             adj[i] = []

#         # s = src, d = dst, w = weight
#         for s, d, w in edges:
#             adj[s].append([d, w])

#         # Compute shortest paths
#         shortest = {}
#         minHeap = [[0, src]]
#         while minHeap:
#             w1, n1 = heapq.heappop(minHeap)
#             if n1 in shortest:
#                 continue
#             shortest[n1] = w1

#             for n2, w2 in adj[n1]:
#                 if n2 not in shortest:
#                     heapq.heappush(minHeap, [w1 + w2, n2])

#         # Fill in missing nodes
#         for i in range(n):
#             if i not in shortest:
#                 shortest[i] = -1

#         return shortest

# Driver code
sol = Solution()

print(sol.dijkstra([[[1, 9]], [[0, 9]]], 0))  # [0, 9]

print(sol.dijkstra([[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]], 2))
