'''

Dijkstra's Algorithm
Implement Dijkstra's shortest path algorithm.

Given a weighted, directed graph, and a starting vertex, return the shortest distance from the starting vertex to every vertex in the graph.

Input:

n - the number of vertices in the graph, where (2 <= n <= 100). Each vertex is labeled from 0 to n - 1.
edges - a list of tuples, each representing a directed edge in the form (u, v, w), where u is the source vertex, v is the destination vertex, and w is the weight of the edge, where (1 <= w <= 10).
src - the source vertex from which to start the algorithm, where (0 <= src < n).
Note: If a vertex is unreachable from the source vertex, the shortest path distance for the unreachable vertex should be -1.

Example 1:

Dijkstra's Algorithm

Input:
n = 5
edges = [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]]
src = 0

Output:
{{0:0}, {1:7}, {2:3}, {3:9}, {4:5}}



'''


from collections import defaultdict
from typing import List, Dict
import heapq


class Solution:
    def shortestPath(self, num_vertices: int, edges: List[List[int]], source_vertex: int) -> Dict[int, int]:
        # Initialize an adjacency list for the graph
        adjacency_list = {i: [] for i in range(num_vertices)}
        print(f"Initial adjacency_list: {adjacency_list}")

        # Populate the adjacency list with the given edges
        for start_vertex, end_vertex, weight in edges:
            adjacency_list[start_vertex].append((end_vertex, weight))
        print(f"Populated adjacency_list: {adjacency_list}")

        # Initialize a dictionary to store the shortest path from the source to each vertex
        shortest_path = {}
        print(f"Initial shortest_path: {shortest_path}")

        # Initialize a min heap with the source vertex and its distance (0)
        min_heap = [(0, source_vertex)]
        print(f"Initial min_heap: {min_heap}")

        while min_heap:
            # Pop the vertex with the smallest distance from the heap
            current_weight, current_vertex = heapq.heappop(min_heap)
            print(f"Popped vertex: {current_vertex}, weight: {current_weight}")

            # If the vertex has already been visited, continue to the next iteration
            if current_vertex in shortest_path:
                print(f"Vertex {current_vertex} already visited, skipping")
                continue

            # Mark the vertex as visited and store its distance in the shortest path dictionary
            shortest_path[current_vertex] = current_weight
            print(f"Marked vertex {
                  current_vertex} as visited, updated shortest_path: {shortest_path}")

            # For each neighbor of the vertex, if it has not been visited, push it into the heap with its distance
            for neighbor_vertex, neighbor_weight in adjacency_list[current_vertex]:
                if neighbor_vertex not in shortest_path:
                    heapq.heappush(min_heap, (current_weight +
                                   neighbor_weight, neighbor_vertex))
                    print(f"Pushed vertex {neighbor_vertex} into min_heap with weight {
                          current_weight + neighbor_weight}")

        # For each vertex that is not reachable from the source, set its shortest path distance to -1
        for vertex in range(num_vertices):
            if vertex not in shortest_path:
                shortest_path[vertex] = -1
                print(f"Vertex {
                      vertex} not reachable from source, set shortest_path[{vertex}] to -1")

        # Return the shortest path dictionary
        return shortest_path


sol = Solution()

print(sol.shortestPath(5, [[0, 1, 10], [0, 2, 3], [1, 3, 2], [2, 1, 4], [
      2, 3, 8], [2, 4, 2], [3, 4, 5]], 0))  # {0: 0, 1: 7, 2: 3, 3: 9, 4: 5}

print(sol.shortestPath(5, [[0, 1, 10], [0, 2, 3], [1, 3, 2], [2, 1, 4], [
      2, 3, 8], [2, 4, 2], [3, 4, 5]], 1))  # {0: -1, 1: 0, 2: 7, 3: 2, 4: 7}
