from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if (2*sum(skill)) % len(skill) != 0:
            return -1
        
        target = (2*sum(skill)) // len(skill) 
        count = {}
        for number in skill:
            if number in count:
                count[number]+= 1
            else:
                count[number] = 1
        chemistry = 0
        for number in skill:
            if not count[number]:
                continue
            dif = target - number
            if dif not in count or not count[dif]:
                return -1
            
            chemistry += number*dif
            count[number]-=1
            count[dif] -= 1
        return chemistry
print(Solution.dividePlayers(None,[2,1,5,2]))
