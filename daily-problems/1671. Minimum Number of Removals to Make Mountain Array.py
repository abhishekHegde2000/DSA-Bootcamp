'''

https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/



1671. Minimum Number of Removals to Make Mountain Array
Hard
Topics
Companies
Hint
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array nums​​​, return the minimum number of elements to remove to make nums​​​ a mountain array.



Example 1:

Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need to remove any elements.
Example 2:

Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].


Constraints:

3 <= nums.length <= 1000
1 <= nums[i] <= 109
It is guaranteed that you can make a mountain array out of nums.

'''

from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)

        lis_length = [1] * N
        lds_length = [1] * N

        # Stores the length of longest increasing subsequence that ends at i.
        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis_length[i] = max(lis_length[i], lis_length[j] + 1)

        # Stores the length of longest decreasing subsequence that starts at i.
        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                if nums[i] > nums[j]:
                    lds_length[i] = max(lds_length[i], lds_length[j] + 1)

        min_removals = float("inf")
        for i in range(N):
            if lis_length[i] > 1 and lds_length[i] > 1:
                min_removals = min(
                    min_removals, N - lis_length[i] - lds_length[i] + 1
                )

        return min_removals


sol = Solution()

print(sol.minimumMountainRemovals([1, 3, 1]))  # 0
print(sol.minimumMountainRemovals([2, 1, 1, 5, 6, 2, 3, 1]))  # 3
print(sol.minimumMountainRemovals([4, 3, 2, 1, 1, 2, 3, 1]))  # 4
print(sol.minimumMountainRemovals([1, 2, 3, 4, 4, 3, 2, 1]))  # 1
print(sol.minimumMountainRemovals([1, 2, 3, 4, 4, 3, 2, 1, 1]))  # 1
