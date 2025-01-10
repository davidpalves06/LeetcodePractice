class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        steps = abs(n)

        def helper(num,power):
            if num == 0:
                return 0
            if power == 0:
                return 1
            res = helper(num * num,power//2)
            return res*num if power%2 else res

        res = helper(x,abs(n))
        return res if n >= 0 else 1/res
    
print(Solution.myPow(None,x = 2.00000, n = 10))
print(Solution.myPow(None,x = 2.10000, n = 3))
print(Solution.myPow(None,x = 2.00000, n = -2))
print(Solution.myPow(None,x = 3.00000, n = 4))