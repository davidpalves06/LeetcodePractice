class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1

        reverse = int(str(abs(x))[::-1])

        if reverse > ((1 << 31) - 1) or reverse < -(1<< 31):
            return 0
        
        return reverse * sign

print(Solution.reverse(None,231))
print(Solution.reverse(None,1234))
print(Solution.reverse(None,-1234))
print(Solution.reverse(None,1234236467))