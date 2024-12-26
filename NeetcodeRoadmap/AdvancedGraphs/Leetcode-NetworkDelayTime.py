from collections import defaultdict, deque
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjList = defaultdict(list)

        for time in times:
            source,dest,weight = time
            adjList[source].append((dest,weight))

        visited = set()
        currentTime = 0
        minHeap = []
        heapq.heappush(minHeap,(0,k))

        while minHeap and len(visited) < n:
            time, dest = heapq.heappop(minHeap)
            if dest not in visited:
                visited.add(dest)
                for edge in adjList[dest]:
                    edgeDest,edgeWeight = edge
                    heapq.heappush(minHeap,(edgeWeight + time,edgeDest))

            currentTime = time

        if len(visited) != n:
            return -1

        return currentTime


print(Solution.networkDelayTime(None,[[1,2,1],[2,3,2]],3,1))