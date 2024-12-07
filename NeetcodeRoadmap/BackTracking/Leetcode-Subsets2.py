from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = set()

        def backtrack(i,cur):
            if i == len(nums):
                subsets.add(tuple(cur))
                return

            cur.append(nums[i])
            backtrack(i + 1,cur)

            cur.pop()
            backtrack(i + 1,cur)
        nums.sort()
        backtrack(0,[])
        return sorted(list(map(lambda x:list(x),subsets)))
    
    
print(Solution.subsetsWithDup(None,[1,2,2]))