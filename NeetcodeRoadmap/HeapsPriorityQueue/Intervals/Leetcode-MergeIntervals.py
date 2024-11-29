import heapq
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        minHeap = []
        for interval in intervals:
            heapq.heappush(minHeap,interval)

        res = []
        intervalToAdd = heapq.heappop(minHeap)
        while minHeap:
            intervalToCompare = heapq.heappop(minHeap)

            if intervalToCompare[0] > intervalToAdd[1]:
                res.append(intervalToAdd)
                intervalToAdd = intervalToCompare
            else:
                intervalToAdd[1] = max(intervalToAdd[1],intervalToCompare[1])
        
        res.append(intervalToAdd)
        return res