from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        twoStairDown = 0
        oneStairDown = 0

        for i in range(2,len(cost)+1):
            oneStairDown,twoStairDown = min(oneStairDown + cost[i-1],twoStairDown + cost[i-2]), oneStairDown


        return oneStairDown
    
print(Solution.minCostClimbingStairs(None,[10,15,20]))