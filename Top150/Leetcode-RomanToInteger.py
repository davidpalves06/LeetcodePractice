class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }

        lastChar = "I"
        res = 0
        for i in range(len(s) - 1,-1,-1):
            if romanDict[s[i]] < romanDict[lastChar]:
                res -= romanDict[s[i]]
            else:
                res += romanDict[s[i]]
            lastChar = s[i]
        return res
    
print(Solution.romanToInt(None,s = "III"))
print(Solution.romanToInt(None,s = "LVIII"))
print(Solution.romanToInt(None,s = "MCMXCIV"))