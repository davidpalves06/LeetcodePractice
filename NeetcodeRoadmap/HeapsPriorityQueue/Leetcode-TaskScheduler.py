from collections import deque
import heapq
from typing import Counter, List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        queue = deque()

        maxHeap = [-count for count in counter.values()]
        heapq.heapify(maxHeap)
        time = 0

        while maxHeap or queue:
            if maxHeap:
                updatedCount = 1 + heapq.heappop(maxHeap)
                if updatedCount:
                    queue.append((updatedCount,time + n))

            if queue:
                if queue[0][1] == time:
                    heapq.heappush(maxHeap,queue.popleft()[0])

            time += 1
        return time