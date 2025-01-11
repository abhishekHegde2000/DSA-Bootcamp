/*

https://www.geeksforgeeks.org/problems/shortest-path-in-weighted-undirected-graph/1


Shortest Path in Weighted undirected graph
Difficulty: MediumAccuracy: 50.0%Submissions: 66K+Points: 4
You are given a weighted undirected graph having n vertices numbered from 1 to n and m edges along with their weights. Find the shortest weight path between the vertex 1 and the vertex n,  if there exists a path, and return a list of integers whose first element is the weight of the path, and the rest consist of the nodes on that path. If no path exists, then return a list containing a single element -1.

The input list of edges is as follows - {a, b, w}, denoting there is an edge between a and b, and w is the weight of that edge.

Note: The driver code here will first check if the weight of the path returned is equal to the sum of the weights along the nodes on that path, if equal it will output the weight of the path, else -2. In case the list contains only a single element (-1) it will simply output -1.

Examples :

Input: n = 5, m= 6, edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
Output: 5
Explanation: Shortest path from 1 to n is by the path 1 4 3 5 whose weight is 5.
Input: n = 2, m= 1, edges = [[1, 2, 2]]
Output: 2
Explanation: Shortest path from 1 to 2 is by the path 1 2 whose weight is 2.
Input: n = 2, m= 0, edges = [ ]
Output: -1
Explanation: Since there are no edges, so no answer is possible.
Expected Time Complexity: O(m* log(n))
Expected Space Complexity: O(n+m)

Constraint:
2 <= n <= 106
0 <= m <= 106
1 <= a, b <= n
1 <= w <= 105

*/

type Edge = [number, number, number]; // Represents [u, v, w]

class Solution {
  shortestPath(n: number, m: number, edges: Edge[]): number[] {
    // Step 1: Create the graph as an adjacency list
    const graph: Map<number, [number, number][]> = new Map();
    for (let i = 1; i <= n; i++) {
      graph.set(i, []);
    }
    for (const [u, v, w] of edges) {
      graph.get(u)?.push([v, w]);
      graph.get(v)?.push([u, w]);
    }

    // Step 2: Initialize Dijkstra's algorithm
    const minHeap: [number, number][] = [[0, 1]]; // (distance, node)
    const distance: number[] = Array(n + 1).fill(Infinity);
    distance[1] = 0;
    const parent: number[] = Array(n + 1).fill(-1); // To reconstruct the path

    // Step 3: Perform Dijkstra's algorithm
    while (minHeap.length > 0) {
      const [currDist, node] = minHeap.shift()!;

      // If a shorter path was already processed, skip
      if (currDist > distance[node]) continue;

      for (const [neighbor, weight] of graph.get(node) || []) {
        const newDist = currDist + weight;
        if (newDist < distance[neighbor]) {
          distance[neighbor] = newDist;
          minHeap.push([newDist, neighbor]);
          parent[neighbor] = node;
          // Maintain the heap property by sorting
          minHeap.sort((a, b) => a[0] - b[0]);
        }
      }
    }

    // Step 4: If the destination is unreachable, return -1
    if (distance[n] === Infinity) {
      return [-1];
    }

    // Step 5: Reconstruct the shortest path
    const path: number[] = [];
    let curr = n;
    while (curr !== -1) {
      path.push(curr);
      curr = parent[curr];
    }
    path.reverse();

    // Step 6: Return the result
    return [distance[n], ...path];
  }
}

// Example usage
const sol = new Solution();
console.log(
  sol.shortestPath(5, 6, [
    [1, 2, 2],
    [2, 5, 5],
    [2, 3, 4],
    [1, 4, 1],
    [4, 3, 3],
    [3, 5, 1],
  ])
); // Output: [5, 1, 4, 3, 5]
console.log(sol.shortestPath(2, 1, [[1, 2, 2]])); // Output: [2, 1, 2]
console.log(sol.shortestPath(2, 0, [])); // Output: [-1]

// Complexity Analysis

// The time complexity for this approach is O(m * log(n)), where m is the number of edges in the graph and n is the number of vertices. The time complexity is dominated by the priority queue operations, which take O(log(n)) time for each edge.
