'''

547. Number of Provinces
Medium
Topics
Companies
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.



Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3


Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]

'''


from typing import List
from collections import defaultdict


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Create an adjacency list to represent the graph
        num_cities = len(isConnected)
        adjacency_list = [[] for _ in range(num_cities)]

        # Populate the adjacency list with the given connections
        for i in range(num_cities):
            for j in range(num_cities):
                if isConnected[i][j] == 1:
                    adjacency_list[i].append(j)

        print(f"Adjacency List: {adjacency_list}")

        # Set to keep track of visited cities
        visited_cities = set()

        # Depth-First Search (DFS) function to explore all cities in the same province
        def dfs(city):
            if city not in visited_cities:
                visited_cities.add(city)
                for neighbor in adjacency_list[city]:
                    dfs(neighbor)

        # Counter for the number of provinces
        province_count = 0

        # Iterate over all cities
        for city in range(num_cities):
            if city not in visited_cities:
                dfs(city)
                province_count += 1

        return province_count

# Example usage:
# sol = Solution()
# print(sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))  # Output: 2
# Example usage:
# sol = Solution()
# print(sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))  # Output: 2


sol = Solution()

print(sol.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
print(sol.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))  # 3
print(sol.findCircleNum([[1, 0, 0], [0, 1, 1], [0, 1, 1]]))  # 1
