from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [[-1] * (amount + 1) for _ in range(len(coins))]

        def dfs(i,a):
            if a == 0:
                return 1
            if i >= len(coins):
                return 0
            
            if memo[i][a] != -1:
                return memo[i][a]

            res = dfs(i+1,a)
            if coins[i] <= a:
                res += dfs(i,a-coins[i])
            memo[i][a] = res
            return res
        
        return dfs(0,amount)
    
print(Solution.change(None,5,[1,2,5]))
print(Solution.change(None,4,[1,2,3]))
print(Solution.change(None,7,[2,4]))
print(Solution.change(None,7,[7]))
print(Solution.change(None,100,[99,1]))
        