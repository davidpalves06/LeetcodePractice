from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        frequencies = [0] * k
        for number in arr:
            frequencies[number%k]+= 1

        for i in range(k):
            if (i == 0):
                if (frequencies[i] % 2 != 0):
                    return False
                else: continue
            if (frequencies[i] != frequencies[k-i]):
                return False
        return True

print(Solution.canArrange(None,[1,2,3,4,5,6],10))
