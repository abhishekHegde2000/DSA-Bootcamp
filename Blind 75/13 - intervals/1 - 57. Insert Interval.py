'''
https://leetcode.com/problems/insert-interval/description/

57. Insert Interval

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
'''

from typing import List
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        # Initialize an empty list to store the final intervals after insertion
        result_intervals = []

        for index in range(len(intervals)):
            # Print the current state of variables for debugging
            print(f"Current interval: {intervals[index]}, New interval: {
                  new_interval}, Result intervals: {result_intervals}")

            # If the end of new_interval is less than the start of the current interval
            if new_interval[1] < intervals[index][0]:
                result_intervals.append(new_interval)
                print(f"New interval inserted before current interval: {
                      result_intervals}")
                return result_intervals + intervals[index:]

            # If the start of new_interval is greater than the end of the current interval
            elif new_interval[0] > intervals[index][1]:
                result_intervals.append(intervals[index])
                print(f"Current interval added to result intervals: {
                      result_intervals}")

            # If the new_interval overlaps with the current interval
            else:
                new_interval[0] = min(new_interval[0], intervals[index][0])
                new_interval[1] = max(new_interval[1], intervals[index][1])
                print(f"New interval updated due to overlap: {new_interval}")

        # Append the new_interval to result_intervals after the loop
        result_intervals.append(new_interval)
        print(f"New interval added to result intervals after loop: {
              result_intervals}")

        return result_intervals


sol = Solution()

print(sol.insert([[1, 3], [6, 9]], [2, 5]))  # [[1,5],[6,9]]
# [[1,2],[3,10],[12,16]]
print(sol.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
print(sol.insert([], [5, 7]))  # [[5,7]]
