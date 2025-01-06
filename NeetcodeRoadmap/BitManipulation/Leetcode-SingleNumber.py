from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = nums[0]
        for i in range(1,len(nums)):
            xor ^= nums[i]

        return xor
    
print(Solution.singleNumber(None,nums = [2,2,1]))
print(Solution.singleNumber(None,nums = [4,1,2,1,2]))
print(Solution.singleNumber(None,nums = [1]))
