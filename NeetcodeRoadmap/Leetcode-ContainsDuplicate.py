from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exists = dict()
        for num in nums:
            if num in exists:
                return True
            exists.setdefault(num)
        return False
    
print(Solution.hasDuplicate(None,[1, 2, 3, 3]))