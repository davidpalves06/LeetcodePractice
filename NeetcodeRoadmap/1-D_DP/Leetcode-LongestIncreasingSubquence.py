from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    LIS[i] = max(LIS[i],1 + LIS[j]) 
        return max(LIS)

print(Solution.lengthOfLIS(None,[5,7,-24,12,13,2,3,12,5,6,35]))