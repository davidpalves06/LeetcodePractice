class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left,right = 0,len(s1) - 1
        counterS1 = {}
        counterS2 = {}

        for c in s1:
            counterS1[c] = 1 + counterS1.get(c,0)
        
        for i in range(right):
            counterS2[s2[i]] = 1 + counterS2.get(s2[i],0)

        while right < len(s2):
            counterS2[s2[right]] = 1 + counterS2.get(s2[right],0)
            if counterS1 == counterS2:
                return True
            else:
                counterS2[s2[left]] -= 1
                if counterS2[s2[left]] == 0:
                    counterS2.pop(s2[left])
                left+=1
                right+=1

        return False
    
print(Solution.checkInclusion(None,"ab","eidboaoo"))

