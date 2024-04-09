'''
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1

'''


# Intuition
# We are given a sorted and rotated array of unique elements. We need to find the index of the target element in this array.

# Approach
# We can use binary search to find the index of the target element in the array.
# We will start with the middle element of the array and then adjust the range based on the comparison of the middle element with the first and last elements of the range.
# We will keep doing this until we find the index of the target element or determine that it is not in the array.

# Pseudo Code
# Let's write the pseudo code for our approach.

# Set the left pointer to 0.
# Set the right pointer to len(nums) - 1.
# While the left pointer is less than or equal to the right pointer:
#     Set the middle pointer to the average of the left and right pointers.
#     If the middle element of the range is equal to the target, return the middle pointer.
#     If the middle element of the range is greater than the last element of the range, the pivot is in the left subarray.
#         If the target is between the first and middle elements of the range, adjust the right pointer to be one less than the middle pointer.
#         Otherwise, adjust the left pointer to be one more than the middle pointer.
#     Otherwise, the pivot is in the right subarray.
#         If the target is between the middle and last elements of the range, adjust the left pointer to be one more than the middle pointer.
#         Otherwise, adjust the right pointer to be one less than the middle pointer.
# Return -1 if the target is not in the array.

# Complexity
# Time complexity: O(log n)
# Space complexity: O(1)

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Initialize variables with meaningful names
        left_search_pointer = 0
        right_search_pointer = len(nums) - 1

        while left_search_pointer <= right_search_pointer:
            # Calculate the middle index
            middle_index = (left_search_pointer + right_search_pointer) // 2

            print(f"Current search range: {left_search_pointer} to {
                  right_search_pointer}, middle index: {middle_index}")

            if nums[middle_index] == target:
                return middle_index  # Target found

            # Determine the pivot's location and adjust the search accordingly
            if nums[middle_index] > nums[right_search_pointer]:
                # Pivot is in the left subarray
                if nums[left_search_pointer] <= target <= nums[middle_index]:
                    print("Pivot in left subarray, searching left half")
                    right_search_pointer = middle_index - 1
                else:
                    print("Pivot in left subarray, searching right half")
                    left_search_pointer = middle_index + 1
            else:
                # Pivot is in the right subarray
                if nums[middle_index] <= target <= nums[right_search_pointer]:
                    print("Pivot in right subarray, searching right half")
                    left_search_pointer = middle_index + 1
                else:
                    print("Pivot in right subarray, searching left half")
                    right_search_pointer = middle_index - 1
        return -1


sol = Solution()

print(sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
print(sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
print(sol.search(nums=[1], target=0))
