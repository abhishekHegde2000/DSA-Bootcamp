'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

'''

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:  # Check if the list is empty
            return 0

        left_ptr = 0  # Initialize the left pointer
        right_ptr = len(nums) - 1  # Initialize the right pointer

        while left_ptr <= right_ptr:  # Loop until the pointers meet
            if nums[left_ptr] == val:  # If the element at left pointer is equal to val
                # Swap the elements at left and right pointers
                nums[left_ptr], nums[right_ptr] = nums[right_ptr], nums[left_ptr]
                right_ptr -= 1  # Decrement the right pointer
            else:
                left_ptr += 1  # Increment the left pointer

        return left_ptr  # Return the position of the left pointer

# example usage


sol = Solution()
print(sol.removeElement([3, 2, 2, 3], 3))  # output: 2, nums = [2,2,_,_]
# output: 5, nums = [0,1,4,0,3,_,_,_]
print(sol.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
nums = [3, 2, 2, 3]
val = 3
print(sol.removeElement(nums, val))  # output: 2, nums = [2,2,_,_]
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(sol.removeElement(nums, val))  # output: 5, nums = [0,1,4,0,3,_,_,_]
