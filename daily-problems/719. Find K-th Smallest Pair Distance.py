'''
https://leetcode.com/problems/find-k-th-smallest-pair-distance/

719. Find K-th Smallest Pair Distance

The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

 

Example 1:

Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Example 2:

Input: nums = [1,1,1], k = 2
Output: 0
Example 3:

Input: nums = [1,6,1], k = 3
Output: 5
 

Constraints:

n == nums.length
2 <= n <= 104
0 <= nums[i] <= 106
1 <= k <= n * (n - 1) / 2

Brute force:

Overview
The goal is to find the k-th smallest distance between any two different elements in an array nums. The distance between two elements nums[i] and nums[j] is defined as the absolute difference between their values, |nums[i] - nums[j]|. We only consider pairs where i is less than j to avoid counting the same pair twice.

For example:

Input: nums = [1, 3, 1], k = 1
Output: 0

Let's look at all possible pairs of elements and their distances:

Pair (1, 3):

Distance: |1 - 3| = 2
Pair (1, 1):

Distance: |1 - 1| = 0
Pair (3, 1):

Distance: |3 - 1| = 2
So, the distances are [2, 0, 2].

To find the k-th smallest distance, we sort these distances: [0, 2, 2].

Since k = 1, we need the 1st smallest distance, which is 0.

Thus, the result is 0.

The brute-force approach involves checking the distance for every possible pair of elements in the array and maintaining the k smallest distances using a heap. Specifically, we iterate over all pairs, calculate their absolute distances, and use a max-heap to keep track of the k smallest distances. If the heap size exceeds k, we remove the largest element. After processing all pairs, the root of the heap will represent the k-th smallest distance.

However, this method is computationally heavy and will lead to a Time Limit Exceeded (TLE) error. The time complexity is dominated by the need to examine all pairs, which is O(n 
2
 ), combined with the overhead of maintaining a heap of size k, resulting in an overall time complexity of O(n 
2
 logk), where n is the number of elements. This makes the approach impractical for large values of n.
'''

import heapq


class Solution:
    def smallestDistancePair(self, nums, k):
        # Length of the input list
        n = len(nums)
        # Max heap to store the k smallest distances (using negative values to simulate max heap)
        max_heap = []

        # Iterate through each pair of elements in nums
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate the absolute difference between the pair
                diff = abs(nums[i] - nums[j])
                print(f"Comparing nums[{i}] = {
                      nums[i]} and nums[{j}] = {nums[j]}, diff = {diff}")

                # If the heap size is less than k, push the negative difference onto the heap
                if len(max_heap) < k:
                    heapq.heappush(max_heap, -diff)
                    print(f"Heap size < {
                          k}, pushed {-diff} onto the heap: {max_heap}")
                else:
                    # If the current difference is smaller than the largest in the heap, replace it
                    if -diff > max_heap[0]:
                        removed = heapq.heappop(max_heap)
                        heapq.heappush(max_heap, -diff)
                        print(f"Replaced {
                              removed} with {-diff} in the heap: {max_heap}")

        # The k-th smallest distance is the root of the heap (negated back to positive)
        result = -max_heap[0]
        print(f"The k-th smallest distance is {result}")
        return result


class Solution:
    def smallestDistancePair(self, nums, k):
        # Length of the input list
        n = len(nums)
        # Max heap to store the k smallest distances (using negative values to simulate max heap)
        max_heap = []

        # Iterate through each pair of elements in nums
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate the absolute difference between the pair
                diff = abs(nums[i] - nums[j])
                print(f"Comparing nums[{i}] = {
                      nums[i]} and nums[{j}] = {nums[j]}, diff = {diff}")

                # If the heap size is less than k, push the negative difference onto the heap
                if len(max_heap) < k:
                    heapq.heappush(max_heap, -diff)
                    print(f"Heap size < {
                          k}, pushed {-diff} onto the heap: {max_heap}")
                else:
                    # If the current difference is smaller than the largest in the heap, replace it
                    if -diff > max_heap[0]:
                        removed = heapq.heappop(max_heap)
                        heapq.heappush(max_heap, -diff)
                        print(f"Replaced {
                              removed} with {-diff} in the heap: {max_heap}")

        # The k-th smallest distance is the largest element in the max heap (negated back to positive)
        kth_smallest_distance = -max_heap[0]
        return kth_smallest_distance


sol = Solution()

print(sol.smallestDistancePair([2, 3, 1, 4], 3))  # 1

print(sol.smallestDistancePair([1, 3, 1], 1))  # 0
print(sol.smallestDistancePair([1, 1, 1], 2))  # 0
print(sol.smallestDistancePair([1, 6, 1], 3))  # 5
