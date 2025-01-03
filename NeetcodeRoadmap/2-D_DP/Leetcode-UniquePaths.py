class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        dp[m-1][n-1] = 1
        
        def dfs(r,c):
            if r >= m or c >= n:
                return 0
            
            if dp[r][c]:
                return dp[r][c]
            
            dp[r][c] = dfs(r+1,c) + dfs(r,c+1)

            return dp[r][c]

        dfs(0,0)
    
        return dp[0][0]
    
print(Solution.uniquePaths(None,3,2))
print(Solution.uniquePaths(None,3,7))