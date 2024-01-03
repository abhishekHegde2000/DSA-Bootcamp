'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''


from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Calculate the length of the list
        list_length = len(nums) - 1
        print(f"List length: {list_length}")

        # Calculate the majority count
        majority_count = list_length // 2
        print(f"Majority count: {majority_count}")

        # Count the occurrences of each number in the list
        num_counter = Counter(nums)
        print(f"Number counter: {num_counter}")

        # Iterate over the counter items
        for num, count in num_counter.items():
            print(f"Checking number {num} with count {count}")
            # If the count of a number is greater than the majority count, return it
            if count > majority_count:
                print(f"Majority element found: {num}")
                return num

        print("No majority element found")
        return None


sol = Solution()
nums = [3, 2, 3]
print(sol.majorityElement(nums))
nums = [2, 2, 1, 1, 1, 2, 2]
print(sol.majorityElement(nums))
