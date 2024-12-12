from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = {i:[] for i in range(numCourses)}

        res = []
        visited = set()
        added = set()
        hasCycle = False
        for prerequisite in prerequisites:
            courseMap[prerequisite[0]].append(prerequisite[1])

        def addCourseToResult(i):
            nonlocal hasCycle
            if i in added:
                return
            if i in visited:
                hasCycle = True
                return
            visited.add(i)
            preCourses = courseMap[i]
            for course in preCourses:
                addCourseToResult(course)
            res.append(i)
            added.add(i)

        for i in range(numCourses):
            if i not in added:
                addCourseToResult(i)
            if hasCycle:
                return []
        
        return res



print(Solution.findOrder(None,3, [[0,1],[1,2],[2,0]]))
