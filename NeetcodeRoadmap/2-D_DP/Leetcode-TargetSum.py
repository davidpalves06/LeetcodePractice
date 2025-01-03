from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = 0

        memo = {}
        def dfs(i,total):
            nonlocal res
            if i == n:
                if total == target:
                    return 1
                return 0
            
            if (i,total) in memo:
                return memo[(i,total)]
            
            localRes = dfs(i+1,total - nums[i])
            localRes += dfs(i+1,total + nums[i])
            memo[(i,total)] = localRes

            return localRes
        
        return dfs(0,0)

print(Solution.findTargetSumWays(None,[1,1,1,1,1],3))
print(Solution.findTargetSumWays(None,[2,2,2],2))
print(Solution.findTargetSumWays(None,[47,23,38,38,3,37,18,29,27,39,29,25,4,2,0,47,10,39,23,17],15))
