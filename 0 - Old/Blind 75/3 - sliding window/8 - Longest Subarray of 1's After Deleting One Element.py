'''
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

'''


from typing import List


class Solution:
    def longestSubarrayWithMaxOnes(self, nums: List[int], maxFlips: int) -> int:
        left = 0
        zerosCount = 0
        maxLength = 0
        # Iterate over the array
        for right in range(len(nums)):
            # If we encounter a 0, increment zerosCount
            if nums[right] == 0:
                zerosCount += 1
            # If zerosCount exceeds maxFlips, move the left end of the window forward
            if zerosCount > maxFlips:
                if nums[left] == 0:
                    zerosCount -= 1
                left += 1
            # Update maxLength
            maxLength = max(maxLength, right - left + 1)
        return maxLength
