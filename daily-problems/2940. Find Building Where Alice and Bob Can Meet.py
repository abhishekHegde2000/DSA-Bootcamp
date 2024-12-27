'''


https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

2940. Find Building Where Alice and Bob Can Meet
Hard
Topics
Companies
Hint
You are given a 0-indexed array heights of positive integers, where heights[i] represents the height of the ith building.

If a person is in building i, they can move to any other building j if and only if i < j and heights[i] < heights[j].

You are also given another array queries where queries[i] = [ai, bi]. On the ith query, Alice is in building ai while Bob is in building bi.

Return an array ans where ans[i] is the index of the leftmost building where Alice and Bob can meet on the ith query. If Alice and Bob cannot move to a common building on query i, set ans[i] to -1.



Example 1:

Input: heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
Output: [2,5,-1,5,2]
Explanation: In the first query, Alice and Bob can move to building 2 since heights[0] < heights[2] and heights[1] < heights[2].
In the second query, Alice and Bob can move to building 5 since heights[0] < heights[5] and heights[3] < heights[5].
In the third query, Alice cannot meet Bob since Alice cannot move to any other building.
In the fourth query, Alice and Bob can move to building 5 since heights[3] < heights[5] and heights[4] < heights[5].
In the fifth query, Alice and Bob are already in the same building.
For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.
Example 2:

Input: heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]
Output: [7,6,-1,4,6]
Explanation: In the first query, Alice can directly move to Bob's building since heights[0] < heights[7].
In the second query, Alice and Bob can move to building 6 since heights[3] < heights[6] and heights[5] < heights[6].
In the third query, Alice cannot meet Bob since Bob cannot move to any other building.
In the fourth query, Alice and Bob can move to building 4 since heights[3] < heights[4] and heights[0] < heights[4].
In the fifth query, Alice can directly move to Bob's building since heights[1] < heights[6].
For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.



Constraints:

1 <= heights.length <= 5 * 104
1 <= heights[i] <= 109
1 <= queries.length <= 5 * 104
queries[i] = [ai, bi]
0 <= ai, bi <= heights.length - 1


'''

import heapq
from collections import deque
from heapq import heappush, heappop


class Solution:
    def leftmostBuildingQueries(self, heights, queries):

        # left to right, up
        # not contiguous, if left == right , then already met
        # o(n)

        n = len(heights)

        res = [-1] * len(queries)

        for i, q in enumerate(queries):
            a, b = sorted(q)

            if a == b or heights[b] >= heights[a]:
                res[i] = b
                continue

            for j in range(b + 1, n):
                if heights[j] >= heights[a] and heights[j] >= heights[b]:
                    res[i] = j
                    break

        return res


class Solution:
    def leftmost_building_queries(self, building_heights, queries):
        """
        Determines the leftmost building index that satisfies the condition
        for each query in `queries`.

        Args:
            building_heights (List[int]): A list of building heights.
            queries (List[Tuple[int, int]]): A list of queries where each query
                is a tuple (start, end) representing two building indices.

        Returns:
            List[int]: A list of results where each entry corresponds to the leftmost
            building index for the respective query in `queries`.
        """
        # Total number of buildings
        num_buildings = len(building_heights)

        # Initialize results list with -1 (default for no valid building found)
        results = [-1] * len(queries)

        # Process each query
        for query_index, query in enumerate(queries):
            # Unpack the start and end indices and ensure they are sorted
            start_index, end_index = sorted(query)

            # Debugging: Print the current query and sorted indices
            print(f"Processing query {query_index}: Original {
                  query}, Sorted: ({start_index}, {end_index})")

            # If the start and end are the same, or the end building is taller or equal to the start building
            if start_index == end_index or building_heights[end_index] >= building_heights[start_index]:
                results[query_index] = end_index
                print(f"Direct match for query {
                      query_index}: Result = {end_index}")
                continue

            # Search for the leftmost building to the right that satisfies the height condition
            for building_index in range(end_index + 1, num_buildings):
                # Check if the building is taller or equal to both the start and end buildings
                if (building_heights[building_index] >= building_heights[start_index] and
                        building_heights[building_index] >= building_heights[end_index]):
                    results[query_index] = building_index
                    print(f"Found match for query {
                          query_index} at building index {building_index}")
                    break

        # Debugging: Print the final results before returning
        print(f"Final results: {results}")

        return results


class Solution:
    def leftmostBuildingQueries(self, heights, queries):
        max_idx = []  # Min-heap to simulate priority queue
        results = [-1] * len(queries)
        store_queries = [[] for _ in heights]

        # Store the mappings for all queries in store_queries.
        for idx, query in enumerate(queries):
            a, b = query
            if a < b and heights[a] < heights[b]:
                results[idx] = b
            elif a > b and heights[a] > heights[b]:
                results[idx] = a
            elif a == b:
                results[idx] = a
            else:
                store_queries[max(a, b)].append(
                    (max(heights[a], heights[b]), idx)
                )

        for idx, height in enumerate(heights):
            # If the heap's smallest value is less than the current height, it is an answer to the query.
            while max_idx and max_idx[0][0] < height:
                _, q_idx = heapq.heappop(max_idx)
                results[q_idx] = idx
            # Push the queries with their maximum index as the current index into the heap.
            for element in store_queries[idx]:
                heapq.heappush(max_idx, element)

        return results


sol = Solution()

print(sol.leftmostBuildingQueries([6, 4, 8, 5, 2, 7], [
      [0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]))  # [2,5,-1,5,2]

print(sol.leftmostBuildingQueries([5, 3, 8, 2, 6, 1, 4, 6], [
      [0, 7], [3, 5], [5, 2], [3, 0], [1, 6]]))  # [7,6,-1,4,6]
