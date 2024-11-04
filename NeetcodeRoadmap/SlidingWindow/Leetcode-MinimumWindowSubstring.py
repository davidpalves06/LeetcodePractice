class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        counterT = {}
        counterS = {}

        resIndex = None
                
        for c in t:
            counterT[c] = 1 + counterT.get(c,0)

        have,need = 0,len(counterT)

        for right in range(len(s)):
            c = s[right]
            counterS[c] = 1 + counterS.get(c,0)

            if counterS.get(c) == counterT.get(c,0):
                have += 1

            while have == need:
                if not resIndex or resIndex[1] - resIndex[0] > right + 1 - left:
                    resIndex = (left,right + 1)
                counterS[s[left]] -= 1
                if counterS.get(s[left]) < counterT.get(s[left],0):
                    have -= 1
                left += 1

        if not resIndex:
            return ""
        return s[resIndex[0]:resIndex[1]]
    
print(Solution.minWindow(None,"AA","AA"))
            