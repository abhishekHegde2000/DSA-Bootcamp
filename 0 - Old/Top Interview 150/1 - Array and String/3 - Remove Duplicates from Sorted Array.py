'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

'''

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize a pointer to keep track of the unique elements
        unique_count = 1

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # Compare the current element with the previous one
            if nums[i] != nums[i - 1]:
                # Update the array in-place with the unique element
                nums[unique_count] = nums[i]
                # Increment the unique count
                unique_count += 1

        # Return the count of unique elements
        return unique_count


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            current_num = nums[i]
            print(f"Checking for duplicates of {current_num}")
            while current_num in nums[i+1:]:
                print(f"Duplicate of {current_num} found. Removing it.")
                nums.remove(current_num)
            i += 1
        print(f"Final array: {nums}")
        return len(nums)


# example usage
sol = Solution()
nums = [1, 1, 2]
print(sol.removeDuplicates(nums))
print(nums)
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(sol.removeDuplicates(nums))
print(nums)


# example usage
sol = Solution()
nums = [1, 1, 2]
print(sol.removeDuplicates(nums))
print(nums)
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(sol.removeDuplicates(nums))
print(nums)
