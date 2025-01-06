class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 1
        res = 0
        while bits <= n:
            if bits & n:
                res += 1
            bits = bits << 1
        return res
    
print(Solution.hammingWeight(None,11))
print(Solution.hammingWeight(None,128))
print(Solution.hammingWeight(None,2147483645))