from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {i:[] for i in range(numCourses)}
        for prerequisite in prerequisites:
            courseMap[prerequisite[0]].append(prerequisite[1])
            
        visited = set()
        def checkForCycle(node):
            if node in visited:
                return True
            
            visited.add(node)

            for course in courseMap[node]:
                if checkForCycle(course):
                    return True
                
            visited.remove(node)

            courseMap[node] = []                        
            return False

        for i in range(numCourses):
            if checkForCycle(i):
                return False
            
        return True
    
print(Solution.canFinish(None,2,[[1,0],[0,1]]))