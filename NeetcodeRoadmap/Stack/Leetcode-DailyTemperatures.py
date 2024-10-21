from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i,temp in enumerate(temperatures):
            if not stack:
                stack.append((temp,i))
                continue
            while stack  and stack[-1][0] < temp:
                index = stack.pop()[1]
                res[index] = i - index
            else:
                stack.append((temp,i))
        return res
    
print(Solution.dailyTemperatures(None,[73,74,75,71,69,72,76,73]))