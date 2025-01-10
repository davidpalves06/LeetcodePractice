from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits == []:
            return [1]
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            digits[-1] = 0
            newList = self.plusOne(digits[:-1])
            newList.append(digits[-1])
            return newList
        
print(Solution.plusOne(Solution(),digits = [1,2,3]))
print(Solution.plusOne(Solution(),digits = [4,3,2,1]))
print(Solution.plusOne(Solution(),digits = [9]))