from collections import defaultdict
import heapq
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = [[] for _ in range(n)]

        for flight in flights:
            source,dest,cost = flight
            adjList[source].append((dest,cost))

        minHeap = []
        heapq.heappush(minHeap,(0,src,0))
        res = -1
        dist = [[float("INF")] * (k+2) for _ in range(n)]
        dist[src][0] = 0
        while minHeap :
            pathCost,dest,stops = heapq.heappop(minHeap)
            print(pathCost,dest,stops)
            if dest == dst:
                res = pathCost
                break
            if stops == k + 1 or dist[dest][stops] < pathCost:
                continue

            for edge in adjList[dest]:
                edgeDest,edgeCost = edge
                newCost = pathCost + edgeCost
                newStops = stops + 1
                if dist[edgeDest][newStops] > newCost:
                    dist[edgeDest][newStops] = newCost
                    heapq.heappush(minHeap,(newCost,edgeDest,newStops))

        return res

print(Solution.findCheapestPrice(None,4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],0,3,1))
print(Solution.findCheapestPrice(None,3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1))
print(Solution.findCheapestPrice(None,3,[[0,1,100],[1,2,100],[0,2,500]],0,2,0))
print(Solution.findCheapestPrice(None,4,[[0,1,1],[0,2,5],[1,2,1],[2,3,1]],0,3,1))