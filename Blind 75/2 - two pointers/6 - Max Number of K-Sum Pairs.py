'''
1679. Max Number of K-Sum Pairs
Solved
Medium
Topics
Companies
Hint
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.

'''

from typing import List


class Solution:
    def maxOperations(self, numbers: List[int], target: int) -> int:
        # Sort the numbers
        numbers.sort()
        print(f"Sorted numbers: {numbers}")

        # Get the length of the numbers
        numLength = len(numbers)

        # Initialize the count of pairs and two pointers
        pairCount = 0
        leftPointer, rightPointer = 0, numLength - 1

        # While the left pointer is less than the right pointer
        while leftPointer < rightPointer:
            # Calculate the sum of the numbers at the left and right pointers
            currentSum = numbers[leftPointer] + numbers[rightPointer]

            # If the current sum is equal to the target
            if currentSum == target:
                # Increment the pair count
                pairCount += 1
                print(
                    f"Found a pair: ({numbers[leftPointer]}, {numbers[rightPointer]}). Current pair count: {pairCount}")

                # Move the left pointer to the right and the right pointer to the left
                leftPointer += 1
                rightPointer -= 1
            # If the current sum is less than the target
            elif currentSum < target:
                # Move the left pointer to the right
                leftPointer += 1
                print(
                    f"Current sum ({currentSum}) is less than target ({target}). Moving left pointer to the right.")
            # If the current sum is greater than the target
            else:
                # Move the right pointer to the left
                rightPointer -= 1
                print(
                    f"Current sum ({currentSum}) is greater than target ({target}). Moving right pointer to the left.")

        # Return the pair count
        return pairCount


sol = Solution()
print(sol.maxOperations([1, 2, 3, 4], 5))
