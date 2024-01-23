'''
https://leetcode.com/problems/combination-sum-iii/

216. Combination Sum III

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
 

Constraints:

2 <= k <= 9
1 <= n <= 60

'''

from typing import List


class Solution:
    def combinationSum3(self, num_elements: int, target: int) -> List[List[int]]:
        # Initialize result list
        result = []

        def backtrack(start, current_combination, remaining_elements, remaining_target):
            # Print current state
            print(f"Start: {start}, Current Combination: {current_combination}, Remaining Elements: {
                  remaining_elements}, Remaining Target: {remaining_target}")

            # If remaining elements is zero and remaining target is zero, a valid combination is found
            if remaining_elements == 0 and remaining_target == 0:
                result.append(current_combination[:])
                return

            # If remaining elements is zero or remaining target is less than zero, the current combination is invalid
            if remaining_elements == 0 or remaining_target < 0:
                return

            # Iterate over the numbers from start to 9
            for num in range(start, 10):
                # Append the current number to current combination
                current_combination.append(num)
                # Recursively call backtrack with the next number, updated current combination, decreased remaining elements, and decreased remaining target
                backtrack(num + 1, current_combination,
                          remaining_elements - 1, remaining_target - num)
                # Remove the last element from current combination to backtrack
                current_combination.pop()

        # Call backtrack with initial parameters
        backtrack(1, [], num_elements, target)
        # Return result
        return result


sol = Solution()
print(sol.combinationSum3(3, 7))
print(sol.combinationSum3(3, 9))
print(sol.combinationSum3(4, 1))


sol = Solution()
print(sol.combinationSum3(3, 7))
print(sol.combinationSum3(3, 9))
print(sol.combinationSum3(4, 1))
