class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m,n = len(num1),len(num2)
        if "0" in [num1, num2]:
            return "0"
        res = [0] * (m + n)
        num1,num2 = num1[::-1], num2[::-1]
        for i in range(m):
            for j in range(n):
                digit = int(num1[i]) * int(num2[j])
                res[i + j] += digit
                res[i + j + 1] += res[i + j] // 10
                res[i + j] = res[i + j] % 10

        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str, res[beg:])
        return "".join(res)


print(Solution.multiply(None,num1 = "3", num2 = "2"))
print(Solution.multiply(None,num1 = "0", num2 = "0"))