from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = 0
        points.sort(key=lambda x:x[1])
        end = float('-inf')
        for point in points:
            if point[0] > end:
                res += 1
                end = point[1]
        return res
    
print(Solution.findMinArrowShots(None,points = [[10,16],[2,8],[1,6],[7,12]]))
print(Solution.findMinArrowShots(None,points = [[1,2],[3,4],[5,6],[7,8]]))
print(Solution.findMinArrowShots(None,points = [[1,2],[2,3],[3,4],[4,5]]))
print(Solution.findMinArrowShots(None,points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))