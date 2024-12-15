from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        def calculateIslandArea(i,j):
            if 0 > i or i >= len(grid) or 0 > j or len(grid[0]) <= j or grid[i][j] == 0 :
                return 0
            
            grid[i][j] = 0

            return 1 + calculateIslandArea(i+1,j) + calculateIslandArea(i,j+1) + calculateIslandArea(i-1,j) + calculateIslandArea(i,j-1)
             
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res,calculateIslandArea(i,j))

        return res
    
print(Solution.maxAreaOfIsland(None,[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))