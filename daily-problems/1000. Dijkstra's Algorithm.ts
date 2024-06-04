import PriorityQueue from "priority-queue-js";

class Solution {
    /**
     * Implementation for Dijkstra's shortest path algorithm
     * @param {number} numNodes Number of nodes in the graph
     * @param {number[][]} edges List of edges [src, dst, weight]
     * @param {number} sourceNode Source node
     * @returns {Object} Shortest distances from source node to other nodes
     */
    shortestPath(
        numNodes: number,
        edges: number[][],
        sourceNode: number
    ): { [key: number]: number } {
        // Initialize adjacency list
        const adjacencyList: { [key: number]: [number, number][] } = {};
        for (let i = 0; i < numNodes; i++) {
            adjacencyList[i] = [];
        }

        // Populate adjacency list from edges
        for (const [startNode, endNode, weight] of edges) {
            adjacencyList[startNode].push([endNode, weight]);
        }
        console.log(`Adjacency List: ${JSON.stringify(adjacencyList)}`);

        // Initialize shortest paths object
        const shortestPaths: { [key: number]: number } = {};
        // Initialize priority queue with source node
        const priorityQueue = new PriorityQueue<number[]>(
            (a, b) => b[0] - a[0]
        );
        priorityQueue.enq([0, sourceNode]);

        // Process nodes in priority queue
        while (!priorityQueue.isEmpty()) {
            const [currentWeight, currentNode] = priorityQueue.deq()!;
            console.log(
                `Processing node ${currentNode} with current weight ${currentWeight}`
            );

            // Skip if node has already been visited
            if (shortestPaths.hasOwnProperty(currentNode)) {
                console.log(`Node ${currentNode} already visited, skipping`);
                continue;
            }

            // Update shortest path for current node
            shortestPaths[currentNode] = currentWeight;
            console.log(
                `Updated shortest path for node ${currentNode}: ${currentWeight}`
            );

            // Add neighbors to priority queue
            for (const [neighborNode, edgeWeight] of adjacencyList[
                currentNode
            ]) {
                if (!shortestPaths.hasOwnProperty(neighborNode)) {
                    priorityQueue.enq([
                        currentWeight + edgeWeight,
                        neighborNode,
                    ]);
                    console.log(
                        `Added neighbor node ${neighborNode} to queue with weight ${
                            currentWeight + edgeWeight
                        }`
                    );
                }
            }
        }

        // Set shortest path to -1 for unreachable nodes
        for (let i = 0; i < numNodes; i++) {
            if (!shortestPaths.hasOwnProperty(i)) {
                shortestPaths[i] = -1;
                console.log(
                    `Node ${i} is unreachable, setting shortest path to -1`
                );
            }
        }

        return shortestPaths;
    }
}

let sol = new Solution();

const solution = new Solution();

// Test case 1
const n1 = 5;
const edges1 = [
    [0, 1, 10],
    [0, 2, 5],
    [1, 2, 2],
    [1, 3, 1],
    [2, 3, 9],
    [2, 4, 2],
    [3, 4, 6],
];
const src1 = 0;
console.log("Test Case 1:", solution.shortestPath(n1, edges1, src1));

// Test case 2
const n2 = 3;
const edges2 = [
    [0, 1, 3],
    [0, 2, 5],
    [1, 2, 2],
];
const src2 = 0;
console.log("Test Case 2:", solution.shortestPath(n2, edges2, src2));

// Test case 3
const n3 = 4;
const edges3 = [
    [0, 1, 1],
    [0, 2, 2],
    [1, 3, 5],
    [2, 3, 2],
];
const src3 = 0;
console.log("Test Case 3:", solution.shortestPath(n3, edges3, src3));
