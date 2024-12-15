from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(i,j):
            queue = deque()
            visited = set()
            queue.append((i,j))
            visited.add((i,j))
            reachedPacific,reachedAtlantic = False,False

            def addCell(i,j,height):
                nonlocal reachedPacific
                nonlocal reachedAtlantic
                if i < 0 or j < 0:
                    reachedPacific = True
                    return
                if i >= len(heights) or j >= len(heights[0]):
                    reachedAtlantic = True
                    return
                
                if heights[i][j] <= height and (i,j) not in visited:
                    queue.append((i,j))
                    visited.add((i,j))

            while queue:
                for i in range((len(queue))):
                    x,y = queue.popleft()
                    height = heights[x][y]
                    addCell(x+1,y,height)
                    addCell(x-1,y,height)
                    addCell(x,y+1,height)
                    addCell(x,y-1,height)
                if reachedAtlantic and reachedPacific:
                    return True
            return False

        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                res.append([i,j]) if bfs(i,j) else res

        return res
    
print(Solution.pacificAtlantic(None,[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))