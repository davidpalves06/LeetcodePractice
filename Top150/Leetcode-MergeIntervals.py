import heapq
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heapq.heapify(intervals)
        res = []
        interval = heapq.heappop(intervals)
        start = interval[0]
        end = interval[1]
        while intervals:
            interval = heapq.heappop(intervals)
            intervalStart = interval[0]
            if intervalStart <= end:
                end = max(end,interval[1])
            else:
                res.append([start,end])
                start = intervalStart
                end = interval[1]
            
        res.append([start,end])
        
        return res

print(Solution.merge(None,intervals = [[1,3],[2,6],[8,10],[15,18]]))
print(Solution.merge(None,intervals = [[1,3]]))

