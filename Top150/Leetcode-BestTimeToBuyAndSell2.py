from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lastPrice = prices[0]
        for price in prices:
            if price > lastPrice:
                res += (price - lastPrice)
            lastPrice = price
        return res

print(Solution.maxProfit(None,prices = [7,1,5,3,6,4])) # 7
print(Solution.maxProfit(None,prices = [1,2,3,4,5])) # 4
print(Solution.maxProfit(None,prices = [7,6,4,3,1])) # 0