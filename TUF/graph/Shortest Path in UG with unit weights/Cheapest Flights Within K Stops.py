'''
https://www.geeksforgeeks.org/problems/cheapest-flights-within-k-stops/1https://www.geeksforgeeks.org/problems/cheapest-flights-within-k-stops/1

Cheapest Flights Within K Stops
Difficulty: MediumAccuracy: 49.99%Submissions: 36K+Points: 4
There are n cities and m edges connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from the city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

Note: The price from city A to B may be different From the price from city B to A.

Example 1:
Input:
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
Output:
700
Explanation:
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

Constraint:
1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
There will not be any multiple flights between the two cities.
0 <= src, dst, k < n
src != dst
'''

from typing import List
import heapq
from collections import defaultdict


class Solution:
    def CheapestFLight(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Step 1: Build the graph using an adjacency list
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))

        # Step 2: Min-heap for priority queue
        heap = [(0, src, k + 1)]  # (cost, city, stops_left)
        # visited[city][stops_left] will store the minimum cost to reach city with stops_left
        visited = [[float('inf')] * (k + 2) for _ in range(n)]
        visited[src][k + 1] = 0

        while heap:
            cost, city, stops = heapq.heappop(heap)

            # If we reach the destination city, return the cost
            if city == dst:
                return cost

            # Explore neighbors only if stops are available
            if stops > 0:
                for neighbor, price in graph[city]:
                    new_cost = cost + price
                    # Only push to the heap if it's cheaper than the previously known cost
                    if new_cost < visited[neighbor][stops - 1]:
                        visited[neighbor][stops - 1] = new_cost
                        heapq.heappush(heap, (new_cost, neighbor, stops - 1))

        # If no valid path is found
        return -1


sol = Solution()

print(sol.CheapestFLight(4, [[0, 1, 100], [1, 2, 100], [
      2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1))  # 700

print(sol.CheapestFLight(
    3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))  # 200

print(sol.CheapestFLight(
    3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))  # 500
