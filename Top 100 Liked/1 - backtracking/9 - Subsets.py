'''
https://leetcode.com/problems/subsets/description/?envType=study-plan-v2&envId=top-100-liked

78. Subsets

Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

'''

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Initialize all_subsets to store all subsets
        all_subsets = []

        def backtrack(current_subset, start):
            # Print current state
            print(f"Current Subset: {current_subset}, Start: {start}")

            # Append a copy of current_subset to all_subsets
            all_subsets.append(current_subset[:])

            # Iterate over the indices i from start to the length of nums
            for i in range(start, len(nums)):
                # Append nums[i] to current_subset
                current_subset.append(nums[i])
                # Print current state
                print(f"New Subset: {current_subset}")

                # Recursively call backtrack with current_subset and i + 1
                backtrack(current_subset, i + 1)

                # Remove the last element from current_subset
                current_subset.pop()

        # Call backtrack with initial parameters
        backtrack([], 0)
        # Return all_subsets
        return all_subsets


sol = Solution()

print(sol.subsets([1, 2, 3]))  # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(sol.subsets([0]))  # [[],[0]]
