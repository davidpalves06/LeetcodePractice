import heapq
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        minHeap = []
        for interval in intervals:
            heapq.heappush(minHeap,interval)
        
        res = 0
        intervalToCompare = heapq.heappop(minHeap)
        while minHeap:
            newInterval = heapq.heappop(minHeap)
            if newInterval[0] < intervalToCompare[1]:
                res += 1
                intervalToCompare[1] = min(intervalToCompare[1],newInterval[1])
            else:
                intervalToCompare = newInterval

        return res
    
print(Solution.eraseOverlapIntervals(None,[[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]))