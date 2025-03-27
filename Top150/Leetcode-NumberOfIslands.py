from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m,n = len(grid), len(grid[0])

        def exploreIsland(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
                return
            
            grid[i][j] = "0"

            exploreIsland(i - 1,j)
            exploreIsland(i + 1,j)
            exploreIsland(i,j - 1)
            exploreIsland(i,j + 1)

        for i in range(m):
            for j in range(n):
                if (grid[i][j] == "1"):
                    res += 1
                    exploreIsland(i,j)

        return res