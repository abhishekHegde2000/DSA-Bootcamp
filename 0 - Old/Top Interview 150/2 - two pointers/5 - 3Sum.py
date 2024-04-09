'''
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the list of numbers
        nums.sort()
        print(f"Sorted nums: {nums}")

        # Initialize a set to store unique triplets
        uniqueTriplets = set()

        # Iterate over the list of numbers
        for currentIndex in range(len(nums) - 2):
            # Skip the same element to avoid duplicate triplets
            if currentIndex > 0 and nums[currentIndex] == nums[currentIndex - 1]:
                continue

            # Initialize two pointers: one at the next index and the other at the end of the list
            leftPointer, rightPointer = currentIndex + 1, len(nums) - 1

            # Move the two pointers towards each other
            while leftPointer < rightPointer:
                currentSum = nums[currentIndex] + \
                    nums[leftPointer] + nums[rightPointer]
                print(f"Current sum: {currentSum}")

                # If the current sum is zero, we found a triplet
                if currentSum == 0:
                    uniqueTriplets.add(
                        (nums[currentIndex], nums[leftPointer], nums[rightPointer]))
                    print(
                        f"Found a triplet: {nums[currentIndex]}, {nums[leftPointer]}, {nums[rightPointer]}")
                    leftPointer += 1
                    rightPointer -= 1
                # If the current sum is less than zero, move the left pointer to the right
                elif currentSum < 0:
                    leftPointer += 1
                # If the current sum is greater than zero, move the right pointer to the left
                else:
                    rightPointer -= 1

        # Convert the set of triplets to a list and return it
        return list(uniqueTriplets)


sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
print(sol.threeSum([0, 1, 1]))
print(sol.threeSum([0, 0, 0]))
