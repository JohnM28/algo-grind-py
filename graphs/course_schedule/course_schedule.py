"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

"""
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Time complexity: O(V + E) where V is the number of courses and E is the number of prerequisites
        -1: traversing
        0: not visited
        1: completed
        """
        course_graph = {i: [] for i in range(numCourses)}
        status = [0] * numCourses
        for u, v in prerequisites:
            course_graph[u].append(v)
        for i in range(numCourses):
            if not self._traverse_and_find(i, course_graph, status):
                return False
        return True

    def _traverse_and_find(self, course, course_graph, status) -> bool:
        if status[course] == -1:
            return False
        if status[course] == 1:
            return True
        status[course] = -1
        for preq in course_graph[course]:
            if course_graph.get(preq):
                if not self._traverse_and_find(preq, course_graph, status):
                    return False
        status[course] = 1
        return True



if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
        (3, [[1, 0], [2, 1]], True),
        (3, [[1, 0], [2, 1], [0, 2]], False),
        (3, [[1, 0], [2, 1], [0, 2], [1, 2]], False),
        (3, [[1, 0], [2, 1], [0, 2], [2, 0]], False),
        (4, [[1, 0], [2, 1], [3, 2]], True),
        (4, [[1, 0], [2, 1], [3, 2], [0, 3]], False)
    ]

    for numCourses, prerequisites, expected in test_cases:
        result = solution.canFinish(numCourses, prerequisites)
        print(f"canFinish({numCourses}, {prerequisites}) = {result}, expected = {expected}")














    #     graph = {i: [] for i in range(numCourses)}
    #     for course, prereq in prerequisites:
    #         graph[course].append(prereq)
    #
    #     visited = [0] * numCourses
    #     for i in range(numCourses):
    #         if not self.dfs(graph, visited, i):
    #             return False
    #     return True
    #
    # def dfs(self, graph, visited, i):
    #     if visited[i] == 1:
    #         return False
    #     if visited[i] == 2:
    #         return True
    #     visited[i] = 1
    #     for j in graph[i]:
    #         if not self.dfs(graph, visited, j):
    #             return False
    #     visited[i] = 2
    #     return True


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
        (3, [[1, 0], [2, 1]], True),
        (3, [[1, 0], [2, 1], [0, 2]], False),
        (3, [[1, 0], [2, 1], [0, 2], [1, 2]], False),
        (3, [[1, 0], [2, 1], [0, 2], [2, 0]], False)
    ]
    for numCourses, prerequisites, expected in test_cases:
        result = solution.canFinish(numCourses, prerequisites)
        print(f"canFinish({numCourses}, {prerequisites}) = {result}, expected = {expected}")