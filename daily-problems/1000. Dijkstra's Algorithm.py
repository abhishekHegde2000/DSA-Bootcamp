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

from typing import List, Dict
import heapq

class Solution:
    def shortest_path(num_vertices: int, edges: List[List[int]], source_vertex: int) -> Dict[int, int]:
    """
    Finds the shortest path from a source vertex to all other vertices in a weighted graph.

    Args:
        num_vertices: The number of vertices in the graph.
        edges: A list of edges in the graph, where each edge is a list of three integers:
            [source vertex, destination vertex, weight].
        source_vertex: The vertex to start the search from.

    Returns:
        A dictionary mapping each vertex to its shortest path distance from the source vertex.
    """

    # Initialize the adjacency list.
    adjacency_list = {vertex: [] for vertex in range(num_vertices)}
    for source, destination, weight in edges:
        adjacency_list[source].append((destination, weight))

    # Initialize the shortest path dictionary.
    shortest_paths = {}

    # Initialize the min-heap with the source vertex.
    min_heap = [(0, source_vertex)]

    # While the min-heap is not empty, do the following:
    while min_heap:
        # Pop the vertex with the smallest distance from the min-heap.
        current_distance, current_vertex = heapq.heappop(min_heap)

        # If the current vertex has already been visited, skip it.
        if current_vertex in shortest_paths:
            continue

        # Add the current vertex to the shortest path dictionary.
        shortest_paths[current_vertex] = current_distance

        # For each neighbor of the current vertex, do the following:
        for neighbor, weight in adjacency_list[current_vertex]:
            # If the neighbor has not been visited, do the following:
            if neighbor not in shortest_paths:
                # Calculate the new distance to the neighbor.
                new_distance = current_distance + weight

                # Push the neighbor and its new distance onto the min-heap.
                heapq.heappush(min_heap, (new_distance, neighbor))

    # Fill the shortest path dictionary for vertices not reachable from the source vertex.
    for vertex in range(num_vertices):
        if vertex not in shortest_paths:
            shortest_paths[vertex


# test case

sol = Solution()

print(sol.shortest_path(5, [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]], 0)) # should return {{0:0}, {1:7}, {2:3}, {3:9}, {4:5}}
