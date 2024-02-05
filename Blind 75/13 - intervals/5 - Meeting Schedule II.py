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
        # Initialize an empty list timePoints
        timePoints = []

        # For each meeting in the meetingsList
        for meeting in meetingsList:
            # Extract the start and end times of the meeting
            start, end = meeting.start, meeting.end
            print(f"Meeting start: {start}, end: {end}")

            # Append a tuple (start, 1) to timePoints to represent a meeting starting
            timePoints.append((start, 1))
            # Append a tuple (end, -1) to timePoints to represent a meeting ending
            timePoints.append((end, -1))

        print(f"Time points before sorting: {timePoints}")

        # Sort timePoints based on the time and then the value (1 or -1)
        timePoints.sort(key=lambda x: (x[0], x[1]))

        print(f"Time points after sorting: {timePoints}")

        # Initialize currentRooms and maxRooms to 0
        currentRooms = 0
        maxRooms = 0

        # For each timePoint in timePoints
        for timePoint in timePoints:
            # Add the value of timePoint to currentRooms
            currentRooms += timePoint[1]
            print(f"Current rooms: {currentRooms}")

            # Update maxRooms to be the maximum of maxRooms and currentRooms
            maxRooms = max(maxRooms, currentRooms)
            print(f"Max rooms: {maxRooms}")

        # Return maxRooms as the minimum number of meeting rooms required
        return maxRooms


print(Solution().minMeetingRooms([(0, 40), (5, 10), (15, 20)]))  # 2
print(Solution().minMeetingRooms([(4, 9)]))  # 1
print(Solution().minMeetingRooms([(0, 8), (8, 10)]))  # 1
print(Solution().minMeetingRooms([(0, 8), (8, 10), (10, 12)]))  # 2
print(Solution().minMeetingRooms([(0, 8), (8, 10), (10, 12), (12, 15)]))  # 2
