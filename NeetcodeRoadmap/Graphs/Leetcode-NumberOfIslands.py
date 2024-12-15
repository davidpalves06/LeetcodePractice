from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        res = 0

        def findIsland(i,j):
            if 0 > i or i >= len(grid) or 0 > j or len(grid[0]) <= j or (i,j) in visited or grid[i][j] == '0' :
                return
            
            visited.add((i,j))

            findIsland(i + 1,j)
            findIsland(i,j + 1)
            findIsland(i - 1,j)
            findIsland(i,j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in visited:
                    res += 1
                    findIsland(i,j)

        return res
    
print(Solution.numIslands(None,[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))