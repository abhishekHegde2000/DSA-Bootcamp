'''
https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/


1509. Minimum Difference Between Largest and Smallest Value in Three Moves

You are given an integer array nums.

In one move, you can choose one element of nums and change it to any value.

Return the minimum difference between the largest and smallest value of nums after performing at most three moves.

 

Example 1:

Input: nums = [5,3,2,4]
Output: 0
Explanation: We can make at most 3 moves.
In the first move, change 2 to 3. nums becomes [5,3,3,4].
In the second move, change 4 to 3. nums becomes [5,3,3,3].
In the third move, change 5 to 3. nums becomes [3,3,3,3].
After performing 3 moves, the difference between the minimum and maximum is 3 - 3 = 0.
Example 2:

Input: nums = [1,5,0,10,14]
Output: 1
Explanation: We can make at most 3 moves.
In the first move, change 5 to 0. nums becomes [1,0,0,10,14].
In the second move, change 10 to 0. nums becomes [1,0,0,0,14].
In the third move, change 14 to 1. nums becomes [1,0,0,0,1].
After performing 3 moves, the difference between the minimum and maximum is 1 - 0 = 1.
It can be shown that there is no way to make the difference 0 in 3 moves.
Example 3:

Input: nums = [3,100,20]
Output: 0
Explanation: We can make at most 3 moves.
In the first move, change 100 to 7. nums becomes [3,7,20].
In the second move, change 20 to 7. nums becomes [3,7,7].
In the third move, change 3 to 7. nums becomes [7,7,7].
After performing 3 moves, the difference between the minimum and maximum is 7 - 7 = 0.
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

'''


import heapq
from tkinter.tix import INTEGER
from typing import List


class Solution:
    def minDifference(self, nums):
        # Check if the number of elements is 4 or less; if so, return 0
        num_elements = len(nums)
        print(f"Number of elements: {num_elements}")

        if num_elements <= 4:
            print("Number of elements is 4 or less, returning 0")
            return 0

        # Sort the list to simplify finding the minimum difference
        nums.sort()
        print(f"Sorted nums: {nums}")

        # Calculate the minimum difference by considering different scenarios of removing up to 3 elements
        min_difference = min(
            nums[-4] - nums[0],  # Removing the last three elements
            # Removing two elements from the end and one from the start
            nums[-3] - nums[1],
            # Removing two elements from the start and one from the end
            nums[-2] - nums[2],
            nums[-1] - nums[3]   # Removing the first three elements
        )
        print(f"Minimum difference calculated: {min_difference}")

        return min_difference


class Solution:
    def minDifference(self, nums):
        # Check the length of nums; if 4 or less, return 0 as we can remove all to minimize difference
        num_elements = len(nums)
        print(f"Number of elements: {num_elements}")

        if num_elements <= 4:
            return 0

        # Sort nums to simplify finding the minimum difference
        nums.sort()
        print(f"Sorted nums: {nums}")

        # Initialize minimum difference to infinity
        min_difference = float('inf')

        # Iterate through the first four elements to consider different scenarios of removing up to 3 elements
        for start_index in range(4):
            end_index = num_elements - 4 + start_index
            current_difference = nums[end_index] - nums[start_index]
            print(f"Current difference ({start_index}, {
                  end_index}): {current_difference}")

            # Update min_difference if the current difference is smaller
            min_difference = min(min_difference, current_difference)

        return min_difference


class Solution:
    def minDifference(self, nums):
        # Check the length of nums; if 4 or less, return 0 as we can remove all to minimize difference
        num_elements = len(nums)

        if num_elements <= 4:
            return 0

        min_four = sorted(heapq.nsmallest(4, nums))
        max_four = sorted(heapq.nlargest(4, nums))

        res = float('inf')

        for i in range(4):

            res = min(
                res, max_four[i] - min_four[i]
            )

        return res


sol = Solution()

print(sol.minDifference([5, 3, 2, 4]))  # 0
print(sol.minDifference([1, 5, 0, 10, 14]))  # 1
print(sol.minDifference([3, 100, 20]))  # 0
