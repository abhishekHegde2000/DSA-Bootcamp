'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 
'''


from typing import List


class Solution:
    def threeSumClosest(self, numbers: List[int], targetSum: int) -> int:
        # Get the length of the numbers
        numLength = len(numbers)

        # If there are less than 4 numbers, return their sum
        if numLength < 4:
            return sum(numbers)

        # Sort the numbers
        numbers.sort()

        # Initialize the closest sum to infinity
        closestSum = float('inf')

        # Iterate over the numbers
        for currentIndex in range(numLength - 2):
            # Initialize two pointers
            leftPointer, rightPointer = currentIndex + 1, numLength - 1

            # While the left pointer is less than the right pointer
            while leftPointer < rightPointer:
                # Calculate the current sum
                currentSum = numbers[currentIndex] + \
                    numbers[leftPointer] + numbers[rightPointer]

                # If the current sum is equal to the target sum, return it
                if currentSum == targetSum:
                    print(
                        f"Found exact target sum with numbers {numbers[currentIndex]}, {numbers[leftPointer]}, and {numbers[rightPointer]}")
                    return currentSum

                # If the current sum is closer to the target sum than the closest sum, update the closest sum
                if abs(currentSum - targetSum) < abs(closestSum - targetSum):
                    closestSum = currentSum
                    print(f"Updated closest sum to {closestSum}")

                # If the current sum is less than the target sum, move the left pointer to the right
                if currentSum < targetSum:
                    leftPointer += 1
                    print(
                        f"Current sum ({currentSum}) is less than target sum ({targetSum}). Moving left pointer to the right.")
                # If the current sum is greater than the target sum, move the right pointer to the left
                else:
                    rightPointer -= 1
                    print(
                        f"Current sum ({currentSum}) is greater than target sum ({targetSum}). Moving right pointer to the left.")

        # Return the closest sum
        return closestSum


sol = Solution()
print(sol.threeSumClosest([-1, 2, 1, -4], 1))
