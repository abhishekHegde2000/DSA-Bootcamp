'''
https://leetcode.com/problems/contiguous-array/

525. Contiguous Array

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

'''

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        mp = {}
        s = 0
        max_length = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                s -= 1
            else:
                s += 1
            if s == 0:
                max_length = i+1
            if s in mp:
                max_length = max(max_length, i-mp[s])
            else:
                mp[s] = i
        return max_length


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        mp = {}
        sum_of_counts = 0
        max_length = 0
        mp[0] = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                sum_of_counts -= 1
            else:
                sum_of_counts += 1
            if sum_of_counts in mp:
                max_length = max(max_length, i-mp[sum_of_counts])
            else:
                mp[sum_of_counts] = i
        return max_length


sol = Solution()
print(sol.findMaxLength([0, 1]))  # 2
print(sol.findMaxLength([0, 1, 0]))  # 2
print(sol.findMaxLength([0, 0, 1, 0, 0, 0, 1, 1]))  # 6
print(sol.findMaxLength([0, 0, 1, 0, 1, 1, 1, 0]))  # 6
