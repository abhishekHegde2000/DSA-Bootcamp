'''
https://leetcode.com/problems/combination-sum/description/?envType=study-plan-v2&envId=top-100-liked

39. Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
'''

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Initialize an empty list to store the combinations
        result = []

        def depthFirstSearch(index, currentCombination, currentTotal):
            # Print the current state of variables for debugging
            print(f"Index: {index}, Current Combination: {
                  currentCombination}, Current Total: {currentTotal}")

            # If the current total is equal to the target, append the current combination to the result
            if currentTotal == target:
                result.append(currentCombination.copy())
                return

            # If the index is out of bounds or the current total exceeds the target, return
            if index >= len(candidates) or currentTotal > target:
                return

            # Add the current candidate to the current combination
            currentCombination.append(candidates[index])
            # Recursively call depthFirstSearch with the same index and the updated current total
            depthFirstSearch(index, currentCombination,
                             currentTotal + candidates[index])
            # Remove the last element from the current combination
            currentCombination.pop()
            # Recursively call depthFirstSearch with index + 1 and the same current total
            depthFirstSearch(index + 1, currentCombination, currentTotal)

        # Call depthFirstSearch with initial parameters
        depthFirstSearch(0, [], 0)
        # Return the result
        return result
