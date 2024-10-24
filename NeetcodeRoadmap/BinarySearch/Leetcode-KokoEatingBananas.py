import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right = 1,max(piles)
        res = 0
        while left <= right:
            pivot = left + ((right - left) // 2)
            currentHours = 0
            for pile in piles:
                currentHours += math.ceil(pile / pivot)
            if currentHours > h:
                left = pivot + 1
            else:
                right = pivot - 1
                res = pivot
        return res

print(Solution.minEatingSpeed(None,[30,11,23,4,20],6))