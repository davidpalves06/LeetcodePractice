class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp={}
        
        def dfs(i,j,k):
            if k == len(s3):
                return (i == len(s1) and j == len(s2))
            
            if (i,j,k) in dp:
                return dp[(i,j,k)]
            
            res = False

            if len(s1) > i and s1[i] == s3[k]:
                res = dfs(i + 1,j,k+1)
            
            if not res and len(s2) > j and s2[j] == s3[k]:
                res = dfs(i,j+1,k+1)

            dp[(i,j,k)] = res
            return res
        
        return dfs(0,0,0)
    
print(Solution.isInterleave(None,s1 = "aaaa", s2 = "bbbb", s3 = "aabbbbaa"))
print(Solution.isInterleave(None,s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))
print(Solution.isInterleave(None,s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"))