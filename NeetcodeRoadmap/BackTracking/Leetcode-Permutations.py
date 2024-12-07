from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        n = len(nums)

        isPicked = [False] * n

        def backtrack(cur,isPicked):
            if len(cur) == n:
                permutations.append(cur.copy())
                return
            for i in range(len(nums)):
                if not isPicked[i]:
                    cur.append(nums[i])
                    isPicked[i] = True
                    backtrack(cur,isPicked)
                    cur.pop()
                    isPicked[i] = False

        backtrack([],isPicked)
        return permutations
    
print(Solution.permute(None,[1,2,3]))