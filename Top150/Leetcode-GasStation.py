from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        tank = 0
        for i in range(len(gas)):
            if tank < 0:
                start = i
                tank = gas[i] - cost[i]
            else:
                tank += (gas[i] - cost[i])

        return start
    
print(Solution.canCompleteCircuit(None,gas = [1,2,3,4,5], cost = [3,4,5,1,2]))
print(Solution.canCompleteCircuit(None,gas = [2,3,4], cost = [3,4,3]))