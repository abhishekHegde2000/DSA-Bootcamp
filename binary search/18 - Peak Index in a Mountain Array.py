'''
852. Peak Index in a Mountain Array

An array arr is a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.

 

Example 1:

Input: arr = [0,1,0]
Output: 1
Example 2:

Input: arr = [0,2,1,0]
Output: 1
Example 3:

Input: arr = [0,10,5,2]
Output: 1
 

'''

from typing import List


from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # Initialize pointers to the start and end of the array
        start = 0
        end = len(arr) - 1

        while start < end:
            # Calculate the middle index
            middle = start + (end - start) // 2

            # If the middle element is greater than the next element, the peak is in the left half
            if arr[middle] > arr[middle + 1]:
                end = middle
            else:
                # Otherwise, the peak is in the right half
                start = middle + 1

        # The peak index is at the start pointer
        return start
