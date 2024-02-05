'''
https://neetcode.io/problems/meeting-schedule

1229. Meeting Scheduler


Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

Example 1:

Input: intervals = [(0,30),(5,10),(15,20)]

Output: false

Explanation:
(0,30),(5,10) and (0,30),(15,20) will conflict
Example 2:

Input: intervals = [(5,8),(9,15)]

Output: true
Note:

(0,8),(8,10) is not considered a conflict at 8
Constraints:

0 <= intervals.length <= 100
0 <= intervals[i].start < intervals[i].end <= 1000
Accepted: 916  |  Submitted: 3839  |  Acceptance Rate: 24%
'''

from typing import List


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort based on start value
        intervals.sort(key=lambda interval: interval.start)
        print(f"intervals = {intervals}")

        for i in range(1, len(intervals)):

            i1 = intervals[i-1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False

        return True


sol = Solution()
print(sol.canAttendMeetings([(0, 30), (5, 10), (15, 20)]))  # False
print(sol.canAttendMeetings([(5, 8), (9, 15)]))  # True
