from collections import defaultdict
import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = defaultdict(list)

        for i in range(len(points)):
            for j in range(i + 1,len(points)):
                point0 = tuple(points[i])
                point1 = tuple(points[j])

                adjList[point0].append(point1)
                adjList[point1].append(point0)

        minHeap = []
        added = set()
        curr = tuple(points[0])
        added.add(curr)
        res = 0

        while len(added) != len(points):
            for point in adjList[curr]:
                weight = abs(point[0] - curr[0]) + abs(point[1] - curr[1])
                heapq.heappush(minHeap,(weight,point))

            while minHeap:
                (weight,pointToAdd) = heapq.heappop(minHeap)
                if pointToAdd not in added:
                    res += weight
                    added.add(pointToAdd)
                    curr = pointToAdd
                    break 

        return res
    
print(Solution.minCostConnectPoints(None,[[3,12],[-2,5],[-4,1]]))


        