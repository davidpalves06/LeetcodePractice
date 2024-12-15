from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        visited = set()
        queue = deque()


        def addCellToQueue(i,j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != -1 and (i,j) not in visited:
                visited.add((i,j))
                queue.append((i,j))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    visited.add((i,j))
                    queue.append((i,j))

        dist = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                grid[r][c] = dist
                addCellToQueue(r+1,c)
                addCellToQueue(r-1,c)
                addCellToQueue(r,c+1)
                addCellToQueue(r,c-1)
            dist += 1


        print(grid)

Solution.islandsAndTreasure(None,[[2147483647,2147483647,2147483647],
                                  [2147483647,-1,2147483647],
                                  [0,2147483647,2147483647]])

Output: [[2,3,4],[1,-1,3],[0,1,2]]