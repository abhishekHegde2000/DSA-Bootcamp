'''
https://leetcode.com/problems/sliding-window-maximum/?envType=study-plan-v2&envId=top-100-liked

239. Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
'''


import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Initialize an empty list for the result, a deque, and two pointers at the start of the list
        result = []
        left_pointer = right_pointer = 0
        indices_deque = collections.deque()

        # While the right pointer is less than the length of the list
        while right_pointer < len(nums):
            # While the deque is not empty and the current number is greater than the last number in the deque
            while indices_deque and nums[right_pointer] > nums[indices_deque[-1]]:
                # Remove the last number from the deque
                indices_deque.pop()
                print(f"Indices deque after popping: {indices_deque}")

            # Add the index of the current number to the deque
            indices_deque.append(right_pointer)
            print(f"Indices deque after appending: {indices_deque}")

            # If the left pointer is greater than the first index in the deque
            if left_pointer > indices_deque[0]:
                # Remove the first index from the deque
                indices_deque.popleft()
                print(f"Indices deque after popleft: {indices_deque}")

            # If the right pointer plus one is greater than or equal to the window size
            if right_pointer + 1 >= k:
                # Add the number at the first index in the deque to the result
                result.append(nums[indices_deque[0]])
                print(f"Result: {result}")
                # Move the left pointer to the right
                left_pointer += 1
                print(f"Moving left pointer to: {left_pointer}")

            # Move the right pointer to the right
            right_pointer += 1
            print(f"Moving right pointer to: {right_pointer}")

        # Return the result
        return result


sol = Solution()
print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3,3,5,5,6,7]
print(sol.maxSlidingWindow([1], 1))  # [1]
print(sol.maxSlidingWindow([1, -1], 1))  # [1, -1]
