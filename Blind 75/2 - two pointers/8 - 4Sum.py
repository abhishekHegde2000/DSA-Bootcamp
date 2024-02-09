'''
https://leetcode.com/problems/4sum/

18. 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
'''
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        uniqueQuadruplets = set()

        for currentIndex in range(len(nums) - 3):
            if currentIndex > 0 and nums[currentIndex] == nums[currentIndex - 1]:
                continue
            for i in range(currentIndex + 1, len(nums) - 2):
                if i > currentIndex + 1 and nums[i] == nums[i - 1]:
                    continue
                leftPointer, rightPointer = i + 1, len(nums) - 1
                while leftPointer < rightPointer:
                    currentSum = nums[currentIndex] + nums[i] + \
                        nums[leftPointer] + nums[rightPointer]
                    if currentSum == target:
                        uniqueQuadruplets.add(
                            (nums[currentIndex], nums[i], nums[leftPointer], nums[rightPointer]))
                        leftPointer += 1
                        rightPointer -= 1
                    elif currentSum < target:
                        leftPointer += 1
                    else:
                        rightPointer -= 1
        return list(uniqueQuadruplets)


sol = Solution()
print(sol.fourSum([1, 0, -1, 0, -2, 2], 0))
print(sol.fourSum([2, 2, 2, 2, 2], 8))
