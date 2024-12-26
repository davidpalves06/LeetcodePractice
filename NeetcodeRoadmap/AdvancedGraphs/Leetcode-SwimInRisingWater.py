import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        minHeap = []
        minHeap.append((grid[0][0],0,0))
        n = len(grid)
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while minHeap:
            time,row,col = heapq.heappop(minHeap)

            if row == n - 1 and col == n - 1:
                return time
            
            for dr,dc in directions:
                neighbourRow = row + dr
                neighbourCol = col + dc

                if neighbourCol < 0 or neighbourCol == n or neighbourRow < 0 or neighbourRow == n or (neighbourRow,neighbourCol) in visited:
                    continue

                visited.add((neighbourRow,neighbourCol))

                heapq.heappush(minHeap,(max(time,grid[neighbourRow][neighbourCol]),neighbourRow,neighbourCol))

print(Solution.swimInWater(None,[[0,2],[1,3]]))
print(Solution.swimInWater(None,[[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))
print(Solution.swimInWater(None,[[0,1,2,10],[9,14,4,13],[12,3,8,15],[11,5,7,6]]))