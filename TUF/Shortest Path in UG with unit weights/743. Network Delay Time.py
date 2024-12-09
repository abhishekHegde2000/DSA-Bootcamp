'''
https://leetcode.com/problems/network-delay-time/description/


743. Network Delay Time
Solved
Medium
Topics
Companies
Hint
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.



Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1


Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
'''

import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Calculate the minimum time it takes for all the nodes to receive the signal
        starting from node k. If any node is unreachable, return -1.

        Args:
            times (List[List[int]]): A list of times represented by [source, destination, weight].
            n (int): The number of nodes in the graph.
            k (int): The starting node to send the signal from.

        Returns:
            int: The minimum time for all nodes to receive the signal, or -1 if some nodes cannot reach the signal.
        """
        # Step 1: Initialize distances array and graph
        # distances from source to each node
        distances = [float('inf')] * (n + 1)
        distances[k] = 0  # distance to source node is 0

        # Graph construction
        graph = {i: [] for i in range(1, n + 1)}
        for source, destination, weight in times:
            # add directed edge source -> destination with weight
            graph[source].append((destination, weight))

        # Step 2: Initialize the priority queue (min-heap)
        min_heap = [(0, k)]  # (current_distance, node)

        while min_heap:
            # Step 3: Pop the node with the smallest distance
            current_time, node = heapq.heappop(min_heap)

            # Step 4: If the current node's distance is already greater, skip it
            if current_time > distances[node]:
                continue

            # Step 5: Explore neighbors
            for neighbor, time in graph[node]:
                new_time = current_time + time
                if new_time < distances[neighbor]:
                    distances[neighbor] = new_time
                    heapq.heappush(min_heap, (new_time, neighbor))

        # Step 6: Check if all nodes are reachable
        # Ignore distances[0] since nodes are 1-indexed
        max_time = max(distances[1:])
        return max_time if max_time < float('inf') else -1


sol = Solution()

print(sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))  # 2
print(sol.networkDelayTime([[1, 2, 1]], 2, 1))  # 1
print(sol.networkDelayTime([[1, 2, 1]], 2, 2))  # -1
