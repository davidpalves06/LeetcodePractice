from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        currMax = 0
        for i in range(len(prices) - 1,-1,-1):
            currMax = max(currMax,prices[i])
            res = max(res,currMax - prices[i])
        
        return res

print(Solution.maxProfit(None,prices = [7,1,5,3,6,4]))
print(Solution.maxProfit(None,prices = [7,6,4,3,1]))