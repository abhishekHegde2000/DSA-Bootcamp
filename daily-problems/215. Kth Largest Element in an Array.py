'''
https://leetcode.com/problems/kth-largest-element-in-an-array/

215. Kth Largest Element in an Array
Solved
Medium
Topics
Companies
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104

'''
import heapq
from heapq import heappush, heappop, nlargest, heapify
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # Sort the nums array in ascending order
        nums.sort()
        print(f"Sorted nums: {nums}")

        # Return the kth largest element in the nums array
        return nums[-k]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # Sort the nums array in ascending order
        num1 = sorted(nums, reverse=True)

        # Return the kth largest element in the nums array
        return num1[k-1]

#  using heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        return heap[0]

# using heapify


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapify(min_heap)

        for num in nums[k:]:
            heappush(min_heap, num)
            heappop(min_heap)

        return min_heap[0]

# making max heap with negative value


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []

        # Convert nums to a max heap by negating the values
        for num in nums:
            heapq.heappush(max_heap, -num)

        # Pop k-1 elements from the heap
        for _ in range(k - 1):
            heapq.heappop(max_heap)

        # The kth largest element is now at the top of the heap (after negating)
        return -max_heap[0]

#  using quickselect


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Adjust k to match 0-indexed array
        k = len(nums) - k
        print(f"Adjusted k: {k}")

        def quickSelect(left: int, right: int) -> int:
            # Choose the pivot as the last element in the current range
            pivot = nums[right]
            print(f"Pivot: {pivot}")

            # Initialize the partition index to the left boundary
            partitionIndex = left
            print(f"Initial partition index: {partitionIndex}")

            # Iterate over the current range
            for i in range(left, right):
                # If the current element is less than or equal to the pivot, swap it with the element at the partition index and increment the partition index
                if nums[i] <= pivot:
                    nums[partitionIndex], nums[i] = nums[i], nums[partitionIndex]
                    partitionIndex += 1
                    print(f"Swapped nums[{i}] and nums[{
                          partitionIndex - 1}], incremented partition index to {partitionIndex}")

            # Swap the pivot with the element at the partition index
            nums[partitionIndex], nums[right] = nums[right], nums[partitionIndex]
            print(f"Swapped pivot and nums[{partitionIndex}]")

            # If the partition index is greater than k, recurse on the left subarray
            if partitionIndex > k:
                print(f"Partition index > k, recursing on left subarray")
                return quickSelect(left, partitionIndex - 1)
            # If the partition index is less than k, recurse on the right subarray
            elif partitionIndex < k:
                print(f"Partition index < k, recursing on right subarray")
                return quickSelect(partitionIndex + 1, right)
            # If the partition index is equal to k, return the element at the partition index
            else:
                print(f"Partition index = k, returning nums[{partitionIndex}]")
                return nums[partitionIndex]

        return quickSelect(0, len(nums) - 1)


sol = Solution()
print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
print(sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
