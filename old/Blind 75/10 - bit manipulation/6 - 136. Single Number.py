'''
https://leetcode.com/problems/single-number/description/?envType=study-plan-v2&envId=leetcode-75

136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

'''
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        res = nums[0]

        for i in range(1, len(nums)):
            res = res ^ nums[i]

        return res

# binary search


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        l, r = 0, len(nums)-1

        while l < r:
            m = l + (r-l)//2

            if m % 2 == 0:
                if nums[m] == nums[m+1]:
                    l = m + 2
                else:
                    r = m
            else:
                if nums[m] == nums[m-1]:
                    l = m + 1
                else:
                    r = m - 1

        return nums[l]


sol = Solution()

print(sol.singleNumber([2, 2, 1]))  # 1
print(sol.singleNumber([4, 1, 2, 1, 2]))  # 4
