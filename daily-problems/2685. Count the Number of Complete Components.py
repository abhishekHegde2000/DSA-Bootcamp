'''
2685. Count the Number of Complete Components
Medium
Topics
Companies
Hint
You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.



Example 1:



Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
Output: 3
Explanation: From the picture above, one can see that all of the components of this graph are complete.
Example 2:



Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
Output: 1
Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.


Constraints:

1 <= n <= 50
0 <= edges.length <= n * (n - 1) / 2
edges[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
There are no repeated edges.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
31.8K
Submissions
47.9K
Acceptance Rate
66.4%
Topics
Depth-First Search
Breadth-First Search
Graph
Companies
Hint 1
Find the connected components of an undirected graph using depth-first search (DFS) or breadth-first search (BFS).
Hint 2
For each connected component, count the number of nodes and edges in the component.
Hint 3
A connected component is complete if and only if the number of edges in the component is equal to m*(m-1)/2, where m is the number of nodes in the component.
'''

from typing import List
from collections import defaultdict


class Solution:
    def countCompleteComponents(self, num_nodes: int, edges: List[List[int]]) -> int:
        # Create an adjacency list to represent the graph
        adjacency_list = {i: [] for i in range(num_nodes)}

        # Populate the adjacency list with the given edges
        for node1, node2 in edges:
            adjacency_list[node1].append(node2)
            adjacency_list[node2].append(node1)

        def dfs(node):
            # Add the node to the current component
            current_component.add(node)
            print(f"Visiting node: {node}, Current component: {
                  current_component}")

            # Recursively visit all unvisited neighbors
            for neighbor in adjacency_list[node]:
                if neighbor not in visited_nodes:
                    visited_nodes.add(neighbor)
                    dfs(neighbor)

        complete_components_count = 0
        visited_nodes = set()

        # Iterate over all nodes to find all components
        for node in range(num_nodes):
            if node not in visited_nodes:
                current_component = set()
                visited_nodes.add(node)
                dfs(node)
                print(f"Finished component: {current_component}")

                # Check if the current component is complete
                if all(len(adjacency_list[n]) == len(current_component) - 1 for n in current_component):
                    complete_components_count += 1
                    print(f"Component {current_component} is complete")

        print(f"Total complete components: {complete_components_count}")
        return complete_components_count

# Example usage:
# sol = Solution()
# print(sol.countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4]]))  # Output: 2


sol = Solution()

print(sol.countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4]]))  # 3
print(sol.countCompleteComponents(
    6, [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]))  # 1
