class Solution:
    def intToRoman(self, num: int) -> str:
        digits = list(map(lambda x: int(x),str(num)))
        magnitudeDict = {
            1:["I","V","X"],
            10:["X","L","C"],
            100:["C","D","M"],
            1000:["M"]
        }
        magnitude = 1
        res = []
        for i in range(len(digits) - 1,-1,-1):
            digit = digits[i]
            magnitudeSymbols = magnitudeDict[magnitude]
            if digit == 4:
                res.append(magnitudeSymbols[1])
                res.append(magnitudeSymbols[0])
            elif digit == 9:
                res.append(magnitudeSymbols[2])
                res.append(magnitudeSymbols[0])
            elif digit >= 5:
                j = 5
                while j < digit:
                    res.append(magnitudeSymbols[0])
                    j += 1
                res.append(magnitudeSymbols[1])
            else:
                j = 0
                while j < digit:
                    res.append(magnitudeSymbols[0])
                    j += 1
            magnitude *= 10

        return "".join(res[::-1])


print(Solution.intToRoman(None, num = 4))
print(Solution.intToRoman(None, num = 3))
print(Solution.intToRoman(None, num = 7))
print(Solution.intToRoman(None, num = 9))
print(Solution.intToRoman(None, num = 10))
print(Solution.intToRoman(None, num = 40))
print(Solution.intToRoman(None, num = 49))
print(Solution.intToRoman(None, num = 99))
print(Solution.intToRoman(None, num = 3749))
print(Solution.intToRoman(None, num = 58))
print(Solution.intToRoman(None, num = 1994))