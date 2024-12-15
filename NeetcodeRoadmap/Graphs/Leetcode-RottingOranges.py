from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        numberOfFreshOranges = 0
        time = 0

        def addRottenCell(x,y):
            nonlocal numberOfFreshOranges
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 0 and (x,y) not in visited:
                grid[x][y] = 2
                queue.append((x,y))
                visited.add((x,y))
                numberOfFreshOranges -= 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    visited.add((i,j))
                if grid[i][j] == 1:
                    numberOfFreshOranges += 1

        if numberOfFreshOranges == 0:
            return 0
        
        while queue:
            for i in range(len(queue)):
                x,y = queue.popleft()
                addRottenCell(x+1,y)
                addRottenCell(x-1,y)
                addRottenCell(x,y+1)
                addRottenCell(x,y-1)
            time += 1
        return time - 1 if numberOfFreshOranges == 0 else -1
    
print(Solution.orangesRotting(None,[[2,1,1],[0,1,1],[1,0,1]]))
            