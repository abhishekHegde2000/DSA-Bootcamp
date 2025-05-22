'''

https://leetcode.com/problems/zero-array-transformation-iii


3362. Zero Array Transformation III
Medium
Topics
Companies
Hint
You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri].

Each queries[i] represents the following action on nums:

Decrement the value at each index in the range [li, ri] in nums by at most 1.
The amount by which the value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to 0.

Return the maximum number of elements that can be removed from queries, such that nums can still be converted to a zero array using the remaining queries. If it is not possible to convert nums to a zero array, return -1.



Example 1:

Input: nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]

Output: 1

Explanation:

After removing queries[2], nums can still be converted to a zero array.

Using queries[0], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
Using queries[1], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
Example 2:

Input: nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]]

Output: 2

Explanation:

We can remove queries[2] and queries[3].

Example 3:

Input: nums = [1,2,3,4], queries = [[0,3]]

Output: -1

Explanation:

nums cannot be converted to a zero array even after using all the queries.



Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
1 <= queries.length <= 105
queries[i].length == 2
0 <= li <= ri < nums.length
'''
from typing import List


from heapq import heappush, heappop
from typing import List


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        # Sort queries by start index
        queries.sort(key=lambda x: x[0])

        heap = []  # max-heap (simulated using negatives)
        deltaArray = [0] * (len(nums) + 1)
        operations = 0  # Tracks the current coverage at index i
        j = 0  # Pointer to current query

        print("Sorted Queries:", queries)

        for i, num in enumerate(nums):
            operations += deltaArray[i]
            print(
                f"\nAt index {i}, nums[i]={num}, current operations={operations}")

            # Push all queries that start at i into the heap (sorted by end)
            while j < len(queries) and queries[j][0] == i:
                heappush(heap, -queries[j][1])
                print(f"  Pushing query {queries[j]} into heap")
                j += 1

            # While we don’t have enough operations to reduce nums[i], pick more queries
            while operations < num and heap and -heap[0] >= i:
                end = -heappop(heap)
                print(f"  Using query ending at {end} to increase operations")
                operations += 1
                deltaArray[end + 1] -= 1  # Schedule decrease after end

            if operations < num:
                print(
                    f"  ❌ Cannot reduce nums[{i}] = {num} with available queries.")
                return -1

        print(f"\n✅ Remaining heap (unused queries): {[-x for x in heap]}")
        return len(heap)


sol = Solution()

print(sol.maxRemoval([2, 0, 2], [[0, 2], [0, 2], [1, 1]]))  # 1
print(sol.maxRemoval([1, 1, 1, 1], [[1, 3], [0, 2], [1, 3], [1, 2]]))  # 2
print(sol.maxRemoval([1, 2, 3, 4], [[0, 3]]))  # -1
