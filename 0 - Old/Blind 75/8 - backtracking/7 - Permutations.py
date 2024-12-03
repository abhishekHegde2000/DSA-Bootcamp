'''
https://leetcode.com/problems/permutations/description/?envType=study-plan-v2&envId=top-100-liked

46. Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

'''

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Initialize result list
        result = []

        # If the length of nums is 1, return a list containing nums as the only permutation
        if len(nums) == 1:
            return [nums[:]]

        # Iterate over the indices of nums
        for i in range(len(nums)):
            # Remove the element at the current index from nums and store it in current_num
            current_num = nums.pop(0)
            # Print current state
            print(f"Current Num: {current_num}, Remaining Nums: {nums}")

            # Recursively call permute on the updated nums and store the returned permutations in remaining_perms
            remaining_perms = self.permute(nums)

            # Iterate over remaining_perms
            for perm in remaining_perms:
                # Append current_num to the end of the current permutation
                perm.append(current_num)
                # Print current state
                print(f"Current Permutation: {perm}")

            # Extend result with remaining_perms
            result.extend(remaining_perms)
            # Append current_num back to nums
            nums.append(current_num)

        # Return result
        return result


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            # Remove the current element
            current_num = nums[i]
            remaining_nums = nums[:i] + nums[i+1:]

            # Generate permutations of the remaining numbers
            remaining_perms = self.permute(remaining_nums)

            # Insert the current number into each permutation
            for perm in remaining_perms:
                res.append([current_num] + perm)

        return res


sol = Solution()

# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(sol.permute([1, 2, 3]))
print(sol.permute([0, 1]))  # [[0,1],[1,0]]
