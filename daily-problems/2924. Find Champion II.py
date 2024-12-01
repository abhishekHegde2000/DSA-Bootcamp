'''

https://leetcode.com/problems/find-champion-ii/description/?envType=daily-question&envId=2024-11-26

2924. Find Champion II
Medium
Topics
Companies
Hint
There are n teams numbered from 0 to n - 1 in a tournament; each team is also a node in a DAG.

You are given the integer n and a 0-indexed 2D integer array edges of length m representing the DAG, where edges[i] = [ui, vi] indicates that there is a directed edge from team ui to team vi in the graph.

A directed edge from a to b in the graph means that team a is stronger than team b and team b is weaker than team a.

Team a will be the champion of the tournament if there is no team b that is stronger than team a.

Return the team that will be the champion of the tournament if there is a unique champion, otherwise, return -1.

Notes

A cycle is a series of nodes a1, a2, ..., an, an+1 such that node a1 is the same node as node an+1, the nodes a1, a2, ..., an are distinct, and there is a directed edge from the node ai to node ai+1 for every i in the range [1, n].
A DAG is a directed graph that does not have any cycle.


Example 1:



Input: n = 3, edges = [[0,1],[1,2]]
Output: 0
Explanation: Team 1 is weaker than team 0. Team 2 is weaker than team 1. So the champion is team 0.
Example 2:



Input: n = 4, edges = [[0,2],[1,3],[1,2]]
Output: -1
Explanation: Team 2 is weaker than team 0 and team 1. Team 3 is weaker than team 1. But team 1 and team 0 are not weaker than any other teams. So the answer is -1.


Constraints:

1 <= n <= 100
m == edges.length
0 <= m <= n * (n - 1) / 2
edges[i].length == 2
0 <= edge[i][j] <= n - 1
edges[i][0] != edges[i][1]
The input is generated such that if team a is stronger than team b, team b is not stronger than team a.
The input is generated such that if team a is stronger than team b and team b is stronger than team c, then team a is stronger than team c.


Topics
Graph
Hint 1
The champion(s) should have in-degree 0 in the DAG.

------------------------------
Complexity Analysis
Here, N is the number of teams given, and M is the number of edges.

Time complexity: O(N+M)

We iterate over each edge to store the indegree of each team, this takes O(M) time. Then we iterate over each team to find the teams with zero indegree to get the champion which will take O(N) time. Hence, the total time complexity is equal to O(N+M)

Space complexity: O(N)

We need a list indegree to store the indegree of each of the N teams. Hence, the total space complexity is equal to O(N).
------------------------------




'''


class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        # Initialize the indegree array to track the number of incoming edges for each team
        indegree = [0] * n

        # Store the indegree of each team
        for edge in edges:
            indegree[edge[1]] += 1

        champ = -1
        champ_count = 0

        # Iterate through all teams to find those with an indegree of 0
        for i in range(n):
            # If the team can be a champion, store the team number and increment the count
            if indegree[i] == 0:
                champ_count += 1
                champ = i

        # If more than one team can be a champion, return -1, otherwise return the champion team number
        return champ if champ_count == 1 else -1


sol = Solution()


print(sol.findChampion(3, [[0, 1], [1, 2]]))  # 0
print(sol.findChampion(4, [[0, 2], [1, 3], [1, 2]]))  # -1
print(sol.findChampion(4, [[0, 1], [1, 2], [2, 3]]))  # 0
