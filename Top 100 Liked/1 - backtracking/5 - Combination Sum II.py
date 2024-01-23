'''
https://leetcode.com/problems/combination-sum-ii/description/

40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

'''

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Initialize an empty list to store the combinations
        combinations = []
        # Sort the candidates list to handle duplicates
        candidates.sort()

        def backtrack(currentIndex, currentCombination, remainingTarget):
            # Print the current state of variables for debugging
            print(f"Current Index: {currentIndex}, Current Combination: {
                  currentCombination}, Remaining Target: {remainingTarget}")

            # If the remaining target is 0, append the current combination to the combinations
            if remainingTarget == 0:
                combinations.append(currentCombination.copy())
                return

            # If the remaining target is less than 0, return
            if remainingTarget < 0:
                return

            # Initialize a variable to keep track of the previous candidate to handle duplicates
            previousCandidate = -1

            for i in range(currentIndex, len(candidates)):
                # If the current candidate is equal to the previous candidate, continue to the next iteration to avoid duplicates
                if candidates[i] == previousCandidate:
                    continue

                # Add the current candidate to the current combination
                currentCombination.append(candidates[i])
                # Recursively call backtrack with the next index and the updated remaining target
                backtrack(i + 1, currentCombination,
                          remainingTarget - candidates[i])
                # Remove the last element from the current combination
                currentCombination.pop()
                # Update the previous candidate
                previousCandidate = candidates[i]

        # Call backtrack with initial parameters
        backtrack(0, [], target)
        # Return the combinations
        return combinations


sol = Solution()

print(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(sol.combinationSum2([2, 5, 2, 1, 2], 5))
