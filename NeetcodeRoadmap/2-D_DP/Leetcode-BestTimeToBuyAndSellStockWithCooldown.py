from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        dp = [[0] * 2 for _ in range(len(prices) + 1)]

        for i in range(len(prices) - 1,-1,-1):
            cooldown = dp[i+1][True]
            # Buying

            buy = dp[i+1][False] - prices[i]

            dp[i][1] = max(buy,cooldown)

            # Selling

            cooldown = dp[i+1][False]
            sell = dp[i+2][True] + prices[i] if i + 2 < len(prices) else prices[i]

            dp[i][0] = max(sell,cooldown)

        return dp[0][1]
    
print(Solution.maxProfit(None,[1,3,4,0,4]))
print(Solution.maxProfit(None,[1,2,4]))
