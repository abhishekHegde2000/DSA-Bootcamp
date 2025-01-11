'''

https://leetcode.com/problems/course-schedule/

207. Course Schedule
Medium
Topics
Companies
Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

'''

from typing import List, Dict, Set, Deque
from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Initialize a graph with each course as a node and its prerequisites as edges
        courseGraph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            courseGraph[course].append(pre)
        print(f"Initial course graph: {courseGraph}")

        # Initialize a set to keep track of visited courses
        visitedCourses = set()
        print(f"Initial visited courses set: {visitedCourses}")

        # Define a depth-first search (DFS) function that takes a course as input
        def dfs(course):
            # If the course has been visited, return False
            if course in visitedCourses:
                return False
            print(f"Course {course} not in visitedCourses")

            # If the course has no prerequisites, return True
            if courseGraph[course] == []:
                return True
            print(f"Course {course} has prerequisites")

            # Mark the course as visited
            visitedCourses.add(course)
            print(f"Visited courses set after adding course {
                  course}: {visitedCourses}")

            # For each prerequisite of the course, call the DFS function on it. If the function returns False, return False
            for pre in courseGraph[course]:
                if not dfs(pre):
                    return False
            print(f"All prerequisites of course {course} can be taken")

            # Remove the course from the visited set and remove its prerequisites from the graph
            visitedCourses.remove(course)
            courseGraph[course] = []
            print(f"Visited courses set after removing course {
                  course}: {visitedCourses}")
            print(f"Course graph after removing prerequisites of course {
                  course}: {courseGraph}")

            # Return True
            return True

        # For each course, call the DFS function on it. If the function returns False, return False
        for course in range(numCourses):
            if not dfs(course):
                return False
            print(f"Course {course} can be finished")

        # Return True
        return True


# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         # Step 1: Build the adjacency list (courseGraph) and calculate indegrees
#         courseGraph = defaultdict(list)
#         indegree = [0] * numCourses

#         for course, prereq in prerequisites:
#             courseGraph[prereq].append(course)
#             indegree[course] += 1

#         # Step 2: Initialize a queue for BFS with courses having zero indegree
#         queue = deque([course for course in range(
#             numCourses) if indegree[course] == 0])

#         # Step 3: Perform BFS
#         while queue:
#             current = queue.popleft()
#             for neighbor in courseGraph[current]:
#                 indegree[neighbor] -= 1
#                 if indegree[neighbor] == 0:
#                     queue.append(neighbor)

#         # Step 4: Check if all courses have zero indegree (no cycles)
#         return all(indegree[course] == 0 for course in range(numCourses))


sol = Solution()

print(sol.canFinish(
    6, [[1, 0], [1, 2], [3, 1], [2, 3], [2, 4], [4, 5], [2, 5]]))  # False

print(sol.canFinish(6, [[1, 0], [1, 2], [3, 1],
      [3, 2], [2, 4], [4, 5], [2, 5]]))  # True
