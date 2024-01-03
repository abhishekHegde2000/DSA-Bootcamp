'''
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''

from typing import List

'''
class Solution:
    def longestConsecutive(self, arr: List[int]) -> int:
        # Remove duplicates and sort the array
        nums = list(set(arr))
        nums.sort()
        print(f"Sorted array: {nums}")

        # If the array has less than 2 elements, return its length
        if len(nums) < 2:
            return len(nums)

        # Initialize counters for the current sequence length and the maximum sequence length
        current_sequence_length = max_sequence_length = 1

        # Iterate over the sorted array
        for i in range(1, len(nums)):
            # If the current number is one more than the previous number
            if nums[i] == nums[i - 1] + 1:
                # Increment the current sequence length
                current_sequence_length += 1
                print(f"Current sequence length: {current_sequence_length}")

                # Update the maximum sequence length
                max_sequence_length = max(
                    max_sequence_length, current_sequence_length)
                print(f"Maximum sequence length: {max_sequence_length}")
            else:
                # Reset the current sequence length
                current_sequence_length = 1

        # Return the maximum sequence length
        return max_sequence_length
'''


class Solution:
    def longestConsecutive(self, arr: List[int]) -> int:
        # Convert the array to a set for O(1) lookup times
        nums_set = set(arr)

        max_sequence_length = 0

        # For each number in the set
        for num in nums_set:
            # If it is the first number of a sequence
            if num - 1 not in nums_set:
                # Check for the rest of the sequence in the set
                current_num = num
                current_sequence_length = 1

                while current_num + 1 in nums_set:
                    current_num += 1
                    current_sequence_length += 1

                # Update the maximum sequence length
                max_sequence_length = max(
                    max_sequence_length, current_sequence_length)

        # Return the maximum sequence length
        return max_sequence_length


sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
