from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)

        for i in range(amount + 1):
            if i == 0:
                dp[i] = 0
                continue
            for coin in coins:
                if coin == i:
                    dp[i] = 1
                elif coin < i:
                    dp[i] = min(1 + dp[i-coin],dp[i])
                else:
                    continue
                    
        return dp[-1] if dp[-1] != amount + 1 else -1

    
print(Solution.coinChange(None,[1],0))