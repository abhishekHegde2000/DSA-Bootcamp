'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

'''

from heapq import heappush, nlargest
from typing import List


from collections import Counter


class Solution:
    def topKFrequent(nums, k):
        # Create a frequency table
        frequency_table = Counter(nums)

        # Initialize a min heap
        min_heap = []

        # Push the frequency and element as a tuple into the min heap
        for num in frequency_table.keys():
            heappush(min_heap, (frequency_table[num], num))

        # Get the k most frequent elements from the min heap
        top_frequent_elements = nlargest(k, min_heap)

        # Initialize an empty list to store the k most frequent elements
        ans = []

        # Add the elements to the list
        for frequency, element in top_frequent_elements:
            ans.append(element)

        # Return the list of the k most frequent elements
        return ans


sol = Solution()
print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(sol.topKFrequent([1], 1))
