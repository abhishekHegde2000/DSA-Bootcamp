'''
https://leetcode.com/problems/find-right-interval/

436. Find Right Interval

You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.

The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.

Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.

 

Example 1:

Input: intervals = [[1,2]]
Output: [-1]
Explanation: There is only one interval in the collection, so it outputs -1.
Example 2:

Input: intervals = [[3,4],[2,3],[1,2]]
Output: [-1,0,1]
Explanation: There is no right interval for [3,4].
The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.
Example 3:

Input: intervals = [[1,4],[2,3],[3,4]]
Output: [-1,2,-1]
Explanation: There is no right interval for [1,4] and [3,4].
The right interval for [2,3] is [3,4] since start2 = 3 is the smallest start that is >= end1 = 3.

'''

from typing import List
class Solution:
    def binary_search(self, sorted_intervals, target):
        left, right = 0, len(sorted_intervals) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            print(f"Mid: {mid}")
            if target == sorted_intervals[mid][0]:
                print(f"Target found at index: {sorted_intervals[mid][1]}")
                return sorted_intervals[mid][1]
            elif target < sorted_intervals[mid][0]:
                right = mid - 1
                result = sorted_intervals[mid][1]
                print(f"Target is less than mid, updating right to: {right} and result to: {result}")
            else:
                left = mid + 1
                print(f"Target is greater than mid, updating left to: {left}")
        print(f"Returning result: {result}")
        return result

    def findRightInterval(self, intervals):
        # Create a new list of intervals with their original indices
        indexed_intervals = [[intervals[i][0], i] for i in range(len(intervals))]
        print(f"Indexed intervals: {indexed_intervals}")
        # Sort the new list of intervals
        indexed_intervals.sort(key=lambda a: (a[0], a[1]))
        print(f"Sorted indexed intervals: {indexed_intervals}")
        # Initialize the result list
        result = [0] * len(intervals)
        # Perform a binary search for each interval in the original list
        for i in range(len(intervals)):
            result[i] = self.binary_search(indexed_intervals, intervals[i][1])
            print(f"Result after {i+1} iterations: {result}")
        return result

# Test cases
solution = Solution()


print(solution.findRightInterval([[1,2]]))  # [-1]
print(solution.findRightInterval([[3,4],[2,3],[1,2]]))  # [-1,0,1]
print(solution.findRightInterval([[1,4],[2,3],[3,4]]))  # [-1,2,-1]

