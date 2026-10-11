"""
207. Course Schedule
https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai.

Return true if you can finish all courses. Otherwise, return false.

Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are 2 courses to take. To take course 1 you should have finished
    course 0. So it is possible.

Example 2:
    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are 2 courses to take. To take course 1 you should have finished
    course 0, and to take course 0 you should also have finished course 1. So it is
    impossible.

Constraints:
    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.
"""

from typing import List
from collections import defaultdict, deque

class Solution:
    """
    Yao's solution, has initialization bug
    """
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degrees = defaultdict(int) # has bug
        graph = defaultdict(list)

        for edge in prerequisites:
            a = edge[0]
            b = edge[1]
            in_degrees[a] += 1
            graph[b].append(a)

        sorted_list = []
        q = deque()
        # initiation step
        for k, cnt in in_degrees.items():
            if cnt == 0:
                q.append(k)

        while q:
            k = q.popleft()
            sorted_list.append(k)
            if k in graph:
                for e in graph[k]: # the end
                    in_degrees[e] -= 1
                    if in_degrees[e] == 0:
                        q.append(e)

        return len(sorted_list) == numCourses
    """
