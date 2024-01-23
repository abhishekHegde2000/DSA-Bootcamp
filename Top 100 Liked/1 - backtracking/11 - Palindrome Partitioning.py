'''
https://leetcode.com/problems/palindrome-partitioning/description/?envType=study-plan-v2&envId=top-100-liked

131. Palindrome Partitioning

Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.


'''

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Initialize result to store all partitions
        result = []
        # Initialize partition to store the current partition
        partition = []

        def dfs(start):
            # Print current state
            print(f"Start: {start}, Partition: {partition}, Result: {result}")

            # If start is equal to the length of s, append a copy of partition to result and return
            if start >= len(s):
                result.append(partition[:])
                return

            # Iterate over the indices end from start to the length of s
            for end in range(start, len(s)):
                # If the substring from start to end is a palindrome, append it to partition
                if self.isPalindrome(s, start, end):
                    partition.append(s[start: end + 1])
                    # Print current state
                    print(f"New Partition: {partition}")

                    # Recursively call dfs with end + 1
                    dfs(end + 1)

                    # Remove the last element from partition
                    partition.pop()

        # Call dfs with initial parameters
        dfs(0)
        # Return result
        return result

    def isPalindrome(self, s, start, end):
        # Check if the substring from start to end is a palindrome
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


sol = Solution()

print(sol.partition("aab"))
print(sol.partition("a"))
