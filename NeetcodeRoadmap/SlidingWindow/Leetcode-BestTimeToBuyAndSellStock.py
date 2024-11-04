from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rightMax = [0] * len(prices)
        currentMax = 0
        res = 0
        for i in range(len(prices) - 1,-1,-1):
            rightMax[i] = currentMax
            currentMax = max(currentMax,prices[i])

        for i in range(0,len(prices)):
            res = max(rightMax[i] - prices[i],res)
        
        return res
    
print(Solution.maxProfit(None,[7,1,5,3,6,4]))