
# https://takeuforward.org/plus/dsa/problems/longest-subarray-with-sum-k

from typing import List

def getLongestSubarray(nums: List[int], k: int) -> int:
    prefix_sum_index = {}
    current_sum = 0
    max_len = 0

    for i, num in enumerate(nums):
        current_sum += num

        # Case 1: subarray from 0..i
        if current_sum == k:
            max_len = i + 1

        # Case 2: subarray found in between
        if (current_sum - k) in prefix_sum_index:
            max_len = max(max_len, i - prefix_sum_index[current_sum - k])

        # Store only the first occurrence
        if current_sum not in prefix_sum_index:
            prefix_sum_index[current_sum] = i

    return max_len

def getLongestSubarray2(nums: List[int], k: int) -> int:
    prefix_sum_index = {0: -1}  # seed
    current_sum = 0
    max_len = 0

    for i, num in enumerate(nums):
        current_sum += num

        if (current_sum - k) in prefix_sum_index:
            max_len = max(max_len, i - prefix_sum_index[current_sum - k])

        if current_sum not in prefix_sum_index:
            prefix_sum_index[current_sum] = i

    return max_len


print(getLongestSubarray([1, 2, 3, 7, 5], 12))
getLongestSubarray2([1, 2, 3, 1], 3)

