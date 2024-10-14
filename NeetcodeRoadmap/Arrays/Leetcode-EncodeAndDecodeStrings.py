from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for word in strs:
            res += word + 'ä'
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        currentWord = ""
        for c in s:
            if (c == 'ä'):
                res.append(currentWord)
                currentWord = ""
            else:
                currentWord += c
        return res
    
print(Solution.encode(None,["neet","code","love","you"]))
print(Solution.decode(None,"neetäcodeäloveäyouä"))
