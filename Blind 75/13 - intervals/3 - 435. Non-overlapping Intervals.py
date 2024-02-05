'''
https://leetcode.com/problems/non-overlapping-intervals/

435. Non-overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104


'''

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort the intervals list based on the start of each interval
        intervals.sort(key=lambda interval: interval[0])
        print(f"Sorted intervals: {intervals}")

        # Initialize a variable to count the number of intervals to remove
        remove_count = 0
        # Initialize a variable with the end of the first interval from the sorted intervals list
        previous_end = intervals[0][1]

        for current_interval in intervals[1:]:
            print(f"Current interval: {current_interval}, Remove count: {
                  remove_count}, Previous end: {previous_end}")

            # If the start of the current interval is greater than or equal to previous_end
            if current_interval[0] >= previous_end:
                # Update previous_end to be the end of the current interval
                previous_end = current_interval[1]
                print(f"Previous end updated: {previous_end}")

            # If the start of the current interval is less than previous_end
            else:
                # Increment remove_count by 1
                remove_count += 1
                # Update previous_end to be the minimum of previous_end and the end of the current interval
                previous_end = min(previous_end, current_interval[1])
                print(f"Remove count incremented: {
                      remove_count}, Previous end updated: {previous_end}")

        return remove_count


sol = Solution()

print(sol.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))  # 1
print(sol.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))  # 2
print(sol.eraseOverlapIntervals([[1, 2], [2, 3]]))  # 0
print(sol.eraseOverlapIntervals([[1, 100], [11, 22], [1, 11], [2, 12]]))  # 2
