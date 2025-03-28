import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points:
            dist = (x ** 2) + (y ** 2)
            heap.append((dist,x,y))

        heapq.heapify(heap)

        res = []
        for _ in range(k):
            closest = heapq.heappop(heap)
            res.append([closest[1],closest[2]])

        return res