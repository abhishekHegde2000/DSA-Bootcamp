'''
https://neetcode.io/problems/meeting-schedule-ii

1229. Meeting Scheduler II

Meeting Schedule II
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2

Explanation:
day1: (0,40)
day2: (5,10),(15,20)
Example 2:

Input: intervals = [(4,9)]

Output: 1
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


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, meetingsList: List[Interval]) -> int:
        start = [i.start for i in meetingsList]
        end = [i.end for i in meetingsList]

        start.sort()
        end.sort()

        res, count = 0, 0
        s, e = 0, 0

        while s < len(start):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)

        return res


print(Solution().minMeetingRooms([(0, 40), (5, 10), (15, 20)]))  # 2
print(Solution().minMeetingRooms([(4, 9)]))  # 1
print(Solution().minMeetingRooms([(0, 8), (8, 10)]))  # 1
print(Solution().minMeetingRooms([(0, 8), (8, 10), (10, 12)]))  # 2
print(Solution().minMeetingRooms([(0, 8), (8, 10), (10, 12), (12, 15)]))  # 2
