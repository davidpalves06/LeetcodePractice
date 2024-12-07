from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def isPali(s,l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
    
        def backTrack(i,j):
            if j >= len(s):
                if i == j:
                    res.append(part.copy())
                return
                
            if isPali(s,i,j):
                part.append(s[i:j+1])
                backTrack(j+1,j+1)
                part.pop()
            
            backTrack(i,j+1)

        backTrack(0,0)

        return res
    
print(Solution.partition(None,"aab"))