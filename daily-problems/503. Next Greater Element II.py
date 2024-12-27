'''
https://leetcode.com/problems/next-greater-element-ii/description/


503. Next Greater Element II
Solved
Medium
Topics
Companies
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.



Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number.
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]


Constraints:

1 <= nums.length <= 104
-109 <= nums[i] <= 109
'''

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # its a circular array, so we can just double the array

        arr = nums + nums

        stack = []

        next_greater = [-1] * len(arr)

        for i in range(len(arr)):
            while stack and arr[stack[-1]] < arr[i]:
                next_greater[stack.pop()] = arr[i]
            stack.append(i)

        return next_greater[:len(nums)]


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # we can also use 2 passes to solve this problem
        # while doing second pass, we can break the loop if the stack is empty
        stack = []
        ans = [-1] * len(nums)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack[-1]] = nums[i]
                stack.pop()
            stack.append(i)

        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack[-1]] = nums[i]
                stack.pop()
            if not stack:
                break

        return ans


sol = Solution()

print(sol.nextGreaterElements([1, 2, 1]))  # [2,-1,2]
print(sol.nextGreaterElements([1, 2, 3, 4, 3]))  # [2,3,4,-1,4]
print(sol.nextGreaterElements([4, 5, 3, 2]))  # [5,-1,4,4]
