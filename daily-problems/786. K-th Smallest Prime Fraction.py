'''

https://leetcode.com/problems/k-th-smallest-prime-fraction/


786. K-th Smallest Prime Fraction

You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

 

Example 1:

Input: arr = [1,2,3,5], k = 3
Output: [2,5]
Explanation: The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
The third fraction is 2/5.
Example 2:

Input: arr = [1,7], k = 1
Output: [1,7]
 

Constraints:

2 <= arr.length <= 1000
1 <= arr[i] <= 3 * 104
arr[0] == 1
arr[i] is a prime number for i > 0.
All the numbers of arr are unique and sorted in strictly increasing order.
1 <= k <= arr.length * (arr.length - 1) / 2
 

Follow up: Can you solve the problem with better than O(n2) complexity?
'''
from heapq import heappush, heappop
from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        n = len(arr)
        left, right = 0, 1.0

        # Binary search for finding the kth smallest prime fraction
        while left < right:
            # Calculate the middle value
            mid = (left + right) / 2
            # Initialize variables to keep track of maximum fraction and indices
            max_fraction = 0.0
            total_smaller_fractions = 0
            numerator_idx, denominator_idx = 0, 0
            j = 1

            # Iterate through the array to find fractions smaller than mid
            for i in range(n - 1):
                while j < n and arr[i] >= mid * arr[j]:
                    j += 1

                # Count smaller fractions
                total_smaller_fractions += (n - j)

                # If we have exhausted the array, break
                if j == n:
                    break

                # Calculate the fraction
                fraction = arr[i] / arr[j]

                # Update max_fraction and indices if necessary
                if fraction > max_fraction:
                    numerator_idx = i
                    denominator_idx = j
                    max_fraction = fraction

            # Check if we have found the kth smallest prime fraction
            if total_smaller_fractions == k:
                return [arr[numerator_idx], arr[denominator_idx]]
            elif total_smaller_fractions > k:
                right = mid  # Adjust the range for binary search
            else:
                left = mid  # Adjust the range for binary search

        return []  # Return empty list if kth smallest prime fraction not found


class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        # Initialize the min heap
        fraction_heap = []
        print(f"Initial fraction_heap: {fraction_heap}")

        # Get the length of the array
        arr_length = len(arr)
        print(f"arr_length: {arr_length}")

        # For each pair of elements in arr (with the second element greater than the first), push the pair and their fraction into fraction_heap
        for i in range(arr_length):
            for j in range(i + 1, arr_length):
                heappush(fraction_heap, (arr[i] / arr[j], (arr[i], arr[j])))
                print(
                    f"Pushed ({arr[i] / arr[j]}, ({arr[i]}, {arr[j]})) into fraction_heap")

        # Pop the heap k times to get the k-th smallest fraction
        for _ in range(k):
            fraction, elements = heappop(fraction_heap)
            print(f"Popped ({fraction}, {elements}) from fraction_heap")

        # Return the pair of elements that make up the k-th smallest fraction
        return list(elements)


'''
                (0.2, (...))
               /             \
      (0.4, (...))   (0.3333333333333333, (...))
     /      \       /
(0.5, (...)) (0.6, (...)) (0.6666666666666666, (...))
'''

sol = Solution()

print(sol.kthSmallestPrimeFraction([1, 2, 3, 5], 3))  # [2, 5]
print(sol.kthSmallestPrimeFraction([1, 7], 1))  # [1, 7]
print(sol.kthSmallestPrimeFraction([1, 2, 3, 5], 1))  # [1, 5]
print(sol.kthSmallestPrimeFraction([1, 2, 3, 5], 2))  # [1, 3]
