'''
https://leetcode.com/problems/partition-labels/description/?envType=study-plan-v2&envId=top-100-liked

763. Partition Labels

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.

'''

from typing import List


class Solution:
    def partitionLabels(self, input_string: str) -> List[int]:
        # Initialize an empty dictionary to store the last occurrence of each character
        last_occurrence_map = {}

        # Iterate over each character and its index in input_string
        for index, char in enumerate(input_string):
            # Update last_occurrence_map with the last occurrence of each character
            last_occurrence_map[char] = index
            print(f"Updated last_occurrence_map: {last_occurrence_map}")

        # Initialize start and end to 0
        start = 0
        end = 0
        print(f"Initial start: {start}, end: {end}")

        # Initialize an empty list to store the lengths of the partitions
        partitions = []

        # Iterate over each character and its index in input_string
        for index, char in enumerate(input_string):
            # If the last occurrence of the current character is greater than end, update end
            if end < last_occurrence_map[char]:
                end = last_occurrence_map[char]
                print(f"Updated end: {end}")

            # If the current index is equal to end, append the length of the current partition to partitions and update start
            if index == end:
                partitions.append(end - start + 1)
                print(f"Added {end - start +
                      1} to partitions. New partitions: {partitions}")
                start = end + 1
                print(f"Updated start: {start}")

        # Return the lengths of the partitions
        return partitions


sol = Solution()

print(sol.partitionLabels("ababcbacadefegdehijhklij"))  # [9,7,8]
print(sol.partitionLabels("eccbbbbdec"))  # [10]
