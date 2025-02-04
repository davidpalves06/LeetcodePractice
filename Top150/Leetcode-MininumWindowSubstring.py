from collections import defaultdict
from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left,right = 0,0
        tCounter = Counter(t)
        sCounter = defaultdict(int)

        minLength = len(s) + 1
        res = ""
        while right < len(s):
            rightLetter = s[right]
            if rightLetter in tCounter:
                sCounter[rightLetter] += 1

            if self.checkIfIsSubstring(sCounter,tCounter):
                while s[left] not in tCounter or sCounter[s[left]] > tCounter[s[left]]:
                    sCounter[s[left]] -= 1
                    left += 1
                if right - left + 1 < minLength:
                    res = s[left:right + 1]
                    minLength = right - left + 1
                sCounter[s[left]] -= 1
                left += 1
            right += 1

        return res
    
    def checkIfIsSubstring(self,sCounter: defaultdict,tCounter: Counter) -> bool:
        for key in tCounter.keys():
            if sCounter[key] < tCounter[key]:
                return False
            
        return True
    
print(Solution.minWindow(Solution(),s = "aaaaaaaaaaaabbbbbcdd", t = "abcdd"))
print(Solution.minWindow(Solution(),s = "ADOBECODEBANC", t = "ABC"))
print(Solution.minWindow(Solution(),s = "a", t = "a"))
print(Solution.minWindow(Solution(),s = "a", t = "aa"))