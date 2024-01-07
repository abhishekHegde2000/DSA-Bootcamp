'''
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
 


'''

from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_number_count = 0
        current_number = 1
        arr_index = 0
        while True:
            print(f"Checking if {current_number} is missing")
            if arr_index < len(arr) and arr[arr_index] == current_number:
                print(f"{current_number} is not missing")
                arr_index += 1
            else:
                print(f"{current_number} is missing")
                missing_number_count += 1
                if missing_number_count == k:
                    print(f"Found the {k}th missing number: {current_number}")
                    return current_number
            current_number += 1


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Initialize pointers to the start and end of the range
        lower_bound = 0
        upper_bound = len(arr)

        while lower_bound < upper_bound:
            # Calculate the middle index
            middle_index = lower_bound + (upper_bound - lower_bound) // 2
            print(f"Checking if the {
                  k}th missing number is before, at, or after index {middle_index}")

            # Determine the appropriate action based on the number of missing numbers before the middle index
            if arr[middle_index] - middle_index - 1 < k:
                print(f"The {k}th missing number is not before index {
                      middle_index}")
                lower_bound = middle_index + 1
            else:
                print(f"The {k}th missing number may be before index {
                      middle_index}")
                upper_bound = middle_index

        # Return the kth missing number
        print(f"The {k}th missing number is {lower_bound + k}")
        return lower_bound + k


sol = Solution()
print(sol.findKthPositive([2, 3, 4, 7, 11], 5))
print(sol.findKthPositive([1, 2, 3, 4], 2))
