from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtrack(i,combination):
            if sum(combination) == target:
                combinations.append(combination.copy())
                return
            if i == len(candidates) or sum(combination) > target:
                return
            candidate = candidates[i]
            combination.append(candidate)
            backtrack(i,combination)

            combination.pop()
            
            backtrack(i + 1,combination)
        
        backtrack(0,[])

        return combinations
    
print(Solution.combinationSum(None,[2,3,6,7],7))

