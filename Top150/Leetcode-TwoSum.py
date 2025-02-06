from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainDict = {}

        for i,num in enumerate(nums):
            if target-num in remainDict:
                return [remainDict[target-num],i]
            remainDict[num] = i

            
print(Solution.twoSum(None,nums = [2,7,11,15], target = 9))
print(Solution.twoSum(None,nums = [3,2,4], target = 6))
print(Solution.twoSum(None,nums = [3,3], target = 6))