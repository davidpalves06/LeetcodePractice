from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairList = [(p,s) for p,s in zip(position,speed)]
        
        car_fleets = 0
        current_Time = 0
        for (p,s) in sorted(pairList)[::-1]:
            destination_arrival = (target - p) / s
            if (destination_arrival > current_Time):
                car_fleets += 1
                current_Time = destination_arrival
        return car_fleets

print(Solution.carFleet(None,100,[0,2,4],[4,2,1]))