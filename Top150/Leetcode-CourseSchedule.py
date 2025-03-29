from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}
        visited = set()
        for prereq in prerequisites:
            course1,course2 = prereq
            if course1 in adjList:
                adjList[course1].append(course2)
            else:
                adjList[course1] = [course2]

        def checkForCycle(num):
            if num in visited:
                return False
            
            visited.add(num)
            res = True
            for neighbour in adjList[num]:
                res = res and checkForCycle(neighbour)

            visited.remove(num)

            adjList[num] = []
            return res

        for num in range(numCourses):
            if (not checkForCycle(num)):
                return False
        return True

print(Solution.canFinish(None,numCourses = 2, prerequisites = [[1,0]]))
print(Solution.canFinish(None,numCourses = 2, prerequisites = [[1,0],[0,1]]))
print(Solution.canFinish(None,numCourses = 5, prerequisites = [[1,4],[2,4],[3,1],[3,2]]))
