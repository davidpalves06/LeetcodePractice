import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.maxElems = k
        heapq.heapify(self.heap)
        while len(self.heap) > self.maxElems:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        if len(self.heap) > self.maxElems:
            heapq.heappop(self.heap)
        
        return self.heap[0]