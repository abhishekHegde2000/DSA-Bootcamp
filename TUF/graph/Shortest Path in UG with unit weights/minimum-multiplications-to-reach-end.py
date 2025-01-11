'''
Given start, end and an array arr of n numbers. At each step, start is multiplied with any number in the array and then mod operation with 100000 is done to get the new start.

Your task is to find the minimum steps in which end can be achieved starting from start. If it is not possible to reach end, then return -1.

Example 1:

Input:
arr[] = {2, 5, 7}
start = 3, end = 30
Output:
2
Explanation:
Step 1: 3*2 = 6 % 100000 = 6
Step 2: 6*5 = 30 % 100000 = 30
Example 2:

Input:
arr[] = {3, 4, 65}
start = 7, end = 66175
Output:
4
Explanation:
Step 1: 7*3 = 21 % 100000 = 21
Step 2: 21*3 = 63 % 100000 = 63
Step 3: 63*65 = 4095 % 100000 = 4095
Step 4: 4095*65 = 266175 % 100000 = 66175
Your Task:
You don't need to print or input anything. Complete the function minimumMultiplications() which takes an integer array arr, an integer start and an integer end as the input parameters and returns an integer, denoting the minumum steps to reach in which end can be achieved starting from start.

Expected Time Complexity: O(105)
Expected Space Complexity: O(105)

Constraints:

1 <= n <= 104
1 <= arr[i] <= 104
1 <= start, end < 105
'''


from typing import List


from typing import List
from collections import deque
from heapq import heappush, heappop


class Solution:
    def minimumMultiplications(self, arr: List[int], start: int, end: int) -> int:
        # Initialize variables
        MOD = 100000
        visited = [False] * MOD  # To track visited states
        # BFS queue, stores (current_number, steps)
        queue = deque([(start, 0)])

        # If start is already the end
        if start == end:
            return 0

        # BFS
        while queue:
            current, steps = queue.popleft()

            # Debug print: Current state
            # print(f"Visiting: {current}, Steps: {steps}")

            # Try all possible multiplications
            for num in arr:
                next_val = (current * num) % MOD

                # If we reach the end
                if next_val == end:
                    return steps + 1

                # If not visited, enqueue it
                if not visited[next_val]:
                    visited[next_val] = True
                    queue.append((next_val, steps + 1))

        # If end is not reachable
        return -1

    def minimumMultiplications_dijkstras(arr: List[int], start: int, end: int) -> int:

        if start == end:
            return 0

        min_heap = [(0, start)]
        visited = {start: 0}
        MOD = 100000

        while min_heap:
            steps, current = heappop(min_heap)

            for num in arr:
                next_num = (current * num) % MOD
                next_steps = steps + 1

                if next_num == end:
                    return next_steps

                if next_num not in visited or next_steps < visited[next_num]:
                    visited[next_num] = next_steps
                    heappush(min_heap, (next_steps, next_num))

        return -1  # If end is not reachable

        def minimumMultiplications_dfs(arr: List[int], start: int, end: int) -> int:

            memo = {}

            def dfs(current, steps):

                if current == end:
                    return steps

                if current in memo:
                    return memo[current]

                min_steps = float("inf")

                for num in arr:
                    next_val = (current * num) % 100000

                    if next_val not in memo:
                        memo[next_val] = dfs(next_val, steps + 1)

                    min_steps = min(min_steps, memo[next_val])

                return min_steps

        return dfs(start, 0) if start != end else -1

    def minimumMultiplications_dp(arr: List[int], start: int, end: int) -> int:
        MOD = 100000  # Constraint for modulo
        dp = [float("inf")] * MOD  # DP array initialized to infinity
        dp[start] = 0  # Start point requires 0 steps

        # Iterate only through reachable states
        for i in range(MOD):
            if dp[i] != float("inf"):  # Only process if `i` is reachable
                for num in arr:
                    next_val = (i * num) % MOD
                    # Update minimum steps
                    dp[next_val] = min(dp[next_val], dp[i] + 1)

        # Return the result for `end`
        return dp[end] if dp[end] != float("inf") else -1


sol = Solution()

print(sol.minimumMultiplications([2, 5, 7], 3, 30))  # 2
print(sol.minimumMultiplications([3, 4, 65], 7, 66175))  # 4
print(sol.minimumMultiplications([2, 3, 4], 1, 10))  # 3
