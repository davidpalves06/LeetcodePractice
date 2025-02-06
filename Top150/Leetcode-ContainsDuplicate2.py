from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexDict = {}

        for i,num in enumerate(nums):
            if num in indexDict and i - indexDict[num] <= k:
                return True

            indexDict[num] = i

        return False
    
print(Solution.containsNearbyDuplicate(None,nums = [1,2,3,1], k = 3))
print(Solution.containsNearbyDuplicate(None,nums = [1,0,1,1], k = 1))
print(Solution.containsNearbyDuplicate(None,nums = [1,2,3,1,2,3], k = 2))