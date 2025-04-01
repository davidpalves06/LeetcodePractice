from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        added = set()
        res = []
        adjList = {i:[] for i in range(numCourses)}
        invalid = False
        for req in prerequisites:
            adjList[req[0]].append(req[1])

        def addCourse(num: int):
            requisites = adjList[num]
            nonlocal invalid
            if num in added:
                return
            if num in visited:
                invalid = True
                return
            visited.add(num)

            for course in requisites:
                addCourse(course)
            
            visited.remove(num)

            res.append(num)
            added.add(num)

            adjList[num] = []

        for num in range(numCourses):
            if num not in added:
                visited = set()
                addCourse(num)
                if invalid:
                    return []
                
        return res
            
print(Solution.findOrder(None,numCourses = 2, prerequisites = [[1,0]]))
print(Solution.findOrder(None,numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))
print(Solution.findOrder(None,numCourses = 1, prerequisites = []))
print(Solution.findOrder(None,numCourses = 3, prerequisites = [[0,1],[0,2],[1,2]]))