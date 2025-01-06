from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)

        for i in range(1,n+1):
            bits = 1
            while bits <= i:
                if bits & i:
                    res[i] += 1
                bits = bits << 1

        return res
    
print(Solution.countBits(None,2))
print(Solution.countBits(None,5))
print(Solution.countBits(None,4))