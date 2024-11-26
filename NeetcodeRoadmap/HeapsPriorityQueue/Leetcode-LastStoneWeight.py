import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first,second = heapq.heappop(stones),heapq.heappop(stones)

            new = first - second

            if new != 0:
                heapq.heappush(stones,new)

        stones.append(0)
        return abs(stones[0])