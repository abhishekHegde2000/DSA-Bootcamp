'''
https://leetcode.com/discuss/interview-question/356935/
https://neetcode.io/problems/count-connected-components

Count Connected Components
There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

Return the total number of connected components in that graph.

Example 1:

Input:
n=3
edges=[[0,1], [0,2]]

Output:
1
Example 2:

Input:
n=6
edges=[[0,1], [1,2], [2, 3], [4, 5]]

Output:
2
Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2

'''

from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create a parent of itself , and give rank 1 for each
        parent = [i for i in range(n)]
        rank = [1] * n

        # find the parent of the node
        def find(node):
            res = node
            while res != parent[res]:
                res = parent[res]
            return res

        # union the nodes
        def union(node1, node2):
            p1 = find(node1)
            p2 = find(node2)
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return 1

        res = n
        for edge in edges:
            res -= union(edge[0], edge[1])

        return res


sol = Solution()
print(sol.countComponents(3, [[0, 1], [0, 2]]))  # 1
print(sol.countComponents(6, [[0, 1], [1, 2], [2, 3], [4, 5]]))  # 2
print(sol.countComponents(6, [[0, 1], [1, 2], [2, 3], [4, 5], [5, 4]]))  # 1
