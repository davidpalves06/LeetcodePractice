class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1),len(word2)

        dp = {}

        def dfs(i,j):
            if i == m:
                return n - j 
            if j == n:
                return m - i
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            if word1[i] == word2[j]:
                dp[(i,j)] = dfs(i+1,j+1)
                return dp[(i,j)]
            
            res = 1 + min(dfs(i+1,j),dfs(i,j+1),dfs(i+1,j+1))

            dp[(i,j)] = res
            return res
        return dfs(0,0)
         
    
print(Solution.minDistance(None,word1 = "horse", word2 = "ros"))
print(Solution.minDistance(None,word1 = "intention", word2 = "execution"))
print(Solution.minDistance(None,word1 = "neatcdee", word2 = "neetcode"))