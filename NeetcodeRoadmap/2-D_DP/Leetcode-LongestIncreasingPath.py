from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        maxRes = 0
        def dfs(i,j,prev):
            nonlocal maxRes
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            
            
            if matrix[i][j] > prev:
                if dp[i][j] != 0:
                    return dp[i][j]
                res = 1 + max(dfs(i+1,j,matrix[i][j]),dfs(i-1,j,matrix[i][j]),dfs(i,j+1,matrix[i][j]),dfs(i,j-1,matrix[i][j]))
                if res > dp[i][j]:
                    dp[i][j] = res
                maxRes = max(maxRes,res)
                return res
            else:
                return 0

        for i in range(m):
            for j in range(n):
                dfs(i,j,-1)

        return maxRes
    
print(Solution.longestIncreasingPath(None,matrix = [[9,9,4],[6,6,8],[2,1,1]]))
print(Solution.longestIncreasingPath(None,matrix = [[3,4,5],[3,2,6],[2,2,1]]))
print(Solution.longestIncreasingPath(None,matrix = [[1]]))
print(Solution.longestIncreasingPath(None,[[1,2,3],[2,1,4],[7,6,5]]))