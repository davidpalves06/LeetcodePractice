class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s),len(p)
        dp = {}
        def dfs(i,j):
            if j == n:
                dp[(i,j)] = i == m
                return dp[(i,j)]
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            match = i < m and (p[j] == '.' or s[i] == p[j]) 
            
            if (j + 1 < n) and p[j+1] == '*':
                dp[(i,j)] = (match and dfs(i+1,j)) or dfs(i,j+2)
                return dp[(i,j)]
            
            if match:
                dp[(i,j)] = dfs(i+1,j+1)
                return dp[(i,j)]
            
            dp[(i,j)] = False
            return dp[(i,j)]
        
        return dfs(0,0)
    
print(Solution.isMatch(None,s = "aa", p = "a"))
print(Solution.isMatch(None,s = "aa", p = "a*"))
print(Solution.isMatch(None,s = "ab", p = ".*"))
print(Solution.isMatch(None,s = "aab", p = "c*a*b"))
            
