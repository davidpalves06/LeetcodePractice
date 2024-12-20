class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1
        for i in range(len(s) - 1,-1,-1):
            if s[i] != '0':
                dp[i] += dp[i + 1]
            else:
                dp[i] = 0
            
            if i + 1 < len(s) and  (s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456')):
                dp[i] += dp[i + 2]

        print(dp)
        return dp[0]
    
print(Solution.numDecodings(None,"062312312"))