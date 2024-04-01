'''
https://leetcode.com/problems/combinations/description/

77. Combinations

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
 

Constraints:

1 <= n <= 20
1 <= k <= n

'''
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Initialize an empty list to store the combinations
        combinations = []

        def generateCombinations(start, currentCombination):
            # Print the current state of variables for debugging
            print(f"Start: {start}, Current Combination: {currentCombination}")

            # If the length of the current combination is equal to k, append a copy of it to the combinations
            if len(currentCombination) == k:
                combinations.append(currentCombination[:])

            # Iterate over the range from start to n + 1
            for i in range(start, n + 1):
                # Append i to the current combination
                currentCombination.append(i)
                # Recursively call generateCombinations with i + 1 and the current combination
                generateCombinations(i + 1, currentCombination)
                # Remove the last element from the current combination
                currentCombination.pop()

        # Call generateCombinations with initial parameters
        generateCombinations(1, [])
        # Return the combinations
        return combinations


solution = Solution()

print(solution.combine(4, 2))
print(solution.combine(1, 1))
