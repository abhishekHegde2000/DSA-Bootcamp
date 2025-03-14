'''
https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable


1579. Remove Max Number of Edges to Keep Graph Fully Traversable

Alice and Bob have an undirected graph of n nodes and three types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can be traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

 

Example 1:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
Example 2:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
Example 3:



Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.
 

 

Constraints:

1 <= n <= 105
1 <= edges.length <= min(105, 3 * n * (n - 1) / 2)
edges[i].length == 3
1 <= typei <= 3
1 <= ui < vi <= n
All tuples (typei, ui, vi) are distinct.
'''


from typing import List


class UF:

    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)
        self.n = n

    def find(self, node):
        root = self.parent[node]
        while root != self.parent[root]:
            root = self.parent[root]
        return root

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)

        if root1 == root2:
            return 0
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
            self.rank[root1] += self.rank[root2]
        else:
            self.parent[root1] = root2
            self.rank[root2] += self.rank[root1]

        self.n -= 1
        return 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        Alice, Bob = UF(n), UF(n)

        cnt = 0

        for t, u, v in edges:
            if t == 3:
                cnt += (Alice.union(u, v) | Bob.union(u, v))

        for t, u, v in edges:
            if t == 1:
                cnt += Alice.union(u, v)
            elif t == 2:
                cnt += Bob.union(u, v)

        if Alice.n == 1 and Bob.n == 1:
            return len(edges) - cnt

        return -1


sol = Solution()

print(sol.maxNumEdgesToRemove(4, [[3, 1, 2], [3, 2, 3], [
      1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]))  # 2
print(sol.maxNumEdgesToRemove(
    4, [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]))  # 0
print(sol.maxNumEdgesToRemove(4, [[3, 2, 3], [1, 1, 2], [2, 3, 4]]))  # -1
