class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(0,32):
            res = res << 1
            power = pow(2,i)
            if power & n:
                res += 1

        return res
    
print(Solution.reverseBits(None,43261596))